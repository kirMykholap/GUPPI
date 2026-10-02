---
type: decision
case: "445.3"
status: current
update: ["[[estimate-spec-write-removes-a-superseded-case]]"]
origin: raw/2026-09-26/2300/ledger.md#case-445.3
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow]
---

## Context

Today the hooks write each Case into the plan file. The `Stop` hook of `rule-spec-write` writes the stored English answer of `case-guppi`, and it writes a short-form defer from the reply. The agent can still edit the plan by hand. `uv run guppi ratified --edit` on `PostToolUse` compares an edited plan with the ratified copy `<plan>.ratified.md`, which the same hook function writes beside it. The comparison covers only what the scripts apply, so a change of a name, `context` or `problem` passes without a word. In session 1745 the agent showed the short-form defer of Case 442. It then edited the plan to translate its heading, `context` and `problem`, and `estimate-orchestration-defers-in-one-reply` failed on that edit. Case 423 deferred this question to `rule-spec-reconcile`. Case 441 answered its second half. `case-guppi` answers in English, the main agent translates only for the chat, and a short form is written in English as it is shown. After that, no step needs the agent to edit the plan. Once nothing but the hook writes the Cases, the copy only compares the plan with itself.

The person decided the following. Every edit of a plan file that exists is refused for the whole session, not only while a line under `## Cases` is open. The one exception is a `Write` that creates a plan file with one title line. The agent's edits of the stores `<plan>.checked.json` are refused too. The ratified copy goes, and with it the `--edit` hook, the marks `<plan>.waiting.json` and the comparison of pre-spec with the copy. The Cyrillic finding of pre-spec stays, and its Estimate moves to `rule-language`. `/hi` opens a session only in plan mode, and a payload with no `permission_mode` is refused. A session repaired without `/hi` is a known path, since the fix of session 1745 was made that way. The refusal is the promise of `rule-event-log`, whose hook writes the `hi` line. `rule-skill-hi` only describes it. In session 1337 a session that began outside plan mode wrote a second plan file under another name. With `/hi` refused outside plan mode, that path needs no exception in the guard. The second count of C4 is text after the Frontier in the defer reply. No mechanical check covers it, and it is not done here. `estimate-orchestration-defers-in-one-reply` stays failed until a later reading. The ticks of `raw/<date>/<hi HHMM>/spec.md` are out of this Case and are Frontier item C14. The agent still ticks that file, so the guard does not cover it.

The frame gives the following. A call the guard refuses has no `PostToolUse`, so the `event tool` hook writes no `tool Write:` line for it, and `plan_path` of `guppi/ledger.py` still names the plan. The docstring of `guppi/guard.py` records the same for its own refusals. `is_plan` of `guppi/ratified.py` and `plan_path` judge a plan path with two copies of one test, and 445.1 puts that test in one function. `uv run guppi guard` stands on the same `PreToolUse` matcher and refuses only files that a rule page governs. No rule page governs a plan file, so the two hooks judge different files. The hooks of one `UserPromptSubmit` group run in parallel. So the refusal of `/hi` lives in `uv run guppi event prompt`, which writes the `hi` line; a refusal in `guppi gate` would still leave the line written. The agent's `Skill` call of `hi` is no path, because the skill carries `disable-model-invocation: true`. The hooks documentation lists `permission_mode` among the input fields common to every event, and its example of `UserPromptSubmit` carries the field. No probe in the repository has read it on that event, so the `method` of `estimate-event-log-records` reads it live. `ratified.untranslated` today reads only the Cases before `## Deferred`, so a short form shown in Russian would pass. 445.4 extends it to `## Deferred`, which is why the person kept the finding. At the first ratification, sub-case 445.5 carried two ledger lines. One created `estimate-skill-hi-opens-only-in-plan-mode`, and one updated `rule-skill-hi`. The ledger only grows, and that Estimate is no longer created. So 445.7 carries the update of `rule-skill-hi` with `{supersedes:case 445.5}`, which retires both lines of 445.5 and takes its section out of the plan.

The frame also gives these contradictions. Case 444.2, ratified in this session, replaces the Criterion of `estimate-spec-write-copies-the-ratified-case`, and its `when` and one `＋` line name the ratified copy. One Criterion is not signed twice in one session, so this Case does not name that Estimate. 444.2 goes back to its `case-guppi` to drop the copy and is ratified again. In the same step, its `case-guppi` corrects the sentence of Case 444's `context` that says `rule-spec-reconcile` stays deferred. The last `－` line of `estimate-spec-write-writes-a-defer` says the ratified copy gets no defer. It stays true when no copy exists, so it stands. The Render of `rule-language` and one `＋` line of `estimate-language-followed` still say that the prose is translated into English before approval. That has been false since Case 441. They stand here and are Frontier item C15. Some Estimates stay true and stand. `estimate-hi-writes-frontier` and `estimate-hi-no-read-calls` read a `/hi` that opens a session, and a refused `/hi` opens none. `estimate-default-mode` promises that the session opens in Plan Mode, and 445.6 enforces that. `estimate-hook-registry-rendered` promises only that the file equals the Render. `estimate-orchestration-shows-the-built-case` already says that the agent edits no Case in the plan, and the guard keeps that true. The `Result` sections and History lines that name the copy are records and stay.

## Problem

Whether a guard refuses every edit of the plan by the agent while a line under `## Cases` of the Frontier is open, and when and how the prose of a Case is translated (the question of case 410).

## Given

`estimate-spec-write-removes-a-superseded-case` — the promise of the removal
**＋** `rule-spec-write` — the rule of the Spec hook
**＋** `guppi/ratified.py` — `remove_superseded`
**＋** `raw/<hi date>/<hi HHMM>/spec.md` — the Spec of the session

## History

- 2026-09-27 created · raw/2026-09-26/2300/ledger.md#case-445.3
