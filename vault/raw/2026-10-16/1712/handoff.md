# Handoff — 2026-10-16, sprint plugin: neutral texts of the clean version, the close commit, backlog cleanup

## Notes from memory

- On Case 861 the person doubted the rule: a MOC with no parent, such as `entity-guppi`, could fairly name `guppi test`, since the whole suite is exactly its tests. The person took the quick fix (a reading by hand) and left the wider rule open.
- Case 858 was ratified, then taken back at /pre-spec once case-guppi read Case 358 and found that its precedent does not hold. The correction of the Context of `decision-case-855` now stands only in `vault/raw/2026-10-16/1712/cases/case-858.md`.
- Case 856.2 is checked by a narrowed list: the known Criterion line of `estimate-ratification-case-id-carries-the-sprint` on the sprints `migration` and `plugin` may stay on the list of the next reading. The person chose to leave that Estimate as it is.
- The person deferred C1 (the clean-branch milestone) and C3 (the install readings) at the end of Plan Mode with no discussion.

## Direct instructions to the librarian

- Case 858 (ledger line 15) is superseded by the take-back Case 863 (line 23, `{supersedes:case 858}`): line 15 must not change `decision-case-855`.
- Case 859 (line 16) carries `{supersedes:case 855}` and retires the one defer of `decision-case-855`, so the cascade archives that page. Case 863 then puts a `defer` on the same page. Check that `generate` takes a defer on a Decision page that the same run archives, and say in the brief what the page holds after the run.
- Case 861 (line 18) carries `{supersedes:case 829}`. `estimate-page-schemas-one-file-per-rule` keeps `decision-case-829` in its `deferred_by` and stays in `backlog.md`, as the last `then` line of Case 861 sets it.
- Cases 856.1 and 856.3 both update `rule-rules-schema` with `replace` pairs. Apply both.
- The Cases built again after /pre-spec (856, 859, 861) were ratified twice, and the ledger holds each of their lines once.
- This run's close commit still uses the four fixed paths: the agent file with the new Render of `rule-close` loads only at the next dispatch.

## What actually got done

- Cases ratified: 856 (856.1, 856.2, 856.3), 857, 859, 860, 861. Short defers: 862 and 863.
- Code: `.guppi/guppi/render.py` gets `--paths`, which prints each file the render writes and writes nothing; it is mutually exclusive with `--check` and `--sync`. Tests: three new tests in `.guppi/tests/test_render.py` (paths printed once with nothing written, a render error that prints no path and exits 1, `--paths` with `--check` or `--sync` exits 2).
- The dirty `plugin/skills/install/SKILL.md` left by the librarian of session 0342 is committed with the work.
- `uv run --project .guppi guppi test`: 1722 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 (`estimate-hi-no-read-calls`, passed, at /hi). Lessons: L24, L25, L26.

## Debt

- No box of code or test is left unticked.
- 25 boxes wait for the librarian or for the moment of their Estimate's reading.
- `estimate-clean-branch-ships-neutral-texts` — after the librarian's run of session 1712: `guppi ship --allow-draft` into an empty folder, every sentence read whole.
- `estimate-rules-schema-checked` — after the librarian's run of session 1712: the live `vault/wiki/rules/schema.yaml`.
- `estimate-close-commits` — after the librarian's run of the next session, whose agent file holds the new Render of `rule-close`. Its pytest part, `test_render.py -k paths`, passes now.
- `estimate-clean-branch-writes-the-session-files` — after the librarian's run of session 1712, in the install session with an empty folder with no git.
- `estimate-git-context-offers-git-init`, `estimate-plugin-install-offers-to-install-uv`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` — one install session by hand: no git, no `uv`, offline (deferred by Case 862).

## Observations

- Red before the work: `guppi check` exit 1 with 12 lines (seven draft pages with `core: true`; `unread: failed` on `estimate-clean-branch-ships-neutral-texts` and `estimate-clean-branch-writes-the-session-files`; `method` on `estimate-guppi-tests-green`, `estimate-harness-make-runs-in-both-shells` and `estimate-page-schemas-one-file-per-rule`). No expected red.
- `uv run --project .guppi guppi render --paths` over the live vault printed 32 paths, `plugin/skills/install/SKILL.md` among them.
- The new close command of Case 857 joins `git add` and `git commit` with `&&`, which Windows PowerShell 5.1 does not parse. The claim that the `$(...)` form runs in both bash and PowerShell was not checked in PowerShell. The librarian runs the command with the Bash tool.
- At /pre-spec, ask-guppi read `decision-case-829`, `-833`, `-849` and `-855` and used their `defer` lists to answer the person's doubt, which goes beyond the reason `.claude/rules/search-leaves-out-decisions.md` asks for. No finding rests on that reading.
- At /pre-spec ask-guppi found four wrong facts in ratified Cases. Three of them became the lessons L24–L26; the fourth, the stale description of Case 858 in Case 859, followed from the take-back.

## For the next session

- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, was left for later again: seven draft pages with `core: true` stop every build of `prod`, and the next tag after `prod-0.2.0` is open. `rule-guppi-package` and `rule-work-mode` in the backlog are two of those seven.
- Whether `rule-estimates-schema` and `names_a_moc_form` of `.guppi/guppi/lint.py` let a MOC with no parent name `guppi test` alone (the person's doubt on Case 861).
- The Context of `decision-case-855` still says that Case 851 makes `/hi` go on to `/sprint-open`. Case 863 deferred it, and `rule-decisions-schema` allows no correction line.
- `estimate-page-schemas-one-file-per-rule` still needs a `method` that lint accepts. Its `deferred_by` points at `decision-case-829`, which this run archives.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
