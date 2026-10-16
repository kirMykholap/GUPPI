# Frontier — session 0342

## Cases

- [-] C1 — `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch` — CI writes a clean branch; what remains: the seven draft pages with `core: true` stop every build of `prod`, and the next tag after `prod-0.2.0`, which the push of session 0104 spent · sprint · defer
  - near `rule-work-mode`, `rule-guppi-package`, `estimate-harness-pipeline`
- [x] C2 — `/hi` in a project that is no git repository: go on and tell the person to run `git init`, or offer to run it (`lesson-hi-fails-outside-a-git-repository`) · brief · case 851
- [x] C3 — `/guppi:install` with no `uv`: whether it offers to install `uv` · brief · case 852
  - near `rule-guppi-package`
- [x] C4 — `/guppi:install` when `uv sync` fails offline; whether `uv sync` takes the `dev` group in a user's project at all · brief · case 853
  - near `rule-guppi-package`
- [x] C5 — The tag `prod-0.2.0` stands on GitHub on a commit whose run failed; whether it stays · brief · work
- [x] C6 — Failed `estimate-clean-branch-ships-the-tests`: L17 failed in the copy on the `[tests/]` test of `test_guppi_package.py`; that test now passes in the repository · brief · work
  - near `estimate-guppi-tests-green`
- [-] C7 — Failed `estimate-clean-branch-writes-the-session-files`: L18 failed, the first `/hi` stopped outside a git repository · brief · defer case 855
- [x] C8 — Failed `estimate-harness-pipeline`: not read at Retro of session 1739; deferred by cases 833 and 849 · brief · work
  - near `estimate-harness-pipeline`

Backlog: 15 items

## Work

- [x] W1 — `estimate-guppi-package-runs-from-its-own-folder` · brief · work
- [x] W2 — `estimate-clean-branch-ships-neutral-texts` · brief · work
- [x] W3 — The `stop:` box at line 165 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`, unticked · brief · work

## Ask

- [x] A1 — `estimate-clean-branch-installs-as-a-plugin` — in session 0104 the person added `scratchpad/ship-plugin` as a catalogue and installed `guppi` from it; did the catalogue add and the plugin install with no error? · brief · work
- [x] A2 — `estimate-guppi-package-is-ready-after-the-install` — no `uv`: the install said `uv` is missing and wrote nothing; with `uv`: it built `.guppi/.venv/` and the hooks ran at the first `/hi`; offline: `uv sync` failed and it stopped, but told the person to type `/hi` after a fix. Does that pass the Criterion? · brief · work
