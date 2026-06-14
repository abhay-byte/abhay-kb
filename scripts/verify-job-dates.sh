#!/bin/bash
# verify-job-dates.sh — Check job listing dates and remove expired ones (>28 days old)

JOBS_FILE="/repos/abhay-kb/jobs.md"
TODAY=$(date +%s)
MAX_AGE_DAYS=28

# Extract all apply links with row info
extract_links() {
    grep -n 'Apply\](' "$JOBS_FILE" | while IFS= read -r line; do
        lineno=$(echo "$line" | cut -d: -f1)
        url=$(echo "$line" | grep -oP 'Apply\]\(\K[^)]+')
        title=$(echo "$line" | sed 's/|/\n/g' | sed -n '3p' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
        company=$(echo "$line" | sed 's/|/\n/g' | sed -n '4p' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
        posted=$(echo "$line" | sed 's/|/\n/g' | sed -n '7p' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
        [ -n "$url" ] && echo "${lineno}|${title}|${company}|${posted}|${url}"
    done
}

# Get date from URL
get_date_from_url() {
    local url="$1"
    curl -sL --max-time 15 "$url" -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36' | grep -ioP '(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+20\d{2}' | head -1
}

# Convert date string to epoch
date_to_epoch() {
    date -d "$1" +%s 2>/dev/null
}

echo "=== JOB DATE VERIFICATION ==="
echo "Date: $(date '+%Y-%m-%d %H:%M %Z')"
echo ""

declare -a REMOVE_LINES=()
VISITED=0

# Process oldest 10 links (first 10 in file)
extract_links | head -10 | while IFS='|' read -r lineno title company posted url; do
    [ -z "$url" ] && continue
    VISITED=$((VISITED + 1))
    
    page_date=$(get_date_from_url "$url")
    
    if [ -n "$page_date" ]; then
        epoch=$(date_to_epoch "$page_date")
        if [ -n "$epoch" ]; then
            age_days=$(( (TODAY - epoch) / 86400 ))
            if [ "$age_days" -gt "$MAX_AGE_DAYS" ]; then
                echo "REMOVE|${lineno}|${title}|${company}|${posted}|${page_date}|${age_days}d|${url}"
            else
                echo "KEEP|${lineno}|${title}|${company}|${posted}|${page_date}|${age_days}d|${url}"
            fi
        else
            echo "UNKNOWN|${lineno}|${title}|${company}|${posted}|${page_date}|parse-fail|${url}"
        fi
    else
        echo "NO_DATE|${lineno}|${title}|${company}|${posted}|?|fetch-fail|${url}"
    fi
done
