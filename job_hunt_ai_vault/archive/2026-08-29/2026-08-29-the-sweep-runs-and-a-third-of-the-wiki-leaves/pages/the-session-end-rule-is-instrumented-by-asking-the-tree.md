---
title: "The session-end rule is instrumented by asking the tree, and no hook is registered for it"
type: decision
status: archived
authority: session-end-instrument
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/settings.json"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-25

> **owner:** «ТАк а какой именно хук ты предлагаешь вешать на конец сессии? Что он делает И зачем?
> Про конец сессии я понял. Сейчас я слежу за этим.. но вот зачем тут хук я пока что не понимаю»

**No hook is registered for the end of a session.** One question removed a build item.

**The rule is instrumented by asking the tree instead** — an uncompiled journal, and commits newer
than the newest journal. Both are questions `--lint` can ask at any time
([[a-session-ends-with-retro-then-handoff-then-ingest]],
[[the-sidecar-is-the-single-definition-of-compiled]]).

# Why a hook can do nothing here

**By the time it fires the ritual is missed and there is nobody to ask.** A `Stop` or `SessionEnd`
hook arrives after the session is over, so it can neither prompt nor block — the failure it would
report is already final.

**The ritual leaves artefacts in the tree**, so the question is answerable at any time and needs no
event at all.

# The framing the proposal came from was inherited and never tested

**A page records the obstacle as *no event exists at which a session's end can be noticed***, and
the session proposed registering a hook for that event
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]). The obstacle is not the event; the
obstacle was the assumption that an event is needed.

# What the harness holds today, read off `.claude/settings.json`

**No `Stop`, `SessionEnd` or `SubagentStop` hook is registered.** What is registered:
`SessionStart`/session-brief, `PreToolUse Edit|Write`/ask-the-vault,
`PreToolUse Agent|Task`/lock-the-librarian, `PreToolUse ExitPlanMode`/check-the-plan,
`PostToolUse ExitPlanMode`/check-the-plan, `PostToolUse Write|Edit`/check-the-journal,
`PostToolUse Agent|Task`/record-the-dispatch, and `MessageDisplay`/catch-the-feedback
([[session-hooks]]).

# Not done

**`--lint` does not ask either question yet.** Neither the uncompiled-journal check nor the
newer-commits check exists, and the merge of the hooks into one pipeline — dropped with the
session-end hook and then recovered — is a proposal
([[the-hooks-merge-into-a-common-pipeline]]).
