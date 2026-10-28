## Case 890 — The check reads a Case built again as its file holds it, and the clean Cases of a batch go first

> **context:**
> The check of the file of a Case judges it with the other Cases of the session. `other_blocks` of `.guppi/guppi/casecheck.py` gives them: each Case of the plan file as last ratified, then each entry of `<plan>.checked.json` under its number alone that the plan file does not hold. A Case built again after its ratification is so taken from the plan file, while `unread_sentences` looks for the words its pairs wrote in a `Read` of its current file `raw/<date>/<hi HHMM>/cases/case-<N>.md`. At `/pre-spec` of session 2307 Case 883 was built again, and the `Stop` check of `rule-case-check` refused the showing of Case 881 three times on 881.24, since the words of the old 883 stood in no file that its `case-guppi` read (`lesson-casecheck-reads-a-sibling-from-the-plan-as-last-ratified`). That refusal held back the reply that showed the five Cases of the loop together, so the one Case with a finding held back the four with none; the person ratified 882, 883, 884 and 886 first and 881 after, and put both matters off by Case 887. The person chose that the check takes such a Case as its file holds it, when its stored entry has no finding, in each judgment that reads `other_blocks`, so that one list of the other Cases stays, as `rule-one-judgment-one-implementation` sets it; and that, when the `Stop` check refuses a showing of a batch for a finding stored with one Case, that Case goes back to its `case-guppi` and leaves the batch and the other Cases are shown for ratification, in every batch before `/pre-spec` and in the loop after its findings. `rule-case-check` and `rule-orchestration` carry `deferred_by` with `decision-case-887`, so Case 890.1 and Case 890.3 carry `{supersedes:case 887}` on the decision lines that name them. `rule-orchestration` also carries `decision-case-884`, for the growing context of `case-guppi`; the person chose to leave that matter out, so no line carries `{supersedes:case 884}`, which would retire the whole of Case 884, and the page stays in `backlog.md` through it. The Frontier line C2 has the source `brief`, so the check of an open `backlog` line does not bear on it. A Grep of `other_blocks` over `.guppi/` printed `.guppi/guppi/casecheck.py` alone, so the change stays in the one function that gives the other Cases; `ratified.py` and `prespec.py` read the plan file by their own `split_cases`, and this Case does not change them. Among the Estimates of `rule-case-check`, the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` says the other Cases are each Case of the plan file, which the change makes false, so Case 890.2 replaces it whole and rewrites that one line, carrying every other line as it stands; `estimate-case-check-applies-the-pairs-of-the-session-in-order`, `estimate-case-check-notes-a-page-the-cascade-archives`, `estimate-case-check-notes-a-sentence-two-cases-change` and `estimate-case-check-leaves-out-a-case-the-file-supersedes` name the other Cases as `other_blocks` gives them, or the pairs of the other Cases of the session applied before those of the file, or a Case a mark leaves out, and stay true, since they do not say which text of a Case counts; `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read` looks for the part another Case wrote in a read of that Case's file, which stays true and now finds it. A Grep of `for one ratification` over `vault/wiki/` printed 12 files: `orchestration.md`, `log.md`, `rule-orchestration`, `rule-prespec`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-orchestration-marks-each-round-of-a-batch`, `estimate-orchestration-signs-a-batch-together`, `estimate-orchestration-signs-items-taken-together`, `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`, `estimate-prespec-confirms-the-findings-once`, `estimate-orchestration-acknowledging-reply` and `estimate-orchestration-batches-cases-out-at-once`. Each hit outside `log.md` and the History lines says that every Case of a batch, or every Case built again, is shown in one reply for one ratification; that showing still comes first, and the new step only follows its refusal, with the Case sent back out of the batch, so the hits stand; the person chose that the Criterion of `estimate-prespec-gathers-the-answers-after-findings` names the new step, and Case 890.4 replaces it, carrying its other lines but the two on the labelled line and on writing nothing else, which gain the exception of the reply that answers the refusal; since `.claude/skills/pre-spec/SKILL.md` takes the new text only at the librarian's render, Case 890.4 also sets its `method` to read the new Render of `rule-prespec` in the Spec at Retro, as the Estimate of Case 890.3 does for `rule-orchestration`. That reply sends a Case to its `case-guppi` and shows Cases while that answer is out, which step 3 of `rule-prespec`, the `**Waiting:**` step of a batch and the sentence of case 730.1 on Cases out at the same time would forbid; so the pair of Case 890.3 says that the Case sent back leaves the batch and that neither of those holds for it in that reply, a second pair of 890.3 says so after the sentence of case 730.1, and a pair of Case 890.4 makes the same exception at the end of step 3, so that the reply ends as a showing ends and names the Case sent back as still out in the agent's own text. The Criterion of `estimate-orchestration-shows-the-built-case` names the reply that follows a refusal of the `Stop` check for a file not sent or a showing that differs from the checked text; a stored finding is neither, so its Criterion stays true and the new step stands beside it. Case 889 makes the hook of `rule-prespec-onward` send the agent on after `/pre-spec` while a Case is still out, with a reason that names it and, while a `case-guppi` has not answered, sends the agent to the end of the turn that `orchestration.md` sets for a Case out; so the pair of Case 890.3 sets that end: the answer to the refusal ends as a showing, and each later turn while the `case-guppi` of the Case sent back has not answered and no Case shown waits for the person ends with the `**Waiting:**` line that names it. This Case does not change that hook. A Grep of `orchestration\.md` over `.guppi/tests/` printed `.guppi/tests/test_orchestration.py`, which reads only the blocks tagged `showing` and `defer` of the live `orchestration.md`, and this Case leaves both blocks as they are; `.guppi/tests/test_case_schema.py` runs `check_answer` with no store, so it does not reach `other_blocks`. The lesson stands in the ledger of session 2307, so no decision line carries `{addresses:...}`.

