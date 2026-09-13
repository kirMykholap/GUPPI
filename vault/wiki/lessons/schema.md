# Lesson — page schema

`wiki/lessons/schema.yaml`

Three blocks: **properties**, **body**, **history**. Always flat — grouping is what Insight is for.

A Lesson is a recorded fact, not a ratified decision. It does not go through a Case and requires no ratification; the ledger hook writes it directly.

## Properties

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `lesson` | Page category. |
| `kind` | yes | `error` \| `knowledge` | `error`: something went wrong. `knowledge`: external material studied once so the source never has to be supplied again. |
| `root_cause` | yes | one line | Why it happened (`error`), or the mechanism the source claims (`knowledge`). Lives in properties because `lessons.index` is built from it, and clustering into an Insight compares exactly this. |
| `status` | yes | `new` \| `clustered` \| `archived` | `clustered` once it belongs to an Insight. Archived when its Insight is `actioned`. |
| `source` | `knowledge` | url or reference | Where the material came from. |
| `insight` | no | slug | The Insight this belongs to, once clustered. Written by the script. |
| `origin` | yes | `raw/YYYY-MM-DD/HHMM/ledger.md#L<n>` (the date form, `raw/YYYY-MM-DD/ledger.md#L<n>`, on pages born before 2026-09-13; case 103.6) | The ledger line. Unlike Entity and Rule, this points at a `lesson[...]` line rather than a `decision[...]` one. |
| `sprint` | yes | sprint id | |
| `created` | yes | date | |
| `tags` | yes | list | Includes what the material applies to, for `knowledge`. |

### Slug

**Area + cause**: `lesson-hooks-sessionstart-cannot-block`, `lesson-pricing-async-in-sync-tx`.

The area groups related lessons together in a plain file listing, and the cause makes near-duplicates visible before anyone opens the index. Naming by symptom was rejected: two unrelated failures often share one symptom, and the symptom is not what clustering compares.

### There is no Estimate

A lesson is a recorded fact: the trigger is the observation, and nothing about it is
checked again. An Estimate exists only for a page with a contract — an Entity or a Rule.
A `knowledge` claim is checked where it is leaned on: by the Estimate of the Rule built
on it (case 53.1).

### There is no `reviewed` status

An intermediate "the librarian looked at it" state records nothing useful — a lesson with no pair is simply still `new`, and will be reconsidered next session anyway. Only membership in an Insight is a real change of state.

## Body

| Section | Required | Content |
|---|---|---|
| `## Trigger` | yes | What happened (`error`), or what was read (`knowledge`). The full account — the one-line version is `root_cause` in properties. |
| `## Root cause` | yes | Expands the property: why this happened, or what the source actually claims and on what grounds. |
| `## Insight` | no | Script places the link once clustered. |

## History

Appended by hook, never by an agent. Always the last section.

## Examples

### error

```markdown
---
type: lesson
kind: error
root_cause: SessionStart cannot block, so nothing gated the first ledger write
status: clustered
insight: insight-hook-gating-assumptions
origin: raw/2026-09-08/ledger.md#L14
sprint: 2026-Q3-s4
created: 2026-09-08
tags: [hooks, ledger, session]
---

## Trigger
The first ratified decision of the session was written to `main` instead of the session
branch. Noticed only at handoff, when the librarian found a ledger line outside the
session folder.

## Root cause
SessionStart cannot block — exit code 2 is a no-op there. The guard had been placed on
SessionStart on the assumption that it behaved like PreToolUse. Nothing actually gated
the write.

## Insight
- [[insight-hook-gating-assumptions]]

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#L14
- 2026-09-15 status: new → clustered
```

### knowledge

```markdown
---
type: lesson
kind: knowledge
root_cause: Per-finding fix subagents each rebuild context and rerun the suite
status: new
source: https://github.com/obra/superpowers
origin: raw/2026-09-12/ledger.md#L07
sprint: 2026-Q3-s4
created: 2026-09-12
tags: [subagents, review, cost]
---

## Trigger
Read the subagent-driven-development skill while deciding how to structure our own
review step.

## Root cause
It dispatches a single fix subagent with the complete findings list rather than one per
finding. The stated reason is that per-finding fixers each rebuild context and rerun the
test suite, and in a real session that wave cost more than all the implementation tasks
combined.

## History
- 2026-09-12 created · raw/2026-09-12/ledger.md#L07
```
