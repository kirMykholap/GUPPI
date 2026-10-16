---
type: decision
case: "846"
status: current
update: ["[[estimate-guppi-package-is-ready-after-the-install]]"]
supersedes: ["[[decision-case-831]]", "[[decision-case-832]]"]
origin: raw/2026-10-16/0104/ledger.md#case-846
sprint: plugin
created: 2026-10-16
tags: [plugin, harness]
---

## Problem

The check of the install has never been read. Its `when` installs from the branch `prod`, which no build has written, while its `method` reads a local copy. That copy needs a tag `prod-x.y.z`, which does not stand yet.

## Recommend

- **Which install does the check describe?**
  - Recommended: (a) the local copy: the `when` names the folder that `guppi ship --allow-draft` writes, added as a catalogue, and the result lines stay. The Criterion is replaced whole and set `pending`.
  - Answer: agreed, (a).
- **How does the reading make `uv` look missing?**
  - Recommended: (a) the same machine: Claude Code started from a terminal whose `PATH` holds no folder of `uv`.
  - Answer: agreed, (a).
- **Does the reading make `uv sync` fail on purpose?**
  - Recommended: (a) yes: a third empty project, with Claude Code started from a terminal with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder.
  - Answer: agreed, (a).
- **Does this reading share its install with the other install checks?**
  - Recommended: (a) yes: the local copy and the empty project with `uv` may be the same as those of the other install readings of the batch.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec`: the readings by hand need steps that only the person can take, and the Case named neither the person's answer nor a `stop:` task. The person agreed to one `stop:` task in this Case for every install by hand of the batch, after the agent builds the copy and runs its own parts, with the four projects in one go, and to a `method` that names the person's answer.
  - Taken: the `method` names the agent's part and the person's answer; a task by hand writes the copy after the tag; one `stop:` task, before the push of the tag, holds the four projects of Cases 843, 845 and 846; `given` names `rule-where-to-stop`.
- **Change**
  - Asked: at `/pre-spec`, the push of the tag stands in the new Case 850, not in Case 847; and the `stop:` task also reads the output of `/guppi:install` and the files of the project with `uv` and of the project with its own `CLAUDE.md` against the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project`, since Case 843 no longer holds a reading task before the push.
  - Taken: the `stop:` task names the push of Case 850 and reads those two projects against that Criterion, right after the installs; `context` names Case 850.

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-846
