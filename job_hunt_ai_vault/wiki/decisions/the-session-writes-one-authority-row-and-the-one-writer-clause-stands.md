---
title: "The session writes one `authority.md` row instead of the librarian, and the one-writer clause stands"
type: decision
status: current
authority: register-writer-exception
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target: none
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/authority.md", ".claude/hooks/lock-the-librarian.ps1"]
tags: [vault, process, agents]
---

# Context

**The session wrote `wiki/decisions/the-cleanup-suspends-the-rules-that-would-refuse-it.md` into the
vault, and the gate went red on its `authority:` slug** — `cleanup-rule-suspension` was in the tree
and not in `authority.md`, which rule 13 compares in both directions.

**`.claude/hooks/lock-the-librarian.ps1` refuses to dispatch the librarian while the gate exits
non-zero.** So the only party permitted to write the register could not be called, because of the
register row only it may write ([[one-page-written-into-the-wiki-reaches-the-register-deadlock]]).

**The one-writer clause on the registers is not among the four rules the cleanup lifted**, which is
why the question was asked at all rather than assumed.

**Files this touches:** `job_hunt_ai_vault/authority.md`, `.claude/hooks/lock-the-librarian.ps1`.

# The question

**Does the session write the one row, or does the decision page get rolled back so the librarian can
be dispatched on a green gate?**

# How it works after

**The session wrote the row.** One line, into `authority.md`, under the family
*draining a folder into the archive*, and the gate went green.

**The clause itself is untouched.** The librarian is still the only writer of `wiki/` and of the
registers; what happened here is a licence for one line, granted on a direct question with the
alternative named.

**It is a licence for one line and not for fifty-three.** The same lock arrives at fifty-three times
this size when the family rules land, and this permission does not reach it
([[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]]).

# Recommendation

**Ask, and take the answer rather than assuming it.** Rolling the page back would have worked and cost
a rewrite; writing the row without asking would have crossed a live prohibition on a convenience. The
question is cheap and the clause is not the kind of rule a session lifts for itself.

**Rejected: rolling back the decision page and dispatching the librarian on a green gate.**

# Ratification

**owner, 2026-08-30: «да»**, given to a direct question that named the alternative.

# What is unresolved about it, and it is not the permission

> [!NOTE] RAISED, NOT RESOLVED — the `authority:` slugs differ, so rule 3 of the gate cannot see this
> and no `CONTRADICTION` block is legal for it.

**[[authority-md-is-a-register-the-one-writer-clause-names]]** (`one-writer-register-set`, live
prohibition, 2026-08-26) says the clause covers `index.md`, `tags.md`, `sprint.md`, `log.md` **and**
`authority.md`, and it explicitly refused to read the clause as a closed list. **This page opens a
hole in it**, and whether the hole is one line or a standing exception is not stated.

**The precedent for this shape asked for more than was given.**
[[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]] granted a session a bounded,
mechanical licence and required it to be **recorded as a divergence, with the owner reading the diff
before the commit**. The journal files this as a decision and not as a divergence, and this page files
it as the journal did rather than promoting it.

**And the delivered text never warned the session.** The rendered slice in the repository's
`CLAUDE.md` still enumerates four registers and not five, so `one-writer-register-set`'s own
obligation — *"the clause's wording names this register alongside the others"* — has never landed.
**The session that hit the deadlock was reading a rule that did not mention the file it was blocked
on.**

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
