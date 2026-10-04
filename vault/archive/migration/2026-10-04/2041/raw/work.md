# Work — session 2041, 2026-10-04

## Baseline

- `make test`: exit 0 — 1166 passed, 6 skipped
- `make lint`: exit 2 — 35 finding lines:

```
rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
rules/rule-ledger-line-withdrawn-on-re-ratification: deferred: 1 time since case 594
rules/rule-morph: deferred: 1 time since case 239
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-ask-finds: unread: failed
estimates/estimate-ask-query-before-a-create: unread: pending
estimates/estimate-backlog-renders: unread: pending
estimates/estimate-brief-written: unread: pending
estimates/estimate-case-build-checks-the-finished-case: unread: pending
estimates/estimate-case-build-writes-the-case: unread: pending
estimates/estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent: unread: pending
estimates/estimate-case-check-requires-each-question-of-the-rounds: unread: pending
estimates/estimate-case-check-sends-back-a-case-number-held-by-another-agent: unread: pending
estimates/estimate-case-check-sends-back-a-clash-with-another-case: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-round: unread: pending
estimates/estimate-case-check-sends-back-a-ratified-case-in-another-shape: unread: pending
estimates/estimate-generate-writes: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: pending
estimates/estimate-hi-writes-frontier: unread: pending
estimates/estimate-lint-runs-every-step: unread: pending
estimates/estimate-session-start-context: unread: pending
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-sprint-close-archives-done-insights-and-lone-lessons: unread: pending
estimates/estimate-sprint-close-archives-the-decisions: unread: pending
estimates/estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest: unread: pending
estimates/estimate-sprint-close-next-session-opens-the-sprint: unread: pending
estimates/estimate-sprint-close-runs-in-the-librarian-run: unread: pending
estimates/estimate-sprint-close-settles-unread-estimates: unread: pending
estimates/estimate-sprint-close-takes-the-readings-in-groups: unread: pending
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-sprint-ticks-the-spec: unread: pending
estimates/estimate-synthesis-clusters: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
```

## Expected red
