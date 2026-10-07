# Brief — 2026-10-07, after the librarian run of session 0636

## Where things stand

- Session 0636 ratified Cases 703 (703.1–703.3), 704, 705 (705.1, 705.2), 706, 710 (710.1, 710.2) and 711 (711.1–711.4). Cases 707, 708 and 709 were dropped with their files emptied; none has a decision line (handoff, What actually got done).
- Code: `guppi/tags.py` (new: `registered_tags`, `declared_tags`, `ratified_tags`); `guppi/casecheck.py` (`unlisted_tags`, `read_outputs`, `unread_sentences`; `check_answer` runs the pairs of the session in order and adds the notes of a shared sentence); `guppi/ledger.py` (`refused_tags`, `tag_message`); `guppi/prespec.py` (`sentence_around`, `shift_spans`, `sentence_parts`, `shared_sentence_note`; `check_pairs` takes `own`, `notes`, `trace`); `guppi/generate.py` (`reword_pattern`; `register_tags` reads through `guppi/tags.py`); `guppi/shellwrite.py` (new); `guppi/cli.py` (`shellwrite`). Tests: `tests/test_casecheck.py`, `tests/test_ledger.py`, `tests/test_shellwrite.py` (new). Handoff: `make test` 1407 passed, 6 skipped; `make style` clean.
- Readings of the session: L11, L12, L13 `passed` by the person's word (Plan Mode); 8 Retro readings `passed`; `estimate-case-build-writes-the-case` and `estimate-case-build-checks-the-finished-case` `failed`, not read. Lessons: none.
- The ledger: 38 lines. The yaml: 32 entries (7 `create`, 18 `update`, 7 `estimate`) and 6 lines folded into creates (L29, L30, L32, L33, L34, L35); every ledger line is accounted for. 32 entries and 17 decision records carry `applied` (49); 0 `failed`, 0 `exists`, 1 `incomplete`, 1 `near`, 0 `merged`; `unparsed: []`.
- Pages created: decisions 17 (703, 703.1–703.3, 704, 705, 705.1, 705.2, 706, 710, 710.1, 710.2, 711, 711.1–711.4); estimates 6 (`estimate-case-check-sends-back-an-unlisted-tag`, `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`, `estimate-shell-write-check-repairs-and-reports`, `estimate-case-check-applies-the-pairs-of-the-session-in-order`, `estimate-case-check-notes-a-sentence-two-cases-change`, `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`, each read `passed` by its folded line); rules 1 (`rule-shell-write-check`, child of `rule-harness`, `built` by the cascade).
- Pages updated: rules 6 by decisions (`rule-case-check` by 703.1, 711.1, 711.2, 711.3; `rule-ledger-write` by 703.2; `rule-case-build` by 705.1, 711.4; `rule-orchestration` by 705.2; `rule-hook-registry` and `rule-harness` by 710.1), and `rule-permissions` by the cascade; estimates 4 by decisions (Criterion replaced: `estimate-case-build-writes-the-case`, `estimate-orchestration-shows-the-built-case`, `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, `estimate-case-build-checks-the-finished-case`) and 7 readings (`estimate-orchestration-shows-the-frontier-after-a-closed-line` failed → passed, `estimate-permissions` pending → passed, `estimate-orchestration-defers-in-one-reply` failed → passed, `estimate-ledger-write-asks-for-the-mark-of-a-lesson` and `estimate-orchestration-shows-the-built-case` → passed, `estimate-case-build-writes-the-case` and `estimate-case-build-checks-the-finished-case` → failed); insights 3 (`insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` a History line by 704 and `addressed_by: "[[decision-case-701.1]]"` by 706; `insight-workflow-file-changed-through-a-shell-command` `actioned`, `addressed_by: "[[decision-case-710.1]]"`, by 710.2; `insight-workflow-edit-pair-signed-from-a-grep-fragment` `actioned`, `addressed_by: "[[decision-case-711.3]]"`, by 711.3).
- The cascade set `rule-orchestration`, `rule-permissions` and `rule-shell-write-check` `draft` → `built`, and archived the 4 clustered children of the two Insights set `actioned`. `tags.md` gained the row `orchestration`; `generate` printed no warning.
- Index check: the one `create` that is not an Estimate is `rule-shell-write-check`. `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 76 lines. `rule-bash-guard` (a heredoc refused before a Bash call) is close but not the same (a file repaired after a Bash or PowerShell call): marked `near: rule-bash-guard`. The index line settled it; no page was opened.
- The handoff's Direct instructions: the 5 `replace` anchors of `rule-case-check` (703.1, 711.1, 711.2, 711.3 ×2) and the 2 of `rule-case-build` (705.1, 711.4) were counted in yaml order before `generate`, each 1 hit, and no new text holds a later anchor; `generate` applied all. The render changed `.claude/settings.json` (the `shellwrite` hook on `PostToolUse` of `Bash|PowerShell`), `.claude/agents/case-guppi.md` and `vault/wiki/orchestration.md`. Both Insights set `actioned` left `backlog.md`.
- `cleanup: 4 page(s) moved` to `vault/archive/migration/2026-10-07/0636/lessons/`: `lesson-case-build-related-cases-same-sentence-missed`, `lesson-session-frontier-rewritten-through-powershell`, `lesson-work-mode-code-rewritten-through-python-write-text`, `lesson-work-mode-file-changed-through-a-bash-heredoc`.
- The scripts ticked 41 boxes of the 0636 Spec; none stays open. `generate` also ticked `read estimate-permissions` in the 0211 Spec. `guppi materialize` named the 0211 and 0425 yamls ("extended with 0 entries"); `generate` wrote 0 pages from them. No unticked line of the 0636 Spec holds `guppi sprint-close`; none ran.
- `guppi sprint` left `sprint.md` unchanged; `guppi glossary` left `glossary.md` unchanged; `guppi backlog` rewrote `backlog.md` (7 items before, 5 after). The run added 74 lines to `log.md`. `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- `guppi archive` exit 0, no stdout, no stderr; it moved no unit. `raw/2026-10-07/0211`, `raw/2026-10-07/0425` and `raw/2026-10-07/0636` stay: the script looks only at units dated before the day of the run, and 0636 is the session of the run.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 76 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 34 lines. The yaml holds no `lesson` entry, so no lesson was compared.

## Readings due

Failed:
- `estimate-case-build-writes-the-case` — failed — `rule-case-build` stands `draft` — result: 2026-10-07, Retro, not read: the undo of a dropped change of case 705.1 reaches `.claude/agents/case-guppi.md` only at the librarian's render of this session, and the person chose to take the reading whole in the next session — read: by hand, live dispatches in a session after the render, a change dropped on a ratified Case included, tokens and seconds of each dispatch in the estimate line (method).
- `estimate-case-build-checks-the-finished-case` — failed — `rule-case-build` stands `draft` — result: 2026-10-07, Retro, not read: the read of the case file of a Case the check names, case 711.4, reaches `.claude/agents/case-guppi.md` only at the librarian's render; at the `/pre-spec` of this session `ask-guppi` found 14 findings on the Cases `case-guppi` built, 5 of them Estimates a Case did not name and 3 facts of a context the vault did not bear out — read: by hand at `/pre-spec`, the findings of `ask-guppi` for each Case `case-guppi` built, the count of each kind in the reading line (method).

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `5 items`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 0636 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 4 pages from `cleanup` under `migration/2026-10-07/0636/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 14 finding lines — 1 `deferred`, 13 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1407 passed, 6 skipped, on the working tree of this run.

## Flags

- `incomplete`: the create of `rule-shell-write-check` (L14, case 710.1) lacked `type` in its Spec block; the page was written and holds `type: rule`.
- `near`: the create of `rule-shell-write-check` is marked `near: rule-bash-guard`.
- No entry marked `failed` or `unparsed`.
- Failed Estimates: `estimate-case-build-writes-the-case` (L37), `estimate-case-build-checks-the-finished-case` (L38), both Retro, not read.
- Contradiction, handoff against disk: Notes from memory say `addressed_by` of the Insights of 710.2 and 711.3 stands bare (`decision-case-710.1`, `decision-case-711.3`); after `generate` both pages hold the quoted wikilink (`"[[decision-case-710.1]]"`, `"[[decision-case-711.3]]"`).
- Handoff, Notes from memory: C7 and C6 were closed by a reading on the person's word alone, not by a Case; their ledger lines (L11, L13) say so.
- Handoff, Notes from memory: on A1 (`estimate-permissions`) the person said no permission prompt came; the agent did not check which paths the `case-guppi` dispatches read. The reading (L12) set it `passed`.
- Handoff, Notes from memory: on C5 the person chose no Case; the reading of `estimate-case-build-writes-the-case` is to be taken whole in the next session; splitting the Estimate per rare condition was proposed and declined.
- Handoff, Notes from memory: on Case 705 the person chose to drop only the change; taking back the whole decision of a ratified Case is left not done.
- Handoff, Notes from memory: on Cases 706 and 710 the person chose no check that sends back an `actioned` Insight with no `addressed_by` before ratification; `make lint` stays the only check.
- Handoff, Notes from memory: C1, C2 and C9 were closed `[-] · sprint · defer` for the session that closes the sprint.
- Handoff, Notes from memory: for Case 710 the person asked for the round to be explained again in plain words.
- Handoff, Observations: `make lint` was red before the work, exit 2, 17 finding lines (1 `schema`, 1 `deferred`, 15 `unread`); it was not run in Retro.
- Handoff, Observations: the read check of 711.3 was not tried live on a sentence in a section whose text differs from its Markdown file, such as a fenced Render.
- Handoff, Observations: `git ls-files -m` lists a file whose only change is CRLF line endings under `* text=auto eol=lf` (tried in a temporary repository).
- Handoff, Observations: at `/pre-spec` the `Stop` check once refused the showing of Case 705 because its file differed from the stored text; what changed the file was not found.
- Handoff, Observations: `ask-guppi` at pre-spec searched the Estimates three times by Grep over their text, not through the `estimates` field; two of its findings rest on those searches.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: none found.
- The lint: 14 finding lines — 1 `deferred` (`rules/rule-morph`), 13 `unread` (11 `pending`, 2 `failed`: the 13 Estimates of Readings due); `make lint` exit 2. The `schema` finding on `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` is gone after 706.
- Reads beyond the frame: none.

## Next session

Cases:
- Taking back the whole decision of a ratified Case is left not done (handoff, For the next session; Case 705, Q1).
- No check sends back a Case that sets an Insight `actioned` with no `addressed_by` before ratification; `make lint` stays the only signal (handoff, For the next session; Case 706, Q2).
- The `method` of `estimate-orchestration-shows-the-frontier-after-a-closed-line` waits for a later session, so the next Case that changes it leaves it `failed` at its own Retro (handoff, For the next session; C7).
- `addressed_by` of a Case of the same session cannot be the quoted wikilink the schema asks for, because the check of the Case file refuses a link to a decision not yet written; one of the two needs a decision (handoff, For the next session).
- `estimate-case-build-writes-the-case` stands `failed`: its reading waits for live dispatches after this render (L37).
- `estimate-case-build-checks-the-finished-case` stands `failed`: its reading waits for a `/pre-spec` after this render (L38).
- `rule-sprint-close` and the close of migration wait for the session that closes the sprint (handoff, Notes from memory: C1, C2, C9).

Work:
- `estimate-hi-writes-frontier`
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

Ask the person:
- none

## Readings at the close

- `make test`: 1407 passed, 6 skipped.
- `make lint`: 14 finding lines — 1 `deferred`, 13 `unread`; exit 2.
- Pages under `vault/wiki/`: rules 76, estimates 240, insights 34, lessons 72, decisions 1254, entities 4.
