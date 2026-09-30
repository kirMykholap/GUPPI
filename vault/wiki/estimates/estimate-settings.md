---
type: estimate
kind: QA
status: passed
target: "[[rule-settings]]"
purpose: The settings file is rendered whole from rule-settings and its children, parses as JSON and loads at session start
method: "make test-harness, then by hand at a later session start: json.load on the rendered file, guppi render --check, and the session-start line in the day's event log"
checked: 2026-09-30
origin: raw/2026-09-12/ledger.md#case-85.2
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Criterion

When:
`uv run guppi render` writes `.claude/settings.json` from `rule-settings` and its children, and the next session starts from that file.

Then:
The file is the Render of `rule-settings`, and the text of each child replaces its `<!-- child -->` line in the order of `children`: `rule-default-mode`, `rule-permissions`, `rule-hook-registry`, `rule-python-utf8`. That order gives the order of the top-level keys of the file: `permissions`, `hooks`, `env`.
**＋** The file parses as JSON, and `uv run guppi render --check` exits 0.
**＋** The next session start writes its `session-start` line into `vault/raw/<date>/event_log.md`, from the hooks of the rendered file.
**－** `rule-settings` holds no rule of its own about what a hook, a permission or a variable of the environment may be.

## Result

2026-09-30, make test-harness: 116 passed; json.load of .claude/settings.json gives the keys permissions, hooks, env in that order and env {PYTHONUTF8: 1}; uv run guppi render --check exit 0; vault/raw/2026-09-30/event_log.md line 994: 05:13:30 96eeee58 session-start startup

## History

- 2026-09-12 created · [[decision-case-85.2]]
- 2026-09-14 updated: Method names make test-harness (case 112.3) · [[decision-case-112.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L35
- 2026-09-29 updated: the Criterion replaced whole — the block 85.2 as When and Then, the line on its own reading into the lines it names; purpose and method set, Context and Method out (case 498.3) · [[decision-case-498.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L48
- 2026-09-30 updated: the Criterion replaced whole — a fourth child, rule-python-utf8, and the env key after hooks · [[decision-case-534.2]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1306/ledger.md#L44
