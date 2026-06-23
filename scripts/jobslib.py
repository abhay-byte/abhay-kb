#!/usr/bin/env python3
"""jobslib.py — Shared library for job listing automation.

Used by sync-jobs.py and verify-jobs.py.
Handles: data load/save, markdown rendering, dedup, expiry, scraping.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.parse import urlparse

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(REPO_DIR, "_data", "jobs.json")
JOBS_MD = os.path.join(REPO_DIR, "jobs.md")
SOURCE_DIR = os.path.join(REPO_DIR, "source")
MAX_AGE_DAYS = 28
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"

CATEGORY_LABELS = {
    "software-engineering": "🟢 Software Engineering",
    "internships": "💼 Internships",
    "game-development": "🎮 Game Development"
}
CATEGORY_ORDER = ["software-engineering", "internships", "game-development"]

DATE_FORMATS = ["%d-%b-%Y", "%B %d, %Y", "%d %B %Y"]

SCRAPE_PAGES = 2  # How many pages to scrape from each aggregator


# ── Helpers ───────────────────────────────────────────────────────────────

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "jobs": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def dedup_jobs(jobs):
    seen = set()
    unique = []
    for job in jobs:
        url = job.get("url", "").strip()
        if url and url not in seen:
            seen.add(url)
            unique.append(job)
    return unique


def filter_expired(jobs):
    now = datetime.now(timezone.utc)
    fresh = []
    removed = []
    for job in jobs:
        posted_str = job.get("posted", "")
        posted_dt = parse_date(posted_str)
        if posted_dt and (now - posted_dt).days > MAX_AGE_DAYS:
            removed.append(job)
        else:
            fresh.append(job)
    return fresh, removed


def parse_date(date_str):
    if not date_str:
        return None
    for fmt in ["%d-%b-%Y", "%B %d, %Y", "%d %B %Y"]:
        try:
            return datetime.strptime(date_str.strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip().strip("-–:;,.").strip()
    # Decode HTML entities
    text = text.replace('&#8211;', '-').replace('&amp;', '&').replace('&#038;', '&')
    text = text.replace('&#8217;', "'").replace('&rsquo;', "'").replace('&lsquo;', "'")
    text = text.replace('&nbsp;', ' ').replace('&#47;', '/')
    return text.strip()


# ── HTTP ──────────────────────────────────────────────────────────────────

def fetch_url(url, timeout=15):
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return None


def check_url_alive(url, timeout=10):
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.getcode() < 400
    except Exception:
        return False


# ── Scraping: Listing pages ───────────────────────────────────────────────

def _fetch_page_with_pagination(base_url, page=1):
    """Fetch a paginated page. Page 1 uses base_url directly."""
    if page == 1:
        url = base_url
    else:
        # WordPress pagination: /page/N/
        url = base_url.rstrip("/") + f"/page/{page}/"
    return fetch_url(url)


def scrape_jobsnet_listing():
    """Scrape jobsnet.in/off-campus-drive/ pages. Returns list of {url, title, posted}."""
    base_url = "https://jobsnet.in/off-campus-drive/"
    all_entries = []

    for page in range(1, SCRAPE_PAGES + 1):
        html = _fetch_page_with_pagination(base_url, page)
        if not html:
            print(f"     jobsnet.in page {page}: failed to fetch")
            continue

        # Each article card
        articles = re.findall(
            r'<article[^>]*class="[^"]*entry-card[^"]*"[^>]*>.*?</article>',
            html, re.DOTALL
        )
        if not articles:
            print(f"     jobsnet.in page {page}: no articles found")
            break

        for art in articles:
            # Title + URL from h3.entry-title
            title_match = re.search(
                r'<h3[^>]*class="[^"]*entry-title[^"]*"[^>]*>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                art, re.DOTALL
            )
            if not title_match:
                continue
            url = title_match.group(1)
            title = clean_text(title_match.group(2))

            # Date from time tag
            date_match = re.search(
                r'<time[^>]*datetime="([^"]+)"[^>]*>(.*?)</time>',
                art, re.DOTALL
            )
            posted = ""
            if date_match:
                posted = clean_text(date_match.group(2))

            all_entries.append({"url": url, "title": title, "posted": posted})

        print(f"     jobsnet.in page {page}: {len(articles)} entries")
        
        # Check if there's a next page
        if page < SCRAPE_PAGES:
            next_link = re.search(r'class="next[^"]*"[^>]*href="([^"]+)"', html)
            if not next_link:
                break  # No more pages

    print(f"  📥 jobsnet.in total: {len(all_entries)} entries")
    return all_entries


def scrape_freshershunt_listing():
    """Scrape freshershunt.in job listing pages. Returns list of {url, title, posted}."""
    base_url = "https://freshershunt.in/off-campus-drive-jobs/off-campus-drive/"
    all_entries = []

    for page in range(1, SCRAPE_PAGES + 1):
        html = _fetch_page_with_pagination(base_url, page)
        if not html:
            print(f"     freshershunt.in page {page}: failed to fetch")
            continue

        # Each article
        articles = re.findall(
            r'<article[^>]*>.*?</article>',
            html, re.DOTALL
        )
        if not articles:
            print(f"     freshershunt.in page {page}: no articles found")
            break

        for art in articles:
            # Title + URL
            title_match = re.search(
                r'<h2[^>]*class="[^"]*entry-title[^"]*"[^>]*>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                art, re.DOTALL
            )
            if not title_match:
                continue
            url = title_match.group(1)
            title = clean_text(title_match.group(2))

            # Date
            date_match = re.search(
                r'<time[^>]*datetime="([^"]+)"[^>]*>(.*?)</time>',
                art, re.DOTALL
            )
            posted = ""
            if date_match:
                posted = clean_text(date_match.group(2))

            all_entries.append({"url": url, "title": title, "posted": posted})

        print(f"     freshershunt.in page {page}: {len(articles)} entries")

        # Check for next page
        if page < SCRAPE_PAGES:
            next_link = re.search(r'class="next[^"]*"[^>]*href="([^"]+)"', html)
            if not next_link:
                break

    print(f"  📥 freshershunt.in total: {len(all_entries)} entries")
    return all_entries


# ── Scraping: Individual job detail ──────────────────────────────────────

def _extract_company_from_title(title):
    """Guess company name from a listing title like 'Company Hiring Title ...'."""
    if not title:
        return ""
    
    # Common patterns: "Company Hiring ...", "Company Off Campus ...", etc.
    # The company is usually the first word(s) before a known trigger word
    patterns = [
        r'^([A-Za-z0-9&.\s()]+?)\s+(?:Off Campus|Hiring|Recruitment|Internship|Walk[- ]In)',
        r'^([A-Za-z0-9&.\s()]+?)\s+(?:is|are)\s+(?:hiring|looking|seeking)',
    ]
    for pat in patterns:
        m = re.search(pat, title, re.IGNORECASE)
        if m:
            c = clean_text(m.group(1))
            # Validate: company shouldn't be too long or contain a job title
            if len(c) > 1 and len(c) < 40 and not re.search(r'(Engineer|Developer|Intern|Analyst|Associate|Program)', c, re.IGNORECASE):
                return c
    
    # Try to find known company names in the title
    known = [
        "Accenture", "Adobe", "Amazon", "Apple", "Capgemini", "Cisco", "Cognizant",
        "Dell", "Deloitte", "Google", "HCL", "HPE", "HP", "IBM", "Infosys", "Intel",
        "JPMorgan", "Microsoft", "Oracle", "Qualcomm", "TCS", "Wipro", "ADP", "Zoom",
        "Fiserv", "MetLife", "Quest Global", "ZS Associates", "Zebra", "Alcon",
        "Adani", "Volvo", "Dentsu", "Ingram Micro", "Calix", "Sanmina", "GE Appliances",
        "SLB", "Harman", "S&P Global", "CSG", "Invesco", "IQVIA", "Deutsche Bank",
        "Syniverse", "Philips", "Emerson", "Lowe's", "Rockwell", "Fortrea", "NTT DATA",
        "CGI", "Honeywell", "Swiss Re", "Principal", "Headout", "Vonage",
        "TransUnion", "Docusign", "Empower", "Johnson Controls", "Siemens",
        "Sutherland", "Canonical", "Citi", "Citigroup", "GlobalLogic", "NEC Corporation",
        "NTT DATA", "Blackhawk Network", "Zinier", "Verint", "Lighthouse",
        "Qualifacts", "Medpace", "Keystone", "Born West", "Tower Research Capital"
    ]
    for name in known:
        if name.lower() in title.lower():
            return name
    
    return ""


def scrape_job_detail(url, default_title="", default_date="", default_company=""):
    """Fetch a single job post page and extract details."""
    result = {
        "title": default_title,
        "company": default_company,
        "location": "",
        "salary": "",
        "posted": default_date,
        "url": url,
        "category": "software-engineering"
    }

    html = fetch_url(url)
    if not html:
        return result

    # ── Title ──
    og_title = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', html)
    if og_title:
        t = clean_text(og_title.group(1))
        t = re.sub(r'\s*[-–|]\s*(?:Jobsnet\.in|Freshershunt).*$', '', t, flags=re.IGNORECASE)
        if t:
            result["title"] = t

    if not result.get("title"):
        h1 = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
        if h1:
            result["title"] = clean_text(h1.group(1))

    # ── Date (from page if not already set) ──
    if not result.get("posted"):
        # Try <time> tag
        time_match = re.search(r'<time[^>]*>(.*?)</time>', html)
        if time_match:
            t = clean_text(time_match.group(1))
            if re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)', t):
                result["posted"] = t
        # Fallback: meta published time
        if not result.get("posted"):
            pub_match = re.search(r'<meta[^>]+property="article:published_time"[^>]+content="([^"]+)"', html)
            if pub_match:
                dt = pub_match.group(1)[:10]  # YYYY-MM-DD
                # Convert to readable format
                try:
                    from datetime import datetime as dt_parse
                    d = dt_parse.strptime(dt, "%Y-%m-%d")
                    result["posted"] = d.strftime("%d-%b-%Y")
                except:
                    result["posted"] = dt
    
    # ── Description ──
    og_desc = re.search(r'<meta[^>]+property="og:description"[^>]+content="([^"]+)"', html)
    desc = og_desc.group(1) if og_desc else ""

    # ── Company ──
    if not result.get("company"):
        if desc:
            for pat in [
                r'^([A-Za-z0-9\s&.()]+?)\s+is\s+(?:currently\s+)?(?:seeking|hiring|looking)',
                r'^([A-Za-z0-9\s&.()]+?)\s+Off\s+Campus',
            ]:
                m = re.search(pat, desc, re.IGNORECASE)
                if m:
                    c = clean_text(m.group(1))
                    # Validate: should not contain job role keywords
                    if c and len(c) < 40 and not re.search(r'(Engineer|Developer|Intern|Analyst|Associate|Program|Software|Trainee)', c, re.IGNORECASE):
                        result["company"] = c
                        break

    if not result.get("company"):
        # Try from the first part of title before a pipe or dash
        title_guess = _extract_company_from_title(result.get("title", ""))
        if title_guess:
            result["company"] = title_guess

    # ── Location ──
    city_pat = r'(?:Bangalore|Bengaluru|Hyderabad|Pune|Chennai|Mumbai|Gurgaon|Gurugram|Noida|Delhi|Pan India|Remote|Kolkata|Ahmedabad|Vadodara|Kozhikode|Navi Mumbai)'
    if desc:
        m = re.search(rf'(?:in|at|Location\s*:)\s*({city_pat}(?:\s*/+\s*{city_pat})*)', desc, re.IGNORECASE)
        if not m:
            m = re.search(city_pat, desc)
        if m:
            result["location"] = clean_text(m.group(0) if m.lastindex is None else m.group(1))

    # ── Salary ──
    # Be specific: actual salary figures with ₹, LPA, etc.
    sal_patterns = [
        r'(?:₹|Rs\.?|INR)\s*[\d,]+\s*(?:-\s*(?:₹|Rs\.?|INR)?\s*[\d,]+)?\s*(?:LPA|Lacs?|Lakhs?|/annum|pa|PA|per annum|CTC)',
        r'~?\s*₹\s*[\d,]+\s*(?:-\s*₹\s*[\d,]+)?\s*(?:LPA|Lacs?|Lakhs?|/annum|PA)',
        r'(?<!\w)[\d]+(?:\s*-\s*[\d]+)?\s*(?:LPA|Lacs?|Lakhs?)',
        r'[\d]+[Kk]\s*(?:-\s*[\d]+[Kk])?\s*(?:per month|/month|/mo)',
        r'₹\s*[\d,]+(?:\s*-\s*₹?[\d,]+)?',
    ]
    for pat in sal_patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            sal = clean_text(m.group(0))
            # Filter out false matches (too short, or not a real salary)
            if len(sal) >= 3 and not re.match(r'^[Kk\s]+$', sal):
                result["salary"] = sal
                break

    # ── Apply URL (stored as secondary info, NOT replacing the aggregator URL)
    # The aggregator URL is kept because it has the posted date, company info, etc.
    # The real apply link is extracted and stored for reference.
    domain = urlparse(url).netloc
    exclude_domains = r'(?:facebook|twitter|x\.com|linkedin|addtoany|share|feedburner|wordpress|gmpg\.org|googletagmanager|googleapis|gravatar|w\.org|js\.delivr|cloudflare|fontawesome|pagead2|googlesyndication|doubleclick|google\.co\.in|googleanalytics|gstatic|pixel|cdn|telegram\.im|fundingchoicesmessages|stats\.wp|google\.com|youtube\.com|chat\.whatsapp|whatsapp\.com|adtrafficquality\.google)'
    all_links = re.findall(r'href="(https?://[^"]+)"', html)
    
    apply_url = ""
    # Look for job portal / career links (must be on a different domain than the aggregator)
    job_patterns = r'(?:careers?\.|myworkdayjobs|greenhouse\.io|lever\.|breezy\.|icims\.|njoyn\.|smartrecruiters|tracelink\.|workforcenow\.adp|accenture\.com.*career|career[^s]|[^a-z]job[s]?\?|jobdetail|position)'
    for link in all_links:
        ld = urlparse(link).netloc
        if ld != domain and re.search(job_patterns, link, re.IGNORECASE):
            apply_url = link
            break
    
    if not apply_url:
        # Second try: any external link not in exclusion list
        for link in all_links:
            ld = urlparse(link).netloc
            if ld and ld != domain and not re.search(exclude_domains, ld, re.IGNORECASE):
                if not any(w in link for w in ['facebook', 'twitter', 'linkedin', 'share', 'addtoany', 'pinterest']):
                    apply_url = link
                    break
    
    if apply_url:
        result["apply_url"] = apply_url
    # Keep the original url (aggregator page) as the primary URL

    # ── Category ──
    tl = result.get("title", "").lower()
    if "intern" in tl:
        result["category"] = "internships"

    return result


# ── Markdown rendering ───────────────────────────────────────────────────

def render_jobs_md(data):
    now = datetime.now(timezone.utc)
    last_updated = data.get("last_updated", now.strftime("%Y-%m-%d"))
    all_jobs = data.get("jobs", [])

    lines = []
    lines.append("---")
    lines.append("layout: standalone")
    lines.append("title: Job Listings")
    lines.append("---")
    lines.append("")
    lines.append("# Job Listings")
    lines.append("")
    lines.append("Daily tracked software engineering and game development opportunities for Abhay Raj.")
    lines.append("Auto-updated daily at 6:30 AM IST.")
    lines.append("")
    lines.append(f"Last updated: {last_updated}")
    lines.append("")
    lines.append("---")
    lines.append("")

    counter = 1
    for cat_key in CATEGORY_ORDER:
        cat_label = CATEGORY_LABELS.get(cat_key, cat_key)
        cat_jobs = [j for j in all_jobs if j.get("category", "software-engineering") == cat_key]
        if not cat_jobs:
            continue

        lines.append(f"## {cat_label}")
        lines.append("")
        lines.append("| # | Title | Company | Location | Salary | Posted | Apply |")
        lines.append("|---|-------|---------|----------|--------|--------|-------|")

        for job in cat_jobs:
            title = str(job.get("title", "Unknown")).replace("|", "\\|")
            company = str(job.get("company", "")).replace("|", "\\|")
            location = str(job.get("location", "")).replace("|", "\\|")
            salary = str(job.get("salary", "")).replace("|", "\\|")
            posted = str(job.get("posted", ""))
            # Use apply_url if available, fall back to url (aggregator)
            url = job.get("apply_url", "") or job.get("url", "#")

            lines.append(f"| {counter} | {title} | {company} | {location} | {salary} | {posted} | [Apply]({url}) |")
            counter += 1

        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 📌 How to Apply")
    lines.append("")
    lines.append("1. Click the Apply link next to any job")
    lines.append("2. Search the company name + job title on LinkedIn/Naukri if the link doesn't work")
    lines.append("3. Keep your resume updated with your GTBIT, B.Tech IT, Avalon, and Gamified experience")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Auto-updated as of {last_updated} by OpenClaw cron job. Listings older than {MAX_AGE_DAYS} days are automatically removed.*")
    lines.append("")

    return "\n".join(lines) + "\n"


def write_jobs_md(md_content):
    with open(JOBS_MD, "w") as f:
        f.write(md_content)
    print(f"  📄 Generated jobs.md ({len(md_content)} bytes)")


def generate_jobs_html(md_content):
    """Generate jobs.html from markdown content using standalone layout."""
    # Strip Jekyll frontmatter
    md_body = re.sub(r'^---\n.*?\n---\n', '', md_content, flags=re.DOTALL)
    
    # Convert markdown to HTML using marked via npx
    try:
        result = subprocess.run(
            ["npx", "--yes", "marked"],
            input=md_body.encode("utf-8"),
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0:
            content_html = result.stdout.decode("utf-8")
        else:
            print(f"  ⚠️  marked conversion failed: {result.stderr.decode()}")
            content_html = f"<pre>{md_body}</pre>"
    except Exception as e:
        print(f"  ⚠️  marked error: {e}")
        content_html = f"<pre>{md_body}</pre>"
    
    # Read the standalone layout template
    layout_path = os.path.join(REPO_DIR, "_layouts", "standalone.html")
    if not os.path.exists(layout_path):
        print(f"  ⚠️  Layout not found: {layout_path}")
        return None
    
    with open(layout_path, "r") as f:
        layout = f.read()
    
    # Replace Jekyll/Liquid template tags
    html = layout
    # {{ content }} → markdown body
    html = html.replace("{{ content }}", content_html)
    # {% if page.title %}...{% else %}...{% endif %}
    html = re.sub(
        r"{%\s*if\s+page\.title\s*%}(.*?){%\s*else\s*%}(.*?){%\s*endif\s*%}",
        r"\1",
        html,
        flags=re.DOTALL
    )
    # Resolve {{ page.title }} when title is known
    html = html.replace("{{ page.title }}", "Job Listings")
    # Any remaining {{ }} expressions
    html = re.sub(r"\{\{\s*[^}]+\s*\}\}", "", html)
    # Any remaining {% %} tags → just remove them
    html = re.sub(r"{%[^%]+%}", "", html)
    
    return html


def write_jobs_html(html_content):
    """Write jobs.html file."""
    html_path = os.path.join(REPO_DIR, "jobs.html")
    with open(html_path, "w") as f:
        f.write(html_content)
    print(f"  📄 Generated jobs.html ({len(html_content)} bytes)")


def sort_jobs_by_date(jobs):
    """Sort jobs descending by posted date (newest first).
    Handles mixed date formats (DD-Mon-YYYY and Month DD, YYYY).
    Jobs without dates go to the end.
    """
    def parse_sort_key(job):
        posted = job.get("posted", "")
        dt = parse_date(posted)
        if dt:
            return dt.timestamp()
        return 0  # No date → put at end
    
    return sorted(jobs, key=parse_sort_key, reverse=True)


def clean_source_dir():
    if not os.path.exists(SOURCE_DIR):
        return
    count = 0
    for f in os.listdir(SOURCE_DIR):
        fpath = os.path.join(SOURCE_DIR, f)
        if os.path.isfile(fpath):
            os.remove(fpath)
            count += 1
    if count > 0:
        print(f"  🧹 Cleaned {count} files from source/")
