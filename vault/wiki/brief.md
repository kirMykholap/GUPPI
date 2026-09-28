# Brief — 2026-09-28, the librarian's run over session 0000 of 2026-09-28

## Where things stand

- Session 0000 ratified Cases 470, 472.1, 472.2, 472.3, 473.1, 473.2, 474.1, 474.2 and 475 (a short defer of `rule-spec-write`). Case 471, 471.1 and 471.2 were ratified and then superseded by 474.1 and 474.2 (handoff).
- Code, commit 0bdffcc: `guppi/prespec.py` and `guppi/casecheck.py`, with tests in `tests/test_prespec.py` and `tests/test_casecheck.py`. The session's `make test` gave 856 passed, 2 skipped; `make style` clean (handoff).
- Readings of the session: `estimate-case-check-requires-a-backlog-item-decided-on-its-page` and `estimate-case-protocol-shows-the-built-case` `passed`; `estimate-language-followed` and `estimate-agent-writing-followed` `failed`. Two lessons: `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent` and `lesson-chat-language-follows-the-last-english-file-read` (handoff).
- Not done in the session: the Spec hook keeps the body of a Case rebuilt as a parent, deferred as Case 475; the unclear Criterion line of `estimate-sprint-migration-file-route-gone`; 17 Estimates not read, each with its reason in the handoff (handoff).
- The walk named `raw/2026-09-27/1255/`, `1819/` and `2050/` (each extended with 0 entries; `generate` 0 pages each), and `raw/2026-09-28/0000/` (written with 35 entries from the 35 lines of its ledger).
- Yaml of 0000: 35 entries: 24 `update`, 4 `create` (lines 7, 10, 16, 19, all Estimates), 4 `estimate`, 2 `lesson` (lines 25, 33), 1 `defer` (line 35, `exists`). 28 are `applied`. 7 are `superseded_by` and not applied: lines 2, 3, 4, 20, 21, 22 (by 474.1) and 23 (by 474.2). The librarian added 3 entries by synthesis, all `applied`. No `near`, no `merged`, no `failed`, `unparsed: []`.
- Pages (`generate`: 46 pages written or changed; `cleanup`: 10 pages moved):
  - decisions: 12 created (470, 471, 471.1, 471.2, 472.1, 472.2, 472.3, 473.1, 473.2, 474.1, 474.2, 475). 4 archived as superseded: 471, 471.1, 471.2 (by 474.1 and 474.2) and 238 (by 473.2).
  - estimates: 4 created, `pending`: `estimate-case-check-notes-a-criterion-line-not-carried` (472.1), `estimate-case-check-notes-a-then-line-shared-by-siblings` (472.2), `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` (473.1), `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (473.2). 4 updated by Cases, all `pending`: `estimate-skill-grill-me-asks-in-rounds` (470), `estimate-prespec-checks-the-form-of-an-item` (472.3, from `passed`), `estimate-documentation-completes` (474.1, from `failed`), `estimate-synthesis-clusters` (474.2, from `passed`). 4 updated by readings: 2 `passed`, 2 `failed`.
  - rules: 8 updated by Cases: `rule-case-check` (472.1, 472.2), `rule-prespec` (472.1, 472.2, 472.3), `rule-materialize` (472.3), `rule-atomicity` (472.3), `rule-retro` (473.1), `rule-case-build` (473.2), `rule-documentation` (474.1), `rule-synthesis` (474.1). `rule-spec-write` deferred by 475 (`deferred_by: [[decision-case-475]]`). Cascade built → draft: `rule-synthesis`.
  - lessons: 2 created: `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent` (`new`) and `lesson-chat-language-follows-the-last-english-file-read` (`clustered`). 1 updated by synthesis: `lesson-retro-answered-in-the-skills-language` → `clustered`. 6 archived because their Insight went `actioned`: `lesson-case-build-a-criterion-replaced-whole-drops-a-line`, `lesson-case-build-one-promise-signed-in-two-sub-cases`, `lesson-case-build-two-promises-in-one-sub-case-with-a-written-criterion`, `lesson-case-build-a-rewritten-criterion-loses-a-finding-text`, `lesson-reader-changed-before-its-writer-closed-the-live-session`, `lesson-work-mode-check-reads-a-page-the-same-spec-changes`.
  - insights: 1 created by synthesis, `open`, severity 2: `insight-session-reply-language-follows-the-english-text-read`. 2 updated to `actioned`: `insight-case-build-promise-lines-compared-by-no-check` (`addressed_by` 472.3), `insight-workflow-code-live-before-the-page-it-reads` (`addressed_by` 473.2; `deferred_by` 238 cleared).
- Governed files `render` rewrote: `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`. `guppi sprint` left `vault/wiki/sprint.md` unchanged. `guppi backlog` rewrote `vault/wiki/backlog.md`: 17 items, as before. It removed the two `actioned` Insights. It added `rule-spec-write` and `insight-session-reply-language-follows-the-english-text-read`, each put off in 0 sessions. `guppi glossary` left `vault/wiki/glossary.md` unchanged.
- `generate` ticked 27 lines of `raw/2026-09-28/0000/spec.md`, 2 of `archive/migration/2026-09-27/2050/raw/spec.md`, 1 of `archive/migration/2026-09-27/1819/raw/spec.md` and 3 of `archive/migration/2026-09-27/1255/raw/spec.md`.

## Readings due

28 Estimates stand `pending` or `failed` after `generate`: 2 `failed`, 26 `pending`. Every rule or entity they read stands `draft`.

- `estimate-language-followed` — `failed` — `rule-language` draft — by hand in the next session (method). Result: the reply that acknowledged Case 471 was written in English in the chat, and the person asked why.
- `estimate-agent-writing-followed` — `failed` — `rule-agent-writing` draft — by hand in a later session, the person's messages of one session (method). Result: the person asked three times for a plain explanation of the agent's text, on the rounds of 472 and 473.
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` draft — `raw/2026-09-28/0000/spec.md` line 46.
- `estimate-case-check-notes-a-criterion-line-not-carried` — `rule-case-check` draft — `raw/2026-09-28/0000/spec.md` line 123.
- `estimate-case-check-notes-a-then-line-shared-by-siblings` — `rule-case-check` draft — `raw/2026-09-28/0000/spec.md` line 181.
- `estimate-prespec-checks-the-form-of-an-item` — `rule-prespec` draft — `raw/2026-09-28/0000/spec.md` line 246.
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` draft — `raw/2026-09-28/0000/spec.md` line 303.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` draft — `raw/2026-09-28/0000/spec.md` line 355.
- `estimate-documentation-completes` — `rule-documentation` draft — `raw/2026-09-28/0000/spec.md` line 468.
- `estimate-synthesis-clusters` — `rule-synthesis` draft — `raw/2026-09-28/0000/spec.md` line 504.
- `estimate-sprint-migration-file-route-gone` — `entity-sprint-migration` draft — `archive/migration/2026-09-27/2050/raw/spec.md` line 53.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `archive/migration/2026-09-27/2050/raw/spec.md` line 154.
- `estimate-prespec-requires-a-backlog-item-decided-on-its-page` — `rule-prespec` draft — `archive/migration/2026-09-27/2050/raw/spec.md` line 281.
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` draft — `archive/migration/2026-09-27/2050/raw/spec.md` line 382.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — `archive/migration/2026-09-27/2050/raw/spec.md` line 440.
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` draft — `archive/migration/2026-09-27/2050/raw/spec.md` line 490.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — `archive/migration/2026-09-27/1819/raw/spec.md` line 396.
- `estimate-carry-over-writes` — `rule-carry-over` draft — `archive/migration/2026-09-27/1255/raw/spec.md` line 595.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `archive/migration/2026-09-27/1255/raw/spec.md` line 895.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `archive/migration/2026-09-27/1255/raw/spec.md` line 944.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-event-log-records` — `rule-event-log` draft — pytest in `tests/test_event.py` and `tests/test_gate.py`; readings by hand (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).

## Flags

- `incomplete` (`criterion`): lines 4 and 22 (`estimate-documentation-completes`, Cases 471 and 471.1) and line 23 (`estimate-synthesis-clusters`, Case 471.2). All three are `superseded_by` and were not applied; 474.1 and 474.2 wrote the Criterion of both pages.
- `failed`, `near`, `merged`, `unparsed`: none in the yamls of 1255, 1819, 2050 and 0000.
- `exists`: line 35 (Case 475, `defer` of `rule-spec-write`); the page stood, no page written; the defer applied.
- Superseded: the 7 entries of Cases 471, 471.1 and 471.2 were not applied. Their Decision pages were written and archived by `cleanup`. The handoff says these lines need no page beyond what `generate` does with a superseded Case, and that `cases/case-471.md` stays in the session folder.
- Synthesis: `lesson-chat-language-follows-the-last-english-file-read` and `lesson-retro-answered-in-the-skills-language` share one cause. They gave `insight-session-reply-language-follows-the-english-text-read` (`open`), and both lessons are `clustered`. `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent` has no pair among the lessons and the Insights and stays `new`. Its cause is the subject of the defer 475.
- Failed Estimates: 2, listed first under Readings due.
- Handoff: the person asked for a plain explanation three times, all on the rounds of case-guppi. Twice the agent gave it in its own words, without case-guppi. The handoff names this as a signal for `rule-case-build` and `rule-agent-writing`.
- Handoff: the sentence on a red check stands in `rule-retro` for now. The person wants to decide where it belongs when `rule-work-mode` is taken up.
- Handoff: the notes of 472 use a threshold of 60 percent of shared words. Nobody measured it, and the person accepted it as it is.
- Handoff: the notes of 472 are loud on a real plan. `guppi prespec --check` printed 19 notes on this session's Spec. The handoff asks the first reading of the note Estimates to judge whether that many is workable.
- Handoff: the person edited `cases/case-471.md` by hand at its first showing and put it back. Its code spans lost their padding. The Spec was written from the stored answer and was not affected.
- Handoff: the `rule-atomicity` line of 472.3 stands among the re-ratification lines of 03:31:13 in the ledger. It applied (line 24). The anchors of 472.1, 472.2 and 472.3 on `rule-prespec` and of 472.1 and 472.2 on `rule-case-check` all applied.
- Handoff: `make lint` stopped at `backlog --check` in Work Mode (case 473.1). After `guppi backlog` ran, `backlog --check` passed; lint now stops at `guppi lint`.
- Contradictions: none found in this run. The unclear Criterion line of `estimate-sprint-migration-file-route-gone` is under Next session, from the handoff.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-work-mode` deferred 32 times since case 29; `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines.
- `archive` (run after the brief): exit 0, no stderr line. It moved `raw/2026-09-27/1255`, `1819` and `2050` to `archive/migration/2026-09-27/<HHMM>/raw`; the Spec paths of this brief name them there. It kept `raw/2026-09-28/0000/`, the session of the run.
- `make lint`, after the render: exit 2, 98 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 32 times since case 29`.
  - `unread: pending` on 26 Estimates and `unread: failed` on 2. These are the 28 Estimates of Readings due.
  - `estimates: unmigrated: 18 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-language-followed` failed: an English reply in the chat on Case 471. Its lesson is clustered under `insight-session-reply-language-follows-the-english-text-read` (handoff, synthesis).
