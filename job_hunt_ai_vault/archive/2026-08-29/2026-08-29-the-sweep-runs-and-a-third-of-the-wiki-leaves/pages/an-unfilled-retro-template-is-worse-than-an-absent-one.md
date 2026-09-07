---
title: "A retro file that is an unfilled template is worse than an absent one"
type: lesson
status: archived
authority: unfilled-retro-template
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", ".claude/skills/retro/SKILL.md", ".claude/templates/retro.md"]
tags: [process, agents, harness]
---

# The incident

**The previous session's `.superpowers/sdd/retro.md` is an unfilled copy of the template.** Stamped
02:38 on 2026-08-19, it still carries `session: YYYY-MM-DD` and every instruction paragraph, and the
only occurrences of `answered:`, `deferred:` and `could-not-close:` in it are **the ones inside the
instructions**.

# The third state, which nobody named

**The `/retro` skill states its own failure mode as silence** — *"a session that skips this skill
produces no file at all, which looks the same from the outside as a session with nothing to confess"*
([[the-retro-step]]).

This is neither of those two. **The file exists, it is the right size, it opens on the right heading,
and it says nothing.**

| state | visible to `test -f` | visible to a size check | visible to a reader who opens it |
|---|---|---|---|
| absent | **yes** | yes | yes |
| written and empty of confessions | no | no | yes |
| **unfilled template** | no | no | only on a careful read |

**Absence is at least visible to the cheapest check there is.** An unfilled template passes that one and
every other cheap one, and it passes them *by being exactly what a written retro looks like from the
outside*.

# Why this is the harness's problem and not the session's

**A skill that names its failure mode has done the hard half**, and it named the wrong one — which is
worth more than the incident: the failure a document anticipates is the failure it defends against, and
the one it does not anticipate arrives looking like success ([[no-rule-reads-a-harness-file]]).

**The transit file is designed to be consumed and gone** ([[the-retro-writes-its-own-transit-file]]), so nothing
downstream re-reads it and nothing notices it never said anything.

**Recorded rather than fixed**: `/retro` is a skill and its wording was not that session's to change
([[ask-before-weakening-or-working-around-a-rule]]). What would catch it is one line, and it is designed
on [[telling-an-unfilled-retro-from-a-written-one]].
