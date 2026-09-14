---
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
status: built
enforcement: hook
implementation_ref: [guppi/ledger.py, guppi/gate.py, tests/test_gate.py, .claude/settings.json]
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
(measured 2026-08-29). Reads every assistant message of this session from `transcript_path`, in order,
falling back to the reply that just finished (`last_assistant_message`) when the
transcript is absent or unreadable, and finds every line that starts with `- decision[`,
`- estimate[` or `- lesson[` **inside a fenced block opened with the `LEDGER` tag** (```` ```LEDGER ````, any case) and appends them to
`vault/raw/<hi date>/<hi HHMM>/ledger.md` — the session's folder, the same across midnight (case 103.1) — interpreting nothing: the text verbatim, the time of writing
between the dash and the text — `- HH:MM:SS decision[...]`, the date being the folder's.
A line anywhere else — bare, or in a block with no tag or another one — is a preview: a
Case's `then` shows lines before they are ratified. The tagged block is what the chat
renders highlighted, so the person sees at a glance what is being recorded. The ledger is
not created at session start; it comes into existence with the first line.

**Checks the event log first.** The log it reads is `raw/<date>/event_log.md` of every
date from today back to the first that holds a `session-start` of this session, joined in
date order; a session that crosses midnight keeps its window. The session is a working one when a `hi` line of this session's id follows its first `session-start` line in the logs walked (case 111.3); the session's folder is the first such `hi`. A `session-start` of another session, before or after, changes nothing; a `hi` with another id does not count. With no stamped `hi` in the logs walked, a `--------` `hi` counts by the rule before 111.3 — after a `session-start` of this session with no other session's start in between — for the sessions the old skill line opened (case 111.6). `compact` and `resume` of the same session do not close the window — `SessionStart` fires on both, and neither changes the person, the branch or the agenda (case 14). When the check fails and there are lines to write, the hook exits 2 with the reason on
stderr — `ledger: N line(s) not written — no /hi recorded for session X. Tell the person;
run /hi, then repeat the lines.` — so the person is told rather than left believing their
decisions were recorded. With `stop_hook_active` set (the re-fire after a block) it exits 0
and writes nothing, so it cannot loop.

A reply that ends in a tool call (`Skill`, `ExitPlanMode`) has no `Stop` of its own, and the text before the call is never kept: not in the transcript, not in `last_assistant_message` (measured in sessions L and N). The harness holds the reply back instead of the agent's memory: `guppi gate` on `PreToolUse Skill` reads the `then` items of every Case in the session's `spec.md` and in the plan file the session's event log names last under `.claude/plans/`, and the decision lines of the session's window as `guppi pretask --check` reads them; an item with no decision line of its Case refuses the call with exit 2 — `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B). The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply.` — and every item with its line, or no source found, passes silently (case 122). `estimate[...]` and `lesson[...]` lines have no source but the text; a loss of one is a Retro finding. A block the agent repeats in a later text reaches the ledger at that `Stop`, with that time; only the last reply of a session can still be lost, and Retro sees it. A line whose text is already
in today's ledger — whatever its time, or with none, as the
hand-written lines of 2026-09-09 have none — is not appended again: this covers the hook
running twice on one reply and the agent repeating a line in a later reply. A hook-written
line is told from a hand-written one by its time.

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
- 2026-09-09 updated: records are the lines of a LEDGER block, not bare lines · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 updated: each written line carries the time of writing · raw/2026-09-09/ledger.md#case-15.3
- 2026-09-09 updated: compact and resume of the same session keep the hi window open · raw/2026-09-09/ledger.md#case-14
- 2026-09-10 status: draft → built · cascade
- 2026-09-10 deferred · raw/2026-09-10/ledger.md#case-51
- 2026-09-11 deferred_by decision-case-51 set · [[decision-case-52.3]]
- 2026-09-11 defer by decision-case-51 superseded · [[decision-case-55.1]]
- 2026-09-11 updated: the hi window spans the dates of the session: the event logs back to its start are joined · [[decision-case-55.1]]
- 2026-09-11 updated: the hi window spans the dates of the session; every LEDGER block of the session's transcript is read at each Stop, the last reply as fallback · [[decision-case-55.2]]
- 2026-09-13 updated: the lines go to the session folder raw/<hi date>/<hi HHMM>/ledger.md; the dedupe reads every ledger under raw/ (case 103.1) · [[decision-case-103.1]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: the window is the session's own stamped hi after its first start; a foreign start no longer closes it (case 111.3) · [[decision-case-111.3]]
- 2026-09-14 deferred · [[decision-case-117]]
- 2026-09-14 updated: an unstamped hi keeps its window by the old rule while no stamped hi exists (case 111.6) · [[decision-case-111.6]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 defer by decision-case-117 superseded · [[decision-case-122]]
- 2026-09-14 updated: guppi gate refuses a Skill call while a then item of the session's Spec or plan file has no decision line in the ledger; the text before a tool call is never kept (case 122) · [[decision-case-122]]
- 2026-09-14 status: draft → built · cascade
