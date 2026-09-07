---
title: "An objection priced against a cost this repository already pays dissolves on a page nobody opened"
type: lesson
status: archived
authority: objection-against-a-sunk-cost
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", ".claude/settings.json", ".claude/hooks/ask-the-vault.ps1"]
tags: [vault, agents, retrieval]
---

# The incident

**The owner rejected `PreToolUse` on `Edit|Write` as the guard for the path-scoped rule**, on 2026-08-19
after probe 4: *"it fires on every edit and write, and scoping is the whole reason `.claude/rules/` with
`paths:` was being tried in the first place."* The previous session queued a **latency measurement** to
price the option and wrote down that the measurement was what the option waited on.

**`.claude/settings.json` has registered `.claude/hooks/ask-the-vault.ps1` under exactly that matcher
since 2026-08-13**, and [[session-hooks]] states it in its own table — *"`PreToolUse` | `Edit|Write`,
narrowed again by path inside the script."*

**A PowerShell process is already spawned on every Edit and Write in this repository.** The cost is sunk,
the measurement is not owed, and the guard is **a fourth branch in a script that already runs** rather
than a new hook — zero new processes
([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]).

# What the corpus held that nobody asked it for

**The script's own header already carries the principle such a guard needs**, written in 2026-08-13 for
the same reason: *"A guard on every edit becomes a ritual performed without reading; a guard on
rule-bearing paths fires exactly where the recorded divergences happened."*

**Nobody had opened the page, because nobody asked.** The question *"what would a guard cost"* was
reasoned out from scratch across two sessions while an entity page answered it — the shape
[[deriving-what-the-vault-already-holds-costs-a-round]] names, arriving here **on a live decision rather
than on a sprint criterion.**

# Why this instance is worse than the one already on the record

**A derivation that agrees costs a round.** A derivation that *disagrees with what exists* costs a
decision: the option was taken off the table, a measurement was scheduled to price something already
paid for, and two sessions planned around it.

**The objection was not wrong about mechanism** — it was wrong about **what is already true of this
repository**, which is precisely the class of fact the vault exists to hold and the class a session is
least likely to check ([[the-vault-is-compiled-not-retrieved]]).

**And it was found by reading the vault by hand**, in a session where dispatching the librarian was
forbidden and `/pre-task` therefore did not run
([[the-pre-task-was-skipped-and-the-rule-has-no-by-hand-form]]). The by-hand read overturned a live
decision that had stood for two sessions, which is an argument for the ritual and not against it.

# What the finding does not do

**It narrows the objection rather than answering it.** What is genuinely lost to a `PreToolUse` guard is
**latency on every edit**, not the ability to tell which file is being touched: the hook receives the tool
input including `file_path`, so it can match and exit immediately. **That latency is the number to
measure before the option is either taken or dropped**, and the owner has said the next session works it
out — so this is not a closed decision and the option is not re-proposed without answering it.
