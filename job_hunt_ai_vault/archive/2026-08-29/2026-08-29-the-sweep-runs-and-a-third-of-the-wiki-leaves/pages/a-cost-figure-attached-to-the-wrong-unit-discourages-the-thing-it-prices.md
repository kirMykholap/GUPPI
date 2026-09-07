---
title: "A cost figure attached to the wrong unit discourages the thing it prices"
type: lesson
status: archived
authority: cost-figure-unit
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md"]
tags: [process, agents, vault]
---

# The figure was right about something else

**The store carried *fifteen to thirty minutes* as the price of a librarian dispatch. Measured, that
is the price of an INGEST.** Two dispatches on 2026-08-20, both reported by the harness rather than
self-reported:

| dispatch | work | wall clock | tokens | tool uses |
|---|---|---|---|---|
| a `/pre-task` question | read-only; enumerated 167 `decisions/` by frontmatter, opened 12 in full | **5m54s** | **98,378** | **36** |
| a narrow write | two frontmatter lines on two named pages | **1m24s** | **21,588** | **12** |
| an ingest, for comparison | the full compile | 25m34s | 224,128 | 82 |

Recorded as observed, and neither converted to money nor restated as a rate
([[a-subagent-cannot-report-its-own-cost]], [[agent-round-trip-cost]]).

# What the wrong unit cost

**The session quoted 15–30 minutes to the owner before he approved spending it, and was wrong by
4x** — in the direction that discourages asking. **Asking paid twice**: the `/pre-task` surfaced a
verdict the vault held no answer to ([[an-absent-render-is-red-on-a-page-that-renders]]) and a hole
`--collect-only` cannot see ([[collect-only-cannot-exercise-an-assertion-message]]).

**The asymmetry is the lesson.** A price quoted too high suppresses the act silently — nobody
records the question they decided not to ask — while a price quoted too low is corrected the first
time the bill arrives. **An overstated cost has no feedback loop.**

# It has bitten this project before, in the same shape

**The implementer figure was applied to a retrieval agent on 2026-08-13 and overstated it by two
orders of magnitude**, nearly deciding a design question on it. The boundary written then —
*a measurement travels with the class of work it was taken on* — is the same boundary broken here,
in the other direction ([[agent-round-trip-cost]]).

# What it moves now

**The scouts proposal is priced against the wrong denominator.** Its per-dispatch floor is argued
against the ingest's cost, and **a narrow dispatch is already cheaper than that floor**
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]).

**The remedy is not a better number, it is the unit beside it.** Every figure in this store's cost
tables names the class of dispatch it was taken on; the one that misled here was quoted without one.

# The class survived on the one page where the figure does the most work — corrected 2026-08-20

**[[a-pre-task-runs-before-anything-non-trivial]] said *"a librarian dispatch runs 15 to 30 minutes
and the fixed cost dominates"* and cited [[agent-round-trip-cost]] for it** — while that page had
already been corrected to say the opposite in its own words. **The citation resolved to a page
contradicting the sentence citing it.**

**That is the worst placement available for this defect.** The number is quoted there precisely as
the counterweight to the trigger, so the reader meeting it is a reader deciding **whether to pay** —
and they were reading a price about five times the measured one, at the exact moment the decision is
made.

**Corrected on the successor**, [[a-pre-task-runs-between-the-plan-and-its-approval]], which carries
the measured figures: a `/pre-task` question at **5m54s**, and a per-dispatch floor of **1.5 to 4.2
minutes** for the class. The retired page carries the correction as a dated note rather than an
edit.

**Reported by the session as a `- miss:` against the librarian**, and it is the shape this store
should expect from that channel: the corpus corrected a figure in one place and left every sentence
that had copied it standing, with the citation still pointing at the corrected page.

# It happened again, and this time a decision was taken on the wrong figure — 2026-08-21

**«About 90 seconds» was quoted as the price of a `/pre-task`-as-agent. 89 s was the wall clock of
one scout reading one folder** — a row in the table on the page that has since been retired as
refused ([[the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched]]).

