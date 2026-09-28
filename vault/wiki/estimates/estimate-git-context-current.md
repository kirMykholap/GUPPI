---
type: estimate
kind: QA
status: pending
target: "[[rule-git-context]]"
purpose: At /hi the context holds the pull, the render sync, the branch and the status; a failing pull does not stop the skill, and no pull runs later
method: by hand at the /hi of the next session on the current remote, and that session's event_log.md read at its close for a later git pull, written into the estimate line
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, git]
---

## Criterion

When:
The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the four commands of `rule-git-context`.

Then:
The context holds `Pull:` with the output of `git pull --ff-only`, then `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
**＋** A pull that fails prints its message on the `Pull:` line, and the skill still completes.
**－** No `git pull` runs later in the session: `vault/raw/<date>/event_log.md` shows none after the `hi` line.

## Result

block 115 at the /hi of 10:29: the `Render:` line is present after `Pull:` and empty on a clean tree; branch and status in context; the failing pull shows its message and the skill completed

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-14 criterion: case 115 added · [[decision-case-115]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L1
- 2026-09-28 updated: the Criterion replaced whole — one When and Then; the Frontier item left to estimate-hi-writes-frontier, the block bookkeeping out; purpose and method set, Context and Method out (case 485.3) · [[decision-case-485.3]]
