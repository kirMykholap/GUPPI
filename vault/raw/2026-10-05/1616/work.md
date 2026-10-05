# Work — session 1616, 2026-10-05

## Baseline

- make test: exit 0 — 1207 passed, 6 skipped
- make lint: exit 2 — 36 finding lines:

  - rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504
  - rules/rule-ledger-line-withdrawn-on-re-ratification: deferred: 1 time since case 594
  - rules/rule-morph: deferred: 1 time since case 239
  - rules/rule-prespec-judges-the-spec-whole: deferred: 1 time since case 643
  - rules/rule-subagent-guppi: deferred: 31 times since case 29
  - estimates/estimate-ask-query-before-a-create: unread: pending
  - estimates/estimate-ask-searches-at-prespec: unread: pending
  - estimates/estimate-backlog-renders: unread: pending
  - estimates/estimate-brief-written: unread: pending
  - estimates/estimate-case-build-checks-the-finished-case: unread: failed
  - estimates/estimate-case-build-writes-the-case: unread: pending
  - estimates/estimate-case-check-requires-a-backlog-item-decided-on-its-page: unread: pending
  - estimates/estimate-case-check-sends-back-a-faulty-case: unread: pending
  - estimates/estimate-case-check-shows-only-the-checked-case: unread: pending
  - estimates/estimate-case-protocol-case-form: unread: failed
  - estimates/estimate-case-protocol-example-passes-the-check: unread: pending
  - estimates/estimate-hi-takes-a-conserved-spec: unread: pending
  - estimates/estimate-hi-writes-frontier: unread: pending
  - estimates/estimate-orchestration-defer-example-passes-the-hook: unread: pending
  - estimates/estimate-orchestration-showing-example-passes-the-check: unread: pending
  - estimates/estimate-orchestration-shows-the-built-case: unread: failed
  - estimates/estimate-permissions: unread: pending
  - estimates/estimate-prespec-confirms-the-findings-once: unread: failed
  - estimates/estimate-search-leaves-out-decisions-in-every-agent: unread: failed
  - estimates/estimate-spec-reconcile-refuses-a-case-file-another-agent-holds: unread: pending
  - estimates/estimate-spec-reconcile-refuses-an-edit-of-the-plan: unread: pending
  - estimates/estimate-spec-write-answers-a-refusal: unread: pending
  - estimates/estimate-spec-write-reaches-the-approved-spec: unread: pending
  - estimates/estimate-sprint-close-next-session-opens-the-sprint: unread: pending
  - estimates/estimate-sprint-close-runs-in-the-librarian-run: unread: pending
  - estimates/estimate-sprint-close-takes-the-readings-in-groups: unread: pending
  - estimates/estimate-sprint-migration-leftovers-gone: unread: pending
  - estimates/estimate-sprint-migration-lint-clean: unread: pending
  - estimates/estimate-sprint-migration-merges: unread: pending
  - estimates/estimate-synthesis-clusters: unread: pending
  - estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline: unread: pending

## Expected red

- `guppi casecheck --subagent` (SubagentStop): sends back a summary of case-guppi with no `**Case:**` line until the librarian renders `.claude/agents/case-guppi.md` from `rule-case-build` (case 662.1)
