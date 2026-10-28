---
type: estimate
kind: QA
status: failed
target: "[[rule-clean-branch]]"
purpose: Whether the rules, the entities and CLAUDE.md of the clean version, and the purpose and the method of each shipped Estimate, describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the Criterion of the shipped Estimates hold only there
method: "by hand, after the librarian's run of session 1907, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line"
checked: 2026-10-17
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
**＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that names a past session of it, a line of its sprint page, its machine or a file that the clean version does not hold.
**＋** No sentence of the `purpose` or the `method` of a shipped Estimate holds only in the repository of GUPPI, such as a `method` that waits for a moment of a past session of it.
**＋** The reader lists, in the estimate line, each sentence of the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
**－** A sentence of the `## Criterion` of a shipped Estimate on that list does not fail this promise.
**－** The History of a page, a sample in a code span or a fenced block, the values of the Render of `rule-guppi-config` and the read rules of the Render of `rule-permissions`, which the setup Case of `rule-morph` sets, are no part of this promise.

## Result

2026-10-17, /hi of session 1805: tag prod-0.2.0 in the history of HEAD; uv run --project .guppi guppi ship --allow-draft into an empty scratchpad folder (exit 0, ten core draft pages named); each sentence of its 81 rules, 3 entities and CLAUDE.md, and the purpose, method and Criterion of its 257 Estimates, read whole by seven reading agents, no keyword search; entity-guppi describes GUPPI as a harness and a vault, rule-language and rule-case-build name the languages by role; the flags of the reading of 2104 on rule-bash-guard, rule-claude-md, rule-documentation, rule-guppi-config, rule-spec-box, rule-vault-layout and rule-retro are gone; it fails on sentences true only in the repository of GUPPI: rule-git-context (How it works, the git commands that stood until a first /hi stopped), rule-harness (Purpose, the plugin install skill among fourteen, rule-plugin-install not shipped), rule-morph (Purpose, rule-plugin-install and rule-clean-branch not shipped), rule-one-judgment-one-implementation (Purpose, an Insight not shipped), rule-page-generation (Purpose, /merge-main not shipped), rule-permissions (Purpose, c--PROJECTS-GUPPI and the folder of the repository of GUPPI), rule-ratification (Render, PLAIN_SPRINTS migration and plugin, case 785.1), rule-decisions-schema (Cases from before sprint ids, the former schema.md), rule-lessons-schema (origin date form before 2026-09-13), rule-search-leaves-out-decisions (Purpose, trials of GUPPI and a lesson not shipped); purpose or method: estimate-generate-writes-rules-from-applies-to (entity-sprint carries rules [rule-sprint]), estimate-skill-sprint-close-leads-the-closing-session (entity-sprint-migration under vault/archive/), estimate-sprint-close-moves-old-event-logs (a root .gitignore); doubtful: rule-skill-hi, rule-retro-onward, rule-spec-reconcile, rule-skill-grill-me, rule-ledger-write, rule-page-read, rule-event-log (reasons from past sessions), rule-rules-schema and rule-estimates-schema (the Makefile), rule-case-protocol and rule-guppi-package (guppi ship), the origin date form and the former schema.md in the other schemas, entity-glossary (retired terms), estimate-ratification-case-id-carries-the-sprint (purpose), estimate-spec-capture-appends (method); Criterion sentences true only in GUPPI: estimate-claude-md-rendered, estimate-case-build-checks-the-finished-case, estimate-case-build-reads-by-need-and-in-parts, estimate-case-protocol-case-form, estimate-case-build-reads-the-test-code-over-a-changed-text, estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check, estimate-case-check-requires-each-question-of-the-rounds, estimate-case-check-sends-back-a-faulty-case, estimate-case-check-sends-back-a-case-number-held-by-another-agent, estimate-compact-recall-reloads, estimate-event-log-records, estimate-git-context-current, estimate-glossary-checks-the-file, estimate-guppi-package-runs-from-its-own-folder, estimate-permissions, estimate-orchestration-asks-in-the-grill-me-shape, estimate-orchestration-forwards-a-discussion-question, estimate-orchestration-batches-cases-out-at-once, estimate-orchestration-signs-a-batch-together, estimate-orchestration-defer-example-passes-the-hook, estimate-prespec-hook-reports-a-pointer-outside-a-bracket, estimate-materialize-marks-exists, estimate-prespec-catches-a-command-line-off-form, estimate-one-judgment-one-implementation-followed, estimate-ratification-case-id-carries-the-sprint, estimate-skill-sprint-close-leads-the-closing-session, estimate-sprint-checks-the-file, estimate-tests-clock-pinned, estimate-sprint-close-moves-old-event-logs, estimate-where-to-stop-stops-only-on-its-conditions, estimate-synthesis-keeps-actioned-by-the-mark, estimate-sprint-close-next-session-opens-the-sprint, estimate-synthesis-clusters

## History

- 2026-10-15 created · [[decision-case-822.7]]
- 2026-10-15 updated: the method waits for a tag prod-x.y.z, without which guppi ship writes nothing · [[decision-case-824]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0342/ledger.md#L2
- 2026-10-16 updated: read again after the three sentences are rewritten; the method waits for the librarian's run of this session and reads each sentence whole · [[decision-case-856.1]]
- 2026-10-17 status: pending → failed · raw/2026-10-16/2104/ledger.md#L2
- 2026-10-17 deferred · [[decision-case-874]]
- 2026-10-17 defer by decision-case-874 superseded · [[decision-case-875]]
- 2026-10-17 updated: the Criterion replaced whole — the purpose and the method of the shipped Estimates hold no sentence true only in the repository of GUPPI, and the read rules of rule-permissions are exempt · [[decision-case-875]]
- 2026-10-17 status: pending → failed · raw/2026-10-17/1805/ledger.md#L1
- 2026-10-26 deferred · [[decision-case-891]]
- 2026-10-28 defer by decision-case-891 superseded · [[decision-case-893.2]]
- 2026-10-28 updated: put-off taken up — the clean version keeps the event logs out of git by vault/.gitignore; the method waits for the librarian's run of session 1907 · [[decision-case-893.2]]
