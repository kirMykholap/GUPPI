---
title: "A selftest case can pin the announcement while the thing it announces is broken"
type: lesson
status: archived
authority: announcement-versus-condition
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "scripts/hook-selftest.ps1", ".claude/hooks/lock-the-librarian.ps1"]
tags: [testing, harness, process]
---

# The incident

**The lock fired for the first time in anger and the owner read a refusal naming a command that does
not exist.** `` `bash scripts/vault-check.sh` `` had reached the caller as `ash scripts/vault-check.sh`
([[a-backtick-in-a-double-quoted-powershell-string-is-an-escape]]).

**A selftest case existed for exactly this and it was green.** `scripts/hook-selftest.ps1` asserted
the literal `THE CONDITION IS`, and that phrase survived intact while the command beside it was
mangled. **Seventy caught, zero missed, over a refusal nobody could act on.**

**The case exists to enforce the owner's rule that a refusal names its condition**
([[a-refusal-is-conditional-or-absolute-and-nothing-else]]). It enforced that the *sentence* was
spoken. It never read what the sentence said.

# The defect was verified as pre-existing rather than assumed

`git log -S` puts the phrase in `.claude/hooks/lock-the-librarian.ps1` at `269c877`, in
`.claude/hooks/check-the-journal.ps1` at `8017f34`, and the guarding assertion at `269c877`.
**The fix is owned by this session; the defect is not** — a distinction worth measuring rather than
guessing, because the alternative reading is that the session broke it while testing it
([[a-claim-asserted-from-prose-rather-than-from-the-file]]).

# The rule

**Assert the condition, not the sentence that introduces it.**

**Hardened the same session:** three cases now pin the literal `` `bash scripts/vault-check.sh` `` —
the lock's deny branch, the lock's cannot-measure branch, and the journal gate's
([[the-journal-gate-hook]]). **No case was added; the count is unchanged at seventy.** A hardened
assertion is not a new case, and a suite whose count did not move can still have got stronger.

# One level up

**This is [[an-instrument-that-fails-towards-nothing-to-do]] applied to a test rather than to a
tool.** The instrument checked that something was said, not that what it said was true — and the
output it produced, `70 caught, 0 missed`, is the output its reader most wants to see.

**The general defence is the same one that worked twice elsewhere**: assert against the thing the
reader will act on, and prove the assertion can fail
([[a-case-that-passes-before-the-change-tests-nothing]],
[[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]).

# It happened again on 2026-08-24, in a suite written the same day, and the fixtures were the cause

**Three cases in `scripts/session-dialogue-selftest.py` were passing for the wrong reason and a
fourth was about to.** Their fixtures carried no `origin` field, so once the speaker classifier
landed they exited 2 reporting *no owner turns* — while their names claimed to test *no session
reply*. The case announced a green outcome about a condition it never reached.

**The fourth was the mirror image**: it asserted that a substring was **absent**, and that substring
sits inside the heading `system (task-notification) - NOT the owner`. It would have gone red for a
reason unrelated to its subject the moment the heading was written.

**All four were caught by running the suite, not by reading it** — which is the same finding this
page opened with, one suite later. The suite went **21 → 32 cases**.

**What generalises is about fixtures rather than assertions.** A fixture missing a field the code
later starts reading turns every case built on it into a test of the missing field, silently, and
the announcement keeps reading green ([[a-fixture-helper-that-hardcodes-a-page-slug-couples-every-case-built-on-it]]).
