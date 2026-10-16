---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether the rules, the entities and CLAUDE.md of the clean version describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the shipped Estimates hold only there
method: "by hand, after the librarian's run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence that holds only in the repository of GUPPI listed in the estimate line (the session of case 856)"
checked: 2026-10-16
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

## Result

2026-10-16, /hi of session 0342: `uv run --project .guppi guppi ship --allow-draft` into an empty scratchpad folder, tag `prod-0.2.0` in the history of HEAD, then a keyword grep of its rules, entities and CLAUDE.md outside History; `entity-guppi` describes GUPPI as a harness and a vault beside the product, and `rule-language` and `rule-case-build` name the languages by role; it fails on three sentences true only in the repository of GUPPI: the `core` field of the Render of `rule-rules-schema` and of `rule-entities-schema` ("a page without it stays in this repository only") and `rule-ratification` ("the sprints `migration` and `plugin` keep that form to their close"); shipped Estimates with such sentences: `estimate-skill-sprint-close-migration-merged-into-main` (purpose, method, Criterion), and the method of `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-decisions` and `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` (`--sprint migration` over the live vault)

## History

- 2026-10-15 created · [[decision-case-822.7]]
- 2026-10-15 updated: the method waits for a tag prod-x.y.z, without which guppi ship writes nothing · [[decision-case-824]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0342/ledger.md#L2
- 2026-10-16 updated: read again after the three sentences are rewritten; the method waits for the librarian's run of this session and reads each sentence whole · [[decision-case-856.1]]
