---
title: "Journal, vault, brief — each artefact has exactly one owner, and the brief is never a source"
type: concept
status: current
authority: vault-artefacts
basis: human
sprint: S0
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md"]
tags: [vault, process]
---

# Three artefacts, three owners

| Artefact | Written by | Rule it lives under |
|---|---|---|
| **journal** — `raw/handoffs/<date>-<slug>.md`, from [[the-handoff-template-maps-onto-the-categories]] | the session, at its end | appended to; **never edited after the fact** |
| **vault** — `wiki/` | the librarian, at ingest | nothing is deleted; a replaced page is deprecated |
| **brief** — `brief.md` | the librarian, at the end of an ingest | **derived. Never a source** |

Each artefact has exactly one writer, and knowing which one you are looking at is what tells you
how much to trust it.

*(The title read "Journal, vault, brief — three artefacts with three owners, and the brief is never
a source" until 2026-08-18. It named the artefacts and counted them in the same line, and the
sentence above carries what the number was actually claiming: the mapping is one-to-one. The
`quantity:` line it stood on argued — *the artefacts counted are named in the title itself* — which
is true, and is the reason striking the number costs the title nothing. It went with the field when
the field was rejected and the rule was made unconditional in both halves ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[a-title-names-what-is-counted-instead-of-counting-it]]). **A fourth thing with a fourth owner is
already named below**, which is the argument against the count standing on its own. The
**filename** still counts, twice, and waits for its rename, which moves an address
([[the-title-rule-extends-to-filenames]], [[a-page-rename-is-sed-and-verify]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

**The owner's method note asked for three layers and they are not these three.** His are `raw/`,
`wiki/` and `CLAUDE.md` — source, compilation, constitution — which is a description of the *store*
([[the-owners-method-note-and-what-was-built-from-it]]). The table above is a description of the
*loop*, and the artefact it turns on, `brief.md`, appears in neither of his notes. The constitution
is here too, as a fourth thing with a fourth owner: it is not written at ingest and it is not
derived ([[claude-md-is-a-map-and-four-rules]]).

## The journal is testimony, the vault is compiled knowledge

The journal records what the session **believed at the time**. If the librarian disagrees with it,
the disagreement goes on a wiki page or into `log.md` — never back into the journal. Otherwise we
lose the ability to find out where a session was wrong, which is most of what
[[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]] was reconstructed from.

## The brief is derived, and that is a hard rule

If the brief is wrong, the fix goes into the vault or into the ingest skill. **A hand-edited brief
that survives a session is immediate divergence** — the same failure as a second copy of a rule.

Its shape is fixed, and **since 2026-08-14 it is one section shorter**: alarms (only when one
holds), sprint, state, what must not be broken, hooks for this work. The active-tasks section was
**removed rather than kept empty** — [[the-brief-has-no-active-tasks-section]], which supersedes
[[active-tasks-stay-empty-until-a-tracker-exists]]. Its **size** is the alarm that bounds a sprint
([[the-growth-signal-is-the-brief]]).

## Ingest sits between the journal and the brief, and is not optional

Without it, knowledge would travel journal → brief and settle only in the derived artefact; within
three sessions briefs would be paraphrasing briefs. What ingest is, mechanically, is
[[ingest-is-units-and-verdicts]]; who performs it is [[one-librarian-behind-every-caller]].

## The loop, and the seams are where it broke

The full cycle is **journal → ingest → brief → hook → next session**, and the session that finished
building it found that **its seams failed, not its pieces**. Every station worked; the joins
between them were assumed. Three things now close them, and each is a different join:

| Seam | What was wrong | What closes it |
|---|---|---|
| session → journal | the rule that a session *ends* by writing one existed nowhere | the repository's `CLAUDE.md`: **"a session ends with `/handoff`, then `/ingest`"** |
| ingest → brief | a brief overtaken by six commits read exactly like a fresh one | [[the-brief-is-stamped-with-its-commit]] |
| brief → next session | nothing delivered it, and nothing said it was old | [[session-hooks]], which reports a stale stamp and a journal newer than the brief as **two different failures** |

Both of the first two were found by the whole-branch review and by nothing before it, because a
per-task review reads a part ([[how-a-slice-is-executed]]).

The split into three is itself the answer to a diagnosis with a date and an author:
[[the-handoff-splits-into-a-handoff-and-a-knowledge-base]]. It also supplies the journal's boundary
test — **if it does not change between sessions, it does not belong in the handoff.**
