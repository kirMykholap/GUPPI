---
title: "DIVERGENCE: the retro's menu step was answered in enumerated prose, and no menu was asked all session"
type: decision
status: archived
authority: retro-question-form
binding: divergence
basis: code
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", ".claude/skills/retro/SKILL.md"]
tags: [process, harness, agents]
---

# What happened, 2026-08-26

**The rule:** step 2 of `/retro` says to use `AskUserQuestion` to ask the owner how he wants to work
the list.

**What was done:** the question was asked in enumerated prose. **The session said so before doing
it**, which is what the ask-before-weakening rule requires
([[ask-before-weakening-or-working-around-a-rule]]).

**Why:** the owner's recorded preference is enumerated prose over a rendered menu — tested twice on
2026-08-24, and he interrupted both times
([[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]). A user instruction
overrides a skill, and he answered in prose without objecting.

# The measurement that belongs beside it

**`session-dialogue.py` reports `menus asked 0` for the whole session**, in which thirty-six
decisions were taken.

**That matters for how those decisions are attributed.** The `owner selected` shape carries a known
framing defect — the alternatives were the session's — and here it applies only to recommendations he
was answering, never to a list he could not see past
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**The retro skill notes that a session whose every ruling arrived through a menu is a session the
owner did not frame.** This is the opposite case, and it is recorded for the same reason.

# What it obliges

**The skill and the preference disagree, and the skill is the thing that is wrong.** Nothing is
changed here — a skill file is not the librarian's to write — and the divergence is the record that
the disagreement is live rather than accidental.
