---
title: "`authority.md` is a register only the librarian writes, and the one-writer clause names it too"
type: decision
status: current
authority: one-writer-register-set
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "job_hunt_ai_vault/authority.md"]
tags: [vault, process, record-schema]
---

# The ruling, 2026-08-26

*(the owner selected it, against the reading that the clause names four registers and `authority.md`
is not among them.)*

**The one-writer clause of 2026-08-17 covers `index.md`, `tags.md`, `sprint.md`, `log.md` **and**
`authority.md`.** The librarian is the only writer of every register named there.

**The reason it was missing is a date, not a judgement.** `authority.md` was created on
2026-08-21, four days after the clause was worded, so the enumeration could not have named it
([[authority-becomes-the-index-and-is-required-outside-rules]]).

**And it behaves exactly like the other four**: `bash scripts/vault-authority.sh --check` compares it
against the tree in both directions, which is the property that makes a second writer detectable and
expensive.

# Rejected

**Rejected: reading the clause as a closed list.** A closed list of registers has to be extended by
every register anyone adds, and the failure mode is silent — a register outside the list has no
declared writer at all ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# What it obliges

**The clause's wording names this register alongside the others**, in the vault's own `CLAUDE.md`
and wherever else the enumeration is rendered. That file is the session's to write
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]), so this page is the decision and
the edit is theirs.

# The obligation above has never landed, and a session hit the register it does not mention — 2026-08-30

**The rendered slice in the repository's `CLAUDE.md` still enumerates four registers** — `index.md`,
`tags.md`, `sprint.md`, `log.md` — **and not this one.** The edit this page ordered has not been made
in the four days since.

**A session then walked into exactly the gap.** It wrote one page into `wiki/decisions/`, the gate
reddened because the page's `authority:` slug was not in `authority.md`, and
`lock-the-librarian.ps1` refused to dispatch the only party permitted to write the row
([[one-page-written-into-the-wiki-reaches-the-register-deadlock]]). **The delivered text it was
reading did not mention the file it was blocked on.**

**The owner cleared it by permitting the session to write that one line**, on a direct question with
the alternative named ([[the-session-writes-one-authority-row-and-the-one-writer-clause-stands]]).

> [!NOTE] RAISED, NOT RESOLVED — the `authority:` slugs differ, so rule 3 of the gate cannot see this
> and no `CONTRADICTION` block is legal for it.

**Whether that permission is one line or a standing exception is not stated**, and this page refused to
read the clause as a closed list precisely so that holes could not be opened by omission. **The
precedent for a bounded licence of this shape** —
[[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]] — **required it to be recorded as
a divergence with the owner reading the diff**; the journal files it as a decision. **Both readings are
live and neither is chosen here.**

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
