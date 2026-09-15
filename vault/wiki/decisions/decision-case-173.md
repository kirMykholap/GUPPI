---
type: decision
case: "173"
status: current
update: ["[[insight-retro-typed-command-is-never-a-tool-call]]", case-schema]
origin: raw/2026-09-15/1809/ledger.md#case-173
sprint: migration
created: 2026-09-15
tags: [hooks, session, harness]
---

## Context

`insight-retro-typed-command-is-never-a-tool-call` is an Insight, `open`, severity 2, with two children: the lessons of sessions O and Q. Its pattern: a slash command typed by the person is expanded by the client into the prompt and is never a Skill tool call; a hook on the Skill tool sees only the agent's own calls, and a cure aimed at the skill's settings (case 150) changed the agent's path and left the typed one as it was. Its Proposal: treat the two paths as two — the agent's call gated on `PreToolUse Skill`, the typed command on `UserPromptSubmit`; a `then` on a slash command names which path it covers, and its reading takes both. The librarian created the Insight in the run of session R, after 169.1–169.3 had ratified most of the Proposal in that session: `guppi gate` is the second command on `UserPromptSubmit` and reads a typed `/pre-task`, `/retro` or `/handoff`; `rule-retro` names both paths; the reading of `estimate-retro-loads` (169.3) takes both — typed and called, two `retro` marks in the event log.

## Problem

The Insight stands first in the Deferred list of the brief and must end in this Plan Mode as `actioned`, a rejection or a `defer`. The mechanics of the Proposal exist since 169.1–169.3, but one sentence of it is ratified nowhere: the rule that a `when` on a slash command names its path and the reading of a `then` covering both takes both. Without it the next Case on `/hi` or `/ask` can again write a `then` that assumes both paths go through the Skill tool — the root of the lessons of O and Q.

## Given

`insight-retro-typed-command-is-never-a-tool-call`: `status: open`, `severity: 2`, no `addressed_by`, no `deferred_by`; an `update` with a `ref`, the page read, no vault query needed.
**＋** `rule-retro-commit` (169.1): the gate on `UserPromptSubmit` reads the payload's `prompt` for `/pre-task`, `/retro`, `/handoff`, the same two checks and the same mark; `rule-hook-registry` (169.2): `guppi gate` is the second command on `UserPromptSubmit`; `rule-retro` (169.3): both paths behind the gate, the reading of `estimate-retro-loads` takes both.
**＋** The readings of 169.1–169.3 stand `pending` until the first typed `/retro` of this session; `actioned` is not terminal — a new lesson with the same root cause reopens the Insight (insights schema, §8), so a failed reading reopens it by itself.
**＋** `case-schema.md` is a Rule-class file: an `update` with `file` and `change`, applied by hand in Work Mode (case 166.1); ledger line `[case-schema]{ref:case-schema}` (cases 92, 123, 149.2). The section "`when` and `then` are the criterion" says nothing today about the paths of a slash command.
**＋** `generate`: an `update` of an Insight with `status: actioned` goes as any update; the cascade archives the `clustered` children and recounts `severity` (case 168 went the same way).
**－** No new Rule page: the sentence has no hook, check or render — it is a rule for writing a Case, and its place is `case-schema.md`.

## History

- 2026-09-15 created · raw/2026-09-15/1809/ledger.md#case-173
