---
title: "`grill-me` — the owner's interview skill, added mid-session on 2026-08-16"
type: entity
status: current
authority: interview-skill
basis: code
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", ".claude/skills/grill-me/SKILL.md"]
tags: [agents, process]
---

# What it is

| Property | |
|---|---|
| Path | `.claude/skills/grill-me/SKILL.md` |
| Appeared | 2026-08-16, **added by the owner mid-session** |
| Kind | a skill — a role mask running in the session's own context, not a dispatched subagent ([[a-skill-is-a-mask-and-a-subagent-is-a-body]]) |
| Landed in git | `d46655c`, together with the journal and the spec of that session |

**It interviews in rounds.** Four moving parts:

- a **design tree** of what has to be settled;
- a **frontier** of questions whose prerequisites are already settled — nothing beyond it is asked;
- **each question carries a recommended answer**, so the owner reviews rather than composes;
- **facts are gathered by the interviewer**, not asked of the owner.

## What it was used for, and what it produced

**It drove the whole second half of the session of 2026-08-16** — the one that produced
[[the-harness-is-compiled-not-maintained]], [[the-frontmatter-core-is-fixed-and-updated-joins-it]],
[[raw-holds-testimony-and-artefacts-are-frozen]] and
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]], with the design itself written
into `docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md` as each answer was settled.

**Its method, and the evidence that the method rather than the tool is what mattered**, is
[[interviewing-in-rounds-asks-only-what-is-unblocked]].

## What is worth knowing about it

**It is the owner's, not the librarian's.** A skill is a harness file, so nothing in the vault
writes it, and it is one of the files the harness build would eventually render into
([[the-harness-is-compiled-not-maintained]], [[marked-regions-and-the-prose-outside-them]]).

**It is short.** Twenty-two lines, which is worth recording beside what it produced: the leverage
came from the shape of the questions and not from the size of the instruction.

# It is the third carrier of the frontier, named 2026-08-30

**`grill-me` EXTENDS the frontier.** The owner closed the three-way collision on the word that day:
`sprint.md` is the frontier **between sessions** and where a deferred pointer lands, `brief.md` is its
**view** at session start generated from `sprint.md`, and this skill **extends** it with what an
interview opens ([[the-frontier-is-one-concept-with-three-carriers]]).

**So the boundary of questions inside a grilling was never a different frontier** — it is the same one,
grown. That is what the ruling settles, and this page had used the word without knowing which of the
three it meant.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
