# Work — session 2000, 2026-09-28

## Baseline

- `make test`: exit 0 — 876 passed, 2 skipped; no failing test.
- `make lint`: exit 2 — 104 findings:

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
rules/rule-spec-box: orphan: no other live page names it in its frontmatter
rules/rule-case-build-checks-its-sub-cases: deferred: 1 time since case 480
rules/rule-morph: deferred: 1 time since case 239
rules/rule-orchestration: deferred: 1 time since case 424
rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481
rules/rule-subagent-guppi: deferred: 31 times since case 29
estimates/estimate-agent-writing-followed: unread: pending
estimates/estimate-carry-over-writes: unread: pending
estimates/estimate-case-build-writes-a-plain-round: unread: pending
estimates/estimate-case-build-writes-the-case: unread: pending
estimates/estimate-case-check-notes-a-criterion-line-not-carried: unread: pending
estimates/estimate-case-check-notes-a-then-line-shared-by-siblings: unread: pending
estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
estimates/estimate-case-check-shows-only-the-checked-case: unread: pending
estimates/estimate-case-protocol-defers-in-one-reply: unread: pending
estimates/estimate-case-protocol-ledger-line-form: unread: pending
estimates/estimate-case-protocol-shows-the-built-case: unread: pending
estimates/estimate-context-size-warns-past-the-limit: unread: pending
estimates/estimate-documentation-completes: unread: pending
estimates/estimate-event-log-records: unread: pending
estimates/estimate-generate-writes-the-decision-page: unread: pending
estimates/estimate-guppi-config-fills-the-languages: unread: pending
estimates/estimate-handoff-holds-each-fact-once: unread: pending
estimates/estimate-language-followed: unread: pending
estimates/estimate-language-spec-prose-in-english: unread: pending
estimates/estimate-permissions: unread: pending
estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note: unread: pending
estimates/estimate-retro-red-in-the-baseline-is-not-charged: unread: pending
estimates/estimate-retro-report-holds-each-fact-once: unread: failed
estimates/estimate-session-phases-in-order: unread: pending
estimates/estimate-skill-wait-what-re-pitches: unread: pending
estimates/estimate-spec-capture-offers-the-fork: unread: pending
estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
estimates/estimate-sprint-migration-file-route-gone: unread: pending
estimates/estimate-sprint-migration-leftovers-gone: unread: pending
estimates/estimate-sprint-migration-lint-clean: unread: pending
estimates/estimate-sprint-migration-merges: unread: pending
estimates/estimate-synthesis-clusters: unread: pending
estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending
estimates: unmigrated: 18 pages in the shape before case 193
```

## Expected red

