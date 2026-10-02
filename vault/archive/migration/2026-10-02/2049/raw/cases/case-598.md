## Case 598 — Cases handled side by side are signed together

> **context:**
> In Plan Mode the main agent takes Frontier items one at a time. It shows one Case per reply and does not move to the next item until that Case is ratified or deferred. The one exception is the loop after the findings of `/pre-spec`: there the Cases built again go out in one reply and are ratified once (case 561.2). The rule goes wrong when a new Case shows that a Case already ratified must change. In session 2049, the round on Case 597 found that a line of Case 596.1 would become false. Case 596 was built again and ratified again in a reply of its own, and Case 597 was then shown and ratified in the next reply. That was two sign-offs for one connected change. The person ruled that items stay one at a time and each Case is ratified after it is discussed. When Cases are handled side by side, the agent waits for the whole batch and shows them together for one ratification. This covers the pre-spec loop and the case where an earlier Case must change because of a new one.
>
> `orchestration.md` holds the rule in `## Plan Mode and the Frontier`. Case 598.1 adds the batch there and in `## Showing and signing a Case`, and names both exceptions to one Case per reply: the pre-spec loop and the batch. A batch runs the steps of the pre-spec loop, so its tools already exist:
> - The docstring of `guppi/casecheck.py` lets a reply that opens with a bold label ending in a colon pass the round check, and that is the `**Waiting:**` line.
> - The same docstring compares each Case a reply shows under its heading and asks for the sending of its file, so several top-level Cases in one reply pass when each file is sent.
> - The Result of `estimate-prespec-gathers-the-answers-after-findings` (session 1202) shows four rebuilt Cases in one reply, ratified once, with no refusal.
>
> The sentence of `## Showing and signing a Case` on sub-cases already says how one reply acknowledges sub-cases ratified together: one `LEDGER` block, one heading that names the ids, one Frontier (case 355.2). 598.2 widens that sentence to every Case ratified in one answer, so that the rule has one wording. The Criterion of `estimate-prespec-gathers-the-answers-after-findings` has a line saying that outside its loop no Case is taken up before the current one is ratified. A batch makes that line false, so 598.3 replaces it. The sentence of `rule-prespec` that lifts the one-at-a-time rule inside its loop stays true and is not changed. The `purpose` of that Estimate speaks only of the loop and stands, and so does its `method`. The `purpose` of `estimate-orchestration-acknowledging-reply` stays true. Its `method` reads only the first acknowledging reply of a session, which may hold no batch, so 598.2 adds to it the first reply that acknowledges Cases ratified together.
>
> This Case was built again on findings 4 and 5 of `/pre-spec`. Finding 4: the first replace of 598.1 named the batch as the only exception and left out the pre-spec loop. Finding 5: 598.2 added a second wording of the sub-case sentence instead of widening it. 598.1 and 598.2 now change the same paragraph of `## Showing and signing a Case` at two anchors that do not overlap. Read side by side, the paragraph says that one reply acknowledges every Case ratified in one answer, and that a Case the person questions goes back and is shown again.
>
> The new Criteria change the old ones in these places only:
> - In `estimate-orchestration-acknowledging-reply`, the `when` adds Cases ratified together in one answer.
> - In the same Estimate, the line on a Case with sub-cases now covers every Case ratified in one answer, with one paragraph `Changes:`.
> - In `estimate-prespec-gathers-the-answers-after-findings`, the line on what holds outside the loop now points to the batch of `orchestration.md`.
>
> Every other line is carried as it stood. The `then` of 598.1 repeats the steps of the loop of 598.3 on purpose: the batch takes those steps, and each Estimate checks them at its own trigger. 598.1 checks them after the person's word on a ratified Case, and 598.3 checks them after the findings of `/pre-spec`.
>
> Case 597 sets what the hook of `rule-prespec-onward` does after the acknowledging reply, and this Case leaves that unchanged. In a batch the line of the new Case under `## Cases` stays open until the batch is ratified, so that hook stays silent. Once the batch is ratified, 597.2 counts the decision lines of the reply as written. Case 596 sets the Retro run and does not touch this moment. A batch in Work Mode is not covered. The person spoke of the work on the Frontier.
>
> The one `create` has a `ref`, so the vault query was not run. A Glob of `vault/{wiki,archive}/**/estimate-orchestration-signs-a-batch-together.md` found no file, so the slug is free.
>
> Frame checks:
> - A Grep of ``[Oo]ne reply shows one Case|one Case at a time|next Case until|ratified or deferred|for one ratification|one ratification`` ran over the repository outside `vault/archive/` and `vault/raw/`. It printed these files:
>   - `.claude/skills/pre-spec/SKILL.md`, `rule-prespec.md`, `estimate-prespec-gathers-the-answers-after-findings.md`
>   - `orchestration.md`, `rule-orchestration.md`, `estimate-orchestration-shows-the-built-case.md`
>   - `glossary.md`, `entity-glossary.md`, `log.md`, `tests/test_ratified.py`
>   - `estimate-case-check-shows-only-the-checked-case.md`, `rule-case-protocol.md` and `rule-case-check.md`, each a History line only
>   - `lesson-case-showing-ratification-fence-outside-the-blockquote.md`, `decision-case-52.2.md`, `decision-case-561.md`
> - The hits read outside History and `log.md` stay true:
>   - The glossary entry Plan Mode says items are worked one by one, and that stays true.
>   - The pre-spec skill describes its own loop.
>   - The test and the lesson concern one `ratification` under one heading.
>   - `estimate-orchestration-shows-the-built-case` describes the showing that each Case of a batch keeps.
>   - The decision pages were not read.
> - A Grep of ``ratified again|re-ratification|shown again|ratifies them all|names the ids`` over `vault/wiki/rules/`, `.claude/` and `vault/wiki/*.md` printed these files:
>   - `brief.md`, `backlog.md`, `orchestration.md`, `case-schema.md`, `log.md`
>   - `rule-prespec.md` (a History line), `rule-orchestration.md`, `rule-case-protocol.md`, `rule-ledger-line-withdrawn-on-re-ratification.md`
> - The hits read outside History, `log.md` and `brief.md` stay true. The backlog lines and `rule-ledger-line-withdrawn-on-re-ratification` concern ledger lines of a re-ratification. `case-schema.md` and its rule say that `case-guppi` builds a Case at every showing again.
> - A Grep of `rule-orchestration|orchestration\.md` over the repository outside `vault/archive/` and `vault/raw/` printed 49 files. A Grep of ``one Case|next Case|item by item|one at a time|together`` then ran over the rule, estimate and skill pages among them that are not named above:
>   - `rule-case-build`, `rule-plan-mode`, `rule-ratification`, `rule-ledger-write`, `rule-internal-context`
>   - `.claude/skills/hi/SKILL.md`, the Estimates of `rule-orchestration`
>   - `insight-prespec-main-agent-question-off-the-grill-me-shape`, `estimate-skill-grill-me-asks-in-rounds`
> - That Grep printed `rule-case-build.md` and `estimate-skill-grill-me-asks-in-rounds.md`. Both speak of building one Case and of the shape of a question, and both stay true.
>
> Estimates:
> - `estimate-orchestration-shows-the-built-case` stands. Each Case of a batch keeps its showing. The number of each question keeps the number of its answer, with the Case id before it, as in the pre-spec loop.
> - `estimate-orchestration-shows-the-frontier-after-a-closed-line`, `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-names-related-cases-in-the-dispatch` stand. Their Criteria speak of a line closed with no ratification, of a defer and of the dispatch, which the batch does not change.
>
> Not done:
> - `insight-prespec-after-findings-loop-unruled`, Frontier item C5, is not taken up.
> - `rule-case-rebuild-cost` is not touched.

