---
title: "A mapping written against a repealed invariant loses rows silently, and the defect can be older than the code"
type: lesson
status: current
authority: repealed-invariant-in-fresh-code
basis: measurement
sprint: S3
created: 2026-08-31
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "scripts/build-families-table.py", "job_hunt_ai_vault/wiki/decisions/authority-uniqueness-becomes-a-per-type-question.md"]
tags: [vault, harness, record-schema]
---

# The incident, 2026-08-31

**`scripts/build-families-table.py` reported 293 prohibitions where the tree holds 295.** It was
written that morning and it keyed a dictionary on `authority:`, which had been unique across the whole
corpus until the day before.

**`authority:` became shareable across types on 2026-08-30**
([[authority-uniqueness-becomes-a-per-type-question]]). The two rows lost were exactly the two slugs
carried by two pages each: the later page overwrote the earlier one in the dict, and nothing raised
anything.

# Why this shape is worth a page

**The defect was a day older than the code that contained it.** The author had every invariant right
except the one that had moved, and the code was correct against the store as it stood the previous
week. Nothing about writing it carefully would have caught that — the mistake is not in the code, it is
in the model of the store the code was written from.

**It fails by under-reporting, which reads as a smaller problem rather than as a broken instrument.**
293 against 295 looks like an off-by-two that somebody will get to. A count that came back *larger*
would have been investigated in the same minute.

**And the instrument was the input to a judgement, not a report.** The table is what the 53 cleanup
verdicts were set from, so two families silently short is two verdicts set against incomplete
information ([[the-cleanup-verdict-names-which-delivery-a-family-gets]]).

# What follows

**A uniqueness assumption is a claim about the corpus and has a date.** When a script keys on a
frontmatter field, the question is not *is this field unique* but *when was that last decided*, and
`job_hunt_ai_vault/CLAUDE.md` is where the answer lives.

**Compare the count against an independent one before trusting a derived table.** Here
`rg -c "^binding: prohibition"` over the tree was the second reading and it is what exposed the gap;
the generator's own total could never have.

**This is not the positional-fixture class.**
[[a-fixture-pinned-to-the-end-of-a-file-expires-when-a-block-is-appended-below-it]] is an artefact
depending on a *position* a later edit moved. Here the artefact depends on an *invariant that was
repealed*, which no amount of reading the file it processes would reveal.

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
