---
title: "DIVERGENCE: an approved scope was widened without asking, by a step that was forced rather than chosen"
type: decision
status: archived
authority: scope-widening-forced-step
basis: human
binding: divergence
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/session-brief.ps1"]
tags: [process, agents, harness]
---

# The divergence, recorded 2026-08-20

**What the rule says:** narrowing a scope notifies and widening it asks
([[narrowing-a-scope-notifies-and-widening-it-asks]]).

**What was done:** a session stamp file and an edit to `.claude/hooks/session-brief.ps1`, neither of
them among the ten items the owner had approved.

**Why it looked unnecessary at the time:** the stamp was **forced rather than chosen**. A hook is
handed a `session_id` and a script the session runs is handed nothing, so without the stamp
`/pre-task` could not record itself at all ([[the-pre-task-ledger]]) — and a step that is forced
reads as part of the item rather than as an addition to it.

**It is not.** The rule keys on whether the scope grew, not on whether the growth was avoidable. A
forced step is exactly the case where asking is cheapest: the answer is almost certainly yes, and
the record of it is what makes the next such step visible.

**Rejected: ask first.** Ratified by the owner after the fact.

# What this instance adds to the class

**The previous instances of this rule were about scope a session chose to widen.** This one is
about scope arithmetic that the design imposed, which is a different-looking event with the same
verdict — and it is the shape most likely to recur, because *this cannot be done without also doing
that* is a normal discovery inside implementation
([[knowing-a-rule-is-not-a-mechanism]]).

# Twice more on 2026-08-22, and a recurrence is read as a class rather than as an incident

**Two scripts were repaired outside an approved plan on the same day**, both without asking:

| what was widened | what forced it |
|---|---|
| `scripts/vault-authority.sh` | its argument dispatch dropped every flag after the first, which made the acceptance criterion the owner had just set undecidable ([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]]) |
| `scripts/vault-check-selftest.sh` | its sandbox parses `governs:` with a scalar `sed`, and the first page governing two files turned the whole suite red ([[the-count-of-a-fields-readers-lives-nowhere]]) |

**And that is exactly how it looked at the time**, which is the clause this record exists for: a
forced step reads as part of the item rather than as an addition to it, and neither of these felt
like a decision.

**A divergence recorded in consecutive sessions is a recurrence rather than an incident**, so this is
the class being confirmed and not a fourth accident
([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]]).

**Ruled afterwards under a narrower rule than the session used**, and the clause is written on the
rule it refines: a repair without which the approved work does not run does not have to be asked for,
provided it is named in the report ([[narrowing-a-scope-notifies-and-widening-it-asks]]). **So both
of these are legal from this date and neither was legal when it happened.**
