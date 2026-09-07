---
title: "The `/pre-task` rule leaves `CLAUDE.md` and its addressee becomes a hook"
type: decision
status: current
authority: pre-task-rule-delivery
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "CLAUDE.md", ".claude/hooks/check-the-plan.ps1"]
tags: [harness, agents, process]
---

# The ruling, 2026-08-20

> **owner:** «hook добавляем, регион в `CLAUDE.md` убираем. Я принимаю этот риск.»

**This is the dated page that [[a-rule-moving-to-conditional-delivery-needs-its-page-first]]
requires, and it is written before the move.** The guarantee changes: a rule rendered into
`CLAUDE.md` reaches every session unconditionally, and a rule delivered by
`.claude/hooks/check-the-plan.ps1` reaches only a session that presents a plan.

**Rejected alternative, offered and declined: add the hook and keep the region.** The argument for
it was that the hook fixes the *moment* of delivery while the file remains the only channel that
works when no hook event fires. **The owner's ground is that delivery which is reliably ignored is
not delivery** — the rule was in that file, arriving in every session, and was skipped three times
in two sessions
([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]]).

# It goes against a criterion of the owner's, knowingly

**[[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]] says `CLAUDE.md` carries
what bootstraps the asking**, and `/pre-task` is the rule that bootstraps the asking. The librarian
raised exactly that at the pre-task run for this work, and the owner ruled anyway.

**This is a change to that criterion, not a case exempted from it.** The distinction is the whole of
why it is written here: an exemption leaves the criterion able to sort the next rule, and a change
does not. What the criterion now has to survive is a rule that bootstraps the asking being delivered
conditionally, on the ground that unconditional delivery which is ignored buys nothing.

**[[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]] rests its own ground on this
rule arriving unconditionally** — *"a rule nobody knows exists is still surfaced"*, because
`/pre-task` enumerates the constraints on a plan. That ground now rests on a rule which arrives only
when a hook event fires. **Re-reading it is the owner's**, and nothing here decides it
([[the-librarian-writes-unattended]]).

# The destination is `.md` and not `.txt`

**The approved plan named a `.txt`, and `/pre-task` caught it before a line was written.** The
governed set is `*.md` under `.claude/` **by property** rather than by a list
([[the-governed-set-is-swept-and-markdown-by-property]]), so a `.txt` would have been invisible to
the address verdict, the hand-edit verdict and the leftover sweep **at once** — the state two of the
owner's rulings exist to forbid ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]],
[[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

**`.claude/hooks/messages/` was created by that session with nobody deciding it should exist**, and
it is decided here: it is the directory the rule's `governs:` names. The injector creates the file
and never the directory, on the reasoning that a missing directory is a typo far more often than an
instruction ([[a-generated-rule-file-with-no-paths-carries-no-frontmatter]]).

# The second move to meet the gate, and the reading it still leaves open

**The first was the AST rule** ([[the-ast-rule-moves-to-prove-the-mechanism]]), which closed the
gate's stricter reading *"at the cost of one section rather than deciding whether it was a gap"* and
left which reading the gate carries **open for whoever brings the second move to it**.

**This is that second move, and it satisfies the strict reading in the same way**: the rejected
alternative is named on the move's own dated page, above. **Neither reading is ruled on here** —
that is a judgement about the project ([[ask-before-weakening-or-working-around-a-rule]]), and it is
raised in the brief a second time rather than settled.

**What the move costs, stated as the gate states it:** unconditional delivery costs context and
nothing else; conditional delivery costs a rule that does not arrive. Here the price is paid where a
session presents no plan and writes nothing — and the write net exists precisely to narrow that gap
([[the-guard-chain-appends-the-net-rather-than-branching-on-it]]).
