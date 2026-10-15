---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch main by the owner alone
method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close
origin: raw/2026-10-10/1713/ledger.md#case-756.4
sprint: plugin
created: 2026-10-10
tags: [sprint, github, git]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `main` of the repository `GUPPI` on GitHub, which `rule-github-repository` describes, from an account other than the owner's, such as a second account that the owner made for the test.

Then:
The workflow `.github/workflows/checks.yml` runs its jobs `test`, `lint` and `style` on `windows-latest` on the pull request, by `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check` and `uv run --project .guppi guppi style`, and shows each result on it.
**＋** A run of a first-time contributor waits until the owner approves it.
**＋** The owner reviews the pull request on GitHub, and only the owner can merge it.
**＋** A merge into `main` waits until the jobs `style` and `test` pass, except for the owner, who is on the bypass list of the ruleset on `main`.
**＋** The other account cannot push to `main` or to `prod`, and a pull request against `prod` cannot be merged.
**－** A red result of the job `lint` does not block a merge into `main`.
**－** The workflow does not run on the event `pull_request_target`, so the code of the pull request reaches no secret of the repository.
**－** The test pull request is closed without a merge, so `main` takes no commit before `plugin` closes.

## History

- 2026-10-10 created · [[decision-case-756.4]]
- 2026-10-10 updated: the Criterion replaced whole — the pull request goes against the branch plugin, and a second account of the owner counts as another account · [[decision-case-766]]
- 2026-10-13 updated: the Criterion replaced whole — the pull request goes against main, only style and test block a merge, only the owner merges, the test pull request is closed without a merge · [[decision-case-794]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
- 2026-10-15 reworded: `make style` → `uv run --project .guppi guppi style` · [[decision-case-820.7]]
- 2026-10-15 updated: the Criterion replaced whole — the jobs of CI run guppi test, guppi check and guppi style in place of the targets of the Makefile · [[decision-case-820.8]]
