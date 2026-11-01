# Handoff — 2026-11-01, the stale defers, the backlog check, the builder's search and /approve-spec

## Notes from memory

- The person asked why the two Estimates stayed deferred by archived decisions and wanted the cause fixed, not only the two pages; the person also asked whether the build of a Case sees the cascade. It does: `cascade_notes` of `/pre-spec` and of the check of a case file now read the same keep judgment as the cascade.
- The person asked for a plain re-pitch of the round of Case 983 before agreeing.
- The person named the command `/approve-spec`, not the recommended `/approve`.
- Case 987.2 changed its moment twice: first "after a refused exit", then, since the Claude Code docs quoted in its `context` say that Esc at the plan dialog stops the turn, one line worded as a condition in the reply that calls `ExitPlanMode`. The docs quoted there were read by `case-guppi`; `ask-guppi` did not read them.
- At `/pre-spec` the person agreed that the trials of `/approve-spec`, of the line of 987.2 and of `/box` wait for this run's render, since a copy taken in Work Mode would hold the old harness.
- The person took three backlog items one at a time: the insight, `rule-ratification`, `rule-spec-box`. For `rule-ratification` the person chose that the put-off removal of `PLAIN_SPRINTS` stays; its Frontier line closed `backlog · kept`, and its count grows by one.
- The Frontier line of the clean branch was put off as a sprint item: it needs a push of `plugin` and a tag, which the person does.

## Direct instructions to the librarian

- Check first that the cascade of this run keeps `decision-case-971`'s and `decision-case-976`'s kin: the code of Case 982.1 is live in this run's `guppi generate`, so a superseded Decision page that a live page names in `deferred_by` or `addressed_by` now stays `superseded` under `wiki/decisions/`. The `update` items of 982.3 carry `{supersedes:case 971}` and `{supersedes:case 976}` on Decision pages that already stand archived under `vault/archive/plugin/2026-11-01/0141/decisions/`; after this run neither `estimate-close-reports-the-run` nor `estimate-handoff-dispatches` should carry `deferred_by`, and `backlog.md` should not list them.
- Case 987.1 creates `rule-skill-approve-spec` with `core: true` and `status` from the create; its render writes `.claude/skills/approve-spec/SKILL.md`, and the `update` of `rule-hook-registry` adds `guppi spec --typed` to `UserPromptSubmit` in `.claude/settings.json`. The code of that hook is committed.
- Cases 984 and 987.2 both update `rule-orchestration`, in different sentences (under `## Who builds a Case` and `## Plan Mode and the Frontier`). Cases 985 and 986 both update `rule-case-build`. Cases 987.1 and 989 both update `rule-spec-box`, in different sentences.
- Case 987.1 sets `insight-plugin-cli-withholds-approval-of-a-long-plan` `actioned` with `addressed_by: decision-case-987.1` and carries `{supersedes:case 957}`.

## What actually got done

- Cases ratified: 982 (982.1, 982.2, 982.3), 983, 984, 985, 986, 987 (987.1, 987.2), 988, 989.
- Code: `.guppi/guppi/generate.py` (`KEEPERS`, `kept_decisions`, `archived_by_cascade` takes the kept set, `cascade` reads it), `.guppi/guppi/sprint_close.py` (`judge_decisions` imports `kept_decisions`), `.guppi/guppi/prespec.py` (`without_cleared`, `cascade_notes` reads the keep; `gate_refusal`, which `gate` prints), `.guppi/guppi/backlog.py` (`render` takes the sessions; `--check` accepts the render without the newest Frontier), `.guppi/guppi/event.py` (`is_typed`, which `is_hi_prompt` calls), `.guppi/guppi/spec.py` (`--typed`, `typed`).
- Tests: `test_generate.py` (4 new, and one assertion of the supersede of a parent changed to the new keep), `test_prespec.py` (2 cascade notes), `test_backlog.py` (3 on `--check`), `test_spec.py` (9 `typed`).
- `guppi test`: 1878 passed, 6 skipped, 1 deselected at the Baseline; 1896 passed, 6 skipped, 1 deselected at Retro. `guppi style` clean after `ruff format` of two files.
- Readings at Retro: L30 `estimate-generate-cascades` passed, L31 `estimate-prespec-notes-a-page-the-cascade-archives` passed, L32 `estimate-backlog-checks-the-file` passed, L33 `estimate-ratification-ledger-line-form` passed. Lessons: L34 `lesson-frontier-backlog-line-closed-by-a-case-that-keeps-its-defer`, L35 `lesson-onward-stop-line-before-a-showing-breaks-its-form`.

## Debt

- No box of code, test or command is left unticked.
- 59 boxes wait for the librarian: the page, render and glossary lines, and the `read` lines.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — after this run's render of `vault/wiki/orchestration.md`, at the Retro of the first session that runs on it.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — after the `/pre-spec` of the first session on the new Render of `rule-case-build`.
- `estimate-case-build-reads-the-link-graph-of-what-it-changes` — the builds of the first session on the new Render of `rule-case-build`.
- `estimate-skill-approve-spec-takes-the-spec` — its pytest part passed at Retro (`test_spec.py -k typed`, 9 passed); its by-hand trial in the CLI waits for this run's render of `.claude/settings.json` and `.claude/skills/approve-spec/SKILL.md`.
- `estimate-orchestration-names-the-typed-approval` — the same CLI trial, after this run's render of `vault/wiki/orchestration.md`.
- `estimate-spec-box-runs-a-conserved-spec` — the trial on a copy (`/carry`, then `/box`), after this run's render of `.claude/skills/box/SKILL.md`.
- `estimate-close-reports-the-run` and `estimate-handoff-dispatches` — Case 982.3 changed only their defer; each waits for the event its `method` names, which the session folders of 0141 and 1721 may already hold (`report.md`, the commit of `/handoff`).

## Observations

- `backlog: vault/wiki/backlog.md differs from its sources` stood in the Baseline, red before the work: this session put off C1 and C8. After the code of Case 983 the live `guppi backlog --check` printed nothing, exit 0.
- The other 12 lines of the Baseline of `guppi check` (10 core pages `draft`, 3 `unread: failed`) were red before the work.
- The test of the supersede of a parent with sub-cases asserted that a sub-case page whose defer target still names it is archived; Case 982.1 makes it stay `superseded`, so its assertion was changed to the new contract.
- `kept_decisions` leaves out a page standing `archived`; `guppi sprint-close` used to count every live page, so a page `archived` but not yet moved no longer keeps a Decision page at the close.
- A `/approve-spec` followed by a tab is not read as the command, the same as `/hi`.

## For the next session

- The hook of `rule-prespec-onward` asks a reply that waits for the person's word to open with `STOP:`, and the check of `rule-case-check` notes any line before a showing; which holds for a Case built again after the check of `/pre-spec` (L35).
- The clean branch of the sprint: push `plugin` and a tag `prod-x.y.z`, and read the CI run; `rule-ratification` now may turn `built` at this run, which leaves fewer `draft` core pages blocking `prod`.

## Ask the person
