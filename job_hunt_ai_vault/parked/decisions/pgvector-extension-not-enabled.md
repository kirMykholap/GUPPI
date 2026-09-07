---
title: "The pgvector image is in place but CREATE EXTENSION vector has not been run"
type: decision
status: current
authority: vector-extension
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [data, architecture]
---

# `CREATE EXTENSION vector` has not been run

The `pgvector/pgvector:pg17` image is in place. The extension is **not** enabled.

**Plan B's first migration must enable it before any `VECTOR(1024)` column.** This is an
obligation rather than a limitation: nothing today needs it, and the day something does, it will
fail at the column definition rather than at the image.

**This page is about the database, not about retrieval.** Whether the vault should be searched by
embedding at all — deferred, with the evidence that would reopen it — is
[[vectors-are-deferred-not-rejected]].

## What "plan B" means, since three pages now depend on it

As of 2026-08-12 the project has shipped plan A and the slices after it. **Plan B is the résumé,
the theses and the matching; plan C is measurement and automation. Neither document is written.**
Matching a vacancy against a résumé does not exist in the tool at all.

Two other pages defer work to plan B by name — a symmetric `salary_raw`
([[salary-cannot-be-reparsed]]) and the pair's own `first_seen_at`/`last_seen_at`
([[sorting-reads-objective-dates-only]]) — so "wait for plan B" is a real address rather than a
figure of speech, but it is an address with no document behind it yet.
