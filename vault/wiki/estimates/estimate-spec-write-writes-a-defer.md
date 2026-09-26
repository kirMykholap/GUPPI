---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: The Stop hook writes a deferred Case into the Spec as the reply showed it
method: uv run pytest tests/test_ratified.py -k defer, then by hand the first defer the person asks for after the change
checked: 2026-09-26
origin: raw/2026-09-25/1228/ledger.md#case-421.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

Then:
The hook writes that Case under `## Deferred` of the plan file while Plan Mode lasts, and of `raw/<date>/<hi HHMM>/spec.md` once that file stands, at Retro: the heading, `context`, `problem` and the `then` block as the reply shows them.
**＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
**＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
**＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
**－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
**－** The ratified copy `<plan>.ratified.md` gets no defer, and the check after the write does not run on it.

## Result

2026-09-26, `uv run pytest tests/test_ratified.py -k defer`: 9 passed; live, Case 442 of session 1745: the Stop hook wrote its heading, context, problem and then block under ## Deferred of the plan file as the reply at 22:00:17 showed them, and the ratified copy holds no Case 442

## History

- 2026-09-25 created · [[decision-case-421.1]]
- 2026-09-26 updated: the Criterion replaced whole — a key of a defer item outside the keys item_keys gives it is refused (case 436.3) · [[decision-case-436.3]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L33
