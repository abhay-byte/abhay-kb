#!/bin/bash
# cron-sync-projects.sh — Runs daily at 6:00 AM IST
# Syncs PROJECTS.md from GitHub API, commits changes, pushes

set -e

export HOME="/home/jica98"
export PATH="/home/jica98/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"

KB_DIR="/home/jica98/repos/abhay-kb"
LOG_FILE="/home/jica98/repos/abhay-kb/scripts/sync-projects.log"

cd "$KB_DIR"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M IST')
echo "[$TIMESTAMP] Starting sync..." >> "$LOG_FILE"

# 1. Sync
python3 scripts/sync-projects.py > /tmp/sync-projects-out.log 2>&1
SYNC_EXIT=$?
if [ $SYNC_EXIT -ne 0 ]; then
    echo "[$TIMESTAMP] ERROR: sync failed (exit $SYNC_EXIT)" >> "$LOG_FILE"
    cat /tmp/sync-projects-out.log >> "$LOG_FILE"
    exit 1
fi

# 2. Stage
git add PROJECTS.md PROJECTS.html scripts/sync-projects.py
CHANGES=$(git diff --cached --name-only)
if [ -z "$CHANGES" ]; then
    echo "[$TIMESTAMP] No changes." >> "$LOG_FILE"
    exit 0
fi

# 3. Summary
REPO_COUNT=$(grep -oP 'Total Repositories[^0-9]*\|\s*\K[0-9]+' PROJECTS.md | head -1)
STAR_COUNT=$(grep -oP 'Total Stars[^0-9]*\|\s*\K[0-9]+' PROJECTS.md | head -1)
TOP_PROJECT=$(sed -n 's/^| 1 | \[\([^]]*\)\].*/\1/p' PROJECTS.md | head -1)

SUMMARY="${REPO_COUNT:-?} repos, ${STAR_COUNT:-?} stars — top: ${TOP_PROJECT:-?}"

# 4. Commit + push
git commit -m "projects: daily sync — $SUMMARY"
git push origin main >> "$LOG_FILE" 2>&1
PUSH_EXIT=$?

if [ $PUSH_EXIT -eq 0 ]; then
    echo "[$TIMESTAMP] Pushed: $SUMMARY" >> "$LOG_FILE"
    echo "$SUMMARY" > /tmp/last-projects-sync.txt
else
    echo "[$TIMESTAMP] ERROR: push failed (exit $PUSH_EXIT)" >> "$LOG_FILE"
fi

echo "[$TIMESTAMP] Done." >> "$LOG_FILE"
