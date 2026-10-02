# Work — session 1725, 2026-10-01

## Baseline

- `make test`: exit 0 — 1050 passed, 2 skipped.
- `make lint`: exit 2 — it stops at its backlog step:
  - `backlog: vault/wiki/backlog.md differs from its sources` (the `[-]` lines of this session's `frontier.md` change the put-off counts that `guppi backlog` reads; the librarian's `guppi backlog` writes the file)
- `uv run guppi lint`, the page step run alone: exit 1, 49 lines —
  - `rules/rule-spec-box: schema: missing field kind`
  - `rules/rule-spec-box: schema: missing field estimates`
  - `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown`
  - `rules/rule-spec-box: orphan: no other live page names it in its frontmatter`
  - `rules/rule-case-rebuild-cost: deferred: 2 times since case 566`
  - `rules/rule-complaint-becomes-a-lesson: deferred: 1 time since case 504`
  - `rules/rule-morph: deferred: 1 time since case 239`
  - `rules/rule-orchestration: deferred: 3 times since case 424`
  - `rules/rule-prespec-script-skips-code-spans: deferred: 1 time since case 481`
  - `rules/rule-subagent-guppi: deferred: 31 times since case 29`
  - 39 `unread` lines, one per Estimate `pending` or `failed`

## Expected red
