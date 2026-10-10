---
type: decision
case: "245"
status: archived
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-18/1957/ledger.md#case-245
sprint: migration
created: 2026-09-18
tags: [sprint, workflow]
---

## Context

`entity-sprint-migration` holds the milestones of the sprint under `## Milestones`; Slice 3b has two items, `rule-work-mode` and `rule-subagent-guppi`. Case 238 deferred `insight-workflow-code-live-before-the-page-it-reads` to Slice 3b, but the milestone does not name it, so the brief (229.4 leaves out only what the sprint page names) and `/hi` carry it as an item of its own. `guppi sprint` ticks an item by the status of its page: `DONE = {built, passed, archived}`; an Insight `actioned` is not in it, and as a line `- [[insight-…]]` of its own it would never close. The Case touches no Estimate: the render of `sprint.md` does not change, the text of one item does.

## Problem

Where on the sprint page to name the Insight so that it goes with `rule-work-mode` and does not stand as a separate item.

## History

- 2026-09-18 created · raw/2026-09-18/1957/ledger.md#case-245
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
