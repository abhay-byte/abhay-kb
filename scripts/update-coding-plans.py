#!/usr/bin/env python3
"""
Fetch coding plans pricing source URLs and detect changes.
Stores raw content in source/ directory with hash tracking.
Removes any Sources section from coding-plans.md.
Regenerates coding-plans.html from coding-plans.md.

Usage:
  python3 scripts/update-coding-plans.py

Behavior:
  - Fetches all source URLs, saves to source/{slug}.md
  - Compares content hashes to detect changes
  - Strips any Sources section from coding-plans.md
  - Regenerates coding-plans.html
  - If any changed → exits with code 2 and lists changes
  - If none changed → exits with code 0
  - If script fails → exits with code 1 (no change detection)
"""

import hashlib, json, os, re, subprocess, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

BASE = Path(__file__).resolve().parent.parent
SOURCE_DIR = BASE / "source"
HASH_FILE = SOURCE_DIR / ".hashes-coding.json"
CODER_MD = BASE / "LLM" / "coding-plans.md"
CODER_HTML = BASE / "LLM" / "coding-plans.html"
LAYOUT_PATH = BASE / "_layouts" / "standalone.html"

USER_AGENT = "Mozilla/5.0 (compatible; KB-CodingPlans-Updater/1.0)"
FETCH_DELAY = 1.5  # seconds between requests


def url_to_slug(url: str) -> str:
    """Convert a URL to a slug."""
    u = url.strip()
    u = re.sub(r'^https?://', '', u)
    u = u.rstrip('/')
    u = re.sub(r'[./]+', '-', u)
    # Truncate to avoid excessively long filenames
    if len(u) > 120:
        u = u[:120]
    return u


def load_hashes():
    if HASH_FILE.exists():
        return json.loads(HASH_FILE.read_text())
    return {}


def save_hashes(hashes):
    HASH_FILE.write_text(json.dumps(hashes, indent=2, sort_keys=True))


def fetch_url(url, retries=2):
    """Fetch URL and return text content, or None on failure."""
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "text/html,*/*;q=0.8"
    })
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read()
                try:
                    return raw.decode("utf-8")
                except:
                    return raw.decode("latin-1")
        except Exception as e:
            if attempt < retries:
                time.sleep(2)
                continue
            print(f"FAILED ({type(e).__name__}: {str(e)[:60]})", end="")
            return None


def save_source(slug, content):
    path = SOURCE_DIR / f"{slug}.md"
    path.write_text(content)


