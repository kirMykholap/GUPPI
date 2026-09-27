---
type: estimate
kind: QA
status: failed
target: "[[rule-retro]]"
purpose: Whether the report of /retro holds each fact once — the ratifications in the closing list only, the unticked boxes of the Spec inside the list of what is not done
method: one reading by hand at the first /retro after the render, recorded in the estimate line
checked: 2026-09-27
origin: raw/2026-09-23/1355/ledger.md#case-376
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes; the agent writes the opening message and the close.

Then:
The opening message holds one numbered list of what is not done: the unticked boxes of `raw/<date>/<hi HHMM>/spec.md` per Case, each marked as waiting for the librarian, as waiting for a later session, or as debt, and what the agent noticed during Work Mode.
**＋** A `read` line is marked as waiting for a later session when this session creates or updates its slug — by a decision line of that slug, or by an `update` that renames a page to it; another `read` line without its line in the Tail is debt.
**－** The opening message holds no list of the ratifications.
**＋** The close holds every ratification of the session, one line per Case, from `uv run guppi tail` grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted.
**＋** The close holds what got done.
**＋** The close holds what is not done: the numbers of the opening list, each with the end it took.
**－** No ratification and no box is named twice in the report.

## Result

2026-09-27, by hand, the /retro of session 1819: the opening list named the unticked boxes per Case (update and create lines of each page), the close named every ratification per Case with the same pages again, and "what got done" and "what is not done" repeated parts of the opening list; the person's complaint: the retro repeats the not-done part several times and needs one standard, to be discussed in the next session

## History

- 2026-09-23 created · [[decision-case-376]]
- 2026-09-25 updated: the Criterion replaced whole — a third mark in the opening list: a read line whose reading waits for a later session (case 428.4) · [[decision-case-428.4]]
- 2026-09-27 status: pending → failed · raw/2026-09-27/1819/ledger.md#L39
