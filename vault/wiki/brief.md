# Brief — 2026-10-07, after the librarian run of session 0211

## Where things stand

- Session 0211 ratified Cases 696 (696.1, 696.2), 697 (697.1–697.4), 698 (698.1, 698.2) and 699 (699.1–699.7). Case 700 was built and dropped; it holds no ledger line, and `raw/2026-10-07/0211/cases/case-700.md` is an empty file.
- Code: `guppi/onward.py` (`--plan` silent before `/pre-spec`, `TO_PRESPEC` gone; a Case that a supersedes mark retires is not out, `session_decisions`, `case_out`; the answer with no `LEDGER` block to a reply the ledger hook sent back is sent on; its own error exits 0 before `/pre-spec`, `after_prespec`); `guppi/prespec.py` (`retired_whole`); `guppi/ledger.py` (`stretch_of`, `refusals_in`, `refusal_records`, `sent_back_last`); `guppi/casecheck.py` (the `Stop` run no longer refuses a layout fault; the new `--prompt` run, `before_message`, `last_reply`, `prompt_note`; `last_refused` takes records). Tests: `tests/test_onward.py`, `tests/test_casecheck.py`. Handoff: `make test` 1344 passed, 6 skipped; `make style` clean.
- Readings: L34–L47; L40 (`estimate-case-build-writes-the-case`) is `failed`, the others `passed`. Lessons: L16, L48, L49.
- The ledger: 49 lines. The yaml: 48 entries from them (L45 folded into the create of L26), plus 8 entries of the synthesis, 56 in all; 56 carry `applied`; 19 decision records; 0 `failed`, 0 `exists`, 0 `incomplete`, 3 `near`, 0 `merged`; `unparsed: []`. Every ledger line is accounted for.
- Pages created: decisions 19 (696, 696.1, 696.2, 697, 697.1–697.4, 698, 698.1, 698.2, 699, 699.1–699.7); estimates 1 (`estimate-orchestration-marks-each-round-of-a-batch`, by 699.5, read `passed` by the folded L45); lessons 3 (`lesson-orchestration-batch-rounds-headed-by-their-case`, `lesson-prespec-onward-an-empty-case-file-keeps-it-silent`, `lesson-work-mode-file-changed-through-a-bash-heredoc`); insights 2 (`insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`, `insight-workflow-file-changed-through-a-shell-command`, both by the synthesis, both `open`, severity 2).
- Pages updated: rules 8 (`rule-prespec-onward` by 696.1, 696.2; `rule-orchestration` by 697.1–697.4, 699.4–699.6; `rule-case-build` by 698.1; `rule-permissions` and `rule-morph` by 698.2; `rule-case-check` by 699.1, 699.2; `rule-hook-registry` by 699.1; `rule-prespec` by 699.7); estimates 14 by decisions (Criterion replaced, set `pending`), then 12 of them read `passed` by L34–L47 and `estimate-case-build-writes-the-case` read `failed`; `estimate-permissions` stays `pending`; insights 1 (`insight-orchestration-items-taken-together-unruled` set `actioned` by 699.5, then the synthesis added a child and set `addressed_by: decision-case-699.5`); lessons 2 by the synthesis (`lesson-prespec-onward-re-ratification-out-after-its-stretch`, `lesson-session-frontier-rewritten-through-powershell`, set `clustered`). The cascade set `rule-case-build` `built` → `draft` and archived the two clustered children of the actioned Insight.
- The handoff's Direct instructions: the pages were written from the yaml that `materialize` lifted from `spec.md`; I changed no entry for this instruction. `rule-morph` got one History line from 698.2, and no text change. On L16, my judgment on the duplicate: not the same page. The same root cause stands in `lesson-orchestration-batch-rounds-headed-by-own-text`, but its trigger is another event (session 0104, Cases 686 and 687). L16 is marked `near` and clustered under `insight-orchestration-items-taken-together-unruled`. The render wrote the four files the handoff names: `.claude/settings.json`, `.claude/agents/case-guppi.md`, `vault/wiki/orchestration.md`, `.claude/skills/pre-spec/SKILL.md`.
- `cleanup: 2 page(s) moved`: `lesson-orchestration-batch-rounds-headed-by-own-text` and `lesson-orchestration-batch-rounds-headed-by-their-case` to `vault/archive/migration/2026-10-07/0211/lessons/`.
- The scripts ticked 52 boxes of the 0211 Spec; one stays open, `read estimate-permissions`. `guppi sprint` left `sprint.md` unchanged; `guppi glossary` left `glossary.md` unchanged; `guppi backlog` rewrote `backlog.md` (7 items before, 8 after: the actioned Insight left `## Deferred`, the two new Insights entered it). The run added 82 lines to `log.md`.
- `guppi materialize` also named the 1448 yaml ("extended with 0 entries"); `generate` wrote 0 pages from it.
- `guppi archive` exit 0, no stderr; it moved one unit, `raw/2026-10-06/1448` → `archive/migration/2026-10-06/1448/raw`, and kept `raw/2026-10-07/0211`, the session of the run.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 76 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 32 lines.
- `lesson-orchestration-batch-rounds-headed-by-their-case` joined `insight-orchestration-items-taken-together-unruled`, which shares the cause of its child `lesson-orchestration-batch-rounds-headed-by-own-text`. The pair: the Insight was set `actioned` by 699.5 in this yaml; the lesson carries `addressed_by: decision-case-699.5`, which is later than the Insight's `decision-case-684.1`, so the synthesis set `addressed_by: decision-case-699.5` and kept `actioned`. The cascade archived both clustered children.
- `lesson-prespec-onward-an-empty-case-file-keeps-it-silent` and `lesson-prespec-onward-re-ratification-out-after-its-stretch` formed the new Insight `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`.
- `lesson-work-mode-file-changed-through-a-bash-heredoc` and `lesson-session-frontier-rewritten-through-powershell` formed the new Insight `insight-workflow-file-changed-through-a-shell-command`.

