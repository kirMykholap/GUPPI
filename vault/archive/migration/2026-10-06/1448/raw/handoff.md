# Handoff — 2026-10-06, the ledger hook, the Case check and the transcripts permission

## Notes from memory

- The person took a side item, C7: a trial of the sample mod `token-weather`. The band it draws did not show in the Code tab of the mobile app, and the person chose to wait for an update of Claude Code (lesson L1). No Case came of it.
- The person picked C4, and the agent put off C1 and C2 (`rule-sprint-close`, the close of migration) as `[-] · sprint · defer` in the same reply, with no question of its own. The person did not object.
- The person called the four showings of one round "very bad" and asked for a fix; that became Case 692.
- Case 693: the person agreed that the allow rule binds to this machine alone. The name of the transcripts folder for another install went into the `purpose` of `rule-morph`, which no Estimate checks.
- After the findings of `/pre-spec`, Case 691 was built again as Case 695, with a new sub-case 695.2 on Retro, and its lines carry `{supersedes:case 691}`.

## Direct instructions to the librarian

- Case 691 (ledger lines L3, L4) is superseded by Case 695. The `create` of `estimate-ledger-write-refuses-a-line-that-is-no-record` stands on L4 and L13: one page, created under 695.1.
- The re-ratified lines of Cases 692 and 693 were not appended again, since their text was the same; each stands once in the ledger.
- Case 693, `rule-morph`: ask-guppi noted that the anchor `so a changed set rewrites no rule;` stands both in the frontmatter `purpose` and in the Purpose section. `guppi prespec --check` printed no finding on it. Check the page after `generate` against the Case.
- Case 695.2: ask-guppi did not open `rule-retro`, `rule-retro-onward` or `estimate-retro-runs-on-to-the-handoff` against its `old` texts. `guppi prespec --check` printed no finding on them. Check that each pair landed.
- The render writes `.claude/settings.json` (Case 693) and `.claude/skills/retro/SKILL.md` (Case 695.2).

## What actually got done

- Cases ratified: 692 (692.1, 692.2), 693, 694 (694.1, 694.2), 695 (695.1, 695.2).
- Code: `guppi/casecheck.py` — `turn_blocks`, `given_back_at`, `texts_after`, `last_refused` and `is_summary`. `texts_before_last_call` and `LEDGER_LINE` are gone, and `PREFIXES` is now imported from `guppi/ledger.py`. `guppi/ledger.py` — `held_message` and `reminder_message` take the slug alone, `named_cases` is gone, and `block_lines`, `stray_lines` and `stray_message` are new, with the hook refusing a line that is no record.
- Tests: `tests/test_casecheck.py`, `tests/test_ledger.py`. `make test`: 1330 passed, 6 skipped. `make style`: clean.
- Readings: L18–L23, all `passed`. Lessons: L1, L2, L24.

## Debt

- No box is debt; no test was reverted.
- 21 boxes wait for the librarian: the page lines, the two `guppi render` lines and the `read` lines of the Estimates read at Retro.
- `estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-brief-written`, `estimate-sprint-close-next-session-opens-the-sprint` — wait for the session after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` — wait for the Work Mode of the session that closes the sprint.
- `estimate-backlog-renders`, `estimate-sprint-close-runs-in-the-librarian-run` — wait for the librarian's run of the session that closes a sprint.

## Observations

- `make lint` was red before the work, exit 2, with 12 finding lines: `rules/rule-morph` deferred, and 11 `unread: pending` on the Estimates of `## Debt`. It was the same after the code changes. It was not run in Retro.
- No line stands under `## Expected red`.
- The new hook code is live from the commit of the work: the hold at Retro already asked "did a Case of this session fix its cause?" with no Case named.
- After the acknowledging reply of Cases 695, 692 and 693, the ledger reminder took the `Stop`, and the run stopped until the person said so (lesson L24).

## For the next session

- Lesson L24: whether the hook of `rule-prespec-onward`, or the rule for the answer to the ledger hook's reminder, sends the agent on to the check and the exit when no Cases line is open.
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint.

## Ask the person

- `estimate-permissions` — needs the person — in the first session after the librarian's render: did a Grep of a subagent on `~/.claude/projects/c--PROJECTS-GUPPI` itself, and on a file inside it, run with no permission prompt?
