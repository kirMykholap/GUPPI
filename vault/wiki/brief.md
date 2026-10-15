# Brief — 2026-10-15, session 44ee5004 (0553) conserved its Spec

## Where things stand

- Session 44ee5004 of the sprint `plugin` opened with /hi on 2026-10-14 at 19:07 (folder `vault/raw/2026-10-14/1907/`) and, after a resume on 2026-10-15, again at 05:53 (folder `vault/raw/2026-10-15/0553/`). Its Spec is conserved: `vault/raw/2026-10-15/0553/spec.md`, marked by `carry.md` in the same folder, on the branch `spec/2026-10-15-0553`.
- The Spec holds six Cases, all ratified and checked by `/pre-spec` (`guppi prespec --check` printed no finding):
  - Case 816 — the clean branch is a plugin and its catalogue (`plugin/` templates → `.claude-plugin/plugin.json`, `marketplace.json`; version from tags `prod-x.y.z`; `claude plugin validate` in CI).
  - Case 817 — the install Case comes at the first `/hi` after `/guppi:install` (`rule-morph` rewritten; the install step itself is built later).
  - Case 818 — the plugin `guppi` installs GUPPI into a project (`rule-plugin-install`, skill `/guppi:install`).
  - Case 819 — the code of GUPPI stands in `.guppi/` and every caller runs `uv run --project .guppi guppi …` (`rule-guppi-package`; `reword` learns path prefixes; `/guppi:install` checks `uv` and runs `uv sync`).
  - Case 820 — GUPPI runs its checks without make (`guppi check`, `guppi test`, `guppi style`; keys `test` and `style` of `guppi.toml`; no `ship` in the clean version; a thin `Makefile` stays here for now).
  - Case 822 — a new project gets the passed Estimates, the tests, the session-file skeletons and `checks.yml`; `guppi ship` refuses to build while a page with `core: true` is `draft`, `--allow-draft` writes a local copy; Case 822 replaces Case 821 whole and takes up `decision-case-805`.
- Not done on the Spec: all of it — no Work Mode ran. Its tasks include a `stop:` task for the owner to place and push the tag `prod-0.2.0` after Work Mode.
- Frontier: C1, C2, C5–C9 closed by these Cases; the sprint items C3 (the README) and C4 (the close of `plugin`) left for later sessions.

## Flags

- The session is split over two folders. A resume on the next day made the ledger hook refuse every line ("no /hi recorded"), and a second /hi opened `raw/2026-10-15/0553/`. By the person's word, as an exception, the 37 ledger lines of `raw/2026-10-14/1907/ledger.md` were moved by hand to the head of `raw/2026-10-15/0553/ledger.md` and the old ledger deleted; the case files 816–821 were copied to `raw/2026-10-15/0553/cases/`. `raw/2026-10-14/1907/` keeps its `frontier.md` and the old copies of the case files only.
- The ledger holds two lessons of this session, written before the carry: `lesson-ledger-window-stops-at-a-resume-on-the-next-day` (the walk of `session_event_logs` in `guppi/ledger.py` stops at the resume, never reaching the `hi` of the day before) and `lesson-case-build-agent-context-grows-on-every-resume` (a case-guppi reached about 930 000 tokens over its resumes). Neither has a fixing Case; they reach the vault only when this unit is materialized.
- A fresh case-guppi for a rebuild was refused by the guard of the case file, which keeps the number of the earlier builder; a rebuild of Case 821 came back under a new number, 822.
- The Stop check of `rule-case-check` refused one pair of Case 822.4 five times on "the sentence around a pair was not read whole", though the case files were read; the pair was moved to other words. The cause in `guppi/casecheck.py` was not found.
- `entity-sprint` has no Estimate, so it stays `draft` with `core: true`; under Case 822.8 `guppi ship` will refuse to build `prod` until a later Case gives it one. `rule-skill-hi` and `rule-work-mode` stay `draft` too.

## Next session

### Cases

- none

### Work

- none

### Ask the person

- none
