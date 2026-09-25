---
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
status: draft
enforcement: hook
implementation_ref: [guppi/ledger.py, guppi/materialize.py, guppi/gate.py, tests/test_ledger.py, tests/test_gate.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-ledger-write-lifts]]", "[[estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session]]"]
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## Purpose

Prevents a ratified line from existing only in a chat reply, or landing in a session no
`/hi` opened. The instruction to write `- decision[...]`, `- estimate[...]` and
`- lesson[...]` lines lives in `case-schema.md`, the Render of `rule-case-protocol` that `/hi` loads (case 273), so a session without `/hi` produces none — and would produce them in *any* session
if the instruction stood in `CLAUDE.md` again, including one with no sprint, no branch context and no brief. Without this hook's check the
ledger would silently gain a session that was never a working session, and the librarian
would materialize pages from it the next day.

## How it works

`uv run guppi ledger` on `Stop` — not `MessageDisplay`, which can neither block nor speak
(measured 2026-08-29). Reads every assistant message of this session from `transcript_path`, in order,
falling back to the reply that just finished (`last_assistant_message`) when the
transcript is absent or unreadable, and finds every line that starts with `- decision[`,
`- estimate[` or `- lesson[` **inside a fenced block opened with the `LEDGER` tag** (```` ```LEDGER ````, any case) and appends them to
`vault/raw/<hi date>/<hi HHMM>/ledger.md` — the session's folder, the same across midnight (case 103.1) — the text verbatim, the time of writing
between the dash and the text — `- HH:MM:SS decision[...]`, the date being the folder's.
A line anywhere else — bare, or in a block with no tag or another one — is a preview: a
Case's `then` shows lines before they are ratified. The tagged block is what the chat
renders highlighted, so the person sees at a glance what is being recorded. The ledger is
not created at session start; it comes into existence with the first line.

**Checks the event log first.** The log it reads is `raw/<date>/event_log.md` of every
date from today back to the first that holds a `session-start` of this session, joined in
date order; a session that crosses midnight keeps its window. The session is a working one when a `hi` line of this session's id follows its first `session-start` line in the logs walked (case 111.3); the session's folder is the first such `hi`. A `session-start` of another session, before or after, changes nothing; a `hi` with another id does not count. A `--------` `hi` never counts: the fallback by position of case 111.6 was removed once every session opened before the stamped `hi` had closed (case 136.3).  `compact` and `resume` of the same session do not close the window — `SessionStart` fires on both, and neither changes the person, the branch or the agenda (case 14). When the check fails and there are lines to write, the hook exits 2 with the reason on
stderr — `ledger: N line(s) not written — no /hi recorded for session X. Tell the person;
run /hi, then repeat the lines.` — so the person is told rather than left believing their
decisions were recorded. With `stop_hook_active` set (the re-fire after a block) it exits 0
and writes nothing, so it cannot loop.

**What a session changes, it does not measure** (case 428.1). An `estimate[<slug>]` line is not written when a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines of the same `Stop`, each line read by `parse_line` of `guppi/materialize.py`; a reading of the old slug of a page an `update` renames falls under the same rule, since the decision line names the old slug. The reading waits for a later session. The judgment reads the ledger alone and holds the whole session, so a refused line of the transcript is refused again at every `Stop`: the hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, and skips an older one without a word. A reading of the new slug of a rename is not caught here: no decision line names it.

A reply that ends in a tool call (`Skill`, `ExitPlanMode`) has no `Stop` of its own. The text before the call is kept in the transcript — measured on Claude Code 2.1.269–2.1.272: the blocks of cases 101, 117 and 222 stood in a text followed by a tool call and reached the ledger at the next `Stop` of the session, 22 minutes, 13 seconds and 14 seconds later; one block, case 109 on 2.1.269, was absent from the transcript and is not explained (case 224.1). A block followed by a tool call waits for the next `Stop`; the reply that ends in the text lands it now, with its own time. The harness holds the reply back instead of the agent's memory: `guppi gate` — on `PreToolUse Skill` for the agent's call, on `UserPromptSubmit` for a typed `/pre-spec`, `/retro` or `/handoff` (case 169.1) — reads the `then` items of every Case in the session's `spec.md` and in the plan file the session's event log names last under `.claude/plans/`, and the decision lines of the session's window as `guppi prespec --check` reads them; an item with no decision line of its Case refuses the call with exit 2 — `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B).` followed by the advice of the path: to the agent `The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply.`, to the person `Ask the agent to end its reply with the LEDGER block, then type /<skill> again.` (case 174) — and every item with its line, or no source found, passes silently (case 122) — except a `/retro` with no source and no `decision`, `estimate` or `lesson` line in the session's ledger window, which `rule-retro-commit` refuses as nothing to review (case 180; case 184). `estimate[...]` and `lesson[...]` lines have no source but the text; a loss of one is a Retro finding. A block the agent repeats in a later text reaches the ledger at that `Stop`, with that time; only the last reply of a session can still be lost, and Retro sees it. A line whose text is already
in today's ledger — whatever its time, or with none, as the
hand-written lines of 2026-09-09 have none — is not appended again: this covers the hook
running twice on one reply and the agent repeating a line in a later reply. A hook-written
line is told from a hand-written one by its time.

Which field carries the reply is measured by the Slice 1 probe before this hook is written;
the implementation arrives in the session after the probe (Slice 1, session B).

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
- 2026-09-14 updated: the fallback of 111.6 — an unstamped hi bound by position — removed; a hi of the session's stamp is the one way to open the window (case 136.3) · [[decision-case-136.3]]
- 2026-09-15 updated: the Spec check of 122 names the second entry of the gate, the typed command (case 169.1) · [[decision-case-169.1]]
- 2026-09-15 updated: the refusal on an unwritten ledger line quoted with both advices, the agent's and the person's (case 174) · [[decision-case-174]]
- 2026-09-16 updated: the pass on "no source found" of 122 narrowed — a /retro with no source and no ledger line is refused by rule-retro-commit (case 180) · [[decision-case-184]]
- 2026-09-18 updated: the text before a tool call is kept in the transcript and read at the next Stop; the gate's advice says so (case 224.1) · [[decision-case-224.1]]
- 2026-09-20 updated: the ledger instruction lives in the Case schema loaded by /hi, not in CLAUDE.md (case 277.2) · [[decision-case-277.2]]
- 2026-09-25 updated: the hook refuses a reading of an Estimate that a decision line of the session creates or updates (case 428.1) · [[decision-case-428.1]]
- 2026-09-25 estimate estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session added · [[decision-case-428.1]]
- 2026-09-25 status: built → draft · cascade
