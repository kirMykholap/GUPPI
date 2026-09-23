---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether the report of /retro holds each fact once — the ratifications in the closing list only, the unticked boxes of the Spec inside the list of what is not done
method: one reading by hand at the first /retro after the render, recorded in the estimate line
origin: raw/2026-09-23/1355/ledger.md#case-376
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes; the agent writes the opening message and the close.

Then:
The opening message holds one numbered list of what is not done: the unticked boxes of `raw/<date>/<hi HHMM>/spec.md` per Case, each marked as waiting for the librarian or as debt, and what the agent noticed during Work Mode.
**－** The opening message holds no list of the ratifications.
**＋** The close holds every ratification of the session, one line per Case, from `uv run guppi tail` grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted.
**＋** The close holds what got done.
**＋** The close holds what is not done: the numbers of the opening list, each with the end it took.
**－** No ratification and no box is named twice in the report.

## History

- 2026-09-23 created · [[decision-case-376]]
