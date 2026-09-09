---
title: "`raw/` gains its internal structure before the archive move, not after"
type: decision
status: current
authority: raw-structure-ordering
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md"]
tags: [vault, process]
---

# The ruling, 2026-08-19

**`raw/` gains its internal structure — `plans/`, `specs/`, `notes/` beside `handoffs/` — before the
move into `archive/`.**

**Rejected: doing it after the move.** Both operations rewrite the same `sources:` lines, so the
later ordering **makes the rewrite run twice** over 150 pages, with the prose half read by eye each
time ([[sed-cannot-tell-an-address-from-a-quotation]]).

## What it closes

**A question open since 2026-08-16.** [[moving-raw-into-a-dated-archive]] listed it — *"whether
`raw/` gains internal structure first, which is agreed as nearly free and also not done"* — and
[[structure-work-agreed-and-not-executed]] has carried the row ever since, priced as *agreed as
nearly free, and still not done*. **The agreement was never the blocker; the ordering was.**

**Nothing is built by this.** The structure does not exist, the move does not exist, and the script
that would perform both does not exist
([[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]],
[[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]). What changed is that the two
items are now one job in a fixed order rather than two items either of which could go first.

## What it obliges

- **The session folder inside `archive/` mirrors whatever `raw/` ends up holding**, because files
  lie in the archive as they lie in `raw/`
  ([[the-archive-gains-a-folder-per-session-inside-the-date]]). Building the structure after the
  move would also mean the archive's own layout was frozen before the layout existed.
- **The citation cost is paid once.** Measured at `b6fc6d8`, 150 of 165 pages name `raw/handoffs`
  and 23 of those in prose; the number is monotonic, so every session that does neither makes both
  larger ([[a-rewriter-must-be-paired-with-a-detector]]).

## Built 2026-08-20 — step 1 of the migration, and the only step that was not blocked

**`raw/plans/` and `raw/specs/` created with `.gitkeep`.**

**`raw/notes/` had no `.gitkeep` and now has one.** Git does not track empty directories, so the
moment the migration empties that folder it disappears on a fresh clone — exactly as
`raw/handoffs/` would without the one it already carries. That is a defect the structure step was
supposed to prevent and had itself.

**Gate unmoved**: exit 0, one advisory, before and after.

**The fourth kind arrived by ruling rather than by this step**: the probe scaffolding went to
`specs/` whole, and **no fifth kind was minted**
([[the-probe-scaffolding-is-archived-whole-into-specs]]). A `logs/` kind is proposed and not built
([[log-md-rotates-per-session-into-the-dated-archive]]).

**And the emptying this structure is for has a hazard nobody had recorded**: two selftest cases
depend on `raw/handoffs/` being non-empty, and they fail loudly with the wrong diagnosis when it is
not ([[failing-loudly-with-the-wrong-diagnosis]],
[[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).
