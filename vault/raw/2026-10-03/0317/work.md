# Work — session 0317, 2026-10-03

## Baseline

- `make test`: exit 0 — 1117 passed, 6 skipped; no failing test
- `make lint`: exit 2

```
rules/rule-case-rebuild-cost: deferred: 2 times since case 566
rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
rules/rule-ledger-line-withdrawn-on-re-ratification: deferred: 1 time since case 594
rules/rule-morph: deferred: 1 time since case 239
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-ask-finds: unread: pending
estimates/estimate-carry-over-writes: unread: pending
estimates/estimate-case-build-writes-the-case: unread: pending
estimates/estimate-case-check-requires-each-question-of-the-rounds: unread: pending
estimates/estimate-case-check-sends-back-a-case-number-held-by-another-agent: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-round: unread: pending
estimates/estimate-case-check-sends-back-a-ratified-case-in-another-shape: unread: pending
estimates/estimate-compact-recall-reloads: unread: pending
estimates/estimate-end-of-work-order: unread: pending
estimates/estimate-event-log-records: unread: pending
estimates/estimate-generate-rewords: unread: pending
estimates/estimate-handoff-dispatches: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: pending
estimates/estimate-hi-takes-a-conserved-spec: unread: pending
estimates/estimate-ledger-write-lifts: unread: pending
estimates/estimate-lint-runs-every-step: unread: pending
estimates/estimate-orchestration-defers-in-one-reply: unread: pending
estimates/estimate-orchestration-shows-the-built-case: unread: failed
estimates/estimate-orchestration-signs-a-batch-together: unread: pending
estimates/estimate-plan-mode-verified: unread: pending
estimates/estimate-prespec-onward-sends-the-agent-on: unread: pending
estimates/estimate-ratification-ledger-line-form: unread: pending
estimates/estimate-retro-loads: unread: pending
estimates/estimate-retro-onward-sends-the-agent-to-the-handoff: unread: pending
estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note: unread: pending
estimates/estimate-retro-runs-on-to-the-handoff: unread: pending
estimates/estimate-session-start-context: unread: pending
estimates/estimate-spec-box-runs-a-conserved-spec: unread: pending
estimates/estimate-spec-capture-offers-the-fork: unread: pending
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-synthesis-clusters: unread: pending
estimates/estimate-where-to-stop-stops-only-on-its-conditions: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
estimates/estimate-work-mode-takes-the-work-readings: unread: pending
```

## Expected red

- `make lint`, the class `moment` of `guppi lint` (case 613.1): 21 findings on the Estimates whose `method` 613.2 and 613.3 rewrite — `estimate-hi-takes-its-readings` and 20 of 613.3; red until the librarian writes those pages