- `estimate-agent-writing-followed` failed: three requests for a plain explanation on the rounds of 472 and 473. The handoff names it as a signal for `rule-case-build` and `rule-agent-writing` (handoff).
- `estimate-sprint-migration-file-route-gone`: its Criterion line "`make lint` has no finding on a schema" has two readings. As "no `schema:` finding" it fails on 64 findings today; as "no finding on a schema page" it passes. The handoff leaves this question for the next Plan Mode (handoff).
- Where the sentence on a red check belongs, `rule-retro` or `rule-work-mode`: the person decides when `rule-work-mode` is taken up (handoff).

Work:
- `estimate-skill-grill-me-asks-in-rounds`
- `estimate-case-check-notes-a-criterion-line-not-carried`
- `estimate-case-check-notes-a-then-line-shared-by-siblings`
- `estimate-prespec-checks-the-form-of-an-item`
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
- `estimate-documentation-completes`
- `estimate-synthesis-clusters`
- `estimate-sprint-migration-file-route-gone`
- `estimate-case-build-writes-the-case`
- `estimate-prespec-requires-a-backlog-item-decided-on-its-page`
- `estimate-generate-writes-the-decision-page`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-handoff-holds-each-fact-once`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-carry-over-writes`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit`
- `estimate-event-log-records`
- `estimate-session-phases-in-order`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- The unticked boxes of the Specs, all `read` lines: `raw/2026-09-28/0000/spec.md` lines 46, 123, 181, 246, 303, 355, 468, 504; `archive/migration/2026-09-27/2050/raw/spec.md` lines 53, 154, 281, 382, 440, 490; `archive/migration/2026-09-27/1819/raw/spec.md` line 396; `archive/migration/2026-09-27/1255/raw/spec.md` lines 595, 895, 944.
- Ledger lines not applied: lines 2–4 and 20–23 of `raw/2026-09-28/0000/ledger.md`, superseded by 474.1 and 474.2. Each of the other 28 of its 35 lines has an applied entry.
- Dirty tree: none after the librarian's commit.

## Readings at the close

- `make test`: 856 passed, 2 skipped.
- `make lint`: exit 2, 98 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 684, estimates 149, rules 68, lessons 58, insights 26, entities 4.
