---
type: estimate
kind: QA
status: pending
target: "[[rule-github-issues]]"
purpose: At /hi the context holds the open issues or the reason gh gives for none, and the skill completes
method: by hand at the /hi of the next session, in the current gh state, written into the estimate line
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

Passing. `gh`'s own message (`To get started with GitHub CLI, please run: gh auth
login`) was in context and the skill completed (2026-09-09, session B).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; purpose and method set, Context and Method out (case 485.4) · [[decision-case-485.4]]
