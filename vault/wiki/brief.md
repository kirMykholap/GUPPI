# Brief — 2026-10-05, after the librarian run of session 2249

## Where things stand

- Session 2249 ratified Cases 675, 676, 677, 678, 679, 680, 682 (682.1, 682.2), 683 and 684 (684.1, 684.2); Case 684 supersedes Case 681 of the same session.
- Code: `guppi/ledger.py` (`unmarked_lessons`, `held_message`, the hold in `run`, the module docstring); `guppi/generate.py` (`generate.decision` leaves an archived earlier page archived; the module docstring). Tests: `tests/test_ledger.py`, 13 new and 6 changed; `tests/test_generate.py`, the archived-supersede test. Handoff: `make test` 1279 passed, 6 skipped; `make style` clean.
- Readings: L20–L24, all 5 passed. Lessons: L25 (`{addressed_by:case 684.1}`), L26.
- The yaml: 24 entries from the 26 ledger lines (L20 folded into the create of L10, L23 into the create of L17) and 4 added by the synthesis; 26 carry `applied`; 2 do not: L7 and L8 (Case 681) carry `superseded_by: '684.2'`, and L8 also `incomplete: [criterion]`; 0 `failed`, 0 `exists`, 0 `near`, 0 `merged`; `unparsed: []`.
- Pages created: decisions 14 (675, 676, 677, 678, 679, 680, 681, 682, 682.1, 682.2, 683, 684, 684.1, 684.2; 681 archived in the same run); estimates 2 (`estimate-ledger-write-asks-for-the-mark-of-a-lesson`, `estimate-orchestration-signs-items-taken-together`, both read `passed`); lessons 2 (`lesson-orchestration-parallel-cases-shown-one-by-one`, clustered and archived in the same run; `lesson-orchestration-own-text-before-a-round`, `new`); insights 1 (`insight-orchestration-items-taken-together-unruled`, by the synthesis, born `actioned`).
- Pages deleted: rules 3 (`rule-prespec-judges-the-spec-whole`, `rule-subagent-guppi`, `rule-complaint-becomes-a-lesson`).
- Pages updated: rules 4 (`rule-ledger-write`, `rule-page-generation`, `rule-decisions-schema`, `rule-orchestration` by 684.1 and 684.2); estimates 3 by decisions (Criteria replaced on `estimate-ledger-write-refuses-a-mark-with-no-decision-line`, `estimate-generate-writes-the-decision-page`, `estimate-orchestration-names-related-cases-in-the-dispatch`), all three then read `passed` (L21, L22, L24); insights 2 (`insight-harness-one-rule-implemented-twice-drifts` and `insight-hi-skill-substitution-checked-by-a-model-call`, both `actioned`, the second with its `pattern` rewritten); entities 2 (`entity-sprint-migration`, `entity-glossary`); lessons 1 by the synthesis (`lesson-orchestration-two-cases-built-side-by-side`, `clustered`, then archived); decisions: 442, 448, 469, 504, 642, 674.3 and 681 set `superseded` and archived, `decision-case-674` took the archive of its child 674.3.
- The 19 Decisions that Case 676 supersedes (cases 183 … 322) stay `archived` under `vault/archive/migration/2026-09-28/1318/decisions/`; each took `decision-case-676` into `superseded_by`; none stands under `vault/wiki/decisions/`.
- `cleanup: 14 page(s) moved`, to `vault/archive/migration/2026-10-06/2249/`: rules 3, lessons 4 (`lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases`, `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier`, `lesson-orchestration-two-cases-built-side-by-side`, `lesson-orchestration-parallel-cases-shown-one-by-one`, children of Insights set `actioned`), decisions 7.
- `generate` wrote `superseded_by` into the 0109 yaml (`'680'`, `decision-case-680`) and the 2103 yaml (`'675'`, `decision-case-675`). The scripts ticked 25 boxes of the 2249 Spec; no box of it stays open.
- The render wrote `vault/wiki/orchestration.md` and `vault/wiki/decisions/schema.yaml`; `guppi glossary` rewrote `glossary.md`; `guppi sprint` left `sprint.md` unchanged; `guppi backlog` rewrote `backlog.md`: 23 items before, 10 after. No script printed a line on stderr.
- `guppi archive` exit 0, no stderr; it moved six units — `raw/2026-10-05/0109`, `0311`, `1343`, `1616`, `1831` and `2103` — each to `archive/migration/2026-10-05/<HHMM>/raw`; it kept `raw/2026-10-05/2249`, the session of the run.
- No live page links to `rule-subagent-guppi`, `rule-complaint-becomes-a-lesson` or `rule-prespec-judges-the-spec-whole`: a Grep of the three slugs over `vault/wiki/` found them in `log.md`, in the old `brief.md` and in two History lines of `entity-sprint-migration`, as plain text.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 81 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 32 lines.
- `lesson-orchestration-parallel-cases-shown-one-by-one` — joined `lesson-orchestration-two-cases-built-side-by-side` in the new `insight-orchestration-items-taken-together-unruled`, born `actioned` with `addressed_by: decision-case-684.1`; both lessons went to the archive by the cascade.
- `lesson-orchestration-own-text-before-a-round` — none: no index line of either Grep names the main agent's own text put before a round that the check refuses; it stays `new`.

