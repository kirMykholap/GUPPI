---
title: "Telling an unfilled retro template from a written retro"
type: proposal
status: idea
authority: unfilled-retro-detection
basis: inference
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", ".claude/skills/retro/SKILL.md", ".claude/templates/retro.md"]
tags: [process, agents, harness]
---

# Raised 2026-08-19, and not built

**The state it detects** is the one nobody named: a retro file that exists, is the right size, opens on
the right heading, and says nothing
([[an-unfilled-retro-template-is-worse-than-an-absent-one]]).

## The predicate, and it is one line

**A retro has not been written if either holds:**

- **its frontmatter still reads `session: YYYY-MM-DD`** — the template's own placeholder, which a written
  retro replaces by construction;
- **it holds no verdict token outside the instruction paragraphs** — no `answered:`, `deferred:` or
  `could-not-close:` other than the ones the template names them in.

**The second clause is the load-bearing one.** A session that fills in the date and nothing else passes
the first, and the tokens are what the file exists to carry.

## Where it goes, and that is the open question

`/retro` is a skill, and **its wording is not a session's to change**
([[ask-before-weakening-or-working-around-a-rule]]). Three placements, and choosing is the owner's:

| where | what it buys | what it costs |
|---|---|---|
| the `/retro` skill's own text | the writer checks itself before reporting done | the party being measured is the party checking ([[the-librarian-writes-unattended]]) |
| `/handoff`, which reads the file next | an independent reader, at the moment the file is consumed ([[the-retro-writes-its-own-transit-file]]) | the retro is already over |
| a hook on the write | mechanical, and it fires at the moment of the defect | a fourth hook, and this project has already priced what a hook costs to get right ([[session-hooks]]) |

**The middle one is the cheapest honest option** and is offered rather than chosen.

## Why it is worth building at all

**The failure the skill anticipates is the failure it defends against.** It anticipates silence, and
silence is visible to `test -f`; this state passes that and every other cheap check
([[knowing-a-rule-is-not-a-mechanism]]).

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

## The predicate is per file, and the family it belongs to needs one verdict per open line — 2026-08-26

**The lessons collector returned this as an append rather than as a new page.** What it found is
that this proposal's predicate answers *was this file written* and the family around it asks a
different question: **whether each line that was opened was closed.**

**The two are not the same check and the second is the one that keeps failing.** A retro can be
written, complete, and still leave a question raised and never answered — which is a state
`test -f` and every content predicate on this page pass without a murmur
([[a-question-asked-is-not-a-question-answered]]).

**The session of 2026-08-26 is the worked example.** Eight exchanges of a retro produced twenty-one
decisions, four measurements and three of its own errors, and **not one `VAULT-FEEDBACK` block was
filed** — a written retro with a silent channel
([[divergence-the-retro-filed-no-feedback-block-while-it-ran]]).

**Nothing on this page is withdrawn.** The per-file predicate is still the cheapest honest option
for the failure it was written against, and this note names the one it does not reach.
