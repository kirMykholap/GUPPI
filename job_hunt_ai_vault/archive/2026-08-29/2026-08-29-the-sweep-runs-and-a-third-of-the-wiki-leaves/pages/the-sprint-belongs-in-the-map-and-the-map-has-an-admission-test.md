---
title: "The sprint belongs in the map, and the map admits an entry only when not knowing it makes the work wrong"
type: decision
status: archived
authority: map-admission
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
tags: [harness, process, vault]
---

# Decided by the owner on 2026-08-17. Not built.

**The sprint is an entity in the repository `CLAUDE.md`'s map, beside the vault and its librarian.**
Not the sprint's contents — `sprint.md` owns those — but the fact that a sprint exists and where it
is.

**And the map gets an admission test, agreed in the same conversation:**

> **An entry earns its place if a session that does not know it does the work *wrong*, not merely
> slowly.**

| Candidate | Verdict, by that test |
|---|---|
| the vault | **in** — not knowing it exists costs every reason the session produced |
| its librarian | **in** — a session that writes `wiki/` by hand breaks the one-writer property ([[the-one-writer-rule-covers-the-registers-too]]) |
| the sprint | **in** — work outside an open sprint has happened for a whole day and nothing stopped it ([[a-gate-that-refuses-work-without-an-open-sprint]]) |
| where `src/` is | **out** — ten seconds of `ls` |
| where the tests are | **out** — same |
| where the hooks are | **out** — same |

**Rejected: a map of locations**, which is what `## Where things are` was and what made it drift four
ways in one day ([[where-things-are-is-deleted-now-and-generated-later]]).

## What it obliges

- **The map is a region, not prose**, or it is the same block again under a new heading. It cannot be
  rendered from a page until `governs:` is read as a field
  ([[governs-becomes-a-property-of-any-page]]).
- **The test is reusable and should be**: it is the same shape as the admission test for a rule page —
  *imperative and not enforced by a test* ([[the-harness-is-compiled-not-maintained]]) — and the same
  shape as the folder-set admission test ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). This
  project now has three, all of the form *what does not knowing it cost*.

The design is [[the-map-in-claude-md-and-its-admission-test]].
