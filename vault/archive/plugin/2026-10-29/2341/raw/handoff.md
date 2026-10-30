# Handoff — 2026-10-29, the librarian's report and the items of the brief of 1930

## Notes from memory

- The person first read the report of session 1930 from another text and gave 15 created, 25 updated and a lint of 12 lines; the reading L3 `failed` rests on it, and L5 `passed` replaces it after the case-guppi of Case 913 quoted the real report. The baseline `guppi check` of this session printed 12 lines, `backlog.md differs from its sources` among them, which may be the text the person read.
- The person asked where the twenty-line limit of the report came from, saw no point in it and dropped it (Case 913). The History of `rule-close` shows no Case that added it after its creation in case 36.1; that origin is an inference, not a record.
- On Case 915 the person rejected every option of the first round: a later Case may still fix a lesson, only an `error` lesson needs the judgment, and the question should not cost a reply in the chat. The chosen form puts the mark into the Case that `case-guppi` builds.
- The person put off C1 (`rule-clean-branch`, the CI run on a tag `prod-x.y.z`) with no Case.
- A3 (`estimate-guppi-package-is-ready-after-the-install`) was not answered: no install from a clean copy was made, and Case 918.4 moved its reading after this session's librarian run.

## Direct instructions to the librarian

- Apply the ledger in order. `estimate-close-reports-in-twenty-lines` takes L3 `failed`, then L5 `passed`, then the `update` of Case 913, which replaces its Criterion, `purpose` and `method`, sets it `pending` and renames it `estimate-close-reports-the-run`; the `estimates` link of `rule-close` follows the rename.
- `estimate-close-commits` takes L1 `passed`, then L8 `failed`, then the `update` of Case 914, which sets it `pending`. `guppi render --paths` now prints bare line feeds: run the close command as `rule-close` writes it, with no `tr -d '\r'`, and say in the report whether it passed at its first run.
- Two Cases change each of these pages in different places: `rule-orchestration` (915.1, 916.1), `rule-case-build` (915.2, 916.2), `rule-ledger-write` (915.1, 915.3). Each `old` string was counted once on its page at Retro.
- The readings of Retro, L30–L39, follow the decision lines of their Estimates and read the Criterion the Spec sets.

## What actually got done

- Cases ratified: 913; 914; 915 (915.1–915.3); 916 (916.1, 916.2); 917 (917.1, 917.2); 918 (918.1–918.4). Cases 913, 915, 916, 917 and 918 were built again on twelve findings of `/pre-spec` and ratified again with the same lines.
- Code: `.guppi/guppi/render.py` (`--paths` sets `newline="\n"` on its stdout), `.guppi/guppi/ledger.py` (`unaddressed`, `reminder_message` and the reminder removed; `unmarked_lessons` leaves out a `knowledge` lesson unless a marked line of its slug stands), `.guppi/guppi/materialize.py` (`unlinked_lessons` removed), `.guppi/guppi/onward.py` and `.guppi/guppi/sprint_close.py` (docstrings).
- Tests: `.guppi/tests/test_render.py` gains a test that runs `--paths` as a child process and finds no carriage return; it failed with the old `render.py`. `.guppi/tests/test_ledger.py` replaces the eleven reminder tests and the `unlinked_lessons` test with five tests of no reminder and two of a `knowledge` lesson.
- `guppi test`: 1786 passed, 6 skipped, 1 deselected. `guppi style`: clean.
- Readings: L1, L2, L5 at `/hi`; L3 and L8 `failed`; L30–L39 at Retro, all `passed`. Lessons: L4, L40, L41.

## Debt

- No box is debt. No red test, no patch.
- 41 boxes of the Spec wait for the librarian: page lines, render lines and `read` lines.
- `estimate-close-reports-the-run` — waits for a librarian's run whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close` when the run starts, which is the run of the next session, then the person's answer on its report.
- `estimate-close-commits` — waits for this session's librarian run: `git log` and `git status` after its commit, and whether the close command passed at its first run; its pytest part passed at Retro.
- `estimate-guppi-package-is-ready-after-the-install` — waits for this session's librarian run, then an install from a clean copy by `guppi ship --allow-draft` at a stop of Work Mode, and the person's answer.
- `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-signs-items-taken-together` — their `method` changed only; each waits for a line `**Other Case:**` that names a Case of the session under the new Render of `rule-orchestration`.

## Observations

- Red before the work: `guppi check` exit 1, 12 lines, `backlog: vault/wiki/backlog.md differs from its sources` among them, and ten `core: true` pages standing `draft`.
- After the librarian's run `rule-sprint-close`, `rule-event-log` and `rule-python-utf8` read their new Criteria as `passed` at Retro; `rule-close` keeps two `pending` Estimates, so `guppi ship` without `--allow-draft` still writes nothing to `prod`.
- When C1 was put off, the main agent did not send the `**Other Case:**` change of Case 918.4 back to Case 918, since the rule of Case 916 was not yet rendered; finding 3.2 of `/pre-spec` brought the same fix.
- `.guppi/tests/test_onward.py` keeps two test names and docstrings that speak of the reminder of the ledger hook; they pass, since they test a refusal of the ledger hook in general.
- Case 917 has no `**Change**` item for its fix of a `/pre-spec` finding, while 913, 915, 916 and 918 have one for each such fix.
- The premise of the brief that no module writes a `.gitignore` into the clean version was half wrong: `guppi ship` writes `vault/.gitignore`.

## For the next session

- Five shipped Estimates hold Criterion sentences true only in the repository of GUPPI, by the Result of `estimate-clean-branch-ships-neutral-texts`: `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-example-passes-the-check`, `estimate-ratification-case-id-carries-the-sprint`. Case 918 left their rewrite to a later Case.
- An `A` line of `/hi` that asks the person to judge a text the main agent cannot open names no place to find it and quotes none of it (lesson L41).
- `rule-clean-branch` stands `built` and keeps `deferred_by: decision-case-893.1`; that defer still holds four Estimates whose rewrite waits: `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-ask-query-before-a-create`, `estimate-compact-recall-reloads`.

## Ask the person

- `estimate-plugin-install-runs-no-hook-before-uv-sync` — needs the person — Have you made the two installs by hand from a clean copy written by `guppi ship --allow-draft`, one normal and one with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR`? If so, did the project hold no `.claude/settings.json` until `uv sync` passed, and did no hook error show after the rollback of the offline one?
