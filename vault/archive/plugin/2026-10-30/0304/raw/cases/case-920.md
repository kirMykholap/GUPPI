## Case 920 — Four shipped checks drop the words that hold only in GUPPI, and the defer of the clean branch ends

> **context:**
> `guppi ship` copies into the clean version each `passed` Estimate whose target page it writes, its Criterion as it stands here (the Purpose of `rule-clean-branch`). The reading of `estimate-clean-branch-ships-neutral-texts` of 2026-10-29 listed Criterion sentences that hold only in the repository of GUPPI, for a Case of a later session to rewrite. Four of them still wait under the defer that `decision-case-893.1` set on `rule-clean-branch`: `estimate-compact-recall-reloads` gives the session folder `raw/2026-09-28/2229/` of this repository as its example, `estimate-ask-query-before-a-create` names Russian and English, `estimate-synthesis-keeps-actioned-by-the-mark` ends a line with the bare case number `(302.2)`, which `guppi ship` does not remove since no word `case` stands before it, and `estimate-synthesis-clusters` names `estimate-documentation-completes`, which the clean version does not hold, since its `method` names a target of the `Makefile`. Case 908 kept the four under the defer because a replaced Criterion sets its Estimate `pending` and the cascade sets its rule `draft` until the reading passes, and `rule-synthesis`, `rule-ask` and `rule-compact-recall` stand `built` with `core: true`; while a page with `core: true` stands `draft`, `guppi ship <folder>` writes nothing. The brief flags the defer as stale, and `backlog.md` lists `rule-clean-branch` as put off in 13 sessions. The last run of `guppi check`, under `## Flags` of `vault/wiki/brief.md`, printed `9 pages with core: true stand draft`, so the clean version is already blocked, and this Case adds three rules to that list.
>
> The person chose to rewrite all four now and to retire the whole defer. Each sub-case replaces the Criterion of one Estimate whole, the old Criterion carried line by line but the one sentence it rewords, and that Estimate checks it. The rule the new texts keep is the Criterion of `estimate-clean-branch-ships-neutral-texts`, which accepts a sentence that states its condition, such as in the repository of GUPPI, and `rule-clean-branch`, which sets a pointer in a bracket of its own that `guppi ship` removes whole; that Criterion stands, since this Case changes texts it judges and not its promise. The `method` of both synthesis Estimates names the librarian without opening with `after` and an event before a colon: `kept_method_waits` of `.guppi/guppi/prespec.py` reports a kept `method` for which `waits_for_another_session` of `.guppi/guppi/lint.py` holds, and that predicate holds for a part that names the librarian unless `waits_for_an_event` matches it, a part that opens with `after`, or `by hand, after`, and names its event before a colon. So Cases 920.3 and 920.4 set each `method` in that form, and each Estimate stays `pending` until its event. The `method` of `estimate-ask-query-before-a-create` already opens with `by hand, after` and names its event, so it stands, and the Estimate waits for a Case that creates a page with no `ref`. The `method` of `estimate-compact-recall-reloads` names no later session and stands; the person chose a stop in Work Mode at which they run `/compact`, so that Retro reads it.
>
> The defer also lists `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question` and `estimate-case-check-sends-back-a-faulty-case`, which Frontier item C2 of this session holds; by the person's answer the defer goes whole, and if C2 ends with no Case, the handoff of this session names those three, as the handoff of session 2341 did. The defer also lists six Estimates whose pointers hold once the Estimate each names passes and ships; the reading of 2026-10-29 read each shipped Estimate whole and listed none of the six. Case 920.5 names `rule-clean-branch` by an `update` with only `change` and carries `{supersedes:case 893.1}`, as `case-schema.md` sets the taking up of a deferred decision; `estimate-generate-writes-the-decision-page` already checks that a superseding Case clears the earlier slug from the `deferred_by` of each page it names, and its Criterion stands, since this Case changes no code of `generate`. Case 919.2 updates `rule-clean-branch` by one pair in this session, and its `context` leaves the defer to this item; the `update` of Case 920.5 changes no text of the page.
>
> A Grep of the repository, `vault/raw/` and `vault/archive/` left out, for `2026-09-28/2229|in Russian or in English|\(302\.2\)|flag of such a read` printed `vault/wiki/log.md`, `estimates/estimate-ask-query-before-a-create.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-compact-recall-reloads.md`, `estimates/estimate-generate-walks-dates.md`, `estimates/estimate-lint-catches-a-broken-fence.md`, `estimates/estimate-prespec-catches-a-broken-fence.md`, `estimates/estimate-synthesis-keeps-actioned-by-the-mark.md` and `estimates/estimate-synthesis-clusters.md`: besides the four pages, the hits are log lines, a Result and `origin` fields, which stand. A Grep of `vault/wiki/`, `log.md` and `brief.md` left out, for `synthesis-keeps-actioned|synthesis-clusters|ask-query-before|compact-recall-reloads` printed `rules/rule-ask.md`, `rules/rule-compact-recall.md`, `rules/rule-synthesis.md`, `estimates/estimate-ask-finds.md` and `estimates/estimate-clean-branch-ships-neutral-texts.md`: fields `estimates`, History lines and a Result, which stand. The same Grep of `.guppi/` and of `.claude/` printed nothing. Of the tests of `.guppi/tests/` that read the live vault, the live build of `test_ship.py` judges each Estimate the clean version takes, and a `pending` Estimate stays out of it; the new texts hold no pointer outside a bracket. The session's ledger holds no `error` lesson, so no line carries a mark.

