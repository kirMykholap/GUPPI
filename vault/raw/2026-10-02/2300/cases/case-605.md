## Case 605 — The Insight on the chat form of a Case takes the colon lesson and is closed by the check of the form of a round

> **context:**
> A rule on how a Case or a round looks in the chat holds only if a script reads it. Otherwise the fault is found later, by the person or at pre-spec. `insight-case-form-chat-form-read-by-no-script` gathers the lessons of this pattern. Earlier Cases closed it three times: case 419.3 (the chat form of a Case is checked on `SubagentStop`), case 449 (the person judges the text of the story sections, so a count in a story section is not checked by a script) and case 537 (the language finding on each answer). Each time a new lesson with the same cause came in, the Insight became `open` again. Its one live child is `lesson-case-protocol-own-text-before-a-round`, clustered on 2026-09-30. In session 1736 the main agent opened each round of `case-guppi` with a line of its own, and no check read the reply. Case 562 closed that cause: the `Stop` run of `rule-case-check` refuses a reply that shows a round after text the main agent wrote itself. `estimate-case-check-refuses-text-before-a-round` checks it.
>
> Case 562 did not close the pattern. `lesson-case-check-question-line-without-colon-unseen` (`new`, 2026-10-02, ledger line 25 of session 2049) records a second fault of the same kind. A round of `case-guppi` came with a question title line that had no colon after the bold title. `QUESTION_LINE` of `guppi/casecheck.py` did not see that line as a question, so no script read the form of the question, and two hand readings found the fault later. That is the Insight's pattern. The synthesis of the librarian did not cluster the lesson, and the brief gave no reason (case 602 fixes that report from now on). Pre-spec found the gap, and the person chose to add the lesson to the Insight in this Case. Case 601.1 of this session closes the cause of that lesson: the `SubagentStop` check sends back a round whose question is out of the grill-me form, and it judges the title line by `QUESTION_LINE`. `rule-insights-schema` makes `addressed_by` one link, to the latest fix, so it names `decision-case-601.1`. The case file of Case 601 is being built again, and the new version names this Insight.
>
> This Case gives the two `update` items that the frame of `rule-synthesis` gives when a lesson joins a live Insight. The Insight gets its `children` with the new lesson. The lesson gets `status: clustered` and `insight`. In the same `update` the Insight is set `actioned`. The values are bare slugs. `guppi/generate.py` writes each field that `REF_FIELDS` of `guppi/pages.py` names — `children`, `insight` and `addressed_by` among them — as a quoted wikilink. A link would also name `decision-case-601.1` before that page exists, and the check of bare links refuses that. The cascade of `guppi/generate.py` then archives both `clustered` children, and `guppi backlog` drops the Insight's line. The Insight stays live, so a new lesson with the same cause opens it again. The Insight's tags stand: the frame of `rule-synthesis` sets the union of tags only when it creates an Insight. Both lessons stand in the ledgers of earlier sessions, so no decision line carries `{addresses}` (`ratification.md`). The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. The Case makes no `create`, so the vault query was not run.
>
> Two Estimates check the fixes: `estimate-case-check-refuses-text-before-a-round` for case 562, and `estimate-case-check-sends-back-a-faulty-round`, created by Case 601.1, for the colon lesson. This Case changes no behaviour, so the Criterion of each stands. `estimate-insights-schema-checked` and `estimate-lessons-schema-checked` cover the schema files, which this Case does not change. The other seven children of the Insight are archived: a Glob of their slugs under `vault/` found each of them under `vault/archive/`.
>
> Frame checks:
> - A Grep of `insight-case-form-chat-form-read-by-no-script` over `vault/wiki/` outside `decisions/` printed these files:
>   - `rules/rule-case-check.md`: its Purpose says that until case 419 no script read a Case before its ratification. That stays true.
>   - `backlog.md`: the Insight's line, which comes from its `open` status.
>   - `lessons/lesson-case-protocol-own-text-before-a-round.md`: the child.
>   - `log.md`: not read.
> - A Grep of `lesson-case-check-question-line-without-colon-unseen` over the repository outside `vault/wiki/decisions/` printed these files:
>   - `vault/wiki/brief.md`: line 85 lists the lesson as a question for this session. Case 601 answers that question.
>   - `log.md`: not read.
>   - Under `raw/2026-10-02/`, `2300/ledger.md`, `2300/frontier.md`, the case files of Cases 601, 602 and 605, `2049/materialize.yaml`, `2049/ledger.md` and `2049/handoff.md`: these are records of the sessions.
>
>   The context of Case 602 says that Case 602 clusters no lesson by hand. That stays true of Case 602.
> - A Grep of both Insight and lesson slugs over the repository outside `vault/` printed no file.
>
> Not done: the Insight's Proposal on a count in a story section stays rejected, as case 449 decided.

