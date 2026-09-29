---
type: estimate
kind: QA
status: passed
target: "[[rule-github-issues]]"
purpose: At /hi the context holds the open issues or the reason gh gives for none, and the skill completes
method: by hand at the /hi of the next session, in the current gh state, written into the estimate line
checked: 2026-09-29
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, github]
---

## Criterion

When:
The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs `gh issue list --limit 5`.

Then:
The line `Open issues:` holds the list of open issues, or the message of `gh` itself that names why there is none.
**＋** Neither answer stops `/hi`: the blocks after the line still run.

## Result

2026-09-29, by hand at the /hi of session 1134: the Open issues line held the message of gh itself (not logged in, run gh auth login), and the Tail block after it still ran

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; purpose and method set, Context and Method out (case 485.4) · [[decision-case-485.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L43
