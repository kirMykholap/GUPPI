---
title: "The feedback reminder fires on the owner's prompt and speaks only when the channel has gone quiet"
type: decision
status: current
authority: feedback-reminder-trigger
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", ".claude/hooks/remind-the-feedback.ps1", ".claude/hooks/remind-the-smoke.ps1"]
tags: [harness, process, vault]
---

# What was built first, and what replaced it — 2026-08-28

**Built first on `PostToolUse` with a `Skill` matcher**, firing once when `/grill-me` opened.
*(the owner said it, in his own words, and the session built it that morning.)*

**Replaced the same day, on his correction:**

> **owner:** «есть другое предложение.. напоминать каждый мой промпт(onSubmit если я правильно
> помню имя). Это звучит довольно логично, так как какраз решения которые я пишу и не хочется
> потерять...»

**So the hook fires on `UserPromptSubmit`, carries a silence counter, and speaks on the third
consecutive quiet prompt.** His ground is the subject rather than the frequency: the rulings worth
losing are the ones that arrive in his prompts, so his prompt is where the reminder belongs.

# Why the correction was right, and the session had already said so

**The first hook carried a header arguing that a per-invocation reminder becomes furniture, and was
a per-invocation reminder** ([[the-session-argued-against-a-design-in-its-own-header-and-shipped-it]]).
The owner supplied what the session had already argued for, and the counter is the part that answers
the argument ([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).

# What was confirmed about the event, and what was not

**Confirmed:** `UserPromptSubmit` is the event name, it takes no matcher, it supports
`hookSpecificOutput.additionalContext`, and it fires on every turn of the owner's.

**Not confirmed:** the name of the field carrying the prompt text, the behaviour on exit 2, and
whether it fires on the first turn. **The hook is therefore built without reading the prompt text**
— which is what makes the three unanswered questions harmless here and leaves them open for any
other hook on the same event.

# What it does not cover

**A session that goes quiet in its own replies.** This hook counts the owner's turns.
`MessageDisplay` is registered and fires on every assistant reply, and that is where a turn counter
covering the session's own silence would live — found this session and not used
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]]).
