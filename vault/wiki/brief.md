# Brief — 2026-10-08, after the librarian run of session 2134

## Where things stand

- Session 2134 ratified Cases 738, 739 (739.1, 739.2), 740, 741 and 742. None is superseded (handoff, What actually got done).
- Code: `guppi/lint.py` and `guppi/prespec.py` (the patch of Case 733: `names_a_moc_form`, `check_form` by `plan_kind`); `guppi/generate.py` (`archived_by_cascade`, which `cascade` calls); `guppi/prespec.py` (`cascade_notes` in the notes of `plan_findings`); `guppi/casecheck.py` (`check_answer` adds the cascade notes). Tests: `tests/test_prespec.py`, `tests/test_casecheck.py`. Handoff: `make test` 1448 passed, 6 skipped; `make style` clean.
- Readings of the session: L10 `estimate-prespec-catches-a-method-without-a-form` `passed` (was `failed`), L11 `estimate-prespec-notes-a-page-the-cascade-archives` `passed` (folded into the `create` of line 2), L12 `estimate-case-check-notes-a-page-the-cascade-archives` `passed` (folded into the `create` of line 3), L13 `estimate-where-to-stop-stops-only-on-its-conditions` `passed`. No lesson.
- The ledger: 13 lines. The yaml: 11 entries (2 `create`, 7 `update`, 2 `estimate`) for lines 1–10 and 13; lines 11 and 12 are folded into the entries of lines 2 and 3, so every ledger line is accounted for. 11 entries and 7 decision records carry `applied`; 0 `failed`, 0 `exists`, 0 `incomplete`, 0 `near`, 0 `merged`; `unparsed: []`. No `new_tags`.
- Pages created: decisions 7 (738, 739, 739.1, 739.2, 740, 741, 742); estimates 2 (`estimate-prespec-notes-a-page-the-cascade-archives`, `estimate-case-check-notes-a-page-the-cascade-archives`, each then `passed`).
- Pages updated: rules 3 (`rule-prespec` — History line by 738, the new Estimate by 739.1, then `draft` → `built` by the cascade; `rule-case-check` — one sentence in its Purpose and the new Estimate by 739.2, stays `built`; `rule-where-to-stop` — condition 8 by 741); estimates 2 (`estimate-prespec-catches-a-method-without-a-form` `failed` → `passed` (L10); `estimate-where-to-stop-stops-only-on-its-conditions` — Criterion replaced by 741, `pending`, then `passed` (L13)); insights 3, each set `actioned`, severity → 0 (`insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` by 740, `insight-permissions-classifier-weighs-the-rules-not-the-persons-word` by 741, `insight-ledger-ratified-line-never-withdrawn` by 742).
- Lessons archived by the cascade of the three `actioned` Insights, moved by `cleanup` (`cleanup: 6 page(s) moved`) to `vault/archive/migration/2026-10-08/2134/lessons/`: `lesson-prespec-parent-of-superseded-sub-cases`, `lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped`, `lesson-case-check-refuses-a-rebuild-under-a-new-number`, `lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat`, `lesson-permissions-auto-mode-refuses-editing-the-case-check-store`, `lesson-case-build-splits-a-ratified-leaf-case`.
- The handoff's Direct instructions, as the run left them: 3 lessons archived under `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line`, 2 under `insight-permissions-classifier-weighs-the-rules-not-the-persons-word`, 1 under `insight-ledger-ratified-line-never-withdrawn`; `backlog.md` no longer lists the three Insights (9 items → 6). `addressed_by` on the pages: `"[[decision-case-725.2]]"` (740), `"[[decision-case-725.1]]"` (742, was `"[[decision-case-671.1]]"`), `"[[decision-case-741]]"` (741; the yaml carried the bare slug, the page holds the quoted wikilink). `estimate-where-to-stop-stops-only-on-its-conditions` ends `passed` with the new Criterion. `rule-case-check` ends `built`; `log.md` holds no status line for it in this run. `vault/wiki/where-to-stop.md` holds condition 8; the Purpose of `rule-case-check` holds the sentence of case 739.2.
- The scripts ticked all 14 boxes of the 2134 Spec; none stays open. No unticked line of the 2134 Spec holds `guppi sprint-close`; none ran.
- `guppi materialize` named the 0050, 0213 and 1547 yamls of 2026-10-08 ("extended with 0 entries"); `generate` wrote 0 pages from each and 23 from the 2134 yaml.
- `render` wrote `vault/wiki/where-to-stop.md`. `guppi sprint` left `sprint.md` unchanged; `guppi backlog` rewrote `backlog.md` (9 items → 6: the three Insights left; `rule-sprint-close` put off in 25 sessions, was 24); `guppi glossary` left `glossary.md` unchanged. The run added 35 lines to `log.md`. `generate`, `cleanup`, `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- `guppi archive` exit 0, no stdout, no stderr; it moved nothing and printed no unit kept.
- Index check: no `create` entry other than an Estimate, so no index Grep ran.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 80 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 36 lines (both run before `generate`). The yaml holds no `lesson` entry, so no lesson was compared and no entry was added.

## Readings due

Failed: none.

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: no unticked `read` line in the 2134 Spec; the method: by hand, the person's answer at the `/hi` of the session after the close of a sprint, written into the estimate line; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run, sections Where things stand, Readings due, Flags, Next session, Readings at the close.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `6 items`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 2134 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 6 pages from `cleanup` under `migration/2026-10-08/2134/lessons/`; `guppi archive` exit 0, no stdout line, nothing moved.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 11 finding lines — 1 `deferred`, 10 `unread: pending`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run (method). This run: `make test` 1448 passed, 6 skipped, on the working tree of this run.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`; no `exists`, no `merged`.
- Failed Estimates: none.
- Handoff, Notes from memory: both items of Slice 5, `rule-sprint-close` and the close of `migration`, were closed `· sprint · defer`: once a Case not about the close was ratified, this session could not be the session that closes the sprint.
- Handoff, Notes from memory: on Case 739 the person answered the first question outside its options (a check by script that reuses the logic of the cascade) and chose (b) against the recommendation on a Case that both sets the status and updates the page.
- Handoff, Notes from memory: the four unticked code boxes of Case 733 in the 0213 Spec stay as that session left them (Case 738); the code landed in the 2134 boxes.
- Handoff, Notes from memory: `ask-guppi` made 3 findings on Cases 738 and 739 at `/pre-spec`, all fixed and confirmed closed; 738 and 739 were ratified a second time.
- Handoff, Observations: `make lint` was red before the work, exit 2, 13 finding lines, among them `backlog: vault/wiki/backlog.md differs from its sources`; that line is not in the lint output of this run.
- Handoff, Observations: Work Mode changed `guppi/generate.py` once through a Python script in the shell; the `shellwrite` hook turned its CRLF line endings into LF.
- Contradictions: none found by this run.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: the lint names none.
- The lint: 11 finding lines — 1 `deferred` (`rules/rule-morph`), 10 `unread: pending`; `make lint` exit 2.

## Next session

Cases:
- The close of `migration` and `rule-sprint-close`: a session of its own, put off again (handoff, For the next session).
- `rules/rule-morph: deferred` stays a lint finding until a Case decides `rule-morph` (handoff, For the next session).

Work:
- `estimate-hi-takes-a-conserved-spec`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- The 4 unticked code boxes of Case 733 in `vault/raw/2026-10-08/0213/spec.md` (`guppi/lint.py`, `guppi/prespec.py`, `tests/test_prespec.py`, `tests/test_lint.py`); Case 738 keeps them unticked, the code landed in the 2134 boxes.

Ask the person:
- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?

## Readings at the close

- `make test`: 1448 passed, 6 skipped.
- `make lint`: 11 finding lines — 1 `deferred`, 10 `unread: pending`; exit 2.
- Pages under `vault/wiki/`: rules 77, estimates 250, insights 36, lessons 74, decisions 1302, entities 4.
