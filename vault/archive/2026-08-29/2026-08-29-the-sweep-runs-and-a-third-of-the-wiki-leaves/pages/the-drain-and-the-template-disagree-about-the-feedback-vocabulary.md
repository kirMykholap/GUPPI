---
title: "The feedback file and the handoff template disagree about the drain's vocabulary, and the transfer that was meant to be mechanical is done by hand"
type: lesson
status: archived
authority: feedback-drain-vocabulary
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", ".superpowers/sdd/vault-feedback.md", ".claude/templates/handoff.md"]
tags: [process, harness, vault]
---

# The disagreement

**`.superpowers/sdd/vault-feedback.md` names four kinds** in its own header: `miss:`, `lint:`,
`measure:`, `process:`.

**`.claude/templates/handoff.md` names a fifth in the `Feedback to the librarian` section**: *"Its
`- harness:` lines go to `Harness` instead."*

**There is no `harness:` kind in the file that is being drained.** So the routing rule names a token
that cannot appear, and the routing it describes therefore never fires.

# What it cost, which is small and is the point

This session's harness items were written as `process:` and **routed to the `Harness` section by hand**
— which is exactly the transfer the matching vocabularies were meant to make mechanical
([[knowing-a-rule-is-not-a-mechanism]]).

**A hand transfer works until the session doing it is tired**, and the section it feeds is the work queue
the next session reads. Nothing downstream can tell a `process:` line that belongs in `Harness` from one
that does not, because the only thing that distinguished them was the token.

# Why it is filed rather than fixed

**One of the two documents is wrong and it is not a session's to choose which.** Either the feedback
file gains a `harness:` kind, or the template's sentence is corrected to say that harness items are
`process:` lines the writer routes. Both are one line, and they oblige different things afterwards.

**This is the class [[no-rule-reads-a-harness-file]] describes**: two instruction files stating one
vocabulary, with nothing comparing them. The drain exists precisely so that a miss does not depend on
anybody remembering it ([[write-the-miss-into-vault-feedback-before-the-turn-ends]]), and a vocabulary
mismatch inside the drain is the same failure one level up.

# Resolved by the owner, in favour of the file — 2026-08-19

**`harness:` is a kind of its own**, and the template's routing sentence stands
([[harness-is-a-feedback-kind-of-its-own]]). The alternative this page named — correcting the template
so harness items are `process:` lines the writer routes — was rejected, because it would fold a
**decided work item** into a kind for **findings**.

**The cost this page priced was paid once more before it closed.** The session of 2026-08-19 again
routed by hand, and the journal it produced carries a `Harness` section of thirteen lines that no
token had selected.

**And the deeper defect is untouched.** The vocabulary still lives in two files with nothing
comparing them: `.superpowers/sdd/vault-feedback.md` gained the word on 2026-08-19 and `log.md` at
the ingest of 2026-08-20, so **they disagreed for a day in the other direction**. The durable fix
this page points at — a `wiki/rules/` page with a region in each file — is designed nowhere
([[no-rule-reads-a-harness-file]]).

# The set of copies is now five, and they were aligned by hand again — 2026-08-24

**The vocabulary became four session kinds and every file naming it was edited by hand**:
`.superpowers/sdd/vault-feedback.md`, `.claude/templates/handoff.md`,
`.claude/skills/handoff/SKILL.md`, `.claude/skills/ingest/SKILL.md`, and `log.md` as the librarian's
own words ([[lint-and-process-stop-being-session-kinds-and-decision-joins]]).

**This page said two files with nothing comparing them; it is five.** The count grew by the
mechanism this page names — each new reader of the vocabulary got a copy, because there was nothing
to render one into it.

**One of the five is invisible to any tree sweep.** `.superpowers/sdd/vault-feedback.md` is
git-ignored, so the detector that would find the other four cannot see the copy that sits in the
channel for reporting blind spots.

**The durable fix is unchanged and is still designed nowhere**: a rule page and a region in each
file. **A rule page did land that day** — the one telling a session to speak its feedback — and it
renders into three of the five, but it carries the *instruction*, not the *vocabulary list*
([[speak-the-feedback-in-the-turn-and-the-hook-files-it]]).
