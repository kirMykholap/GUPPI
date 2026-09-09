---
title: "An unsourced number is dropped, not resolved by choosing one of the candidates"
type: decision
status: archived
authority: unsourced-figures
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-14
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md"]
tags: [vault, process, testing]
---

# Drop the quantity, keep the claim

**Decided by the owner on 2026-08-14**, on a concrete case: [[test-suite-wall-clock]] said suite
re-runs took "a large share of **the six hours** that slice took", while
[[how-a-slice-is-executed]], [[agent-round-trip-cost]] and the primary journal all say **eight to
ten hours** — and `grep` over both of that page's own sources finds no occurrence of "six hours" at
all.

**The owner does not know which slice the figure refers to and considers the number unimportant.**

**Rejected: picking between six and eight-to-ten.** A `basis: measurement` page carrying a number
its sources do not is the failure; replacing it with a *different* number the owner cannot vouch
for reproduces the failure with better manners. **Rejected equally: leaving it and adding a
caveat** — the number would keep being quoted, because quantities travel and caveats do not.

**Chosen:** the quantity is removed from the assertion and the claim it supported is kept — *"a
large share of that slice"*. If the slice is ever identified, the figure returns **named**.

**Applied by an agent to itself, 2026-08-15.** A librarian dispatch handed a brief containing two
figures corrected both against measurement rather than repeating them — 217 tag assignments was
stale by twelve, "35 python files" is 34 plus `app.css` — and then **declined to write a third
number that no source records and no measurement can now recover.** That is this rule working
without anyone invoking it, and it is the first instance of it being obeyed rather than imposed
([[how-a-slice-is-executed]] for what caught the other three errors in the same batch of
dispatches).

## What it obliges of the librarian

- **the correction is written, not silently applied.** Nothing is deleted here: the page keeps a
  dated note of what it used to say and why the figure went, so "why did this stop saying six
  hours" is answerable;
- **`basis: measurement` is a promise about provenance**, not about precision. A page carrying that
  value must be able to point at where each of its numbers came from — which is the rule
  [[a-stated-count-drifts-from-the-list-it-heads]] arrives at from the other direction, and the two
  are the same discipline: a number travels with its source or it does not travel.

# An invented denominator inside a design document, caught before publishing — 2026-08-29

**A first draft of the agent architecture said "181 of 313 live pages" for `entities/` and `concepts/`,
and the denominator was invented.** `wiki/` held **556** — `decisions/` 295, `concepts/` 138,
`proposals/` 46, `entities/` 43, `lessons/` 18, `rules/` 16 — measured off the tree the same hour.

**Corrected before the document was published, and recorded anyway**, which is the point of this page:
**a denominator nobody measured reads exactly like one that was.** Nothing in the sentence marked it as
a guess, and the correction happened because somebody counted rather than because anything flagged it.

**The count is decided by a command** — `bash scripts/vault-catalogue.sh` — and no copy of it belongs in
prose, which is why the figure above is dated where it stands
([[the-index-is-a-map-not-a-catalogue]], [[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
