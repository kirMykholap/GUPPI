---
title: "Deactivation is profile-scoped because «the site closed this vacancy» cannot be known"
type: concept
status: current
authority: deactivation-scope
basis: human
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [deactivation, profile, data]
---

# Why deactivation is profile-scoped

`missed_checks` and `is_active` moved off the objective `vacancies` row onto the
profile↔vacancy pair — `profile_vacancies`, formerly `applications`.

**The reason is epistemic, not architectural.** "This vacancy was closed by the site" cannot be
known: **no profile sees the whole exchange.** What we observe is that a particular set of
searches stopped returning it.

So the honest statement is *"this profile stopped finding it"* — and that statement is
profile-scoped by definition. The schema follows the claim we can actually make.

This is the "why" beneath every rule in [[deactivation-cycle]]. Those eight conditions are what
"stopped finding it" means operationally; this page is why the sentence is phrased that way in the
first place.

It also explains a limitation that would otherwise look like a bug: a second profile meeting a
vacancy the first already knows is told «новых 0», because `stats.new` counts objective rows
rather than what is new *to this profile*. Objective facts stay objective; only the judgement is
scoped.

See [[deactivation-cycle]] for what the judgement does in practice.
