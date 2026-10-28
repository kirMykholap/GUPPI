# Frontier — 2026-10-28, session 1907

## Cases

- [-] C1 — `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, CI writes a clean version of the project to a branch of its own; what remains: the owner pushes `plugin` and a tag `prod-x.y.z`, and the CI run is read; while a page with `core: true` stands `draft`, that run writes nothing to `prod` · sprint · defer
  - near `rule-clean-branch`, `estimate-clean-branch-writes-the-session-files`, `estimate-clean-branch-ships-neutral-texts`
- [x] C2 — The growing context of `case-guppi`, put off on `rule-orchestration` by Case 884 · brief · case 895
  - near `rule-orchestration`
- [x] C3 — `estimate-clean-branch-ships-neutral-texts` (failed): its reading of 2026-10-17 lists sentences true only in the repository of GUPPI; put off by Case 891 · brief · case 893
  - near `rule-clean-branch`, `rule-guppi-package`, `entity-guppi`
- [x] C4 — A defect: `.guppi/tests/test_casecheck.py` lines 2695 and 2740 hold `Case 5`, which the `ship` check of `guppi check` names as a reference to a case · brief · case 892
  - near `rule-clean-branch`, `rule-lint`
- [x] C5 — `case-guppi` asks the person for permission to write its case file: the main conversation stands in plan mode, so the subagent stays in plan mode whatever its `permissionMode`, and `permissions.allow` names no `cases/` path · person · case 894
  - near `rule-orchestration`

Backlog: 17 items

## Work

- [x] W1 — `estimate-case-build-reads-no-sibling-file-mid-send`: its event is seen in the handoff of 0118 (Cases 889 and 890 built side by side, a second pass) · brief · work
- [x] W2 — `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: its event is seen in the handoff of 0118, as above · brief · work

## Ask

- [ ] A1 — `estimate-guppi-package-is-ready-after-the-install` — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`? · brief
