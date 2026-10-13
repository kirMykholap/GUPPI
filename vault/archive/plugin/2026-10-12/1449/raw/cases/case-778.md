## Case 778 — A waiting reading of the sprint page makes no Cases line at /hi

> **context:**
> When `/hi` writes the Frontier, it takes each open `W` reading whose method runs now. For each other open `W` line it writes a Cases line that asks to fix the method, replace the Criterion or archive the page (case 670.6). The one exception is a `W` line whose `method` names the session that closes a sprint, or the session after it, which stays open under `## Work` (case 670.5). An Estimate whose `target` is the live sprint page waits by design: since case 772 the brief leaves it out of `Work` and `Ask the person` until its moment, and Retro neither reads it nor sets it `failed` while its work is not done; the Retro of the session that finishes its work, or the closing Case of `/sprint-close`, reads it. The `/hi` step got no such exception. At the `/hi` of session 2350 it wrote four Cases lines for Estimates of `entity-sprint-plugin` whose work belongs to later milestones, and the person closed them `· work` (`lesson-hi-unread-sprint-reading-made-a-case-line`, ledger line 13 of session 2350). Today's brief lists no such reading under `Work`, but the short brief of `carry` copies each open `W` line of the Frontier into `Work` (`rule-carry-over`), so such a line can still reach `/hi`. The person chose that such a line stays open under `## Work` and makes no Cases line, judged from the `target` of the Estimate's page, with no judgment of whether the work is done: a reading that runs now is still taken, and one that cannot waits for the Retro or the close that `rule-retro` names. The Render of `rule-skill-hi` has the reading step open only the page of each Estimate it reads, and a `W` line of the short brief of `carry` is a slug alone, since that brief leaves out Readings due (`rule-carry-over`), so neither the method nor the `target` of a reading that cannot run is at hand; pre-spec found this, and the Case has the reading step open the page of the Estimate of each open `W` line and judge from it both whether the reading runs now and its `target`. So two lines of the Criterion of `estimate-hi-takes-its-readings` are not carried on purpose: the `＋` line that the agent opens the page of each Estimate it reads, and the `－` line that only the reading step opens the pages of the Estimates it reads. Both are replaced by lines that name the page of the Estimate of each open `W` line. The person asked whether such Estimates stay visible: the brief's Readings due lists every `pending` Estimate with where it is read, `make lint` prints one `unread: pending` finding per such Estimate (`check_unread` in `guppi/lint.py`), and the handoff names each Estimate whose reading cannot be taken yet with its moment. The person chose to leave out of this Case Estimates that wait for any other event, since the rule on methods in `rule-case-protocol` has pre-spec report a `method` that waits for a later session, a session of a sprint, the session that closes one, the librarian or a `/hi` (case 670.4), with one exception, an Estimate whose target is a sprint page (case 772.4); the wait of a `W` line whose `method` names the close of a sprint stands in `rule-skill-hi` (case 670.5) and `rule-brief` (case 772.1). In the Render of `rule-skill-hi`, four sentences state this step: the Cases source of an open `W` line whose reading cannot run now, which stands, since such a line is still written by the reading step; the sentence on which pages the step opens, which the Case rewrites; the sentence that makes the Cases line, which the new exception bounds; and the exception of the close of a sprint, after which the new sentence stands. The Criterion of `estimate-hi-takes-its-readings` speaks of this step, so it is replaced whole with one more `－` line, and its `purpose`, which names the Cases line for each other open `W` line, is set anew; its `method` reads the new Render in the Spec at the Retro of the session that changes it and stands. The Criterion of `estimate-hi-writes-frontier` names that source as written by the reading step, which stays true, so it stands. A Grep for the pattern ``open `W` line|W` line`` over `vault/wiki/rules/`, `.claude/` and `vault/wiki/orchestration.md` printed `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-brief.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-work-mode.md` and `vault/wiki/rules/rule-carry-over.md`: Work Mode takes a `W` reading only when its work is built and its moment has come, Retro and the brief already wait for an Estimate of the live sprint page, `carry` copies open `W` lines, and `orchestration.md` lets a `W` line stay open through Plan Mode, so none of them is made false. Case 777 reads `.claude/skills/hi/SKILL.md` at this session's Retro for the opening of a sprint, a moment this Case does not touch.

> **problem:**
> `/hi` makes a Cases line for an open `W` reading of an Estimate of the live sprint page that waits by design, so the person closes a line that needed no decision.

> **recommend:**
> - **What should `/hi` do with a waiting sprint-page check**
>   - Recommended: (a) it stays open in Work, as the close-of-sprint checks do.
>   - Answer: not answered; replaced by the question on which readings skip the decision item at `/hi`.
> - **How should `/hi` tell that a sprint check's work is not done**
>   - Recommended: (a) no judgment of done at `/hi`: any open Work line of a check of the live sprint page that cannot be read now stays open in Work.
>   - Answer: agreed, (a).
> - **Which check confirms the change**
>   - Recommended: (a) add one exception line to `estimate-hi-takes-its-readings` and set its purpose anew; its method stands.
>   - Answer: agreed, (a).
> - **Which readings should skip the decision item at `/hi`**
>   - Recommended: (a) only the checks of the live sprint page; any other reading `/hi` cannot take still becomes a decision item.
>   - Answer: agreed, (a). The person first proposed that every reading `/hi` cannot take stays in Work, is flagged by the librarian, and goes to the backlog by a defer at the next `/hi`, and asked whether such checks stay visible; after the answer the person agreed with the recommendation.
> - **Should a check be allowed to wait for some event**
>   - Recommended: (a) not in this Case; checks that wait for another event stay not allowed, and a wider rule is an item of its own.
>   - Answer: agreed, (a).

> **given:**
> `rule-skill-hi`: the rule of `/hi`, rendered into `.claude/skills/hi/SKILL.md`, whose reading step changes.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `entity-sprint-<id>`: the live sprint page, the `target` of the Estimates that wait.
> **＋** `rule-retro`: sets when an Estimate of the live sprint page is read.
> **＋** `vault/wiki/brief.md` and `raw/<date>/<hi HHMM>/frontier.md`: the brief whose readings `/hi` takes and the Frontier it writes.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** A `W` line of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose reading cannot run now stays open under `## Work` and is no Cases line. It waits for the moment that `rule-retro` sets for it. The agent judges this from the `target` of the page of that Estimate, with no judgment of whether the work is done.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens pages: the page of the Estimate of each open `W` line.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5). ``
>   - new: `` A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5). A `W` line of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose reading cannot run now stays open under `## Work` too and makes no Cases line: it waits for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, as `rule-retro` sets it; judge this from the `target` of its page, with no judgment of whether its work is done (case 778). ``
>   - old: `` this step opens the page of each Estimate it reads and judges the reading against its `## Criterion`. ``
>   - new: `` this step opens the page of the Estimate of each open `W` line, judges from it whether its reading runs now, and judges each reading it takes against its `## Criterion` (case 778). ``
>   - change: `an open W line of an Estimate of the live sprint page whose reading cannot run now stays open under Work and makes no Cases line (case 778)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-takes-its-readings`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint and those of an Estimate of the live sprint page, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates of its open W lines
>     ```
>   - change: `the Criterion replaced whole — an open W line of an Estimate of the live sprint page whose reading cannot run now stays open under Work and is no Cases line`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 778][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 778][update][estimate-hi-takes-its-readings]{ref:rule-skill-hi}
> ```
