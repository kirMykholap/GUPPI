---
title: "`## Where things are` is deleted now, and a generator fills its place later"
type: decision
status: archived
authority: where-things-are
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
tags: [harness, process, vault]
---

# Decided by the owner on 2026-08-17, at `bdab5c9`

The dispatch-table decision left this block *"dropped or generated"*
([[the-repository-claude-md-becomes-a-dispatch-table]]). **He took the first half, and took it
first**: the block is gone from the repository's `CLAUDE.md` today, and a generator comes later.

**Rejected: correcting the block.** That is exactly what
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]] exists to refuse — a copy that has
drifted twice is repaired by removing it, not by making it right one more time.

## The four defects it was carrying, measured at `e478c19`

| What it said | What was true |
|---|---|
| the vault tooling is `vault-check.sh`, `vault-units.sh`, `vault-coverage.sh` | **two scripts behind** — `vault-catalogue.sh` and `vault-inject.sh` were missing (already on the record) |
| `.claude/` is `skills/`, `agents/`, `hooks/`, `settings.json` | **`templates/` omitted** — not recorded until this session |
| the vault is `raw/handoffs/`, `wiki/`, `brief.md`, `log.md`, `tags.md`, `index.md`, `sprint.md` | `wiki/rules/`, `pages.base` and `archive/` omitted |
| *"its directory name is the owner's to change and nothing may depend on it"* | **contradicts [[governs-is-a-path-from-the-repository-root]]**, which fixed the vault's directory name in `governs:` a day earlier — not recorded until this session |
| `docs/HANDOFF.md` — a pointer to the above | the file exists and the project no longer routes through it ([[docs-handoff-is-a-pointer-nothing-routes-through]]) |

**Two of those five were new instances** for the register on
[[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]], which stood at seven before this
session.

## What it obliges

- **The generator is owed, and it is not this block's alone**: the same mechanism — a marked region
  filled from the tree rather than from a page — serves `make help` and the map as well
  ([[a-generator-fills-a-marked-region-from-the-tree]]).
- **Until it exists, a session finds `src/` by looking.** That was weighed and accepted on the map's
  admission test: not knowing where `src/` is costs ten seconds of `ls`, which is *slower* and not
  *wrong* ([[the-sprint-belongs-in-the-map-and-the-map-has-an-admission-test]]).
- **The deletion is not itself a loss of knowledge.** Git records the tree better than any prose
  about it, which is the vault's own standing rule about what does not belong in it.
