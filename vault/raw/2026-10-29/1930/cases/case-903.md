## Case 903 — The close check waits for a kind of run, and the report gets a check of its own

> **context:**
> `estimate-close-commits` checks that the librarian's run ends in one separate commit of `vault/` and the rendered files, leaves no rendered file modified or untracked, and returns a report of twenty lines or fewer. It is `pending`. Its `method` waits for the librarian's run of "the next session" that holds "the new Render" of `rule-close`. That moment belongs to one past session of GUPPI. The Criterion of `estimate-clean-branch-ships-neutral-texts` refuses a `method` of a shipped Estimate that waits for a moment of a past session of GUPPI, and accepts one that waits for a kind of moment that comes again in any project. `ships` of `.guppi/guppi/ship.py` ships an Estimate only when it stands `passed` and its target is a page with `core: true`, as `rule-close` is, so the `method` would be read once this page passes. A second fault blocks the reading. The `method` reads the librarian's report in the transcript of the session of the run, and `rule-skill-hi` sets that `/hi` reads no transcript of an earlier session (case 670.5). `decision-case-885` put the page off for that reason, and `lesson-brief-lists-transcript-readings-under-work` records the same stall. `/handoff` dispatches the librarian and shows its report to the person unchanged, as `.claude/skills/handoff/SKILL.md` sets it. In a session that `/box` runs, `/handoff` dispatches nothing, and step 6 of `.claude/skills/box/SKILL.md` does the same instead. Nothing in the vault keeps the report. The `method` passage of `rule-estimates-schema` sets that a reading names its moment by its kind, and that any such moment after the render counts. Its passage on the single Estimate sets that a line with a test or a reading of its own is split off. So Case 903.1 replaces the Criterion of `estimate-close-commits` without the report line, which leaves it on purpose since Case 903.2 carries that promise, sets its `purpose` and `method` anew, and waits for a librarian's run whose `.claude/agents/librarian-guppi.md` already holds the Render of `rule-close` when the run starts. The librarian loads that file when its run starts, and the render rewrites it during the run, so a run that only renders a change still follows the old text. Case 903.2 creates `estimate-close-reports-in-twenty-lines` for the report, read by the person's answer. I read `tied_to_a_one_off_moment`, `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment` and `check_unread` of `.guppi/guppi/lint.py` against both new `method` texts. Neither holds "first" before "after the render". Each opens a part with "by hand, after" and names its event before a colon, so `waits_for_an_event` accepts it. `check_unread` gives no finding for a `pending` page with such a `method`. The decision line of 903.1 carries `{supersedes:case 885}`, as Case 902 asked in its Other Case line. `case-schema.md` sets that a defer is cleared from each page the superseding Case names. The Criterion of `estimate-generate-writes-the-decision-page` sets the same for an earlier page that stands `archived`, as `decision-case-885` does, so that mark removes `decision-case-885` from the `deferred_by` of `estimate-close-commits`. Case 902 leaves this defer to Case 903.1 and no longer says that `estimate-close-commits` keeps it. It changes only `estimate-spec-write-writes-a-defer`, which this Case does not touch, and it says that `decision-case-885` takes both Cases into its `superseded_by`. A Grep of `estimate-close-commits` over `vault/wiki/`, with `decisions/` left out, printed `brief.md`, `backlog.md`, `log.md`, `rules/rule-close.md` and `lessons/lesson-brief-lists-transcript-readings-under-work.md`. `rule-close` lists the page in `estimates`, which `generate` fills. The lesson records a past fact and stands. `backlog.md` is written again by `guppi backlog`. A Glob `vault/**/estimate-close-report*.md` printed nothing, so the new slug is free. No new Estimate checks the new wording. `estimate-clean-branch-ships-neutral-texts` already checks each `method` of a shipped Estimate by this yardstick, and its Criterion stands, since this Case changes no rule of what ships.

> **problem:**
> The `method` of `estimate-close-commits` waits for a moment that comes once in GUPPI only. It also reads the librarian's report in a transcript that `/hi` may not open, so the reading is never taken.

