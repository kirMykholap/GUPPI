# Handoff — 2026-10-29, the items of the brief of 0327

## Notes from memory

- The person took every recommendation of every round and asked one discussion question: how `/guppi:install` treats a project that already holds its own `.claude/settings.json`, `CLAUDE.md` and hooks. The answer was that step 3 refuses such a project whole. The person then asked for a way to install GUPPI into an existing project. It became a Frontier item and was put off by Case 911.
- In the summary of Case 902, the `**Other Case:**` line named an item that was not yet a Case: C7, the rewording of `estimate-close-commits`. `vault/wiki/orchestration.md` sets that line only for a Case of the session that stands. The main agent showed 902 as it stood and passed the change into the prompt that later dispatched Case 903.
- Case 905 came back from `/pre-spec` with sub-cases. A ratified Case with no sub-cases may not come back under its number in another shape, so `case-guppi` built it again as Case 912, whose lines carry `{supersedes:case 905}`.
- The /hi reading of `estimate-clean-branch-ships-neutral-texts` (L1) rests on six reading agents. The main agent judged their doubtful sentences as holding: `CLAUDE.md` naming English and Russian from the values of `rule-guppi-config`, `PLAIN_SPRINTS` in `rule-ratification`, the Makefile in `rule-rules-schema`, and `guppi.toml` in `rule-guppi-config` and `rule-morph`.

## Direct instructions to the librarian

- Case 905 (L10, L11) is superseded whole by Case 912 (L18–L20). No page takes an entry of 905.
- The decision lines of Cases 902, 903, 904, 908.1 and 908.2 were ratified a second time after `/pre-spec`. The ledger keeps only the first lines, which are the same text. The Spec holds the texts built again, and those are the ones to apply.
- `decision-case-885` is superseded by both Case 902 and Case 903.1, so its `superseded_by` takes both. `decision-case-891` is superseded by Case 902. Both stand archived, and both should stay archived. Check after `generate` that neither `estimate-spec-write-writes-a-defer` nor `estimate-close-commits` carries `deferred_by`, and that both leave `backlog.md`.
- Case 912.1 changes `rule-plugin-install` and Case 911 defers the same page. `/pre-spec` printed this as a note. Both entries apply.
- `## How it works` of `rule-spec-reconcile` was removed by hand in Work Mode as the task of Case 904.1 set it. The `update` of 904.1 on that page is a History line, and the section should not come back.
- The render line of Case 912 writes `plugin/skills/install/SKILL.md`.

## What actually got done

- Cases ratified: 902; 903 (903.1, 903.2); 904 (904.1–904.3); 908 (908.1–908.3); 912 (912.1, 912.2). Short-form defers: 907 (`rule-ratification`), 909 (`rule-spec-capture`), 910 (`rule-skill-sprint-open`), 911 (`rule-plugin-install`). Case 906 was dropped for the defer of 907 and holds no decision line.
- Code: `.guppi/guppi/casecheck.py` lost the old path of the `SubagentStop` check (`answer_of` and `write_case_files` removed, docstrings follow). `.guppi/guppi/ratified.py` got a docstring only. Tests: `.guppi/tests/test_casecheck.py`, whose helpers `answer` and `transcript` now write a Case into its file and whose old-path tests were removed or rewritten to assert that nothing is stored; `.guppi/tests/test_case_schema.py`, which reads `case-example.md` alone.
- `uv run --project .guppi guppi test`: 1790 passed, 6 skipped, 1 deselected. The baseline was 1792: five old-path tests went and three came. `uv run --project .guppi guppi style`: clean.
- Readings: L1 at /hi, and L22–L25 at Retro, all `passed`. Lesson: L26.

## Debt

- No box is debt. The boxes left open wait for the librarian: the page lines, the render line and the `read` lines whose readings stand in the ledger.
- `estimate-close-commits`: waits for a librarian's run whose `.claude/agents/librarian-guppi.md` holds the Render of `rule-close` when the run starts. The run of this session is one, so it can be read at the next `/hi` by `git log`, `git status` and `test_render.py -k paths`.
- `estimate-close-reports-in-twenty-lines`: waits for the same run. The person's answer on the report of this session's run is the reading.
- `estimate-plugin-install-runs-no-hook-before-uv-sync` and `estimate-guppi-package-is-ready-after-the-install`: wait for the librarian's run of this session, with a tag `prod-x.y.z` in the history of HEAD. Then come two installs by hand from a clean copy: one normal, one offline with an empty `uv` cache.
- `estimate-orchestration-shows-the-built-case`: waits for the first summary of `case-guppi` in Plan Mode that carries a line `**Other Case:**` naming a Case of the session that stands. This session's line named an item that was not yet a Case.

## Observations

- `uv run --project .guppi guppi check` was red before the work with 10 lines, and Work Mode added none: `backlog: vault/wiki/backlog.md differs from its sources`, the 8 pages with `core: true` that stand `draft`, and `estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`.
- `/pre-spec` found 10 faults in Cases already shown and ratified, all closed when the Cases were built again. The lesson of L26 covers two of them.

## For the next session

- `vault/wiki/orchestration.md` does not set what the main agent does with an `**Other Case:**` line that names a Frontier item not yet built as a Case.
- The /hi reading of `estimate-clean-branch-ships-neutral-texts` lists Criterion sentences that hold only in the repository of GUPPI. Cases 904 and 908 rewrote some of them. These remain:
  - `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` (English named, not by role);
  - `estimate-guppi-package-is-ready-after-the-install` (its new Criterion of Case 912.2 should be checked against that list);
  - `estimate-sprint-close-moves-old-event-logs` (`.gitignore`);
  - `estimate-python-utf8-output-intact` (cp1252);
  - `estimate-synthesis-keeps-actioned-by-the-mark`, whose case reference `(302.2)` `guppi ship` left in its prose;
  - the four Estimates still under the defer of `decision-case-893.1`.
- The `method` of `estimate-sprint-close-moves-old-event-logs` reads a line of `.gitignore`. The clean version holds no `.gitignore`, and no module writes one.

## Ask the person

- `estimate-permissions` — needs the person — In this session's Plan Mode, did Claude Code ask you before `case-guppi` wrote each case file under `vault/raw/2026-10-29/1930/cases/`? And did you see any prompt at a Grep or Read of a subagent on the folder of saved transcripts? (The allow list of `.claude/settings.json` matches the Criterion, and `test_render.py -k json` passed, 4 tests.)
