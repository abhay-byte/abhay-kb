#!/bin/bash
# DSA Weekly Summary — runs every Sunday, sends weekly progress email

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DSA_DIR="$(dirname "$SCRIPT_DIR")"
TRACKER="$DSA_DIR/tracker.json"
AGENTMAIL_API_KEY="am_us_inbox_1f3e4c9f980cd74da03b8ac2bd4748ece495515d62f7b024c5d3f5217324c70f"
AGENTMAIL_INBOX="ab-brain-bot@agentmail.to"
SEND_TO="abhay02delhi@gmail.com"
DATE=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)
YEAR=$(date +%Y)

# Read tracker
TOTAL_GIVEN=$(python3 -c "import json; d=json.load(open('$TRACKER')); print(d['daily']['total_questions_given'])")
TOTAL_COMPLETED=$(python3 -c "import json; d=json.load(open('$TRACKER')); print(d['daily']['total_questions_completed'])")
CURRENT_LECTURE=$(python3 -c "import json; d=json.load(open('$TRACKER')); print(d['current_lecture'])")

# Get this week's daily logs
WEEK_DIR="$DSA_DIR/progress/daily"
THIS_WEEK_LOGS=$(find "$WEEK_DIR" -name "*.md" -newer "$WEEK_DIR/$(date -d '7 days ago' +%Y-%m-%d 2>/dev/null || echo '1970-01-01').md" 2>/dev/null || find "$WEEK_DIR" -name "*.md" | head -7)

# Count completed this week
WEEK_COMPLETED=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
import datetime
week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
count = sum(1 for entry in d['completion_log'] if entry.get('completed') and entry.get('date_completed','') >= week_ago)
print(count)
")

# Build list of what was done this week
WEEK_COMPLETED_LIST=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
import datetime
week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
done = [entry for entry in d['completion_log'] if entry.get('completed') and entry.get('date_completed','') >= week_ago]
if done:
    for entry in done:
        print(f\"✅ {entry['question']} (L{entry['lecture']})\")
else:
    print('Nothing completed this week yet')
")

WEEK_PENDING_LIST=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
import datetime
week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
pending = [entry for entry in d['completion_log'] if not entry.get('completed') and entry.get('date_given','') >= week_ago]
if pending:
    for entry in pending:
        print(f\"⬜ {entry['question']} (L{entry['lecture']})\")
")

EMAIL_TEXT="📊 DSA Weekly Report — Week $WEEK_NUM ($YEAR)
━━━━━━━━━━━━━━━━━━━━━━━━━
Report Date: $DATE
━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Overall Progress
• Questions Given: $TOTAL_GIVEN
• Completed: $TOTAL_COMPLETED
• Current Lecture: $CURRENT_LECTURE

━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Completed This Week:
$WEEK_COMPLETED_LIST

━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Still Pending This Week:
$WEEK_PENDING_LIST
━━━━━━━━━━━━━━━━━━━━━━━━━

Keep pushing! Next week we continue with more problems. 🚀"

EMAIL_HTML="<html>
<body style='font-family: sans-serif; background: #0d0d0d; color: #e0e0e0; padding: 20px;'>
<div style='max-width: 600px; margin: 0 auto;'>
<div style='border-bottom: 2px solid #fabd2f; padding-bottom: 12px; margin-bottom: 20px;'>
<h1 style='color: #fff; margin: 0;'>📊 DSA Weekly Report</h1>
<p style='color: #888; margin: 4px 0 0;'>Week $WEEK_NUM ($YEAR) — $DATE</p>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px;'>
<h3 style='color: #fabd2f; margin: 0 0 12px;'>📊 Overall Progress</h3>
<table style='width: 100%; color: #ccc; font-size: 14px;'>
<tr><td>Questions Given</td><td style='text-align: right; color: #fff; font-weight: bold;'>$TOTAL_GIVEN</td></tr>
<tr><td>Questions Completed</td><td style='text-align: right; color: #34a853; font-weight: bold;'>$TOTAL_COMPLETED</td></tr>
<tr><td>Current Lecture</td><td style='text-align: right; color: #fabd2f; font-weight: bold;'>$CURRENT_LECTURE</td></tr>
</table>
</div>

<div style='background: #111122; border-radius: 8px; padding: 16px; margin-bottom: 16px; border-left: 3px solid #34a853;'>
<h3 style='color: #34a853; margin: 0 0 8px;'>✅ Completed This Week</h3>
<pre style='color: #ccc; margin: 0; font-size: 13px; white-space: pre-wrap;'>$WEEK_COMPLETED_LIST</pre>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px; border-left: 3px solid #fabd2f;'>
<h3 style='color: #fabd2f; margin: 0 0 8px;'>📋 Still Pending</h3>
<pre style='color: #ccc; margin: 0; font-size: 13px; white-space: pre-wrap;'>$WEEK_PENDING_LIST</pre>
</div>

<p style='color: #666; text-align: center; margin-top: 24px; font-size: 12px;'>Keep pushing! 🚀</p>
</div>
</body>
</html>"

# Send email
curl -s -X POST "https://api.agentmail.to/v0/inboxes/$AGENTMAIL_INBOX/messages" \
  -H "Authorization: Bearer $AGENTMAIL_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"to\": [\"$SEND_TO\"],
    \"subject\": \"📊 DSA Weekly Report — Week $WEEK_NUM\",
    \"text\": $(echo "$EMAIL_TEXT" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))"),
    \"html\": $(echo "$EMAIL_HTML" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")
  }"

echo "Weekly report email sent for week $WEEK_NUM"

# Write weekly markdown log
cat > "$DSA_DIR/progress/weekly/$YEAR-W$WEEK_NUM.md" << EOF
# 📊 DSA Weekly Report — Week $WEEK_NUM, $YEAR

**Report Date:** $DATE

## Overall Progress
- **Questions Given:** $TOTAL_GIVEN
- **Completed:** $TOTAL_COMPLETED
- **Current Lecture:** Lecture $CURRENT_LECTURE

## ✅ Completed This Week
$WEEK_COMPLETED_LIST

## 📋 Pending
$WEEK_PENDING_LIST

---

*Next week: continue with more DSA problems! 🚀*
EOF

echo "✓ Weekly log created: progress/weekly/$YEAR-W$WEEK_NUM.md"
