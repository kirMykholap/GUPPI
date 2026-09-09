---
title: "The `governs:` branch widens and the branches beside it stay rules-only, each for its own reason"
type: decision
status: deprecated
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
tags: [harness, record-schema, vault]
superseded_by: [[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]
---

# Decided 2026-08-18: three branches, three fates

The retired design called this *"the drop of a gate"* and there are **three** branches behind it in
`scripts/vault-check.sh`, with three different correct outcomes. Executing that sentence literally
would have reddened the check ([[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]]).

| Branch | Fate | Why |
|---|---|---|
| `nogoverns` — a rule page naming no destination | **stays rules-only** | widening it makes `governs:` required on all 258 pages, and most of the corpus delivers nothing by design |
| `governs` — collect the field and build the slug-to-destination pairs | **widens** | it builds the pair table the address verdict joins against, so the verdict is blind outside `rules/` without it |
| `ruleclaim` — `authority:` may not sit beside `governs:` | **stays rules-only** | its argument is rule-specific: a decision and the rule stating it share a slug and would read as a contradiction ([[rules-becomes-a-type-of-its-own]]) |

**`governs` is the one that had to move**, and it is the one that made a `concepts/` page renderable
at all ([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]).

## What the narrow `ruleclaim` leaves open, on purpose

**Whether a non-rule page may carry `authority:` *and* render is unruled**, and keeping that gate
narrow is what preserves the question instead of answering it by accident from inside a script.
Today it is neither open nor closed — it is invisible — which is why it owes a page of its own:
[[authority-beside-governs-on-a-non-rule-page-is-unruled]].

**The first non-rule page to render deliberately carries no `authority:`** for exactly this reason
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]).

## The general shape

**A gate named in the singular can hold several rules.** Three branches read the same condition and
were counted as one thing by the page that priced the work, which is the same class of error as a
stated count drifting from the list it heads ([[a-stated-count-drifts-from-the-list-it-heads]]) —
here inside a design rather than inside prose.

---

*Retired 2026-08-19.* **The `ruleclaim` row of the table above is no longer true**: that branch fires
on any page carrying `authority:` beside `governs:`, and the successor carries the current reading of
all three branches ([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]).

**It was retired by its own argument.** This page kept the branch narrow so the question *may a
non-rule page own an `authority:` and render* would stay askable; the vault answered that question the
next day ([[authority-beside-governs-is-forbidden-on-any-page]]), and a gate held narrow to preserve
an answered question is a gate narrower than its rule.

**What is kept here and not repeated on the successor** is the ground for the other two branches as it
stood on 2026-08-18, and the general finding this page was written for: *a gate named in the singular
can hold several rules*.
