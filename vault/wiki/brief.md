# Brief — 2026-10-06, after the librarian run of session 1448

## Where things stand

- Session 1448 ratified Cases 692 (692.1, 692.2), 693, 694 (694.1, 694.2) and 695 (695.1, 695.2). Case 691 was built again after `/pre-spec` as Case 695, whose lines carry `{supersedes:case 691}`.
- Code: `guppi/casecheck.py` (`turn_blocks`, `given_back_at`, `texts_after`, `last_refused`, `is_summary`; `texts_before_last_call` and `LEDGER_LINE` gone; `PREFIXES` imported from `guppi/ledger.py`); `guppi/ledger.py` (`held_message` and `reminder_message` take the slug alone; `named_cases` gone; `block_lines`, `stray_lines`, `stray_message` new; the hook refuses a line that is no record). Tests: `tests/test_casecheck.py`, `tests/test_ledger.py`. Handoff: `make test` 1330 passed, 6 skipped; `make style` clean.
- Readings: L18–L23, all `passed`. Lessons: L1, L2, L24.
- The yaml: 23 entries from the 24 ledger lines (L18 folded into the create of L13); 21 carry `applied`; L3 and L4 (Case 691) carry `superseded_by: '695.2'` and were not applied; all 11 decision records carry `applied`; 0 `failed`, 0 `exists`, 1 `incomplete` (L4), 3 `near`, 0 `merged`, 0 entries added by the synthesis; `unparsed: []`.
- Pages created: decisions 11 (691, 692, 692.1, 692.2, 693, 694, 694.1, 694.2, 695, 695.1, 695.2); estimates 1 (`estimate-ledger-write-refuses-a-line-that-is-no-record`, from L13, read `passed` by the folded L18); lessons 3 (`lesson-hooks-a-mod-draws-nothing-in-the-mobile-code-tab`, `lesson-case-check-round-refused-for-an-own-text-no-showing-clears`, `lesson-prespec-onward-a-reminder-answer-ends-the-run`).
- Pages updated: rules 6 (`rule-case-check` by 692.1; `rule-permissions` and `rule-morph` by 693; `rule-ledger-write` by 695.1; `rule-retro` and `rule-retro-onward` by 695.2); estimates 6 by decisions (Criterion replaced, set `pending`): `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-refuses-text-outside-the-list`, `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`, `estimate-retro-runs-on-to-the-handoff` — each then read `passed` (L19–L23) — and `estimate-permissions`, which stays `pending`; decisions 1 (`decision-case-691`, superseded by 695.1 and 695.2). The cascade set `rule-permissions` `built` → `draft`.
- The handoff's Direct instructions, checked on the pages: `rule-morph` took the `purpose` of Case 693 in its frontmatter, and the pair `so a changed set rewrites no rule;` landed once, in the Purpose section; the anchor now stands in both places, each time followed by the new text the Case gives. The pairs of 695.2 landed: `rule-retro` (the refused record lines, the line that is no record left out, `/handoff` with nothing left), `rule-retro-onward` (the answer that writes none and calls `/handoff`), and `estimate-retro-runs-on-to-the-handoff` (its `purpose` and Criterion replaced as the Case gives them). The create of `estimate-ledger-write-refuses-a-line-that-is-no-record` became one page, from L13 under 695.1. No instruction was refused.
- `cleanup: 1 page(s) moved`: `decision-case-691` to `vault/archive/migration/2026-10-07/1448/decisions/`.
- The scripts ticked 21 boxes of the 1448 Spec; one stays open, `read estimate-permissions`. The render wrote `.claude/settings.json` (the line `Read(~/.claude/projects/c--PROJECTS-GUPPI)` added) and `.claude/skills/retro/SKILL.md`. `guppi sprint` left `sprint.md` unchanged; `guppi glossary` left `glossary.md` unchanged; `guppi backlog` rewrote the `rule-morph` line of `backlog.md` (7 items before and after). No script printed a line on stderr. The run added 39 lines to `log.md`.
- `guppi materialize` named the 0104 yaml too ("extended with 0 entries"); `generate` wrote 0 pages from it.
- `guppi archive` exit 0, no stderr; it moved one unit, `raw/2026-10-06/0104` → `archive/migration/2026-10-06/0104/raw`, and kept `raw/2026-10-06/1448`, the session of the run.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 73 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 32 lines.
- `lesson-hooks-a-mod-draws-nothing-in-the-mobile-code-tab` — none: no lesson or Insight names a mod or the mobile Code tab; the nearest, `lesson-hooks-a-stop-system-message-shows-no-markdown-in-vs-code`, is about another channel in another client.
- `lesson-case-check-round-refused-for-an-own-text-no-showing-clears` — none: its cause is the scope of the check (every text of the turn); `lesson-orchestration-own-text-before-a-round` has the agent's habit as its cause, and no Insight names a refusal that its own step cannot clear.
- `lesson-prespec-onward-a-reminder-answer-ends-the-run` — none: `lesson-prespec-onward-re-ratification-out-after-its-stretch` has the stretch window as its cause; `insight-prespec-after-findings-loop-unruled` is about the loop after the findings of `/pre-spec`, not the answer to a ledger reminder.

