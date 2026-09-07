---
title: "The selftest is a mutation test of the gate, and its cost follows from that shape"
type: concept
status: current
authority: selftest-shape
basis: code
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-check-selftest.sh", "scripts/vault-check.sh"]
tags: [testing, harness, vault]
---

# What each case does

**Take a known-good copy of the tree, break exactly one thing, run the gate, and assert that it
reddened *with the message naming that thing*.** The last clause is the whole of the design: a case
that only asserts a non-zero exit passes when any unrelated rule fires, and this store has already
lost cases to exactly that ([[a-case-that-fails-for-its-own-reason-tests-nothing-either]],
[[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

**The copy is per case, and that is not thrift being ignored.** A breakage that leaks from one case
into the next makes the next fail with the wrong diagnosis — it goes red for a reason nobody chose,
and the report names a rule that was never touched
([[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]],
[[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]).

# The cost is a consequence of the shape and not an inefficiency

**Most cases break one rule and evaluate all of them.** Counted 2026-08-23: 102 of the cases plant a
single defect, and every one of those runs the whole gate — twenty rules over the whole sandbox — to
read one message.

**So the suite's wall clock is (number of cases) x (cost of a full gate run)**, and the gate's own
cost grows with the corpus. Both terms move in the same direction as the store grows, which is why
the total is superlinear in the number of pages
([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]).

# What follows for making it cheaper, and what it forbids

**Narrowing a case to one rule is the obvious lever and it is not free.** Running all twenty gives
incidental coverage nobody designed and nobody watches; a case that runs one rule loses it silently
([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).

**The clean cases can never be narrowed.** A `run_clean` case asserts *nothing anywhere went red*,
and that proposition has no single rule to point at — narrowing it would change what it says
([[a-clean-case-built-on-a-helper-that-plants-a-red-tree-can-never-be-green]]).

# Why this is worth writing down at all

**A mutation test is evidence about the checker rather than about the corpus.** Its green says the
gate still catches what it was written to catch — not that the tree is sound, which is the gate's own
job. Confusing the two is how a suite comes to be trusted for something it never measured
([[a-test-green-under-any-implementation]], [[a-gate-guarantees-agreement-never-truth]]).

# Only one of this project's four selftests is expensive, and the reason is this shape — 2026-08-26

**`vault-check-selftest.sh` builds one sandbox root and one pristine copy of the corpus, then gives
each of its ~178 cases its own working copy of that baseline and runs the gate inside it**, through a
worker pool.

**The other three copy no corpus per case at all.** That is the whole difference:

| suite | cases | wall clock |
|---|---|---|
| `hook-selftest.ps1` | 148 | 2m17s |
| `session-dialogue-selftest.py` | 52 | seconds |
| `vault-measure-selftest.py` | 59 | seconds |
| `vault-check-selftest.sh` | ~178 | about an hour |

**So the cost is structural rather than a matter of how many cases there are**, and it is why the
smoke runner takes the first three whole and needs the fourth narrowed
([[the-smoke-runner-is-built-first-thing-next-session]],
[[the-suite-gets-a-subset-mode-that-issues-no-verdict]]).

**It is also why the suite left the session loop rather than being sped up first**
([[the-suite-stops-running-every-session]]).

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