> **problem:**
> The check of a Case reads another Case built again from the plan as last ratified and looks for its words in its current file, so a sibling built again makes the check fail until it is ratified again; and one Case of a batch with a stored finding holds back the showing of every Case of the batch.

> **recommend:**
> - **Which text of another Case the check uses**
>   - Recommended: (a) the last built text, for every check.
>   - Answer: agreed, (a).
> - **What happens when the check refuses one Case of a batch**
>   - Recommended: (a) the clean Cases are shown at once, and the faulty one goes back.
>   - Answer: agreed, (a).
> - **The other put-off on `rule-orchestration`**
>   - Recommended: (a) it stays out of this Case.
>   - Answer: agreed, (a).
> - **Where the clean Cases go first**
>   - Recommended: (a) in both places, a batch before `/pre-spec` and the loop after its findings.
>   - Answer: agreed, (a).
> - **How the change to the check is checked**
>   - Recommended: (a) a new check, with the clash check reworded.
>   - Answer: agreed, (a).
> - **How the change to the batch is checked**
>   - Recommended: (a) a new check for the batch, and the loop check reworded.
>   - Answer: agreed, (a).

### Case 890.1 — A Case built again counts as its file holds it

> **given:**
> `estimate-case-check-takes-a-case-built-again-from-its-file`: the new check of which text of another Case counts.
> **＋** `rule-case-check`: the rule of the check, whose Purpose gains the sentence.
> **＋** `.guppi/guppi/casecheck.py`: `other_blocks`, the one list of the other Cases of the session.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the check.
> **＋** `<plan>.checked.json`: the store of the checked Cases beside the plan file.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files.
> **＋** `rule-one-judgment-one-implementation`: one list of the other Cases for every judgment.

> **when:**
> The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file under `raw/<date>/<hi HHMM>/cases/`, while the plan file of the session holds another Case that `<plan>.checked.json` holds under its number alone with another text, since it was built again after its ratification.

> **then:**
> The hook takes that other Case as `<plan>.checked.json` holds it, in place of its text in the plan file, when its entry holds no finding and the file under `raw/<date>/<hi HHMM>/cases/` of its top-level Case holds its heading.
> **＋** It takes it so in each judgment that reads the other Cases of the session through `other_blocks` of `.guppi/guppi/casecheck.py`: the clash of two Cases, the order of the `replace` and `reword` pairs, the read of the sentence around each pair, and the notes of the cascade.
> **＋** A part of a sentence that a pair of that other Case wrote then counts as read when it stands whole in the outputs of the `Read` calls of the subagent on the file of that Case.
> **＋** The other Cases keep the order of the plan file, and the entries the plan file does not hold come after them, as before.
> **－** An entry with findings, an entry joined with an agent id, and an entry whose top-level file is empty or no longer holds its heading leave the other Case as the plan file holds it.
> **－** The hook writes nothing to the plan file or to `<plan>.checked.json` for this judgment.

