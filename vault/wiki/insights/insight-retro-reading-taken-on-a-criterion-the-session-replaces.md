---
type: insight
pattern: The Retro takes the readings a list asks for — a read line of an older Spec, the Work list of the brief — and writes each without holding its slug against the Cases of the same session, so an Estimate whose Criterion a Case of that Spec replaces gets a reading on a Criterion nobody built; no check compares an estimate line with the Spec of its own session.
status: open
children: ["[[lesson-retro-reading-of-a-replaced-criterion]]", "[[lesson-retro-reading-of-a-criterion-this-spec-replaces]]"]
severity: 2
origin: raw/2026-09-25/1228/ledger.md#L44
sprint: migration
created: 2026-09-25
tags: [session, workflow]
---

## Pattern

The Retro takes the readings a list asks for — a read line of an older Spec, the Work list of the brief — and writes each without holding its slug against the Cases of the same session, so an Estimate whose Criterion a Case of that Spec replaces gets a reading on a Criterion nobody built; no check compares an estimate line with the Spec of its own session. In session 1749 the Retro wrote `estimate-retro-loads` passed on the Criterion of 270.3 after 282 had replaced it (`lesson-retro-reading-of-a-replaced-criterion`); in session 1228 it wrote the reading of `estimate-frame-check-finds-a-contradiction`, whose Criterion Case 419.2 of the same Spec replaces and whose page it renames (`lesson-retro-reading-of-a-criterion-this-spec-replaces`).

## Proposal

A suggestion, not a decision: a check at the Retro, or at the ledger write, could hold each `estimate[...]` line against the `then` blocks of the session's Spec and refuse a reading of an Estimate whose Criterion a Case of that Spec replaces or whose page it renames.

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#L44
