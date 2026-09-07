---
title: "`/ingest` runs after `/handoff` at the end of a session, and the end-of-session skill is renamed"
type: decision
status: current
authority: ingest-cadence
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "CLAUDE.md"]
tags: [vault, process, agents]
supersedes: [[ingest-is-batched-at-the-retrospective]]
---

# Decided 2026-08-16, in the second session of that day

**`/ingest` runs after `/handoff`, at the end of a session** — the cadence the repository's
`CLAUDE.md` has stated all along.

> [!NOTE] CONTRADICTION — RESOLVED
> [[ingest-is-batched-at-the-retrospective]], decided the same day in the earlier session, said
> `/ingest` **moves to the retrospective** and runs once over every journal written since the
> last one. Both pages were `current`, both `basis: human`, both dated 2026-08-16. **The owner
> retired that page on 2026-08-17 and this one stands**, taking `authority: ingest-cadence` with
> it. What the retired page measured is not lost: it is carried below, in the one form that
> survives the cadence going back to per session.

## The ambiguity it exposed, which is the more useful half

**"Retrospective" names two different rituals** in this project — the one at the end of every
session, and the one at the end of every sprint. The earlier decision put `/ingest` on "the
retrospective" and read it as the sprint one; the repository's `CLAUDE.md` reads it as the session
one. One word, two cadences, and nothing distinguishing them.

**The owner's decision is to rename the end-of-session skill** so the word stops meaning two
things. Which name it takes is not settled.

## What survives of batching

**Batching survives as the shape of a single dispatch:** one dispatch, sources compiled one at a
time inside it. The measurement the cadence argument rested on — a librarian dispatch costs 15-30
minutes and the fixed cost dominates ([[agent-round-trip-cost]]) — **only holds for one dispatch**,
so "one at a time" stays true of compilation and stops being true of dispatch.

That is also what the divergence between the ingest skill and the earlier decision was measuring:
the skill's line *"one source at a time - never batch several handoffs"* is right about compilation
and wrong about dispatch, which is why it read as a flat contradiction
([[no-rule-reads-a-harness-file]]).

## What it obliges

- **Step 8 of an ingest compares a journal against the tree**, and at this cadence the tree has
  moved less, which is the one thing the per-sprint cadence made worse
  ([[fidelity-to-a-source-and-fidelity-to-the-tree]], [[staleness-checks-run-at-different-times-and-ask-different-questions]]).
- **The brief's growth signal is sampled every session again** ([[the-growth-signal-is-the-brief]]).
- **`.claude/skills/ingest/SKILL.md` still says the opposite** and is one of the two files the
  marked-region markup starts with ([[marked-regions-and-the-prose-outside-them]]).

## Performed 2026-08-17, and the open half is now closed

**The retirement happened.** [[ingest-is-batched-at-the-retrospective]] is `deprecated`, carries
`superseded_by:` this page, and sits in `archive/`. This page holds `authority: ingest-cadence`.
**Rejected: keeping both with a resolved note**, which leaves two live answers to one question.

**The name is chosen.** The rename this page recorded as undecided was settled the same day: the end
of a session is a **retrospective**, `/handoff` follows it, and the sprint-level ritual is renamed
*sprint retrospective* ([[the-end-of-a-session-is-a-retrospective]]).

**Four live citations were left arguing from an archived page**, which is
[[a-live-page-can-argue-from-a-deprecated-one]] happening again — this time **caused by a write**
rather than found in one. Each is annotated where it stands:
[[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]] row 6,
[[no-rule-reads-a-harness-file]] row 5, [[agent-round-trip-cost]] for the cost arithmetic, which
survives, and `tags.md` in a definition.

**What the divergence against `.claude/skills/ingest/SKILL.md` is now about.** With the batched page
retired, the skill's line *"one source at a time — never batch several handoffs"* is **correct about
compilation**; the disagreement is only about dispatch, which is what this page already says. The
skill has since been rewritten to say both halves.
