# Handoff — 2026-10-12, sprint plugin: the supersede list, the waiting sprint reading at /hi, the Criterion of the sprint opening

## Notes from memory

- Case 778: the person first proposed a wider path: every reading that `/hi` cannot take stays in Work, the librarian flags it, and the next `/hi` puts it into the backlog by a defer, so that no session opens with what cannot be read. The person also asked whether `pending` Estimates stay visible. After the answer (Readings due of the brief, `unread: pending` of `make lint`, the handoff) the person agreed to the narrow change, the Estimates of the live sprint page only. The person said plainly that Estimates may wait for events other than the close of a sprint; Case 778 left that out on purpose (its question 5).
- Case 777 was ratified on the recommendation to drop only the transcript words; `/pre-spec` showed that the rest of the `When` line kept the same defect, and the person chose to rewrite the trigger, so Case 779 replaces it.
- The milestone line of GitHub pull requests was put off untouched again, at the person's word "откладываем и идём работать".

## Direct instructions to the librarian

- Case 779 carries `{supersedes:case 777}`; both update `estimate-sprint-close-next-session-opens-the-sprint`, and Case 777 left the Spec. Check that the page holds the Criterion of Case 779 and that `decision-case-777` is marked superseded by 779.
- `guppi materialize` now writes the entry-level `superseded_by` as a list (case 776): the yaml of this unit marks the entries of 777 `superseded_by: ['779']`. A one-value field in an older yaml is read as a list of one.
- Case 778 rewrites two sentences of `rule-skill-hi` by `replace`; each `old` string stood once on the page at Retro. Check the render of `.claude/skills/hi/SKILL.md`.
- `guppi prespec --check` printed three `note:` lines that a Criterion line is not carried (778 twice, 779 once); each is dropped on purpose and named in the context of its Case.

## What actually got done

- Cases ratified: 776, 778, 779.
- Code: `guppi/materialize.py` — `mark_superseded` reads the entry's `superseded_by` through `cases_of` and appends the Case when the list does not hold it; the docstrings of `cases_of` and of the module name the list. Tests: `tests/test_materialize.py` — the entry assertions compare to a list; two new tests: two lines that retire one Case are both listed in ledger order; a one-value mark of an older yaml is appended to, and a Case already listed adds nothing.
- `make test`: 1497 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 7, 8 and 9, all `passed`. Lesson: ledger line 10.

## Debt

- No box of code, test or command is debt.
- 9 boxes wait for the librarian: the page lines and `read` lines of Cases 776, 778 and 779, and the render line of `.claude/skills/hi/SKILL.md`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — the `/hi` of the session after the one whose Work Mode writes README.md, before the close of the sprint.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — the Retro of the session that finishes the GitHub milestone, or the close of the sprint.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — the Retro of the session that finishes the milestone The clean branch, or the close of the sprint.
- `estimate-sprint-plugin-installs-as-a-plugin` — the Retro of the session that finishes the milestone The plugin, or the close of the sprint.
- `estimate-hi-writes-frontier` — the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of `/sprint-open`.
- `estimate-brief-written` — the person's answer at the `/hi` after the librarian's run of the session that closes a sprint.

## Observations

- The archived yaml `vault/archive/plugin/2026-10-10/1913/raw/materialize.yaml` keeps `superseded_by: '775.2'` on both `defer` entries of case 771, by the person's choice in Case 776; its `decisions` record of 771 names both 775.1 and 775.2.
- `ask-guppi` reported that once it ran a content Grep over an archived yaml, which its frame forbids; no finding rested on it.
- The `make lint` of the baseline printed the same 8 lines the brief named (`rule-morph` deferred, 7 `unread: pending`); they were red before the work. `make lint` was not run after the work.

## For the next session

- Estimates that wait for an event other than the close of a sprint — a moment that the rule on methods (`rule-case-protocol`, case 670.4) now has pre-spec report — and the path the person proposed for a reading that `/hi` cannot take: Work, a flag of the librarian, a defer into the backlog at the next `/hi`. Case 778 left both out.
- The cause of the lesson of ledger line 10: `case-guppi` judged a Criterion against the item's own words and not against `rule-case-protocol` (case 670.4), so its recommended option kept the defect.
- The milestone line "the repository on GitHub set up so that a pull request from another person is easy to review" still holds the current milestone open alone.

## Ask the person
