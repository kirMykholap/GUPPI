# Brief — 2026-10-05, after the librarian run of session 1831

## Where things stand

- Session 1831 ratified Cases 669 (669.1–669.16), 670 (670.1–670.7) and 671 (671.1, 671.2); all three were built again on the findings of pre-spec and ratified again. 669 closed 15 Estimates as `passed` by the person's decision.
- Code: `guppi/ledger.py` (`refused_readings` waits for the `retro` mark of the session, 670.1), `guppi/onward.py` (`retro_mark`, `retro_moment`), `guppi/lint.py` (`waits_for_another_session`), `guppi/prespec.py` (the finding `method waits for another session`), `guppi/casecheck.py` (`target_findings`, `lined_numbers`, `supersede_marks`). Tests: `tests/test_ledger.py` (4 new), `tests/test_lint.py` (2 new), `tests/test_prespec.py` (2 new), `tests/test_casecheck.py` (6 new, `-k dropped_target`). Handoff: `make test` 1258 passed, 6 skipped; `make style` clean.
- Readings: L1–L9 at `/hi` (8 passed, L8 `estimate-ask-searches-at-prespec` failed). Lesson: L10.
- The yaml: 48 entries, one per ledger line (L1–L48); 48 carry `applied`; 0 `failed`, 0 `exists`, 0 `incomplete`, 0 `near`; `unparsed: []`; no entry added by the index check or the synthesis. `generate` printed for L41, L42 and L43 "repeats line 16 / 17 / 20 of case 669.6 / 669.7 / 669.10; nothing applied".
- Pages created: decisions 28 (669 and 669.1–669.16, 670 and 670.1–670.7, 671, 671.1, 671.2); estimates 2 (`estimate-prespec-hook-reports-a-method-that-waits-for-another-session`, `estimate-case-check-sends-back-a-ratified-case-without-a-target`); lessons 1 (`lesson-orchestration-two-cases-built-side-by-side`).
- Pages updated: estimates 29 (9 readings L1–L9; 15 set `passed` by 669.1–669.15, `estimate-ask-searches-at-prespec` among both; 6 Criteria replaced by 670.1, 670.2, 670.3, 670.5, 670.6, 670.7); rules 20 (8 by decisions: `rule-ledger-write`, `rule-orchestration`, `rule-retro`, `rule-handoff`, `rule-case-protocol` (670.4, 671.2, 669.16), `rule-skill-hi`, `rule-estimates-schema`, `rule-work-mode`; 2 by a new Estimate: `rule-prespec-hook`, `rule-case-check`; 10 by the cascade alone); insights 1 (`insight-ledger-ratified-line-never-withdrawn` set `actioned`, `addressed_by: decision-case-671.1`, its Proposal line rewritten). Decisions 10 set superseded: 594, 617, 622, 630, 647, 657, 659, 665, 666, 667.
- Pages deleted: rules 1 (`rule-ledger-line-withdrawn-on-re-ratification`, 671.2).
- The cascade: `draft → built` on 12 rules — `rule-ask`, `rule-case-build`, `rule-case-protocol`, `rule-materialize`, `rule-orchestration`, `rule-page-generation`, `rule-permissions`, `rule-prespec`, `rule-search-leaves-out-decisions`, `rule-spec-reconcile`, `rule-spec-write`, `rule-synthesis`; `built → draft` on 3 — `rule-handoff`, `rule-ledger-write`, `rule-prespec-hook`. `rule-case-check` stays `draft` (new pending Estimate of 671.1).
- Pages archived by `generate` and `cleanup` (`cleanup: 13 page(s) moved`), under `vault/archive/migration/2026-10-05/1831/`: decisions 10 (the superseded ones above), lessons 2 (`lesson-ledger-a-dropped-item-needs-a-superseding-sub-case`, `lesson-case-build-renamed-a-slug-of-a-ratified-case-under-its-old-number`, by the actioned Insight), rules 1 (`rule-ledger-line-withdrawn-on-re-ratification`).
- The handoff checks: L1–L9 applied before the 669 updates (log: L8 set `estimate-ask-searches-at-prespec` `failed`, then 669.15 set it `passed`; the 669.15 Result keeps the L8 reading). The pages of 669.6, 669.7 and 669.10 were updated once; 659, 630, 617 and 622 were set superseded and archived. The three `rule-case-protocol` updates applied in ledger order L33 (670.4), L39 (671.2), L44 (669.16) with no error; `vault/wiki/case-schema.md` is one file, changed once in the tree. `backlog.md` went from 25 to 23 items: both `rule-ledger-line-withdrawn-on-re-ratification` and `insight-ledger-ratified-line-never-withdrawn` left it.
- `guppi materialize` extended the yamls of 0109, 0311, 1343 and 1616 with 0 entries; `generate` wrote `superseded_by` marks into the yamls of 0311, 1343 and 1616 (669.6, 669.12, 669.13, 669.14). The scripts ticked 45 boxes of the 1831 Spec, 1 `read` line of the 0311 Spec, 2 of the 1343 Spec and 7 of the 1616 Spec.
- The render wrote `.claude/skills/handoff/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/skills/work/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md` and `vault/wiki/estimates/schema.yaml`. `guppi sprint` and `guppi glossary` left `sprint.md` and `glossary.md` unchanged; `guppi backlog` rewrote `backlog.md`. No script printed a line on stderr.
- `guppi archive` printed nothing on stdout or stderr and moved no unit: the five units with a ledger (0109, 0311, 1343, 1616, 1831) are dated 2026-10-05, the day of the run, which it does not look at; the earlier dates of `vault/raw/` hold only `event_log.md`.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 81 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 32 lines.
- `lesson-orchestration-two-cases-built-side-by-side` — none: no index line holds a second Case started before the first was ratified outside the side-by-side forms `rule-orchestration` allows; `insight-prespec-after-findings-loop-unruled` names the absence of a rule for the loop after the findings, a loop the lesson says the rule now allows. It stays `new`.

