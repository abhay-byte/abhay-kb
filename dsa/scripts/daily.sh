#!/bin/bash
# DSA Daily — sends 2 questions at 8am daily
# Reads from tracker.json & questions.json, picks 2 questions,
# sends email, updates tracker + daily log

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DSA_DIR="$(dirname "$SCRIPT_DIR")"
TRACKER="$DSA_DIR/tracker.json"
QUESTIONS="$DSA_DIR/questions.json"
AGENTMAIL_API_KEY="am_us_inbox_1f3e4c9f980cd74da03b8ac2bd4748ece495515d62f7b024c5d3f5217324c70f"
AGENTMAIL_INBOX="ab-brain-bot@agentmail.to"
SEND_TO="abhay02delhi@gmail.com"
DATE=$(date +%Y-%m-%d)
DAY_OF_WEEK=$(date +%u)  # 1=Mon, 7=Sun

# Read current state
CURRENT_LECTURE=$(python3 -c "import json; f=open('$TRACKER'); d=json.load(f); print(d['current_lecture']); f.close()")
TOTAL_GIVEN=$(python3 -c "import json; f=open('$TRACKER'); d=json.load(f); print(d['daily']['total_questions_given']); f.close()")
TOTAL_COMPLETED=$(python3 -c "import json; f=open('$TRACKER'); d=json.load(f); print(d['daily']['total_questions_completed']); f.close()")

