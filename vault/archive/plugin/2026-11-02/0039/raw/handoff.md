# Handoff — 2026-11-02, the failed checks of case-build and orchestration, the link graph dropped

## Notes from memory

- The person asked for a plain account of each failed Estimate before taking it up (C2, C3, C4), and twice judged that the check itself, not the agent, needed changing: for 998 the person chose to count only what gets past the approved Spec, after four failures on readers that `/pre-spec` had caught.
- On C2 the main agent first proposed a hook that sets the `limit` of a Read of `.guppi/links.md` to the end of a block; the person rejected the frame — "Читать полностью 7000 строк, ты серьезно?" — and asked whether the vault, Obsidian pages with frontmatter, already gives the graph. Case 999 drops the graph whole for a search by the names in the frontmatter of the changed page. The person's words in the Case file are the source of that choice.
- For 998 Q1 the person chose (b), a reading at Retro and again after the next session, against the recommendation; `rule-retro` takes a reading once, so Q4 made it one reading after the next session, covering both.
- All three Cases were built again on the findings of `/pre-spec` and ratified again; `ask-guppi` confirmed its 7 findings closed.

## Direct instructions to the librarian

- Case 999.1 deletes `entity-link-graph`, `rule-link-graph-at-session-start` and their two Estimates; check that cleanup takes them out of the `children` and `estimates` lists of `rule-harness`, `entity-guppi` and `rule-case-build`, and that no live page keeps a `target` or `parent` on them.
- Case 999.2 renames `estimate-case-build-reads-the-link-graph-of-what-it-changes` to `estimate-case-build-searches-the-names-of-what-it-changes`; check that every link follows the rename, the `estimates` of `rule-case-build` included.
- The render of `.claude/settings.json` from the update of `rule-hook-registry` removes the `SessionStart` hook `guppi links --write`; check that the hook is gone from the file after `guppi render`.
- The reading of `estimate-sprint-plugin-check-finds-no-bare-slug-link` was taken at this Retro, before its page `estimate-link-graph-prints-the-neighbours` moves to the archive.

## What actually got done

- Cases ratified: 997, 998, 999 (999.1, 999.2).
- Code: `.guppi/guppi/links.py` and `.guppi/tests/test_links.py` deleted; `.guppi/guppi/cli.py` (import and `COMMANDS` entry of `links`, docstring), `.guppi/guppi/pages.py` (docstring), `.guppi/guppi/ship.py` (`LEFT_OUT` entry `.guppi/links.md`), `.guppi/.gitignore` (line `links.md`); the local `.guppi/links.md` deleted by hand.
- `uv run --project .guppi guppi test`: 1891 passed, 6 skipped, 1 deselected (1904 before; the 13 tests of `test_links.py` went with the module). `uv run --project .guppi guppi style`: clean.
- Readings: L14 `estimate-sprint-plugin-check-finds-no-bare-slug-link` `passed`. Lesson: L15 `lesson-grep-glob-brace-list-of-paths-matches-nothing` (knowledge).

## Debt

- No box of code, test or by-hand check is left; no patch.
- 18 boxes wait for the librarian.
- `estimate-orchestration-acknowledging-reply` — waits for the librarian's render that writes into `vault/wiki/orchestration.md` the paragraph of Case 997.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — waits for the Retro of the session after the one whose Spec holds a Case that changes a step, built on the Render of `rule-case-build`.
- `estimate-case-build-searches-the-names-of-what-it-changes` — waits for the `/pre-spec` of a session whose `case-guppi` runs on the Render of Case 999.2.
- `estimate-sprint-plugin-link-graph-is-gone` — an Estimate of the live sprint page, read once after the librarian's run that applies Case 999.1; its Retro is the next session's.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — an Estimate of the live sprint page; waits for the run of `.github/workflows/prod.yml` on a tag `prod-x.y.z`, or the close of `plugin`.

## Observations

- Red before the work (Baseline): `guppi check` exit 1, 7 lines — `status: a page with core: true that is draft` on `rule-case-build`, `rule-morph`, `rule-orchestration`, `rule-skill-approve-spec`; `unread: failed` on the three Estimates this session updates.
- Expected red: `guppi check` (lint, `path`) on `rule-link-graph-at-session-start`, whose `implementation_ref` names the deleted `links.py` and `test_links.py` — waits for the librarian's run that deletes the page.
- Expected red: the `SessionStart` hook `guppi links --write` of `.claude/settings.json` is an unknown command until the render of `.claude/settings.json` from `rule-hook-registry`; a `SessionStart` exit 2 blocks nothing (`lesson-hooks-sessionstart-cannot-block`).
- C1, the clean branch, was left in the sprint: a run of `prod.yml` now writes nothing to `prod` while a page with `core: true` blocks the build. After this librarian's run `rule-case-build` and `rule-orchestration` should block no more, their failed Estimates set `pending`; `rule-skill-approve-spec` and `rule-morph` were never `built` and still block. Judged from the statuses, not by a command.

## For the next session

- The tag `prod-x.y.z` that `estimate-sprint-plugin-ci-writes-a-clean-branch` waits for writes nothing while `rule-skill-approve-spec` and `rule-morph` block the clean build: whether to wait for their Estimates (the CLI trial of `/approve-spec`; the setup skill of `rule-morph` in the milestone The plugin), or to decide that `rule-morph` is not `core` until it is built.

## Ask the person

- `estimate-skill-approve-spec-takes-the-spec` — needs the person — on a copy of the repository, in the Claude Code CLI in a standalone terminal: does `/approve-spec`, typed after Esc and Shift+Tab, append the plan to `spec.md`, and is it blocked when typed in Plan Mode?
- `estimate-orchestration-names-the-typed-approval` — needs the person — in the same CLI trial: does the reply that calls `ExitPlanMode` hold, before the call, the conditional line on Esc, Shift+Tab and `/approve-spec`?
- `estimate-spec-box-runs-a-conserved-spec` — needs the person — on a copy of the repository, one session saves a small Spec by `/carry` and a second runs it by `/box`: does it come out as the Criterion says?
