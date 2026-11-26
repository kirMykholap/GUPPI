# Handoff — 2026-11-25, the guard of a case number, the install readings and one-off Estimates

## Notes from memory

- The person asked why parts that passed before were read again, and why not one project. Case 1055 then settled on five projects, since three Criteria exclude each other.
- The person reversed Cases 1046 and 1051 in their own words: a failed reading is not done, and `once` means that one passed reading is enough. The wider rule, that a passed one-off Estimate is never read again when its pages change, was not ratified. It stands only as the Backlog line that Case 1057.1 adds to `entity-sprint-plugin`.
- The person reported "a problem in p2". It was the red style of the copy, which the error lesson of this session records, and not a fault of the install.
- The push of `plugin` at the stop of Case 1055.5 carried the commits before this session's work. The work and the session folder were committed after it, so `plugin` is ahead of `origin/plugin` again.

## Direct instructions to the librarian

- Case 1055.5 carries `{supersedes:case 949}`: the put-off of `estimate-plugin-install-sets-aside-the-files-of-the-project` is retired, not applied.
- Case 1053 and Case 1057 were each ratified twice, after `/pre-spec`. The second form of each stands.
- The readings of the five install Estimates were taken on their new `method`. Write each `method` first, then the reading.
- `vault/wiki/sprint.md` must be rendered after `entity-sprint-plugin` changes. The failed one-off line of `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` is no longer ticked.

## What actually got done

- Cases ratified: 1053.1, 1053.2, 1054.1, 1054.2, 1055.1–1055.5, 1057.1–1057.5.
- Code:
  - `.guppi/guppi/ratified.py`: `held_number` refuses a first write of a case file whose number has a decision line in the session's ledger.
  - `.guppi/guppi/prespec.py`: `check_stop_before_render`, with `code_spans` over `lint.CODE_SPAN`.
  - `.guppi/guppi/sprint.py`: ticks only a `passed` Estimate.
  - `.guppi/guppi/sprint_close.py`: settles an Estimate of the sprint page only by `--archive-unread`.
  - `.guppi/guppi/ledger.py`: a docstring.
- Tests:
  - `.guppi/tests/test_ratified.py`: five tests `number_held` on the ledger.
  - `.guppi/tests/test_prespec.py`: six tests `stop_before_render`.
  - `.guppi/tests/test_sprint.py`: `test_a_failed_one_off_estimate_stays_unticked_and_keeps_its_status`, renamed.
  - `.guppi/tests/test_sprint_close.py`: `test_settle_failed_sprint_page_estimate_only_by_archive_unread`, renamed and rewritten.
- `uv run --project .guppi guppi test`: 1994 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 (Work reading at `/hi`), L23–L31 (Retro). Lessons: L32 (knowledge), L33 (error).
- By hand:
  - The clean copy was written under `C:/tmp/guppi-1055/copy`.
  - The five test projects stand under `C:/tmp/guppi-1055/`.

## Debt

No box of the Spec is debt. 38 boxes wait for the librarian.

- `estimate-orchestration-dispatches-case-guppi-at-a-level`: waits for a session whose `orchestration.md` holds the new Render of Case 1054.1. Its first part, the Render in the Spec read against the Criterion, holds.
- `estimate-case-build-settles-form-by-itself`: waits for a session whose `case-guppi.md` holds the new Render of Case 1054.2. Its first part, read the same way, holds.
- `estimate-sprint-plugin-done-counts-a-one-off-reading`: waits for the librarian's run of session 0816.
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`: waits for a `case-guppi` build of the sprint `plugin` whose Case adds a file outside `vault/wiki/`. No Case of this session added one.
- `estimate-sprint-close-takes-the-readings-in-groups`: waits for the Work Mode of a session that closes a sprint.

## Observations

- Expected red: the step `guppi sprint --check` of `uv run --project .guppi guppi check` is red on `vault/wiki/sprint.md` until the librarian renders it from `entity-sprint-plugin`.
- Red before the work, by `## Baseline`: `rules/rule-case-build`, `rules/rule-morph` and `rules/rule-orchestration` print `core: true that is draft`. `estimate-case-build-settles-form-by-itself`, `estimate-orchestration-dispatches-case-guppi-at-a-level` and `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` print `unread: failed`. The first two Estimates are now `pending` by Case 1054. The third is `pending` by Case 1057.4.
- In p1 and p2 the Claude Code CLI could not approve the long plan of the session at `ExitPlanMode`. `/approve-spec` approved it.
- `uv sync` in each test project warned that `build_system.requires = ["uv-build>=0.11,<0.12"]` of `.guppi/pyproject.toml` does not hold uv 0.13.10. The build passed.
- The setup Case of p2 first proposed the transcripts folder with a lower-case `c--`. A Glob found the folder with an upper-case `C--`, and the Case used that name.

## For the next session

- Whether the copy for an install stop is written only after `uv run --project .guppi guppi style` is clean, or Work Mode runs the style check before a stop that hands over a copy. The error lesson of this session records the cause.
- Whether `.guppi/pyproject.toml` should widen its `uv-build` bound past 0.12.
- The Backlog line of Case 1057.1: whether a passed one-off Estimate is never read again.

## Ask the person

- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?
