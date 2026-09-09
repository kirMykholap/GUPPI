---
title: "What an agent round trip costs, and why the figure describes implementer trips only"
type: lesson
status: archived
authority: agent-round-trip-cost
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [process, agents]
---

# An agent round trip costs 5 to 35 minutes

Measured on slice 3, which cost a session of eight to ten hours — an outcome the owner called
unacceptable for what it produced.

Where the time went, measured rather than guessed:

- every task ran implementer → review → fix wave → re-review. **Seven tasks × three or four round
  trips is the session.**
- **fix waves are the most expensive step**: 35 minutes for one, and 30 for a task that was then
  thrown away;
- Minor findings were dispatched to agents — a 10–35 minute round trip for a one-line comment,
  several times. The skill never asked for that; it says to *record* Minor findings.

What the measurement bought is [[how-a-slice-is-executed]]: the implementer trip and the fix-wave
trip were removed, because neither buys anything an edit in the main session does not. Review
stayed, and stayed whole.

## The boundary of the number, which matters as much as the number

**It describes *implementer* trips — agents that write code and run tests.** It does not describe
every subagent call. A librarian call, which greps and reads a dozen pages, is tens of seconds.

That distinction was not recorded at first, and on 2026-08-13 the figure was applied to a retrieval
agent, overstating its cost by two orders of magnitude and nearly deciding a design question on it.
A measurement travels with the class of work it was taken on, or it misleads the next person to
quote it.

### The librarian call now has numbers, measured 2026-08-14

Five `vault-librarian` dispatches, the acceptance run ([[the-acceptance-questions]]). Reported by
the harness as `subagent_tokens`, **whose composition is undocumented** — input, output or both is
not stated anywhere we can read — so it is recorded as observed and **not converted to money or
restated as a rate** ([[a-subagent-cannot-report-its-own-cost]]):

| | tokens | wall-clock |
|---|---|---|
| Q1 | 27584 | 2m54s |
| Q2 | 30420 | 2m54s |
| Q3 | 58779 | 8m20s |
| Q4 | 63400 | 6m53s |
| **Q5** | **25341** | **1m43s** |

**Q5 — 25341 tokens, 103 seconds — is the figure for a plain `/vault-ask`.** Q3 and Q4 carried
extra instructed work (a search-term report, and writes to `tags.md`), which is most of the spread
and all of the wall-clock difference. The 2026-08-13 claim that a librarian call is "tens of
seconds" was optimistic by a factor of two on this evidence, and the shape of the correction is the
usual one: the estimate stood until someone measured it.

### The writing class has four points now, measured 2026-08-15

A librarian *question* and a librarian *dispatch that writes* are two classes of work, and the
table above is the first. Four dispatches in one session gave the second its first figures. Same
caveat as above: `subagent_tokens` has undocumented composition and is recorded **as observed**,
never as a rate and never as money ([[a-subagent-cannot-report-its-own-cost]]).

| dispatch | work | tokens | wall-clock | tool uses | produced |
|---|---|---|---|---|---|
| 1 (2026-08-14) | ingest of a 29-unit note | 144119 | 15m25s | 66 | 3 pages, 5 updates, 1 contradiction |
| 2 | ingest of a 91-unit note + 2 more tasks | 183809 | 29m26s | 103 | 6 pages, 8 updates, 3 registers, 1 contradiction resolved |
| 3 | writing only, four tasks, no source compiled | 125348 | 14m26s | 58 | 5 pages, 2 supersessions, 6 updates |
| 4 | the first `/vault-lint`, over 108 pages | 232794 | 26m34s | 131 | 13 findings, 16 pages fixed |
| **total** | four dispatches, one session | **686070** | **85m51s** | **358** | |

**Two things the four points say, and one they do not.**

- **The fixed cost of a dispatch dominates a small one.** Points 1 and 2 are roughly three times
  the units for twice the wall-clock. Splitting work across dispatches is therefore not free, and
  when it is done anyway there has to be a reason worth about fifteen minutes
  ([[the-audit-is-dispatched-after-the-writes]] is one).
- **An audit costs about what a large ingest does** — point 4 against point 2. That is the price
  tag on `/vault-lint`'s once-per-sprint cadence.
- **None of them says what a dispatch carrying *one* task costs.** All four carried several, and
  point 3 is the closest thing to a floor at 14m26s for four tasks and no source.

