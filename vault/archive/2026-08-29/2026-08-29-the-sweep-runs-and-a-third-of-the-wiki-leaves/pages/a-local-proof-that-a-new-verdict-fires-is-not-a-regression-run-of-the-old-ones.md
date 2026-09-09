---
title: "A local proof that a new verdict fires is not a regression run of the old ones"
type: lesson
status: archived
authority: local-proof-versus-regression
basis: measurement
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# What happened, 2026-08-23

**Three new refusals were each verified by planting an offender in the real tree and reading the
refusal back, then reverting and reading the pass** — both directions, on the tree that would ship.
The session reported all three as proved and moved to the next phase.

**Meanwhile the suite had gone from `caught 158, missed 0` to `caught 157, missed 1`.** The case
`a status the schema lacks` greps the gate's message for `status 'draft'`, and that message no
longer existed: the hardcoded status pair and the sentence beside it had been removed in the same
change that moved the legal values into the schemas
([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**Behaviour never lapsed.** The gate still reddened an illegal status; only the wording the case
matched on had gone. **The regression was in the instrument, not in the thing measured** — which is
why nothing the session did could have shown it.

# The two questions, and only the first was asked

| the question | what answers it | what it costs |
|---|---|---|
| does this new verdict fire, and does it stay quiet when it should | plant an offender, read it back, revert, read the pass | a minute, in the real tree |
| do the verdicts that were already there still fire | the whole suite | minutes, and nothing runs it unasked |

**A plant answers the first and is silent about the second, and the silence is not visible from
inside the first.** The plant passes, the report says *verified both ways*, and every word of that
is true about the verdict it names.

# What made it discoverable at all, which is the uncomfortable part

**Nothing runs the suite automatically.** The only reason it ran on 2026-08-23 is that the
librarian, dispatched for something else, flagged an unrelated archive case in its report. **A
side effect of a different task is what stood between this session and shipping a suite one case
short.**

# The rule

**A change to a verdict's message or shape is finished when the suite has been run, not when the
plant has been read back.** The plant is the proof that the new thing works; the suite is the only
thing that answers for the cases nobody thought to grep
([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).

**And a report saying *verified in both directions* is answering the narrow question**, so it says
so. Claiming more than was checked is the failure this store has already named from three other
angles ([[a-hole-was-shipped-in-work-already-reported-as-verified]],
[[a-chain-proved-in-halves-is-not-proved]]).

# One level up

**This is [[an-instrument-that-fails-towards-nothing-to-do]] applied to a session's own report.**
`caught 157, missed 1` is loud; what was quiet was the absence of any run at all, and an absent
reading looks exactly like a clean one from a distance.
