# Work — session 1739

## Baseline

- `make test`: exit 0 — 1620 passed, 6 skipped
- `make lint`: exit 0 — no finding line

## Expected red

- `.guppi/tests/test_guppi_package.py`: red on the old command in the files of `.claude/` and on `.claude/settings.json` without the new `COMMAND`s, until the librarian's render; red on the old command and paths in live rules, entities and Estimates, until the librarian's `reword` of `rule-guppi-package` (Case 819.1)
- `make lint` (`guppi lint`, `method` and `path`): red on each page whose `method`, `implementation_ref`, `governs` or `code_ref` names `guppi/…` or `tests/…` at the root, until the librarian's `reword` of `rule-guppi-package` (Case 819.1)
- `guppi test` and `guppi style`, and the jobs `test` and `style` of `.github/workflows/checks.yml`: exit 1 on `guppi.toml: no key test` / `no key style`, until the librarian renders `guppi.toml` from `rule-guppi-config` (Cases 820.2, 820.7)
- `make lint` (`guppi lint`, `status`): `a page with core: true that is draft` on `entity-sprint`, `rule-morph`, `rule-skill-hi`, `rule-skill-merge-main`, `rule-skill-pr-review` and `rule-work-mode`, and on each core page the librarian's run sets `draft`, until each such page is `built` or loses `core` (Case 822.9)

## Conserved Spec

vault/raw/2026-10-15/0553/
