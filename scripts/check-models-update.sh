#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

echo "=== Models Update Check: $(date -u) ==="

# Fetch sources and detect changes
python3 scripts/update-models.py
EXIT_CODE=$?

if [ $EXIT_CODE -eq 2 ]; then
    echo "CHANGED: Some model pricing sources have been updated."
    echo "Triggering LLM analysis for models.md update..."
    exit 0  # Success — cron agent will handle the actual update
elif [ $EXIT_CODE -eq 0 ]; then
    echo "OK: No changes detected."
    exit 0
else
    echo "ERROR: Script failed with exit code $EXIT_CODE"
    exit 1
fi
