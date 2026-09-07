---
title: "A tree broken for a real reason is a better fixture than a planted offender"
type: lesson
status: archived
authority: real-breakage-as-a-fixture
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", ".claude/hooks/lock-the-librarian.ps1", ".claude/hooks/ask-the-vault.ps1"]
tags: [testing, harness, agents]
---

# What was owed, and what supplied it

**The lock's acceptance test needed a red tree** and had been waiting for a restart since the hook
was built ([[the-librarian-lock-hook]], [[the-deferrals-of-this-session-go-onto-the-sprint]]).

**The owner's own rename of the agent file made one** — in the real tree, for a real reason, four
`sources:` lines pointing at a path that had moved. **Nothing had to be planted and nothing had to
be cleaned up.**

# Both acceptance tests were run and both passed

- **The lock fires.** A real dispatch of `vault-librarian` against a genuinely red tree was denied
  and the refusal carried the gate's four lines. **Proved twice** — once before the message fix and
  once after, the second run free because the tree was still red.
- **`ask-the-vault.ps1` reaches a subagent's writes.** A `general-purpose` subagent writing a path
  ending in `CLAUDE.md` received the guard verbatim, *"You are editing a file that carries a project
  rule…"* — confirming [[hooks-in-the-settings-file-apply-inside-subagents]] for the Write path
  specifically.

# Why the real breakage is worth more than the planted one

**A planted offender has to be proved before it is believed and removed afterwards**, and both steps
have failed here: a planted file that did not read back as planted
([[a-planted-offender-is-proved-by-reading-it-back]]), and a sandbox the check could not see
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

**A real breakage carries its own evidence.** The gate named the four pages; the lock quoted the
gate; the refusal was read by the owner rather than by the test. **Nothing in that chain was
arranged for the test, so nothing in it could have been arranged wrongly.**

# The cost, and it is not free

**A real red tree is also a deadlock** — the lock refused the only writer that could clear it
([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]) — **and it hides the health
of what it guards** ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). The lesson is
that a real breakage should be *used* when one appears, not that one should be waited for or caused.

# A hook fired on a live edit inside the session that built it — 2026-08-20

**Both branches of the new pre-task machinery were exercised without planting anything**: the write
net, on a real edit made while the session was still building it, and the loud failure when the rule
text cannot be delivered — because at that moment `.claude/hooks/messages/pre-task.md` genuinely did
not exist, the rule page being the librarian's to write
([[the-plan-check-hook]], [[a-pre-task-runs-between-the-plan-and-its-approval]]).

**The absent-file branch is the one this page's argument covers best.** Arranging it deliberately
means deleting a generated file and remembering to restore it; here the tree was in that state for a
real reason, for hours, and the branch was tested by working rather than by staging.

# A test that catches its own author is better evidence than a planted offender — 2026-08-21

**The hook register's first run printed `MISSED` on two of its four cases, and both were real
defects in the case code**: an invalid character class, and a scalar indexed as an array while
printing the right answer beside itself — the worst shape a test can take, because the output looks
like the answer ([[a-case-that-fails-for-its-own-reason-tests-nothing-either]]).

**Both directions were therefore observed on the real tree**, without anything being planted: the
cases failed while the tree was correct, and passed once they were fixed. That is why the four are
trusted without a further proof run
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**What it does not license.** The evidence is about the case, not about the subject: a case that
fails for its own reason and is then repaired has still never been shown to fail for the reason it
was written ([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*
