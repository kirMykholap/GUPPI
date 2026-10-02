---
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
status: draft
enforcement: hook
implementation_ref: [guppi/ledger.py, guppi/materialize.py, guppi/gate.py, tests/test_ledger.py, tests/test_gate.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-ledger-write-lifts]]", "[[estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session]]", "[[estimate-ledger-write-refuses-a-lesson-without-its-prefix]]", "[[estimate-ledger-write-refuses-a-mark-with-no-decision-line]]", "[[estimate-ledger-write-refuses-a-line-it-cannot-read]]", "[[estimate-ledger-write-exits-2-on-an-error]]"]
deferred_by: ["[[decision-case-442]]"]
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
- 2026-09-26 deferred · [[decision-case-442]]
- 2026-09-26 status: draft → built · cascade
- 2026-09-27 estimate estimate-ledger-write-refuses-a-lesson-without-its-prefix added · [[decision-case-460.5]]
- 2026-09-27 updated: the ledger hook refuses a lesson line whose slug lacks lesson- (case 460.5) · [[decision-case-460.5]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-09-29 updated: the ledger hook refuses a lesson line whose {addressed_by:case N} has no decision line of Case N before it (case 497.1) · [[decision-case-497.1]]
- 2026-09-29 estimate estimate-ledger-write-refuses-a-mark-with-no-decision-line added · [[decision-case-497.1]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: the hook refuses a line that parse_line cannot read (case 552.2) · [[decision-case-552.2]]
- 2026-09-30 estimate estimate-ledger-write-refuses-a-line-it-cannot-read added · [[decision-case-552.2]]
- 2026-09-30 updated: the hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 552.4) · [[decision-case-552.4]]
- 2026-09-30 estimate estimate-ledger-write-exits-2-on-an-error added · [[decision-case-552.4]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 status: draft → built · cascade
- 2026-10-01 updated: the hook writes whatever stop_hook_active says; each refused line is told once a stretch, and no hi and its own error once a stretch, judged by its own refusals in the transcript (case 577.3) · [[decision-case-577.3]]
- 2026-10-01 updated: an error of the hook comes back at the first Stop of each stretch; an error while it reads the payload exits 0, since the hook cannot tell its own refusal then (case 577.4) · [[decision-case-577.4]]
- 2026-10-01 status: built → draft · cascade