> **tasks:**
> - [ ] create `estimate-case-check-takes-a-case-built-again-from-its-file`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of the file of a Case takes another Case of the session that was built again after its ratification as its stored text holds it, in place of the plan file, in every judgment that reads the other Cases, so that the words its pairs wrote are found in a read of its file`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k built_again_sibling`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `while the build it replaces stands in the plan (case 725.2).`
>   - new: `while the build it replaces stands in the plan (case 725.2). A Case of the plan that was built again after its ratification, whose entry in the store holds no finding and whose top-level file still holds it, is taken as the store holds it, in place of the plan, in each judgment that reads the other Cases, so that the words its pairs wrote are judged, and looked for in a read of its file, as the person will ratify them (as set in case 890.1).`
>   - change: `a Case built again after its ratification counts as its stored text holds it, not as the plan holds it`
> - [ ] `.guppi/guppi/casecheck.py`: in `other_blocks`, for each Case of the plan, the entry of the store under the same id with no findings and a text, whose top-level file is not `dropped` and is not `left_by_its_file`, gives its `then` block in place of the plan's, in the plan's order; the docstring of `other_blocks` and the passage of the module docstring that says "each Case of the plan file, then each entry of the store under the number alone that the plan does not hold" say so.
> - [ ] `.guppi/tests/test_casecheck.py`: tests named `built_again_sibling`: a Case of the plan built again in the store with a pair that writes a new sentence, and an answer whose pair matches in that sentence with a `Read` of the page and of the file of that Case, gives no finding that the sentence was not read; an old text that only the plan's version wrote gives the answer a finding of `check_pairs`; an entry with findings, and an entry whose file no longer holds its heading, leave the plan's text; the first two fail on the code before the change.
> - [ ] read `estimate-case-check-takes-a-case-built-again-from-its-file`

> **ratification:**
> ```
> - decision[case 890.1][create][estimate-case-check-takes-a-case-built-again-from-its-file]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 890.1][update][rule-case-check]{ref:rule-case-check}{supersedes:case 887}
> ```

### Case 890.2 — The clash check names the text of a Case built again

> **given:**
> `estimate-case-check-sends-back-a-clash-with-another-case`: its Criterion is replaced whole.
> **＋** `estimate-case-check-takes-a-case-built-again-from-its-file`: which text of a Case built again counts.
> **＋** `estimate-case-check-leaves-out-a-case-the-file-supersedes`: the Cases a mark of the file leaves out.
> **＋** `.guppi/guppi/casecheck.py`: the hook and `other_blocks`.
> **＋** `.guppi/guppi/prespec.py`: `check_same_target`, the judgment of a clash.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the clash.
> **＋** `<plan>.checked.json`: the store of the checked Cases beside the plan file.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a top-level Case.
> **＋** `uv run --project .guppi guppi ratified`: the `Stop` hook that writes the Cases into the plan file.
> **＋** `rule-prespec-onward`: the hook that judges a dropped Case by the same function.

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.