**The honest figure is about 90 s for the empty case and 3–5 minutes where there are findings**,
because an agent doing the whole ritual returns to the measured 5m54s minus the enumeration saving
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**The owner had already ruled on it.** «Мы платим за это 90 секунд в среднем» was said before the
correction was offered ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]). **This is the
direction this page did not predict**: the first occurrence overstated a price and suppressed the
act, which fails silently; this one understated it and bought a ruling, which fails loudly and later.

**The asymmetry above still holds and is not weakened.** A price quoted too low is corrected the
first time the bill arrives — and the bill has not arrived, because nothing is built.

# Having read this page did not prevent it

**This is the second time this exact defect is on the record here, and the store had a page for it —
this one.** The session that quoted the wrong unit had read it.

**That is the argument this project already made about rules generally**: knowing a rule is not a
mechanism, and the remedy for a defect that survives being written down is something that runs
([[knowing-a-rule-is-not-a-mechanism]], [[no-rule-reads-a-harness-file]]).

**What would have caught it is cheap and is not built**: a figure quoted for a class of dispatch has
to name the class it was measured on, and both occurrences failed at exactly that line
([[agent-round-trip-cost]], [[an-unsourced-number-is-dropped-not-chosen]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# A third occurrence, and this time in the file a reader opens while deciding whether to pay — 2026-08-21

**`wiki/concepts/the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch.md` and
`.claude/skills/pre-task/SKILL.md` both quote `1m24s` and `21.6k tokens` as the price of phase 2's
read.** In [[agent-round-trip-cost]] that same row is labelled **a narrow write — two frontmatter
lines on two named pages.** A write figure is being quoted as a read price.

**And phase 2 has never been run**, so its price is unmeasured rather than merely mis-stated
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

**The section above already says that having read this page did not prevent it. It now has a third
instance**, and the remedy it names — a figure quoted for a class of dispatch must name the class it
was measured on — is still not built into anything that runs
([[knowing-a-rule-is-not-a-mechanism]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# One of the two files the third occurrence names was deleted, and the other now carries a measurement — 2026-08-22

**`.claude/skills/pre-task/SKILL.md` no longer exists.** It was deleted on 2026-08-22, when the
ritual became an agent ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]). **The section
above is not repointed and this page's `sources:` is unchanged**: the claim is that `1m24s` and
`21.6k tokens` stood at that path, and `.claude/agents/pre-task.md` carries no such figure — so
moving the name would turn a true sentence into a false one. The file is named here as deleted only
so that a reader is not left hunting for it ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**Ten `wiki/` pages that cited the skill in `sources:` were repointed to the agent on the same day**,
and this page was deliberately excluded from that sweep for the reason above.

**Phase 2's read is measured, so the third occurrence's *unmeasured rather than mis-stated* half is
now dated.** 233,165 tokens, 49 tool uses, 10m40s, 65 pages opened over a 43-page shortlist, read off
the harness's usage report rather than reported by the subagent
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]],
[[a-subagent-cannot-report-its-own-cost]]).

**The defect this page names is untouched by that.** A measured figure is not thereby attached to the
right unit: this one was taken on a `vault-librarian` dispatch over a named shortlist — phase 2 as
the skill defined it — and the mechanism that exists today reads inside the pre-task agent's own
body. **It is quoted with the class it was measured on, which is the remedy this page has asked for
three times and which is still built into nothing that runs** ([[knowing-a-rule-is-not-a-mechanism]]).

## The unit the price was owed on has its own reading now — 2026-08-22

**The paragraph above says the measured figure was taken on a class that no longer runs and that the
mechanism which does *reads inside the pre-task agent's own body*. That body has been measured:**
146,705 tokens, 57 tool uses, 13m36s, 53 pages shortlisted from 362 filtered rows, 16 opened in full
and 16 in part ([[agent-round-trip-cost]],
[[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**The remedy was applied by hand again, which is this page's standing complaint.** The figure is
quoted with its class — the whole ritual in one body, not a dispatch over somebody's shortlist —
because a librarian wrote it that way, and nothing that runs enforces it
([[knowing-a-rule-is-not-a-mechanism]]).

**The two figures are far enough apart to matter to a reader deciding whether to pay**: fewer tokens
and a longer clock than the phase-2 reading beside it. **Quoting either one as *the price of a
`/pre-task`* would be the defect this page is about**, and both now carry their unit.
