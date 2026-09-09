---
title: "A `/pre-task` runs before anything non-trivial, and before an area untouched this session"
type: rule
status: deprecated
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "[[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]", "[[one-librarian-behind-every-caller]]", ".claude/agents/pre-task.md"]
tags: [harness, agents, vault]
superseded_by: [[a-pre-task-runs-between-the-plan-and-its-approval]]
---

# What travels

<!-- text -->
`/pre-task` before implementing anything non-trivial, and before touching an area you have not
touched this session. It is the same librarian, asked about a plan instead of a topic.
<!-- /text -->

**That is the `/pre-task` paragraph of the repository's `CLAUDE.md`, to the byte** — cut out at
`e478c19` by line number and diffed against the slice above rather than read against it. The diff is
empty. The `/vault-ask` paragraph directly above it in that file is **not** part of this slice and
is not a rule page: it is a pointer at a callable thing, and the file keeps its own pointers
([[the-repository-claude-md-becomes-a-dispatch-table]]).

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

**This rule *is* the question.** It has no failure mode other than not being read: nobody who has
skipped a `/pre-task` ever notices that they did, because what a pre-task returns is a constraint
the plan had already assumed away, and a plan with an assumed-away constraint reads as a good plan.

That is not a guess about the failure — it is what every measured run has returned. The findings on
[[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]] are of exactly one kind: a check
that would have been green over an empty set, a field named in prose that no schema could evaluate,
and a path that resolved to a different file depending on where you stood. **In each case the code
would have been written, would have passed, and would have been wrong.** None of the three was
reachable by writing the code carefully.

So the rule is delivered rather than cited. A reader who is about to skip it has, by construction,
no reason to go looking for the page that says not to.

# A second measurement, 2026-08-17

The session that ordered this page ran another one, and it found **three defects in the proposal it
was checking. One of them would have made the selftest case pass for the wrong reason.**

That is this project's most-repeated failure returning inside the instrument built to catch it — a
check that passes having examined nothing
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). It is also the second time a
`/pre-task` has corrected a design *this project had already argued out in writing*
([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]): a proposal page is a question put
to the owner, not a settled fact, and reading it as a specification is how a defect survives review.

**Three runs are on the record — the two of that lesson and the one above — and each returned at
least one finding.** That is the number to watch: the day one returns nothing is the day the trigger
is worth re-examining, and until then the cost argument has an answer.

# Why the trigger has a half that is not a judgement

*Non-trivial* is a judgement about the work, made by the party that wants to start it — which is the
party least able to make it, since the whole point is that they do not know what constrains them.
**The second half is not a judgement at all**: *an area you have not touched this session* is a fact
about the session, and it fires precisely where the first half would have said no.

That half is the one the measured lesson recommends copying, in its own words: run it before an area
you have not touched this session, and before any plan whose correctness depends on what the tree
currently contains.

# What is being called, and why it reads differently from `/vault-ask`

**The same librarian, asked about a plan instead of a topic** — the rule says so, and it is the
whole of what makes the two entry points one definition rather than two
([[one-librarian-behind-every-caller]], [[vault-librarian]]). The discipline is the opposite one, and
that is the part a reader gets wrong:

- a **topic** query bounds reading — stop at about ten pages and report what could not be narrowed,
  because a librarian that reads forty pages answers worse than one that reads five;
- a **plan** query bounds *opening* and never *enumerating*. It sweeps frontmatter across every
  `decisions/` page and opens only what the titles implicate, because a ranked partial answer is the
  dangerous one when the decision your plan violates is twelfth of eight returned.

**The cost is real and this project has never pretended otherwise** — a librarian dispatch runs 15
to 30 minutes and the fixed cost dominates ([[agent-round-trip-cost]]). The measurement is the
counterweight to that number, not a denial of it, and it is the reason the trigger is written as two
conditions rather than as *when in doubt*.

# Why no test holds it

**Nothing in the tree records whether a plan was checked before it was written.** A pre-task leaves
no artefact: its answer arrives in a transcript, the plan that follows looks identical whether or
not it ran, and a check could at best confirm that some document still says the words. What that is
worth is on the record — seven harness divergences, none caught by anything mechanical
([[no-rule-reads-a-harness-file]]).

It therefore passes the folder's admission test exactly: imperative, and not enforced by a test
([[rules-becomes-a-type-of-its-own]]).

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]).

**The page and its region belong in one change, and this page arrived first.** Until the session
marks the region and runs the injector, rule 12 reports this rule as governing a file that carries
no region for it ([[a-governed-file-with-no-region-is-an-advisory]]). If the rule is ever replaced,
the successor renders and this page does not ([[a-deprecated-rule-does-not-render]]).

# What is on the lesson instead of here

[[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]] answers
`authority: pre-task-value` and carries the findings run by run. This page carries the instruction
and carries `governs:` in place of an `authority:`, so the pair does not read as two answers to one
question ([[rules-becomes-a-type-of-its-own]]).

# Retired 2026-08-20, and the cost figure above was wrong while it stood

**Superseded by [[a-pre-task-runs-between-the-plan-and-its-approval]].** The trigger changed, so
this is a changed claim rather than a corrected title: the rule now keys on a plan being presented
and on the first write of a session that presents none, and *an area you have not touched this
session* is deliberately not carried over
([[the-pre-task-trigger-becomes-the-plan-and-the-first-write]]).

**The text above no longer renders anywhere.** A deprecated rule does not render
([[a-deprecated-rule-does-not-render]]), the successor governs
`.claude/hooks/messages/pre-task.md` under `render: whole` rather than `CLAUDE.md`, and the region
this page held left that file in the same change
([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]).

**The cost figure in *What is being called* is wrong and is corrected on the successor, not here.**
This page says *"a librarian dispatch runs 15 to 30 minutes and the fixed cost dominates"* and cites
[[agent-round-trip-cost]]; that page says **the per-dispatch floor for this class is 1.5 to 4.2
minutes, not 15 to 30**, and measures a `/pre-task` question at **5m54s**. The citation had been
resolving to a page contradicting the sentence that cited it, on the one page where the figure does
the most work — it is quoted here as the counterweight to the trigger, so a reader deciding whether
to pay was reading about five times the measured price
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]). Reported as a
`- miss:` by the session of 2026-08-20 and corrected at that day's third ingest.

**And *"nothing in the tree records whether a plan was checked before it was written"* stopped being
true on 2026-08-20**, in the same session: the ritual records itself into a ledger
([[the-pre-task-ledger]], [[the-ritual-records-itself-rather-than-being-detected]]). The sentence is
left standing because it was true from 2026-08-17 until that day, and because it is what the session
that built the artefact was answering.
