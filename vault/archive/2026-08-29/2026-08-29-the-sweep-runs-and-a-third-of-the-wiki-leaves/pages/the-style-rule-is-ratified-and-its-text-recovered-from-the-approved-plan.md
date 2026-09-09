---
title: "The style rule is ratified, and its text was recovered from the plan the owner approved"
type: decision
status: archived
authority: style-rule-ratification
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "[[a-style-rule-for-the-prose-a-session-writes]]", "CLAUDE.md"]
tags: [process, harness, vault]
---

# The ruling, 2026-08-23

**The style rule lands today.** The owner was asked in a retro whether it lands this session or the
next, and answered `сегодня`. That is the ruling this page records, and it is the only part of the
chain that is certain, dated and citable from this session.

**Its text was ratified earlier and no artefact carried it.** The journal of the first session of
2026-08-23 records the ratification as a menu selection:

- `owner selected: мой вариант` — the five lines as that session revised his own first draft,
  **chosen against that draft**. The revision removed a duplicated clause about sources, gave *KISS*
  a concrete form, and added *the answer in the first sentence*.

**Nothing here is written as a quotation, and that is a rule rather than a caution.** A ruling taken
from a rendered menu is neither a quotation nor a paraphrase: the label is carried verbatim, without
quotation marks, and it is never signed `owner:`
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]],
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]). **His own words about the five
lines exist nowhere in this store**, so no `owner:` block is written on this page and none was
invented for it.

**The other ratification is an approval rather than an utterance.** The five lines stood under phase
A1 of the plan he approved when S3 was opened, and approving a plan is a decision — the ruling is
his, the wording is the session's, and it is signed by nobody. **That is the same shape S3's own
goal and acceptance criteria carry**, stated at the opening of `sprint.md` for the same reason.

# What was ratified, and why it is not copied onto this page

**The text is the rule, and it lives on
[[write-plainly-name-the-source-and-say-what-is-not-done]]**, inside the `<!-- text -->` slice the
injector renders into the repository's `CLAUDE.md`.

**A second copy here would be checked by nothing.** The injector compares the slice against the
region byte for byte on every run; prose on a decision page is compared against nothing at all, and
this corpus has already been bitten by exactly that — [[english-is-the-rule-and-the-russian-past-is-deferred]]
restates the language rule's list and had to be corrected on its own when a word was struck from the
slice ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**So the five lines travel from the plan to the rule page and to nowhere else**, and they travel
verbatim: they are what was ratified, and improving them here would put a third wording in play.

# Where the text was, and why it was believed lost

**The alarm was raised and the alarm was wrong.** The brief of 2026-08-23 reported that
`grep -ril KISS` over the whole repository matches a journal and nothing else, that *the five lines
survive only in the chat log*, and that recovering them meant asking the owner again — which is what
[[a-style-rule-for-the-prose-a-session-writes]] records as its central finding.

**The search was scoped to the repository, and the text was never in the repository.** The plan the
owner reads in order to approve it is written for him and lives outside the tree, by the language
rule that says so ([[english-in-the-repository-russian-with-the-owner]],
[[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]). It is at
`C:\Users\kir\.claude\plans\agile-percolating-wall.md`, lines 167 to 172, under phase A1 — the same
plan whose approval opened S3.

**That path is deliberately not in `sources:`.** Rule 2 of `bash scripts/vault-check.sh` tests every
non-wikilink, non-URL entry of that field with `[ -e ]` and reddens the gate when it resolves to
nothing. The file is outside version control and outside this repository, so a citation there would
be a path this store cannot keep true, and the repair when it rotted would be deleting the one
citation this page exists to make. It is in the body instead, where a reader can follow it and no
check can be falsified by the owner tidying his plans directory.

# What it was chosen against

**Asking him for the five lines a third time**, which the brief recommended and which was the
obvious move. It was refused because it would have **re-derived text that already existed**: a third
wording, produced by a third session, presented for a third ratification, with the ratified one
sitting unread on disk the whole time. What he ratified is not a topic to be re-elicited — it is a
document.

# The finding, and it is the reusable half

**A rule ratified in conversation and not written into a file does not exist.** This one demonstrated
it twice: it was ratified, it changed nothing, it was ratified again, and it still changed nothing —
because on neither occasion did the ratification produce an artefact any session reads. The closing
ritual exists to prevent precisely that, and here it recorded the loss faithfully without preventing
it ([[journal-vault-brief-each-artefact-has-one-owner]],
[[a-question-asked-is-not-a-question-answered]]).

**And the second half is about the search rather than the writing: a grep scoped to the repository
cannot see the artefact the owner approves.** The alarm that the text was lost was itself wrong, and
nothing mechanical could have said so — the file it was in is not one this project owns. Where a
thing is written decides whether it can be found again, and *the whole repository* is a smaller net
than it sounds like.

# What this obliges

**The five lines bind the prose a session writes**, delivered into the repository's `CLAUDE.md` as a
rendered region, so every session reads them whether or not it went looking
([[what-travels-from-a-rule-page-is-a-marked-slice]],
[[a-region-is-a-paired-comment-named-for-a-rule]]).

**It owes a mechanical instrument, and does not have one.** Every rule in `wiki/rules/` owes one or a
page saying why it cannot have one, which is acceptance criterion 1 of S3
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]). Prose style is a judgement and no linter
here reads natural language, so this rule joins the ones whose instrument is open. **Nothing on this
page settles that**, and the rule page names it as owed rather than answered.

# What is not decided here

- **Whether it governs `wiki/` as well.** `governs: CLAUDE.md` names the repository's file and
  nothing else. Whether the librarian's own prose falls under it was raised by
  [[a-style-rule-for-the-prose-a-session-writes]] and was never put to him.
- **Whether anything checks it.** Open, above.
- **A citation to this session's journal is owed and deliberately unwritten.** The document in which
  he answered `сегодня` does not exist yet — it is written at `/handoff` and compiled at `/ingest` —
  and a `sources:` path to a file that is not there reads as provenance and is not. The next ingest
  owes it, the same way [[the-ask-before-weakening-rule-is-ratified-after-being-enforced-without-a-decision]]
  was owed one.
