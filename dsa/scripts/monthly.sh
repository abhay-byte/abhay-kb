#!/bin/bash
# DSA Monthly Summary — runs on last day of month, sends monthly progress email

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DSA_DIR="$(dirname "$SCRIPT_DIR")"
TRACKER="$DSA_DIR/tracker.json"
AGENTMAIL_API_KEY="am_us_inbox_1f3e4c9f980cd74da03b8ac2bd4748ece495515d62f7b024c5d3f5217324c70f"
AGENTMAIL_INBOX="ab-brain-bot@agentmail.to"
SEND_TO="abhay02delhi@gmail.com"
DATE=$(date +%Y-%m-%d)
MONTH=$(date +%m)
YEAR=$(date +%Y)
MONTH_NAME=$(date +%B)

# Read tracker
TOTAL_GIVEN=$(python3 -c "import json; d=json.load(open('$TRACKER')); print(d['daily']['total_questions_given'])")
TOTAL_COMPLETED=$(python3 -c "import json; d=json.load(open('$TRACKER')); print(d['daily']['total_questions_completed'])")
CURRENT_LECTURE=$(python3 -c "import json; d=json.load(open('$TRACKER')); print(d['current_lecture'])")

# Count completed this month
MONTH_COMPLETED=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
count = sum(1 for entry in d['completion_log'] if entry.get('completed') and entry.get('date_completed','').startswith('$YEAR-$MONTH'))
print(count)
")

# List completed this month
MONTH_COMPLETED_LIST=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
done = [entry for entry in d['completion_log'] if entry.get('completed') and entry.get('date_completed','').startswith('$YEAR-$MONTH')]
if done:
    for entry in done:
        print(f\"  ✅ {entry['question']} (L{entry['lecture']}) — {entry.get('date_completed','')}\")
else:
    print('  No questions completed this month')
")

# Group by lecture
LECTURE_BREAKDOWN=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
done = [entry for entry in d['completion_log'] if entry.get('completed') and entry.get('date_completed','').startswith('$YEAR-$MONTH')]
by_lecture = {}
for entry in done:
    lec = entry['lecture']
    if lec not in by_lecture:
        by_lecture[lec] = []
    by_lecture[lec].append(entry)
for lec in sorted(by_lecture.keys()):
    print(f'  📚 Lecture {lec}: {len(by_lecture[lec])} questions')
")

# Pending (all time)
PENDING=$(python3 -c "
import json
d=json.load(open('$TRACKER'))
pending = [entry for entry in d['completion_log'] if not entry.get('completed')]
if pending:
    print(f'  {len(pending)} questions remaining')
else:
    print('  All questions completed! 🎉')
")

EMAIL_TEXT="📈 DSA Monthly Report — $MONTH_NAME $YEAR
━━━━━━━━━━━━━━━━━━━━━━━━━
Report Date: $DATE
━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Overall Progress
• Questions Given: $TOTAL_GIVEN
• Completed: $TOTAL_COMPLETED
• Completion Rate: $(python3 -c "print(f\"{($TOTAL_COMPLETED*100//max($TOTAL_GIVEN,1))}%\")")
• Current Lecture: $CURRENT_LECTURE

━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Completed in $MONTH_NAME:
$MONTH_COMPLETED_LIST

━━━━━━━━━━━━━━━━━━━━━━━━━
📚 By Lecture:
$LECTURE_BREAKDOWN

━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Remaining:
$PENDING

━━━━━━━━━━━━━━━━━━━━━━━━━
Great work this month! Let's keep the momentum for next month. 💪"

EMAIL_HTML="<html>
<body style='font-family: sans-serif; background: #0d0d0d; color: #e0e0e0; padding: 20px;'>
<div style='max-width: 600px; margin: 0 auto;'>
<div style='border-bottom: 2px solid #fabd2f; padding-bottom: 12px; margin-bottom: 20px;'>
<h1 style='color: #fff; margin: 0;'>📈 DSA Monthly Report</h1>
<p style='color: #888; margin: 4px 0 0;'>$MONTH_NAME $YEAR — $DATE</p>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px;'>
<h3 style='color: #fabd2f; margin: 0 0 12px;'>📊 Overall Progress</h3>
<table style='width: 100%; color: #ccc; font-size: 14px;'>
<tr><td>Questions Given</td><td style='text-align: right; color: #fff; font-weight: bold;'>$TOTAL_GIVEN</td></tr>
<tr><td>Questions Completed</td><td style='text-align: right; color: #34a853; font-weight: bold;'>$TOTAL_COMPLETED</td></tr>
<tr><td>Completion Rate</td><td style='text-align: right; color: #fabd2f; font-weight: bold;'>$(python3 -c "print(f\"{($TOTAL_COMPLETED*100//max($TOTAL_GIVEN,1))}%\")")</td></tr>
<tr><td>Current Lecture</td><td style='text-align: right; color: #fabd2f; font-weight: bold;'>$CURRENT_LECTURE</td></tr>
</table>
</div>

<div style='background: #111122; border-radius: 8px; padding: 16px; margin-bottom: 16px; border-left: 3px solid #34a853;'>
<h3 style='color: #34a853; margin: 0 0 8px;'>✅ Completed in $MONTH_NAME</h3>
<pre style='color: #ccc; margin: 0; font-size: 13px; white-space: pre-wrap;'>$MONTH_COMPLETED_LIST</pre>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px; border-left: 3px solid #4a9eff;'>
<h3 style='color: #4a9eff; margin: 0 0 8px;'>📚 By Lecture</h3>
<pre style='color: #ccc; margin: 0; font-size: 13px; white-space: pre-wrap;'>$LECTURE_BREAKDOWN</pre>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px; border-left: 3px solid #fabd2f;'>
<h3 style='color: #fabd2f; margin: 0 0 8px;'>📋 Remaining</h3>
<pre style='color: #ccc; margin: 0; font-size: 13px; white-space: pre-wrap;'>$PENDING</pre>
</div>

<p style='color: #666; text-align: center; margin-top: 24px; font-size: 12px;'>Great work this month! Keep the momentum going! 💪</p>
</div>
</body>
</html>"

# Send email
curl -s -X POST "https://api.agentmail.to/v0/inboxes/$AGENTMAIL_INBOX/messages" \
  -H "Authorization: Bearer $AGENTMAIL_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"to\": [\"$SEND_TO\"],
    \"subject\": \"📈 DSA Monthly Report — $MONTH_NAME $YEAR\",
    \"text\": $(echo "$EMAIL_TEXT" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))"),
    \"html\": $(echo "$EMAIL_HTML" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")
  }"

echo "Monthly report email sent for $MONTH_NAME $YEAR"

# Write monthly markdown log
cat > "$DSA_DIR/progress/monthly/$YEAR-$MONTH.md" << EOF
# 📈 DSA Monthly Report — $MONTH_NAME $YEAR

**Report Date:** $DATE

## Overall Progress
- **Questions Given:** $TOTAL_GIVEN
- **Completed:** $TOTAL_COMPLETED
- **Completion Rate:** $(python3 -c "print(f\"{($TOTAL_COMPLETED*100//max($TOTAL_GIVEN,1))}%\")")
- **Current Lecture:** Lecture $CURRENT_LECTURE

## ✅ Completed in $MONTH_NAME
$MONTH_COMPLETED_LIST

## 📚 By Lecture
$LECTURE_BREAKDOWN

## 📋 Remaining
$PENDING

---

*Keep going! Next month will be even better! 💪*
EOF

echo "✓ Monthly log created: progress/monthly/$YEAR-$MONTH.md"
