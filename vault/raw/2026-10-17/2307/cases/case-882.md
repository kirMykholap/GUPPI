## Case 882 — Two shipped Criteria hold in any project, the rest stays put off

> **context:**
> `guppi ship` builds the clean version of GUPPI and copies into it each Estimate that `ships` of `.guppi/guppi/ship.py` admits: `passed`, its target a page the copy writes, and no target of the `Makefile` in its `method`. The `## Criterion` goes with it. The reading of `estimate-clean-branch-ships-neutral-texts` at the `/hi` of session 1805 listed the shipped Estimates whose Criterion holds a sentence true only in the repository of GUPPI; that promise does not fail on them, by its `－` line. Case 880 rewrote part of that list, and its sub-case 880.21 put the rest off on `rule-clean-branch`, as the Decision page `decision-case-880.21` gives it. A Criterion changes only whole, and a replaced Criterion sets its Estimate `pending` (`case-schema.md`). A pending Estimate leaves the copy until it passes. At the librarian's run `cascade` of `.guppi/guppi/generate.py` sets a rule or an entity with an Estimate that is not `passed` to `draft`, and while a page with `core: true` stands `draft`, `guppi ship <folder>` writes nothing and exits 1, as `rule-clean-branch` sets it. By the person's choices this Case takes only the two Criteria whose new reading the Retro of this session can take, so no rule goes `draft`. In `estimate-glossary-checks-the-file` the copy holds no `Makefile`, so the check is said to run as `uv run --project .guppi guppi check` runs it; `STEPS` of `.guppi/guppi/check.py` runs `guppi glossary --check`, and `rule-glossary` already names `guppi check` in place of `make lint`. In `estimate-orchestration-asks-in-the-grill-me-shape` the word Russian becomes the language of the chat; in this repository that is Russian, by `chat_lang = "ru"` of `guppi.toml`, and `vault/wiki/orchestration.md` still says Russian in its own text, a sentence of a rule that this Case does not change. Each of the two `method` values is set anew: the old one of the glossary Estimate runs `guppi check` after the librarian's run, which `kept_method_waits` of `.guppi/guppi/prespec.py` reports for a replaced Criterion, since `waits_for_another_session` of `.guppi/guppi/lint.py` matches the word librarian in a part that does not open with `after`; the old one of the grill-me Estimate reads at the Retro of a session that changes the Render of `rule-orchestration`, and no Case of this session changes it. The new methods name neither the librarian nor another session. The lines of the old Criteria that the new `when` and `then` do not carry word for word are the rewritten ones: the `When` line of the glossary Estimate, which named the target `lint` of the `Makefile`, and the line on Russian of the grill-me Estimate. The `When` of the grill-me Estimate, a list of five kinds of question and a closing line on the render, is said again as `**＋**` lines, since the operands of `case-schema.md` take no list there; it holds the same five kinds and the same render. The other six of the eight stay put off by name: `estimate-compact-recall-reloads`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-permissions` and `estimate-ask-query-before-a-create`, each of whose readings waits for a moment this session may not hold. So do the old path of the Case check, the `.gitignore` of the copy and the six pointers to pending Estimates. 882.3 takes up the put-off of 880.21 and puts `rule-clean-branch` off again with the rest named; `decision-case-880.21` then goes `superseded`, and in the cascade of the same run `archived_by_cascade` of `.guppi/guppi/generate.py` takes each Decision page standing `superseded`, so the page ends `archived`; the pages it changed stay as they are. Case 881 of this session left out, by the person's choice, the `.gitignore` texts outside the Criteria: the `method` of `estimate-sprint-close-moves-old-event-logs`, the sentence of `rule-event-log` that the log is gitignored and the row `Event log` of `entity-glossary`, which calls it the gitignored log. No put-off held them, so the purpose of the defer of 882.3 names them too, beside the two Criteria that promise a `.gitignore`; all wait for a Case of their own on whether the clean version gets a `.gitignore`. The finished file of Case 881 says that these texts wait for the put-off of 882.3. Case 886 of this session replaces the Criterion of `estimate-sprint-close-moves-old-event-logs`, on the logs the close keeps, and keeps its line on `.gitignore` word for word and its `method`, so the put-off of 882.3 still names a Criterion and a method that promise a `.gitignore`. Case 884 of this session changes `rule-orchestration` by a `change` alone and a put-off, and changes no Estimate that this Case changes or names. Each of 882.1 and 882.2 is checked by the Estimate whose Criterion it replaces. 882.3 is checked by the `uv run --project .guppi guppi check` of the librarian's run, which the brief reports, its step `guppi backlog --check` promised by `estimate-backlog-checks-the-file`, whose Criterion stands. That a `supersedes` clears the put-off on each page the superseding Case names is the promise of `estimate-generate-writes-the-decision-page`; Case 883 of this session replaces its Criterion whole and sets it `pending`, adding that a record carrying `superseded_by` still gets its Decision page with its `supersedes` list but that list changes no other page. The record of 882.3 carries no `superseded_by`, so its `supersedes` still clears the put-off of `decision-case-880.21`, as the file of Case 883 says. So the check of 882.3 rests also on the reading of that Estimate that the Retro of this session takes on the Criterion of Case 883. A Grep of the two Estimate slugs and `decision-case-880.21` over `.guppi/tests/` printed `test_glossary.py`, whose docstring alone names `estimate-glossary-checks-the-file`. The new texts hold no case number, no `uv run guppi` and no `uv run pytest`, so `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` of `test_ship.py` and `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `test_guppi_package.py` stay green.

