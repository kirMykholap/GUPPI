---
title: "The guard is not built, and the AST rule's move now waits on it rather than on the probe"
type: decision
status: deprecated
authority: ast-move-blocker
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md"]
tags: [harness, agents, testing]
superseded_by: [[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]]
---

# Deferred 2026-08-19, and what changed is the blocker rather than the schedule

**The guard was this session's chosen body of work and was not started**, because the instrument that
would have verified it was returning a fifth of its cases — `caught 24, missed 96`
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]). Building it would have
produced **something unverifiable that looked finished**, and the session would have reported it as done.

**Rejected: starting it once the suite was repaired**, late in the session. The owner was told plainly at
the end and re-chose commit-and-ritual.

# The blocker moved, and this is the correction worth carrying

**It was the probe. The probe is answered. It is now the guard.**

Probe 4 ran on 2026-08-19 and returned **against** the move: after a `/compact` the Edit proceeds with no
re-read, the scoped rule is gone, and nothing brings it back
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]],
[[the-compaction-probe-runs-after-the-ingest-and-the-ast-move-waits-on-it]]).

**So the AST boundary rule does not move on the strength of *whoever edits it will have read it***
([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]],
[[moving-a-rule-into-claude-rules-with-a-paths-scope]]). A guard comes first, and it has to cover the
post-compaction edit specifically.

**No criterion is read off here.** The sprint's own *next* line is where the ordering lives, and reading
a criterion is the owner's ([[a-sprint-closes-on-its-goal]]).

# What not doing it costs

- **The rule stays in the repository's `CLAUDE.md` and reaches every session unconditionally**, which is
  the safe default and is what stands ([[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]]).
- **Region coverage stays at `1 of 14`** until the probe scaffolding is deleted, which this ingest
  unblocks ([[the-conditional-delivery-probe]],
  [[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

**Its shape is settled and costs nothing to resume**:
[[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]].

# Retired 2026-08-20: the guard was built and the move went ahead

**Both the title and the *what not doing it costs* section are false as of 2026-08-20.** The guard
is a branch in `.claude/hooks/ask-the-vault.ps1`, the AST rule governs
`.claude/rules/ast-boundaries.md`, and the region has left `CLAUDE.md`
([[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]],
[[the-guard-branch-lives-inside-a-hook-that-already-runs]]).

**Read this page for why the guard was deferred on 2026-08-19** — the instrument that would have
verified it was returning a fifth of its cases, so building it would have produced something
unverifiable that looked finished. That reasoning is unaffected by the outcome and is the reason the
build waited a day ([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**And read it for the blocker moving rather than the schedule**, which is the correction it was
written to carry: it was the probe, the probe answered, and it became the guard.
