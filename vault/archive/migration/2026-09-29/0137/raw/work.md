# Work — session 0137, 2026-09-29

## Baseline

- `make test`: exit 0 — 891 passed, 2 skipped; no failing test.
- `make lint`: exit 2 — 145 findings, as printed:

```
rules/rule-spec-box: schema: missing field kind
rules/rule-spec-box: schema: missing field estimates
decisions/decision-case-1: schema: missing section ## Context
decisions/decision-case-1: schema: missing section ## Problem
decisions/decision-case-10: schema: missing section ## Context
decisions/decision-case-10: schema: missing section ## Problem
decisions/decision-case-11: schema: missing section ## Context
decisions/decision-case-11: schema: missing section ## Problem
decisions/decision-case-12: schema: missing section ## Context
decisions/decision-case-12: schema: missing section ## Problem
decisions/decision-case-13: schema: missing section ## Context
decisions/decision-case-13: schema: missing section ## Problem
decisions/decision-case-14: schema: missing section ## Context
decisions/decision-case-14: schema: missing section ## Problem
decisions/decision-case-15.1: schema: missing section ## Context
decisions/decision-case-15.1: schema: missing section ## Problem
decisions/decision-case-15.3: schema: missing section ## Context
decisions/decision-case-15.3: schema: missing section ## Problem
decisions/decision-case-16.1: schema: missing section ## Context
decisions/decision-case-16.1: schema: missing section ## Problem
decisions/decision-case-16.2: schema: missing section ## Context
decisions/decision-case-16.2: schema: missing section ## Problem
decisions/decision-case-17: schema: missing section ## Context
decisions/decision-case-17: schema: missing section ## Problem
decisions/decision-case-18.1: schema: missing section ## Context
decisions/decision-case-18.1: schema: missing section ## Problem
decisions/decision-case-18.2: schema: missing section ## Context
decisions/decision-case-18.2: schema: missing section ## Problem
decisions/decision-case-18.3: schema: missing section ## Context
decisions/decision-case-18.3: schema: missing section ## Problem
decisions/decision-case-19: schema: missing section ## Context
decisions/decision-case-19: schema: missing section ## Problem
decisions/decision-case-2: schema: missing section ## Context
decisions/decision-case-2: schema: missing section ## Problem
decisions/decision-case-20: schema: missing section ## Context
decisions/decision-case-20: schema: missing section ## Problem
decisions/decision-case-21: schema: missing section ## Context
decisions/decision-case-21: schema: missing section ## Problem
decisions/decision-case-24.1: schema: missing section ## Context
decisions/decision-case-24.1: schema: missing section ## Problem
decisions/decision-case-25: schema: missing section ## Context
decisions/decision-case-25: schema: missing section ## Problem
decisions/decision-case-26.1: schema: missing section ## Context
decisions/decision-case-26.1: schema: missing section ## Problem
decisions/decision-case-26.2: schema: missing section ## Context
decisions/decision-case-26.2: schema: missing section ## Problem
decisions/decision-case-27: schema: missing section ## Context
decisions/decision-case-27: schema: missing section ## Problem
decisions/decision-case-28: schema: missing section ## Context
decisions/decision-case-28: schema: missing section ## Problem
decisions/decision-case-3: schema: missing section ## Context
decisions/decision-case-3: schema: missing section ## Problem
decisions/decision-case-4: schema: missing section ## Context
decisions/decision-case-4: schema: missing section ## Problem
decisions/decision-case-5: schema: missing section ## Context
decisions/decision-case-5: schema: missing section ## Problem
decisions/decision-case-6: schema: missing section ## Context
decisions/decision-case-6: schema: missing section ## Problem
decisions/decision-case-7: schema: missing section ## Context
decisions/decision-case-7: schema: missing section ## Problem
decisions/decision-case-8: schema: missing section ## Context
decisions/decision-case-8: schema: missing section ## Problem
decisions/decision-case-9: schema: missing section ## Context
decisions/decision-case-9: schema: missing section ## Problem
decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown
rules/rule-spec-box: orphan: no other live page names it in its frontmatter
rules/rule-case-build-checks-its-sub-cases: deferred: 1 time since case 480
rules/rule-morph: deferred: 1 time since case 239
rules/rule-orchestration: deferred: 1 time since case 424
rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-agent-writing-followed: unread: pending
estimates/estimate-atomicity-rendered: unread: pending
estimates/estimate-carry-over-writes: unread: pending
estimates/estimate-case-build-writes-a-plain-round: unread: failed
estimates/estimate-case-build-writes-the-case: unread: pending
estimates/estimate-case-check-notes-a-then-line-shared-by-siblings: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
estimates/estimate-case-check-shows-only-the-checked-case: unread: pending
estimates/estimate-case-protocol-defers-in-one-reply: unread: pending
estimates/estimate-case-protocol-ledger-line-form: unread: pending
estimates/estimate-claude-md-rendered: unread: pending
estimates/estimate-close-commits: unread: pending
estimates/estimate-compact-recall-reloads: unread: pending
estimates/estimate-context-size-warns-past-the-limit: unread: pending
estimates/estimate-decisions-schema-checked: unread: pending
estimates/estimate-documentation-completes: unread: pending
estimates/estimate-entities-schema-checked: unread: pending
estimates/estimate-estimates-schema-checked: unread: pending
estimates/estimate-event-log-records: unread: pending
estimates/estimate-generate-renames: unread: pending
estimates/estimate-generate-rewords: unread: pending
estimates/estimate-generate-walks-dates: unread: pending
estimates/estimate-generate-writes-rules-from-applies-to: unread: pending
estimates/estimate-generate-writes-the-decision-page: unread: pending
estimates/estimate-generate-writes: unread: pending
estimates/estimate-git-context-current: unread: pending
estimates/estimate-github-issues-listed: unread: pending
estimates/estimate-glossary-checks-the-file: unread: pending
estimates/estimate-glossary-renders-the-terms: unread: pending
estimates/estimate-glossary-terms-defined: unread: pending
estimates/estimate-glossary-ticks-the-spec: unread: pending
estimates/estimate-guppi-tests-green: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: pending
estimates/estimate-hi-no-read-calls: unread: pending
estimates/estimate-ledger-tail: unread: pending
estimates/estimate-lessons-schema-checked: unread: pending
estimates/estimate-lint-catches-a-broken-fence: unread: pending
estimates/estimate-materialize-judges-a-fence: unread: pending
estimates/estimate-materialize-lifts-unfiltered-on-a-schema-change: unread: pending
estimates/estimate-materialize-refolds-a-reading-on-a-supersede: unread: pending
estimates/estimate-one-judgment-one-implementation-followed: unread: pending
estimates/estimate-page-schemas-one-file-per-rule: unread: pending
estimates/estimate-permissions: unread: pending
estimates/estimate-plan-mode-verified: unread: pending
estimates/estimate-prespec-catches-a-broken-fence: unread: pending
estimates/estimate-prespec-catches-a-command-line-off-form: unread: pending
estimates/estimate-prespec-catches-a-method-without-a-form: unread: pending
estimates/estimate-prespec-catches-a-superseded-case: unread: pending
estimates/estimate-prespec-catches-an-unwrapped-render: unread: pending
estimates/estimate-prespec-catches-bare-wikilinks: unread: pending
estimates/estimate-prespec-hook-gates: unread: pending
estimates/estimate-prespec-simulates-the-pairs: unread: pending
estimates/estimate-render-harness-ticks-the-spec: unread: pending
estimates/estimate-retro-commit-gates: unread: pending
estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note: unread: pending
estimates/estimate-retro-red-in-the-baseline-is-not-charged: unread: pending
estimates/estimate-retro-report-holds-each-fact-once: unread: pending
estimates/estimate-rules-schema-checked: unread: pending
estimates/estimate-session-phases-in-order: unread: pending
estimates/estimate-session-start-context: unread: pending
estimates/estimate-skill-wait-what-re-pitches: unread: failed
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-sprint-checks-the-file: unread: pending
estimates/estimate-sprint-drops-an-emptied-milestone: unread: pending
estimates/estimate-sprint-migration-index-dissolved: unread: pending
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-sprint-migration-rule-class-files-dissolved: unread: pending
estimates/estimate-sprint-ticks-the-spec: unread: pending
estimates/estimate-synthesis-clusters: unread: pending
estimates/estimate-vault-layout-holds: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
estimates: unmigrated: 12 pages in the shape before case 193
```

## Expected red
