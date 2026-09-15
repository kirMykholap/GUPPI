---
type: insight
pattern: The event log ties a hi line to its session by the session-start lines around it, not by an id; any start that is missing from the window or added to it sends the hi to the wrong session and the ledger writer refuses.
status: actioned
children: ["[[lesson-ledger-hook-hi-lost-at-midnight]]", "[[lesson-hi-taken-by-a-session-started-in-the-same-second]]", "[[lesson-pretask-line-unstamped-and-bound-by-position]]"]
severity: 0
addressed_by: "[[decision-case-136.4]]"
origin: raw/2026-09-14/0747/ledger.md#L2
sprint: migration
created: 2026-09-14
tags: [harness, hooks, ledger]
---

## Pattern

Two lessons on one binding.

`lesson-ledger-hook-hi-lost-at-midnight` (session H): the session crossed midnight; the
hook read the log of the new day only, found a `hi` with no session-start of its own
session before it, and refused 44 lines with "no /hi recorded".

`lesson-hi-taken-by-a-session-started-in-the-same-second` (session M): a second session,
started by `resume` in the same second, put its session-start between this session's
start and the `hi`; the `hi` went to the other session and the first ledger line was
refused with the same message.

In both, the `hi` line carries no session id (`CLAUDE_SESSION_ID` is empty in the skill's
shell), so `hi_recorded` binds it by position among the session-start lines of the log. A
start out of the window, or a stranger's start inside it, breaks the binding the same
way.

## Proposal

A suggestion, not a decision. Case 111 (111.1, 111.3, 111.6) already writes a stamped
`<stamp> hi` line from the `UserPromptSubmit` hook, which carries the session id, and
reads the window by that stamp with the old rule as a fallback. The readings of
`estimate-event-log-records` and `estimate-ledger-write-lifts` at the next `/hi` decide
whether the binding by position can be retired; if the hook does not fire on a slash
command, the fallback keeps both lessons live and a Case on 111.4 is due.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#L2
- 2026-09-14 updated: synthesis: lesson-pretask-line-unstamped-and-bound-by-position added, the pretask line is bound to its session by position as the hi was, no session id in the skill shell · raw/2026-09-14/1029/ledger.md#L40
- 2026-09-14 updated: actioned: the hi is stamped by 111, the marks pretask/retro/handoff by guppi gate (136.1), pretask.window and the ledger window read by stamp only (136.2, 136.3) (case 136.4) · [[decision-case-136.4]]
