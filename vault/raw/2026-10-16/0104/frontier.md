# Frontier — session 0104

## Cases

- [x] C1 — `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch` — CI writes a clean branch; what remains: a tag `prod-x.y.z` on the last commit of `plugin` and the run of `prod.yml` it starts, read by its Estimate; the draft pages with `core: true` still stop every build of `prod` without `--allow-draft` · sprint · case 847
  - near `entity-sprint-plugin`, `estimate-clean-branch-installs-as-a-plugin`
- [-] C2 — Whether the root `pyproject.toml` keeps the pytest settings beside `.guppi/pyproject.toml` until the Case that removes it · brief · defer case 848
  - near `rule-guppi-package`, `estimate-guppi-package-runs-from-its-own-folder`
- [x] C3 — Failed `estimate-guppi-package-runs-from-its-own-folder`: L5 failed on the `[tests/]` test; deferred by case 837 · brief · case 840
  - near `rule-guppi-package`, `rule-page-generation`
- [x] C4 — Failed `estimate-clean-branch-installs-as-a-plugin`: not read, no tag `prod-x.y.z`; deferred by case 831 · brief · case 842
  - near `estimate-plugin-install-writes-guppi-into-an-empty-project`, `estimate-guppi-package-is-ready-after-the-install`
- [x] C5 — Failed `estimate-plugin-install-writes-guppi-into-an-empty-project`: not read, no tag `prod-x.y.z`; deferred by case 831 · brief · case 843
  - near `estimate-guppi-package-is-ready-after-the-install`
- [-] C6 — Failed `estimate-harness-pipeline`: not read at Retro of session 1739; deferred by case 833 · brief · defer case 849
  - near `estimate-guppi-tests-green`, `rule-lint`
- [x] C7 — Contradiction: `estimate-guppi-package-runs-from-its-own-folder` against the example `tests/` of Case 819.2 in `rule-page-generation` and `estimate-generate-rewords` · brief · case 840
  - near `rule-page-generation`, `rule-guppi-package`
- [x] C8 — `estimate-clean-branch-ships-the-tests`: its reading waits for a tag `prod-x.y.z`; defer it into `backlog.md` · brief · case 844
- [x] C9 — `estimate-clean-branch-writes-the-session-files`: its reading waits for a tag `prod-x.y.z` and an install in an empty project by hand; defer it into `backlog.md` · brief · case 845
  - near `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [x] C10 — `estimate-guppi-package-is-ready-after-the-install`: its reading waits for a tag `prod-x.y.z`; deferred by cases 831 and 832 · backlog · case 846
- [x] C11 — `entity-sprint-plugin`: the milestone line of the sprint page still names `prod-2`; deferred by case 830 · backlog · case 847

Backlog: 19 items

## Work

- [x] W1 — `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets` · brief · work

## Ask
