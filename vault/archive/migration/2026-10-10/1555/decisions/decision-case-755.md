---
type: decision
case: "755"
status: archived
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-10-10/1555/ledger.md#case-755
sprint: migration
created: 2026-10-10
tags: [sprint, workflow]
---

## Problem

The sprint `migration` has reached its last milestone, the close. The close needs its readings sorted and taken, a choice for each Estimate still unread after Work Mode, and the close line that the librarian runs.

## Recommend

- **When is the group 2 check read**
  - Recommended: (a) read at Retro of this session, with the close line not naming it.
  - Answer: agreed, (a).
- **What happens to the five checks of groups 3 and 4**
  - Recommended: (a) carry all five by `--carry`, to be read by the session that opens the next sprint.
  - Answer: agreed, (a).
- **What to do about the lint-clean check that will fail**
  - Recommended: (a) read it as it stands; a `failed` reading goes to the archive with the sprint page, its status kept.
  - Answer: agreed, (a).
- **Is the old migration plan deleted in this session**
  - Recommended: (a) delete it in Work Mode, before the last commit and `make test`.
  - Answer: agreed, (a).
- **Change**
  - Asked: the findings of `/pre-spec` — the `then` line on a `failed` Estimate worded as the code does it, the count of the Estimates of `entity-sprint-migration` fixed, `estimate-skill-sprint-close-leads-the-closing-session` named, and the other moves of the close named; and a `by hand` task in Work Mode that runs the preview of the close with the same `--carry` flags, a refusal in it a stop for the person's word.
  - Taken: the four findings fixed in `context`, `given` and `then`; the preview task added, with what it expects set by the question below.
- **What the preview in Work Mode should show**
  - Recommended: (a) expect the lines "not settled" for exactly the three Estimates of the sprint page and `estimate-sprint-close-takes-the-readings-in-groups`, and stop Work Mode on any other refusal line.
  - Answer: agreed, (a).

## History

- 2026-10-10 created · raw/2026-10-10/1555/ledger.md#case-755
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