> **problem:**
> Only the loop after the findings of `/pre-spec` lets Cases go out together for one ratification. When a new Case shows that a ratified Case must change, the changed Case is ratified again in a reply of its own, and the new Case in the next one. Nothing gathers the Cases handled side by side into one sign-off.

> **recommend:**
> - **Which Cases can be signed together outside the pre-spec loop?**
>   - Recommended: (a) one by one, with a batch only when Cases are handled side by side. Frontier items are taken one at a time, and each Case is ratified once discussed. After the findings of `/pre-spec`, and when a new Case shows that a ratified Case must change, the agent waits for the whole batch and shows all of it in one reply for one ratification.
>   - Answer: agreed with the recommendation, (a). In the first round the person had chosen (b), to hold every ratification for a batch, and the person's own answer in the second round replaced it.
> - **What the reply that shows a Case asks you**
>   - Recommended: (a) sign now or move on. The reply asks for the sign-off or lets the Case wait for the batch.
>   - Answer: in the person's own words: items of the Frontier are taken one after another and each Case is ratified after it is discussed. When several Cases are considered side by side, the agent always waits for the batch and shows all the Cases together. The cases are after the pre-spec check, or when it becomes clear that an earlier Case needs a change because of new edits. The person asked whether this holds.
> - **When the agent asks for the batch sign-off**
>   - Recommended: (a) when every open item under the Cases list is a waiting Case, and whenever the person asks; the person may name the Cases they sign.
>   - Answer: not answered; replaced by **How a batch runs in the middle of Plan Mode**.
> - **What the batch sign-off reply shows**
>   - Recommended: (a) a short list with no files and no ledger lines.
>   - Answer: not answered; replaced by **How a batch runs in the middle of Plan Mode**.
> - **How the Frontier shows a waiting Case**
>   - Recommended: (a) the line stays open as it is.
>   - Answer: not answered; replaced by **Which Cases can be signed together outside the pre-spec loop?**, under which no Case waits unsigned.
> - **How a batch runs in the middle of Plan Mode**
>   - Recommended: (a) the same steps as the pre-spec loop. The agent sends the ratified Case back to its `case-guppi`, writes one `**Waiting:**` line while an answer is out, gathers the rounds into one list numbered by Case, and shows all the Cases of the batch in one reply for one ratification.
>   - Answer: agreed with the recommendation, (a).
> - **If you sign only part of a batch**
>   - Recommended: (a) name the Cases you sign, as with sub-cases. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or with any Case it changes in turn.
>   - Answer: agreed with the recommendation, (a).
> - **How the change is checked, and what else it changes**
>   - Recommended: (a) three sub-cases. The first changes `rule-orchestration` and creates an Estimate for the batch. The second replaces the Criterion of `estimate-orchestration-acknowledging-reply`. The third replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings` without its line on what holds outside the loop.
>   - Answer: agreed with the recommendation, (a).

### Case 598.1 — A ratified Case that must change goes out with the Case that changes it

> **given:**
> `rule-orchestration` — the rule of the main agent's work, its `Render` changed
> **＋** `vault/wiki/orchestration.md` — the render of `rule-orchestration`
> **＋** `estimate-orchestration-signs-a-batch-together` — the new promise
> **＋** `rule-prespec` and `/pre-spec` — the loop after the findings, whose steps the batch takes; unchanged
> **＋** `rule-case-check` — the `Stop` check, which lets a line under a bold label pass and asks for the file of each Case shown; unchanged
> **＋** `case-guppi` and `SendMessage` — the agent that builds each Case, and the call that sends a Case back to it
> **＋** `.claude/skills/grill-me/SKILL.md` — the shape of each question of the list
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose items are taken one at a time

> **when:**
> In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
> **＋** A Case that a Case of the batch asks to change in the same way joins the batch.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
> **＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
> **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change.
> **－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` One reply shows one Case, in the form of `case-schema.md` as `case-guppi` built it. ``
>   - new: `` One reply shows one Case, in the form of `case-schema.md` as `case-guppi` built it, except Cases handled side by side and shown together for one ratification: in the loop after the findings of `/pre-spec` and in a batch, as below (case 598.1). ``
>   - old: `` Never move to the next Case until this one is ratified or deferred — but in the loop after the findings of `/pre-spec`, where the Cases built again go out together and come back for one ratification, as `rule-prespec` sets it (case 561.2). ``
>   - new: `` Never move to the next Case until this one is ratified or deferred — but where Cases are handled side by side they go out together and come back for one ratification: in the loop after the findings of `/pre-spec`, as `rule-prespec` sets it (case 561.2), and in a batch, when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (case 598.1). ``
>   - old: `a sub-case the person questions or changes is shown again alone (case 355.2).`
>   - new: `` a sub-case the person questions or changes is shown again alone (case 355.2). When, before `/pre-spec`, the person's answer to a round or the person's word on a shown Case asks that a Case already ratified in the session change, the agent sends that Case back to its `case-guppi` by `SendMessage` and shows neither it nor the Case being built alone: the two are a batch, and a Case that a Case of the batch asks to change in the same way joins it. The batch takes the steps of the loop of `rule-prespec`: while an answer is out, each turn ends with one line under the bold label `**Waiting:**`, translated, naming the Cases that have answered and those still out, and nothing else; one list shows every round that came back, each question numbered `<Case id>.Q<n>`; each answer goes to the `case-guppi` of its Case, all in one message; and every Case of the batch is shown in one reply, each in the showing `## Who builds a Case` sets, for one ratification. The person ratifies the batch at once or names the ids; a Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change (case 598.1). ``
>   - change: `Cases handled side by side go out together: a ratified Case that must change is shown with the Case that changes it, for one ratification (case 598.1)`
> - [ ] create `estimate-orchestration-signs-a-batch-together`
>   - type: `estimate`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether, when the person's word asks that a ratified Case change while another Case is built, the main agent sends it back and shows the two Cases together for one ratification, with the rounds gathered and the waits marked as after the findings of pre-spec`
>   - method: `by hand at the first Plan Mode of a later session after the render in which the person's word asks that a ratified Case change: the SendMessage calls and the replies from that word to the acknowledging reply, read in the transcript`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-signs-a-batch-together`

> **ratification:**
> ```
> - decision[case 598.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 598.1][create][estimate-orchestration-signs-a-batch-together]{ref:rule-orchestration}{tags:session,workflow}
> ```

### Case 598.2 — One reply acknowledges every Case ratified in one answer

> **given:**
> `rule-orchestration` — the sentence on sub-cases in `## Showing and signing a Case`, widened
> **＋** `vault/wiki/orchestration.md` — the render of `rule-orchestration`
> **＋** `estimate-orchestration-acknowledging-reply` — the promise of the reply, its Criterion and `method` replaced
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows
> **＋** `rule-ledger-write` — the ledger hook, which writes the `LEDGER` block and does not append a line it already holds; unchanged
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no line under `## Cases` is open; unchanged
> **＋** `raw/2026-10-02/2049/cases/case-597.md` — Case 597, which sets what that hook does after this reply

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the person ratifies them all at once or names the ids, and the acknowledging reply carries one `LEDGER` block with the lines of every sub-case ratified, one heading `## Case N — ratified` naming those ids, and one Frontier; ``
>   - new: `` the person ratifies them all at once or names the ids; one reply acknowledges every Case the person ratified in one answer — a Case with its sub-cases, or the Cases of a batch or of the loop after the findings of `/pre-spec` — with one `LEDGER` block holding the decision lines of each, one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier (case 598.2); ``
>   - change: `one reply acknowledges every Case ratified in one answer, under one heading that names their ids (case 598.2)`
> - [ ] update `estimate-orchestration-acknowledging-reply`
>   - set: `{status: pending, method: "one reading by hand of the first acknowledging reply of a session, and of the first reply that acknowledges Cases ratified together in one answer"}`
>   - change: `the Criterion replaced whole — one reply acknowledges every Case ratified in one answer (case 598.2)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-acknowledging-reply`

> **ratification:**
> ```
> - decision[case 598.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 598.2][update][estimate-orchestration-acknowledging-reply]{ref:rule-orchestration}
> ```

### Case 598.3 — The pre-spec loop no longer owns signing together

> **given:**
> `estimate-prespec-gathers-the-answers-after-findings` — the promise of the loop after the findings, its Criterion replaced
> **＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — the loop after the findings; unchanged
> **＋** `vault/wiki/orchestration.md` — sets the batch outside the loop
> **＋** `case-guppi` and `SendMessage` — the agent of each Case, and the call that sends it its findings
> **＋** `.claude/skills/grill-me/SKILL.md` — the shape of each question
> **＋** `uv run guppi casecheck` — the `Stop` check of `rule-case-check`

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

> **tasks:**
> - [ ] update `estimate-prespec-gathers-the-answers-after-findings`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — outside the loop, Cases go out together only in a batch that orchestration.md sets (case 598.3)`
> - [ ] read `estimate-prespec-gathers-the-answers-after-findings`

> **ratification:**
> ```
> - decision[case 598.3][update][estimate-prespec-gathers-the-answers-after-findings]{ref:rule-prespec}
> ```
