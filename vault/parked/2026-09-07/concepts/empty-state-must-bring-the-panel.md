---
title: "An empty state that points at a control must bring that control with it"
type: concept
status: current
authority: empty-state-recovery
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [htmx, filters]
---

# An empty state must bring along the control it points at

With every tag disabled, the empty table says «Включите хотя бы один в панели тегов выше». Doing
exactly that left both collection buttons disabled.

The chain: `can_collect` is read **at render time**; the tag toggle redrew the tags panel and the
chips but **not** the collection panel; and an idle panel does not poll
([[polling-only-during-a-run]]). So a disabled button raises no click, and **the page had no way
back to itself.**

Fixed by bringing the panel along out of band — the same technique the chips already used, for the
same stated reason.

## Two things this cost, both worth keeping

**The live check missed it**, because the walk's scenario re-enabled the tags through the CLI
rather than through the page. A walk that reaches a state by a different route than the user would
does not test the route.

**An empty state is a branch like any other and needs its cases enumerated.** Three different
situations pointed at a control that could not help, each found by a different pass: every tag
disabled *and* every chip cleared (the cure is the chip row directly above the table, not the far
panel); a profile whose chip row is empty (the marker claimed a chip set had been cleared, pointing
at nothing — see [[tags-set-marker]]); and the same page reached by a hand-typed `?tags_set=true`.
One message written for the case that prompted it is not an empty state.
