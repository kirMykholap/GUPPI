---
title: "A frontmatter value outside its schema's list is red, not an advisory"
type: decision
status: archived
authority: schema-value-enforcement
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/decisions/_schema.yaml"]
tags: [record-schema, harness, vault]
---

# The ruling, 2026-08-19

> **owner: a value outside the schema's list is red, not advisory** — `basis: banana` must not pass.

**Rejected: leaving the gate enforcing presence alone**, which is what it had done since `basis` was
promoted into `required:` on the owner's ruling of the same week
([[the-frontmatter-core-is-fixed-and-updated-joins-it]], [[the-per-folder-frontmatter-schema]]).
Presence without a legal set is a field every author guesses the values of, which is the failure the
register admission test exists to stop
([[a-field-with-no-register-produces-unique-values-by-default]]).

## Why red rather than an advisory

**Advisory is this store's shape for a verdict whose repair moves an address**
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]). Repairing a wrong `basis:`
moves nothing — it is one word on one page, and there is no sweep to schedule. The asymmetry that
justifies the softer verdict is simply absent here.

**And the field it protects is the one conflict resolution rests on.** `basis` ranks two pages that
disagree; a page whose `basis` is a word nobody defined ranks against nothing, silently and in the
direction of looking authoritative.

## Where the list lives, and what it obliges

**In `values:` inside each folder's `_schema.yaml`** — the mechanism and the shape it was chosen
over are [[the-legal-value-list-lives-in-each-folders-schema]]. The gate builds the legal set in the
same `awk` pass that reads the key set and prints a red verdict for a value outside it
([[a-fields-legal-values-live-beside-its-legal-keys]]).

**A `values:` header that parses to nothing is red too.** A silent empty set passes everything, in
the direction that hides a defect — the same permissive-failure argument the missing-schema verdict
was written on ([[a-denominator-is-walked-off-the-input-list]]).

**What it closed:** [[the-per-folder-frontmatter-schema]] ended on *"Still not enforced: the value.
The schema says `basis` must be present; nothing says it must be one of the five. `basis: banana`
passes."* It does not pass any more.
