---
title: "A new verdict is proved by planting an offender in the real tree, because the check resolves its vault relative to itself"
type: concept
status: current
authority: verdict-proof-procedure
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# The property

`scripts/vault-check.sh` opens with `cd "$(dirname "$0")/.."` and finds its vault from there — the
top-level directory containing a `wiki/`. **It has no argument that points it somewhere else.** So a
copy of the corpus made in a sandbox directory is not a thing the script can be aimed at: run it and
it checks the real tree, whatever is in front of it.

That is deliberate and it is what makes the command safe to give a reader as a bare line. The cost is on the other side: **a verdict
cannot be demonstrated against a fabricated corpus.**

# The consequence for proving a verdict

**A new verdict is proved by planting an offending page in the real tree and reverting in the same
command.** One shell line writes the page, runs the check, greps for the message and removes the
page, so the tree is never left dirty even if the assertion fails:

```
cp /dev/null wiki/concepts/_probe.md; printf '...' > wiki/concepts/_probe.md; \
  bash scripts/vault-check.sh | grep 'the message'; rm wiki/concepts/_probe.md
```

**Every verdict added on 2026-08-19 was proved that way** — the three the per-folder schema
introduced and the widened `ruleclaim`
([[the-per-folder-frontmatter-schema]],
[[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]).

# What this is not, and the distinction matters

**It is not a substitute for the selftest.** `vault-check-selftest.sh` builds a pristine copy and
plants fixtures in it, and it can do that because it is the script's own harness rather than a caller
of it. The plant-and-revert line proves *this verdict fires on this shape today*; the suite proves
*the rule still catches what it was written for, tomorrow, after somebody edits the check*
([[vault-scripts]], [[a-case-that-passes-before-the-change-tests-nothing]]).

**Doing only the plant-and-revert is how a verdict lands with no case behind it.** Doing only the
suite is how a fixture defect passes for a rule that was never exercised against the real corpus
([[a-fixture-must-materialise-what-the-subject-reads]],
[[the-fixture-corpus-goes-red-before-the-rule-it-was-never-written-for]]). Both, in that order, is
what this session did and what the procedure is.

# The risk it carries, named so it is handled

**The window between the plant and the revert is a window in which the real corpus is wrong.** It is
one command long and the tree is committed either side of it, so `git status` and `git checkout` are
the recovery — but a plant that is written and not reverted, in a session that is then interrupted,
leaves a page in `wiki/` that the librarian did not write. **The revert belongs in the same command
as the plant**, never in the next one.

# The sandbox route exists after all — 2026-08-28

**`VAULT=` overrides the discovery**, in `scripts/vault-check.sh` and `scripts/vault-archive.sh`
alike, so a copy of the corpus in a scratch directory *can* be checked. The property described at the
top of this page — no argument points the script anywhere else — is true of arguments and silent
about the environment.

**Proved on 2026-08-28 against a sandbox copy of the live corpus**: three offenders planted at once,
each of the two new status values read in the folder where it is red and the one where it is not
([[a-status-value-is-either-an-address-or-a-stage-and-the-gate-treats-them-oppositely]]).

**And the sandbox is strictly better here.** No live file is touched, so the window in which the real
corpus is wrong does not open at all, and more than one offender can be planted in a run.

**The session reached it by being refused.** It planted in the live tree first, on this page's own
procedure, and `ask-the-vault.ps1` stopped it
([[divergence-the-session-planted-an-offender-in-the-live-wiki-and-the-lock-hook-stopped-it]]).

**What stands unchanged is the distinction below**: a local proof that a verdict fires is not a
regression run, and both are owed
([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]]).
