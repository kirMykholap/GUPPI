---
title: "A `/pre-task` runs between the plan and its approval, and before the first write where no plan was presented"
type: rule
status: current
governs: .claude/hooks/messages/pre-task.md
render: whole
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/check-the-plan.ps1", ".claude/hooks/pre-task-state.ps1", "CLAUDE.md"]
decided_by: [[the-pre-task-trigger-becomes-the-plan-and-the-first-write]]
tags: [harness, agents, process]
supersedes: [[a-pre-task-runs-before-anything-non-trivial]]
---

# What travels

<!-- text -->
`/pre-task` runs between the plan and its approval: the plan you present has already been checked
against the vault. If work starts without a plan, it runs before the first write.

You perform it by dispatching the `pre-task` agent — `subagent_type: "pre-task"` — and by nothing
else. It is no longer a skill anybody can type.
<!-- /text -->

**The first paragraph is the owner's own wording, quoted from the session of 2026-08-20 and not
paraphrased. The second is not his and was added on 2026-08-22**, by the session that turned the
ritual into an agent; it is written in this project's own voice and is marked here so that nothing
inside the slice is read as a quotation of him
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]],
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]). **What he ruled is that
`/pre-task` becomes an agent** ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]); the
sentence saying *how you invoke it* is the consequence written down, not something he said.

**Why the slice had to gain it.** Until 2026-08-22 the rule said only *when*, and *how* needed no
saying: `/pre-task` was a skill and typing its name was the whole invocation. With
`.claude/skills/pre-task/` deleted, a reader who obeys this rule exactly has no way to obey it —
which is the failure class this store already has a page for
([[the-pre-task-was-skipped-and-the-rule-has-no-by-hand-form]]).

**It stays one contiguous piece**, so the one-slice rule is unaffected: two paragraphs the
destination needs whole are still one run of text
([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]). The decision that replaced the
trigger is [[the-pre-task-trigger-becomes-the-plan-and-the-first-write]]; this page carries the text
that decision obliges, and everything below the line stays here
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why the trigger is a fact about the session and not a judgement about the work

**The predecessor keyed on `non-trivial`** — a judgement about the work, made by the party that
wants to start it, which is the party least able to make it. It was skipped in consecutive sessions,
three recorded instances with three different causes, and **in none of them did the session believe
it was starting implementation**
([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]]).

**Presenting a plan is a fact a hook can see.** So is the first write of a session that presented
none. Neither asks anybody to classify their own work.

**The second half of the old trigger — *an area you have not touched this session* — is deliberately
not carried over**, on the owner's word, and the narrowing it leaves open is stated on the decision
page rather than hidden here.

# Why it cannot wait for a question

**This rule *is* the question.** It has no failure mode other than not being read: nobody who has
skipped a `/pre-task` ever notices that they did, because what it returns is a constraint the plan
had already assumed away, and a plan with an assumed-away constraint reads as a good plan.

That is not a guess. **Every measured run on the record has returned at least one finding**
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]) — a check that would
have been green over an empty set, a field named in prose that no schema could evaluate, a path that
resolved to a different file depending on where you stood, and on 2026-08-20 a destination whose
extension put it outside the governed set entirely.

# What it costs, measured, and the figure this page used to carry

**A `/pre-task` question is 5m54s** — 98,378 tokens, enumerating 167 `decisions/` pages by
frontmatter and opening 12 in full ([[agent-round-trip-cost]]). The per-dispatch floor for this
class is **1.5 to 4.2 minutes**.

**The predecessor page said *15 to 30 minutes* and cited the same page for it.** That band is an
*ingest*, not a question, and the citation had gone on resolving to a page that says the opposite in
its own words. The number is quoted here precisely as the counterweight to the trigger, so a reader
deciding whether to run the ritual was reading a price about five times the measured one — the class
[[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]] names, surviving on the
one page where the figure does the most work. Corrected at the ingest of 2026-08-20, reported as a
`- miss:` by the session that found it.

# What is being called, and why it reads differently from `/vault-ask`

**The same librarian, asked about a plan instead of a topic**
([[one-librarian-behind-every-caller]], [[vault-librarian]]). The discipline is the opposite one:

- a **topic** query bounds reading — stop at about ten pages and report what could not be narrowed;
- a **plan** query bounds *opening* and never *enumerating*. It sweeps frontmatter across every
  `decisions/` page and opens only what the titles implicate, because a ranked partial answer is the
  dangerous one when the decision your plan violates is twelfth of eight returned.

**One `/pre-task` per approved scope, and the answer comes back per item**
([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]).

# A test does not hold it, and an artefact now records it

**The predecessor said *nothing in the tree records whether a plan was checked before it was
written*.** That is no longer true: `scripts/record-pre-task.ps1` writes a row and
`.superpowers/sdd/pre-task-ledger.tsv` keeps it ([[the-pre-task-ledger]]). The ritual **records
itself** rather than being detected, and the failure direction is the safe one
([[the-ritual-records-itself-rather-than-being-detected]]).

