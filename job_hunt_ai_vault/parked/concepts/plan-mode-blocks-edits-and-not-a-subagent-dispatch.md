---
title: "Plan mode blocks edits and not a subagent dispatch, which is what makes the ritual possible there"
type: concept
status: current
authority: plan-mode-and-subagents
basis: external
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/check-the-plan.ps1"]
tags: [agents, vault, harness]
---

# What plan mode stops

**It blocks edits. It does not block a dispatch.** That is load-bearing rather than incidental: the
whole design of the pre-task trigger has the ritual running **inside** plan mode, between a finished
plan and its approval ([[a-pre-task-runs-between-the-plan-and-its-approval]],
[[the-plan-check-hook]]).

If a dispatch were blocked there, the only available moments would be before a plan exists — when
there is nothing to check — or after approval, when the constraint the answer names has already been
designed around.

# The consequence nobody had recorded

**A librarian answering during planning cannot widen the alias list in `tags.md`**, because that
write is blocked by the mode rather than by any rule of this vault.

**So an answer given during planning may be the one that most needed an alias and least could add
one.** The words a question was asked in are known exactly at that moment and are gone afterwards
([[aliases-carry-the-question-across-languages]]). Nothing routes them anywhere today; a session
that notices it writes the line into `.superpowers/sdd/vault-feedback.md`
([[write-the-miss-into-vault-feedback-before-the-turn-ends]]), which survives the mode because it is
drained by `/handoff` and not by a write during the plan.

**The one-writer property is untouched by this** — a blocked write is not a second writer, and the
lock narrows on the dispatch rather than on the mode
([[the-librarian-lock-hook]], [[dispatch-librarians-in-parallel-only-for-reading]]).

# And the dispatch is cheap in the dimension that would otherwise forbid it

**A mode switch invalidates no cache, and a subagent's call and result merely append to the parent**
([[switching-permission-modes-is-cache-safe]]). So the objection to running the ritual inside plan
mode is wall clock and nothing else.

# A hook writes during plan mode; a script the session runs does not — 2026-08-21

**The rows prove it.** `first-write`, `advised-write` and `advised-plan` all carry `plan` in their
permission-mode column, and every one of them was appended by a hook
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]], [[the-pre-task-ledger]]).

**This dissolved a design deadlock rather than answering it.** The problem was never that the ledger
is unwritable during planning: it was that `scripts/record-pre-task.ps1` is launched **by the
session** rather than by an event, and a session's write is what plan mode stops
([[a-blocker-can-be-dissolved-instead-of-answered]],
[[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

**The consequence found the day the ritual gained its first phase**: phase 1 was run by hand inside
plan mode and the hook still reported that no pre-task had run, because the recording is a write and
the rule places the ritual **between** the plan and its approval
([[a-pre-task-runs-between-the-plan-and-its-approval]], [[the-plan-check-hook]]).

**So a pre-task agent will find misses in plan mode and cannot record them there.** That is the same
shape this page already records about the librarian and its alias list, and it is known before the
agent is built rather than after ([[write-the-miss-into-vault-feedback-before-the-turn-ends]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*
