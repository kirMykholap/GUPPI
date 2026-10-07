# Brief — 2026-10-07, after the librarian run of session 0425

## Where things stand

- Session 0425 ratified Case 701 (701.1–701.7) and Case 702 (handoff, What actually got done).
- Code: `guppi/casecheck.py` (`dropped`; `other_blocks` takes the session folder and skips a dropped Case; `check_answer` and `judge_and_store` pass the folder); `guppi/onward.py` (`case_out` and `built_after` skip an empty Case file by `casecheck.dropped`); `guppi/ratified.py` (`read_tasks` reads a tag line into `new_tags` at the head of the `then` block and refuses one off the form). Tests: `tests/test_onward.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`. Handoff: `make test` 1361 passed, 6 skipped; `make style` clean.
- Readings: L19–L23 `passed`; L24 (`estimate-case-build-writes-the-case`), L25 (`estimate-orchestration-defers-in-one-reply`) and L26 (`estimate-orchestration-shows-the-frontier-after-a-closed-line`) `failed`, Retro, not read. Lesson: L27.
- The ledger: 27 lines. The yaml: 26 entries from them (L22 folded into the create of L9), plus 2 entries of the synthesis, 28 in all; 28 carry `applied`; 9 decision records, 9 `applied`; 0 `failed`, 0 `exists`, 0 `incomplete`, 0 `near`, 0 `merged`; `unparsed: []`. Every ledger line is accounted for.
- Pages created: decisions 9 (701, 701.1–701.7, 702); estimates 1 (`estimate-spec-write-reads-a-new-tag`, by 702, read `passed` by the folded L22); lessons 1 (`lesson-work-mode-code-rewritten-through-python-write-text`, L27, set `clustered` by the synthesis).
- Pages updated: rules 6 (`rule-prespec-onward` by 701.1, 701.2; `rule-case-build` by 701.3; `rule-orchestration` by 701.4, 701.5, 701.6; `rule-case-check` by 701.7; `rule-spec-write` and `rule-case-protocol` by 702); estimates 7 by decisions (Criterion replaced, set `pending`), then 4 read `passed` (L19, L20, L21, L23) and 3 read `failed` (L24, L25, L26); insights 2 (`insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` set `actioned` by 701.1; `insight-workflow-file-changed-through-a-shell-command` gained a child by the synthesis, severity 3 after the run). The cascade set `rule-orchestration` `built` → `draft` and archived the two clustered children of the actioned Insight.
- Index check: the only `create` of the yaml is an Estimate, so no index Grep ran.
- The handoff's Direct instructions: the 13 `replace` anchors of the six rule pages were counted in yaml order before `generate`, each 1 hit, and `generate` applied all; the pages were written from the yaml `materialize` lifted from `spec.md`, and no entry was changed for the instruction on the two ratifications of Case 701. The render wrote the three files the handoff names: `.claude/agents/case-guppi.md`, `vault/wiki/orchestration.md`, `vault/wiki/case-schema.md`.
- `cleanup: 2 page(s) moved`: `lesson-prespec-onward-an-empty-case-file-keeps-it-silent` and `lesson-prespec-onward-re-ratification-out-after-its-stretch` to `vault/archive/migration/2026-10-07/0425/lessons/`.
- The scripts ticked 29 boxes of the 0425 Spec; none stays open. `guppi sprint` left `sprint.md` unchanged; `guppi glossary` left `glossary.md` unchanged; `guppi backlog` rewrote `backlog.md` (8 items before, 7 after: the actioned Insight left `## Deferred`; `insight-workflow-file-changed-through-a-shell-command` went from severity 2 to 3). The run added 44 lines to `log.md`.
- `guppi materialize` also named the 0211 yaml ("extended with 0 entries"); `generate` wrote 0 pages from it.
- `guppi archive` exit 0, no stdout, no stderr; it moved no unit. `raw/2026-10-07/0211` and `raw/2026-10-07/0425` stay: the script looks only at units dated before the day of the run, and 0425 is the session of the run.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 77 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 34 lines.
- `lesson-work-mode-code-rewritten-through-python-write-text` joined `insight-workflow-file-changed-through-a-shell-command` (`open`); the Insight's `status` is kept.

## Readings due

Failed:
- `estimate-case-build-writes-the-case` — failed — `rule-case-build` stands `draft` — result: 2026-10-07, Retro, not read: the drop of case 701.3 reaches `.claude/agents/case-guppi.md` only at this render, and no Case with a create without a ref, no Case sent back and fixed by Edit and no change on one sub-case came up — read: by hand, live dispatches in a session after the render, a Case dropped by a message of the main agent included, tokens and seconds of each dispatch in the estimate line (method).
- `estimate-orchestration-defers-in-one-reply` — failed — `rule-orchestration` stands `draft` — result: 2026-10-07, Retro, not read: no decision was put off in session 0425, and the drop of case 701.5 reaches `orchestration.md` only at this render — read: by hand, a decision the person asks to put off, its line of `frontier.md` closed `[-] … · defer case N` (method).
- `estimate-orchestration-shows-the-frontier-after-a-closed-line` — failed — `rule-orchestration` stands `draft` — result: 2026-10-07, Retro, not read: its method reads the reply in a later session, and the wait for `**Dropped:**` of case 701.6 reaches `orchestration.md` only at this render — read: by hand, in a later session, the first reply in Plan Mode after the first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer (method).

