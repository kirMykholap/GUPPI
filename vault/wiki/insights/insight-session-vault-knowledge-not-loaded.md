---
type: insight
pattern: A fact the vault holds does not reach the session that needs it; only brief.md, CLAUDE.md, the skills and the agent frames are loaded, and everything else waits for a read the agent must first think to make.
status: open
children: [lesson-readings-after-librarian-invisible-to-next-hi, lesson-vault-lesson-absent-at-the-moment-it-applies]
severity: 2
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

## Children

- [[lesson-readings-after-librarian-invisible-to-next-hi]]
- [[lesson-vault-lesson-absent-at-the-moment-it-applies]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L210
