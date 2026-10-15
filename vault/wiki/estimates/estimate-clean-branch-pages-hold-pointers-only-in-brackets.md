---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether the pages with core: true, the schema.yaml of each category and the files of .claude/ rendered from such pages hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --review prints no line on a pointer outside a bracket there and no bracket it removes holds a definition or the slug of a shipped rule that the sentence needs"
method: "by hand, after the librarian's run that applies case 809: the lines of uv run --project .guppi guppi ship --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion"
checked: 2026-10-14
origin: raw/2026-10-14/0101/ledger.md#case-809
sprint: plugin
created: 2026-10-14
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

Then:
It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
**＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
**＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
**－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
**－** A line on a file under `.guppi/guppi/` is no part of this promise.

## Result

2026-10-14, session 0232, uv run guppi ship --review into an empty temporary folder: exit 0, 100 lines, every one "a bracket with words", 0 on a pointer outside a bracket; 31 on guppi/ (outside the promise), 69 on vault/wiki/ (the schema.yaml of six categories, rule pages, entity-glossary, orchestration.md), 0 on .claude/; the bracket text of all 69 read, and the whole sentence of 17 of them: each bracket holds pointers with the history, the session or the date they name, none the definition of a term or the slug of a core rule its sentence names as its source

## History

- 2026-10-14 created · [[decision-case-809]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0232/ledger.md#L1
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