Pending:
- `estimate-permissions` — pending — `rule-permissions` stands `draft` — read: the person's word on the client's prompt, in a session after the librarian's render, at the Greps and the Read its method names and at the Write of the Case file of `case-guppi` (method).
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `7 items`, `## Conserved Specs` empty, 7 lines under `## Deferred`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 0425 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 2 pages from `cleanup` under `migration/2026-10-07/0425/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 17 finding lines — 1 `schema`, 1 `deferred`, 15 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1361 passed, 6 skipped, on the working tree of this run.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`.
- Failed Estimates: `estimate-case-build-writes-the-case` (L24), `estimate-orchestration-defers-in-one-reply` (L25), `estimate-orchestration-shows-the-frontier-after-a-closed-line` (L26), all Retro, not read; the cascade set `rule-orchestration` `built` → `draft`.
- Contradiction, from the lint: `insights/insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out: schema: missing field addressed_by (given {'status': 'actioned'})`. The entry of L3 (case 701.1) sets `status: actioned` with no `addressed_by`; the entry stands as written.
- Handoff, Direct instructions: "read the Case from the Spec, not from the first lines" for Case 701 — not carried out as a read of the Spec's Cases; this frame says the librarian's job needs `spec.md` only for its unticked lines and the lines this run ticked; the yaml holds the decision records `materialize` lifted from `spec.md`, and all 9 applied.
- Handoff, Notes from memory: on Case 701 the person kept the line in `estimate-case-build-writes-the-case` that checks the drop, knowing it holds the Estimate unpassed until a session after the render.
- Handoff, Notes from memory: on Case 702 the person chose to register the tag against the recommendation; the declaration of `orchestration` was put to a later session.
- Handoff, Notes from memory: C4 needed no Case of its own; its `case-guppi` answered with a `**Fact:**` and the line closed under case 701.
- Handoff, Notes from memory: A1 (`estimate-permissions`) stays open; the agent counted the tool calls of the three `case-guppi` transcripts: every `file_path` and `path` lay under `c:\PROJECTS\GUPPI`; the person said no permission prompt came while the Case files were written.
- Handoff, Notes from memory: C1 and C2 (`rule-sprint-close`, the close of migration) were closed `[-] · sprint · defer` for a session of their own; the person agreed.
- Handoff, Notes from memory: at `/pre-spec`, `ask-guppi` did not check that each new `old` anchor hits its page once, nor that the code tasks fit the code.
- Handoff, Observations: `make lint` was red before the work, exit 2, 14 finding lines (1 `deferred`, 13 `unread`); it was not run in Retro.
- Handoff, Observations: the answer of `case-guppi` to a `SendMessage` came back each time in a turn of its own, as a task notification; the `**Waiting:**` step of 701.4 rests on this.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: none found.
- The lint: 17 finding lines — 1 `schema` (`insights/insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`), 1 `deferred` (`rules/rule-morph`), 15 `unread` (12 `pending`, 3 `failed`: the 15 Estimates of Readings due); `make lint` exit 2.
- Reads beyond the frame: none.

## Next session

Cases:
- Declare the tag `orchestration` by a tag line in a Case, once the render puts the form into `case-schema.md`; that Case also needs a decision line of a page change (handoff, For the next session; Case 702, Q4 (a)).
- No check stops a tag that `tags.md` does not hold from getting onto a lesson line or a `create` line; the warning of `guppi generate` stays the only signal (handoff, For the next session; Case 702, Q2 (a)).
- `estimate-case-build-writes-the-case` stands `failed`: its reading waits for a live dropped Case after this render (handoff, For the next session).
- `estimate-orchestration-defers-in-one-reply` stands `failed`: its reading waits for a decision put off after this render (handoff, For the next session).
- `estimate-orchestration-shows-the-frontier-after-a-closed-line` stands `failed`: its reading waits for a reply that closes a line with no ratification after this render (handoff, For the next session).
- A ratified Case that is sent back and then dropped still keeps the hook of `rule-prespec-onward` silent: its file is never emptied (handoff, For the next session; Case 701, left not done).
- `rule-sprint-close` and the close of migration still wait for a session of their own (handoff, For the next session).
- `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` stands `actioned` with no `addressed_by`, a `schema` finding of `make lint` (the entry of L3, case 701.1).

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
- `estimate-permissions` — needs the person — in a session where `case-guppi` reads a transcript under `~/.claude/projects/c--PROJECTS-GUPPI` or a path outside the project that no rule names: did that read and the write of its Case file, in `permissionMode: auto`, come with no permission prompt?

## Readings at the close

- `make test`: 1361 passed, 6 skipped.
- `make lint`: 17 finding lines — 1 `schema`, 1 `deferred`, 15 `unread`; exit 2.
- Pages under `vault/wiki/`: rules 76, estimates 235, insights 35, lessons 77, decisions 1238, entities 5.
