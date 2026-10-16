## Case 845 — The check of the session files is read after the tag

> **context:**
> `estimate-clean-branch-writes-the-session-files` (case 822.3, pending, target `rule-clean-branch`) promises that `guppi ship` writes `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` and `log.md` of a new project as skeletons that their checks pass, and that the first `/hi` of a project that installs GUPPI from that copy starts `/sprint-open`. Its `method` waits only for the librarian's run of its change, and that run has passed. The real blocker is a tag: `run` of `.guppi/guppi/ship.py` prints "ship: no tag prod-x.y.z in the history of HEAD; nothing written" and exits 1 when `version` finds no tag that `VERSION_TAG` accepts. The brief reports in `## Readings due` on the sibling check `estimate-clean-branch-ships-neutral-texts` that "`git tag` holds `prod-1` and `prod-2` only", and on this check that "This run ran no `guppi ship`". The last step of the reading is by hand: the person installs the copy in an empty project, types `/guppi:install`, reopens Claude Code and types `/hi`.
>
> The brief proposed to defer the check into `backlog.md`. The person chose instead to read it in this session, in one batch with the other items that wait for a tag `prod-x.y.z`. Case 841 of this batch owns the task that sets the tag, and this Case sets no tag of its own. The person chose that the `method` names the tag as the event it waits for (Q1), as case 824 did for `estimate-clean-branch-ships-neutral-texts`. The rule against which each option was judged is the form of a `method` in `case-schema.md`: a part between two `;` that opens with `by hand, after` and names its event before a colon waits for that event, and Retro leaves the Estimate `pending` until that event comes (cases 670.4, 781). The new `method` waits for the tag alone. The clause on the librarian's run of its change is dropped: once this update applies, "its change" would read as the change of this Case, whose librarian's run comes after the Retro of this session, so Retro would leave the page unread (a finding of `/pre-spec`). The first part of the `method`, the tests named `skeleton`, waits for no event. The target carries no `core: true`, so the rule of a pointer in a bracket (case 807.4) does not bind the new text, and it holds no pointer.
>
> An `update` that sets only `method` is an update of one part alone: `names_a_part` of `.guppi/guppi/materialize.py` returns true for an item with no `status` under `set` and no `Criterion` under `sections`, and the Render of `rule-retro` says that such an Estimate "is neither read nor set `failed`". So the update sets `pending`, and the Case's `when` and `then` are the Criterion of the page word for word, so that the scripts write it back unchanged, as Case 844 does for `estimate-clean-branch-ships-the-tests`. The Criterion stands as it was, since the behaviour it checks does not change. The person first chose a `stop:` task of this Case for the install by hand (Q2). At `/pre-spec` the person chose instead one `stop:` task in Case 846 for every install by hand of this batch, the empty project with `uv` where the install, `/guppi:install`, the reopen and `/hi` of this reading run among them. That file did not yet hold that task when this Case was written, so this Case holds no `stop:` task and points to that one. Retro takes the reading from what the person reported at that stop and from the run of `guppi ship --allow-draft`, the `skeleton` tests and the three checks over the copy; if no tag stands then, the page stays `pending`. The brief's `## Readings at the close` reports "`uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected (exit 1)"; that failure is in `test_guppi_package.py` on `tests/`, which Case 840 handles, and no test of `skeleton` failed. A Grep of `estimate-clean-branch-writes-the-session-files` over the repository outside `vault/raw/` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`. The hit in `rule-clean-branch` is its list of `estimates`, and the hit in `estimate-clean-branch-writes-a-clean-copy` names what the check sets in place of the session files; neither speaks of the `method`, and both stand. The hits in `brief.md` and `log.md` are not read. `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `.guppi/tests/test_guppi_package.py` reads each live page against `OLD_COMMANDS`, `uv run guppi` and `uv run pytest`, and `OLD_PATHS`, `guppi/` and `tests/`. The new `method` names `uv run --project .guppi` and `.guppi/tests/test_ship.py` as the old one does, and adds no other command or path, so it gives that test no hit the old text did not give; the failure on `tests/` is the item of Case 840.