## Readings due

Pending:
- `estimate-permissions` — pending — `rule-permissions` stands `draft` — read: `- [ ] read estimate-permissions` of `raw/2026-10-06/1448/spec.md`; its method names the person's word on the client's prompt, in a session after the librarian's render, at a Grep of a subagent on `~/.claude/projects/c--PROJECTS-GUPPI` itself and on a file under it.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `7 items`, `## Conserved Specs` empty, 7 lines under `## Deferred`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 1448 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 1 page from `cleanup` under `migration/2026-10-07/1448/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 13 finding lines — 1 `deferred`, 12 `unread`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1330 passed, 6 skipped, on the working tree of this run.

No Estimate stands `failed`.

## Flags

- `incomplete`: L4, `decision[case 691][create][estimate-ledger-write-refuses-a-line-that-is-no-record]`, lacks `criterion`; it is superseded and wrote no page; the page came from L13 with its Criterion.
- `near`: L1 `lesson-hooks-a-mod-draws-nothing-in-the-mobile-code-tab` near `lesson-hooks-a-stop-system-message-shows-no-markdown-in-vs-code`; L2 `lesson-case-check-round-refused-for-an-own-text-no-showing-clears` near `lesson-orchestration-own-text-before-a-round`; L24 `lesson-prespec-onward-a-reminder-answer-ends-the-run` near `lesson-prespec-onward-re-ratification-out-after-its-stretch`.
- No entry marked `failed` or `unparsed`. Failed Estimates: none.
- Handoff, Notes from memory: the agent put off C1 and C2 (`rule-sprint-close`, the close of migration) as `[-] · sprint · defer` in the reply where the person picked C4, with no question of its own; the person did not object.
- Handoff, Notes from memory: the folder name of the transcripts for another install went into the `purpose` of `rule-morph`, which no Estimate checks.
- Handoff, Observations: `make lint` was red before the work, exit 2, 12 finding lines; it was not run in Retro; no line stands under `## Expected red`.
- Handoff, Observations: the new hook code was live from the commit of the work; the hold at Retro asked "did a Case of this session fix its cause?" with no Case named.
- Handoff, Observations: after the acknowledging reply of Cases 695, 692 and 693 the ledger reminder took the `Stop`, and the run stopped until the person spoke (lesson L24).
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: none found. Contradictions: none found.
- The lint: 13 finding lines — 1 `deferred` (`rules/rule-morph`), 12 `unread: pending` (the 12 Estimates of Readings due); `make lint` exit 2.
- Reads beyond the frame: none.

## Next session

Cases:
- Lesson L24: whether the hook of `rule-prespec-onward`, or the rule for the answer to the ledger hook's reminder, sends the agent on to the check and the exit when no Cases line is open (handoff, For the next session).
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint (handoff, For the next session).

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
- `estimate-permissions` — needs the person — in the first session after the librarian's render: did a Grep of a subagent on `~/.claude/projects/c--PROJECTS-GUPPI` itself, and on a file inside it, run with no permission prompt?

## Readings at the close

- `make test`: 1330 passed, 6 skipped.
- `make lint`: 13 finding lines — 1 `deferred`, 12 `unread`; exit 2.
- Pages under `vault/wiki/`: rules 75, estimates 232, insights 32, lessons 76, decisions 1209, entities 4.
