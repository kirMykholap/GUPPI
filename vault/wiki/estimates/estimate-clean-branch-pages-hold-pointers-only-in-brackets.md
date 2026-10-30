---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether the pages with core: true, the schema.yaml of each category and the files of .claude/ rendered from such pages hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --review prints no line on a pointer outside a bracket there and no bracket it removes holds a definition or the slug of a shipped rule that the sentence needs"
method: "by hand, at Retro: the lines of uv run --project .guppi guppi ship --allow-draft --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion"
checked: 2026-10-30
origin: raw/2026-10-14/0101/ledger.md#case-809
sprint: plugin
created: 2026-10-14
tags: [ci, plugin]
---

## Criterion

When:
At Retro of the session, `uv run --project .guppi guppi ship --allow-draft --review <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder, with a tag `prod-x.y.z` in the history of HEAD.

Then:
It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
**＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
**＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
**－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
**－** A line on a page with `core: true` that stands `draft` sets no exit code and is no part of this promise.
**－** A line on a file under `.guppi/guppi/` is no part of this promise.

## Result

2026-10-30, Retro of session 2005, tag prod-0.2.0 in the history of HEAD: uv run --project .guppi guppi ship --allow-draft --review into the empty folder scratchpad/review939 exit 0, 316 lines: 13 on pages with core: true that stand draft, and 303 lines "a bracket with words", none on a pointer outside a bracket; the 194 lines on vault/wiki/ and .claude/ read: each bracket holds pointers to cases, sessions, dates or the history of this repository that a pointer names, none the definition of a term its sentence needs or the slug of a core page naming the rule that sets it

## History

- 2026-10-14 created · [[decision-case-809]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0232/ledger.md#L1
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-30 updated: the Criterion replaced whole — the reading passes --allow-draft, so no draft page with core: true stops it · [[decision-case-939]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L48
