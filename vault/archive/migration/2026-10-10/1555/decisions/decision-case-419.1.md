---
type: decision
case: "419.1"
status: archived
update: ["[[rule-case-protocol]]", "[[estimate-orchestration-shows-the-built-case]]", "[[rule-ask]]", "[[rule-skill-hi]]", "[[rule-prespec]]"]
origin: raw/2026-09-25/1228/ledger.md#case-419.1
sprint: migration
created: 2026-09-25
tags: [session, workflow, ledger, harness]
---

## Context

Today the main agent reads the pages itself. Before a `create` it asks the vault through `ask-guppi`, sends the frame to `frame-guppi` for a check, and writes the Case into the chat itself. No script reads the form of a Case in the chat. The hook of `rule-spec-write` checks a Case only after its ratification. So a fault of the form is found by the person or by `ask-guppi` at pre-spec. This happened in session 0051 and is recorded in `insight-case-form-chat-form-read-by-no-script`. Case 416 deferred a new scheme until a live probe. The probe showed two facts. First: `SubagentStop` with exit 2 sends the subagent back with the text of the hook, and the payload holds `agent_type`, `last_assistant_message` and `stop_hook_active`. Second: a Case cannot be shown through `systemMessage`. So the main agent shows the Case, and a hook compares the showing with the checked answer. This Case takes the core of the scheme of 416: who builds a Case, how it is checked, and how the showing is compared. `{supersedes:case 416}` lifts the defer from every page 416 deferred. The parts outside the core are to be deferred again by a short Case: the defers written by the hook, a guard on the plan with the translation after it, and a rule of its own for the orchestration. The question of Case 403, whether a subagent pays, becomes the method of the Estimate of `case-guppi`. `frame-guppi` read the frame of every sub-case and found a contradiction: the Purpose of `rule-ask` named `ask-guppi` the one entry point, each call in the event log; 419.1 rewrites that Purpose whole. `ask-guppi` was not dispatched: the one `create` of a rule, `rule-case-check`, has a `ref`; a Glob found the slugs `rule-case-check` and `rule-case-build` free. Estimates left alone, and why: `estimate-ask-finds` reads how `ask-guppi` answers, not who calls it; the Estimates of `rule-skill-hi` read the Frontier; the Estimates of `rule-spec-write` read the write after ratification; `estimate-hook-registry-rendered` reads only that the file equals the Render.

## Problem

How a Case is built, checked and shown, so that the person sees only a Case that passed the checks of pre-spec, and the reading of the vault and the frame does not fill the main agent's context.

## Given

`rule-case-protocol` — the rule of the Case: who builds it, and the story sections
**＋** `vault/wiki/case-schema.md` — its render
**＋** `estimate-orchestration-shows-the-built-case` — the Estimate of the frame read before a showing, renamed `estimate-orchestration-shows-the-built-case`
**＋** `rule-ask` — the rule of `ask-guppi`: who asks the vault, and when
**＋** `.claude/agents/ask-guppi.md` — its render
**＋** `rule-skill-hi` — the rule of `/hi`: its sentence on the vault before a `create`
**＋** `.claude/skills/hi/SKILL.md` — its render
**＋** `rule-prespec` — the rule of pre-spec: its sentence on the question before a `create`

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#case-419.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
