---
title: "`pages.base` stays tracked and stops being watched: a session commits it without discussion"
type: decision
status: current
authority: pages-base-review
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "job_hunt_ai_vault/pages.base"]
tags: [vault, process]
---

# Decided by the owner on 2026-08-17

**He edits it often, through Obsidian, and its diff is not a review item.** A session commits it
without discussion and never treats a change to it as something to explain.

**Rejected: untracking it.** That would leave any other checkout without the view the vault documents
([[pages-base]], [[the-page-list-is-a-query-not-a-generated-file]]). Tracked and unwatched is the
combination he wants, and the two halves are independent.

## What it obliges

- **A dirty `pages.base` is never evidence that a write went wrong.** It had been reported as an alarm
  twice: Obsidian rewrote the `harness` view's state — a `type == "rule"` filter, two extra columns,
  a `file.name` sort — while the librarian was writing pages beside it, and the librarian correctly
  declined to revert it and incorrectly kept raising it
  ([[staging-by-wildcard-sweeps-the-other-partys-edit]]).
- **It is still the owner's file and not the librarian's.** Nothing here licenses writing to it; what
  changes is that its diff is not reported.
- **The change of standing is the whole content of this decision.** The file is unchanged in kind —
  an Obsidian base, a query rather than a list, evaluated when it is opened and therefore never stale.

**This does not extend to any other file the owner edits.** The registers stay the librarian's
([[the-one-writer-rule-covers-the-registers-too]]), and `sprint.md` stays the owner's to judge.
