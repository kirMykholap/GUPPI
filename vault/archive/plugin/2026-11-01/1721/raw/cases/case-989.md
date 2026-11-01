## Case 989 — A trial run on a copy reads the check of /box

> **context:**
> `/box` runs a Spec that an earlier session saved by `/carry` and could not finish: it checks the Spec, runs it on its own branch, merges the branch back and has the librarian write the pages on the shared branch. `rule-spec-box` has `core: true` and stands `draft`. Its History shows that it went back to `draft` by the cascade after Case 956.4 added two steps to `/box`, showing `report.md` and committing it alone, and replaced the Criterion of `estimate-spec-box-runs-a-conserved-spec`, which set that Estimate `pending`. Its method waits for a session that runs a saved Spec by `/box`, and none has run since. The last reading, of 2026-10-04 in session 1416, passed each step but the two new ones. This session cannot run `/box` on the live repository, since `estimate-spec-box-refuses-a-stale-spec` promises that `guppi box --check` refuses a session that ratified a Case of its own. While the page is `draft`, the brief of the last librarian's run reports it among the lines of `guppi check` ("10 `status: a page with core: true that is draft`"), and `drafts` of `.guppi/guppi/ship.py` stops the build of the clean version before it writes `prod` for each such page. The page has no `deferred_by`. It stands in `backlog.md` because `deferred` of `.guppi/guppi/backlog.py`, read whole, lists each line of the `## Backlog` of each sprint page, the closed ones under `vault/archive/` too, and the closed sprint `migration` names `[[rule-spec-box]]` there. `finished` drops such a line once its page stands `built` (as read whole in case 962). The person chose a trial on a copy of the repository. At `/pre-spec` the person agreed that it runs after the librarian's run of this session and not in its Work Mode. The Render of `rule-orchestration` says a file rendered from a Rule page "changes at the librarian's render after the session" (case 690.2), and no task of this Case renders `.claude/skills/box/SKILL.md` earlier. The method of the Estimate is set anew, opening its by-hand part with `after` and the event, and its Criterion and its status stand. The Case is checked by `estimate-spec-box-runs-a-conserved-spec`. Its Criterion already promises each step of `/box`, the two new ones too, and only its moment changes. `estimate-spec-box-refuses-a-stale-spec` stays `passed`, since `guppi box --check` does not change.
>
> The Purpose of `rule-spec-box` ends by pointing to a line of the Backlog of the closed sprint `entity-sprint-migration` for the second part of `/box`. Case 962 put that work as a note in the Backlog of the live sprint page `entity-sprint-plugin`. That note now holds the work in the backlog list, and the person chose to point there. The second part stays out of this Case. No Estimate checks the pointer, since an update of a Purpose touches no Estimate (case 378.5). Case 987.1 of this session rewords two sentences of the Render of `rule-spec-box`, the description of `/box` and the sentence on its argument. This Case changes only the last sentence of the Purpose, so the pairs do not meet. I read the finished file of Case 987 whole. Its pairs on `rule-spec-box` touch only the Render. Its render line of `.claude/skills/box/SKILL.md` is run by the librarian. The by-hand part of each of its methods waits for the librarian's run after this session, so its trials and this one wait for the same event. The trial of this Case waits for the librarian's run that applies this Case's `update` of `rule-spec-box`, and that run renders `.claude/skills/box/SKILL.md` from the page as it then stands. A Grep of `estimate-spec-box-runs-a-conserved-spec|second part` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `backlog.md`, `entities/entity-sprint-plugin.md` and `rules/rule-spec-box.md`, and over `.claude/` it printed nothing. `backlog.md` is written by its script. The note of `entity-sprint-plugin` stays true. A Grep of `rule-spec-box|box/SKILL|spec-box-runs` over `.guppi/tests/` printed only a docstring of `test_box.py`, so no test reads the changed text live. The `.guppi/links.md` block of `rule-spec-box` names no neighbour that the change makes false. `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec` is part of the second part. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> The check of `/box` waits for a run that no session plans, so `rule-spec-box` stays `draft`, `guppi check` reports it, the build of the clean version is refused, and the Purpose points to the second part of `/box` on a closed sprint page.

