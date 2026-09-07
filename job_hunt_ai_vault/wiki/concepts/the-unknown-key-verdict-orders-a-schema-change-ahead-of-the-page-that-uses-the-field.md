---
title: "The unknown-key verdict orders a schema change ahead of the page that uses the field"
type: concept
status: current
authority: schema-change-order
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/concepts/_schema.yaml", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [record-schema, harness, vault]
---

# The mechanism

**`vault-check.sh` builds its `allowed` key set from `required:` and `optional:` and nothing else**
([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]), **and the unknown-key verdict runs
through `note()`, which sets `fail=1`.**

**So a field on a page the folder's schema does not admit is red — on the page, not on the schema.**

# The consequence: a schema change has a forced order

Admitting a field to a folder and using it are two edits, and only one order is green:

1. the field is admitted to `required:` or `optional:` in that folder's `_schema.yaml`;
2. **only then** may a page in that folder carry it;
3. and code that defaulted the field stops defaulting last, once every page that needs it has it.

**Doing part of it is worse than doing none.** Move 2 before move 1 reddens every page that gained
the field, and the verdict names the page rather than the omission that caused it — a diagnosis that
points at the wrong file ([[failing-loudly-with-the-wrong-diagnosis]]).

**Exercised on the `render:` default removal, 2026-08-20**, all three moves in that order
([[an-absent-render-is-red-on-a-page-that-renders]],
[[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]). Move 2 stamped
`render: region` on the two `concepts/` pages carrying `governs:`, and the injector's counts were
byte-identical before and after — the stamp changed what the gate reads, not what the injector
writes.

# Why the order is load-bearing rather than stylistic

**The two halves of a schema change are owned by different writers.** The `_schema.yaml` is the
session's to edit ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]); the pages are
the librarian's ([[the-librarian-writes-unattended]]). **The ordering constraint therefore crosses a
handover**, and neither party can see the other's half go red from where it stands.

# Promotion has an order of its own, and it is the reverse of what a plan will assume — 2026-08-23

**Admitting a key and *promoting* one are two different sequences.** The section above orders the
admission; this one orders the move from `optional:` to `required:`, and it is written down in
`wiki/proposals/_schema.yaml` as a comment block rather than on a page of its own until now:

1. the key is legal and **optional**;
2. the back-fill — every page in the folder gains the field;
3. **only then** the promotion to `required:`.

**Required first turns the gate red on every page in the folder at once.** And
`lock-the-librarian.ps1` reads a red gate as a refusal to dispatch, which locks out the only writer
permitted to fill the field — so the deadlock is not merely inconvenient, it removes the party that
would clear it ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]],
[[the-librarian-lock-hook]]).

**The plan of 2026-08-23 had it backwards and `/pre-task` reversed it** before anything was written
([[a-pre-task-runs-between-the-plan-and-its-approval]]).

**Three fields have now taken this order**: `basis:`, `authority:` and `decided_by:` in
`wiki/rules/`. The first two are recorded in their folders' own schema comments; the third is
recorded on [[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]].

**The two orders compose and do not conflict.** Admission puts the key in `optional:` first;
promotion moves it to `required:` last. Between them sits the back-fill, which is the only step a
plan tends to price at zero.
