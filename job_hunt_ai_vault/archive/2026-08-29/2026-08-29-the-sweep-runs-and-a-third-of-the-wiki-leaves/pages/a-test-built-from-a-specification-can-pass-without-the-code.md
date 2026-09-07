---
title: "A test built from a specification can pass without the code it tests, so build the case from the mechanism"
type: lesson
status: archived
authority: case-from-mechanism
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The near-miss, exactly

The proposal said the hole was *"a region carrying a rule's slug in a different governed file"*. A
selftest case written from that sentence puts a region in the wrong file and asserts red.

**It is red — and it was red before the change.** The injector opens the governed file, finds no region
for the rule, and rule 12 fails. **The case would have passed with the new code reverted**, which is a
case that asserts the tree rather than the change ([[a-test-green-under-any-implementation]]).

**The fix was to build the case from the mechanism instead**: a region in the right file **and** a copy in
another governed file — the state where rule 11's per-file duplicate key passes and rule 12 never looks
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

## Why "read the spec, write the test" fails here specifically

**A specification states an *intent*; a test has to state a *state of the world that only the new code
distinguishes*.** Those coincide only when the specification's author already knew which other verdicts
cover which cases — and the author of a proposal, by construction, is writing before the code exists
([[a-proposal-can-be-wrong-about-the-hole-it-describes]]).

So the question a new case has to answer is not *does this match the requirement* but **which state does
this case put the tree in that nothing else already reports**. That question can only be answered against
the mechanism, and answering it is what found the leftover-duplicate case.

## Where this sits among the failures of the same family

| Page | The failure |
|---|---|
| [[a-test-green-under-any-implementation]] | a case that passes whatever the code does |
| [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]] | a check green because it examined nothing |
| [[a-test-that-fails-for-its-own-reasons-proves-nothing]] | a case red for a reason outside the change |
| **this page** | a case red **for the right observable and the wrong cause** |

**The fourth is the hardest to see**, because the run is red before the change and red after, and the
diff looks like it is being tested. The tell is the one this project can apply cheaply: **revert the code
and run the case.** That check cost seconds here and it is the only one that would have caught it.