> **problem:**
> The clean version ships the Criteria of `passed` Estimates with sentences true only in the repository of GUPPI, and each rewrite sets its Estimate `pending`, which turns its rule `draft` and stops the build of the clean version until a reading passes.

> **recommend:**
> - **What does this Case take?**
>   - Recommended: (a) only the eight rewordings.
>   - Answer: agreed, (a).
> - **Which of the eight are reworded now?**
>   - Recommended: (a) only the two that this session's Retro can read.
>   - Answer: agreed, (a).
> - **How is a sentence reworded?**
>   - Recommended: (a) the same way as the last two sessions.
>   - Answer: agreed, (a).
> - **What happens to the put-off on `rule-clean-branch`?**
>   - Recommended: (a) take it up and put it off again, naming only what is left.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes of the findings of `/pre-spec`: name Case 883 on the reading of `estimate-generate-writes-the-decision-page`, name the `.gitignore` texts outside the Criteria in the put-off, and say that the old Decision page ends `archived`.
>   - Taken: the `context` names Case 883 and the archive step of the cascade, and the purpose of the defer of 882.3 names the three `.gitignore` texts.

### Case 882.1 — The glossary check names the command that runs it in any project

> **given:**
> `estimate-glossary-checks-the-file`: its Criterion is replaced whole and its `method` set anew.
> **＋** `rule-glossary`: its target.
> **＋** `entity-glossary`: the page the check renders.
> **＋** `vault/wiki/glossary.md`: the file the check compares.
> **＋** `.guppi/guppi/check.py`: the command `guppi check`, whose steps run `guppi glossary --check`.
> **＋** `.guppi/tests/test_glossary.py`: the tests of the check.

> **when:**
> `uv run --project .guppi guppi glossary --check` runs, as `uv run --project .guppi guppi check` runs it, and renders the file from `entity-glossary` in memory.

> **then:**
> When `vault/wiki/glossary.md` differs from the render or is missing, stdout holds one line `glossary: <file> differs from entity-glossary`, the file named by its path from the project root, and the check exits 1.
> **＋** When the file equals the render, the check exits 0 with no output.
> **－** The check writes no file and ticks no line of a Spec.

