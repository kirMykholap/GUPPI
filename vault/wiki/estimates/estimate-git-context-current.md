---
type: estimate
kind: QA
status: pending
target: rule-git-context
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, git]
---

## Context

The pull is the step most likely to fail here, and on 2026-09-09 it is expected to: the
remote is another repository and the branch has no upstream. The check is that the failure
is visible and harmless, not that the pull succeeds.

## Criterion

Branch and short status are in context; a failing pull shows its message there and the
skill still completes; no pull happens later in the session.

### case 115

When:
The person invokes `/hi`.

Then:
After the `Pull:` line the context holds a `Render:` line with the output of `uv run guppi render --sync`: a diff per governed file that differed and was written, or nothing.
**＋** A diff on that line is a Frontier item, as the one of the session start is.
**＋** `estimate-git-context-current` gets a `### case 115` block, `pending`; read at the next `/hi` after the render: the `Render:` line is present and empty on a clean tree.
**－** `{supersedes:case 106}`: `decision-case-106` is superseded, `rule-skill-hi` loses `deferred_by`.

## Method

One reading at a session start, by hand, on the current remote.

## Result

Passing. `Branch: migration`, an empty `Status:` and the pull's own message (`There is
no tracking information for the current branch`) were in context; the skill completed;
no pull happened later in the session (2026-09-09, session B).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-14 criterion: case 115 added · [[decision-case-115]]