> **recommend:**
> - **How the waiting check of /box gets read**
>   - Recommended: (a) a trial run on a copy of the repository, in this session's Work Mode.
>   - Answer: agreed, (a).
> - **Where the page points for the second part of /box**
>   - Recommended: (a) to the note on the live sprint page `entity-sprint-plugin`.
>   - Answer: agreed, (a).
> - **Whether the second part of /box enters this Case**
>   - Recommended: (a) no, it stays a note on the sprint page.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the trial of `/box` runs after the librarian's run of this session, since `.claude/skills/box/SKILL.md` is rendered only then, and not in this session's Work Mode.
>   - Taken: the method of `estimate-spec-box-runs-a-conserved-spec` waits for that librarian's run, and the task that stopped Work Mode for the trial is gone.

> **given:**
> `rule-spec-box`: the rule of `/box`, whose Purpose points to the second part.
> **＋** `.claude/skills/box/SKILL.md`: the skill, as rendered from that rule.
> **＋** `estimate-spec-box-runs-a-conserved-spec`: the check of `/box`, whose method is set anew.
> **＋** `entity-sprint-plugin`: the live sprint page, whose Backlog holds the second part as a note.
> **＋** `/carry`: the skill that saves the Spec of the trial.
> **＋** `~/.claude/projects/`: the folder of the transcripts the reading reads.

> **when:**
> After the librarian's run that applies the `update` of `rule-spec-box` and renders `.claude/skills/box/SKILL.md`, the person runs on a copy of the repository a session that saves a small Spec by `/carry` and a second session that runs it by `/box`.

> **then:**
> The second session runs `/box` through the dispatch of `librarian-guppi` and the commit of `report.md`.
> **＋** Git log, the branches and the folders of the copy, and the transcript of the second session under `~/.claude/projects/`, are read against the Criterion of `estimate-spec-box-runs-a-conserved-spec`, and its estimate line names that transcript.
> **＋** The Purpose of `rule-spec-box` points to the note on the second part of `/box` in the Backlog of `entity-sprint-plugin`.
> **－** The trial writes nothing to the live repository; the estimate line is the only record of it.
> **－** The second part of `/box` is not designed here, and the note of `entity-sprint-plugin` stays as it stands.

> **tasks:**
> - [ ] update `rule-spec-box`
>   - old: `` Both wait for a second part (a line of the Backlog of `entity-sprint-migration`, case 591). ``
>   - new: `` Both wait for a second part (a note of the Backlog of `entity-sprint-plugin`, as set in case 962). ``
>   - change: `the second part of /box is pointed to on the live sprint page`
> - [ ] update `estimate-spec-box-runs-a-conserved-spec`
>   - set:
>     ```
>     method: "uv run --project .guppi guppi render --check; by hand, after the librarian's run that applies the update of rule-spec-box pointing to the Backlog of entity-sprint-plugin and renders .claude/skills/box/SKILL.md: on a copy of the repository, one session saves a small Spec by /carry and a second session takes it at its Frontier and runs it by /box; git log, the branches, the folders of that session and of the conserved Spec, the librarian's commit and the commit of report.md read in the copy, and the dispatch line and the text shown to the person read in the transcript of the second session under ~/.claude/projects/, recorded in the estimate line with that transcript named"
>     ```
>   - change: `method: a trial run of /box on a copy of the repository, after the librarian's run that renders the skill`
> - [ ] read `estimate-spec-box-runs-a-conserved-spec`

> **ratification:**
> ```
> - decision[case 989][update][rule-spec-box]{ref:rule-spec-box}
> - decision[case 989][update][estimate-spec-box-runs-a-conserved-spec]{ref:rule-spec-box}
> ```