Before this, the only figures in this project were for single librarian *questions* — 3 to 8
minutes each, in the table above — and the boundary that opens this section was written to stop
the implementer number being applied to them. It applies in this direction too: **an ingest is not
a question**, and 25341 tokens is not the number to quote for one.

## What the range still lacks, recorded on 2026-08-13

**The 5-minute lower bound has no named instance.** The 35-minute figure is attached to specific
trips — a fix wave, and a task later thrown away — while nothing in the record says which trip took
five. The upper bound is what the decision rests on, so the range is not wrong where it is used;
but quote the lower bound as an estimate until an instance is named.

### A fifth writing point, measured 2026-08-16

| dispatch | work | tokens | wall-clock | tool uses | produced |
|---|---|---|---|---|---|
| 5 (2026-08-16) | writing only, S1 criterion 3 | 115165 | 13m22s | 46 | 3 pages, 5 updates, a `log.md` entry, a regenerated catalogue |

**It sits inside the 14–29 minute band already recorded** — just under its floor, and the closest
thing this project has to one: no source compiled, a bounded task list. Same caveat as the table
above: `subagent_tokens` has undocumented composition, so the figure is recorded **as observed** and
is neither converted to money nor restated as a rate ([[a-subagent-cannot-report-its-own-cost]]).

**This is the number that moved a cadence.** Because the fixed cost dominates, `/ingest` was taken
off the per-session schedule and batched at the retrospective on the same day
([[ingest-is-batched-at-the-retrospective]]), and the same arithmetic is one half of the open
question about whether `/vault-ask` should dispatch at all
([[a-skill-is-a-mask-and-a-subagent-is-a-body]]).

## The cadence this number moved has since moved back — annotated 2026-08-17

[[ingest-is-batched-at-the-retrospective]] is **deprecated and archived**; `/ingest` runs after
`/handoff`, at the end of every session ([[ingest-runs-after-handoff-at-the-end-of-a-session]]).

**The arithmetic above survives the reversal intact**, and it is worth stating why: the fixed cost
is paid **per dispatch**, not per source. So "batch several sources" survives as the shape of a
single dispatch — one round trip, sources compiled one at a time inside it — while the per-sprint
cadence it was used to argue for did not. **A measurement that is used to settle a question can
outlive the answer it produced**, and the citation above is left in place for exactly that reason
([[a-live-page-can-argue-from-a-deprecated-one]]).

## A death is not always a re-dispatch — 2026-08-17

The librarian died on a 529 after 24 tool calls and ~98k tokens, having read the corpus and produced
nothing. **Resuming the same agent reused that context**; a fresh dispatch would have paid for the
reading twice — [[a-dead-subagent-can-be-resumed-instead-of-re-dispatched]].

## A read-only scout is a third class, and it has its own floor — measured 2026-08-20

**Six read-only `Explore` subagents, one per `wiki/` folder, dispatched together against six real
claims. Wall clock 249 s for 1028 s of work — 4.13x**, a batch being as long as its slowest member:
rules 89 s, proposals 127 s, entities 181 s, decisions 185 s, concepts 197 s, lessons 249 s.
**592k subagent tokens over 203 tool uses**, recorded as observed
([[a-subagent-cannot-report-its-own-cost]]).

**The per-dispatch floor for this class is 1.5 to 4.2 minutes, not 15 to 30.** The 15-to-30 band in
the tables above belongs to a **librarian doing full work** and cannot be assumed of a scout — which
is the same boundary this page opens with, applied a third time.

**So the fixed cost does not dominate for a scout**, and the design that needed that result gets it
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]). For the comparison the store already
holds: four librarian dispatches at 686k tokens and 85m51s, in the table above.

**The three classes now measured, and they differ by an order of magnitude:**

| class | wall clock per dispatch |
|---|---|
| read-only scout | 1.5 - 4.2 min |
| librarian question | 1.7 - 8.3 min |
| librarian dispatch that writes | 13 - 29 min |
| implementer | 5 - 35 min |

**The figure still owed is not a cost at all**: what fraction of a librarian round trip is read-only
search. Without it, 4x on the reading half buys an unknown share of the whole — and it is free to
collect, because the librarian's own tool calls are in its transcript.

## The librarian dispatch is not one price, and this page's band was the ingest's — 2026-08-20

**Two more points, both from the harness rather than self-reported**, taken in the session that
found the store quoting the wrong denominator:

