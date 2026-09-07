---
title: "Application statuses stay English identifiers inside a Russian interface"
type: decision
status: current
authority: status-vocabulary
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "CLAUDE.md"]
tags: [web, data]
---

# Statuses stay English identifiers

`new`, `applied`, `call` — in a Russian interface.

**They are identifiers, not copy.** The project's language rule puts product content the owner
sees in Russian and everything written into the repository in English; a status value is stored,
compared and queried, so it belongs to the second group even though it surfaces in the first.

Deliberate, and cosmetic only in the sense that it is visible.
