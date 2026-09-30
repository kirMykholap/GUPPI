# Work — session 1736, 2026-09-30

Branch: migration. The Baseline is taken after the code of 552.1 (`guppi/materialize.py`, `tests/test_materialize.py`), built before the Spec with the person's consent to unblock the ledger hook.

## Baseline

`make test`: exit 2 — 1 failed, 976 passed, 2 skipped.

- FAILED tests/test_schemas.py::test_a_decision_page_without_context_has_no_finding

`make lint`: exit 2 — 61 finding lines.

- rules/rule-spec-box: schema: missing field kind
- rules/rule-spec-box: schema: missing field estimates
- decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown
- rules/rule-spec-box: orphan: no other live page names it in its frontmatter
- rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
- rules/rule-morph: deferred: 1 time since case 239
- rules/rule-orchestration: deferred: 2 times since case 424
- rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481
- rules/rule-subagent-guppi: deferred: 31 times since case 29
- estimates/estimate-ask-finds: unread: pending
- estimates/estimate-brief-written: unread: pending
- estimates/estimate-carry-over-writes: unread: pending
- estimates/estimate-case-build-checks-the-finished-case: unread: pending
- estimates/estimate-case-build-records-the-rounds-in-recommend: unread: pending
- estimates/estimate-case-build-writes-a-plain-round: unread: failed
- estimates/estimate-case-build-writes-the-case: unread: pending
- estimates/estimate-case-check-refuses-a-problem-in-a-sub-case: unread: pending
- estimates/estimate-case-check-requires-each-question-of-the-rounds: unread: pending
- estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
- estimates/estimate-case-check-shows-only-the-checked-case: unread: pending
- estimates/estimate-case-protocol-case-form: unread: pending
- estimates/estimate-case-protocol-ledger-line-form: unread: pending
- estimates/estimate-case-protocol-shows-the-built-case: unread: pending
- estimates/estimate-compact-recall-reloads: unread: pending
- estimates/estimate-decisions-schema-checked: unread: pending
- estimates/estimate-documentation-completes: unread: pending
- estimates/estimate-end-of-work-order: unread: pending
- estimates/estimate-event-log-records: unread: pending
- estimates/estimate-generate-replace-takes-the-leading-indent: unread: pending
- estimates/estimate-generate-rewords: unread: pending
- estimates/estimate-generate-writes-the-decision-page: unread: pending
- estimates/estimate-generate-writes: unread: pending
- estimates/estimate-glossary-terms-defined: unread: failed
- estimates/estimate-governed-files-hook-refuses: unread: pending
- estimates/estimate-handoff-dispatches: unread: pending
- estimates/estimate-handoff-holds-each-fact-once: unread: pending
- estimates/estimate-hi-takes-its-readings: unread: failed
- estimates/estimate-lint-finds-a-broken-link: unread: pending
- estimates/estimate-materialize-assembles: unread: pending
- estimates/estimate-permissions: unread: pending
- estimates/estimate-plan-mode-verified: unread: pending
- estimates/estimate-prespec-catches-an-indent-added-twice: unread: pending
- estimates/estimate-python-utf8-output-intact: unread: pending
- estimates/estimate-retro-commit-gates: unread: pending
- estimates/estimate-retro-loads: unread: pending
- estimates/estimate-retro-onward-sends-the-agent-to-the-handoff: unread: pending
- estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note: unread: pending
- estimates/estimate-retro-red-in-the-baseline-is-not-charged: unread: pending
- estimates/estimate-retro-runs-on-to-the-handoff: unread: pending
- estimates/estimate-session-phases-in-order: unread: pending
- estimates/estimate-session-start-context: unread: pending
- estimates/estimate-skill-grill-me-asks-in-rounds: unread: failed
- estimates/estimate-spec-write-copies-the-ratified-case: unread: pending
- estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
- estimates/estimate-spec-write-writes-a-defer: unread: pending
- estimates/estimate-sprint-migration-leftovers-gone: unread: pending
- estimates/estimate-sprint-migration-lint-clean: unread: pending
- estimates/estimate-sprint-migration-merges: unread: pending
- estimates/estimate-where-to-stop-stops-only-on-its-conditions: unread: pending
- estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
- estimates/estimate-work-mode-takes-the-work-readings: unread: pending

## Expected red