| dispatch | work | tokens | wall-clock | tool uses |
|---|---|---|---|---|
| a `/pre-task` question | read-only; enumerated 167 `decisions/` by frontmatter, opened 12 in full | 98378 | **5m54s** | 36 |
| a narrow write | two frontmatter lines on two named pages | 21588 | **1m24s** | 12 |
| an ingest, the day before | the full compile of one journal | 224128 | 25m34s | 82 |

**So the 15-to-30-minute band in the tables above is the cost of an INGEST and has been quoted as
the cost of a DISPATCH.** The session quoted 15–30 to the owner before running the `/pre-task` and
was wrong by 4x, in the direction that discourages asking
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**This is the boundary at the top of this page, broken from the other side.** The 2026-08-13 error
applied an implementer figure to a retrieval agent and overstated it; this one applies a full-work
figure to a narrow dispatch and does the same. **The remedy is unchanged**: a figure travels with
the class it was taken on.

**The figure this page said was owed is now answered, as a self-report and no better.** The ingest's
own account: 79 calls, 41 read-type against 38 write-type, **first write 4m34s into a 24m30s run —
19% of elapsed time before writing began**, which is the only counted figure among them. **11 of the
41 reads came after writing started and are reads of its own output**, which no scout dispatched in
advance could perform. Its estimate of the scoutable share is **20–30%**. The split is a self-report
and is weaker than the harness figures beside it ([[a-subagent-cannot-report-its-own-cost]]).

**The arithmetic the owner asked for, from those numbers:** 4.13x on 20–30% removes 15–23% of the
wall clock — three to five minutes of twenty-four — and the six scouts that buy it cost **592k
tokens against the 224k the whole ingest cost**. All figures recorded as observed, and none
converted to money or restated as a rate.

## A second reading of a `/pre-task` question, and the wall clock did not move — 2026-08-20

| dispatch | work | wall-clock |
|---|---|---|
| a `/pre-task` question, 2026-08-20 fourth session | read-only; enumerated **184** `decisions/` pages by frontmatter, opened **47** in full — 25 from `decisions/` and 22 from elsewhere | **5m54s** |

**Same wall clock as the reading in the table above, against roughly four times the pages opened**
— 12 in full then, 47 now. **No token figure accompanies it**: the session reported the clock and
the counts, and a subagent cannot see its own usage
([[a-subagent-cannot-report-its-own-cost]]).

**Two readings are not a rate and are not converted into one** ([[an-unsourced-number-is-dropped-not-chosen]]).
What the pair does support is narrower and more useful: **the cost of a `/pre-task` is dominated by
something other than how much it reads**, so an answer that opens more pages is not thereby a more
expensive answer. The figure that would settle it — the fixed share of a dispatch — is the one this
page has recorded as owed since 2026-08-19.

## The narrow read over a named shortlist has its first figure, and it is the largest question yet — 2026-08-22

| dispatch | work | tokens | wall-clock | tool uses |
|---|---|---|---|---|
| a `/pre-task` phase 2 | read-only; a 43-page shortlist named by a catalogue pass, **65** opened in full | 233165 | **10m40s** | 49 |

**From the harness's usage report, not self-reported** ([[a-subagent-cannot-report-its-own-cost]]),
and recorded as observed — not converted to money and not restated as a rate.

**It breaks the librarian-question band this page has carried since 2026-08-14.** The band was 1.7 to
8.3 minutes; this is 10m40s, at roughly two and a half times the tokens of the largest reading in it
(98,378) and more than a full ingest cost (224,128). **What separates it from the questions beside it is how much it opened**: 65
pages in full, against 12 and 47 for the two `/pre-task` readings above.

**So the pair of readings above no longer supports what it was read to support.** *The cost of a
`/pre-task` is dominated by something other than how much it reads* rested on two runs at the same
wall clock across 12 and 47 pages; a third point at 65 pages and nearly twice the clock is against
it. **Three points are still not a rate** ([[an-unsourced-number-is-dropped-not-chosen]]), and what
they now support is only that the earlier pair did not settle the question.

