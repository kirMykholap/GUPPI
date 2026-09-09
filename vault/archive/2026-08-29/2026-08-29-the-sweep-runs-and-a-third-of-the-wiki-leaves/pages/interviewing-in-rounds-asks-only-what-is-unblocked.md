---
title: "Interviewing in rounds worked, and its discipline is the transferable part"
type: lesson
status: archived
authority: interview-discipline
basis: human
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", ".claude/skills/grill-me/SKILL.md"]
tags: [agents, process]
---

# What the round structure did, and what to keep if the tool changes

The whole second half of the design session of 2026-08-16 was run by an interview skill
([[grill-me-skill]]), and it worked: a session with no code produced a settled design for the
harness, a settled record schema, and a decision on what `raw/` is for.

**Three rules are the transferable part**, and none of them depends on the tool:

1. **Ask only the questions whose prerequisites are settled.** A design has a dependency order, and
  a question asked ahead of it collects an answer that has to be revisited — which is how a
  conversation produces the appearance of progress and no decisions.
2. **Give a recommended answer with every question.** It converts an open prompt into a review,
  which is the cheaper cognitive act and the one the owner has repeatedly said he can perform
  ([[the-owners-question-was-how-would-you-check-that]]).
3. **Go and find the facts rather than asking for them.** The interviewer measures; the owner
  decides.

## The evidence that rule 3 is load-bearing

**Four turns of that session changed a recommendation because a fact came back different from the
guess.** The recommendation was written first, the fact was fetched second, and the fact won —
which means those four decisions would have been taken wrongly had the question been asked instead
of the measurement being made. Two of them are on
[[measurement-settled-what-argument-could-not]].

**Recommending without checking is the failure this defends against**, and it is the same one the
store keeps recording from other directions: a plausible document that cannot be verified is
trusted ([[the-unreadable-mass-is-in-the-plans-not-the-vault]]).

## Where it sits beside what is already recorded

An interview is a **mask**, not a dispatch — it ran inside the session's own context, with its own
role, which is exactly the distinction the owner drew about the tooling
([[a-skill-is-a-mask-and-a-subagent-is-a-body]]). The cost profile is therefore the cheap one: no
round-trip, no isolated context to re-establish ([[agent-round-trip-cost]]).