> **problem:**
> The Insight still stands `open` in the backlog. Its one live lesson was closed by case 562. A second lesson of its pattern, the question title line without the colon, stands `new` and is part of no Insight. Case 601.1 of this session closes the cause of that second lesson. The question was whether to close the Insight now, and with which lessons and which fix.

> **recommend:**
> - Recommended: close the Insight now, with `addressed_by` naming `decision-case-562`, the decision whose `Stop` check refuses a round shown after the main agent's own text.
>   - Answer: ratified as built
> - **Change**
>   - Asked: pre-spec found that `lesson-case-check-question-line-without-colon-unseen`, recorded after case 562, fits the Insight's pattern, and that Case 601.1 is then the latest fix. The person chose to add that lesson to the Insight's `children`, set it `clustered` with `insight`, have `addressed_by` name `decision-case-601.1`, and let the cascade archive both lessons with the Insight `actioned`.
>   - Taken: the Insight's `update` sets `children` with the new lesson, `status: actioned` and `addressed_by: decision-case-601.1`. A second `update` sets the lesson `clustered` with `insight`. The context no longer claims that no lesson of the cause came in after case 562.

> **given:**
> `insight-case-form-chat-form-read-by-no-script` — the Insight; its `children` widened and its status set `actioned`
> **＋** `lesson-case-check-question-line-without-colon-unseen` — the lesson of the colon, set `clustered` under the Insight
> **＋** `lesson-case-protocol-own-text-before-a-round` — the live `clustered` child that already stands
> **＋** `decision-case-601.1` — the decision that closes the cause of the colon lesson, named by `addressed_by`; built from `raw/2026-10-02/2300/cases/case-601.md`; unchanged here
> **＋** `rule-insights-schema` and `rule-lessons-schema` — the fields `children`, `addressed_by`, `insight` and the cascade; unchanged
> **＋** `rule-synthesis` — the form of the `update` items that add a lesson to a live Insight; unchanged
> **＋** `guppi/generate.py` and `guppi/pages.py` — apply the items, write the slug fields as wikilinks and run the cascade; unchanged
> **＋** `guppi/backlog.py` and `vault/wiki/backlog.md` — the list of the `open` Insights; unchanged code

> **when:**
> `uv run guppi generate` applies the `update` items of `insight-case-form-chat-form-read-by-no-script` and `lesson-case-check-question-line-without-colon-unseen`, and `uv run guppi backlog` then writes `vault/wiki/backlog.md`.

> **then:**
> `insight-case-form-chat-form-read-by-no-script` has `lesson-case-check-question-line-without-colon-unseen` among its `children`, `status: actioned` and `addressed_by` naming `decision-case-601.1`.
> **＋** `lesson-case-check-question-line-without-colon-unseen` has `status: clustered` and `insight` naming `insight-case-form-chat-form-read-by-no-script`.
> **＋** The cascade of `guppi/generate.py` archives `lesson-case-protocol-own-text-before-a-round` and `lesson-case-check-question-line-without-colon-unseen`.
> **＋** `vault/wiki/backlog.md` holds no line for the Insight.
> **－** The Insight is not archived. It stays live, and a new lesson with its cause opens it again.
> **－** The tags of the Insight do not change.
> **－** `decision-case-601.1`, `rule-insights-schema`, `rule-lessons-schema` and `rule-synthesis` do not change.

> **tasks:**
> - [ ] update `insight-case-form-chat-form-read-by-no-script`
>   - set: `{children: [lesson-case-form-the-spec-free-sections-written-last, lesson-case-form-ratification-used-for-the-agents-caveats, lesson-case-form-a-count-in-the-sentence-that-opens-a-list, lesson-case-form-given-written-before-tasks, lesson-case-build-a-list-in-context, lesson-case-build-quotes-the-person-in-the-chat-language, lesson-case-build-rebuild-quotes-the-relayed-words, lesson-case-protocol-own-text-before-a-round, lesson-case-check-question-line-without-colon-unseen], status: actioned, addressed_by: decision-case-601.1}`
>   - change: `child lesson-case-check-question-line-without-colon-unseen added; actioned: the Stop check of rule-case-check refuses a round shown after a text of the main agent's own (case 562), and the SubagentStop check sends back a round with a question out of the grill-me form (case 601.1); a count in a story section stays rejected (case 449) (case 605)`
> - [ ] update `lesson-case-check-question-line-without-colon-unseen`
>   - set: `{status: clustered, insight: insight-case-form-chat-form-read-by-no-script}`
>   - change: `clustered under insight-case-form-chat-form-read-by-no-script (case 605)`

> **ratification:**
> ```
> - decision[case 605][update][insight-case-form-chat-form-read-by-no-script]{ref:insight-case-form-chat-form-read-by-no-script}
> - decision[case 605][update][lesson-case-check-question-line-without-colon-unseen]{ref:insight-case-form-chat-form-read-by-no-script}
> ```
