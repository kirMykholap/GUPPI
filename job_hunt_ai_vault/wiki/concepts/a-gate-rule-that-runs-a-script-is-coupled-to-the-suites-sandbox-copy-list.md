---
title: "A gate rule that runs a script is coupled to the suite's sandbox copy list, and the coupling is total"
type: concept
status: current
authority: sandbox-copy-list-coupling
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check-selftest.sh", "scripts/vault-check.sh"]
tags: [vault, harness, testing]
---

# The coupling

**`scripts/vault-check-selftest.sh` builds its sandbox by copying scripts in by name.** It copied
seven; the rule added on 2026-08-26 runs an eighth, `scripts/vault-measure.py`, which is the first
Python script on that list.

**An uncopied script is not a partial failure but a total one.** The rule prints `missing file`,
which arrives as a `note`, which is `fail=1` — and that reddens **all 27 `run_clean` cases at
once**, because every one of them asserts a clean tree.

**The half that keeps quiet is the dangerous half.** Every `run_case` expecting exit 1 goes on
passing, without its own verdict ever firing: the case is green for the wrong reason and says
nothing about the rule it exists to pin ([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

# It was asked before the rule was written, and the file itself said to

**The file's own comment at line 71 records this coupling from `vault-authority.sh` in August** and
says to ask the question whenever a rule delegates. On 2026-08-26 it was asked *before* the rule was
written rather than after the suite went red — which is the whole value of a comment that names a
recurrence rather than an incident.

**The reading afterwards: `caught 178, missed 0`, exit 0**, with rule 15, its three cases, the two
rule 11 measure cases and the copy-list change all in, against about 173 cases before. **The 27
clean cases did not break, which is the risk the copy-list change existed to remove.**

# What it obliges

**Every new gate rule that runs a script owes the copy list a line, in the same change.** There is
no detector: nothing compares the set of scripts the gate invokes against the set the sandbox
copies, and the failure surfaces as 27 unrelated cases going red together
([[the-count-of-a-fields-readers-lives-nowhere]]).
