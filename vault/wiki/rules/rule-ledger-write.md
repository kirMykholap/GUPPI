---
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
status: draft
enforcement: hook
implementation_ref: [guppi/ledger.py, .claude/settings.json]
parent: rule-session-start
estimates: [estimate-ledger-write-lifts]
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## Purpose

Prevents a ratified line from existing only in a chat reply, or landing in a session no
`/hi` opened. The instruction to write `- decision[...]`, `- estimate[...]` and
`- lesson[...]` lines lives in `CLAUDE.md`, so the agent produces them in *any* session —
including one with no sprint, no branch context and no brief. Without this hook's check the
ledger would silently gain a session that was never a working session, and the librarian
would materialize pages from it the next day.

## How it works

`uv run guppi ledger` on `Stop` — not `MessageDisplay`, which can neither block nor speak
(measured 2026-08-29). Reads the reply that just finished, finds every line that starts
with `- decision[`, `- estimate[` or `- lesson[` at column zero **and is not inside a
fenced block** — a fenced line is a preview, a Case's `then` shows lines before they are
ratified — and appends them verbatim to `vault/raw/<today>/ledger.md`, interpreting
nothing. The ledger is not created at session start; it comes into existence with the
first line.

**Checks the event log first.** The session is a working one when a `hi` line follows the
last `session-start` line of this session's id, with no other session's start in between.
When the check fails and there are lines to write, the hook exits 2 with the reason on
stderr — `ledger: N line(s) not written — no /hi recorded for session X. Tell the person;
run /hi, then repeat the lines.` — so the person is told rather than left believing their
decisions were recorded. With `stop_hook_active` set (the re-fire after a block) it exits 0
and writes nothing, so it cannot loop.

A line already present in today's ledger, verbatim, is not appended again: this covers the
hook running twice on one reply and the agent repeating a line in a later reply.

Which field carries the reply is measured by the Slice 1 probe before this hook is written;
the implementation arrives in the session after the probe (Slice 1, session B).

## Estimates

- [[estimate-ledger-write-lifts]]

## Parent

- [[rule-session-start]]

## Implementation

- `guppi/ledger.py`
- `.claude/settings.json`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
