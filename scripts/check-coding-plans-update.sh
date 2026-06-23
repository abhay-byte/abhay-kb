#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

echo "=== Coding Plans Update Check: $(date -u) ==="

# Fetch sources, strip Sources section, regenerate HTML, detect changes
python3 scripts/update-coding-plans.py
EXIT_CODE=$?

if [ $EXIT_CODE -eq 2 ]; then
    echo "CHANGED: Some coding plan sources have been updated."
    echo "Triggering LLM analysis for coding-plans.md update..."
    exit 0  # Success — cron agent will handle the actual update
elif [ $EXIT_CODE -eq 0 ]; then
    echo "OK: No changes detected."
    exit 0
else
    echo "ERROR: Script failed with exit code $EXIT_CODE"
    exit 1
fi
