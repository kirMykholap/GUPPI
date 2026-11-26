# Handoff — 2026-11-25, the event log, the sprint view, the license of the copy

## Notes from memory

- The session stood still at its first Case: `guppi caseid` found no plan file, since the event log cut its path at 80 characters. The person appended the whole path to `vault/raw/2026-11-25/event_log.md` by hand with `Add-Content` (line 30), after a first command for bash failed in PowerShell; every later hook of the session found the plan by that line. Case 1045 fixes the cause in `event.py`.
- The person questioned the logic of C6 — a one-off Estimate that can never pass while the sprint page asks every Estimate to pass. That talk led to Case 1046 (done means read for a one-off Estimate) and, at `/pre-spec`, to Case 1051 (the view ticks it). The person chose that the sprint page stays `draft` until the close, so "done" in its Purpose is not the status `built`.
- C7, the `given` of Case 1042.1, closed with no Case: the line stands only in the files of session 1353, which nothing reads.
- Case 1048: its `method` now waits for "the first /pre-spec that runs once this Criterion is set", which reads in two ways; Retro took this session's `/pre-spec`, the first after Case 1048 was ratified, as that event.
- Case 1049.2 was replaced in Work Mode by Case 1052: its `method` put the install by hand at a stop of this Work Mode, before the render of the skill it tests.
- The `case-guppi` of Case 1046 first wrote the Case beside it as `case-1050.md`, while 1050 is the short-form defer; it stands as 1051, and `case-1050.md` is empty.
- The `case-guppi` of Case 1052 got the same note of the check of `rule-case-check` twice ("the sentence around a pair was not read whole") and said it had read the sentences; the second note named two of the four pairs again, the third run passed.

## Direct instructions to the librarian

- Case 1046 and Case 1052 (for 1049.2) both update `entity-sprint-plugin`: 1046 its Purpose, the sentence that opens with `Done when every Estimate of this page passes:`; 1052 its `## Backlog`, the license line. Case 1050 defers the same page. Apply all three.
- Case 1049.2 is superseded whole by Case 1052; apply nothing of 1049.2.
- Case 1051 sets `rule-sprint` `draft` by the creation of `estimate-sprint-ticks-a-read-one-off-estimate`, which Retro read `passed`; `rule-sprint` carries `core: true`.
- After `guppi sprint`, the line of `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` under Done when of `sprint.md` should stand `- [x] … · failed`, if that page carries `once: true`.
- Cases 1047 and 1048 carry `{supersedes:case 1038}` and `{supersedes:case 1037}`: the two Estimates leave `backlog.md`.

## What actually got done

- Cases ratified: 1045, 1046, 1047, 1048, 1049.1, 1050 (a defer of `entity-sprint-plugin`), 1051, 1052. Case 1044 was dropped.
- Code: `.guppi/guppi/event.py` (`WHOLE_KEYS`, a `file_path` stays whole), `.guppi/guppi/ship.py` (`LICENSE` in `ROOT_FILES`, `LICENSE_FILES` to `.guppi/LICENSE`), `.guppi/guppi/ledger.py` (`is_one_off`), `.guppi/guppi/lint.py` (imports it), `.guppi/guppi/sprint.py` (ticks a failed one-off Estimate). Tests: `.guppi/tests/test_event.py` (2 new), `.guppi/tests/test_ship.py` (2 new), `.guppi/tests/test_sprint.py` (1 new).
- `guppi test`: exit 0, 1983 passed, 6 skipped, 2 deselected. `guppi style`: clean.
- Readings at `/hi`: L1 `failed`, L2 `passed`, L3 `failed`. Lesson L4. Readings at Retro: `estimate-event-log-keeps-the-whole-path`, `estimate-clean-branch-ships-the-license`, `estimate-sprint-ticks-a-read-one-off-estimate`, `estimate-ask-searches-at-prespec` and `estimate-case-build-searches-the-names-of-what-it-changes`, all `passed`; lessons `lesson-case-build-numbers-a-new-case-from-the-case-files-alone` and `lesson-case-build-puts-a-reading-before-the-render-it-tests`.

## Debt

- No box of code, a test or a command is left unticked.
- The other unticked boxes wait for the librarian: the page lines, the render line and the sprint lines, and the `read` lines of the two Estimates below.
- `estimate-sprint-plugin-done-counts-a-one-off-reading` — waits for the librarian's run of this session.
- `estimate-plugin-install-writes-guppi-into-an-empty-project` — waits for the librarian's run of this session, then an install by hand in a later session, in a project that holds only a `LICENSE` of its own.
- `estimate-plugin-install-asks-one-approval-in-plan-mode`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-git-context-offers-git-init` — each waits for installs by hand from an `--allow-draft` copy.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — waits for an acknowledging reply after `/pre-spec` that waits for the person's word; none came in this session.

## Observations

- Expected red: `guppi sprint --check`, a step of `guppi check`, prints `sprint: vault/wiki/sprint.md differs from entity-sprint-plugin` until the librarian's `guppi sprint` renders `vault/wiki/sprint.md` with the tick of Case 1051.
- Red before the work (Baseline): `guppi check` exit 1 — three `core: true` pages `draft` (`rule-ask`, `rule-case-build`, `rule-morph`) and three `unread: failed` Estimates (`estimate-ask-searches-at-prespec`, `estimate-case-build-searches-the-names-of-what-it-changes`, `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`).
- Claude Code now names a plan file with `-of-<session uuid>`; a subagent in Plan Mode is offered a plan file whose name adds `-agent-<id>`. With whole paths, a subagent that writes such a file with a title line alone would be taken by `plan_path` as the session's plan; Case 1045 left this out by the person's choice.
- The reading of `estimate-orchestration-dispatches-case-guppi-at-a-level` (`failed`) shows the level is set at dispatch from the item, before the Case is known to touch a hook.
- The reading of `estimate-case-build-searches-the-names-of-what-it-changes` judged most of the 600-odd listed files by the group reasons of `context`, not one by one; the notes of 1049 and 1051 listed 138 and 204 files.

## For the next session

- `estimate-orchestration-dispatches-case-guppi-at-a-level` failed: the level of the dispatch is judged from the item before the Case is built; whether the rule or the Criterion changes.
- `estimate-case-build-settles-form-by-itself` failed: two rounds of session 1353 asked a choice of form (a new Estimate or a replaced Criterion); whether the Render of `rule-case-build` or the Criterion changes.
- `lesson-case-build-numbers-a-new-case-from-the-case-files-alone`: a short-form Case has no case file, and a new Case beside a ratified one took its number.
- `lesson-case-build-puts-a-reading-before-the-render-it-tests`: a `method` asked for a reading of a Render before its render; the fifth question of `ask-guppi` at `/pre-spec` did not catch it.

## Ask the person

- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?
