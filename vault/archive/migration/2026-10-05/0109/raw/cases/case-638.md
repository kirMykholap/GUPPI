## Case 638 — The ask-guppi confirmation allows a short paragraph per finding, ends with what it did not check and the files it read, and the message that asks for it invites no new finding

> **context:**
> At `/pre-spec`, a finding of `ask-guppi` can send a Case back to its `case-guppi` to be rebuilt. The main agent then sends the rebuilt Cases to the same `ask-guppi` runs, and each run says whether each of its findings is closed (case 634.2). The frame of `ask-guppi` asks for one line per finding: `closed`, or `not closed` and one sentence on what still stands. Nothing more may stand in the answer. The reading of `estimate-prespec-confirms-the-findings-once` at the `/pre-spec` of session 2245 failed on two points. First, both runs gave the right verdicts but not in that form. The confirmation answers stand in the last assistant text of the agent transcripts `agent-aab5addf1e347ccb8.jsonl` (Case 636) and `agent-a390781c7f1241c18.jsonl` (Case 637), in the subagents folder of session `7086b96c`:
> - The run of Case 636 opened with three sentences. It put each verdict on a line of its own, with two to five sentences under it, and closed with a **Not checked** list and a **Files read** list. Its **Not checked** list named a part of the rebuilt Case that it could not settle without a new read.
> - The run of Case 637 gave each finding a paragraph: the verdict, then three to five sentences. A paragraph of four sentences followed, saying it had not judged the overlap with Case 636, and then a **Files read** list.
>
> The `## Result` of the Estimate counts one to four sentences and two to four sentences, and it records no list. The counts above come from the transcripts. Second, the main agent's message invited "a new defect the rebuild itself brought in". Both runs declined it, because their frame forbids a new finding. `lesson-prespec-confirmation-prompt-invites-a-new-finding` records the second point, under `insight-prespec-after-findings-loop-unruled`. In the decision on Case 634, the person ruled out a new check run because a fresh agent always finds something and the checks would never end. The one-line form came from that Case's recommendation wording, not from an answer of the person.
>
> The person chose these changes. The answer gives each finding a line of its own with `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why. After the findings stands a list of what the run did not check, and then a list of the paths of the files it read. Nothing else stands. The general instruction of Claude Code to share file paths is met by the second list. The `/pre-spec` rule also says what the main agent's message asks: whether each finding is closed, and nothing more. The person was not sure about the rule on the message and chose to try it as planned. No hook checks the form. A Grep of `ask-guppi|ask_guppi` over `guppi/` printed nothing, so no code judges an answer of `ask-guppi`, and this Case adds none. The next reading of the Estimate shows whether the new words hold.
>
> The list of what the run did not check came from the `/pre-spec` of this session. The first build allowed only the list of files read and forbade a list of what was not checked. The run of `ask-guppi` that judged this Case found that this left no place to name what was not done. `rule-agent-writing` (`built`, rendered into `CLAUDE.md`) asks that the not-done is never left implied. Case 639 keeps that list in the first answer of the same agent and ends it with a line for each search rule the agent broke. A confirmation that breaks its frame, for example by running a Grep, had no line to say so. The person chose the form of the first answer. After the findings stands the list of what was not checked, "none" when the run checked all of it and broke no rule, its last lines one per rule a search broke. Then stands the list of the files read. The new text of `rule-ask` points to the paragraph on the first answer for that list, the paragraph Case 639 changes. If Case 639 changes which rules such a line names, the confirmation follows it. The run of Case 637 wrote what it did not judge in a paragraph of its own; the new form puts that in the list.
>
> The pages. `rule-prespec` and `rule-ask` are both `draft`. Every item is an `update` with a `ref`, so the vault query of `ask-guppi` was not run. The Criterion of `estimate-prespec-confirms-the-findings-once` is replaced whole. Its `purpose` states the old one-line form, and its `method` names the render by case 634.2, so both are set anew. Most lines of the old Criterion stand word for word: the question after the confirmation, the showing in one reply, no second confirmation, no new finding and no Grep, and the onward hook. Three lines change on purpose:
> - The first line now says the main agent asks only whether each finding is closed. A new `－` line says the message invites no new finding.
> - The line on the one-line answer is replaced by the verdict line with at most three sentences under it.
> - A new line sets the list of what was not checked and the list of files read.
>
> The searches this Case rests on:
> - A Grep of `finding is closed|findings is closed|not closed|confirm(s|ed|ation)? (its|their|of) (own )?findings` over `vault/wiki/rules/` printed `rule-orchestration.md`, `rule-prespec.md` and `rule-ask.md`, and the same Grep over `.claude/` printed `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/ask-guppi.md`. They are placed as follows:
>   - The confirmation paragraph of `rule-ask` and step 6 of `rule-prespec` enter the Case, and so do their renders.
>   - Step 7 of `rule-prespec` says that what step 6 found closed and not closed stands after the horizontal rule. It stays true.
>   - The live hit in `rule-orchestration.md` lists the question on a finding not closed among the main agent's own questions. It stays true.
>   - The other hits are History lines, which were not read.
> - The same Grep over `vault/wiki/orchestration.md` printed 1 occurrence. It says `ask-guppi` is asked again only to confirm its own findings, and names the question on a finding not closed, and both stay true.
> - The same Grep over `vault/wiki/estimates/` printed `estimate-orchestration-shows-the-built-case.md`, `estimate-prespec-confirms-the-findings-once.md` and `estimate-orchestration-asks-in-the-grill-me-shape.md`. The second enters the Case. The other two speak of when `ask-guppi` is dispatched and of the shape of the question after the confirmation. Neither speaks of the form of the answer or of the words of the message, so their Criteria stand.
> - A Grep of `one line per finding|one sentence on what still stands` over `.claude/` printed `.claude/agents/ask-guppi.md`, which enters the Case. Over `guppi/` it printed `guppi/lint.py`, whose docstring speaks of the output of lint, and it stands.
>
> The other Estimates of the two rules stand. `estimate-ask-finds`, which Case 639 replaces, `estimate-ask-searches-at-prespec` and `estimate-ask-query-before-a-create` speak of the first answer of `ask-guppi` and of the vault query, not of the confirmation. `estimate-prespec-gathers-the-answers-after-findings` speaks of steps 2 to 5 of the loop, which do not change.
>
> Not done:
> - No hook enforces the form. The person chose to allow the paragraph rather than enforce it.
> - No mark is written on the lesson or the Insight. The lesson is of another session, and the librarian's run judges the Insight.
> - The failed reading of `estimate-ask-searches-at-prespec` is the subject of Case 640, which this Case does not cover.

> **problem:**
> The frame of `ask-guppi` asks for one line per finding at the confirmation. Both runs of the last `/pre-spec` wrote reasons of several sentences instead. Both added a list of files read, and one added a list of what it did not check. Their verdicts were right. The main agent's message also invited a new finding, which the frame forbids. The question is whether that form is enforced or loosened, what else the answer may hold, and whether the message gets a rule of its own.

> **recommend:**
> - **How the form of the confirmation answer is held**
>   - Recommended: (a) allow a short paragraph: for each finding, the verdict on its own line under its number, then at most a short paragraph of up to three sentences on why; the rule text and the check's wording change to match.
>   - Answer: (a).
> - **What else may stand in the confirmation answer**
>   - Recommended: (a) findings only, even where a general instruction asks for file paths.
>   - Answer: (b) after the findings, one list of the paths of the files the agent read; no list of what it did not check.
> - **Whether the main agent's confirmation message gets its own rule**
>   - Recommended: (a) the `/pre-spec` rule says the message asks only whether each finding is closed and invites no new finding and no new judgment of the Case; the check gets a line on it.
>   - Answer: the person asked for an explanation, then said they are not sure but will try it as planned: (a).
> - **Change**
>   - Asked: at the `/pre-spec` of this session, the run of `ask-guppi` found that the ban on a list of what was not checked goes against `rule-agent-writing`, and leaves a confirmation that breaks its frame no line to say so. Asked whether the confirmation takes the form of the first answer or keeps the form as chosen, the person chose (a), the form of the first answer, as recommended.
>   - Taken: after the findings stands a list of what was not checked, "none" when all is checked and no rule broken, its last lines one per rule a search broke, as Case 639 sets it for the first answer; then the list of files read; `rule-agent-writing` and the case file of Case 639 enter `given`.
> - **Change**
>   - Asked: the same `/pre-spec` found that the `context` counted the sentences of the two answers and named their lists differently from the `## Result` of the Estimate.
>   - Taken: the counts and the lists now come from the two agent transcripts, which the `context` names, and the `problem` says which run added which list.

