---
title: "description_is_full has no producer in production — the guard is correct and the case cannot arise"
type: decision
status: current
authority: description-fullness-producer
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [data, collection]
---

# `description_is_full` has no producer in production

Only `WorkUaParser.fetch_description` can download a full text. That method is **not declared in
the `BaseParser` contract** and **nothing in production code calls it** — only tests do.

So `description_is_full=true` cannot arise in the database today. The guard "a snippet never
overwrites a full description" ([[absent-values-never-overwrite]]) is correct and is held by a
test, but it describes a case that ordinary collection does not create.

**This is a legitimate stub for plan B, not a defect.** Recorded so that nobody reads the guard as
evidence that full descriptions are being collected, and so that nobody deletes the guard as dead
code.

It does not get in the way today.
