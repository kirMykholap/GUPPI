---
title: "`/ingest` chooses its source by sidecar absence, because a date prefix stops ordering sessions once there is more than one a day"
type: decision
status: current
authority: ingest-source-selection
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, harness, process]
---

# Decided 2026-08-20, in the fourth session of that day, and built in `abd2a53`

**The source is every handoff in `raw/handoffs/` matching `2*.md` with no `<name>.coverage.tsv`
beside it.** Where more than one is uncompiled they are taken oldest first by the date in their
names, one at a time inside the one dispatch; where every handoff has a sidecar the skill says
there is nothing to ingest **rather than picking one**.

**What it replaced was not a decision — it was prose in one skill file**: *the newest handoff by the
date in its name*. Three journals now carry `2026-08-20` and that rule has nothing left to break the
tie. **Nothing in `decisions/` had ruled on source selection**, so this page supersedes nothing.

## What was rejected

- **The `ingested:` line of `brief.md`**, which the brief itself proposed as the tie-break. It names
  the one journal last compiled, which is enough to say *not that one* and not enough to order the
  remaining two of three same-day journals ([[the-brief-is-stamped-with-its-commit]]).
- **mtime**, which any checkout rewrites and which the skill already forbade for that reason. A
  clone rewrites them in index order, which is how the first version of the brief's own staleness
  check came to fire on every fresh clone ([[session-hooks]]).

## What it obliges

**The predicate is scoped to `raw/handoffs/` with the `2*.md` filter**, and the scope is the
decision rather than an implementation detail: `raw/plans/` and `raw/specs/` hold artefacts that are
frozen and cited rather than compiled, so they will never earn a sidecar and an unscoped predicate
would offer them for ever ([[raw-holds-testimony-and-artefacts-are-frozen]]).

**Oldest first, one at a time inside one dispatch, is not new here.** It is the shape
[[ingest-runs-after-handoff-at-the-end-of-a-session]] already settled — batching survives as the
shape of a single dispatch, and compilation stays one source at a time.

**The test is a file-existence test and no ordering can break it**, which is the property the date
prefix lacked ([[the-sidecar-is-the-single-definition-of-compiled]]).

## The branch that fired on the day it was built was *nothing to ingest*

Applied to the real tree that night: **18 handoffs matched `2*.md` and none was uncompiled**, three
of them dated `2026-08-20`. The tie-break the change exists for bites at the next `/handoff` rather
than at the run that built it — so the rule shipped without its own case being exercised, and the
journal says so rather than implying otherwise.
