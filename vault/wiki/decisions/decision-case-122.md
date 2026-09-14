---
type: decision
case: "122"
status: current
update: ["[[rule-ledger-write]]", "[[rule-case-protocol]]"]
supersedes: ["[[decision-case-117]]"]
origin: raw/2026-09-14/1029/ledger.md#case-122
sprint: migration
created: 2026-09-14
tags: [session, hooks, harness, ledger, workflow]
---

## Context

Four lessons on one writer: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (F), `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (I, archived), `lesson-transcript-omits-text-emitted-before-tool-calls` (L) and `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live` (M). The `Stop` hook reads the final text of a turn; a reply that ends in `Skill`, `ExitPlanMode` or any tool call has no `Stop` and its text is not in the transcript. The Insight's Proposal has stood unactioned since session I. (Case 117 as it stands.)

## Problem

The rule "a reply with ledger lines ends in text" lives in the agent's memory only, and the agent broke it with the lesson live. Either the hook reaches those lines — a `PreToolUse` hook on `Skill|ExitPlanMode` that reads the reply under way, if the payload carries it — or the harness makes the agent's rule mechanical: `CLAUDE.md` says it, and `guppi gate` refuses a `Skill` call while the reply holds an unwritten `LEDGER` block. Which of the two is measurable is a Plan Mode of its own. (Case 117 as it stands.)

## Given

Measured in session N at 10:4x: a text emitted before a `Bash` call in the same reply is absent from `~/.claude/projects/…/19037d1c….jsonl` — the assistant records around it are `thinking` and `tool_use` only — and session M's transcript holds no assistant text between the owner's «ратифицирую» (record 650) and the `Skill` call of `/pre-task` (679): the block of 115 and 116 was never persisted. A `PreToolUse` payload carries `tool_name`, `tool_input`, `transcript_path`, no reply text. The question of the Insight's Proposal is settled: absent, not dropped.
**＋** `rule-ledger-write` (`Leaf`, `draft`, `estimate-ledger-write-lifts` `pending` on blocks 111.3, 111.6): "a reply that ended in a tool call reaches the ledger at the next `Stop` of the session" — true only when the agent repeats the block. `deferred_by: [decision-case-117]`.
**＋** `guppi gate` (`rule-retro-commit`, `built`) already runs on `PreToolUse` with the matcher `Skill` and refuses `/handoff` on a dirty tree; `.claude/settings.json` needs no change, `rule-hook-registry` is not touched.
**＋** `guppi pretask --check` already finds "item […] has no decision line" (`pretask.check_lines`, `window_lines`, `session_decisions`, `split_cases`, `then_blocks`); the gate reuses them and reports only that half. `rule-pretask` is not changed: the check at `/pre-task` stays as it is.
**＋** The plan file is in no payload; the event log holds `tool Write:` / `tool Edit:` lines with the full path (`- 07:52:53 fde37e7c tool Write: C:\Users\kir\.claude\plans\async-sauteeing-moon.md`). The gate takes the last such path of this session's stamp under `.claude/plans/`. Retro's defers go to `spec.md` only, so the gate reads that file too; `/handoff` after a Retro reply with defer lines is refused the same way.
**＋** `rule-case-protocol` (`Leaf`, `built`, `render` into `CLAUDE.md`, `estimate-case-protocol-loaded` `passed`): the paragraph "Ledger lines are written by the `Stop` hook, from the reply, verbatim" says nothing about where in the reply.
**－** `estimate[...]` and `lesson[...]` lines have no source but the text; the gate does not see them. The sentence in `CLAUDE.md` covers them; a loss of one is still a Retro finding, as today.
**－** `ExitPlanMode` is not gated here: `/pre-task` precedes it and is a `Skill` call, so a reply that ratifies and closes Plan Mode at once is refused at the `/pre-task` step.
**－** Without a `hi`, without a Spec and without a plan path in the log the gate has nothing to check and exits 0; the `/handoff` refusal of `rule-retro-commit` stays as it is.
**－** The Frontier line F1 closes on this Case.

## Criterion

- [[estimate-ledger-write-lifts]] § case 122

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-122
