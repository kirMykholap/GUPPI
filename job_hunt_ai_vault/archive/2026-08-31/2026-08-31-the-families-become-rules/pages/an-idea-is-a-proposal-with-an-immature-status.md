---
title: "An idea lives in `proposals/` with `status: idea` — the folder is the kind, the status is the maturity"
type: decision
status: archived
authority: idea-home
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "sprint.md", "scripts/vault-check.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [vault, record-schema]
---

# Decided 2026-08-17, and argued down from a different shape first

**An idea — pre-design, half-thought, not yet a proposal — is filed in `wiki/proposals/` and marked
`status: idea`.** The rule under it is general: **the folder is the KIND of a record and the status
is its MATURITY.**

**The owner first proposed `concepts/` with that status, and that was argued down on the record.**
Two reasons, and both are structural rather than aesthetic:

- `proposals/` exists as a folder precisely so that an intention **cannot** be filed as a record of
  something built — a failure that has happened twice here
  ([[proposals-are-a-folder-not-a-status]], [[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]);
- the schema knows two statuses and rule 2 of `vault-check.sh` enforces them, so a third value has
  to be added deliberately in both places rather than assumed into existence.

**The reconciliation:** a status *is* the right mechanism for *half-thought against designed* — the
owner's instinct was right about the axis — and the folder still has to carry the guarantee about
*kind*. Neither replaces the other.

## Decided and not built

`idea` is not in the schema and not in the check. Adding it is: the vault's `CLAUDE.md`, rule 2 of
`vault-check.sh`, and a case in `vault-check-selftest.sh`. **Until then an idea still has nowhere to
go**, which is the condition this decision was taken to end — it answers S2's second blocking
question and does not discharge it ([[what-the-harness-build-waits-on]]).

**What it will oblige when built:** `status: idea` is a third value in a field two rules read, and
[[the-proposal-status-cannot-tell-built-from-refused]] is already an open defect in the same field.
Whoever adds the value should read that page first — a status set that cannot say *refused* will not
be improved by also having to say *unripe*.

# The value is minted, and a verdict pairing it with `decided_by:` is ordered built — 2026-08-23

**`idea` is declared in `wiki/proposals/_schema.yaml` and is red in every other folder.** It was
decided on 2026-08-17 and unminted until then, so no page has ever been able to carry it and none
does ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**The owner ordered a verdict pairing `status: idea` with `decided_by:` — «нужно построить».** The
session had built it from his own sentence, dropped it the same hour on the argument that it makes
this field mean *authorisation* where the ruling above makes it mean *maturity*, and was overruled
twice ([[the-idea-and-decided-by-pair-is-ordered-built-and-the-back-fill-goes-first]],
[[a-verdict-pairing-the-idea-status-with-a-named-decision]]).

**Nothing here resolves that tension.** The ruling above still says the folder is the kind and the
status is the maturity; whether the pairing can be built without giving the field a second meaning
is the open question the design carries.
