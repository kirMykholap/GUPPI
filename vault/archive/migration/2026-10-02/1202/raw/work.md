# Work — session 1202, 2026-10-02

## Baseline

- `make test`: exit 0 — 1053 passed, 6 skipped.
- `make lint`: exit 2, stopped at its backlog step:
  - `backlog: vault/wiki/backlog.md differs from its sources`
  - `make: *** [Makefile:49: lint] Error 1`
- The later steps run alone: `guppi glossary --check` exit 0; `guppi lint` exit 1:
  - `rules/rule-spec-box: schema: missing field kind`
  - `rules/rule-spec-box: schema: missing field estimates`
  - `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section: ```markdown`
  - `rules/rule-spec-box: orphan: no other live page names it in its frontmatter`
  - 7 `deferred` lines: `rule-case-rebuild-cost`, `rule-complaint-becomes-a-lesson`, `rule-morph`, `rule-orchestration`, `rule-prespec-script-skips-code-spans`, `rule-subagent-guppi`, `rule-turn-start-one-judgment`
  - 28 `unread: pending` lines, one per Estimate of the brief's Readings due

## Expected red
