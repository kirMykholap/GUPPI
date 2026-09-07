---
title: "A wrong answer from the vault is written into the feedback file in the turn it is noticed"
type: rule
status: deprecated
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "[[feedback-is-recorded-in-the-turn-it-is-noticed]]", "[[vault-feedback-file]]", "[[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]"]
decided_by: [[feedback-is-recorded-in-the-turn-it-is-noticed]]
superseded_by: [[speak-the-feedback-in-the-turn-and-the-hook-files-it]]
tags: [harness, vault, process]
---

# What travels

<!-- text -->
**When the vault answers wrong, write one line into** `.superpowers/sdd/vault-feedback.md` **in that
same turn** — never carry it in your head to the end of the session. `/handoff` drains that file
into `Feedback to the librarian` and `/ingest` files it as a `- miss:`, so the loop closes on its own. Recording is
not arguing: it costs a line, and whether the corpus changes is the owner's call, later.
<!-- /text -->

**That is the feedback paragraph of the repository's `CLAUDE.md`, to the byte** — cut out at
`e478c19` by line number and diffed against the slice above rather than read against it. The diff is
empty.

**Its third line runs to 115 characters and is carried unwrapped on purpose.** It reached that
length at `074e7a8`, when `section 7` was replaced in place by `` `Feedback to the librarian` `` and
nobody rewrapped ([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]). Rewrapping it
here would be a change nobody decided, made invisible by a migration that is supposed to be a move —
the same reason an ordinal was stripped from a rule and nothing else was touched
([[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]]). Rewrap it in the page and the file
together, or not at all; rewrapping one end is what rule 12 exists to catch.

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

**The moment this rule addresses is the moment the vault failed, and nobody plans for that moment.**
A session asks the store something, gets a bad answer, works around it and moves on; the rule has to
already be in hand, because the thing that would send a reader looking for it is exactly the thing
that just went wrong.

**And what is lost by waiting is specific.** By handoff time the question, the grep that returned
nothing and the page that should have carried it are gone. What arrives at handoff instead is a mood
about the vault ([[feedback-is-recorded-in-the-turn-it-is-noticed]], [[vault-feedback-file]]).

# The clause that makes the channel usable

*Recording is not arguing: it costs a line, and whether the corpus changes is the owner's call,
later.* **That sentence is load-bearing and belongs inside the slice.** A channel that requires a
case to be made is a channel nobody uses at 2 a.m., and the decision behind this rule says so in
those words.

It is also what keeps the observation honest. The reporter is the party that was let down, writing
in the moment it happened; the librarian only files. Before this, the misses in `log.md` were written
**by the librarian about itself** at ingest time — the party being reviewed reporting the review
([[journal-vault-brief-each-artefact-has-one-owner]]).

# Why the rule names one kind and the file takes more

The text names `- miss:` because a miss is what this rule is about. **The file carries a vocabulary
of four**, defined in its own header rather than here:

| kind | what it reports |
|---|---|
| `miss:` | the vault failed to supply something, and where that surfaced |
| `lint:` | a defect in the corpus — a stale claim, a contradiction, a copied list |
| `measure:` | a number, with what it does and does not mean |
| `process:` | the ritual or the harness failed, independently of what the corpus holds |

