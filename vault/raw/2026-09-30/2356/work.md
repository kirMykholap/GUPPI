# Work — session 2356, 2026-09-30

## Baseline

- `make test`: exit 0 — 997 passed, 2 skipped.
- `make lint`: exit 2 — it stops at `guppi backlog --check`:
  - `backlog: vault/wiki/backlog.md differs from its sources` (the line of `rule-spec-box` reads "put off in 6 sessions" from its sources against 5 in the file: the defer of case 565 in this session's ledger)
- The steps after it, run one by one: `guppi render --check` exit 0, `guppi sprint --check` exit 0, `guppi glossary --check` exit 0, `guppi lint` exit 1:
  - `rules/rule-spec-box: schema: missing field kind`
  - `rules/rule-spec-box: schema: missing field estimates`
  - `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown`
  - `rules/rule-spec-box: orphan: no other live page names it in its frontmatter`
  - `rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504`
  - `rules/rule-morph: deferred: 1 time since case 239`
  - `rules/rule-orchestration: deferred: 2 times since case 424`
  - `rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481`
  - `rules/rule-subagent-guppi: deferred: 31 times since case 29`
  - 42 `unread` lines, one per Estimate not read.

## Expected red
