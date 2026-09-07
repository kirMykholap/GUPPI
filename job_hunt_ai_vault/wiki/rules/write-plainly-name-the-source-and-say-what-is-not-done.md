---
title: "Write plainly, name the source, answer first, and say what is not done"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "CLAUDE.md"]
decided_by: [[the-style-rule-is-ratified-and-its-text-recovered-from-the-approved-plan]]
tags: [process, harness]
---

# What travels

<!-- text -->
- Keep the facts and remove the sales pitch.
- Name a real source or remove the claim.
- Plain language by default, never on request: short sentences, active voice, a common word over a
  term.
- Give the answer in the first sentence, then the list, and keep the reasoning below it skippable.
  No "if X then Y".
- One question per message.
- Say what is done and what is not done. Never leave the not-done implied.
<!-- /text -->

**That text is the ratified one and it is not this page's to improve.** It was recovered verbatim
from the plan the owner approved when S3 was opened, at
`C:\Users\kir\.claude\plans\agile-percolating-wall.md`, lines 167 to 172, under phase A1. Nothing in
it was reordered, rewritten or expanded — *KISS* in particular stays the word he ratified rather than
the sentence a later reader would have preferred
([[the-style-rule-is-ratified-and-its-text-recovered-from-the-approved-plan]]).

**Amended 2026-08-25, and the paragraph above is a statement about 2026-08-23.** The slice no
longer holds that text — the owner amended it, in his own words, and the amendment is at the foot
of this page ([[the-style-rules-slice-is-amended-rather-than-superseded]]).

**Everything below this line stays here** ([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it is a rule and not advice

**The owner opened 2026-08-23 by saying he cannot read what this project writes**, and this was the
first thing he asked for that day. It is about the prose he reads: in chat, in a plan he must
approve, and in the answers this store hands back.

**Style is chosen at the first sentence, and asked afterwards the paragraph is already written.**
That is the admission test for the rules that reach the repository's `CLAUDE.md` — obeying them late
is the same as not obeying them at all ([[claude-md-is-a-map-and-four-rules]]). A session that has
to go looking for a style rule writes in whatever register it started in, and the reader who pays for
it is the one who cannot ask.

# What each line is doing there, and what the ratification changed

**The wording is the session's and the ruling is his.** It arrived as `owner selected: мой вариант`,
chosen against his own first draft — a menu selection, which is neither a quotation nor a paraphrase
and is never signed `owner:`
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**Three things separate the ratified text from his draft**, and they are the whole of what the
revision did: a duplicated clause about sources was removed, *KISS* was given a concrete form rather
than left as a slogan, and the line requiring **the answer in the first sentence** was added.

**The last line is the one this store keeps breaking.** *Say what is done and what is not done* is
the same obligation the handoff template carries as its `Not done` section and the librarian's
answers carry as `Not in the vault`: an omission reads exactly like an absence, and a reader cannot
tell a thing that was not done from a thing that was not mentioned.

# Where it renders

`governs: CLAUDE.md` — the repository's file, a path from the repository root and resolved against
nothing else ([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment
named for this page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]), under a heading of
its own that follows `## Language`: **which language to write in, then how to write it.** The
heading is prose the file owns and stays outside the region.

**The blank line after the slice is written by the injector and is not typed onto this page**
([[the-injector-writes-the-separator-inside-the-region]]).

# What is open, and it is named rather than answered

- **Whether it governs `wiki/` as well.** The destination is the repository's `CLAUDE.md` and
  nothing else. The complaint that produced the rule was about prose the owner reads, and most of
  this store is prose he does not; whether the librarian's own writing falls under it was never put
  to him ([[a-style-rule-for-the-prose-a-session-writes]]).
- **Whether anything can check it.** Nothing does today. Every rule here owes a mechanical
  instrument or a page saying why it cannot have one, which is acceptance criterion 1 of S3
  ([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).

# Why no instrument holds it yet

**Prose style is a judgement, and it is the same class the language rule sits in**: no linter in this
project reads natural language, and the mechanical proxies available all fire on correct text. A
sentence-length threshold would redden a correct long sentence; a grep for adjectives would redden a
description. **A verdict that fires when nothing is wrong is one a reader learns not to read**
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

**The nearest honest instrument is a human one**, and it already exists: the owner reads the plan and
the chat, which is how the complaint that produced this rule arrived in the first place. Whether that
counts as the instrument the criterion asks for is his call, not this page's.

# What it cost to get here

**It was ratified twice and written nowhere**, and each ratification produced no artefact any session
reads. The store then recorded the loss correctly and drew the wrong conclusion from it: a
repository-wide `grep -ril KISS` matched a journal and nothing else, and the plan the owner approves
lives outside the repository by the language rule that says so
([[english-in-the-repository-russian-with-the-owner]],
[[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]). Asking him a third time was the
recommended repair and was refused
([[the-style-rule-is-ratified-and-its-text-recovered-from-the-approved-plan]]).

# The amendment of 2026-08-25, and it is an amendment rather than a supersession

> **owner:** «это поправка»

**The claim is unchanged — write so the owner can read it — so no successor is written and this page
does not move to `archive/`** ([[the-style-rules-slice-is-amended-rather-than-superseded]]).

**What the slice said until this date**, kept here because nothing on a page is deleted:

```
- Keep the facts and remove the sales pitch.
- Name a real source or remove the claim.
- KISS: short sentences, active voice, a common word over a term.
- Give the answer in the first sentence, then the list. No "if X then Y".
- Say what is done and what is not done. Never leave the not-done implied.
```

**What changed, and it is three things.** The plain-language line absorbs the line that said *KISS*
and carries the words he asked for — «Простой язык по умолчанию. Не по запросу». The answer-first line
gains that the reasoning below it must be skippable. *One question per message* is added.

> **owner:** «Главное - добавить туда "Простой язык по умолчанию. Не по запросу". Он пока что хорошо
> себя показывал всегда»

**A line the session proposed was dropped by the session**, and the narrowing was announced rather than
done quietly: no page slugs in chat. **owner:** «не стоит так переживать за slug в чате - это меньшая
из проблем.» ([[narrowing-a-scope-notifies-and-widening-it-asks]]).

**Two of the things he had to ask for were already here**, which is why this is a rewording rather than
an extension: the failure was compliance, not coverage.

**The word *KISS* leaves, and it was the one word the ratification of 2026-08-23 deliberately kept.**
That is recorded rather than glossed: what replaced it is his own instruction, given on this date.
