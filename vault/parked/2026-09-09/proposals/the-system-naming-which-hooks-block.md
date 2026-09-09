---
title: "The system naming which hooks block and which only speak"
type: proposal
status: current
authority: hook-blocking-register
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/settings.json", ".claude/hooks/ask-the-vault.ps1"]
decided_by: [[advisory-is-the-default-for-a-hook]]
tags: [harness, agents, process]
---

# Raised 2026-08-19, and not built

> **owner:** «нужно будет обсудить что блокирует а что нет. Запишем на будущее» — 2026-08-19.

**The conversation is owed, not the answer.** What exists already is the default and its exception
test: advisory unless the action is irreversible **and** the refusal cannot be wrong
([[advisory-is-the-default-for-a-hook]]). **What does not exist is the system** — a per-hook
statement of which one refuses, on what test, and where that statement lives.

# What it has to cover

- **Which hooks refuse an operation and which only speak.** Today that is not a list: every hook
  speaks, and each of them arrived at that independently ([[session-hooks]],
  [[the-journal-gate-hook]]).
- **On what test the difference is decided**, so that the next hook is classified rather than
  chosen. The exception test is stated; whether it is the whole of the test is what the conversation
  is for.
- **Where the classification is recorded.** A hook's own header does not count — nothing reads a
  harness file ([[no-rule-reads-a-harness-file]]), and a policy in a script is a policy nobody can
  cite.
- **What a refusal looks like to the caller.** A `PreToolUse` hook that blocks has to say why in a
  way the session can act on; an event whose exit code is ignored cannot block at all, which is
  already true of `InstructionsLoaded`.

# What is known and does not need re-deriving

**The only hook ever designed to refuse is [[a-lock-on-the-librarian-dispatch]]**, and it is
unbuilt. Its case is instructive because it is the one that plausibly meets both conditions: a
second librarian writing concurrently is not undoable, and the lock's refusal is decidable from a
file rather than from a judgement ([[parallel-librarians-break-the-one-writer-property]]).

**`a-gate-that-refuses-work-without-an-open-sprint` cannot live on `SessionStart` at all**, because
that event injects context and has no way to deny ([[a-gate-that-refuses-work-without-an-open-sprint]]).
So the space is not *which hooks should block* but *which hook events can*.

# What not building it costs

**Every hook's blocking behaviour stays a per-hook choice made by whoever writes it.** The default
narrows that — a new hook is advisory unless its page argues otherwise — but nothing enumerates the
set, so *"no hook blocks"* is a statement nobody can check without reading every script.

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]],
[[proposals-are-a-folder-not-a-status]]).

# Two more hook surfaces were added without it — 2026-08-20

**`.claude/hooks/check-the-plan.ps1` and the pre-task net inside `.claude/hooks/ask-the-vault.ps1`**
were both written and both chose advisory, correctly and for a stated reason
([[advisory-is-the-default-for-a-hook]], [[the-plan-check-hook]]).

**The owner asked for this conversation on 2026-08-20 and the session added the surfaces before it
happened.** The cost of not having had it is unchanged and is still nil today: the working rule
answered all three questions put to it that day. **The cost arrives when it stops answering** —
which is what an enumerated set would make visible before rather than after.

**It stays unbuilt and this is not a bid to build it.** The page records that the set grew while the
enumeration did not.

# Two of the four bullets above landed, and the conversation is smaller than it was — 2026-08-21

**Where the classification is recorded: `scripts/hook-selftest.ps1`**, a case per registration, on
the owner's ruling that the list lives in a test and never in prose alone
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**On what test the difference is decided: a measured condition, a measurement reliable where the
hook stands, and a refusal that says how to clear it** — ratified the same day, replacing the test
this page cites, which the owner says he never gave
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]],
[[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

**And the space this page named is now bounded by measurement rather than by argument.** It said
*"the space is not which hooks should block but which hook events can"*, and that is now asserted by
a case: `PostToolUse` fires after the act and `SessionStart` injects context, so **the conversation
is about the `PreToolUse` registrations and nothing else.**

**It stays `current` and is deliberately not retired.** The owed conversation is what remains —
which of those registrations should refuse — and the owner scheduled it twice
([[a-conversation-the-owner-scheduled-is-displaced-by-the-work-beside-it]],
[[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*
