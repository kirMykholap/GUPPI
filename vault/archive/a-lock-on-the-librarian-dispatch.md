---
title: "A `PreToolUse` lock on the librarian dispatch, and the fact it waits on"
type: proposal
status: deprecated
superseded_by: \"[[the-librarian-lock-hook]]\"
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/hooks/check-the-journal.ps1", ".claude/settings.json"]
tags: [harness, agents]
---

# The shape, designed 2026-08-17 and not built

**A `PreToolUse` hook on the agent-dispatch tool, narrowed by `subagent_type: vault-librarian`,
returning `permissionDecision: deny` while `scripts/vault-check.sh` exits non-zero.**

The owner's reading, and it is right: [[the-journal-gate-hook]] **reports** a malformed journal and
refuses nothing. The expensive irreversible step is the one after it.

**What it protects.** A librarian round trip costs fifteen to thirty minutes whatever it is given
([[agent-round-trip-cost]]), and it writes sidecars keyed by line number — so an ingest run against
a broken input cannot simply be re-run over a corrected journal, because `raw/` is immutable and the
verdicts are addressed by line ([[raw-holds-testimony-and-artefacts-are-frozen]]).

**Pre rather than Post, unlike the journal gate**, and for the mirror reason: here the condition —
the check being red — is knowable *before* the act, and the act is what costs.

# The one fact that must be established first

**The exact matcher string for the agent-dispatch tool in this harness.** Guessing it produces a
hook that never fires and **looks identical to one that has nothing to say** — the failure this
project has already shipped once, in a guard whose regex errored on every payload and still exited 0
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

The selftest case is therefore not optional and has a known shape: a payload that must be denied and
a payload that must pass, both proved before the hook is trusted
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

# What is open

- Whether a **red check for an unrelated reason** should block an ingest at all. The check is global;
  the journal is one file. A denial the session cannot clear is a gate that gets disabled.
- Whether the denial message can carry the check's output, as the `PostToolUse` gate does.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# Built 2026-08-20, and retired

`.claude/hooks/lock-the-librarian.ps1` exists and both open questions above are answered
([[the-librarian-lock-hook]], [[a-refusal-is-conditional-or-absolute-and-nothing-else]]). **The fact this page said
must be established first was established**: the dispatch tool is `Agent`, renamed from `Task` with
the old name kept as an alias, and `SubagentStart` cannot block
([[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]]).

**The selftest case this page called not optional is twelve cases**, eleven behavioural and one on
the registration ([[the-locks-matcher-is-pinned-by-a-selftest-case-rather-than-widened]]).

**What is still unproved is the half this page did not name**: that the harness fires the hook at
all. It is on the successor page as an acceptance test after a restart.
