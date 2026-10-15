---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-close]]"
purpose: Whether the session that opens the sprint plugin moves main to the last commit of migration by a fast-forward, goes on on the branch plugin, deletes migration and ticks the merge line of the closing Spec
method: "by hand, at the Retro of the session that opens the sprint plugin: git branch --list, git log -1 main against the last commit of migration that Work Mode printed, the uv run --project .guppi guppi test run of its Work Mode against work.md, and vault/raw/2026-10-10/1555/spec.md"
origin: raw/2026-10-10/1713/ledger.md#case-762
sprint: plugin
created: 2026-10-10
tags: [sprint, git, workflow]
---

## Criterion

When:
In Work Mode of the session that opens the sprint `plugin`, the agent runs the merge of `migration` into `main`, the task line that the closing Case of `migration` left unticked in `vault/raw/2026-10-10/1555/spec.md`.

Then:
`main` moves to the last commit of `migration` by `git merge --ff-only`, and no merge commit is made.
**＋** The agent makes the branch `plugin` from `main`, switches to it, and deletes `migration` by `git branch -d`.
**＋** The rest of Work Mode runs on `plugin`.
**＋** `uv run --project .guppi guppi test` on `plugin`, right after the switch, fails no test that `## Baseline` of `vault/raw/2026-10-10/1713/work.md` does not hold.
**＋** The merge line in `vault/raw/2026-10-10/1555/spec.md` stands ticked.
**－** When `git merge --ff-only` or `git branch -d` refuses, the agent stops on the first condition of `vault/wiki/where-to-stop.md`, a fork that no ratified Case decides, shows the refusal, and the run goes on from where it stopped after the person's answer.

## Result

2026-10-10, Retro of session 1713, from what its Work Mode printed: `git switch main` then `git merge --ff-only migration` printed "Updating 047a6125..ab8be60f / Fast-forward", no merge commit; `git switch -c plugin`, `git branch -d migration` printed "Deleted branch migration (was ab8be60f)"; `git branch --list` main and plugin, current plugin; `git log -1` main and plugin both ab8be60f; `make test` on plugin right after the switch 1490 passed, 6 skipped, exit 0, and the Baseline of work.md holds no failing test; line 78 of vault/raw/2026-10-10/1555/spec.md stands ticked; not exercised: a refusal of the merge or of the deletion

## History

- 2026-10-10 created · [[decision-case-762]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1713/ledger.md#L20
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
