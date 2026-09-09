---
title: "A genuine owner quote was flagged by a scanner that cannot see the dispatch brief"
type: lesson
status: archived
authority: quote-scan-false-positive
basis: code
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", ".claude/agents/vault-librarian.md"]
tags: [agents, vault, process]
---

# What happened, 2026-08-23

**A security scanner flagged a subagent's result as a fabricated owner quotation.** The block was
genuine: it was checked character by character against what the owner typed, and it matched.

**The scanner was not wrong about what it could see.** It reads the subagent's transcript, and in
that transcript **no user turn exists** — the quotation reached the agent through the dispatch
brief, which is how this ritual is designed to work ([[vault-librarian]]).

# Why this false positive is structural rather than a one-off

**Every quotation a librarian writes arrives the same way.** The agent's context is empty of the
session; the owner's words come in as text inside its instructions
([[vault-librarian]]). So *a quotation with no user turn behind it* describes every legitimate
owner block this store has ever compiled, and a detector keyed on that property flags all of them.

**The detector's question and the real question are different.** *Did a user say this in this
transcript* is answerable and useless here. *Do these characters match what he typed* is the one
that matters, and nothing in the transcript can answer it.

# The check was worth running anyway, and that is the load-bearing half

**A fabricated quote signed with his name is this project's worst failure mode.** It has already
happened once: a paraphrase signed `owner:` stood for three days and later sessions reasoned from
it as his word ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

**So the response to the flag was to verify, not to dismiss.** *I am confident* is not a
verification; comparing the characters is. The verification is cheap and the failure it guards
against is not recoverable, which is the whole argument for doing it every time the question is
raised
([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]],
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

# What it obliges

**A flag of this shape is answered with the comparison and the comparison is recorded**, so the next
session meets the finding rather than the alarm. Nothing about the dispatch changes: routing his
words through a brief is what lets the librarian quote him at all.
