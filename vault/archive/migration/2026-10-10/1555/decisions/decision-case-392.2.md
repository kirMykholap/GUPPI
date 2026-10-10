---
type: decision
case: "392.2"
status: archived
create: ["[[estimate-context-size-warns-past-the-limit]]"]
update: ["[[rule-context-size]]", "[[rule-hook-registry]]"]
origin: raw/2026-09-24/1303/ledger.md#case-392.2
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session, render]
---

## Context

Today the person does not see how full the context window is. In VS Code the indicator in the prompt box shows only past 50%, and `/context` is typed by hand. A hook gets only `transcript_path`, not the size of the context: the answer of the Claude Code documentation (`hooks-guide.md`), brought by the agent `claude-code-guide`. The size can be counted from the transcript: every reply of the model carries `usage` there, and the sum of input, cache read, cache creation and output is the size of the context; the measurement of this session was taken that way. The stdout of a `UserPromptSubmit` hook reaches only the agent: the person did not see the line `hi: 13:03:25 …` after `/hi`. For the person there is the `systemMessage` of a `Stop` hook; the documentation says it is shown to the user, and is silent on `Stop` in VS Code. So the first reading is live: if the line is not seen, Case 392.1 is shown again with the fallback, the line written by the agent, about 20 tokens a reply. By Case 391.2 this Case calls for `frame-guppi`, which exists only from the next session; the agent read the frame itself: the Render of `rule-hook-registry`, the `Stop` and `UserPromptSubmit` keys of `.claude/settings.json` (`guppi ledger`, `guppi ratified`, `guppi event prompt`, `guppi gate`), `rule-bash-guard` as the pattern of a hook rule, and the docstring of `guppi/ledger.py`. Two findings. First, `guppi ratified` may exit 2, and then `Stop` fires again with `stop_hook_active`, so the new hook stays silent on the re-fire, or the line comes out twice. Second, the ledger hook takes the final reply from `last_assistant_message`, since at `Stop` the transcript may not hold the last call yet; so the number is the last call the transcript holds, and may lag one call. Both went into `then`. `rule-hook-registry` stands `built`; its `estimate-hook-registry-rendered` still holds a block of the old model that counts the commands of `UserPromptSubmit`, so 392.4 replaces its Criterion with the live reading of 378.5. `rule-context-size` goes under `rule-harness`, whose Purpose counts the rules outside its pipeline; 392.3 brings that count and `estimate-harness-pipeline` up to date. A rule whose hook only prints has a precedent in `rule-compact-recall`. No vault query: every `create` line of the ledger carries a `ref`. The names `rule-context-size`, `guppi/context.py` and the two Estimate slugs are free: a grep found none.

## Problem

The person sees in the chat neither the size of the context nor its growth over a reply, and nothing stops a session that has grown too large. Are a line after each reply and a warning past 400 000 tokens needed?

## Given

`rule-context-size` — the rule 392.1 creates.
**＋** `estimate-context-size-warns-past-the-limit` — its Estimate.
**＋** `guppi/context.py` — the same count of N; `tests/test_context.py` — its tests.
**＋** `rule-hook-registry` — the `"UserPromptSubmit"` key of its Render.
**＋** `.claude/settings.json` — the rendered hooks, where `guppi event prompt` also prints to the agent's context.

## History

- 2026-09-24 created · raw/2026-09-24/1303/ledger.md#case-392.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