> **tasks:**
> - [ ] update `estimate-glossary-checks-the-file`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_glossary.py; uv run --project .guppi guppi glossary --check in the working tree at Retro: exit 0 and no output"
>     ```
>   - change: `the Criterion replaced whole — the check runs as guppi check runs it, not as a target of the Makefile; the method reads at Retro`
> - [ ] read `estimate-glossary-checks-the-file`

> **ratification:**
> ```
> - decision[case 882.1][update][estimate-glossary-checks-the-file]{ref:rule-glossary}
> ```

### Case 882.2 — The main agent asks its own questions in the language of the chat

> **given:**
> `estimate-orchestration-asks-in-the-grill-me-shape`: its Criterion is replaced whole and its `method` set anew.
> **＋** `rule-orchestration`: its target.
> **＋** `vault/wiki/orchestration.md`: the file rendered from it.
> **＋** `.claude/skills/grill-me/SKILL.md`: the skill that sets the question shape.
> **＋** `case-guppi`: the agent whose rounds are outside this promise.
> **＋** `ask-guppi`: the agent whose findings `/pre-spec` confirms.
> **＋** `/pre-spec`: the skill whose report and findings raise a question.
> **＋** `/hi`: the skill that opens a session.
> **＋** `/work` and `/carry`: the two skills of the choice that keeps its own form.
> **＋** `rule-spec-capture`: the rule that sets that choice.

> **when:**
> The main agent puts a question to the person itself, outside a round of `case-guppi`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** The question is a decision it needs in the report of `/pre-spec`, a question at `/hi` or a question at a stop of Work Mode.
> **＋** Or, in Work Mode, it is the question whether another Case of the session changes after a Case was bounded around a clash with it.
> **＋** Or, at `/pre-spec`, after the `ask-guppi` runs confirm their findings, it is the question whether each finding not closed is fixed or left.

> **then:**
> Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
> **＋** It stands in the language of the chat, and its labels may stand translated.
> **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.
> **－** In Plan Mode the main agent puts no question whether another Case is built again after a clash.

> **tasks:**
> - [ ] update `estimate-orchestration-asks-in-the-grill-me-shape`
>   - set:
>     ```
>     status: pending
>     method: "by hand at the Retro of a session that changes this Criterion or the Render of rule-orchestration: vault/wiki/orchestration.md as rendered, or the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the question stands in the language of the chat, not in Russian; the method reads at the Retro of a session that changes the Criterion too`
> - [ ] read `estimate-orchestration-asks-in-the-grill-me-shape`

> **ratification:**
> ```
> - decision[case 882.2][update][estimate-orchestration-asks-in-the-grill-me-shape]{ref:rule-orchestration}
> ```

### Case 882.3 — The rest of the rewrite stays put off by name

> **given:**
> `rule-clean-branch`: the rule of the clean version, whose put-off is taken up and put off again.
> **＋** `vault/wiki/backlog.md`: the list of the pages put off.

> **when:**
> The librarian's run of this session applies the decision lines of this sub-case to `rule-clean-branch`, and `uv run --project .guppi guppi check` runs at the end of that run.

> **then:**
> `rule-clean-branch` is put off by the Decision page of this sub-case alone, whose `## Deferred` gives the put-off of this sub-case word for word: each Estimate and each other text that is still left, and why it is left.
> **＋** `vault/wiki/backlog.md` keeps its line for `rule-clean-branch`, and the step `guppi backlog --check` of `uv run --project .guppi guppi check` prints no line.
> **－** The changes that the earlier put-off made to the other pages stay as they are.

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - change: `the put-off of case 880.21 taken up and put off again, two Criteria of its list rewritten by case 882`
> - [ ] defer `rule-clean-branch`
>   - type: `rule`
>   - purpose: `The rest of the rewrite of the sentences inside the Criterion of shipped Estimates that hold only in the repository of GUPPI, which Cases 880 and 882 left: estimate-compact-recall-reloads (an example session folder of the repository of GUPPI), estimate-orchestration-forwards-a-discussion-question (the answer translated into Russian), estimate-synthesis-keeps-actioned-by-the-mark (a case number with no word case before it), estimate-synthesis-clusters (a pointer to estimate-documentation-completes, which does not ship), estimate-permissions (the folder c--PROJECTS-GUPPI) and estimate-ask-query-before-a-create (Russian and English), whose new readings wait for a later moment, so that a Criterion replaced now would set each pending and its rule draft until that moment; estimate-case-check-sends-back-a-faulty-case, whose sentence goes when a Case removes the old path of the check from .guppi/guppi/casecheck.py; estimate-event-log-records and estimate-sprint-close-moves-old-event-logs, whose Criteria promise a .gitignore that the clean version does not hold, together with the method of estimate-sprint-close-moves-old-event-logs, the sentence of rule-event-log that the log is gitignored and the row Event log of entity-glossary, which calls it the gitignored log, all of which wait for a Case of their own that first decides whether the clean version gets a .gitignore; and the pointers in estimate-case-build-checks-the-finished-case, estimate-case-build-reads-by-need-and-in-parts, estimate-case-protocol-case-form, estimate-orchestration-batches-cases-out-at-once, estimate-orchestration-signs-a-batch-together and estimate-sprint-close-next-session-opens-the-sprint, which hold once the pending Estimate each names passes and ships; put off by the person in session 2307`

> **ratification:**
> ```
> - decision[case 882.3][update][rule-clean-branch]{ref:rule-clean-branch}{supersedes:case 880.21}
> - decision[case 882.3][defer][rule-clean-branch]{ref:rule-clean-branch}
> ```
