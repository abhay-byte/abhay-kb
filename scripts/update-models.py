#!/usr/bin/env python3
"""
Fetch LLM model pricing sources and detect changes.
Stores raw content in source/ directory with hash tracking.

Slug ↔ URL mapping is derived from source URLs embedded in models.md.

Usage:
  python3 scripts/update-models.py

Behavior:
  - Fetches all source URLs, saves to source/{slug}.md
  - Compares content hashes to detect changes
  - If any changed → exits with code 2 and lists changes
  - If none changed → exits with code 0
  - If script fails → exits with code 1 (no change detection)
"""

import hashlib, json, os, re, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

BASE = Path(__file__).resolve().parent.parent
SOURCE_DIR = BASE / "source"
HASH_FILE = SOURCE_DIR / ".hashes.json"
MODELS_MD = BASE / "LLM" / "models.md"
MODELS_HTML = BASE / "LLM" / "models.html"

USER_AGENT = "Mozilla/5.0 (compatible; KB-Models-Updater/1.0)"
FETCH_DELAY = 1.5  # seconds between requests


def url_to_slug(url: str) -> str:
    """Convert a URL to a slug like the ones in models.md Sources section.
    E.g. https://platform.claude.com/docs/en/about/claude/pricing
       → platform-claude-com-docs-en-about-claude-pricing
    """
    # Remove protocol
    u = url.strip()
    u = re.sub(r'^https?://', '', u)
    u = u.rstrip('/')
    # Replace dots, slashes, and special chars with hyphens
    u = re.sub(r'[./]+', '-', u)
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
    """Strip volatile elements (timestamps, tokens, nonces, etc.) before hashing."""
    import html
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # Remove JSON inline data blobs (common in Next.js, etc.)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    # Remove nonce/csrf tokens
    text = re.sub(r'nonce="[^"]+"', '', text)
    text = re.sub(r'csrf[t_-]?token["\s=]+[a-zA-Z0-9_-]{20,}', '', text, flags=re.IGNORECASE)
    # Remove data-* attributes with volatile values (UUIDs, timestamps)
    text = re.sub(r'data-[a-z-]+="[a-f0-9]{8,}(-[a-f0-9]{4,}){3,}[a-f0-9]{12,}"', '', text)
    # Remove version query params (?v=..., ?t=...)
    text = re.sub(r'[?&](?:v|t|ver|ts|_|rnd)=\d+', '', text)
    # Remove build IDs, cache busters in URLs
    text = re.sub(r'/_next/static/[a-f0-9]{16,}/', '/_next/static/', text)
    # Remove sentry/observability trace IDs
    text = re.sub(r'name="sentry-trace"[^/]+/>', '', text)
    text = re.sub(r'name="baggage"[^/]+/>', '', text)
    # Remove timestamp/date markers embedded in HTML
    text = re.sub(r'"@timestamp":"[^"]+"', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def hash_content(content):
    normalized = normalize_content(content)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def main():
    SOURCE_DIR.mkdir(exist_ok=True)

    if not MODELS_MD.exists():
        print(f"ERROR: {MODELS_MD} not found")
        sys.exit(1)

    content = MODELS_MD.read_text()

    # Extract ALL external URLs from models.md
    all_urls = re.findall(r'https?://[^\s\)\]",<>]+', content)
    # Normalize: strip trailing punctuation that's not part of URL
    normalized = []
    for u in all_urls:
        u = u.rstrip(').,;:!?')
        if any(u.startswith(p) for p in ['http://www.w3.org']):
            continue  # skip SVG namespace
        normalized.append(u)

    # Deduplicate while preserving order
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

        content = fetch_url(url)
        if content is None:
            print()
            continue  # skip failed URLs, don't mark as changed

        # Skip pages that return error content despite HTTP 200
        title_match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
        page_title = title_match.group(1).lower() if title_match else ''
        if 'not found' in page_title or '404' in page_title or 'error' in page_title:
            print(f'PAGE_ERROR ({page_title[:30]})')
            # Keep old hash to avoid false change detection
            old_h = old_hashes.get(slug)
            if old_h:
                new_hashes[slug] = old_h
            else:
                # First time seeing this error; still track new hash
                h = hash_content(content)
                new_hashes[slug] = h
                save_source(slug, content)
            continue

        h = hash_content(content)
        new_hashes[slug] = h
        save_source(slug, content)

        old_h = old_hashes.get(slug)
        if old_h is None:
            print(f"NEW ({len(content)} bytes)")
            changed.append(slug)
        elif old_h != h:
            print(f"CHANGED ({len(content)} bytes)")
            changed.append(slug)
        else:
            print("unchanged")

        time.sleep(FETCH_DELAY)

    save_hashes(new_hashes)

    # Clean stale source files
    known_slugs = set(new_hashes.keys())
    existing = set(f.stem for f in SOURCE_DIR.glob("*.md") if f.name != ".hashes.json")
    stale = existing - known_slugs
    for s in stale:
        (SOURCE_DIR / f"{s}.md").unlink()
        print(f"  Removed stale source: {s}")

    if changed:
        print(f"\n⚠ {len(changed)} source{'s' if len(changed)>1 else ''} changed:")
        for s in changed:
            print(f"  - {s}")
        print("\nmodels.md may need updating. Exit code 2")
        sys.exit(2)
    else:
        print(f"\n✓ All {len(unique_urls)} sources unchanged")
        sys.exit(0)


if __name__ == "__main__":
    main()
