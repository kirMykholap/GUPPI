---
type: estimate
kind: QA
status: pending
target: "[[rule-settings]]"
purpose: The settings file is rendered whole from rule-settings and its three children, parses as JSON and loads at session start
method: "make test-harness, then by hand at a later session start: json.load on the rendered file, guppi render --check, and the session-start line in the day's event log"
origin: raw/2026-09-12/ledger.md#case-85.2
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Criterion

When:
`uv run guppi render` writes `.claude/settings.json` from `rule-settings` and its children, and the next session starts from that file.

Then:
The file is the Render of `rule-settings`, and the text of each child replaces its `<!-- child -->` line in the order of `children`: `rule-default-mode`, `rule-permissions`, `rule-hook-registry`. That order is the order of the keys in the file.
**＋** The file parses as JSON, and `uv run guppi render --check` exits 0.
**＋** The next session start writes its `session-start` line into `vault/raw/<date>/event_log.md`, from the hooks of the rendered file.
**－** `rule-settings` holds no rule of its own about what a hook or a permission may be.

## Result

session M start 07:30:30: .claude/settings.json rendered by the librarian of session L parses as JSON, guppi render --check exits 0, and the session-start line of fde37e7c was written from the rendered file

## History

- 2026-09-12 created · [[decision-case-85.2]]
- 2026-09-14 updated: Method names make test-harness (case 112.3) · [[decision-case-112.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L35
- 2026-09-29 updated: the Criterion replaced whole — the block 85.2 as When and Then, the line on its own reading into the lines it names; purpose and method set, Context and Method out (case 498.3) · [[decision-case-498.3]]