> **then:**
> The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `.guppi/guppi/prespec.py`, imported, not copied: each Case of the plan file, as `estimate-case-check-takes-a-case-built-again-from-its-file` sets it for a Case built again after its ratification, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
> **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
> **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
> **－** A stored Case that has findings, an entry joined with an agent id, a Case whose number a `{supersedes:case N}` mark of the session's ledger names, and a Case left out as `estimate-case-check-leaves-out-a-case-the-file-supersedes` sets are not compared.
> **－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds nothing but blank space is a dropped Case and is not compared, judged by the one function of `.guppi/guppi/casecheck.py` that the hook of `rule-prespec-onward` uses too.
> **－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds text but no heading of its id is a part that a Case built again no longer holds, and is not compared; its entry stays in the store.
> **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
> **－** Two other Cases that clash with each other give this answer no finding.
> **－** The `Stop` hook `uv run --project .guppi guppi ratified` keeps its check of the Cases it writes, by the same function.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-clash-with-another-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a Case of the plan built again after its ratification is compared as its stored text holds it`
> - [ ] `.guppi/tests/test_casecheck.py`: a test named `session_clash` has a Case of the plan that sets a field to one value and its entry built again in the store that sets another, and asserts that an answer clashes with the stored value and not with the plan's; it fails on the code before the change.
> - [ ] read `estimate-case-check-sends-back-a-clash-with-another-case`

> **ratification:**
> ```
> - decision[case 890.2][update][estimate-case-check-sends-back-a-clash-with-another-case]{ref:rule-case-check}
> ```

### Case 890.3 — The clean Cases of a batch are shown while the faulty one goes back

> **given:**
> `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`: the new check of the showing after a refusal.
> **＋** `rule-orchestration`: the rule of the main agent, whose Render gains the sentence.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-case-check`: the `Stop` check that refuses a showing of a Case with a stored finding.
> **＋** `<plan>.checked.json`: the store that holds the findings of each Case.
> **＋** `rule-prespec`: the loop after the findings of `/pre-spec`.
> **＋** `case-guppi`: the agent that builds each Case.
> **＋** `raw/2026-10-26/0118/cases/case-889.md`: the Case whose hook names the Case sent back after `/pre-spec` and points to `orchestration.md` for the end of the turn.

> **when:**
> In Plan Mode, the `Stop` check of `rule-case-check` refuses a reply of the main agent that shows the Cases of a batch, for a finding that `<plan>.checked.json` holds with one of them, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent sends the Case whose finding the refusal names, with its top-level Case and each sub-case of that file, back to its `case-guppi` by `SendMessage` with the finding, and that Case leaves the batch.
> **＋** In its answer to the refusal it shows the other Cases of the batch, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification, and the person ratifies them at once or names the ids.
> **＋** The Case sent back is shown when its `case-guppi` answers, as a Case the person questions or changes is shown again: alone when no other Case of the session is out, and otherwise in a batch with the Cases still out.
> **＋** The answer to the refusal ends as a showing ends, its own text after the horizontal rule naming the Case sent back as still out; the Case sent back is out of the batch, so neither the `**Waiting:**` line of a batch nor the joining of Cases out at the same time holds for it in that answer.
> **＋** Each later turn that ends while its `case-guppi` has not answered, and while no Case shown waits for the person's word, ends with one line under the bold label `**Waiting:**`, translated, that names the Case sent back, and nothing else.
> **＋** This holds in every batch before `/pre-spec` and in the loop after the findings of `/pre-spec` that `rule-prespec` sets.
> **－** A refusal for a file not sent, or for a showing that differs from the stored text, sends no Case back: the main agent sends the file and shows the Cases as `vault/wiki/orchestration.md` sets it.
> **－** The main agent puts before the person no Case that the check refused for a stored finding.

> **tasks:**
> - [ ] create `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether, when the Stop check of rule-case-check refuses the showing of a batch for a finding stored with one of its Cases, the main agent sends that Case back to its case-guppi, out of the batch, and shows the other Cases for ratification, before /pre-spec and in the loop after its findings`
>   - method: `by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] update `rule-orchestration`
>   - old: `or in a new batch with each Case it asks to change (case 598.1).`
>   - new: `` or in a new batch with each Case it asks to change (case 598.1). When the `Stop` check of `rule-case-check` refuses a reply that shows the Cases of a batch, or of the loop after the findings of `/pre-spec`, for a finding stored with one of them, the agent sends that Case, with each Case of its file, back to its `case-guppi` by `SendMessage` with the finding, that Case leaves the batch, and the agent's answer to the refusal shows the other Cases for one ratification and ends as a showing ends, its own text after the horizontal rule naming the Case sent back as still out, since neither the `**Waiting:**` line of a batch nor the sentence below on Cases out at the same time holds for a Case out of the batch; each later turn that ends while its `case-guppi` has not answered, and while no Case shown waits for the person's word, ends with one line under the bold label `**Waiting:**`, translated, that names it, and nothing else; the Case sent back is shown when its `case-guppi` answers, as a Case the person questions or changes is shown again, and a refusal for a file not sent or for a showing that differs from the stored text sends no Case back (as set in case 890.3). ``
>   - old: `and every Case of the batch is shown in one reply (case 730.1).`
>   - new: `and every Case of the batch is shown in one reply (case 730.1). A Case sent back for a finding stored with it, while the other Cases are shown, is no such route: it is out of the batch, as the sentence above on a refusal sets it (as set in case 890.3).`
>   - change: `a Case of a batch with a stored finding goes back to its case-guppi and the other Cases are shown for ratification`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`