## Readings due

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method; its `- [ ] read` box stands open in the 1831 Spec, now under `vault/archive/migration/2026-10-05/1831/raw/`).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method).
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `10 items`, `## Conserved Specs` empty, 10 lines under `## Deferred`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 2249 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 14 pages from `cleanup` under `migration/2026-10-06/2249/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method).
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 12 finding lines — 1 `deferred`, 11 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1279 passed, 6 skipped, on the working tree of this run.

No Estimate stands `failed`.

## Flags

- `incomplete`: L8 of the 2249 yaml (Case 681, create `estimate-orchestration-signs-items-taken-together`) lacks `criterion`; the entry carries `superseded_by: '684.2'` and was not applied; L17 of Case 684.1 created the page with its Criterion.
- No entry marked `failed`, `near` or `unparsed`. Failed Estimates: none.
- Handoff, Direct instructions: `backlog.md` was to drop from 23 items to 15; it dropped to 10. Beyond the 3 deleted rules and the 5 plain notes of the sprint page, 5 more items left: `entity-sprint-migration`, `rule-ledger-write` and `rule-page-generation` (their defers of cases 642, 442 and 469 retired by the supersedes marks of Cases 680, 682.1 and 683), and `insight-harness-one-rule-implemented-twice-drifts` and `insight-hi-skill-substitution-checked-by-a-model-call` (set `actioned` by Cases 678 and 679).
- Handoff, Observations: `make lint` was red before the work, exit 2: 4 `deferred` and 11 `unread` lines.
- Handoff, Observations: the `ask-guppi` run of `/pre-spec` reported a Grep over `vault/wiki/` that the frame of case 633.2 forbids it; no finding rested on it.
- Handoff, Observations: the hold of Case 682.1 asks about every unmarked lesson after any decision line, so the reply that ends Retro of a session that ratified Cases is held once for each such lesson.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: none found. Contradictions: none found.
- The lint: 12 finding lines — 1 `deferred`, 11 `unread` (11 pending); no other finding; `make lint` exits red (exit 2).
- Read beyond the frame: the `status` and `superseded_by` lines of the 19 archived Decision pages under `vault/archive/migration/2026-09-28/1318/decisions/`, by a grep of their text, for the check the handoff asked in its Direct instructions (that each took `decision-case-676` and stayed archived).

## Next session

Cases:
- The rest of the backlog groups the person saw: Plan Mode and pre-spec (`rule-prespec-onward`, `insight-prespec-after-findings-loop-unruled`, `insight-case-show-built-case-retyped-by-hand`); the knowledge of the agent (`insight-session-vault-knowledge-not-loaded`, `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`); Work Mode (`rule-work-mode`, `rule-spec-box`); strategy (`entity-guppi`, `rule-morph`) (handoff, For the next session).
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint (handoff, For the next session).
- The `{addresses:...}` mark on a decision line written after an unmarked lesson stays unchecked (Case 682; handoff, For the next session).

Work:
- `estimate-hi-writes-frontier` (its `- [ ] read` box in the 1831 Spec, line 1004, archived with its unit)
- `estimate-hi-takes-a-conserved-spec`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- Ledger lines this run did not apply: L7 and L8 of the 2249 ledger (Case 681), marked `superseded_by: '684.2'`; the ledger holds 26 lines, the yaml 24 entries for them and 2 lines folded (L20, L23).

Ask the person:
- none

## Readings at the close

- `make test`: 1279 passed, 6 skipped.
- `make lint`: 12 finding lines — 1 `deferred`, 11 `unread`; red.
- Pages: decisions 1176, estimates 225, rules 75, lessons 79, insights 32, entities 4; `vault/archive/` 934 `.md` files after `guppi archive`.