What still holds is that no *test* holds the rule: the ledger is a record, not an assertion, and
seven harness divergences are on the record with none caught by anything mechanical
([[no-rule-reads-a-harness-file]]). It passes the folder's admission test exactly — imperative, and
not enforced by a test ([[rules-becomes-a-type-of-its-own]]).

# Where it renders

`governs: .claude/hooks/messages/pre-task.md` under `render: whole` — a file the injector owns end
to end, generated from this page and delivered by `.claude/hooks/check-the-plan.ps1` at the moment a
plan is about to be presented ([[the-plan-check-hook]]). **It carries no `paths:` and therefore no
frontmatter block at all**: a hook message has no file to match, and `paths:` is required only where
Claude Code reads it ([[paths-is-required-where-it-is-read-and-nowhere-else]],
[[a-generated-rule-file-with-no-paths-carries-no-frontmatter]]).

**The region left the repository's `CLAUDE.md` in the same change this page landed in**, or rule 11's
address verdict fires on the leftover
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]). What that costs — a rule
that arrives only when a hook event fires — is the whole subject of
[[the-pre-task-rule-leaves-claude-md-for-a-hook-message]], and it goes against a criterion of the
owner's knowingly.

**A hook that cannot find this file says so out loud** rather than going quiet: the message names the
path, the injector and the repair, because a guard that is silently absent is worse than none.

# The librarian is no longer who answers this, and the sentence above stands as written — 2026-08-22

**The section *What is being called* says *"The same librarian, asked about a plan instead of a
topic."* That went false today.** `/pre-task` dispatches `subagent_type: "pre-task"`, a definition of
its own at `.claude/agents/pre-task.md`, and no `vault-librarian` is involved in the ritual at all
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).

**The sentence is not rewritten.** It is testimony about the day it was written, and it was true from
2026-08-13 until this morning ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]],
[[the-region-coverage-figure-is-dated-where-it-stands]]). **It sits outside the rendered slice**, so
nothing broke mechanically and no region disagreed with this page while it was false.

**What did not change is the reason that section gives.** *Duplicated instructions diverge* is still
why there was one definition for four callers ([[one-librarian-behind-every-caller]]) — and it is
exactly why a second definition was allowed to exist only alongside a rule page that renders the
shared half into both
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]). **The principle is
honoured by rendering instead of copying**, rather than abandoned by writing a second agent.

**The opposite-discipline paragraph in that section is now the pre-task agent's own text**, delivered
by its definition rather than by a librarian's instructions, and this rule's slice names the
dispatch that reaches it.

# The count came out of that sentence rather than being renumbered — 2026-08-22

**What stood there until this date:** *"Five measured runs are on the record and every one returned
at least one finding"*. **It is replaced by the claim without the number**, and the number is not
patched to a new one.

**Renumbering was refused rather than overlooked.** Patching a drifted count into a fresh one buys
one correct reading and leaves the mechanism that produced the drift intact, and the corpus has
ruled on that twice ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[the-region-coverage-figure-is-dated-where-it-stands]], [[a-stated-count-drifts-from-the-list-it-heads]]).

**And *eight* would have been this librarian's arithmetic rather than any page's claim.**
[[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]] is the authority on the count; it
states **seven, plus the run of 2026-08-22**, and it deliberately does not add them, because what the
2026-08-22 run returned was never reported. Writing a total here would have asserted, in a rule page,
a figure the page it cites declines to state ([[an-unsourced-number-is-dropped-not-chosen]]).

**The claim itself is untouched and is what the sentence was for.** It is the counterweight to the
trigger: the ritual's only failure mode is not being read, and the evidence that reading it pays is
that no measured run has yet come back empty. **The day one does is the day the trigger is worth
re-examining**, and that sentence lives on the lesson page rather than here.

**The sentence is outside the `<!-- text -->` slice, so nothing rendered changes.** The hook message
`.claude/hooks/messages/pre-task.md` carries the slice alone, and the injector rewrites nothing here
([[what-travels-from-a-rule-page-is-a-marked-slice]], [[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]).

## The same count stood in three harness files, and the third was found by the ritual itself

**`.claude/agents/pre-task.md` and `.claude/hooks/check-the-plan.ps1` now both read *every measured
run on the record has returned at least one finding*.** They are the session's to write and not the
librarian's, and the session made the same repair in the same change
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

**The copy inside the hook was in no plan.** It was named by the `pre-task` agent checking the plan
that repaired the other two — a copy of a sentence, in a file nobody was editing, that a search for
the *page* would never have reached ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

**Three copies of one sentence is the shape this corpus keeps meeting**, and nothing mechanical
compares a rule page's prose against a harness file's: only the marked slice is compared, and this
sentence was outside it ([[no-rule-reads-a-harness-file]], [[knowing-a-rule-is-not-a-mechanism]]).
