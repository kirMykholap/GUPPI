---
title: "The corpus is mostly about itself, and the owner noticed before any instrument did"
type: lesson
status: current
authority: corpus-self-reference-share
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md"]
tags: [vault, process, architecture]
---

# The incident

**The session of 2026-08-30 opened with the owner saying he had stopped understanding what the project
does.** Nothing in the harness had raised that; he raised it. The numbers below were measured for him
afterwards, from git and the tree.

# What was measured

**Commits.** Since 2026-08-13 the repository has taken **124 commits, of which 2 touched `src/` or
`tests/`**; the other 118 touched the vault, `.claude`, `scripts` or `docs`. **The last change to
`src/` is `e15a12c`, 2026-08-12** — seventeen days before.

**Subject.** `wiki/` held **568 live pages, of which 68 match any of**
`vacanc|work.ua|dou.ua|ваканс|htmx|postgres|scraper|parser` — **12%**. By folder: decisions 32 of 299,
concepts 23 of 140, entities 5 of 45, proposals 4 of 49, lessons 1 of 18, rules 1 of 17.

**Size.** The vault side is **~62,000 lines of markdown** (wiki 45,788 plus registers 16,371) against
**20,659 lines of Python** under `src/` and `tests/`, with a further **10,459 lines in `scripts/`** and
**4,399 in `.claude/`**.

**Startup cost.** What loads before the first prompt, measured 2026-08-29: the vault's `CLAUDE.md` at
25,020 bytes, `brief.md` at 14,050, the repository `CLAUDE.md` at 9,296, `MEMORY.md` at 2,253 — about
**50 KB, or ~13,000 tokens**, of which the vault's own schema document is half.

# What the numbers do and do not mean

**They mean the store and its instruments are together about three and a half times the product they
document**, and that the corpus is overwhelmingly about itself. **The 12% is generous**: it is a
mention test, not a subject test, so the true product share is **lower rather than higher**.

**They do not mean the product is finished** — nothing here measures that — **and they do not mean the
instrument is worthless.** They mean its running cost is now visible and its saving is not.

**The size figures exclude `archive/`**, which holds a further 326 pages.

# The part that is a lesson rather than a number

**The product has been static by decision, not by drift**
([[product-work-does-not-interleave-into-the-vault-sprint]]) — so none of the above is a surprise to
the tree. **It was a surprise to the owner**, which is the actual finding: **nothing in this repository
reports the ratio it is running at.** The brief reports growth; no instrument reports what the growth
is about.

**And the largest fixed cost per session and per agent is the vault describing itself.** That is a
cost paid before any question is asked, by every agent, on every dispatch
([[what-loads-into-every-session-before-the-first-prompt]]).

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
