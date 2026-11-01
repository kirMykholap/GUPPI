---
type: decision
case: "989"
status: current
update: ["[[rule-spec-box]]", "[[estimate-spec-box-runs-a-conserved-spec]]"]
origin: raw/2026-11-01/1721/ledger.md#case-989
sprint: plugin
created: 2026-11-01
tags: [session, workflow, git, harness, render]
---

## Problem

The check of `/box` waits for a run that no session plans, so `rule-spec-box` stays `draft`, `guppi check` reports it, the build of the clean version is refused, and the Purpose points to the second part of `/box` on a closed sprint page.

## Recommend

- **How the waiting check of /box gets read**
  - Recommended: (a) a trial run on a copy of the repository, in this session's Work Mode.
  - Answer: agreed, (a).
- **Where the page points for the second part of /box**
  - Recommended: (a) to the note on the live sprint page `entity-sprint-plugin`.
  - Answer: agreed, (a).
- **Whether the second part of /box enters this Case**
  - Recommended: (a) no, it stays a note on the sprint page.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the person agreed that the trial of `/box` runs after the librarian's run of this session, since `.claude/skills/box/SKILL.md` is rendered only then, and not in this session's Work Mode.
  - Taken: the method of `estimate-spec-box-runs-a-conserved-spec` waits for that librarian's run, and the task that stopped Work Mode for the trial is gone.

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#case-989
