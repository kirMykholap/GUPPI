# Work — session 0039 (2026-11-02)

## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1904 passed, 6 skipped, 1 deselected
- `uv run --project .guppi guppi check`: exit 1
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-skill-approve-spec: status: a page with core: true that is draft
  - estimates/estimate-case-build-reads-the-link-graph-of-what-it-changes: unread: failed
  - estimates/estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed
  - estimates/estimate-orchestration-acknowledging-reply: unread: failed

## Expected red

- `uv run --project .guppi guppi check` (lint, `path`): `rules/rule-link-graph-at-session-start` names `.guppi/guppi/links.py` and `.guppi/tests/test_links.py` in `implementation_ref`, deleted by Case 999.1; waits for the librarian's run that deletes the page.
- the `SessionStart` hook `guppi links --write` of `.claude/settings.json`: an unknown command until `guppi render` writes `.claude/settings.json` from the update of `rule-hook-registry` at the librarian's run.
