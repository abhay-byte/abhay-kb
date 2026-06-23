#!/usr/bin/env python3
"""sync-jobs.py — Scrape job aggregators, fetch details, append new jobs.

Runs daily as part of the job listing automation.
Usage: python3 scripts/sync-jobs.py [--dry-run]
"""

import sys
import os

# Add script dir to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jobslib import (
    load_data, save_data, dedup_jobs,
    scrape_jobsnet_listing, scrape_freshershunt_listing,
    scrape_job_detail, render_jobs_md, generate_jobs_html,
    write_jobs_md, write_jobs_html,
    clean_source_dir, MAX_AGE_DAYS
)
from datetime import datetime, timezone


def main():
    dry_run = "--dry-run" in sys.argv
    
    print(f"=== Job Sync === {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    if dry_run:
        print("  🏁 DRY RUN — no files will be saved")
    
    # 1. Load existing data
    data = load_data()
    existing_jobs = data.get("jobs", [])
    existing_urls = set(j.get("url", "") for j in existing_jobs)
    print(f"  📂 Existing jobs: {len(existing_jobs)}")
    
    # 2. Scrape listing pages for new URLs
    print("  🔍 Scraping aggregators...")
    all_new_entries = []
    
    # jobsnet.in
    jn_entries = scrape_jobsnet_listing()
    print(f"     jobsnet.in: {len(jn_entries)} entries")
    all_new_entries.extend(jn_entries)
    
    # freshershunt.in
    fs_entries = scrape_freshershunt_listing()
    print(f"     freshershunt.in: {len(fs_entries)} entries")
    all_new_entries.extend(fs_entries)
    
    # 3. Filter out URLs we already have
    new_urls = []
    for entry in all_new_entries:
        url = entry.get("url", "").strip()
        if url and url not in existing_urls:
            new_urls.append(entry)
            existing_urls.add(url)  # Prevent duplicates within this batch
    
    print(f"  🆕 New URLs to scrape: {len(new_urls)}")
    
    if not new_urls:
        print("  ✅ No new jobs to add")
        # Still regenerate markdown with current data
        if not dry_run:
            md = render_jobs_md(data)
            write_jobs_md(md)
            clean_source_dir()
        print("  ✅ Done")
        return
    
    # 4. Scrape each new job's detail page
    print(f"  🔎 Scraping individual job pages...")
    new_jobs = []
    scrape_count = 0
    for entry in new_urls:
        url = entry.get("url", "")
        default_date = entry.get("posted", "")
        scrape_count += 1
        print(f"     [{scrape_count}/{len(new_urls)}] {url[:60]}...")
        
        detail = scrape_job_detail(url, default_date)
        
        # Only add if we got at least a title
        if detail.get("title") or detail.get("company"):
            new_jobs.append(detail)
        else:
            # Still add with whatever we got (URL at minimum)
            if not detail.get("title"):
                # Extract title from URL as fallback
                path = url.rstrip("/").split("/")[-1]
                detail["title"] = path.replace("-", " ").title()
            new_jobs.append(detail)
    
    print(f"  📥 Scraped details for {len(new_jobs)} new jobs")
    
    # 5. Merge with existing jobs
    all_jobs = existing_jobs + new_jobs
    all_jobs = dedup_jobs(all_jobs)
    data["jobs"] = all_jobs
    data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    print(f"  📊 Total jobs after sync: {len(all_jobs)}")
    print(f"     New additions: {len(new_jobs)}")
    
    # 6. Generate markdown + HTML
    md = render_jobs_md(data)
    html = generate_jobs_html(md)
    
    if dry_run:
        print("  🏁 DRY RUN complete — files not saved")
        return
    
    # 7. Save everything
    save_data(data)
    write_jobs_md(md)
    if html:
        write_jobs_html(html)
    clean_source_dir()
    
    print("  ✅ Jobs sync complete!")


if __name__ == "__main__":
    main()
