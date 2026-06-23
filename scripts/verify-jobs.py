#!/usr/bin/env python3
"""verify-jobs.py — Check each job's apply URL, remove dead/expired ones.

Runs daily after sync-jobs.
Usage: python3 scripts/verify-jobs.py [--dry-run]
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jobslib import (
    load_data, save_data, dedup_jobs, filter_expired, sort_jobs_by_date,
    check_url_alive, render_jobs_md, generate_jobs_html,
    write_jobs_md, write_jobs_html,
    clean_source_dir, MAX_AGE_DAYS
)
from datetime import datetime, timezone, timedelta


def main():
    dry_run = "--dry-run" in sys.argv
    
    print(f"=== Job Verify === {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    if dry_run:
        print("  🏁 DRY RUN — no files will be saved")
    
    # 1. Load data
    data = load_data()
    all_jobs = data.get("jobs", [])
    print(f"  📂 Jobs loaded: {len(all_jobs)}")
    
    # 2. Remove expired by date (>28 days)
    fresh_jobs, expired_by_date = filter_expired(all_jobs)
    print(f"  📅 Expired by date (>={MAX_AGE_DAYS} days): {len(expired_by_date)}")
    for j in expired_by_date[:5]:
        print(f"     - {j.get('title', '?')} @ {j.get('company', '?')} ({j.get('posted', '?')})")
    if len(expired_by_date) > 5:
        print(f"     ... and {len(expired_by_date) - 5} more")
    
    # 3. Check each remaining job's apply URL with curl
    print("  🔗 Checking apply URLs...")
    dead_urls = []
    still_alive = []
    
    total = len(fresh_jobs)
    for idx, job in enumerate(fresh_jobs):
        url = job.get("url", "")
        if not url or url == "#":
            dead_urls.append(job)
            continue
        
        # Show progress
        progress = f"[{idx+1}/{total}]"
        title_short = (job.get("title", "?") + " @ " + job.get("company", "?"))[:50]
        
        alive = check_url_alive(url)
        if alive:
            still_alive.append(job)
            if idx % 10 == 0:
                print(f"     {progress} ✅ {title_short}")
        else:
            dead_urls.append(job)
            print(f"     {progress} ❌ DEAD: {title_short}")
    
    print(f"  🔗 URL check results:")
    print(f"     Alive: {len(still_alive)}")
    print(f"     Dead/removed: {len(dead_urls)}")
    
    # 4. Clean + sort
    data["jobs"] = sort_jobs_by_date(still_alive)
    data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    total_removed = len(expired_by_date) + len(dead_urls)
    print(f"  📊 Total jobs after verify: {len(still_alive)}")
    print(f"     Removed: {total_removed}")
    
    # 5. Generate markdown + HTML
    md = render_jobs_md(data)
    html = generate_jobs_html(md)
    
    if dry_run:
        print("  🏁 DRY RUN complete — files not saved")
        return
    
    # 6. Save everything
    save_data(data)
    write_jobs_md(md)
    if html:
        write_jobs_html(html)
    clean_source_dir()
    
    print("  ✅ Jobs verify complete!")


if __name__ == "__main__":
    main()