## Readings due

Pending:
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — pending — `rule-ledger-write` stands `draft` — read: `- [ ] read` line of the 1831 Spec; `uv run pytest tests/test_ledger.py` (method).
- `estimate-retro-loads` — pending — `rule-retro` stands `draft` — read: `- [ ] read` line of the 1831 Spec; by hand, `.claude/skills/retro/SKILL.md` as rendered, against the Criterion (method).
- `estimate-handoff-holds-each-fact-once` — pending — `rule-handoff` stands `draft` — read: `- [ ] read` line of the 1831 Spec; by hand, `.claude/skills/handoff/SKILL.md` as rendered, against the Criterion (method).
- `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` — pending — `rule-prespec-hook` stands `draft` — read: `- [ ] read` line of the 1831 Spec; `uv run pytest tests/test_prespec.py tests/test_lint.py -k waits` (method).
- `estimate-hi-takes-its-readings` — pending — `rule-skill-hi` stands `draft` — read: `- [ ] read` line of the 1831 Spec; by hand, the skill file rendered from `rule-skill-hi`, against the Criterion (method).
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: `- [ ] read` line of the 1831 Spec; by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-work-mode-takes-the-work-readings` — pending — `rule-work-mode` stands `draft` — read: `- [ ] read` line of the 1831 Spec; by hand, the skill file rendered from `rule-work-mode`, against the Criterion (method).
- `estimate-case-check-sends-back-a-ratified-case-without-a-target` — pending — `rule-case-check` stands `draft` — read: `- [ ] read` line of the 1831 Spec; `uv run pytest tests/test_casecheck.py -k dropped_target` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no line of the 1831 Spec holds `guppi sprint-close`; none ran.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr, `backlog.md` rewritten, 25 → 23 items; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no `guppi sprint-close` line in the 1831 Spec, none run; `vault/archive/` received 13 pages from `cleanup` under `migration/2026-10-05/1831/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method).
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 22 lines — 4 `deferred`, 18 `unread`.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1258 passed, 6 skipped, on the working tree of this run.

