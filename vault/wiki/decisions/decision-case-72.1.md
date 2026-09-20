---
type: decision
case: "72.1"
status: current
update: [case-schema, index, glossary, "[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]"]
origin: raw/2026-09-12/ledger.md#case-72.1
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger]
---

## Context

Cases 70 and 71 showed the seam: the Estimate of a Leaf is signed in the `then` block
but reaches the vault only through a second ledger line the agent writes by hand, its
criterion is a second wording of the Case's `when` and `then`, and a contract change
rewrites it by hand with `replace` (the class of
`insight-workflow-contract-change-leaves-its-derived-text-stale`). The owner and the
agent settled the scheme in session J: one Leaf, one Estimate; the Case's `when` and
`then` are its Criterion, paragraph by Case; the Case's `problem` is its Context, once;
the agent writes `method` on a `create` and `contract: same|changed` on an `update`,
nothing else; the scripts do the rest.

## Problem

Six pieces of the harness say or do the old thing: the Case form (`case-schema.md`,
`index.md`, the glossary, the Render of `rule-case-protocol`), the two page schemas
(estimates, decisions), `materialize`, `generate`, `pretask --check` and `lint`. Each is
one contract; each is a sub-case below.

## Given

`case-schema.md`: "The Estimate's criterion is the `when` and `then` of the Case, copied
without change" — never done; a Leaf `create` holds a nested `estimate` with its own
`criterion` and `method`; "An `update` that changes a Leaf's contract carries, in the
same block, the `update` of its Estimate". `index.md` §3 "Paired Estimate on create"
shows two lines; §5 row `create — (Leaf)`: "Also log a paired `create` for its
Estimate"; §7: a contract change "updates the `Criterion` of that page's existing
Estimate ... in the same Case". Glossary row `Types`: "a Leaf brings a paired Estimate
`create`".
**＋** `estimates/schema.md` body: Context, Criterion, Method required, Result optional,
"`Result` is overwritten, not appended". `decisions/schema.md` body: Context, Problem,
Given, When; "What was decided (`then`) lives on the target pages, not here."
**＋** `materialize.find_item` reads a nested `estimate` only for a line with its slug;
`_lift_item` maps `context`, `criterion`, `method` into sections. `generate` writes an
Estimate from a `create` entry with `ref`, appends the slug to the target's `estimates`
(lines 278–281, 335–341), and on an `estimate` entry overwrites `## Result`.
`pretask.items_of` exempts a nested estimate; `pretask --check` has no finding for a
missing `method`, a missing `contract`, or two contracts in one Case. `lint` requires
`## When` on a decision page with a kind other than `defer`.
**＋** Slugs in `wiki/estimates/` are hand-named; a derived slug
`estimate-<target minus its prefix>` collides with none of the 34.
**＋** The Rule pages touched: `rule-case-protocol` (render, governs `CLAUDE.md`,
`estimate-case-protocol-loaded`), `rule-materialize` (check, `estimate-materialize-assembles`),
`rule-page-generation` (check, `estimate-generate-writes`), `rule-prespec` (render,
`estimate-prespec-reconciles`), `rule-lint` (check, `estimate-lint-catches`).
**－** Case 53.2 stays: a second Estimate on one target only for a condition that fails
and is fixed apart, named by `slug` in that Case. Case 68 (deferred, the `defer`-only
wording of `rule-prespec`) is not taken up here.
**－** MOC pages get an Estimate the same way, only when a Case gives them `method`;
without it, none.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-72.1
