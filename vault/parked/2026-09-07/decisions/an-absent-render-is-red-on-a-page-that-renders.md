---
title: "An absent `render:` on a page that renders is red, printed by the injector and surfaced by the gate"
type: decision
status: current
authority: absent-render-verdict
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "scripts/vault-inject.sh", "job_hunt_ai_vault/wiki/concepts/_schema.yaml"]
tags: [harness, vault, record-schema]
---

# The ruling, 2026-08-20

> **owner: absent `render:` on a page that renders is RED** — printed by the injector and surfaced
> by rule 12 of the gate.

**This is what replaces the default.** [[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]
ruled that the injector's `region` default goes, and named nothing that takes its place; **the vault
held no verdict at all until the owner was asked**. The gap was surfaced by `/pre-task` before any
code was written, which is the one thing this record can say about the ritual that a brief cannot.

## What was rejected, and both refusals are mechanical rather than tasteful

- **An advisory.** The injector's only output channel is `say()`, which raises `problems` and forces
  exit 1, and rule 12 reads every `vault-inject: ` line into `note()`. **There is no non-red channel
  to put an advisory in**, so choosing one would have required a second ruling on rule 12's `case`
  statement in the same breath ([[the-injector-has-no-output-channel-that-is-not-red]]).
- **A silent skip**, which the vault forbids outright: a wrong record is acceptable and an invisible
  one is not ([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

## The removal landed in the order the check forces

1. `render` admitted to `optional:` in `wiki/concepts/_schema.yaml`, **with its `values:` list
   copied from `wiki/rules/_schema.yaml`**;
2. the librarian stamped `render: region` on the two `concepts/` pages carrying `governs:`, at
   line 6, where all nine rule pages carry it — injector counts byte-identical before and after;
3. the default in `scripts/vault-inject.sh` removed, and `""` spelled out as its own case arm.

**The order is load-bearing rather than stylistic** and the reason is the gate's own key set:
move 2 before move 1 is red on both pages
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

**The decider moved with it:** `scripts/vault-check-selftest.sh` went from `caught 133, missed 0` to
`caught 135, missed 0`, two cases and one fixture variant added — one for an absent field, one for a
value outside the schema's list. **The absent-field case was run against the unchanged injector
first and read `MISSED`**, which is what makes it a test rather than a decoration
([[a-case-that-passes-before-the-change-tests-nothing]]).

## The `values:` copy rides with this ruling and is obliged by nothing

**No page obliges a field newly admitted to a second folder to bring its legal-value list.**
[[the-legal-value-list-lives-in-each-folders-schema]] obliges the reverse direction only — a change
to an existing set is made in every folder's file.

**Without the copy, `render: banana` passes rule 2 on a `concepts/` page while failing on a `rules/`
one, and the injector cannot cover for it**: it reads `render` only after skipping every page with
no `governs:` ([[the-injector-reads-render-only-after-it-has-skipped-a-page-without-governs]]).

**It is written here rather than left as an inference** so that the next field admitted to a second
folder does not rediscover it. **Whether it becomes a rule is open and is the owner's.**
