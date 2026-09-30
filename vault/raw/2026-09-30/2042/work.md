## Baseline

- `make test`: exit 0 — 984 passed, 2 skipped; no failing test.
- `make lint`: exit 2 — 51 lines; each finding line as printed:

```
rules/rule-spec-box: schema: missing field kind
rules/rule-spec-box: schema: missing field estimates
decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown
rules/rule-spec-box: orphan: no other live page names it in its frontmatter
rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
rules/rule-morph: deferred: 1 time since case 239
rules/rule-orchestration: deferred: 2 times since case 424
rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-ask-finds: unread: pending
estimates/estimate-carry-over-writes: unread: pending
estimates/estimate-case-build-checks-the-finished-case: unread: failed
estimates/estimate-case-build-records-the-rounds-in-recommend: unread: failed
estimates/estimate-case-build-writes-a-plain-round: unread: failed
estimates/estimate-case-build-writes-the-case: unread: pending
estimates/estimate-case-check-requires-each-question-of-the-rounds: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
estimates/estimate-case-check-shows-only-the-checked-case: unread: pending
estimates/estimate-case-protocol-ledger-line-form: unread: pending
estimates/estimate-case-protocol-shows-the-built-case: unread: failed
estimates/estimate-case-protocol-shows-the-frontier-after-a-closed-line: unread: pending
estimates/estimate-compact-recall-reloads: unread: pending
estimates/estimate-decisions-schema-checked: unread: pending
estimates/estimate-documentation-completes: unread: failed
estimates/estimate-end-of-work-order: unread: pending
estimates/estimate-event-log-records: unread: pending
estimates/estimate-generate-rewords: unread: pending
estimates/estimate-governed-files-hook-refuses: unread: pending
estimates/estimate-handoff-dispatches: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: pending
estimates/estimate-ledger-write-exits-2-on-an-error: unread: pending
estimates/estimate-ledger-write-lifts: unread: pending
estimates/estimate-ledger-write-refuses-a-line-it-cannot-read: unread: pending
estimates/estimate-plan-mode-verified: unread: pending
estimates/estimate-python-utf8-output-intact: unread: pending
estimates/estimate-retro-commit-gates: unread: pending
estimates/estimate-retro-loads: unread: pending
estimates/estimate-retro-onward-sends-the-agent-to-the-handoff: unread: pending
estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note: unread: pending
estimates/estimate-retro-red-in-the-baseline-is-not-charged: unread: pending
estimates/estimate-retro-runs-on-to-the-handoff: unread: pending
estimates/estimate-session-phases-in-order: unread: pending
estimates/estimate-session-start-context: unread: pending
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-spec-write-writes-a-defer: unread: failed
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-where-to-stop-stops-only-on-its-conditions: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
make: *** [Makefile:51: lint] Error 1
```

## Expected red

