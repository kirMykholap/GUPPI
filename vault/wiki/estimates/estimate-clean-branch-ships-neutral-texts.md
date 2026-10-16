---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether the rules, the entities and CLAUDE.md of the clean version, and the purpose and the method of each shipped Estimate, describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the Criterion of the shipped Estimates hold only there
method: "by hand, after the librarian's run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line"
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
**＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that names a past session of it, a line of its sprint page, its machine or a file that the clean version does not hold.
**＋** No sentence of the `purpose` or the `method` of a shipped Estimate holds only in the repository of GUPPI, such as a `method` that waits for a moment of a past session of it.
**＋** The reader lists, in the estimate line, each sentence of the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
**－** A sentence of the `## Criterion` of a shipped Estimate on that list does not fail this promise.
**－** The History of a page, a sample in a code span or a fenced block, the values of the Render of `rule-guppi-config` and the read rules of the Render of `rule-permissions`, which the setup Case of `rule-morph` sets, are no part of this promise.

## Result

2026-10-16, /hi of session 2104: tag prod-0.2.0 in the history of HEAD; uv run --project .guppi guppi ship --allow-draft into an empty scratchpad folder; each sentence of its 81 rules, 3 entities and CLAUDE.md, and the purpose, method and Criterion of its 257 Estimates, read whole by seven reading agents, no keyword search; entity-guppi describes GUPPI as a harness and a vault beside the product, and rule-language and rule-case-build name the languages by role (CLAUDE.md holds English and Russian as the values of rule-guppi-config); the three sentences of the reading of session 0342 are gone; it fails on sentences true only in the repository of GUPPI: rule-spec-box and rule-vault-layout (Purpose, entity-sprint-migration), rule-morph (Purpose, a line of the Backlog of entity-sprint-plugin and its milestone The plugin), rule-guppi-config (Purpose, a line of the Backlog of entity-sprint-plugin), rule-documentation (Render, the Makefile as a file of the scripts), rule-bash-guard (Purpose, "this Windows machine" and sessions H, L, M), rule-claude-md (Purpose, how CLAUDE.md was written before the page), rule-permissions (Render, Read of ~/.claude/projects/c--PROJECTS-GUPPI); doubtful: rule-decisions-schema (Cases and pages from before sprint ids), the origin date form before 2026-09-13 in four schemas, rule-retro ("gh is not available"), and reasons drawn from GUPPI's own sessions in rule-skill-hi, rule-tests-clock-pinned, rule-shell-write-check, rule-python-utf8, rule-powershell-guard and rule-page-read; shipped Estimates with such sentences: estimate-ratification-case-id-carries-the-sprint, estimate-skill-sprint-close-leads-the-closing-session, estimate-sprint-close-takes-the-readings-in-groups (GUPPI's sprints and a dated session folder), estimate-sprint-checks-the-file, estimate-tests-clock-pinned, estimate-glossary-checks-the-file (the Makefile), estimate-ask-query-before-a-create, estimate-guppi-config-fills-the-languages, estimate-orchestration-asks-in-the-grill-me-shape, estimate-orchestration-forwards-a-discussion-question, estimate-orchestration-shows-the-built-case (English and Russian by name), estimate-case-build-reads-the-test-code-over-a-changed-text, estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check (Insights and Decisions of GUPPI), estimate-claude-md-rendered (the description of GUPPI), estimate-git-context-current (the GitHub remote of GUPPI), estimate-guppi-package-runs-from-its-own-folder (the root, the Makefile and prod.yml of GUPPI), estimate-one-judgment-one-implementation-followed (code in .guppi/guppi/), estimate-permissions (c--PROJECTS-GUPPI), estimate-sprint-close-moves-old-event-logs (a root .gitignore); a method tied to one past session of GUPPI: estimate-hi-no-read-calls, estimate-orchestration-acknowledges-the-opening-with-the-frontier, estimate-orchestration-marks-each-round-of-a-batch, estimate-orchestration-sets-off-each-reply-of-case-guppi, estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter, estimate-prespec-catches-a-command-line-off-form, estimate-prespec-gathers-the-answers-after-findings, estimate-render-harness-ticks-the-spec, estimate-skill-sprint-open-asks-the-opening-questions, estimate-skill-sprint-open-refuses-a-taken-sprint-id, estimate-skill-sprint-open-merges-the-closed-sprint-branch, estimate-sprint-close-next-session-opens-the-sprint, estimate-case-build-answers-what-done-means, estimate-case-build-finds-an-existing-judgment, estimate-case-build-judges-options-against-the-broken-rule, estimate-case-build-offers-a-page-for-code-no-page-covers, estimate-case-build-reads-the-last-output-of-a-check, estimate-case-example-passes-the-check, estimate-generate-writes-rules-from-applies-to

## History

- 2026-10-15 created · [[decision-case-822.7]]
- 2026-10-15 updated: the method waits for a tag prod-x.y.z, without which guppi ship writes nothing · [[decision-case-824]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0342/ledger.md#L2
- 2026-10-16 updated: read again after the three sentences are rewritten; the method waits for the librarian's run of this session and reads each sentence whole · [[decision-case-856.1]]
- 2026-10-17 status: pending → failed · raw/2026-10-16/2104/ledger.md#L2
- 2026-10-17 deferred · [[decision-case-874]]
- 2026-10-17 defer by decision-case-874 superseded · [[decision-case-875]]
- 2026-10-17 updated: the Criterion replaced whole — the purpose and the method of the shipped Estimates hold no sentence true only in the repository of GUPPI, and the read rules of rule-permissions are exempt · [[decision-case-875]]