`process:` was adopted on 2026-08-17, **after two lines had already been filed under it by a session
that had no such kind** ([[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]). The librarian transferred them under
the kind they were written with and raised the vocabulary as an alarm rather than reclassifying them
— which is the same discipline this rule asks of the writer, applied one hop later.

The `measure:` kind is not a convenience either: **a subagent cannot report its own token cost**, so
that figure reaches `log.md` by no other route ([[a-subagent-cannot-report-its-own-cost]]).

# Its failure mode is silence, and that is why it is delivered

**Nothing checks that the file was written to, and nothing checks that it was drained.** A session
that never opens it produces a handoff whose feedback section reads *none* and looks identical to a
session where the vault answered everything ([[vault-feedback-file]]).

That is not hypothetical at any scale. **Six lines sat undrained**, written by a session that wrote
no journal at all, and they were carried forward verbatim by the next one and marked as inherited.
And the file's own header went on saying `section 7` after the handoff's sections lost their
numbers, because the sweep that found every other copy of that mapping searched the tree and **this
file is git-ignored** — the one detector that worked had a blind spot exactly where the channel for
reporting blind spots lives.

**A rule whose failure mode is silence has to arrive before the work**, which is the property the
injector preserves and the reason this text is rendered rather than cited
([[a-region-is-a-paired-comment-named-for-a-rule]]).

# What the lines are evidence for

They are **the only test data this store has**. Whether this vault ever gets a vector index is
supposed to be decided by them rather than by argument ([[vectors-are-deferred-not-rejected]]), and
the store is verified by use rather than by reading because the owner has said that reading an
English corpus is not a check he can perform ([[feedback-is-recorded-in-the-turn-it-is-noticed]]).

So a line skipped is not a courtesy withheld. It is a data point deleted from the only experiment
running here.

# The duplication this rule is about to remove

**The decision behind it obliges three files to carry it** — the repository's `CLAUDE.md`,
`/vault-ask` and `/handoff` — because a rule about noticing has to be where the noticing happens
([[feedback-is-recorded-in-the-turn-it-is-noticed]]). Three copies of one rule in three files with
different owners is precisely what marked regions exist for
([[marked-regions-and-the-prose-outside-them]], [[the-harness-is-compiled-not-maintained]]).

**Only this destination is claimed by this page.** `governs:` names the one file a rule's text is
rendered into ([[governs-is-a-path-from-the-repository-root]]), so the other two copies remain
hand-written and can still drift. That is a known gap and not an oversight: whether one rule may
render into more than one file has not been decided, and it is not the librarian's to decide.

# Why no test holds it

**The trigger is a judgement made inside a turn** — *this answer was wrong* — and no artefact records
that judgement unless the rule is obeyed. A check would have to know what the session asked and what
it should have got, which is the answer the check does not have. Imperative, unenforceable, admitted
([[rules-becomes-a-type-of-its-own]]).

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else. The text lands
in a paired comment named for this page's slug, in a file on its way to being a dispatch table
([[the-repository-claude-md-becomes-a-dispatch-table]]).

**The page and its region belong in one change, and this page arrived first.** Until the session
marks the region and runs the injector, rule 12 reports this rule as governing a file that carries no
region for it ([[a-governed-file-with-no-region-is-an-advisory]]). If the rule is ever replaced, the
successor renders and this page does not ([[a-deprecated-rule-does-not-render]]).

# The instruction, the decision and the file are different pages

[[feedback-is-recorded-in-the-turn-it-is-noticed]] answers `authority: fidelity-verification`;
[[vault-feedback-file]] answers `authority: feedback-channel`; [[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]
answers `authority: feedback-kinds`. This page carries only the instruction and carries `governs:` in
place of an `authority:`, so it does not read as a rival answer to any of them
([[rules-becomes-a-type-of-its-own]]).

# Retired 2026-08-24, and its claim was replaced rather than corrected

**A session no longer writes the file.** It prints a fenced `VAULT-FEEDBACK` block in its own reply
and `.claude/hooks/catch-the-feedback.ps1` files it, so the verb and the object of the sentence in
the slice above are both wrong from this date
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]]).

**The successor is [[speak-the-feedback-in-the-turn-and-the-hook-files-it]]**, which governs three
files rather than one and carries four kinds rather than naming one. This page renders nothing from
here on, which is the property that lets its region be renamed in `CLAUDE.md` without two rules
writing into one place ([[a-deprecated-rule-does-not-render]]).

**The gap this page named as known is closed by the successor.** It said *only this destination is
claimed by this page*, and that the other two copies remained hand-written and could still drift;
the successor names all three in `governs:`, so the drift has an instrument rather than a note.

**Its table of four kinds went false on the same day** — `lint:` and `process:` stopped being
session kinds ([[lint-and-process-stop-being-session-kinds-and-decision-joins]]). The table is left
as written: it is what the vocabulary was between 2026-08-17 and 2026-08-24, and `raw/` carries
journals written in those words.
