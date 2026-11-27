# Handoff — 2026-11-27, sprint plugin: the map with boxes, the style check before each stop, the first sketch

## Notes from memory

- The picture of Case 1082 took three tries: the first export kept 4638×3710 at 1 092 135 bytes, the second came at 1000×800 but 709 414 bytes, over the bound of 500 000. The person chose to raise the bound rather than compress again, so Case 1086 replaced Case 1082 in Work Mode with a bound of 1 000 000 bytes. The person earlier picked about 1000 px themselves, knowing the small text blurs; the reading of `estimate-guppi-repository-readme-shows-the-first-sketch` at `/hi` judged the old picture and stands, as the `context` of the Case says.
- On Code Mode the person found it a weak option for now (no VS Code panel, no Remote Control) and asked whether its gains can be had without it. The answer: same quality, about 8% cheaper, slower. The person left it out; no Case, a `knowledge` lesson keeps the finding.
- For the map, the person wants to see the boxes in the plan file above all (Q1 c of Case 1085), against the recommendation of `spec.md` only.

## Direct instructions to the librarian

- Case 1086 supersedes Case 1082 whole: both `create` the same slug `estimate-sprint-plugin-first-sketch-picture-is-small`; only the line of 1086, with `{supersedes:case 1082}`, applies.
- Case 1085.2 updates `rule-hook-registry` by one `replace` pair whose `old` is `guppi shellwrite", "timeout": 30 } ] }`: check by a Grep that it hits the page once before `generate`; then `guppi render` writes the new `PostToolUse` entry `guppi ratified --boxes` into `.claude/settings.json`.
- Case 1085.1 updates `rule-spec-write` and `rule-spec-capture` by one `replace` pair each; `rule-spec-write` carries `deferred_by` of `decision-case-1081`, and no line of this session supersedes that defer, so it stays in the backlog.
- The lesson `lesson-work-mode-style-check-skipped-at-a-repeated-stop` carries `{addressed_by:case 1084}`; compare it with `lesson-…` pages of the style step of case 1061, if any.
- `tick_read`, `tick_spec`, `tick_command_lines` and `tick` now rebuild the map of each `spec.md` they tick. The first tick of `vault/raw/2026-11-27/0947/spec.md` rewrites its map, written in the old form with ✅ and no boxes, into the new form; that is the change the Case sets, not a fault.

## What actually got done

- Cases ratified: 1084; 1085 with 1085.1 to 1085.9; 1086. Case 1082 is superseded by 1086 and not counted.
- Code: `.guppi/guppi/ratified.py` — the boxes of the map, `rebuild_spec_maps`, `is_session_spec`, the mode `--boxes`, the `Stop` hook rebuilding the maps of `spec.md`; `.guppi/guppi/generate.py`, `render.py` and `sprint_close.py` — the tickers rebuild the maps; `.guppi/guppi/spec.py` — its docstring names the new writers of the maps. Tests: `test_ratified.py` (the `map` tests changed, `spec_map` tests added), `test_generate.py`, `test_render.py`, `test_sprint_close.py` (`spec_map` tests). `plugin/assets/GUPPI.png` replaced by the person's export, 1000×800, 709 414 bytes.
- `uv run --project .guppi guppi test`: 2058 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: at `/hi`, ledger lines 1 (`failed`) and 2 (`passed`); at Retro, lines 20 to 25, all `passed`. Lessons: line 4 (`knowledge`, Code Mode left out) and line 26 (`error`, the style step skipped at a repeated stop).
- The trial of 1085.9 ran in Work Mode on a scratch file.

## Debt

- No box is debt; no test was reverted.
- 23 boxes wait for the librarian: the page lines, the two `guppi render` lines and the `read` lines whose readings stand in the ledger.
- `estimate-work-mode-runs-the-style-check-before-a-stop` — waits for the first `/work` that loads after the librarian's render of `.claude/skills/work/SKILL.md` from the Render of 1084 and reaches a `stop:` task.
- `estimate-spec-write-shows-the-boxes-in-the-plan-file` — waits for the exit of Plan Mode and the first tick of Work Mode in the VS Code extension of the next session whose plan file holds a ratified Case.
- `estimate-render-harness-ticks-the-spec`, `estimate-sprint-ticks-the-spec`, `estimate-glossary-ticks-the-spec` — each waits for the librarian's run of this session, the `spec.md` of the session read against its Criterion after it.

## Observations

- The style step of `/work` ran before the first stop at the `stop:` task of Case 1082 (`All checks passed!`) and not before the two later stops at the same task, after the person's two exports that missed the bound; the lesson of line 26 holds it.
- The trial of 1085.9: an `Edit` after a command rewrote the file runs and writes, and gives back a note that the file changed on disk since the last read. So after the render of `--boxes`, each tick of Work Mode in `spec.md` after a rebuild of its map works with no new `Read`, with that note.
- An `Edit` of a task line of a `spec.md` with a map names the line by its start at the first character, since the same text stands indented in the map line.
- Case 1085 came back from the loop after `/pre-spec` under its own number with a new sub-case, 1085.9; the librarian may judge it against `estimate-orchestration-leaves-the-number-to-case-guppi`.
- To cross-check the PNG header once, `uv run --with pillow` ran from the repository root; it reported one package uninstalled in the root environment; no tracked file changed.
- No red before the work, no expected red.

## For the next session

- C1, the clean branch (`rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`), was put off again: the owner pushes `plugin` and a tag `prod-x.y.z`.
- Two options of the Code Mode answer were not built and are items only if the person asks: a rule that a task over many files goes through a script, and a trial that makes the start context of a session smaller without Code Mode.

## Ask the person

- `estimate-spec-write-shows-the-map-in-the-plan-view` — needs the person — at the exit of Plan Mode of session 1402, did the plan view in VS Code show the table, the Mermaid diagram and the signs of the map of the Cases as you want them? (That map still had signs and no boxes.)
