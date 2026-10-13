# Work — session 2118

## Baseline

- `make test`: exit 0 — 1601 passed, 6 skipped.
- `make lint`: exit 0 — no line.

## Expected red

- `make lint`, its step `guppi ship --check` (case 807.2): red on the pointers of `.claude/` and `CLAUDE.md`, files rendered from Rule pages, which a Case of the next session rewords through those pages (case 807.3). At the end of Work Mode the step printed no line: `.claude/` and `CLAUDE.md` hold no pointer outside a bracket, only brackets with words that `--review` lists.