**The class it was taken on, stated because this page's whole subject is that a figure travels with
one.** A `vault-librarian` dispatch over a named shortlist — phase 2 as `.claude/skills/pre-task/`
defined it, measured on the day that skill was deleted. The mechanism that exists now does the same
reading inside the pre-task agent, after its own phase 1, and has not been measured
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]],
[[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

## The mechanism that actually exists has a price, and it is the first reading of the whole ritual — 2026-08-22

| dispatch | work | tokens | wall-clock | tool uses |
|---|---|---|---|---|
| the `pre-task` **agent**, both phases in its own body | read-only; **53** pages shortlisted from **362** filtered catalogue rows, **16** opened in full and **16** in part | 146705 | **13m36s** | 57 |

**Two of the shortlisted pages were reached past the `binding:` filter and five were reached only by
following a link**, which is the walk the shortlist cannot produce by construction
([[the-folder-is-the-first-narrowing]], [[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**This is the reading the section above records as owed.** That section ends *"the mechanism that
exists now does the same reading inside the pre-task agent, after its own phase 1, and has not been
measured"*, and the sentence is dated here rather than rewritten
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**Read off the harness's usage report, not self-reported** ([[a-subagent-cannot-report-its-own-cost]]),
and recorded as observed rather than converted into money or a rate
([[an-unsourced-number-is-dropped-not-chosen]]).

### It is a different class from the row above it, and the comparison is the interesting part

**The phase-2 row is a read over a shortlist somebody else built; this row is the whole ritual,
shortlist included.** So they are not two readings of one thing, and this page's own subject is that
a figure travels with the class it was taken on.

**Against that caveat, the pair disagrees in two directions at once.** This run cost **fewer tokens**
than the phase-2 read — 146,705 against 233,165 — while spending **more wall clock**, 13m36s against
10m40s, and **more tool uses**, 57 against 49. It opened **16** pages in full where the other opened
65.

**So *the cost is dominated by how much it reads* is now contradicted from the other side.** The
earlier pair supported it, the phase-2 point was against it, and this point opens a quarter as many
pages for two thirds of the tokens and half again the clock. **Four points are not a rate**, and what
they support is only that pages-opened predicts neither the clock nor the tokens
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**And it is above the band this page carried until 2026-08-22 for a second time.** The
librarian-question band was 1.7 to 8.3 minutes; both readings of a full `/pre-task` since are outside
it, so the band describes a topic question and not this ritual.

## A narrow brief costs about a third of a wide one — 2026-08-22

**The title-rename dispatch: 50,160 tokens, 4m15s.** One page, one field, a stated rejected
alternative, and a check that nothing cited the page by its title
([[claude-code-config-loading]]).

**Against the wide write dispatches of the same session — 130k–150k tokens and 15–18 minutes each**,
each carrying a section's worth of rulings across ten or more pages. **So the band this page tracks
splits by brief width and not only by kind of work**: the same agent, the same corpus, a third of the
price.

**The session quoted fifteen minutes for it beforehand and was wrong by a factor of three**, in the
expensive direction — which is the direction that suppresses a dispatch that should have happened
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**Read off the harness's usage report, not self-reported** ([[a-subagent-cannot-report-its-own-cost]]),
and recorded as observed rather than converted into a rate ([[an-unsourced-number-is-dropped-not-chosen]]).

# A whole session's dispatch bill, read off the harness — 2026-08-26

**Seven dispatches cost 1,224,158 tokens and about 103 minutes of wall clock**, which is more than
half that session's wall clock:

| dispatch | tokens | wall clock |
|---|---|---|
| librarian write | 116,887 | 10 min |
| librarian write | 200,585 | 21 min |
| librarian write | 185,785 | 19 min |
| librarian write | 209,240 | 20 min |
| librarian topic query | 132,407 | — |
| librarian topic query | 164,532 | — |
| `/pre-task` | 214,722 | 17 min |

**What it does not say is what the time is spent on.** No split between corpus reading, gate runs and
page writing was measured, and none is derivable from these numbers. The corpus stood at about 720
live pages, so a write dispatch that reads before it writes is paying a bill that grows on its own
([[every-recorded-fix-for-the-suite-attacks-a-constant-and-the-corpus-is-the-term-that-grows]]).

**Read off the harness's usage report and not self-reported**, as every figure on this page is
([[a-subagent-cannot-report-its-own-cost]]).

**The session dispatched a twenty-minute agent without quoting its cost first**, which the
proportionality rule asks for before the money is spent; the owner asked for the number afterwards
rather than being offered it, and the same omission covers all four write dispatches
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**The owner named the librarian's dispatch as a conversation of its own for the next session** —
«обязательно поднять вопрос работы библиотекаря и его диспатча» — rather than a work item, so nothing
is designed against these numbers here.
