---
title: "A rule reaches a session by several routes, and only one transition between them had a written gate"
type: concept
status: current
authority: rule-delivery-modes
basis: inference
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md"]
tags: [harness, process, agents]
---

# The routes

| how it arrives | when it arrives |
|---|---|
| rendered into the repository's `CLAUDE.md` | **unconditionally**, every session, every turn |
| a file under `.claude/rules/` with a `paths:` scope | **on a matching read**, and on nothing else ([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]) |
| a hook message | **on the hook's own trigger** ([[session-hooks]]) |

**Only the first is unconditional.** The other two are deliveries that depend on something the
session does, and a session that does not do it never sees the rule.

# The gate was written for one of the two transitions and not for the class

**The gate of 2026-08-18 governs `CLAUDE.md` → `.claude/rules/`.** Its safety test — the dangerous
action must force a matching read — is a test about `paths:` scoping, and it is meaningful only
there.

**`CLAUDE.md` → a hook message is the other transition, and it was outside the gate.** The
`/pre-task` rule took it on 2026-08-20 with a direct ruling of its own, so nothing was smuggled
([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]) — but nothing in writing said the gate
applied.

**The gap is closed by widening the subject rather than by listing the modes**
([[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]]). The safety
test stays where it means something, because a hook reads no file and cannot be asked whether a
read forces it.

# Why the table above is not the rule

**A table of delivery modes is a list, and a list of ways a rule can arrive has to be extended by
every mechanism anyone invents.** The predicate the gate asks — *has this rule stopped arriving
unconditionally?* — needs no maintenance
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# A fourth route was invented on 2026-08-30, and the section above predicted it

**A rule page under `render: authority` is written into no file and is fetched by a hook when a file
its slug answers for is touched** ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).

**It arrives as a hook message, which is row three of the table**, so the table does not need a fourth
row — **but the trigger is new**: not the hook's own schedule, and not a `paths:` match, but a lookup
on the subject of the file being written. **That is the difference worth naming**, and it is exactly
why the gate asks a predicate instead of reading the table.

**The gate applies to it and was satisfied before the mode was used.** Moving a rule off unconditional
delivery needs its own dated decision with a rejected alternative
([[a-rule-moving-to-conditional-delivery-needs-its-page-first]],
[[the-conditional-delivery-gate-covers-any-departure-from-unconditional-delivery]]); the alternative
named was rendering into the vault's own `CLAUDE.md`, and the decision was written before any rule
page ([[the-rule-about-rules-is-served-by-the-hook-and-not-rendered-into-claude-md]]).

**The safety test still means nothing here, for the same reason it means nothing for a hook message**:
this route reads no file on the reader's behalf and cannot be asked whether the dangerous action forces
a matching read. **What it can be asked is whether the delivery exists at all, and today it does
not** — the hook has no `authority:` matching branch
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

**Eleven rules stay on the unconditional route deliberately.** They render into the repository's
`CLAUDE.md` and must be known **before** any write happens; a delivery triggered by touching a file
arrives after the decision to touch it.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
