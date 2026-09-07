---
title: "A long document contradicts itself, and position does not tell you which passage won — a date or a commit does"
type: lesson
status: archived
authority: superseded-text-in-a-long-source
basis: inference
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md"]
tags: [vault, process]
---

# Two versions of one claim, and position does not separate them

**Where a long source disagrees with itself, prefer the passage that carries a date or a commit.
Where neither does, check the code.** Not the later passage, and not the earlier one: in the only
document this vault has had to apply the rule to, the correct version came **first** both times it
could be tested.

## The two instances, both checkable at the line

| Claim | Correct passage | Superseded passage | What marks the winner |
|---|---|---|---|
| the post-collection chain | line **151** — chips first, then the rows | line **363** — the filters form hears the event | 151 names the commit `dd1b446`; 363 names nothing |
| the salary re-parse | line **397** (§0.5) — «done 2026-08-05… Do not repeat it» | line **1160** (§6) — a full re-parse is still «нужен» | 397 carries a date; 1160 dates nothing |

Both in `raw/handoffs/2026-08-12-handoff-before-the-vault.md`. The first cost a Critical
([[table-refreshes-itself]] describes the chain the code actually has). The second cost nothing,
because [[salary-cannot-be-reparsed]] took the earlier text and is right — the same choice, made
correctly, by the same pass that got the first one wrong.

## Why position says nothing about that document in particular

**It did not grow by appending. It grew by prepending.** §0, «What the next session does first»,
was rewritten at the top of the file at the start of each session, while the per-slice records
below it stayed frozen at the date of their slice: line 363 sits in §0.4 «What slice 2b built»,
line 1160 in §6 «Известные ограничения». A section that is the record of a past slice is not
updated when the thing it records changes — that is what makes it a record rather than a
description.

So «the later passage wins» is not a weaker rule than the one above. It is the wrong rule, and it
would have picked the wrong passage twice out of twice here.

## What the first compiling pass actually did, as far as it can be established

**This page said until 2026-08-13 that «the first compiling pass copied the first version it
met», and that cannot be what happened**: the first version it met was the correct one.

What the artefacts do show — the page's first committed version, `5b13412`, read beside the
source:

- its title and lead are lines 363–365 almost verbatim, «because the form is what knows the
  current filters, and the panel is not»;
- its bullets are lines 25–32 — the §0 blockquote about the 2026-08-11 re-read, which is *earlier*
  than 363 and was used;
- nothing from line 151 appears at all: no chips-first order, no `#tag-chips`, no `dd1b446`.

The pass therefore composed one page out of **two** passages, and took its topic sentence from the
one whose wording matched the topic: line 363 opens «**The table refreshes itself**», and the page
is called `table-refreshes-itself`. Line 151 is a bullet whose own bold lead is about the chip row,
under a heading about what the next session does.

**Why line 151 was not used cannot be established.** Whether it was read and discarded or never
reached leaves no artefact, and this page will not pretend otherwise. What can be said is that the
mechanism was **vocabulary, not position** — the first *hit* on the topic's own words was the
superseded one, which is the only sense in which this page's filename is accurate. The filename is
kept because every citing page uses it and because renaming loses more than it fixes; the rule is
the one at the top.

Two of the four statements above are verifiable by anyone (the line numbers, and the diff at
`5b13412`); the third — what the pass was doing — is reconstruction, which is why the whole page
is marked `basis: inference` rather than at the strength of its evidence.

## Why this is the vault's own thesis, turned against it

The vault exists because a 129 KB document that is appended to and prepended to cannot be kept
true. **The migration out of that document was performed by reading it the way that made it
untrue.** The resulting page contradicted its own second half and passed every mechanical check:
the page existed, its identifiers matched, its links resolved. An outside reviewer found it by
reading the templates and marked it Critical.

- **Read to the end before writing the page.** Still the first instruction, now for a sharper
  reason: you cannot know which passage carries the date until you have seen them all.
- **Say on the page what the superseded version claimed**, because "why did we move away from X"
  is a legitimate question six months later.
- **Coverage would not have caught this and cannot.** It is a fidelity failure: every unit had a
  verdict and the verdict pointed at a page that said the wrong thing. Fidelity is checked by
  sampling and by the acceptance questions ([[ingest-is-units-and-verdicts]]).

This is also the argument for the vault's supersession rules rather than for editing in place: a
replaced page is deprecated and names its successor, so the two versions cannot sit silently in one
file with nothing but their position to tell them apart.

## The sibling failure: a source that was never right

Recorded 2026-08-13, from the first fidelity sample this vault has run. §6 of that day's journal
said `docs/HANDOFF.md` had **245 units**; the script had never produced that number under any rule.
The page compiled from it inherited the error **into its title**, where it guarded the gate on
retiring the file — see [[handoff-retires-only-when-every-unit-has-a-verdict]].

Two things generalise, and neither is worth a page of its own:

- **A source can be simply wrong, not merely out of date.** Reading to the end does not help; only
  re-deriving the claim does. Prefer a claim a reader can re-run — the name of a command — over
  the value it printed once.
- **A number in a title is a hostage to the tool that produced it.** A measurement in the body can
  carry its date and be corrected beside its predecessor; a title is quoted, greped and linked, and
  it cannot be dated. Keep derived numbers out of titles.

**Coverage would report both of these green.** The verdict existed and pointed at a real page; only
opening the unit beside the page it became caught it.

## The class has now been met three times, and the third was at 24× the scale

**A verdict, or a citation, can point at a page that does not contain the claim — and no script can
see it.** Three instances, each found a different way, all on 2026-08-13:

| Instance | Found by |
|---|---|
| a number in a page title that no tool had ever produced | **sampling** ten sidecar lines against their pages |
| `alembic check` filed to a page with no mention of migrations | a **reviewer**, reading the pair |
| **24 pages citing `docs/HANDOFF.md`**, a 27-line pointer at `d30b317` and **29 lines when measured 2026-08-15** | the librarian, greping its own `sources:` fields |

The third is the one to remember, because it was not a mistake anybody made: the pages were right
when they were written, and **the file they cited was truncated out from under them**. Rule 11 of
`vault-check.sh` asks only whether the path exists ([[vault-scripts]]). They were repointed to the
verbatim copy in `raw/`, which is where the claims actually are — and that is the general remedy:
**cite the immutable copy, not the living document.**
