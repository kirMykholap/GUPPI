---
title: "The stack stays htmx, and React arrives as islands only where a screen's state must live in a tab"
type: decision
status: current
authority: frontend-stack
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md"]
tags: [architecture, htmx, frontend]
---

# The stack stays htmx

Decided in the slice 3 design conversation, recorded with its reasoning in that spec's §9, and
listed in the handoff among **decisions the next session should not relitigate**.

## htmx stays

A filter change costs **5.9 ms** against a 250 ms debounce. And the shapes differ: **server cost is
bounded by `PAGE_SIZE`, while client cost grows with the total.** That asymmetry is the argument —
not the millisecond, which is merely comfortable today.

## React arrives as islands, and only on one condition

> **When a screen's state must live in a tab rather than in the database.**

- **Qualifies:** the resume editor, the AI interview. Their state is genuinely in-tab.
- **Does not qualify:** matching with live re-ranking. It would mean moving that page wholesale,
  and its state belongs in the database.

This is the answer to "I am thinking of rewriting the view in React": the condition is not taste
or ambition, it is *where the state has to live*. A screen whose state can live in the database has
no claim on an island.

## Two riders

**No table library** — they all want to own the data client-side. Verified by downloading and
grepping seven of them; see [[server-renders-the-table]].

**A vendored stylesheet is not a dependency**, which is how `htmx.min.js` already ships. That is
what made the visual slice possible without touching the no-npm rule — and the visual slice then
chose not to vendor one anyway, for reasons of its own:
[[the-palette-grows-into-a-design-system]].

## What this does not settle

Whether the vacancy table itself stays server-rendered was deferred separately and is to be
revisited against a dressed table — [[server-renders-the-table]] holds that thread. And our own
JavaScript has its own boundary, narrower than this one: [[javascript-policy]].
