---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether the rules, the entities and CLAUDE.md of the clean version, and the purpose and the method of each shipped Estimate, describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the Criterion of the shipped Estimates hold only there
method: "by hand, after the librarian's run of the session that replaces this Criterion, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line"
checked: 2026-10-29
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
**＋** A `method` that waits for a kind of moment that comes again in any project, such as the Retro of the session that changes its rule or the Spec that changes it, holds.
**＋** The reader lists, in the estimate line, each sentence of the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
**－** A sentence that holds as it reads in a project that installed GUPPI does not fail this promise, such as one that states its condition, in the repository of GUPPI or where the module of the command `ship` stands, or one that says what `guppi ship` did to the files the project holds.
**－** A sentence of the `## Criterion` of a shipped Estimate on that list does not fail this promise.
**－** The History of a page, a sample in a code span or a fenced block, the values of the Render of `rule-guppi-config` and the read rules of the Render of `rule-permissions`, which the setup Case of `rule-morph` sets, are no part of this promise.

## Result

2026-10-29, Plan Mode of session 0327: git tag --merged HEAD prints prod-0.2.0, prod-1, prod-2; uv run --project .guppi guppi ship --allow-draft into an empty scratchpad folder (exit 0, ten core draft pages named); each file of its 82 rules, 3 entities, CLAUDE.md and 265 Estimates read whole by five reading agents, no keyword search; entity-guppi describes GUPPI as a harness and a vault, rule-language and rule-case-build name the languages by role; the /merge-main and /pr-review sentences of 2312 now stand conditional; it fails on sentences true only in the repository of GUPPI: entity-guppi (purpose and Purpose name entity-guppi-repository), rule-case-protocol (Language: guppi ship removes the bracket), rule-entities-schema and rule-estimates-schema (origin, sprint, core: guppi ship; "no Estimate of the repository that builds that version carries it"), rule-guppi-package (guppi ship writes no pyproject.toml), rule-ratification (PLAIN_SPRINTS migration and plugin), rule-rules-schema (the Makefile filter, guppi ship); method tied to a moment of a past session of GUPPI ("the session that changes it", "the new Render", "the next session", "the Spec that changes it"): estimate-prespec-gathers-the-answers-after-findings, estimate-prespec-reconciles, estimate-retro-loads, estimate-where-to-stop-stops-only-on-its-conditions, estimate-work-mode-takes-the-work-readings, estimate-spec-reconcile-refuses-an-edit-of-the-plan, estimate-skill-sprint-open-merges-the-closed-sprint-branch, estimate-handoff-holds-each-fact-once, estimate-hi-takes-its-readings, estimate-internal-context-loaded, estimate-language-followed, estimate-ledger-tail, estimate-one-judgment-one-implementation-followed, estimate-orchestration-asks-in-the-grill-me-shape, estimate-orchestration-batches-cases-out-at-once, estimate-orchestration-defers-in-one-reply, estimate-orchestration-rechecks-a-sibling-after-a-joint-send, estimate-orchestration-says-when-a-rendered-change-lands, estimate-orchestration-shows-the-clean-cases-of-a-batch-first, estimate-orchestration-signs-a-batch-together, estimate-orchestration-takes-back-a-ratified-case, estimate-permissions, estimate-brief-carries-the-run-facts, estimate-brief-written, estimate-case-build-checks-the-finished-case, estimate-case-build-goes-on-after-a-compaction, estimate-case-build-reads-a-prompt-fact-at-its-source, estimate-case-build-reads-by-need-and-in-parts, estimate-case-build-reads-no-sibling-file-mid-send, estimate-case-build-reads-the-code-it-states, estimate-case-build-reads-the-test-code-over-a-changed-text, estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check, estimate-case-build-writes-the-case, estimate-context-size-shown-after-each-reply (the VS Code chat); doubtful: rule-lint (guppi ship --check, conditional), rule-page-generation and rule-vault-layout (the merge of main with no condition on /merge-main), rule-spec-reconcile ("until the writer is live"), rule-spec-box ("a second part"), rule-work-mode ("not decided yet"), estimate-case-build-finds-an-existing-judgment (purpose, .guppi/guppi/), about twenty methods that wait for "a later session", "the first" or "the render"; Criterion sentences true only in GUPPI: estimate-ratification-case-id-carries-the-sprint, estimate-synthesis-keeps-actioned-by-the-mark, estimate-sprint-close-next-session-opens-the-sprint and estimate-synthesis-clusters (name estimate pages not shipped), estimate-permissions (c--PROJECTS-GUPPI), estimate-orchestration-forwards-a-discussion-question (Russian), estimate-orchestration-batches-cases-out-at-once, estimate-materialize-judges-a-fence, estimate-materialize-lifts-a-lesson, estimate-case-build-checks-a-fact-of-an-outside-tool, estimate-case-build-goes-on-after-a-compaction, estimate-case-check-sends-back-a-faulty-case, estimate-case-example-passes-the-check, estimate-case-protocol-case-form, estimate-case-build-finds-an-existing-judgment, estimate-glossary-terms-defined

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
- 2026-10-29 status: failed → failed · raw/2026-10-28/2312/ledger.md#L8
- 2026-10-29 updated: read again after the texts of case 897 land; the method waits for the librarian's run of session 2312 · [[decision-case-897.6]]
- 2026-10-29 status: failed → failed · raw/2026-10-29/0327/ledger.md#L1
- 2026-10-29 updated: the Criterion replaced whole — a sentence that holds as it reads in an installed project passes, and a method may wait for a kind of moment that comes again in any project · [[decision-case-898.1]]
