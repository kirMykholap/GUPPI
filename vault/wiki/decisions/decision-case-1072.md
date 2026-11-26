---
type: decision
case: "1072"
status: current
children: ["[[decision-case-1072.1]]", "[[decision-case-1072.2]]"]
origin: raw/2026-11-26/2333/ledger.md#case-1072
sprint: plugin
created: 2026-11-26
tags: [sprint, session, harness, workflow]
---

## Problem

The check that `/retro` loads on a red test waits for a load that names no client, while only a load in the Claude Code CLI can show it. The rule now also forbids a transcript reading in an Estimate of a rule page that gets a new `method`.

## Recommend

- **How the check of /retro on a red test is taken**
  - Recommended: (a) split: a text check on `rule-retro`, the lines Tests and Style of `.claude/skills/retro/SKILL.md` read and the `--exit-zero` tests of `.guppi/tests/test_commands.py` run; and a one-off check on `entity-sprint-plugin` that reads a load of `/retro` in the Claude Code CLI in its transcript, before the close of the sprint `plugin`.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the words of the load leave Case 1072.1 so the load is signed once, in Case 1072.2. Asked of the person: how many load paths of `/retro` in the CLI Case 1072.2 checks, recommended (a), only the agent's call at the end of `/work`.
  - Taken: the `when`, `then` and `purpose` of Case 1072.1 name only the flag, the exit 0 of a red run and the line Ledger. By the person's answer, agreed (a), the `when`, `purpose` and `method` of Case 1072.2 name only the agent's call of `/retro` at the end of `/work`, and the typed `/retro` is not read.

## History

- 2026-11-27 created · raw/2026-11-26/2333/ledger.md#case-1072
