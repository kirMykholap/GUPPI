---
title: "A style rule for the prose a session writes, ratified before anything carried it"
type: proposal
status: archived
authority: session-writing-style
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
decided_by: [[the-style-rule-is-ratified-and-its-text-recovered-from-the-approved-plan]]
tags: [vault, process, harness]
---

# What it is

**A rule, five lines long, governing how a session writes** — the prose in chat, in a plan, and in
this store. The owner opened 2026-08-23 by saying he cannot read what this project writes, and the
rule is the answer he asked for **first**, ahead of everything else that session did.

**owner selected: мой вариант** — the five lines as the session revised his own first draft,
chosen against that draft. A selection rather than an utterance: the wording is the session's and
the choice is his ([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**What the revision changed, which is all that survives of the content:**

- a duplicated clause about sources was removed;
- *KISS* was given a concrete form rather than left as a slogan;
- a line was added requiring **the answer in the first sentence**.

# The text is not in this repository, and that is the finding

**Nothing in `raw/`, in the vault, in `.superpowers/sdd/` or in the tree holds the five lines.**
The journal records that they exist, that they were ratified twice, and what the revision did to
them — and not one of the five. **They survive only in the chat log of 2026-08-23**, which nothing
here reads.

**That is the exact failure the closing ritual exists to prevent**, met by the artefact that
performs it: a design ratified in conversation and not written down is lost when the session ends,
and the journal is the only channel that survives it
([[journal-vault-brief-each-artefact-has-one-owner]],
[[a-question-asked-is-not-a-question-answered]]). Recording *that* it is lost is the most this page
can do; recovering it means asking him again.

# What it would take

**It is a `wiki/rules/` page**, by that folder's own admission test: a rule the harness renders into
the file it governs rather than a reader remembers
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]],
[[what-travels-from-a-rule-page-is-a-marked-slice]]). Its destination is the repository's
`CLAUDE.md`, or the vault's, or both — `governs:` takes a list
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

**Three steps and none of them are large:** recover the five lines from him, write the rule page
with its slice, mark the region in the destination and run the injector
([[a-region-is-a-paired-comment-named-for-a-rule]]).

# What is open

- **Whether it reaches the corpus as well as the chat.** A style rule that governs `CLAUDE.md`
  reaches every session; whether it also governs what the librarian writes into `wiki/` is a
  different question and was not asked. **The complaint that produced it was about prose he reads**,
  and most of `wiki/` is prose he does not.
- **Whether anything checks it.** Prose style is a judgement, so this is one of the rules that may
  end up with a page saying why no instrument can have it
  ([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).
- **Ratified twice and unwritten is itself the risk.** A second ratification did not make it
  happen, and a third will not either
  ([[a-conversation-the-owner-scheduled-is-displaced-by-the-work-beside-it]]).

# Consequence of not building it

**Every future session reads the same prose he opened this one by saying he cannot read**, and the
one thing he asked for first stays the one thing that did not land.

# It was built the same day, and the section above is wrong about one thing — 2026-08-23

**The rule exists.** [[write-plainly-name-the-source-and-say-what-is-not-done]] carries the five
lines in its `<!-- text -->` slice and renders them into the repository's `CLAUDE.md`;
[[the-style-rule-is-ratified-and-its-text-recovered-from-the-approved-plan]] is the decision behind
it. The owner ordered it written today rather than next session.

**The section *The text is not in this repository, and that is the finding* is wrong in its
conclusion and right in its evidence, and it is kept whole.** The evidence stands: nothing in
`raw/`, in the vault, in `.superpowers/sdd/` or in the tree held the five lines, and `grep -ril KISS`
over the repository matched a journal and nothing else. **The conclusion — that they survive only in
the chat log and that recovering them means asking him again — was false when it was written.** They
were in the plan he approved when S3 was opened, which lives outside the repository by the language
rule that says so ([[english-in-the-repository-russian-with-the-owner]],
[[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]).

**So the finding survives in a sharper form**: a repository-wide grep is not a search of everything
this project produces, and the artefact the owner reads in order to approve it is the one document
guaranteed to be outside the net.

**The title was corrected in place and the filename was not touched.** It read *ratified and still
unwritten* until this section was appended. A title correction moves no address and is not a
supersession, which is the store's own rule; the filename is the address every link here resolves
to.

**Two of the three open questions above are still open** — whether the rule reaches `wiki/` as well
as `CLAUDE.md`, and whether anything can check it — and both moved onto the rule page and the
decision, where a reader who lands on the live pages will meet them
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).

**This page is `status: implemented` and has not moved to `archive/`.** It takes the mark and waits
here until it is moved, which is what the mark is for; both live pages name it, so the precondition
`scripts/vault-archive.sh` enforces is already satisfied. The move was left undone deliberately:
`archive/` is organised as one folder per session and this session has none yet — it is created at
`/ingest` — so archiving now would file the page under the previous session's name.

# What the retro settled about it, and why it is still here — 2026-08-23, in the second session of that day

**The scope question this page raised is answered: the rule does not govern `wiki/`.** It governs
what a session writes for the owner — chat and the plan he approves — and the librarian works to
this store's own rules ([[the-style-rules-watcher-is-the-owner-and-it-governs-chat-alone]]).

**Its watcher is the owner**, so it joins the rules with no mechanical instrument and does not wait
for one ([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).

**This page carries `status: implemented` — the first use of the value, minted the day before.** It
has not moved to `archive/`, and that is deliberate rather than owed: the mark opens a state, and
the move happens once a live page names it and there is a session folder to move it into
([[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]],
[[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).