> **problem:**
> The check of the session files names an event that has passed, not the tag without which `guppi ship` writes nothing, and its last step needs the person, so it would stay unread again.

> **recommend:**
> - **Does the line on how the check is read change to name the tag?**
>   - Recommended: (a) the method waits for the tag too.
>   - Answer: agreed, (a).
> - **Who does the install in the empty project, and when?**
>   - Recommended: (a) a stop step in Work Mode after the tag.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`: an `update` that sets only `method` names one part alone, so Retro would neither read the page nor set it `failed`, and the `read` task would be debt.
>   - Taken: the update sets `pending`, and the `when` and `then` are the Criterion of the page word for word, so it is written back unchanged.
> - **Change**
>   - Asked: a finding of `/pre-spec`: the clause on the librarian's run of its change would read as the change of this Case, whose librarian's run comes after this Retro.
>   - Taken: the `method` waits for the tag `prod-x.y.z` alone.
> - **Change**
>   - Asked: the person's answer at `/pre-spec`: one `stop:` task in Case 846 for every install by hand of the batch, the install and `/hi` of this reading among them.
>   - Taken: the `stop:` task and the task by hand of this Case go; Retro reads the page from that one stop and the run over the copy.

> **given:**
> `estimate-clean-branch-writes-the-session-files`: the check of the session files as skeletons, set `pending`, its Criterion kept and its `method` set anew.
> **＋** `rule-clean-branch` and `uv run --project .guppi guppi ship <folder>`: the rule of `guppi ship` and the command, whose module `.guppi/guppi/ship.py` needs a tag `prod-x.y.z`.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/glossary.md` and `vault/wiki/log.md`: the session files the copy writes as skeletons.
> **＋** `closed_form` of `.guppi/guppi/sprint.py`, `guppi backlog`, `guppi glossary`, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`: the writers and the checks of those files.
> **＋** The plugin `guppi`, `/guppi:install`, `/hi` and `/sprint-open`: the install and the skills that open a session and a sprint.
> **＋** `.guppi/tests/test_ship.py` and `uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton`: the tests of the skeletons, the first part of the `method`.
> **＋** `rule-retro`: the rule of the reading of an Estimate whose `method` waits for an event.
> **＋** `vault/raw/2026-10-16/0104/cases/case-846.md`: the Case that holds the one `stop:` task for the installs by hand of this batch.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or, in an empty project, the person installs the plugin `guppi` from such a copy, types `/guppi:install`, reopens Claude Code there and types `/hi`.

> **then:**
> It writes `vault/wiki/sprint.md` as `closed_form` of `.guppi/guppi/sprint.py` writes it for the sprint `guppi`, so its first `## ` heading carries the mark of a closed sprint.
> **＋** It writes `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version, by their own code.
> **＋** It writes a `vault/wiki/brief.md` whose `Cases` of its `## Next session` open with the line `open the next sprint — no sprint is open since the close of guppi`, and a `vault/wiki/log.md` that holds its heading and the paragraph under it alone.
> **＋** Over the clean version, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` print nothing and exit 0.
> **＋** In that project, the first `/hi` starts `/sprint-open` before the Frontier.
> **－** It writes no `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` or `log.md` of the project it builds from.

> **tasks:**
> - [ ] update `estimate-clean-branch-writes-the-session-files`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after a tag prod-x.y.z stands in the history of HEAD: in an empty project, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, the copy and the empty project with uv being those of the reading of estimate-guppi-package-is-ready-after-the-install where that reading runs at the same commit, /guppi:install typed, Claude Code reopened and /hi typed, and guppi sprint --check, guppi backlog --check and guppi glossary --check run over the copy, read against the Criterion"
>     ```
>   - change: `the method waits for a tag prod-x.y.z in the history of HEAD, without which guppi ship writes nothing; the Criterion stands`
> - [ ] read `estimate-clean-branch-writes-the-session-files`

> **ratification:**
> ```
> - decision[case 845][update][estimate-clean-branch-writes-the-session-files]{ref:rule-clean-branch}
> ```
