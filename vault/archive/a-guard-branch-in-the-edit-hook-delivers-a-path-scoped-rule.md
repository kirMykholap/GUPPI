---
title: "A guard branch in the edit hook that delivers a path-scoped rule the compaction dropped"
type: proposal
status: deprecated
basis: human
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", ".claude/hooks/ask-the-vault.ps1", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, agents, process]
superseded_by: [[the-guard-branch-lives-inside-a-hook-that-already-runs]]
---

# Designed 2026-08-19, and not built

**The hole it closes:** a governed file read before a `/compact` and edited after it is edited with no
rule in context and no signal that one is missing
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]). A guard is therefore not a
reminder — **it is a second trigger, bound to something that recurs.**

## The shape, and the owner confirmed it

**A fourth branch in `.claude/hooks/ask-the-vault.ps1`.** It:

1. scans `.claude/rules/*.md`;
2. parses each file's `paths:` frontmatter ([[paths-lives-on-the-vault-page-and-is-written-widest]]);
3. matches that against the payload's `file_path`;
4. injects the file's body as `additionalContext`.

**The rule stays defined once** — generated whole from its vault page
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
[[generating-a-claude-rules-file-whole-from-its-vault-page]]) — and **both triggers hand out the same
text**: the native Read delivery, and this hook on the operation probe 4 measured going through
unguarded.

## What it costs, and the surprising half is that it costs nothing new

**Zero new processes.** `.claude/settings.json` has registered that script under `PreToolUse` on
`Edit|Write` since 2026-08-13, narrowed by path inside the script ([[session-hooks]]). The latency a
previous session queued a measurement for is **sunk**, and the measurement is not owed
([[an-objection-priced-against-a-cost-already-paid-dissolves-on-a-page-nobody-opened]]).

**Its honest cost: on a normal Read→Edit flow the rule arrives twice**, and the hook cannot see the
context to know. That is duplication of a slice-sized text, paid on every edit of a governed file, and it
is stated here rather than discovered.

**And the script's own header already carries the principle it needs**: *"A guard on every edit becomes a
ritual performed without reading; a guard on rule-bearing paths fires exactly where the recorded
divergences happened."*

## What is open

**The owner's objection to `PreToolUse` on `Edit|Write` is narrowed, not answered.** He rejected it
because it fires on every edit and write; the finding above shows the mechanism can match the path and
exit immediately, so **no scoping is lost — what is spent is latency on every `Edit|Write` in the
repository.** That number is what the option is either taken or dropped on, and he said the next session
works it out. **Do not re-propose it without that.**

**Cases are owed in `scripts/hook-selftest.ps1`**, which today covers the guard's existing branches only.

## What it blocks while it stands

**The AST boundary rule's move** ([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]],
[[moving-a-rule-into-claude-rules-with-a-paths-scope]]).

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# Built 2026-08-19 and retired 2026-08-20, with where each part went

**The shape landed as designed** — a branch in `.claude/hooks/ask-the-vault.ps1` that scans
`.claude/rules/*.md`, parses `paths:`, matches the payload's `file_path` and injects the body as
`additionalContext` ([[the-guard-branch-lives-inside-a-hook-that-already-runs]]).

| What lived here | Where it lives now |
|---|---|
| the mechanism, and the four properties that are decisions rather than details | [[the-guard-branch-lives-inside-a-hook-that-already-runs]] |
| the hole it closes, and why a guard is a trigger rather than a reminder | that page, and [[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]] |
| *both triggers hand out the same text*, and the comment-stripping it obliged | that page, with the measurement on [[a-loss-measured-between-different-quantities-is-not-a-loss]] |
| **it stays advisory**, which this design chose without a ruling behind it | ruled since: [[advisory-is-the-default-for-a-hook]] |
| the honest cost — the rule arrives twice on a Read→Edit flow | carried over verbatim onto the mechanism page |
| the open latency number the owner said the next session works out | measured: 17–21 ms on top of 177 ms, in `log.md` under 2026-08-20 |
| the owed cases in `scripts/hook-selftest.ps1` | written — 54 caught, 0 missed, and which of them prove anything is on the mechanism page |
| what it blocked while it stood | discharged: [[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]] |

**Retired under the policy rather than by a call on this page**
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
