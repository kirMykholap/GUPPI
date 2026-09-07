---
title: "The session wrote `wiki/` by hand, and it is recorded as one divergence rather than as a series of small permissions"
type: decision
status: current
authority: wiki-write-exception
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/hooks/session-brief.ps1", "CLAUDE.md"]
tags: [vault, agents, process]
---

# The rule, and what was done against it on 2026-08-17

**The librarian is the only writer of `wiki/`** ([[the-librarian-writes-unattended]]), and the
guard hook says so on every write into it ([[session-hooks]]). On 2026-08-17 the main session wrote
`wiki/` by hand:

| What was edited | How many pages |
|---|---|
| a title corrected, or a `quantity:` line added | thirty-seven |
| `sources:` repointed | two |
| retitled again at the retro | one |

**Each write was ordered by the owner**, after the librarian had returned. The same permission
covered a fix to `.claude/hooks/session-brief.ps1` and the clauses added to the vault's own
`CLAUDE.md`.

**Rejected: leaving it as a series of small permissions.** One permission at a time reads as
routine; the count in one line reads as a divergence, and it only became a line because the retro
asked for one ([[the-retro-step]]). Recording it is what makes the exception reviewable, which is
the whole of this project's enforcement model — git plus the log, never a gate
([[the-librarian-writes-unattended]]).

## Why it was safe here, and what the rule owes

Two properties made these writes safe, and **neither is written into any rule**:

- **no concurrency** — the librarian had returned, so there was no parallel writer and no lost write
  ([[parallel-librarians-break-the-one-writer-property]]);
- **the owner reviewed the diff before the commit**, which is the review that replaced asking
  permission.

**The rule owes a clause naming exactly that**: who may write `wiki/` when the librarian is not
running, and what makes it safe. Until it has one, every such repair is an undocumented divergence,
and the vault's own record — that supersession and deletion belong to the owner's session — already
assumes an exception the rule does not state. **The librarian does not write the store's rulebook**,
so this page records the gap and the brief raises it.

## The related one, from the same commit

`git add -A` swept a deletion that was not this session's into this session's commit; the owner had
removed a design PDF while the commit was being assembled and chose to leave it. The rule broken
there is written nowhere at all — [[staging-by-wildcard-sweeps-the-other-partys-edit]].

## The clause is written, 2026-08-17

**The gap this page named is closed** — [[the-one-writer-rule-covers-the-registers-too]] carries the
owner's own wording: *the librarian owns `wiki/` and the registers; a session edits a register only
in the same change that deletes or renames what that register points at, and every such edit is
recorded as a divergence.*

The finding that produced it is that **the hook was already stricter than the text**
([[the-hook-was-stricter-than-the-rule-it-enforced]]). The two properties this page said the rule
still owes — no concurrency, and the owner reviewing the diff — are **still owed**; the clause
settles who may write and when, not what makes an out-of-band write safe.

## Three more divergences, from the second session of 2026-08-17

| What was edited | Why it was done anyway |
|---|---|
| **the vault's own `CLAUDE.md`**, by hand | it looked inapplicable: the rule names `wiki/` in both places that state it, and the schema file sits above `wiki/`. Rejected alternative: dispatch the librarian for a schema the check had just made mandatory |
| **`index.md`**, by hand, with the register guard hook firing mid-edit | the same change deleted `catalogue.md`, which that paragraph pointed at. Rejected alternative: leave a register pointing at a deleted file. This is the case the new clause permits |
| **`wiki/rules/` created by hand**, with a `.gitkeep` | rule 1 requires the directory and git does not track an empty one. It felt unlike writing to `wiki/` because it is a directory rather than a page — **which is the sentence every divergence here opens with** |

**A fourth, of a different kind, from the same session:** four commits went straight to `main`
against the harness default of branching first, and the owner's answer made it the convention
rather than an exception ([[main-is-this-repositorys-branch-convention]]).

## A hand-edit inside a marked region: priority raised by the owner, 2026-08-18

**It is forbidden by nothing**, and it sat on the deferral register as *"the mechanism is protected
by two people remembering it"* ([[what-the-harness-build-waits-on]]).

**owner: priority raised.** It is no longer a deferral for lack of importance, because this session
measured that **the gate did not catch one form of it either**: a blank line added by hand inside
any of the ten regions passed a comparison that claimed byte equality and did not have it
([[a-command-substitution-strips-the-newline-a-gate-compares]]). That defect is fixed; the
prohibition is still nowhere.

**What the gate does and does not cover, now that it works.** It compares a region's bytes against
its page's slice and rewrites the region, so a hand-edit inside a region is *detected and silently
overwritten* on the next run — the edit is lost rather than refused, and nothing tells whoever made
it. That is a different failure from the one the register described, and it is a hole with evidence
rather than a hypothetical ([[a-gate-guarantees-agreement-never-truth]],
[[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]]).

**Do not hand-write a rendered region.** The writer owns those bytes
([[the-injector-writes-the-separator-inside-the-region]]).

## The vault's own `CLAUDE.md` stops being a divergence — 2026-08-19

The third row of the table above — *the vault's own `CLAUDE.md`, by hand* — records the first of what
became three such divergences. **The clause taken on 2026-08-19 makes that class legal**:
what the gate reads as its own input is the session's to write, the owner reads the diff before the
commit, and **no divergence is recorded**
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

**The rows above are not retracted.** They are what happened, and they are the evidence the clause was
taken on ([[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]]).

**The two properties this page said the rule still owes are written down for that file and only that
file.** No concurrency and a reviewed diff are the clause's stated reason; for `wiki/` and the registers
they remain owed, which is what the section above already says.
