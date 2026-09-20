---
type: insight
pattern: A fact the vault holds does not reach the session that needs it; only brief.md, CLAUDE.md, the skills and the agent frames are loaded, and everything else waits for a read the agent must first think to make.
status: actioned
children: ["[[lesson-readings-after-librarian-invisible-to-next-hi]]", "[[lesson-vault-lesson-absent-at-the-moment-it-applies]]", "[[lesson-heredoc-trap-hit-twice-with-its-lesson-live]]", "[[lesson-heredoc-trap-hit-a-third-time-in-work-mode]]", "[[lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook]]", "[[lesson-spec-render-line-form-unmatched-by-the-ticker]]"]
severity: 0
addressed_by: "[[decision-case-284.1]]"
origin: raw/2026-09-12/ledger.md#L210
sprint: migration
created: 2026-09-12
tags: [harness, workflow]
---

## Pattern

Two lessons where a fact was in the record and still absent from the session that needed it.

`lesson-readings-after-librarian-invisible-to-next-hi` (session F): fourteen estimate and lesson lines written after the librarian's commit sit in the ledger; `/hi` loads `brief.md`, and `brief.md` was written before them, so the next session's Frontier does not hold them.

`lesson-vault-lesson-absent-at-the-moment-it-applies` (session K): `lesson-bash-tool-heredoc-escapes-interpreted` names the exact trap that broke a test file twice in one session; the page was in the vault the whole time and nothing put it in front of the agent.

In both, the channel into a session is a fixed set of artifacts - `CLAUDE.md`, the skills, the agent frames, `brief.md` - and a fact outside that set travels only by a read the agent must first decide to make.

## Proposal

A suggestion, not a decision. Give the session a second channel beside the brief: the unmaterialized ledger tail at `/hi` (already deferred as `rule-ledger-tail`, decision-case-79), and a way for a Rule page to name the lessons that bear on it, so the pages loaded with a phase carry the traps of that phase. Whether either belongs in the prompt or in a hook is a Case.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L210
- 2026-09-13 updated: synthesis: lesson-heredoc-trap-hit-twice-with-its-lesson-live added, the same trap with its lesson live · raw/2026-09-13/0652/ledger.md#L3
- 2026-09-14 updated: synthesis: lesson-heredoc-trap-hit-a-third-time-in-work-mode added, the same trap a third time with the Insight live · raw/2026-09-14/0747/ledger.md#L51
- 2026-09-14 updated: synthesis: lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook added, the same trap a fourth time, in the session that ratified the hook against it · raw/2026-09-14/1029/ledger.md#L39
- 2026-09-14 updated: actioned: the ledger tail (rule-ledger-tail, 101.2) answers the first child, the bash guard (rule-bash-guard, 127) the four heredoc children; a lessons list on a Rule page rejected — a text to remember is the channel that failed (case 134) · [[decision-case-134]]
- 2026-09-20 updated: synthesis: lesson-spec-render-line-form-unmatched-by-the-ticker added, the form of a render line held in rule-render-harness (case 235) and in no text the Spec is written from; reopened from actioned · raw/2026-09-20/1749/ledger.md#L8
- 2026-09-21 updated: actioned: the sixth child, the form of a render line, closed in its own session by 279.1 (the form in the schema /hi loads) and 279.2 (pre-spec refuses a line of another form); the Proposal's first half done by 101.2, its second rejected by 134 (case 284.1) · [[decision-case-284.1]]