def normalize_content(content: str) -> str:
    """Strip volatile elements before hashing."""
    text = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'nonce="[^"]+"', '', text)
    text = re.sub(r'csrf[t_-]?token["\s=]+[a-zA-Z0-9_-]{20,}', '', text, flags=re.IGNORECASE)
    text = re.sub(r'data-[a-z-]+="[a-f0-9]{8,}(-[a-f0-9]{4,}){3,}[a-f0-9]{12,}"', '', text)
    text = re.sub(r'[?&](?:v|t|ver|ts|_|rnd)=\d+', '', text)
    text = re.sub(r'/_next/static/[a-f0-9]{16,}/', '/_next/static/', text)
    text = re.sub(r'name="sentry-trace"[^/]+/>', '', text)
    text = re.sub(r'name="baggage"[^/]+/>', '', text)
    text = re.sub(r'"@timestamp":"[^"]+"', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def hash_content(content):
    normalized = normalize_content(content)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def strip_sources_section(md_content: str) -> str:
    """Remove the ## Sources section and any trailing --- from markdown."""
    # Remove ## Sources and everything after it
    text = re.sub(r'\n+## Sources\s*.*$', '', md_content, flags=re.DOTALL)
    # Remove trailing horizontal rules
    text = re.sub(r'\n---\s*$', '', text)
    return text


def generate_html(md_content: str) -> str:
    """Generate standalone HTML from markdown content."""
    md_body = re.sub(r'^---\n.*?\n---\n', '', md_content, flags=re.DOTALL)

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
            print(f"  ⚠️ marked conversion failed: {result.stderr.decode()}")
            content_html = f"<pre>{md_body}</pre>"
    except Exception as e:
        print(f"  ⚠️ marked error: {e}")
        content_html = f"<pre>{md_body}</pre>"

    if not LAYOUT_PATH.exists():
        print(f"  ❌ Layout not found: {LAYOUT_PATH}")
        return None

    layout = LAYOUT_PATH.read_text()
    html = layout
    html = html.replace("{{ content }}", content_html)
    html = re.sub(
        r"{%\s*if\s+page\.title\s*%}(.*?){%\s*else\s*%}(.*?){%\s*endif\s*%}",
        r"\1", html, flags=re.DOTALL
    )
    html = html.replace("{{ page.title }}", "Coding Plans")
    html = re.sub(r"\{\{\s*[^}]+\s*\}\}", "", html)
    html = re.sub(r"{%[^%]+%}", "", html)
    return html


def main():
    SOURCE_DIR.mkdir(exist_ok=True)

    if not CODER_MD.exists():
        print(f"ERROR: {CODER_MD} not found")
        sys.exit(1)

    content = CODER_MD.read_text()

    # Strip any Sources section first
    cleaned = strip_sources_section(content)

    # Update the last-updated date
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cleaned = re.sub(
        r'(Last updated: )\d{4}-\d{2}-\d{2}',
        r'\g<1>' + today,
        cleaned
    )

    # Extract ALL external URLs from coding-plans.md
    all_urls = re.findall(r'https?://[^\s\)\]",<>]+', cleaned)
    normalized = []
    for u in all_urls:
        u = u.rstrip(').,;:!?')
        # Skip SVG namespace URLs, data URIs, etc.
        if any(u.startswith(p) for p in ['http://www.w3.org', 'data:']):
            continue
        normalized.append(u)

    # Deduplicate
    seen = set()
    unique_urls = []
    for u in normalized:
        if u not in seen:
            seen.add(u)
            unique_urls.append(u)

    print(f"✓ Found {len(unique_urls)} unique source URLs")

    old_hashes = load_hashes()
    new_hashes = {}
    changed = []

    for i, url in enumerate(unique_urls, 1):
        slug = url_to_slug(url)
        print(f"  [{i}/{len(unique_urls)}] {slug}...", end=" ", flush=True)

        fetched = fetch_url(url)
        if fetched is None:
            print()
            continue

        # Skip error pages
        title_match = re.search(r'<title>([^<]+)</title>', fetched, re.IGNORECASE)
        page_title = title_match.group(1).lower() if title_match else ''
        if 'not found' in page_title or '404' in page_title or 'error' in page_title:
            print(f'PAGE_ERROR ({page_title[:30]})')
            old_h = old_hashes.get(slug)
            if old_h:
                new_hashes[slug] = old_h
            else:
                h = hash_content(fetched)
                new_hashes[slug] = h
                save_source(slug, fetched)
            continue

        h = hash_content(fetched)
        new_hashes[slug] = h
        save_source(slug, fetched)

        old_h = old_hashes.get(slug)
        if old_h is None:
            print(f"NEW ({len(fetched)} bytes)")
            changed.append(slug)
        elif old_h != h:
            print(f"CHANGED ({len(fetched)} bytes)")
            changed.append(slug)
        else:
            print("unchanged")

        time.sleep(FETCH_DELAY)

    save_hashes(new_hashes)

    # Clean stale source files
    known_slugs = set(new_hashes.keys())
    existing = set(f.stem for f in SOURCE_DIR.glob("*.md") if f.name != ".hashes.json" and not f.name.endswith("-coding.json"))
    stale = existing - known_slugs
    for s in stale:
        (SOURCE_DIR / f"{s}.md").unlink()
        print(f"  Removed stale source: {s}")

    # If Sources section was removed or file was otherwise updated, write back
    if cleaned != content:
        CODER_MD.write_text(cleaned)
        changed.append("sources-section-removed")
        print("  Removed Sources section from coding-plans.md")

        # Regenerate HTML
        html = generate_html(cleaned)
        if html:
            CODER_HTML.write_text(html)
            print(f"  📄 Generated coding-plans.html ({len(html)} bytes)")

    if changed:
        print(f"\n⚠ {len(changed)} source{'s' if len(changed)>1 else ''} changed:")
        for s in changed:
            print(f"  - {s}")
        print("\ncoding-plans.md updated. Exit code 2")
        sys.exit(2)
    else:
        print(f"\n✓ All {len(unique_urls)} sources unchanged, coding-plans.md clean")
        sys.exit(0)


if __name__ == "__main__":
    main()
