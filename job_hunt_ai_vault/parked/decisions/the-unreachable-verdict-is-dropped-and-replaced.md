---
title: "The verdict comparing a marker's type against its page's `type:` is dropped as unreachable, and replaced by one that fires"
type: decision
status: current
authority: dropped-type-verdict
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# Decided 2026-08-18, during the build, and announced rather than asked

**The designed verdict cannot fire.** *A marker whose type disagrees with its page's `type:`* was
one of the two new red verdicts the owner approved. The type word picks the folder, and rule 2
already requires every page in a folder to carry that folder's singular — so the disagreement it
looks for is **rule 2 failing on that page**, not a second fault. Building it would have added a
case that passes for a reason unrelated to what it claims
([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**What replaced it is reachable, and is the likeliest way to misspell an address now that the type
is part of one**: where the slug exists under a *different* type, the same red names the folder the
page is actually in. `<!-- entity: x -->` against `wiki/decisions/x.md` gets told where `x` is.

**Rejected: build the verdict as specified.** Refused because a check that can only fire as a
second report of somebody else's failure is a green that examined nothing
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## This is a divergence, and it is recorded as one

The owner had approved **three** verdicts and **two** shipped. The substitution was announced in
the same turn, before building, and **not asked**. Under the rule derived from the same session it
is a legal notification rather than an owed question — a narrowed scope notifies, a replaced or
widened one asks ([[narrowing-a-scope-notifies-and-widening-it-asks]]) — and it is written down
here because *every recorded divergence in this project began with the rule looking unnecessary*.

## Where the design was wrong, and where it was read

The proposal that specified the verdict is retired
([[the-marker-carries-a-type-and-governs-is-read-as-a-field]]). Its unreachability survived a full
design pass, an owner's approval and a proposal page before anyone asked *when could this fire*;
it was caught at `/pre-task`, reading the code, and not by reading the proposal
([[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]],
[[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

# Second occurrence, same place — 2026-08-29

**Plan part F would have checked that a page named in any `supersedes:` is not itself `current`. Of the
36 `supersedes:` targets in the corpus, zero are live**, because the field is written in the same act
that completes the supersession. **The verdict could only ever have fired as a second report of
somebody else's failure, which is a green that examined nothing.**

**It is dropped, and the session understood it rather than the owner ruling it.**

**What makes this worth a dated section rather than a shrug**: the previous unreachable verdict — the
one this page is about — also survived a full design pass and an owner's approval before `/pre-task`
caught it by reading the code. **Twice now, in the same place in the process.** The refusal is cheap;
the design pass that precedes it is not.

**`supersedes:` is legal in all six folder schemas and is read by no verdict in `scripts/vault-check.sh`
at all** — it appears there once, inside a comment about link sweeping. So the field is available and
the check that would use it has nothing to catch.

**A slug correction, because the journal names one that does not exist.** The handoff cites
`the-verdict-comparing-a-markers-type-is-dropped-as-unreachable`; **that string is this page's title,
not a filename, and it resolves to nothing.** The lesson carrying the general form,
`a-verdict-that-cannot-fire-is-worse-than-no-verdict`, is in
`archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/`, which is why the
second occurrence lands here.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
