# Work — session 0004, 2026-10-04

## Baseline

- `make test`: exit 0, 1129 passed, 6 skipped; no failing test
- `make lint`: exit 2, 38 finding lines

```
entities/entity-reading-probe: schema: missing field parent (given {'kind': 'Leaf'})
entities/entity-reading-probe: orphan: no other live page names it in its frontmatter
rules/rule-case-rebuild-cost: deferred: 2 times since case 566
rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
rules/rule-ledger-line-withdrawn-on-re-ratification: deferred: 1 time since case 594
rules/rule-morph: deferred: 1 time since case 239
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-ask-finds: unread: pending
estimates/estimate-case-check-requires-each-question-of-the-rounds: unread: pending
estimates/estimate-case-check-sends-back-a-case-number-held-by-another-agent: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-round: unread: pending
estimates/estimate-case-check-sends-back-a-ratified-case-in-another-shape: unread: pending
estimates/estimate-generate-rewords: unread: pending
estimates/estimate-handoff-dispatches: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: failed
estimates/estimate-hi-takes-a-conserved-spec: unread: failed
estimates/estimate-lint-runs-every-step: unread: pending
estimates/estimate-orchestration-shows-the-built-case: unread: failed
estimates/estimate-orchestration-signs-a-batch-together: unread: pending
estimates/estimate-prespec-onward-sends-the-agent-on: unread: pending
estimates/estimate-ratification-ledger-line-form: unread: pending
estimates/estimate-retro-loads: unread: pending
estimates/estimate-retro-onward-sends-the-agent-to-the-handoff: unread: pending
estimates/estimate-retro-runs-on-to-the-handoff: unread: pending
estimates/estimate-session-start-context: unread: pending
estimates/estimate-spec-box-runs-a-conserved-spec: unread: pending
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-sprint-close-archives-done-insights-and-lone-lessons: unread: pending
estimates/estimate-sprint-close-archives-the-decisions: unread: pending
estimates/estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest: unread: pending
estimates/estimate-sprint-close-settles-unread-estimates: unread: pending
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-where-to-stop-stops-only-on-its-conditions: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
estimates/estimate-work-mode-takes-the-work-readings: unread: pending
```

## Expected red

