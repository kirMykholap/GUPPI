---
title: "What survives a compaction is whatever has something that runs it again, and a scoped rule has nothing"
type: concept
status: current
authority: compaction-survival
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/_probe-paths.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/instructions-loaded.ps1"]
tags: [harness, agents, process]
---

# Measured 2026-08-19, probe 4

Three things crossed the same `/compact` in one session and **only one was lost**, so the difference
between them is the finding rather than the loss ([[the-conditional-delivery-probe]]).

| what | mechanism | after `/compact` |
|---|---|---|
| `brief.md` | the `SessionStart` hook, whose matcher names `compact` | **arrived** |
| the repository's `CLAUDE.md` | unconditional project memory | **reloaded**, `"load_reason":"compact"` |
| `.claude/rules/_probe-paths.md` | conditional delivery scoped by `paths:` | **did not return** |

**What survives is whatever has something that runs it again.** The brief has a hook bound to the
compaction event itself; project memory has an unconditional reload; **a path-scoped rule's trigger is a
Read that already happened, and it does not happen a second time on its own.**

The sequence, from the hook's log rather than from any reader's introspection — a session that has read
the runbook can quote either nonce for the wrong reason
([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]):

1. probe 1 loaded the rule at 23:45:03;
2. `/compact` ran at 03:19:43, logging `"file_path":"...\CLAUDE.md","load_reason":"compact"` and **no
   accompanying `path_glob_match` line**;
3. an Edit on `probe/probe-target.md` was attempted with no read in the post-compaction context. It
   returned `String to replace not found in file`, **the read gate did not fire**, and the hook produced
   **no line at all** — the mechanism never ran, rather than running unseen;
4. a Read of the same file a minute later re-delivered the whole rule, `"load_reason":"path_glob_match"`
   at 03:20:37, so the mechanism was alive the whole time.

# Two things this measured that the probe was not asked for

**Delivery is triggered by the Read tool, not by touching a matching path.** An Edit on a matching path
delivers nothing. The runbook had excused *creating a file* and *a bare Bash command* as known negatives
and **silently assumed Edit was a positive**, which is what made probe 4 look capable of closing the
compaction question rather than opening a wider one
([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]).

**The Edit tool's read gate is *session*-scoped, not context-scoped.** It survived the compaction here,
which is exactly why the Edit sailed past it: the tool remembered the read, the model did not have the
rule, and neither said so.

# The hole has one shape and it is narrow

**A governed file read before a compaction and edited after it is edited with no rule in context and no
signal that one is missing.** Every other route — a fresh session, a subagent, a first touch of the file
— goes through a Read and does get the rule
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

**So a guard is not "remind the model". It is a second trigger, and it has to be bound to something that
recurs** ([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]). The obvious binding is the
operation that was measured going through unguarded.

**What it decides:** the AST boundary rule does not move on the strength of *whoever edits it will have
read it* ([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]]).
