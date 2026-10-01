---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: The Stop hook writes a deferred Case into the Spec as the reply showed it
method: uv run pytest tests/test_ratified.py -k defer, then by hand the first defer the person asks for after the change
checked: 2026-10-01
origin: raw/2026-09-25/1228/ledger.md#case-421.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

Then:
The hook writes that Case under `## Deferred` of the plan file while `spec.md` in the session's folder does not stand, and of that `spec.md` once it stands: the heading, `context`, `problem` and the `then` block as the reply shows them.
**＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
**＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
**＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
**＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
**－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
**－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
**－** The check after the write does not run on the Case.

## Result

2026-10-01, uv run pytest tests/test_ratified.py -k defer: 13 passed, 76 deselected; by hand, the seven short-form defers 570 to 576 of session 1237, shown in the reply of 14:08:36 with one LEDGER block (ledger lines 21-27): each stands under the Deferred heading of the plan file linear-soaring-fairy.md (line 374, 7 Case headings) and of raw/2026-10-01/1237/spec.md (line 376), each with its heading, context, problem and a then fence holding one defer item with its slug; the agent wrote none of them, and the reading of estimate-case-protocol-defers-in-one-reply in the same session (ledger line 31) records that the Spec hook wrote the seven; not exercised: an error of the hook on a malformed line

## History

- 2026-09-25 created · [[decision-case-421.1]]
- 2026-09-26 updated: the Criterion replaced whole — a key of a defer item outside the keys item_keys gives it is refused (case 436.3) · [[decision-case-436.3]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L33
- 2026-09-29 updated: the Criterion replaced whole — a then block that holds a YAML comment is refused (case 521.1) · [[decision-case-521.1]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0138/ledger.md#L6
- 2026-09-30 updated: the Criterion replaced whole — a defer goes into spec.md once it stands, with no Retro moment; the clause on the ratified copy dropped (case 542) · [[decision-case-542]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L41
- 2026-10-01 deferred · [[decision-case-564]]
- 2026-10-01 deferred · [[decision-case-573]]
- 2026-10-01 status: failed → passed · raw/2026-10-01/1441/ledger.md#L21