# Get questions for current lecture
LECTURE_QUESTIONS=$(python3 -c "
import json
f=open('$QUESTIONS')
data=json.load(f)
for lec in data['lectures']:
    if lec['id'] == $CURRENT_LECTURE:
        print(json.dumps(lec))
        break
f.close()
")
LECTURE_TITLE=$(echo "$LECTURE_QUESTIONS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['title'])")
ALL_QS=$(echo "$LECTURE_QUESTIONS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d['questions']))")

# Count how many questions have been given from this lecture so far
QS_GIVEN=$(python3 -c "
import json
f=open('$TRACKER')
d=json.load(f)
lecture_key = f'lecture_{$CURRENT_LECTURE}'
count = sum(1 for entry in d['completion_log'] if entry['lecture'] == $CURRENT_LECTURE)
print(count)
f.close()
")

ALL_QS_COUNT=$(echo "$ALL_QS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d))")

# If all questions from current lecture are done, move to next
if [ "$QS_GIVEN" -ge "$ALL_QS_COUNT" ]; then
  CURRENT_LECTURE=$((CURRENT_LECTURE + 1))
  # Update tracker
  python3 -c "
import json
f=open('$TRACKER')
d=json.load(f)
d['current_lecture'] = $CURRENT_LECTURE
f.close()
json.dump(d, open('$TRACKER','w'), indent=2)
"
  QS_GIVEN=0
  # Get new lecture questions
  LECTURE_QUESTIONS=$(python3 -c "
import json
f=open('$QUESTIONS')
data=json.load(f)
for lec in data['lectures']:
    if lec['id'] == $CURRENT_LECTURE:
        print(json.dumps(lec))
        break
f.close()
")
  LECTURE_TITLE=$(echo "$LECTURE_QUESTIONS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['title'])")
  ALL_QS=$(echo "$LECTURE_QUESTIONS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d['questions']))")
  ALL_QS_COUNT=$(echo "$ALL_QS" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d))")
fi

# Pick 2 questions (next two not yet given from this lecture)
SELECTED=$(python3 -c "
import json
f=open('$TRACKER')
d=json.load(f)
f.close()

lecture_key = $CURRENT_LECTURE
given = [entry['question'] for entry in d['completion_log'] if entry['lecture'] == lecture_key]

all_qs = json.loads('$ALL_QS')
available = [q for q in all_qs if q not in given]
count = len(available)

if count == 0:
    print('__ALL_DONE__')
elif count == 1:
    print(json.dumps([available[0]]))
else:
    print(json.dumps(available[:2]))
")

if [ "$SELECTED" = "__ALL_DONE__" ]; then
  echo "All questions done for lecture $CURRENT_LECTURE. Moving to next."
  # Log this in daily file
  cat > "$DSA_DIR/progress/daily/$DATE.md" << EOF
# 📅 DSA Daily — $DATE

**Lecture:** $LECTURE_TITLE (L$CURRENT_LECTURE)

No new questions — all questions from this lecture completed!

**Total Given:** $TOTAL_GIVEN
**Total Completed:** $TOTAL_COMPLETED
EOF
  exit 0
fi

# Get the two questions
Q1=$(echo "$SELECTED" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[0])")
if [ "$(echo "$SELECTED" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d))")" -ge 2 ]; then
  Q2=$(echo "$SELECTED" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[1])")
else
  Q2="(none — only 1 question remaining)"
fi

# Update tracker
python3 -c "
import json
f=open('$TRACKER')
d=json.load(f)
d['daily']['total_questions_given'] += 2
d['daily']['last_given_date'] = '$DATE'
d['daily']['today_questions'] = ['$Q1', '$Q2']
# Add to completion log (marked not completed)
d['completion_log'].append({'lecture': $CURRENT_LECTURE, 'question': '$Q1', 'date_given': '$DATE', 'completed': false})
d['completion_log'].append({'lecture': $CURRENT_LECTURE, 'question': '$Q2', 'date_given': '$DATE', 'completed': false})
json.dump(d, open('$TRACKER','w'), indent=2)
"

# Read lecture notes content
LECTURE_FILE="$DSA_DIR/lectures/lecture-$(printf '%02d' $CURRENT_LECTURE).md"
LECTURE_NOTES=$(head -30 "$LECTURE_FILE" 2>/dev/null | tail -25)

# Build email content
TODAYS_TOTAL=$((TOTAL_GIVEN + 2))

EMAIL_TEXT="🧠 DSA Daily Practice — $DATE

━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Current Lecture: $LECTURE_TITLE (L$CURRENT_LECTURE)
━━━━━━━━━━━━━━━━━━━━━━━━━

Today's Questions:

1️⃣  $Q1
2️⃣  $Q2

━━━━━━━━━━━━━━━━━━━━━━━━━
📖 Lecture Notes Preview:
$LECTURE_NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Progress
• Questions Given: $TODAYS_TOTAL
• Questions Completed: $TOTAL_COMPLETED

✅ How to mark a question as done:
Just send me a message saying \"Done: <question name>\" or reply to this email

━━━━━━━━━━━━━━━━━━━━━━━━━
Keep going! 🚀"

EMAIL_HTML="<html>
<body style='font-family: sans-serif; background: #0d0d0d; color: #e0e0e0; padding: 20px;'>
<div style='max-width: 600px; margin: 0 auto;'>
<div style='border-bottom: 2px solid #fabd2f; padding-bottom: 12px; margin-bottom: 20px;'>
<h1 style='color: #fff; margin: 0;'>🧠 DSA Daily Practice</h1>
<p style='color: #888; margin: 4px 0 0;'>$DATE</p>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px;'>
<h2 style='color: #fabd2f; margin: 0 0 4px;'>📚 $LECTURE_TITLE</h2>
<p style='color: #888; margin: 0;'>Lecture $CURRENT_LECTURE</p>
</div>

<div style='background: #111122; border-radius: 8px; padding: 16px; margin-bottom: 16px; border-left: 3px solid #fabd2f;'>
<h3 style='color: #fff; margin: 0 0 12px;'>Today's Questions</h3>
<ol style='color: #ccc; margin: 0; font-size: 15px;'>
<li><strong style='color: #fff;'>$Q1</strong></li>
<li><strong style='color: #fff;'>$Q2</strong></li>
</ol>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px;'>
<h3 style='color: #fabd2f; margin: 0 0 8px;'>📖 Lecture Notes</h3>
<pre style='background: #0a0a1a; color: #c8c8e8; padding: 12px; border-radius: 6px; font-size: 12px; overflow-x: auto; white-space: pre-wrap;'>$(echo "$LECTURE_NOTES" | head -15)</pre>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; margin-bottom: 16px;'>
<h3 style='color: #fabd2f; margin: 0 0 8px;'>📊 Progress</h3>
<table style='width: 100%; color: #ccc; font-size: 14px;'>
<tr><td>Questions Given</td><td style='text-align: right; color: #fff; font-weight: bold;'>$TODAYS_TOTAL</td></tr>
<tr><td>Questions Completed</td><td style='text-align: right; color: #34a853; font-weight: bold;'>$TOTAL_COMPLETED</td></tr>
</table>
</div>

<div style='background: #1a1a1a; border-radius: 8px; padding: 16px; border-left: 3px solid #34a853;'>
<p style='color: #999; margin: 0; font-size: 13px;'>
✅ <strong style='color: #ccc;'>How to mark done:</strong> Reply to this email or message me with <code style='color: #fabd2f;'>Done: &lt;question name&gt;</code>
</p>
</div>

<p style='color: #666; text-align: center; margin-top: 24px; font-size: 12px;'>Keep going! 🚀</p>
</div>
</body>
</html>"

# Send email via AgentMail API
curl -s -X POST "https://api.agentmail.to/v0/inboxes/$AGENTMAIL_INBOX/messages" \
  -H "Authorization: Bearer $AGENTMAIL_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"to\": [\"$SEND_TO\"],
    \"subject\": \"🧠 DSA: $Q1 + $Q2 — $DATE\",
    \"text\": $(echo "$EMAIL_TEXT" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))"),
    \"html\": $(echo "$EMAIL_HTML" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")
  }"

echo "Email sent for $DATE: Q1='$Q1', Q2='$Q2'"

# Create daily markdown log
cat > "$DSA_DIR/progress/daily/$DATE.md" << EOF
# 📅 DSA Daily — $DATE

**Lecture:** $LECTURE_TITLE (Lecture $CURRENT_LECTURE)

## Today's Questions
1. $Q1
2. $Q2

## Status
- [ ] $Q1
- [ ] $Q2

## Notes
<!-- Add your notes or completion status here -->

---

**Total Given:** $TODAYS_TOTAL | **Completed:** $TOTAL_COMPLETED
EOF

echo "✓ Daily log created: progress/daily/$DATE.md"
