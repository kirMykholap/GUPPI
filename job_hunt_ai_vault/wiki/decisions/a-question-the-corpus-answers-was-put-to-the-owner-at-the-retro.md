---
title: "A divergence: a question the corpus already answered was put to the owner at the retro"
type: decision
status: current
authority: retro-corpus-question-divergence
basis: human
binding: prohibition
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/skills/retro/SKILL.md"]
tags: [process, vault, agents]
---

# The divergence, 2026-08-19

**The rule:** `/retro` says *where a question can be answered by reading the repository or asking the
vault, do that instead of asking the owner*.

**What was done:** the retro's frontier carried a line about `pages.base` gaining a filter on its
*Every page* view, classified as *deliberate, or a stray click*, and it was put to the owner. He
answered «мы уже говорили об этом».

**[[pages-base-is-not-a-review-item]] settles it** — *"`pages.base` stays tracked and stops being
watched: a session commits it without discussion"* — and it was found **in one grep, after the round
had been spent**.

**Rejected alternative: grep first.** It costs one command.

## Why it looked unnecessary at the time, and this is the useful half

**Three other frontier lines had been checked against the tree and dropped or closed** in the same
pass, so the habit was live rather than absent. **Every one of those three was about something the
session had built itself.**

**This one arrived through `git status` as somebody else's change**, and a change from outside got
classified as *unexplained* rather than as *unasked-about*. The two words route to different places:
*unexplained* routes to the owner, *unasked-about* routes to the corpus.

**The trigger that falls out is on its own page**, because it generalises past this incident:
[[a-file-this-session-did-not-touch-is-a-vault-question-before-an-owner-question]].

## What makes this instance worse than the earlier ones

**It is the third instance of the shape on the record and the first inside `/retro`**
([[deriving-what-the-vault-already-holds-costs-a-round]],
[[an-objection-priced-against-a-cost-already-paid-dissolves-on-a-page-nobody-opened]]). The other
two were derivations — work redone that the vault held. **This one is different in one respect: the
skill running at that moment tells the session not to do it**, and the instruction was in context.

**So the failure is not that the rule was unknown.** Knowing a rule is not a mechanism
([[knowing-a-rule-is-not-a-mechanism]]), and what was missing is the trigger that turns a category
of observation into a grep.
