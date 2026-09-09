---
title: "The paragraph was deleted on purpose, so the question is no longer what catches a loss but what tells a loss from a deletion"
type: decision
status: current
authority: claude-md-loss-vs-deletion
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", "archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", "CLAUDE.md"]
tags: [vault, process]
---

# What the owner said, and what it costs the sprint

**The owner, 2026-08-15: he removed the paragraph by hand.** The ingest of 2026-08-14 had read the
disappearance of the language rule's boundary — *what predates 2026-08-05 stays Russian, do not
mass-translate, do not rename existing tests* — out of the shortened `CLAUDE.md` as a **loss**, and
revived it as a page ([[the-language-rule-applies-only-to-new-work]], since retired into `archive/`
and superseded by [[english-is-the-rule-and-the-russian-past-is-deferred]]).

It was not a loss. It was an edit, and the vault reconstructed a rule its author had deliberately
withdrawn — which is the same failure class as compiling an intention as testimony
([[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]), arriving from the other
direction.

**Rejected: leaving acceptance criterion 4 of S1 as written.** It asks for *"a check that fires
when a cut of `CLAUDE.md` drops something no page holds"*. That question is now known to be the
wrong one, or at least only half of it:

| the question the criterion asks | the question this decision adds |
|---|---|
| what catches a rule that was **lost** in a cut? | what distinguishes a **loss** from a **deletion**? |

A check that fires on every removed paragraph reports the owner's own edits back to him, and an
alarm that fires on intended behaviour is the failure this project has written down three times
([[vault-scripts]], [[line-endings-make-git-status-overstate-what-changed]]).

**Whether criterion 4 is rewritten, and into what, is the owner's** — a sprint's goal is changed by
him and recorded in `sprint.md`, never adjusted by the librarian
([[a-sprint-closes-on-its-goal]]).

## Why the existing verdict cannot answer either question

`elsewhere:CLAUDE.md` is a legal coverage verdict: it says *this unit's content lives in a file
outside the vault*. It asserts nothing about that file continuing to say it, and no script here
looks at `CLAUDE.md` for content at all — rule 15 checks only that the page names it cites exist
([[vault-scripts]], [[the-verdict-is-the-write]]). So every such verdict is a claim with no
custodian, and both questions above land on the same gap.

**How many there are — measured, because the journal's figure and the tree disagree.** The journal
of 2026-08-15 says *"Nine such verdicts exist"*. Counted over all six sidecars at `14d3d51`:

```
grep -h "elsewhere:" job_hunt_ai_vault/raw/*/*.coverage.tsv | grep -ci claude     # 18
```

- **7 point at the repository's `CLAUDE.md`** — six written `elsewhere:CLAUDE.md`, all in
  `2026-08-12-handoff-before-the-vault.coverage.tsv`, and one written
  `elsewhere:the repository's CLAUDE.md`;
- **11 point at the vault's own `CLAUDE.md`**, which is the schema file and a different custodian
  question again — the schema file is not a wiki page and nothing compares it against the decisions
  it states.

Seven, not nine, for the file the criterion is about. The journal is left as written, because
`raw/` is immutable and what a session believed is data
([[the-handoff-template-maps-onto-the-categories]]); this is the correction beside it, and it is
one more instance of [[a-stated-count-drifts-from-the-list-it-heads]].

## What it obliges

**A cut of either `CLAUDE.md` is still an event the vault must be told about.** Nothing changes
about [[the-verdict-is-the-write]]'s obligation to re-read every `elsewhere:` verdict when the file
it names is edited. What changes is the outcome of that re-read: *the owner meant it* is now a
legal answer, and the only party who can give it is him.