> **recommend:**
> - **Where the librarian's report is read**
>   - Recommended: (b) split the report into its own check, answered by the person after `/box` shows the report; `estimate-close-commits` keeps what `git log` and `git status` show.
>   - Answer: agreed, (b).
> - **Which librarian's run the reading waits for**
>   - Recommended: (a) a run that starts with the current text of `rule-close` in its file.
>   - Answer: agreed, (a).
> - **What checks the new wording**
>   - Recommended: (a) no new check: `estimate-clean-branch-ships-neutral-texts` covers it.
>   - Answer: agreed, (a).

### Case 903.1 — The close commit is read after a run that holds the Render of rule-close

> **given:**
> `estimate-close-commits`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-close`: its Render sets the commit at the close.
> **＋** `.claude/agents/librarian-guppi.md`: the file that holds the Render of `rule-close`.
> **＋** `vault/`: the folder the close commit takes.
> **＋** `.guppi/guppi/render.py`: writes the rendered files and prints their list.
> **＋** `.guppi/tests/test_render.py`: the tests of `guppi render --paths`.
> **＋** `plugin/skills/install/SKILL.md`: the file that `rule-plugin-install` renders.
> **＋** `decision-case-885`: the archived Decision that put the check off.
> **＋** `rule-estimates-schema`: sets how a `method` names its moment.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, and writes nothing.
> **＋** `git log` shows one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
> **＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
> **＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
> **－** The commit takes no path that neither `vault/` nor that list names.
> **－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

> **tasks:**
> - [ ] update `estimate-close-commits`
>   - set:
>     ```
>     status: pending
>     purpose: The librarian's run ends in one separate commit of vault and each file the render writes, with no rendered file left modified or untracked
>     method: "uv run --project .guppi pytest .guppi/tests/test_render.py -k paths; by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: git log shows the commit of that run and the paths it touched, and git status shows no file the render wrote as modified or untracked"
>     ```
>   - change: `the Criterion replaced whole without the report, which estimate-close-reports-in-twenty-lines checks; the method waits for a librarian's run that holds the Render of rule-close, and reads no transcript`
> - [ ] read `estimate-close-commits`

> **ratification:**
> ```
> - decision[case 903.1][update][estimate-close-commits]{ref:rule-close}{supersedes:case 885}
> ```

### Case 903.2 — The person reads the librarian's report

> **given:**
> `estimate-close-reports-in-twenty-lines`: the new check of the librarian's report.
> **＋** `rule-close`: its Render sets the report.
> **＋** `.claude/agents/librarian-guppi.md`: the file that holds the Render of `rule-close`.
> **＋** `.claude/skills/handoff/SKILL.md`: dispatches the librarian and shows its report to the person.
> **＋** `.claude/skills/box/SKILL.md`: does the same in a session that `/box` runs.
> **＋** `rule-skill-hi`: `/hi` reads no transcript of an earlier session.
> **＋** `rule-estimates-schema`: sets that a line with a reading of its own is split off.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches ends, and `/handoff` shows its report to the person.
> **＋** In a session that `/box` runs, `/box` of `.claude/skills/box/SKILL.md` dispatches that run and shows its report to the person instead.

> **then:**
> The report reaches the person with the counts, the flags and the lint total.
> **＋** The report holds twenty lines or fewer.

> **tasks:**
> - [ ] create `estimate-close-reports-in-twenty-lines`
>   - ref: `rule-close`
>   - kind: `QA`
>   - purpose: `Whether the librarian's report, as /handoff or /box shows it, gives the counts, the flags and the lint total in twenty lines or fewer`
>   - method: `by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: the person's answer on whether the report that /handoff, or /box in a session that /box runs, showed after that run gave the counts, the flags and the lint total in twenty lines or fewer`
>   - tags: `[harness, workflow, librarian]`
> - [ ] read `estimate-close-reports-in-twenty-lines`

> **ratification:**
> ```
> - decision[case 903.2][create][estimate-close-reports-in-twenty-lines]{ref:rule-close}{tags:harness,workflow,librarian}
> ```