## Readings due

Failed:
- `estimate-case-build-writes-the-case` — failed — `rule-case-build` stands `draft` — result: 2026-10-07, Retro, not read: the anchor `permissionMode: acceptEdits` of `rule-case-build` stands once, but the method needs live dispatches in a session after the librarian's render — read: by hand, live dispatches in a session after the render, the Case file written in Plan Mode with no prompt, tokens and seconds of each dispatch in the estimate line (method).

Pending:
- `estimate-permissions` — pending — `rule-permissions` stands `draft` — read: `- [ ] read estimate-permissions` of `raw/2026-10-07/0211/spec.md`; its method names the person's word on the client's prompt, in a session after the librarian's render.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `8 items`, `## Conserved Specs` empty, 8 lines under `## Deferred`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 0211 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 2 pages from `cleanup` under `migration/2026-10-07/0211/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 14 finding lines — 1 `deferred`, 13 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1344 passed, 6 skipped, on the working tree of this run.

## Flags

- `near`: L16 `lesson-orchestration-batch-rounds-headed-by-their-case` near `lesson-orchestration-batch-rounds-headed-by-own-text`; L48 `lesson-prespec-onward-an-empty-case-file-keeps-it-silent` near `lesson-prespec-onward-re-ratification-out-after-its-stretch`; L49 `lesson-work-mode-file-changed-through-a-bash-heredoc` near `lesson-session-frontier-rewritten-through-powershell`.
- No entry marked `incomplete`, `failed` or `unparsed`.
- Failed Estimate: `estimate-case-build-writes-the-case` (L40, Retro, not read); the cascade set `rule-case-build` `built` → `draft`.
- `guppi generate` stderr: `generate: tag orchestration is used but not registered in tags.md`. The tag comes from L16 and L48. The synthesis carried it into the tags of `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` as part of the union.
- Handoff, Notes from memory: the agent closed C1 and C2 (`rule-sprint-close`, the close of migration) `[-] · sprint · defer`, because a session that closes a sprint holds no other Cases; the person did not object.
- Handoff, Notes from memory: the `prespec` line of an interrupted first `/pre-spec` call stayed in the event log, so the hook of `rule-prespec-onward` counted `/pre-spec` as run (Case 697).
- Handoff, Notes from memory: A1 (`estimate-permissions`) closed `· work` with no reading line; the person said the prompt for reading the transcript came after `case-guppi` started, so the old Criterion failed in fact; 698.2 replaced that Criterion, and no `failed` line was written.
- Handoff, Notes from memory: Case 698 was first built again as a Case 700 that superseded it; the `Stop` check refused to show it, and 698 was built again under its own id; Case 700 holds no ledger line.
- Handoff, Observations: `make lint` was red before the work, exit 2, 13 finding lines (1 `deferred`, 12 `unread`); it was not run in Retro.
- Handoff, Observations: `casecheck --prompt` runs only once the render registers it; until this run's render, a layout fault of a showing was neither refused nor told.
- Handoff, Observations: the harness flagged two subagent answers as instruction-shaped (they mentioned `settings.json` and `bypassPermissions`); nothing in them was acted on.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: none found. Contradictions: none found.
- The lint: 14 finding lines — 1 `deferred` (`rules/rule-morph`), 13 `unread` (12 `pending`, 1 `failed`: the 13 Estimates of Readings due); `make lint` exit 2.
- Reads beyond the frame: none.

## Next session

Cases:
- Lesson L48: decide whether `case-guppi` removes the file of a Case it drops, or whether the hook of `rule-prespec-onward` leaves out a file that no ledger line and no reply names (handoff, For the next session); its Insight is `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`.
- `rule-sprint-close` and the close of migration still wait for a session of their own (handoff, For the next session).
- `estimate-case-build-writes-the-case` stands `failed` (Retro, not read); its live dispatches can be read in the first session after the render (handoff, For the next session).
- The tag `orchestration` is used by L16, L48 and one new Insight but is not registered in `tags.md` (`guppi generate` stderr).

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
- `estimate-permissions` — needs the person — in the first session after the librarian's render: did `case-guppi`, in `permissionMode: auto`, read a transcript under `~/.claude/projects/c--PROJECTS-GUPPI`, read a path outside the project that no rule names, and write its Case file, all with no permission prompt? (the open boxes `read estimate-permissions` of `archive/migration/2026-10-06/1448/raw/spec.md` and `raw/2026-10-07/0211/spec.md`)

## Readings at the close

- `make test`: 1344 passed, 6 skipped.
- `make lint`: 14 finding lines — 1 `deferred`, 13 `unread`; exit 2.
- Pages under `vault/wiki/`: rules 75, estimates 233, insights 34, lessons 77, decisions 1228, entities 4.