> **given:**
> `rule-prespec` and `.claude/skills/pre-spec/SKILL.md`: the skill and its render. Step 6 of the loop after the findings changes.
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md`: the frame of the agent and its render. The form of the answer to the confirmation changes.
> **＋** `estimate-prespec-confirms-the-findings-once`: its Criterion is replaced whole, and its `purpose` and `method` are set anew.
> **＋** `vault/raw/2026-10-05/0109/cases/case-639.md`: it sets the list of what was not checked in the first answer, the list the confirmation follows.
> **＋** `rule-agent-writing` and `CLAUDE.md`: they ask that the not-done is named.
> **＋** `rule-orchestration` and `vault/wiki/orchestration.md`: they name the confirmation and the question after it. Unchanged.
> **＋** `rule-prespec-onward` and `guppi/onward.py`: after the ratification of the Cases built again, they send the agent to the check and the exit. Unchanged.
> **＋** `case-guppi` and `.claude/skills/grill-me/SKILL.md`: they rebuild a Case on a finding and set the shape of the question after the confirmation.

> **when:**
> `/pre-spec` has reported findings that sent Cases of the plan back, and every `case-guppi` that got a finding has answered with its Case built again, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The main agent sends each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and asks only whether each of its findings is closed.
> **＋** For each finding of its own, under the finding's number, each `ask-guppi` answers with a line that holds `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why.
> **＋** After the findings stands one list of what the agent did not check in confirming them. The list says "none" when it checked all of it and its searches broke no rule. Its last lines name each rule that a search of the agent broke, one line each, and say whether a verdict rests on what that search printed. Then stands a list of the paths of the files the agent read, and nothing else stands before or after.
> **＋** The main agent asks the person a question after the confirmation, in the shape of `.claude/skills/grill-me/SKILL.md`: whether each finding not closed is fixed or left; it sends a finding to be fixed to the `case-guppi` of its Case.
> **＋** It then shows every Case built again in one reply, for one ratification, and writes what the confirmation found closed and not closed in its own text after the horizontal rule.
> **－** The message of the main agent invites no new finding and no new judgment of a Case beyond those findings.
> **－** No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched.
> **－** The answer of `ask-guppi` names no new finding; it runs no Grep, the Grep of the rules included, and reads only the Cases built again and the pages its findings name.
> **－** After that ratification the hook of `rule-prespec-onward` sends the agent to the check and the exit, as before.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` and ask whether each of its findings is closed; wait for every answer as step 3 sets it. ``
>   - new: `` and ask only whether each of its findings is closed: the message invites no new finding and no new judgment of a Case beyond those findings (case 638); wait for every answer as step 3 sets it. ``
>   - change: `the confirmation message of step 6 asks only whether each finding is closed and invites no new finding (case 638)`
> - [ ] update `rule-ask`
>   - old: `` answer with one line per finding of yours, under its number: `closed`, or `not closed` and one sentence on what still stands. Run no Grep ``
>   - new: `` answer, for each finding of yours under its number, with a line that holds `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why. After the findings stand one list of what you did not check in confirming them, in the form the paragraph below sets for that list of the first answer — "none" when you checked all of it and your searches broke no rule, its last lines one per rule a search of yours broke, each saying whether a verdict rests on what that search printed — and then the list of the paths of the files you read; nothing else stands before or after them (case 638). Run no Grep ``
>   - change: `the confirmation answer gives each finding a verdict line and at most three sentences on why, then the list of what was not checked in the form of the first answer, then the list of the files read, and nothing else (case 638)`
> - [ ] update `estimate-prespec-confirms-the-findings-once`
>   - set:
>     ```
>     status: pending
>     purpose: 'Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, asked by a message that invites no new finding, with no Grep, a verdict line closed or not closed per finding and at most three sentences on why, then a list of what was not checked ending with a line per rule a search broke, and the list of the files read and nothing else, no new finding, a finding not closed fixed or left by the person''s answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice'
>     method: 'by hand at the /pre-spec of a later session whose findings send a Case back to its case-guppi, after the render of .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md by case 638: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line'
>     ```
>   - change: `the Criterion replaced whole — a verdict line and at most three sentences per finding, then what was not checked and the files read; the confirmation message invites no new finding (case 638)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-prespec-confirms-the-findings-once`

> **ratification:**
> ```
> - decision[case 638][update][rule-prespec]{ref:rule-prespec}
> - decision[case 638][update][rule-ask]{ref:rule-ask}
> - decision[case 638][update][estimate-prespec-confirms-the-findings-once]{ref:rule-prespec}
> ```