> **ratification:**
> ```
> - decision[case 890.3][create][estimate-orchestration-shows-the-clean-cases-of-a-batch-first]{ref:rule-orchestration}{tags:session,workflow}
> - decision[case 890.3][update][rule-orchestration]{ref:rule-orchestration}{supersedes:case 887}
> ```

### Case 890.4 — The loop after the findings shows the clean Cases first

> **given:**
> `estimate-prespec-gathers-the-answers-after-findings`: its Criterion is replaced whole.
> **＋** `rule-prespec`: the skill `/pre-spec`, whose step 7 gains the sentence.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the file rendered from `rule-prespec`.
> **＋** `vault/wiki/orchestration.md`: the showing of a Case and of a batch.
> **＋** `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`: the check of the showing after a refusal.
> **＋** `rule-case-check`: the `Stop` check that refuses a showing of a Case with a stored finding.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a question.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose items the labels name.
> **＋** `uv run --project .guppi guppi casecheck`: the command of the check.

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out, but for the reply that answers a refusal of the showing of the Cases built again, which ends as `estimate-orchestration-shows-the-clean-cases-of-a-batch-first` sets it.
> **＋** That line holds nothing of what an answer says and no question, and but for that reply the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`; a horizontal rule stands before the first round of the list and one between the last question of one Case and the round of the next, and no heading or other line of the main agent's own but such a rule marks where a round begins.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **＋** After a refusal of that reply by `rule-case-check`, step 7 of `.claude/skills/pre-spec/SKILL.md` sends the main agent to the step of `vault/wiki/orchestration.md` that `estimate-orchestration-shows-the-clean-cases-of-a-batch-first` checks.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run --project .guppi guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` 7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. ``
>   - new: `` 7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. When the check of `rule-case-check` refuses that reply for a finding stored with one of those Cases, send that Case back to its `case-guppi` with the finding and show the others for ratification, as `vault/wiki/orchestration.md` sets it for a batch, and end that reply as the exception of step 3 sets it (as set in case 890.4). ``
>   - old: `` and the label lets the reply pass the check of `rule-case-check` (case 581.1). ``
>   - new: `` and the label lets the reply pass the check of `rule-case-check` (case 581.1). The one exception is the reply of step 7 that answers a refusal of the check for a finding stored with one Case built again: it sends that Case back to its `case-guppi`, shows the other Cases, and ends as a showing ends, your own text after the horizontal rule naming the Case sent back as still out (as set in case 890.4). ``
>   - change: `step 7 sends a Case built again with a stored finding back and shows the others for ratification; step 3 makes that reply its one exception`
> - [ ] update `estimate-prespec-gathers-the-answers-after-findings`
>   - set:
>     ```
>     status: pending
>     method: "by hand at Retro of the session that changes it: the new Render of rule-prespec in the Spec, read against the Criterion, recorded in the estimate line"
>     purpose: "Whether after the findings of pre-spec the main agent sends nothing to a case-guppi until the person has answered every question of the report, then sends each case-guppi its findings with the answers in one message, ends each waiting turn with one labelled line and writes nothing else while answers are out, gathers every round into one numbered list, and shows the Cases built again in one reply, a Case whose stored finding the check refuses sent back and the others shown, as estimate-orchestration-shows-the-clean-cases-of-a-batch-first sets it"
>     ```
>   - change: `the Criterion replaced whole — after a refusal for a stored finding, step 7 sends that Case back and shows the others`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-gathers-the-answers-after-findings`

> **ratification:**
> ```
> - decision[case 890.4][update][rule-prespec]{ref:rule-prespec}
> - decision[case 890.4][update][estimate-prespec-gathers-the-answers-after-findings]{ref:rule-prespec}
> ```
