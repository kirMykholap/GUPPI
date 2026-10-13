---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: "Whether the pages with core: true, the schema.yaml of each category and the files of .claude/ rendered from such pages hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --review prints no line on a pointer outside a bracket there and no bracket it removes holds a definition or the slug of a shipped rule that the sentence needs"
method: "by hand, after the librarian's run that applies case 809: the lines of uv run guppi ship --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion"
origin: raw/2026-10-14/0101/ledger.md#case-809
sprint: plugin
created: 2026-10-14
tags: [ci, plugin]
---

## Criterion

When:
`uv run guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

Then:
It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
**＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
**＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
**－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
**－** A line on a file under `guppi/` is no part of this promise.

## History

- 2026-10-14 created · [[decision-case-809]]
