---
type: decision
case: "672"
status: archived
update: ["[[estimate-generate-ticks-the-spec]]", "[[rule-page-generation]]", "[[rule-orchestration]]"]
origin: raw/2026-10-05/2103/ledger.md#case-672
sprint: migration
created: 2026-10-05
tags: [harness, workflow, ledger, session]
---

## Problem

When the person closes an Estimate as passed or failed by decision, `generate` leaves its `read` lines open in every Spec, and no later run ticks them. Eleven such lines stand open now in two Specs of earlier sessions, and the brief brings them back as work at every session.

## Recommend

- **Whether the script ticks a read line when a decision sets the state of a check**
  - Recommended: (a) a change that sets a check `passed` or `failed` ticks every open `read` line of that check in every live plan under `vault/raw/`, by the walk and the skips of a reading; a change that sets `pending` ticks nothing.
  - Answer: agreed, (a).
- **What happens to the eleven lines open now**
  - Recommended: (a) Work Mode of this session ticks them once by hand, and no other line changes.
  - Answer: agreed, (a).
- **Whether a ticked line shows that no reading was taken**
  - Recommended: (a) a plain tick; the page of the check records the decision.
  - Answer: agreed, (a).
- **How the one-time ticking of the eleven lines is checked**
  - Recommended: (a) a new check, read in Work Mode of this session by one search that must print nothing.
  - Answer: (b): no new checks are needed; whether the boxes are ticked or not is not critical. A `by hand` box in Work Mode runs the search.
- **Change**
  - Asked: at pre-spec the hand ticking was found to break the rule that Work Mode ticks no `read` line; the person answered that it is a one-time exception that needs no documenting.
  - Taken: the hand-ticking task stays, no rule or Estimate of Work Mode is named or changed, and `context` records the exception; the `by hand` search now runs over the two Specs alone, with the backtick before each slug.

## History

- 2026-10-05 created · raw/2026-10-05/2103/ledger.md#case-672
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
