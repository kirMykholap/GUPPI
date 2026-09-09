---
title: "What the gate reads as its own input is the session's to write, and no divergence is recorded for it"
type: decision
status: current
authority: vault-schema-write-permission
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "job_hunt_ai_vault/CLAUDE.md", "job_hunt_ai_vault/wiki/decisions/_schema.yaml"]
tags: [vault, agents, process]
---

# The clause, taken 2026-08-19

> **owner: what the gate reads as its own input is the session's to write** — `job_hunt_ai_vault/CLAUDE.md`
> and every `wiki/*/_schema.yaml`. The owner reads the diff before the commit, the librarian writes
> neither, and **no divergence is recorded for either**.

It is written into `job_hunt_ai_vault/CLAUDE.md` under a new `## Who writes what`, by the authority
it itself grants. The one-writer rule over `wiki/` and the registers is untouched
([[the-librarian-writes-unattended]], [[the-one-writer-rule-covers-the-registers-too]]).

**Rejected: the librarian's, like the registers.** And **rejected: the owner's alone.**

**Why.** This file is the librarian's own instructions and the schemas constrain what it may write,
so **a librarian writing them is the one arrangement in which a change has no reader but its
author.** What made the two hand-edits of 2026-08-19 safe was never the recording — it was that no
librarian was running and that the change was a `git diff` the owner read
([[parallel-librarians-break-the-one-writer-property]]). The clause states those two properties
instead of the paperwork.

# The half that was a widening, and it was asked separately

The brief asked for a clause about one file. **The answer covers two**, because a `_schema.yaml` is
the same kind of object: an input the gate reads, constraining what the librarian may write. That
widening was **put to the owner separately before it was taken**, rather than folded into the
narrower question ([[narrowing-a-scope-notifies-and-widening-it-asks]]).

**A `_schema.yaml` is still not a place to reason from the corpus.** Its header rule stands: a field
moves from `optional` to `required` when a decision says so, and the decision names the page it is
written on ([[the-per-folder-frontmatter-schema]],
[[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]]). Being the
session's to edit changes who holds the pen, not what may be written.

# What it obliges

- **The two divergences already on the record stand as history and are not retracted** —
  [[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]] and
  [[hand-edits-of-the-wiki-are-a-recorded-divergence]]. Both carry a note that the clause now exists;
  neither is rewritten, because what they record is what happened before it did.
- **The gap the brief raised twice is closed.** A session editing either file is doing what the rule
  says, and nothing is filed against it.
- **The owner reading the diff is now a property the clause names**, which means it can be diverged
  from — and it was, on this clause's own first application
  ([[the-gate-input-clause-was-not-exercised-on-its-first-application]]).

# The `authority:` slug arrived here on 2026-08-19, on the owner's ruling

**`authority: vault-schema-write-permission` moved onto this page**, off
[[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]], which
answers that question with *still owed*. Ruled 2026-08-19, on the brief's alarm.

**This page held `gate-input-write-permission` until then**, which described the clause rather than
the question a reader arrives with. The question is *who may write the vault's schema*, and this is
where it is answered.

# The owner stated the division wider than the question — 2026-08-24

> **owner:** «Библиотекарь отвечает за документы, сессия правит harness, хуки, скрипты, код и
> прочее.»

**He was asked about one file and answered about the boundary.** The question was whether editing
`wiki/proposals/_schema.yaml` was a divergence, while a `PreToolUse:Edit` hook warned about the
vault's single writer. The answer is the general rule: **the librarian owns the documents; the
session owns the harness, the hooks, the scripts and the code.**

**Nothing above is narrowed by this and the clause of 2026-08-19 is unchanged.** What is new is that
the same boundary now has a statement that does not depend on the two file classes this page
enumerates.

**And the hook's net is wider than the rule**, which is recorded as a defect rather than fixed here
([[the-harness-defects-found-this-session-enter-the-sprint-one-line-each]]).
