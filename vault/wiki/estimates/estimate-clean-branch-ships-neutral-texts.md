---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether the rules, the entities and CLAUDE.md of the clean version describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the shipped Estimates hold only there
method: "by hand, after a tag prod-x.y.z stands in the history of HEAD and after the librarian's run of the session that set this method: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and the pages and the files it wrote read against the Criterion, each sentence that holds only in the repository of GUPPI listed in the estimate line (the session of case 824)"
origin: raw/2026-10-15/0553/ledger.md#case-822.7
sprint: plugin
created: 2026-10-15
tags: [plugin, ci]
---

## Criterion

When:
Someone reads the pages and the files of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

Then:
`entity-guppi` describes GUPPI as a harness and a vault, and not as the thing that the project builds.
**＋** `rule-language` and `rule-case-build` name the language of the repository and the language of the chat by their role, not as English and Russian.
**＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that takes its repository on GitHub or its languages for those of the project.
**＋** The reader lists, in the estimate line, each sentence of the `purpose`, the `method` and the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
**－** A sentence of a shipped Estimate on that list does not fail this promise.
**－** The History of a page, a sample in a code span or a fenced block, and the values of the Render of `rule-guppi-config` are no part of this promise.

## History

- 2026-10-15 created · [[decision-case-822.7]]
- 2026-10-15 updated: the method waits for a tag prod-x.y.z, without which guppi ship writes nothing · [[decision-case-824]]
