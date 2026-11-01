---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether guppi check prints no ref line for lesson-ledger-reading-writes-a-bare-wikilink once the bare link of its root cause stands in a code span, in the section and the field, the rest of that page as it stood but the line its History gains
method: "by hand, after the librarian's run that applies the update of lesson-ledger-reading-writes-a-bare-wikilink: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/lessons/lesson-ledger-reading-writes-a-bare-wikilink.md, the diff of the Root cause and the root_cause field, one line added to the History, and of no other field or section, read against the Criterion, both outputs in the estimate line"
origin: raw/2026-11-01/0141/ledger.md#case-978
sprint: plugin
created: 2026-11-01
tags: [sprint, harness]
once: true
---

## Criterion

When:
`uv run --project .guppi guppi check` runs the lint of `.guppi/guppi/lint.py` over the live pages of `vault/wiki/`, after the librarian's run that applies the `update` of `lesson-ledger-reading-writes-a-bare-wikilink`.
**＋** The last change of the file of `lesson-ledger-reading-writes-a-bare-wikilink` is read by `git log -p -1` on its path.

Then:
It prints no `ref` line for `lesson-ledger-reading-writes-a-bare-wikilink`.
**＋** The `## Root cause` and the field `root_cause` of `lesson-ledger-reading-writes-a-bare-wikilink` hold `[[slug]]` inside a code span, and the rest of their text as it stood.
**－** The `## Trigger`, the status and the other fields of `lesson-ledger-reading-writes-a-bare-wikilink` do not change, and its `## History` changes only by the line the update appends.

## History

- 2026-11-01 created · [[decision-case-978]]