> **problem:**
> Four checks that ship with GUPPI hold a sentence true only in its own repository, and the defer that keeps their rewrite on `rule-clean-branch` has been put off for 13 sessions and is flagged as stale.

> **recommend:**
> - **Which of the four checks does this Case rewrite now?**
>   - Recommended: (a) all four now, and the defer goes.
>   - Answer: agreed, (a).
> - **What happens to the rest of the note when it is retired?**
>   - Recommended: (a) retire the whole defer; item C2 carries its three checks.
>   - Answer: agreed, (a).
> - **How does the recall check give its sample session folder?**
>   - Recommended: (a) a general pattern, `raw/<date>/<hi HHMM>/`.
>   - Answer: agreed, (a).
> - **How does the vault-query check name the two languages?**
>   - Recommended: (a) by their role, the language of the chat and the language of the repository.
>   - Answer: agreed, (a).
> - **What becomes of the bare case number in the check of a marked lesson?**
>   - Recommended: (a) a pointer in its own bracket, `(as set in case 302.2)`.
>   - Answer: agreed, (a).
> - **What becomes of the link to a check that does not ship, in the clustering check?**
>   - Recommended: (a) state the condition, in the repository of GUPPI.
>   - Answer: agreed, (a).
> - **How do the two synthesis checks say when they are read?**
>   - Recommended: (a) rewrite both methods in the form that names the event.
>   - Answer: agreed, (a).
> - **When is the live part of the recall check read?**
>   - Recommended: (a) in this session: a stop of Work Mode at which the person runs `/compact`, read at Retro.
>   - Answer: agreed, (a).

### Case 920.1 — The recall check gives its session folder as a pattern

> **given:**
> `estimate-compact-recall-reloads`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/recall.py`: the hook the Criterion speaks of.
> **＋** `.claude/skills/hi/SKILL.md`: the `@` files the hook lists.
> **＋** `raw/<date>/<hi HHMM>/`: the pattern of the session folder the header names.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.

> **when:**
> The client compacts the context of a session, on the person's command or on its own, and `SessionStart` fires with `source: compact` and runs `.guppi/guppi/recall.py`.

> **then:**
> With a `hi` in the session's window, stdout holds a header line, "recall: the context was compacted at HH:MM:SS; the session is" followed by the session folder under the vault, such as `raw/<date>/<hi HHMM>/`, and "Read before the next reply:". Then comes one path per line: the `@` files of `.claude/skills/hi/SKILL.md` in their order, the session's `frontier.md` when it exists, and the Spec when one exists. Last come the line `Frontier:` and the text of `frontier.md` as it stands.
> **＋** The Spec is the `spec.md` of the folder, or before the approval the plan file the event log names last.
> **＋** The list of paths is the `@` lines of the skill file at the moment the hook fires, with no copy in the code: a file added to those lines is in the list without a change to the hook.
> **＋** The texts of the files, the Frontier apart, are not printed, only the paths; the output stays under 10,000 characters.
> **－** Without a `hi` in the window, nothing is printed on stdout, and the exit is 0.
> **－** Another `source` gives nothing: the matcher keeps the hook from firing, and the code checks `source` itself.
> **－** Exit 0 always; an error prints nothing and blocks nothing; the hook writes no file and no event line — `session-start compact` is written by `guppi event`.

> **tasks:**
> - [ ] update `estimate-compact-recall-reloads`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the example session folder is a pattern, not a folder of this repository`
> - [ ] stop: in Work Mode, the person runs `/compact` in the working session, so that the hook of `rule-compact-recall` fires with `source: compact`.
> - [ ] read `estimate-compact-recall-reloads`

> **ratification:**
> ```
> - decision[case 920.1][update][estimate-compact-recall-reloads]{ref:rule-compact-recall}
> ```

### Case 920.2 — The vault-query check names the languages by their role

