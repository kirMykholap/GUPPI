# Work — session 0248, 2026-09-30

## Baseline

- `make test`: exit 0 — 934 passed, 2 skipped
- `make lint`: exit 2 — 88 lines of output:

```
rules/rule-spec-box: schema: missing field kind
rules/rule-spec-box: schema: missing field estimates
decisions/decision-case-1: schema: missing section ## Problem
decisions/decision-case-10: schema: missing section ## Problem
decisions/decision-case-11: schema: missing section ## Problem
decisions/decision-case-12: schema: missing section ## Problem
decisions/decision-case-13: schema: missing section ## Problem
decisions/decision-case-14: schema: missing section ## Problem
decisions/decision-case-15.1: schema: missing section ## Problem
decisions/decision-case-15.3: schema: missing section ## Problem
decisions/decision-case-16.1: schema: missing section ## Problem
decisions/decision-case-16.2: schema: missing section ## Problem
decisions/decision-case-17: schema: missing section ## Problem
decisions/decision-case-18.1: schema: missing section ## Problem
decisions/decision-case-18.2: schema: missing section ## Problem
decisions/decision-case-18.3: schema: missing section ## Problem
decisions/decision-case-19: schema: missing section ## Problem
decisions/decision-case-2: schema: missing section ## Problem
decisions/decision-case-20: schema: missing section ## Problem
decisions/decision-case-21: schema: missing section ## Problem
decisions/decision-case-24.1: schema: missing section ## Problem
decisions/decision-case-25: schema: missing section ## Problem
decisions/decision-case-26.1: schema: missing section ## Problem
decisions/decision-case-26.2: schema: missing section ## Problem
decisions/decision-case-27: schema: missing section ## Problem
decisions/decision-case-28: schema: missing section ## Problem
decisions/decision-case-3: schema: missing section ## Problem
decisions/decision-case-4: schema: missing section ## Problem
decisions/decision-case-5: schema: missing section ## Problem
decisions/decision-case-6: schema: missing section ## Problem
decisions/decision-case-7: schema: missing section ## Problem
decisions/decision-case-8: schema: missing section ## Problem
decisions/decision-case-9: schema: missing section ## Problem
decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown
rules/rule-spec-box: orphan: no other live page names it in its frontmatter
rules/rule-case-build-checks-its-sub-cases: deferred: 1 time since case 480
rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
rules/rule-morph: deferred: 1 time since case 239
rules/rule-orchestration: deferred: 1 time since case 424
rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-agent-writing-followed: unread: pending
estimates/estimate-ask-finds: unread: pending
estimates/estimate-bash-guard: unread: pending
estimates/estimate-brief-written: unread: pending
estimates/estimate-case-build-writes-a-plain-round: unread: pending
estimates/estimate-case-build-writes-the-case: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
estimates/estimate-case-check-shows-only-the-checked-case: unread: pending
estimates/estimate-case-protocol-defers-in-one-reply: unread: pending
estimates/estimate-case-protocol-ledger-line-form: unread: pending
estimates/estimate-case-protocol-shows-the-built-case: unread: pending
estimates/estimate-compact-recall-reloads: unread: pending
estimates/estimate-documentation-completes: unread: pending
estimates/estimate-end-of-work-order: unread: pending
estimates/estimate-event-log-records: unread: pending
estimates/estimate-generate-renames: unread: pending
estimates/estimate-generate-rewords: unread: pending
estimates/estimate-generate-writes: unread: pending
estimates/estimate-git-context-current: unread: pending
estimates/estimate-glossary-terms-defined: unread: pending
estimates/estimate-governed-files-hook-refuses: unread: pending
estimates/estimate-handoff-dispatches: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: pending
estimates/estimate-hi-no-read-calls: unread: pending
estimates/estimate-hi-takes-its-readings: unread: pending
estimates/estimate-hi-writes-frontier: unread: pending
estimates/estimate-permissions: unread: pending
estimates/estimate-plan-mode-verified: unread: pending
estimates/estimate-prespec-checks-the-frontier: unread: pending
estimates/estimate-retro-commit-gates: unread: pending
estimates/estimate-retro-loads: unread: pending
estimates/estimate-retro-onward-sends-the-agent-to-the-handoff: unread: pending
estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note: unread: pending
estimates/estimate-retro-red-in-the-baseline-is-not-charged: unread: pending
estimates/estimate-retro-runs-on-to-the-handoff: unread: pending
estimates/estimate-session-phases-in-order: unread: pending
estimates/estimate-session-start-context: unread: pending
estimates/estimate-skill-grill-me-asks-in-rounds: unread: pending
estimates/estimate-skill-wait-what-re-pitches: unread: pending
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-where-to-stop-stops-only-on-its-conditions: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
estimates/estimate-work-mode-takes-the-work-readings: unread: pending
make: *** [Makefile:51: lint] Error 1
```

## Expected red