No Estimate stands `failed`.

## Flags

- No entry marked `incomplete`, `failed` or `near`; `unparsed: []`.
- `generate` stdout: L41, L42 and L43 (669.6, 669.7, 669.10 with `{supersedes}` marks) repeat L16, L17 and L20; nothing applied for them; the yaml marks all three `applied`.
- Failed Estimates: none.
- 11 `- [ ] read` boxes stay open for Estimates that 669 set `passed`: 5 in the 0311 Spec (`estimate-spec-write-reaches-the-approved-spec`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-check-requires-a-backlog-item-decided-on-its-page`) and 6 in the 1616 Spec (`estimate-prespec-catches-a-superseded-case`, `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`, `estimate-case-build-writes-the-case`, `estimate-orchestration-shows-the-built-case`, `estimate-search-leaves-out-decisions-in-every-agent`, `estimate-synthesis-reads-the-status-its-yaml-sets`); no script of this run ticked them.
- Handoff, Direct instructions: "`backlog.md` should then count one item fewer" — it counts two fewer (25 → 23); the actioned `insight-ledger-ratified-line-never-withdrawn` left it too.
- Handoff, Observations: a re-ratification that only adds `{supersedes}` marks leaves the first ledger line beside the marked one (669.6, 669.7, 669.10); the check of 671.1 does not catch it.
- Handoff, Observations: the Estimates 670 updates keep their old methods, and several name a later `/hi`; the finding of 670.4 judges only a method a plan writes.
- Stale defers, from the lint: `rule-subagent-guppi` deferred 31 times since case 29; `rule-complaint-becomes-a-lesson` (since case 504), `rule-morph` (since case 239), `rule-prespec-judges-the-spec-whole` (since case 643), 1 time each.
- MOC candidates: none found. Contradictions: none found.
- The lint: 22 lines — 4 `deferred`, 18 `unread` (18 pending); no other finding; `make lint` exits red.
- Read beyond the frame: a Grep of `sprint-close` over the whole 1831 `spec.md` printed part of line 375, a `then` block line, beside its unticked lines; step 2 needed it to find a `guppi sprint-close` task line (none found).
- Read beyond the frame: line 11 of the 1831 `spec.md`, a quoted frame line the Grep of `- [ ]` matched and cut; Readings due and Next session needed to see whether it was a task line (it is not).

## Next session

Cases:
- Under 670.5 the next `/hi` reads no transcript, and an open W line it cannot take from files and commands becomes a Cases line; `estimate-hi-takes-its-readings` and `estimate-handoff-holds-each-fact-once` name a later session in their methods — whether their methods are rewritten to run in their own session (handoff, For the next session).
- The two ledger lines each for 669.6, 669.7 and 669.10: whether a re-ratification that changes only marks needs a check or a rule (handoff, For the next session; `generate` applied the second line of each as nothing).
- C3 `rule-sprint-close` and C4 the close of migration stay for the session that closes the sprint (handoff, For the next session).
- 11 `- [ ] read` boxes of the 0311 and 1616 Specs stand open for Estimates set `passed` by 669, and no script ticks them (this run's `git diff` of the Specs).

Work:
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
- `estimate-retro-loads`
- `estimate-handoff-holds-each-fact-once`
- `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
- `estimate-hi-takes-its-readings`
- `estimate-hi-writes-frontier`
- `estimate-work-mode-takes-the-work-readings`
- `estimate-case-check-sends-back-a-ratified-case-without-a-target`
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
- Ledger lines this run did not apply: none skipped; the ledger holds 48 lines and the yaml an entry for each; L41–L43 were marked `applied` with nothing applied, as repeats of L16, L17 and L20.

Ask the person:
- none

## Readings at the close

- `make test`: 1258 passed, 6 skipped.
- `make lint`: 22 lines — 4 `deferred`, 18 `unread`; red.
- Pages: decisions 1164, estimates 223, rules 78, lessons 80, insights 31, entities 4; `vault/archive/` 863 pages.