> **given:**
> `estimate-ask-query-before-a-create`: its Criterion is replaced whole.
> **＋** `.claude/agents/case-guppi.md`: the agent that runs the query.
> **＋** `.claude/agents/ask-guppi.md`: the recipe of the query, rendered from `rule-ask`.
> **＋** `vault/wiki/rules/`: the folder of the first Grep of the query.
> **＋** `vault/archive/`: the folder the Glob of a slug runs over.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in the language of the chat or in the language of the repository, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

> **tasks:**
> - [ ] update `estimate-ask-query-before-a-create`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the languages are named by their role`
> - [ ] read `estimate-ask-query-before-a-create`

> **ratification:**
> ```
> - decision[case 920.2][update][estimate-ask-query-before-a-create]{ref:rule-ask}
> ```

### Case 920.3 — The check of a marked lesson holds its case number in a pointer bracket

> **given:**
> `estimate-synthesis-keeps-actioned-by-the-mark`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian, who does the synthesis.
> **＋** `rule-clean-branch`: sets the bracket of a pointer.
> **＋** `decision-case-M`: the placeholder for the decision that the `actioned` Insight names.
> **＋** `.guppi/guppi/lint.py`: `waits_for_an_event`, which judges the wait of the `method`.

> **when:**
> The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

> **then:**
> When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
> **＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
> **＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
> **＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}` (as set in case 302.2).
> **＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
> **－** `addressed_by` never names two decisions.

> **tasks:**
> - [ ] update `estimate-synthesis-keeps-actioned-by-the-mark`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`: the yaml and the brief read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the case number stands in a pointer bracket; the method names its event`
> - [ ] read `estimate-synthesis-keeps-actioned-by-the-mark`

> **ratification:**
> ```
> - decision[case 920.3][update][estimate-synthesis-keeps-actioned-by-the-mark]{ref:rule-synthesis}
> ```

### Case 920.4 — The clustering check states where the flag of a read lives

> **given:**
> `estimate-synthesis-clusters`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian, who does the synthesis.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.
> **＋** `.guppi/guppi/lint.py`: `waits_for_an_event`, which judges the wait of the `method`.
> **＋** `vault/wiki/lessons/`: the lessons the synthesis groups.
> **＋** `vault/wiki/insights/`: the Insights the lessons join.
> **＋** `vault/archive/`: the archive, whose read fails nothing here.
> **＋** `estimate-documentation-completes`: the check that, in the repository of GUPPI, flags such a read.

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every page the librarian opens at synthesis to judge whether a lesson shares its root cause is named in the report with the outcome: the Insight it joined, or none and why. A read of its Trigger, Root cause, `root_cause`, Pattern or `pattern` outside the two Greps is such an opening.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read at synthesis of only the fields `status`, `insight`, `children` and `tags` of a page under `vault/wiki/lessons/` or `vault/wiki/insights/`, made to learn which lessons are grouped or which lessons an Insight holds, is not named in the report and fails nothing here.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and, in the repository of GUPPI, the flag of such a read is the promise of `estimate-documentation-completes`.

> **tasks:**
> - [ ] update `estimate-synthesis-clusters`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a librarian's run whose `materialize.yaml` holds at least two lesson entries: the yaml and the report read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the flag of a read is named in the repository of GUPPI only; the method names its event`
> - [ ] read `estimate-synthesis-clusters`

> **ratification:**
> ```
> - decision[case 920.4][update][estimate-synthesis-clusters]{ref:rule-synthesis}
> ```

### Case 920.5 — The defer of the clean branch ends

> **given:**
> `rule-clean-branch`: the page whose `deferred_by` names `decision-case-893.1`.
> **＋** `decision-case-893.1`: the deferred decision this Case takes up.
> **＋** `.guppi/guppi/generate.py`: clears the defer of a page the superseding Case names.
> **＋** `estimate-generate-writes-the-decision-page`: checks that clearing.
> **＋** `vault/raw/2026-10-30/0304/cases/case-919.md`: Case 919.2 updates `rule-clean-branch` in this session.

> **when:**
> The librarian's run applies the Spec of this session by `generate` of `.guppi/guppi/generate.py`.

> **then:**
> `rule-clean-branch` holds no `deferred_by`, and `decision-case-893.1` stands `superseded`.
> **＋** `guppi backlog` writes no line of `rule-clean-branch` for a defer.
> **－** No text of `rule-clean-branch` changes by this Case.

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - change: `the defer of case 893.1 taken up: its four Criteria rewritten by case 920, its other checks held by a Frontier item or passed`

> **ratification:**
> ```
> - decision[case 920.5][update][rule-clean-branch]{ref:rule-clean-branch}{supersedes:case 893.1}
> ```
