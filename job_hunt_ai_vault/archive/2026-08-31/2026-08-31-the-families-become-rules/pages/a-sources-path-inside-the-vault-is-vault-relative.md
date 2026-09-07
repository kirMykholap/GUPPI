---
title: "A `sources:` path inside the vault is vault-relative, and one outside it is written from the repository root"
type: decision
status: archived
authority: sources-path-root
binding: prohibition
basis: measurement
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-archive.sh", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# Ruled 2026-08-20, and measured rather than chosen

**Inside the vault, vault-relative. Outside it, from the repository root.**

The corpus was already unanimous and nobody had written it down:

| what is cited | how it is written | how often |
|---|---|---|
| `raw/...` | vault-relative | 398 |
| `archive/handoffs/TEMPLATE.md` | vault-relative, its only instance | 1 |
| `scripts/...` | from the repository root | 173 |
| `.claude/...` | from the repository root | 97 |
| `docs/...` | from the repository root | 45 |

**Rejected: a single root for everything**, which would have moved 399 citations to settle a rule
nothing was violating.

## Why it stopped being habit and became a rule

**`scripts/vault-archive.sh` now depends on it.** It rewrites `sources:` lines by exact string
match ([[a-path-is-never-a-pattern]]), so the spelling of a path is an interface rather than a
style. A convention that held on habit and was written nowhere is one nobody can be shown to have
broken.

**It is not a new precedent** and it was kept rather than introduced — which is the honest framing:
the ruling records what the corpus does, so no page is wrong today.

## What it does not settle

**Rule 2 of the gate resolves a `sources:` path by trying both roots**, and that is deliberate
tolerance rather than agreement. `governs:` is the field that resolves against nothing else,
because the injector writes the file it names and a path meaning two files renders into the wrong
one.
