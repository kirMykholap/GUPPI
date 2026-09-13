# Insight — page schema

`wiki/insights/schema.yaml`

Three blocks: **properties**, **body**, **history**. Always a MOC — a single unclustered lesson is just a Lesson.

**Insight is its own type, not a kind of Lesson.** It shares no fields with one: no `trigger`, no `root_cause`, no `source`, no Estimate. It has `children`, `severity` and `addressed_by`, which a Lesson does not. Two schemas under one name would have meant a page where most fields are inapplicable whichever kind it is.

Created by the librarian, never by a decision. It reaches the human through `brief.md` and becomes an ordinary ratified Case there.

## Properties

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `insight` | Page category. |
| `pattern` | yes | one line | The shared root cause, stated once. `insights.index` is built from it. |
| `status` | yes | `open` \| `actioned` \| `archived` | `actioned` when a ratified decision has addressed it. Not terminal — a new Lesson with the same root cause reopens it. `archived` when the cascade of `generate` finds an `open` Insight with no live child (case 104.3); an `actioned` Insight is never archived by the cascade, it is kept for the recurrence. |
| `children` | yes | list of slugs | The Lessons clustered here. Unordered. |
| `severity` | yes | integer | `count(children where status != archived)`. Recomputed by lint, never written by hand. |
| `addressed_by` | no | decision slug | The ratified decision that fixed the pattern. |
| `origin` | yes | date + session | When the librarian first clustered it. Unlike every other category this does not point at a ledger line — no decision created it. |
| `sprint` | yes | sprint id | |
| `created` | yes | date | |
| `tags` | yes | list | |

### Threshold

An Insight is created on the **second** Lesson sharing a root cause. One occurrence is an incident; two is a pattern.

The archive is not searched. A Lesson is archived only when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — and that Insight stays live with its `pattern` in `insights-index.md`; a recurrence after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight.

### Reopening

`actioned` is not an end state. When a new Lesson matches the root cause of an `actioned` Insight, the Insight returns to `open` and the new Lesson becomes a child. Previously archived children stay archived, so `severity` counts only the current run. No separate recurrence counter — the fact is legible from History plus the retained `addressed_by`.

### Slug

Area + pattern, as for Lessons: `insight-hooks-lifecycle-assumptions`.

## Body

| Section | Required | Content |
|---|---|---|
| `## Pattern` | yes | Expands the property: what the clustered lessons have in common, stated as a mechanism rather than a list of symptoms. |
| `## Proposal` | no | What the librarian suggests doing about it. A suggestion, not a decision — it is ratified, rejected or reshaped in a later Case. |
| `## Children` | yes | Script places Lesson links here. |
| `## Addressed by` | no | Script places the decision link here once fixed. |

## History

Appended by hook, never by an agent. Always the last section. Reopening is visible here.

## Example

```markdown
---
type: insight
pattern: Hooks were assumed to gate execution without checking which events can block
status: actioned
children: [lesson-hooks-sessionstart-cannot-block, lesson-hooks-subagentstart-no-gate]
severity: 2
addressed_by: decision-hook-capability-table
origin: 2026-09-15 · session-2026-09-15
sprint: 2026-Q3-s4
created: 2026-09-15
tags: [hooks, session]
---

## Pattern
Both failures came from placing a guard on an event that cannot block. The events were
chosen by when they fire, without checking whether a non-zero exit there actually stops
anything. The shape recurs because the two properties are independent and only one is
obvious from the event name.

## Proposal
A capability table in the session-start rule: for each hook event, whether exit 2 blocks.
Consult it before placing any guard.

## Children
- [[lesson-hooks-sessionstart-cannot-block]]
- [[lesson-hooks-subagentstart-no-gate]]

## Addressed by
- [[decision-hook-capability-table]]

## History
- 2026-09-15 created · clustered from 2 lessons
- 2026-09-19 status: open → actioned · decision-hook-capability-table
```
