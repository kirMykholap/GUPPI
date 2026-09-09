---
title: "A path-scoped rule fires on a read, and an Edit on a matching path delivers nothing"
type: concept
status: deprecated
authority: scoped-rule-trigger
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "[[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md"]
tags: [agents, harness, process]
superseded_by: [[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]
---

# What the documentation says, and what the tool contracts add to it

**The vendor documentation says "reads" and is silent on Edit, Write and Bash**
([[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]). The gap is closed by the
tools' own contracts rather than by measurement:

| action on a matching path | does the rule arrive |
|---|---|
| reading the file | **yes** — the documented case |
| editing an existing file | **yes, by implication** — Edit requires the file to have been read in this session |
| writing over an existing file | **yes, by implication** — Write requires the same |
| creating a new file | **no** — there is nothing to have read |
| a Bash command touching the path | **no** — no read tool is involved |

> **The second row is measured false, 2026-08-19.** An Edit on a matching path delivers **nothing** —
> the hook produced no line at all. See *The table was measured and one row of it is wrong* below.

**That "touching an existing file triggers the rule" is the owner's reading and it is correct**: the
read the rule needs is the one the editing tool already demands. It is `basis: human` for that
reason and not `external` — the vendor text does not say it.

# Why this decides which rules can move at all

**The criterion is that the dangerous action requires reading a matching file first.** Applied with
the table above, of the nine rules in the repository's `CLAUDE.md` exactly one survives it
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]):

- **the AST boundary rule moves** — its dangerous action is editing an existing boundary test;
- **the JavaScript rule does not** — the dangerous action is writing a *new* file, which matches no
  read ([[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]);
- **the test-database rule does not** — `uv run pytest` is a command, and a command reads nothing
  ([[the-suite-never-runs-against-the-production-database]]).

**The two failures are the same failure**: the rule is scoped to the artefact and the danger is in an
action that never opens it.

# The two questions the contracts do not close

**After `/compact` a scoped rule is not re-injected**; it returns only on a fresh matching read.
Whether that matters reduces to one measurable thing — **whether Edit demands a re-read after
compaction**. If it does, the rule comes back on its own and the question closes; if it does not,
the rule is gone, nothing brings it back, and the loss is invisible in the transcript.

**Whether a scoped rule reaches a subagent that reads a matching file is documented nowhere**, and
every task here is reviewed by one. That is the blocker rather than a detail.

**Both are laid as measurements rather than argued** — [[the-conditional-delivery-probe]], probes 4
and 2 respectively, inert until the harness restarts.

# The table was measured and one row of it is wrong — 2026-08-19

**Probe 4 falsified the second row.** *"Editing an existing file — yes, by implication — Edit requires
the file to have been read in this session"* is false as a statement about delivery, and the reasoning
under it is where it goes wrong.

**Delivery is triggered by the Read tool, not by touching a matching path.** The Edit produced **no hook
line at all**, so the mechanism never fired — not *fired and was not shown*
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

**And the Edit tool's read gate is *session*-scoped, not context-scoped.** It survives a `/compact`, so
after one the Edit sails through: the tool remembers the read, the model does not have the rule, and
nothing reports the gap.

## What that does to the rest of the table

| row | how it stands now |
|---|---|
| reading the file | **unchanged — yes**, and it is the only trigger there is |
| **editing an existing file** | **no.** The gate that made it look like *yes* is a different mechanism from delivery |
| writing over an existing file | **assume no**, on the same reasoning; not separately measured |
| creating a new file | still **no**, and now for the stated reason rather than the implied one |
| a Bash command touching the path | still **no**, same |

**Rows two and three were true only while nothing had cleared the context**, which is a much weaker
claim than *by implication*. Rows four and five were right for a reason the page did not give.

## What it reaches

**This is the page the movability criterion rests on**, cited by
[[moving-a-rule-into-claude-rules-with-a-paths-scope]] to decide which of nine rules can move — **so the
correction reaches that proposal and not only this page.** The criterion itself survives: *the dangerous
action requires reading a matching file first* is still what separates the AST rule from the other two.
What fails is the assumption that the dangerous action **is** a read, which is why the move now needs a
guard rather than nothing ([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]],
[[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]).

**Both of the open questions at the foot of this page are now answered** and neither answer is the one
the page hoped for: compaction does **not** close on a demanded re-read
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]), and a scoped rule **does**
reach a subagent ([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

*The title is corrected in place and the page keeps `basis: human`, because what the owner read is what
this page records and a measurement does not retroactively change whose reading it was. A title
corrected in place is not a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]), and
whether this page should instead be superseded whole is raised in the brief rather than decided here.*

# Superseded whole on 2026-08-20, on the owner's ruling

**Ruled 2026-08-19, on the brief's alarm**: this page is to be **superseded whole**, not left as a
title corrected in place. The in-place correction was the narrower of the options available and the
owner took the wider one — the same shape as the criterion rewording of the following day
([[hiding-a-file-from-a-denominator-is-weaker-than-counting-it-as-handled]]).

**The successor is [[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]**, which
carries the corrected table, the movability criterion unchanged, and the answers to both of the open
questions at the foot of this page.

**Read this page for what was believed and why it looked sound**: the reasoning that Edit's read
gate implies delivery is the exact confusion the measurement separated, and it is the only record of
it ([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).
