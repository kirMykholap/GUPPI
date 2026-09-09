---
title: "A figure measured before the tree moved is not a measurement of the tree it is now read against"
type: lesson
status: archived
authority: unrepeated-measurement
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "job_hunt_ai_vault/sprint.md", "scripts/vault-check-selftest.sh"]
tags: [testing, vault, process]
---

# The incident

**`sprint.md` reads criterion 1 against `caught 120, missed 0`.** That figure was measured on
2026-08-19 — and **before the page carrying the new `_schema.yaml` citations was compiled in the same
ingest**. It stopped being true the moment that page landed, because those citations are what the
sandbox's placeholder loop then materialised into a decoy vault
([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]).

**Measured on the tree that now exists: `caught 24, missed 96`** — reproduced with the six
`_schema.yaml` files reverted to their committed state, so the `basis` promotion is not implicated
([[the-frontmatter-core-is-fixed-and-updated-joins-it]]).

**Nobody re-ran it in between**, and the criterion went on being read against a number the corpus had
already invalidated.

# Why this one is not the same as quoting a figure nobody measured

**The figure was honestly measured and was true when it was taken.** That is the whole difficulty: it
carries real provenance, so re-running it looks like redundant work
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]] is the other failure, where the
predicate under the number was never stated).

**What moved was the subject, not the instrument.** The suite reads the corpus, the corpus grew a
citation, and the citation was written by the same ingest that quoted the figure. **The measurement and
the thing that falsified it were in the same commit range**, which is the narrowest possible window and
the one nobody watches ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

# The rule

**A number is a measurement of the tree it was run on.** Quoting it against a later tree is an
inference, and it is a weak one whenever the subject reads the corpus.

**A suite whose input is the whole store has to be re-run at the end of the ingest that changed the
store**, not before it. The sprint criterion that names this suite as its decider is exactly the place
that reading is made — and it was made once, off a stale run, for the length of a sprint
([[a-sprint-closes-on-its-goal]]).

*The journal this is compiled from says nobody re-ran the suite for six days. That is not what the tree
shows: the ingest that landed the citations is `27ffa4b` at 03:06 on 2026-08-19 and the red reading was
taken the same night, before `bade6c9` at 05:25. The gap is hours. Corrected here rather than compiled,
because the lesson does not depend on the interval and the interval is checkable.*
