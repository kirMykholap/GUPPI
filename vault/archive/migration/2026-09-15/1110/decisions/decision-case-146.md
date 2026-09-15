---
type: decision
case: "146"
status: archived
defer: ["[[rule-lint]]"]
superseded_by: ["[[decision-case-156]]"]
origin: raw/2026-09-14/1633/ledger.md#case-146
sprint: migration
created: 2026-09-14
tags: [harness, workflow]
---

## Context

After session O `guppi lint` reports six new `orphan` findings: the six Insights actioned by 134, 135, 136.4, 137, 138, 139.2; after this session four more (142.3, 143, 144.3, 145.3). An orphan in `rule-lint` is a live entity, rule, estimate or insight no other live page names in its frontmatter. An Insight is named by its children's `insight` field; on `actioned` the cascade of 104.2 archives the children, and the Insight is left with no live inbound link by construction — while `rule-synthesis` and `index.md` §8 keep it live so a recurrence is caught by its `pattern` in the index.

## Problem

Two ratified norms — the children of an actioned Insight are archived; an actioned Insight stays live — together guarantee a third's finding, `orphan`, which catches nothing: the page has a pointer out (`addressed_by`) and its Decision page names it under `update`. The owner opened a wider question first: Obsidian's own graph sees the actioned Insight as connected (its `## Children` wikilinks reach the archived pages, its `## Addressed by` the Decision), and the notion of an orphan may follow Obsidian's once the frontmatter refs are wikilinks (Case 147). Which of the two definitions lint keeps is decided after that.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-146
- 2026-09-15 superseded by decision-case-156 · [[decision-case-156]]
- 2026-09-15 archived · superseded
- 2026-09-15 archived · cleanup
