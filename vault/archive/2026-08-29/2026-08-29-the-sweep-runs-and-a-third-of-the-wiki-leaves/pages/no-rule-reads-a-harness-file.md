---
title: "No rule reads a harness file, and none compares a skill against a decision"
type: lesson
status: archived
authority: harness-divergence-shape
basis: measurement
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", ".claude/skills/ingest/SKILL.md"]
tags: [harness, process, vault]
---

# Three more in one session, all found the same way

**Three divergences were found on 2026-08-16, all by reading two files side by side**, bringing the
running total to **seven**. Not one was found by a check, because the shape of the failure is that
**no rule reads a `CLAUDE.md`, and no rule compares a skill against a decision.**

| # | The divergence | Found while |
|---|---|---|
| 5 | `.claude/skills/ingest/SKILL.md` line 9 says *"one source at a time — never batch several handoffs"*; `ingest-is-batched-at-the-retrospective`, decided the same day, says ingest runs once over every journal since the last. The skill's last commit, `f7f654e`, predates the decision | measuring how `/ingest` would have to change |
| 6 | the vault's `CLAUDE.md` documents a duplicate check that never compares values | trying to explain `authority` to the owner ([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]) |
| 7 | [[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]] says *"Four instances are now on record"* over a table of five rows | reading it for the `CLAUDE.md`-staleness discussion ([[a-stated-count-drifts-from-the-list-it-heads]]) |

## The one that widens the class

**#5 is the first divergence found between a skill and a decision rather than inside a
`CLAUDE.md`.** Until it, every recorded instance was a rule file drifting from the corpus, and the
gap could be described as "nothing reads a `CLAUDE.md`". It is larger than that: **nothing reads any
harness file against the vault**, and a skill is a harness file with a procedure in it.

The resolution of that particular divergence is not that the skill was simply stale — it was right
about compilation and wrong about dispatch, which is what
[[ingest-runs-after-handoff-at-the-end-of-a-session]] separates. **A divergence found by a check
would still have needed a human to say which side was wrong**, which is the same boundary
[[a-gate-guarantees-agreement-never-truth]] draws.

## Why the total is worth carrying

Seven instances of one failure class, none of them caught by anything mechanical, is the evidence
the harness build rests on ([[the-harness-is-compiled-not-maintained]]). The count is derived from
the table above plus the four already tabulated on
[[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]; it is meant to grow, and it is
re-derived rather than carried ([[a-stated-count-drifts-from-the-list-it-heads]]).

## Row 5 now cites an archived page — annotated 2026-08-17, not repointed

`ingest-is-batched-at-the-retrospective` was **deprecated and moved to `archive/`** by the owner on
2026-08-17, and [[ingest-runs-after-handoff-at-the-end-of-a-session]] took
`authority: ingest-cadence` with it. Row 5 stands as written, because it records what was true when
the divergence was found, and the divergence itself is real and still counted.

**What changed is the shape of the disagreement, not its existence.** With the batched page retired,
the skill's line *"one source at a time — never batch several handoffs"* is **correct about
compilation**; the divergence is only about **dispatch**, which is what the successor already said
and what the skill has since been rewritten to say in both halves.

A live page arguing from an archived one is [[a-live-page-can-argue-from-a-deprecated-one]], and
this instance was **created by a write** rather than found in a sweep.
