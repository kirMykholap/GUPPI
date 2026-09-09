---
title: "«How would you check that?» produced the best design decisions of the session — the coverage script, and ingest defined as units with verdicts"
type: lesson
status: archived
authority: unverifiable-means-underdesigned
basis: human
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md"]
tags: [process, testing]
---

# The scepticism outperformed the plan

On 2026-08-13 the owner asked twice, in different words, **how any of this could be checked** — how
he would know the vault was not quietly lying, and how anyone would know a document had been fully
processed.

He was right both times, and both questions changed the design:

- the first produced `scripts/vault-coverage.sh`;
- the second produced the definition of ingest as **units with verdicts**
  ([[ingest-is-units-and-verdicts]]), replacing "read the document and file its sections".

**The session's two best design decisions came from his scepticism rather than from the plan.**

*(The title read "«How would you check that?» produced the two best design decisions of the
session" until 2026-08-18, and the bullets above are where the count now lives, as evidence rather
than as a headline. **Two was a fact of one past session** and could not drift — 2026-08-13 is over
and it produced what it produced. That reasoning stood in a `quantity:` line until the field was
rejected and the rule made unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]): a number that genuinely
cannot drift still leaves the title, because the mechanism that let a page say so has been
withdrawn. The title now names the decisions instead of counting them
([[a-title-names-what-is-counted-instead-of-counting-it]]), and that is a correction in place
rather than a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## The lesson is about what to do with the question

The plan was detailed and had been reviewed. What it lacked was not detail: **it described
behaviour without describing how the behaviour would be observed.** A design that cannot be
checked is not a design that is merely unverified — it is one that has not finished being
designed, and the missing part is usually load-bearing.

So when the owner says he cannot see how to check something, **build the check rather than
explaining the intent again**. Both times here, the check turned out to be a twenty-line bash
script, and both times it immediately found something ([[vault-scripts]]).

The neighbouring lesson, about checks that exist and prove nothing:
[[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]].
