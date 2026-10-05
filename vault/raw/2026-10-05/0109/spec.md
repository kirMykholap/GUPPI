<!-- approved 03:00:55 · session c080a934 -->

# Spec — session 0109, 2026-10-05

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

```then
update:
- slug: rule-prespec
  replace:
  - old: and ask whether each of its findings is closed; wait for every answer as step 3 sets it.
    new: 'and ask only whether each of its findings is closed: the message invites no new finding and no new judgment of a Case beyond those findings (case 638); wait for every answer as step 3 sets it.'
  change: the confirmation message of step 6 asks only whether each finding is closed and invites no new finding (case 638)
- slug: rule-ask
  replace:
  - old: 'answer with one line per finding of yours, under its number: `closed`, or `not closed` and one sentence on what still stands. Run no Grep'
    new: answer, for each finding of yours under its number, with a line that holds `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why. After the findings stand one list of what you did not check in confirming them, in the form the paragraph below sets for that list of the first answer — "none" when you checked all of it and your searches broke no rule, its last lines one per rule a search of yours broke, each saying whether a verdict rests on what that search printed — and then the list of the paths of the files you read; nothing else stands before or after them (case 638). Run no Grep
  change: the confirmation answer gives each finding a verdict line and at most three sentences on why, then the list of what was not checked in the form of the first answer, then the list of the files read, and nothing else (case 638)
- slug: estimate-prespec-confirms-the-findings-once
  set:
    status: pending
    purpose: Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, asked by a message that invites no new finding, with no Grep, a verdict line closed or not closed per finding and at most three sentences on why, then a list of what was not checked ending with a line per rule a search broke, and the list of the files read and nothing else, no new finding, a finding not closed fixed or left by the person's answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice
    method: 'by hand at the /pre-spec of a later session whose findings send a Case back to its case-guppi, after the render of .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md by case 638: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — a verdict line and at most three sentences per finding, then what was not checked and the files read; the confirmation message invites no new finding (case 638)
```

```tasks
- [ ] update `rule-prespec`
- [ ] update `rule-ask`
- [ ] update `estimate-prespec-confirms-the-findings-once`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-prespec-confirms-the-findings-once`
```

## Case 639 — ask-guppi's first answer at /pre-spec has only findings or "none" under each question, and a line for each search rule it broke

> **context:**
> At the first run of `/pre-spec`, one `ask-guppi` run judges each top-level Case of the plan. It reads the other Cases only to look for a clash with them. Its answer has a set form. It opens with one line on what it read. Under each of the three questions of the skill stands a numbered list of findings, or "none". After the findings come a list of what it did not check and a list of the files it read. The frame forbids a summary and a list of what holds (case 633.1). The reading of `estimate-ask-finds` at the `/hi` of session 0109 failed on both answers at the `/pre-spec` of session 2245. Each answer wrote a paragraph of what holds under question 1. The run of Case 636 wrote it after "none". It said that the `old` text of a `replace` stands word for word in the Render, and that Case 637 changes none of its pages. The run of Case 637 wrote "No clash found between Case 637 and Case 636" after its finding. The frame tells the agent to read the other Cases for a clash, but it does not say what to write when it finds none. At the reading before this one, the extra text was a heading, a summary paragraph, a line on Cases 630 and 631, a paragraph "What the vault does bear out" and a list "Not checked". It is now one paragraph. Both answers also ended their list of what was not checked with a note on a rule of their own search that they broke. The run of Case 636 had searched the archive by content. The run of Case 637 had run a Grep meant to leave out Decision pages, and that Grep printed some. The Criterion does not speak of such a note, and the reading did not count it.
>
> The person chose two changes. Under each question stand only its numbered findings, or "none" alone. No sentence may say what the agent checked and found sound, and this includes a clash with another Case it did not find. The list of what was not checked may end with one line for each search rule that the agent broke, saying whether a finding rests on what that search printed. No hook enforces the form: a Grep of `ask-guppi|ask_guppi` over `guppi/` printed nothing, so no code judges an answer of `ask-guppi`. The next reading of the Estimate shows whether the words hold. If it fails again, a check in code is the next step.
>
> This Case was built again on two findings of `/pre-spec`:
> - Finding 1.1: the broken-rule lines covered only the frame of `ask-guppi`. Case 640 adds a second search rule for every agent, in `.claude/rules/search-leaves-out-decisions.md`. A Grep over `vault/wiki/` without the glob `!**/decisions/**` that prints no Decision line breaks only that file, and under the old wording the list could still say "none". The broken-rule lines now name each rule of either file that a search broke. The list says "none" only when no rule of either file was broken.
> - Finding 3.1: the earlier extra text is now worded as the `## Result` of `estimate-ask-finds` records it.
>
> The pages. `rule-ask` is `draft`. Every item is an `update` with a `ref`, so the vault query of `ask-guppi` was not run. The Criterion of `estimate-ask-finds` is replaced whole. Its `purpose` states the old form, and its `method` names the render by case 633.1, so both are set anew. Most lines of the old Criterion stand word for word in the new one. Two lines change on purpose:
> - The line on the list of what was not checked now says when that list says "none", and adds its end lines on the search rules that were broken.
> - The `－` line on a sentence under a question is new. It says that nothing else stands under a question.
>
> Case 638 of this session also changes `rule-ask`, in its paragraph on the confirmation of findings. It is being built again so that its confirmation answer takes the same end lines. This Case changes only the paragraph on the first answer. Its anchors are not in the paragraph that Case 638 changes, and it sets nothing at the confirmation. Case 640 creates `.claude/rules/search-leaves-out-decisions.md` and does not change `rule-ask`. This Case does not change that file. It only names the file as a source of rules that a broken-rule line reports.
>
> The searches this Case rests on:
> - A Grep of `list of what holds|did not check|says "none"` over `vault/wiki/`, with `decisions/` left out, printed `rule-ask.md`, `estimate-ask-finds.md`, `rule-prespec.md`, `estimate-prespec-reconciles.md`, `lesson-case-ratification-preview-before-its-targets.md` and `log.md`. They are placed as follows:
>   - The first two enter the Case.
>   - `rule-prespec` and the Criterion of `estimate-prespec-reconciles` say that the main agent's report gives, for each run, its list of what it did not check. With the new end lines, that list still stands and the report still carries it. Both stay true, so that Criterion stands.
>   - The hit in the lesson is about a Case preview, not about `ask-guppi`.
>   - The hits in `log.md` and in History lines were not read.
> - The same Grep over `.claude/` printed `.claude/agents/ask-guppi.md`, which enters the Case by its render, and `.claude/skills/pre-spec/SKILL.md`. The skill is the render of `rule-prespec` and stays true for the reason above.
>
> The other Estimates of `rule-ask` stand. `estimate-ask-query-before-a-create` speaks of the vault query of `case-guppi`. `estimate-ask-searches-at-prespec` speaks of which searches the agent runs, not of how its answer reports them. The search that printed Decision lines is the subject of Case 640, which this Case does not cover.

> **problem:**
> The first answer of `ask-guppi` at `/pre-spec` still writes a paragraph of what holds under a question, mostly about the clash with another Case that it did not find. The frame forbids this, but it does not say what stands under a question when nothing is found. Both answers also ended their list of what was not checked with a note on a search rule they broke, and neither the frame nor the check speaks of such a note.

> **recommend:**
> - **How the answer is kept free of a paragraph of what holds**
>   - Recommended: (a) say it plainly: under each question stand only its numbered findings, or "none" alone. No sentence on what was checked and found sound, and this includes a clash with another Case that was not found. The check gets the same line. No code changes.
>   - Answer: (a).
> - **Whether a note on a rule the agent broke may stay in the answer**
>   - Recommended: (b) allow it: the list of what was not checked may end with one line for each rule the agent broke in its search, saying whether a finding rests on it. The rule and the check say so.
>   - Answer: (b).

> **given:**
> `rule-ask` and `.claude/agents/ask-guppi.md`: the frame of the agent and its render. The paragraph on the first answer at `/pre-spec` changes.
> **＋** `estimate-ask-finds`: its Criterion is replaced whole, and its `purpose` and `method` are set anew.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the search rule for every agent that Case 640 creates. Its rules are reported like those of the frame.
> **＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md`: they dispatch the agent with the three questions and carry its list of what it did not check into the report. Unchanged.
> **＋** `vault/raw/<date>/event_log.md`: the event log, where the dispatch is recorded.
> **＋** `vault/raw/2026-10-05/0109/cases/case-638.md`: it changes the paragraph of `rule-ask` on the confirmation of findings.
> **＋** `vault/raw/2026-10-05/0109/cases/case-640.md`: it creates `.claude/rules/search-leaves-out-decisions.md`.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question of `.claude/skills/pre-spec/SKILL.md`, in its order: what contradicts a page, a rule or another Case; an Estimate a Case does not name that speaks of the thing the Case changes; a fact of a `context` the vault does not bear out.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

```then
update:
- slug: rule-ask
  replace:
  - old: and a question with no finding says "none" (case 626.1).
    new: 'and a question with no finding says "none" (case 626.1). Under a question stand only its numbered findings, or "none" alone: no sentence on what you checked and found sound, a clash with another Case you did not find included (case 639).'
  - old: '"none" when you checked all of it, and then the list of the paths of the files you read;'
    new: '"none" when you checked all of it and your searches broke no rule of this file or of `.claude/rules/search-leaves-out-decisions.md`; its last lines name each rule of those files that a search of yours broke, one line each, and say whether a finding rests on what that search printed (case 639); and then the list of the paths of the files you read;'
  change: under a question of the first answer at /pre-spec stand only its findings or "none", no sentence on what holds; the list of what was not checked ends with a line per search rule broken, of the frame or of .claude/rules/search-leaves-out-decisions.md (case 639)
- slug: estimate-ask-finds
  set:
    status: pending
    purpose: Whether ask-guppi answers the questions of /pre-spec with one line on what it read, one numbered list of findings under each question and nothing else under it, each finding naming its Case and the page or Cases it bears on, then a list of what it did not check ending with a line per search rule it broke, of its frame or of .claude/rules/search-leaves-out-decisions.md, and a list of the paths of the files it read, and nothing else
    method: 'by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 639, read in its agent transcript against the event log, recorded in the estimate line'
  change: the Criterion replaced whole — only findings or "none" under a question, no sentence on a clash not found; the list of what was not checked ends with a line per search rule broken, of the frame or of .claude/rules/search-leaves-out-decisions.md (case 639)
```

```tasks
- [ ] update `rule-ask`
- [ ] update `estimate-ask-finds`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-ask-finds`
```

## Case 640 — A file under `.claude/rules/` keeps the text of Decision pages out of the searches of the main agent, `ask-guppi` and `case-guppi`

> **context:**
> `ask-guppi` may not search `vault/wiki/decisions/` except for two named reasons, and both reasons open one Decision page by its path. Its frame does not say how to leave that folder out of a Grep over all of `vault/wiki/`. At the `/pre-spec` of session 2245, call 16 of agent `a390781c7f1241c18` ran a Grep over `vault/wiki` with the glob `!decisions/**`, and the Grep printed lines of Decision pages. The reading of `estimate-ask-searches-at-prespec` at the `/hi` of session 0109 failed on that call. The cause is the way the Grep tool reads a glob. A glob that holds a slash counts from the working directory, which is the repository root, and not from the folder being searched. So `!decisions/**` skips only a `decisions/` folder at the root, and there is none.
>
> I tested this with Greps of `^type: decision` over `vault/wiki/`:
> - With the glob `!decisions/**`, the Grep printed 1080 files.
> - With `!**/decisions/**`, it printed 1 file, `rule-decisions-schema.md`, which is not a Decision page.
> - With `!vault/wiki/decisions/**`, it printed the same 1 file.
> - With `*.md !**/decisions/**`, it printed the same 1 file, so the exclusion also works next to a second filter.
>
> The Glob tool has no field for an exclusion. It prints paths only.
>
> The person first chose to name the glob that works in the frame of `ask-guppi`. They then chose to put the rule in one file under `.claude/rules/`, so that it holds for more than one agent, `case-guppi` included. Claude Code loads the files of `.claude/rules/` into context the way it loads `CLAUDE.md`. The folder does not exist yet: a Glob `.claude/rules/**` printed nothing. The file binds every Grep over `vault/wiki/` or a folder that holds it. It also says that the text of a Decision page is read only by a Read of its path, for a reason the frame of the agent names. A Glob stays free, because it shows no text. No frame lets the main agent read a Decision page, so a question on why something was decided goes to `ask-guppi`, whose frame allows that read.
>
> The `/pre-spec` findings on the ratified Case raised two questions, and the person answered both.
>
> First, where the rule lives. `rule-page-read` records that a file in `.claude/rules/` was weighed for its own rule and not taken, because it is text the agent may follow, and whether it loads inside a subagent is not documented. `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction` says the same of a rules file scoped by `paths:`. It ends: a rule every writer must follow goes where it loads for sure, which is `CLAUDE.md`, the agent's definition or the skill. The new file has no `paths:`, so it does not depend on a matching read. Whether it loads in a subagent is still unknown. The person chose to keep `.claude/rules/` as a trial. The first reading of `estimate-search-leaves-out-decisions-in-every-agent` shows whether the file stands in the context of `ask-guppi` and `case-guppi`. If it does not, a later Case moves the text to `CLAUDE.md`. The sentence of `rule-page-read` stands. It records a choice made for that rule, and its fact about subagents is what this reading tests. The lesson is of another session and gets no mark.
>
> Second, whether the rule binds the librarian. The frame of the librarian, the render of `rule-documentation`, says no read is forbidden to it. A read its job does not need, the text of a Decision page included, gets a line under Flags of the brief and is not a fault. The frame also has it run `git diff` on the files the scripts of the run wrote. The person chose to leave the librarian outside the rule. The file binds the main agent, `ask-guppi` and `case-guppi`, and says the librarian follows its own frame. So that frame and `estimate-documentation-completes` stand, and the new Estimate does not read the librarian.
>
> The pages. `rule-search-leaves-out-decisions` is new, a render Leaf under `rule-harness`. Like `CLAUDE.md`, it governs a file the agent reads when it acts, and the governed-files hook and `render --check` refuse drift in that file. `guppi/render.py` and `guppi/guard.py` read any `governs` path, and `write_all` creates the missing folder, so no code changes. The Purpose of `rule-harness` counts nine rules that run in no pipeline. A tenth child makes that count false, so the Purpose is updated. The `children` field is filled by the scripts from `ref`. A Glob `vault/**/*search-leaves-out-decisions*` printed nothing, so both new slugs are free. The Estimate slug adds `-in-every-agent` to the name shown in the round, to follow the slug form of `case-schema.md`. Both creates carry a `ref`, so the vault query of `ask-guppi` was not run.
>
> What the Case does with the Estimates:
> - `estimate-ask-searches-at-prespec` keeps its Criterion. Its last line already promises that no Grep or Read of `ask-guppi` reaches `vault/wiki/decisions/` outside the two reasons. Only its `method` is set anew, to name the render by this Case.
> - The new Estimate checks the main agent, `ask-guppi` and `case-guppi`, and whether the file loads.
> - `estimate-harness-pipeline` keeps its Criterion. Its line on the rules in no pipeline lists rules the Purpose of `rule-harness` names, and it already leaves out the settings file of guppi that the Purpose names. So it reads as rules the Purpose must hold, not as the whole list. After the update the Purpose still names each rule of that line, and the line stays true.
>
> The frame I read, by these searches:
> - A Grep of `` (Grep|grep|search)[^.]{0,80}`vault/wiki/` `` over `vault/wiki/rules/` printed `rule-case-build.md` and `rule-ask.md`. Over `.claude/` it printed `.claude/agents/case-guppi.md` and `.claude/agents/ask-guppi.md`. These are the rules that set what an agent does at a Grep over the wiki. Each forbids searching the Decision pages and allows only reads by path. The new file agrees with them and gives the means, so they stand.
> - A Grep of `decisions/` over `vault/wiki/rules/` printed `rule-case-build.md`, `rule-ask.md`, `rule-documentation.md`, `rule-decisions-schema.md` and `rule-vault-layout.md`. Over `.claude/` it printed `.claude/agents/librarian-guppi.md`, `.claude/agents/case-guppi.md` and `.claude/agents/ask-guppi.md`. Here is why each stands:
>   - The librarian is outside the rule, for the reason above.
>   - `rule-decisions-schema` governs the `schema.yaml` of the folder, and `rule-vault-layout` lists the folder. Neither speaks of a search.
> - A Grep of `decisions?/|Decision page` over `vault/wiki/estimates/` printed 16 files. Here is how they are placed:
>   - `estimate-ask-searches-at-prespec` enters the Case.
>   - `estimate-case-build-checks-the-finished-case` already promises that `case-guppi` searches the live pages with the Decision pages left out, so its Criterion stands.
>   - `estimate-documentation-completes` stands, because the librarian is outside the rule.
>   - `estimate-sprint-close-archives-the-decisions` is read by a script against the folder, as its Result records, and the file binds no script.
>   - The rest speak of the scripts that write, move, lint or rename Decision pages, not of an agent's search.
> - A Grep of `\.claude/rules` over `vault/wiki/`, with `!**/decisions/**`, printed `rule-page-read.md`, placed above.
> - A Grep of `every subagent|system prompt` over `vault/wiki/`, with `!**/decisions/**`, printed 8 files:
>   - `glossary.md`, `entity-glossary.md`, `rule-claude-md.md`, `rule-internal-context.md`, `rule-one-judgment-one-implementation.md`, `estimate-claude-md-rendered.md` and `estimate-one-judgment-one-implementation-followed.md` say that `CLAUDE.md` is the system prompt, which every session and every subagent loads. The How it works of `rule-claude-md` says the file holds what each agent needs and no more. These stay true. `CLAUDE.md` is still the system prompt and gains nothing. The new file is a second loaded text beside it, and `CLAUDE.md` does not claim to be the only one.
>   - `lesson-subagents-parallel-on-one-tree-red-mid-flight.md` speaks of tests run while subagents edit, not of what they load.
>
> Case 638 changes the confirmation paragraph of `rule-ask`, and this Case does not touch it. Case 639, built again in the same batch, lets the first answer of `ask-guppi` end its list of what was not checked with a line for each rule binding the agent that a search broke, the file of this Case included. This Case does not change `rule-ask`.
>
> Not done:
> - No hook refuses a Grep without the exclusion, and no `deny` permission locks the folder. If the next reading fails, those are the next step.
> - The frames of `ask-guppi`, `case-guppi` and the librarian are not changed.
> - The failed reading line of `estimate-ask-searches-at-prespec` is the main agent's, and this Case writes none.

> **problem:**
> A Grep of `ask-guppi` meant to leave out the Decision pages printed them, because the glob was written from the searched folder and the Grep tool reads it from the repository root. No text tells any agent which glob works, and the frame of each agent states the ban in its own words. The question is where one rule for the agents stands, which agents it binds, what it binds, and how it is checked.

> **recommend:**
> - **How the frame keeps Decision pages out of a search**
>   - Recommended: (a) name the glob that works: one sentence in `rule-ask` saying that a Grep or Glob over `vault/wiki/` or a wider folder leaves out Decision pages with `!**/decisions/**`, and that a glob written from the searched folder does not.
>   - Answer: (a). The person also asked whether this could be done through `.claude/rules/`, so that it holds for every agent, `case-guppi` included.
> - **Whether the frame of `case-guppi` gets the same sentence**
>   - Recommended: (b) both frames, one sub-case each.
>   - Answer: not answered; replaced by **Where the rule on Decision pages lives**.
> - **How the fix is checked**
>   - Recommended: (a) a new check on the new rule: at the `/hi` of a later session, the transcripts of the main agent, `ask-guppi`, `case-guppi` and the librarian are read to see that the file stands in each subagent's context and that no Grep or Glob over `vault/wiki/` or a wider folder printed a line of a Decision page. `estimate-ask-searches-at-prespec` keeps its check, and its method names the render by this Case.
>   - Answer: (a).
> - **Where the rule on Decision pages lives**
>   - Recommended: (b) one file in `.claude/rules/`, rendered from a new Rule page, loaded by every agent. The frames keep their own reasons for opening a Decision page.
>   - Answer: (b), to try it.
> - **What the file in `.claude/rules/` forbids**
>   - Recommended: (a) every search leaves them out: every Grep or Glob over `vault/wiki/` or a wider folder leaves out Decision pages with `!**/decisions/**`; a glob written from the searched folder does not; a Decision page is opened only by its path, where the agent's frame allows it; this binds the main agent too.
>   - Answer: (a).
> - **What the file says about Glob**
>   - Recommended: (a) the rule binds Grep, and Glob stays free: every Grep over `vault/wiki/` or a wider folder carries `!**/decisions/**`, alone or next to another filter; the text of a Decision page is read only by a Read of its path where the frame allows; a Glob may print a path of a Decision page; the new check looks at Grep and Read only.
>   - Answer: (a).
> - **Change**
>   - Asked: on the pre-spec findings that `rule-page-read` and `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction` doubt that a file of `.claude/rules/` loads in a subagent, the main agent asked where the rule lives: (a) in `CLAUDE.md`, or (b) `.claude/rules/` kept as a trial. It recommended (a). The person chose (b).
>   - Taken: the file stays under `.claude/rules/`. `given` names `rule-page-read` and the lesson. `context` says why the Case tries again: the first reading of the new Estimate shows whether the file loads in a subagent, and if not, a later Case moves the text to `CLAUDE.md`.
> - **Change**
>   - Asked: on the pre-spec finding that the rule clashes with the librarian's frame and `estimate-documentation-completes`, the main agent asked whether the rule binds the librarian: (a) the librarian is outside it, or (b) it is bound and its frame and that Estimate change. It recommended (a). The person chose (a).
>   - Taken: the file binds the main agent, `ask-guppi` and `case-guppi`, and says the librarian follows its own frame. The librarian leaves `when` and the new Estimate. The `－` line on the librarian's `git` command is replaced by one that leaves its calls out of the promise, and its frame and `estimate-documentation-completes` stand.

> **given:**
> `rule-search-leaves-out-decisions` and `.claude/rules/search-leaves-out-decisions.md`: the new rule and its render. It names the glob `!**/decisions/**` for a Grep over `vault/wiki/` and keeps out `vault/wiki/decisions/`.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the new check of that rule.
> **＋** `rule-harness` and `estimate-harness-pipeline`: the parent MOC, whose Purpose counts the rules in no pipeline, and the Estimate that lists them. The Criterion is unchanged.
> **＋** `estimate-ask-searches-at-prespec`: its `method` is set anew; its Criterion stands.
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md`, with `rule-case-build` and `.claude/agents/case-guppi.md`: the frames that name the reasons to open a Decision page. Unchanged.
> **＋** `rule-documentation`, `.claude/agents/librarian-guppi.md` and `estimate-documentation-completes`: the frame of the librarian and its check, outside the rule. Unchanged.
> **＋** `rule-page-read` and `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction`: they doubt that a file of `.claude/rules/` loads in a subagent. Unchanged.
> **＋** `rule-claude-md` and `entity-glossary`: they call `CLAUDE.md` the system prompt of every session and subagent. Unchanged.
> **＋** `vault/raw/2026-10-05/0109/cases/case-639.md`: it lets the first answer of `ask-guppi` name a search rule it broke.

> **when:**
> A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Grep, Glob or Read.

> **then:**
> `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
> **＋** Each Grep whose path is `vault/wiki/` or a folder that holds it carries `!**/decisions/**` in its glob, alone or after another filter, and prints no line of a page under `vault/wiki/decisions/`.
> **＋** The text of a Decision page reaches one of these agents only by a Read of its path, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi`, and for no reason in the main agent.
> **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
> **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

```then
create:
- slug: rule-search-leaves-out-decisions
  ref: rule-harness
  kind: Leaf
  purpose: Prevents the text of a Decision page from entering the context of the main agent, ask-guppi or case-guppi through a search of the vault
  enforcement: render
  governs: .claude/rules/search-leaves-out-decisions.md
  render_mode: full
  tags:
  - harness
  - workflow
  - session
  sections:
    Purpose: 'Prevents the text of a Decision page from entering the context of the main agent, `ask-guppi` or `case-guppi` through a search of the vault. A Decision page states a Case at its moment, and the folder holds a page per Case, so a search over the whole wiki that does not leave them out fills the context with them. The frames of `ask-guppi` and `case-guppi` forbid the search, but none named a glob that works, and the one an agent wrote did not: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from the folder it searches, so `!decisions/**` over `vault/wiki/` left nothing out (case 640). The librarian follows its own frame, which flags such a read rather than forbids it. The rule stands in one file under `.claude/rules/`, which Claude Code loads into context with no `paths:` to scope it. Whether such a file loads inside a subagent was not documented when [[rule-page-read]] weighed one ([[lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction]]); this rule tries it, its Estimate reads whether it loads, and if it does not, a later Case moves the text to `CLAUDE.md`.'
    Render: |-
      <!-- rule-search-leaves-out-decisions -->
      # The text of Decision pages stays out of every search

      This file binds the main agent, `ask-guppi` and `case-guppi` (case 640). The librarian follows `.claude/agents/librarian-guppi.md`, and this file does not bind it.

      - Every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, carries `!**/decisions/**` in its `glob`: alone, or after another filter with a space between them, as in `*.md !**/decisions/**`.
      - A glob written from the searched folder, such as `!decisions/**`, does not leave the folder out: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from its `path`.
      - The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, and only for a reason the frame of the agent names.
      - A Glob may print the path of a Decision page: a path is no text of the page.
      <!-- /rule-search-leaves-out-decisions -->
- slug: estimate-search-leaves-out-decisions-in-every-agent
  ref: rule-search-leaves-out-decisions
  kind: QA
  purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, each of their Greps over vault/wiki/ or a folder that holds it leaves out the Decision pages with !**/decisions/**, and the text of a Decision page reaches them only by a Read of its path for a reason their frame names
  method: 'by hand at the /hi of a later session: the transcripts of the main agent and of each ask-guppi and case-guppi of a session after the render of .claude/rules/search-leaves-out-decisions.md by case 640, whether the file stands in each context and each Grep, Glob and Read call, read against the Criterion, recorded in the estimate line'
  tags:
  - harness
  - workflow
  - session
update:
- slug: rule-harness
  replace:
  - old: 'Nine more belong here and run in no pipeline:'
    new: 'Ten more belong here and run in no pipeline:'
  - old: the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1).
    new: the hook that shows the size of the context, the hooks that read a page of the vault without its History, and the file under `.claude/rules/` that keeps the text of Decision pages out of a search (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1, 640).
  change: 'a tenth rule outside the pipeline: the file under .claude/rules/ that keeps Decision pages out of a search (case 640)'
- slug: estimate-ask-searches-at-prespec
  set:
    method: 'by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.2 and of .claude/rules/search-leaves-out-decisions.md by case 640, read in its agent transcript against the Criterion, recorded in the estimate line'
  change: the method names the render of .claude/rules/search-leaves-out-decisions.md by case 640; the Criterion stands
```

```tasks
- [ ] create `rule-search-leaves-out-decisions`
- [ ] create `estimate-search-leaves-out-decisions-in-every-agent`
- [ ] update `rule-harness`
- [ ] update `estimate-ask-searches-at-prespec`
- [ ] `uv run guppi render`: `.claude/rules/search-leaves-out-decisions.md`
- [ ] read `estimate-search-leaves-out-decisions-in-every-agent`
```

## Case 641 — The session's Estimate names a make target over the phases' tests

> **context:**
> `make lint` holds a rule for an Estimate of a MOC, a page that groups child pages. If the Estimate's `method` is a reading by hand and names no `make <target>`, every counted Estimate of the children must be a reading too. A sibling Estimate that names a target also clears the rule. Otherwise lint reports the Estimate (`check_method` in `guppi/lint.py`, cases 112.1, 212; the `method` field of `rule-estimates-schema`). The aim of the rule is that a reading by hand on the parent cannot hide the test pipelines of the children. `rule-session` is a MOC over the five phases. Its one Estimate, `estimate-session-phases-in-order`, is a reading by hand of the marks a finished session leaves, in time order. Case 637.4 set the method of `estimate-session-start-context`, an Estimate of the child `rule-session-start`, to `make test-session-start` alone. Since then that child is checked by tests only, and lint prints `estimates/estimate-session-phases-in-order: method: says by hand while estimate-session-start-context names a test file` (brief of 2026-10-04). The Estimates of the other children still pair a target with a reading by hand, or are readings. The Makefile has one pipeline per phase that has tests: `test-session-start`, `test-plan-mode`, `test-end-of-work` and `test-documentation`. Work Mode has none, and no target runs these four together. This Case adds a target `test-session` that runs the four, after the pattern of the per-MOC pipelines. It puts that target first in the method, before the same reading by hand. A `make <target>` the Makefile holds passes a MOC's Estimate whatever else the method says, so the finding clears. The rule of lint does not change. Its Estimate, `estimate-lint-checks-the-method`, already promises that such a target passes, so its Criterion stands. Only the `method` field of `estimate-session-phases-in-order` changes. Its Criterion speaks of the marks of a session and their order, not of how the check runs. So the Criterion and the status `passed` stand. The update carries no `set.status`.
>
> Two other Estimates make promises about every target of the Makefile, and both cover the new target (pre-spec findings on this Case). Both Criteria stand. `estimate-harness-make-runs-in-both-shells`, on `rule-harness`, promises that no recipe reads the stdin of its caller and no target writes to the working tree. `test-session` has no recipe of its own. It only names the four phase targets as prerequisites, and each of their recipes already closes stdin and only runs `pytest`. `estimate-tests-clock-pinned`, on `rule-tests-clock-pinned`, promises that the targets `test` and `test-*` run under the autouse fixture that pins the clock. `test-session` runs the same `pytest` calls as the four targets, so the fixture applies to them unchanged. The `then` keeps one line on each of these two promises for the new target. Neither Estimate is set `pending`.
>
> The page changes at the librarian's `generate`, so the `make lint` of that run shows the finding gone, and the brief reports it. Work Mode runs `make test-session` once to check the new target. Two searches over the repository, `vault/archive/`, `vault/raw/` and `vault/wiki/decisions/` excluded, back this. The first, Grep `estimate-session-phases-in-order`, printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-session.md`. The hit in `rule-session.md` is its `estimates` field, which stays true. The brief and the log are not read. The second, Grep `test-session`, printed `vault/wiki/brief.md`, `vault/wiki/estimates/estimate-session-start-context.md` and `Makefile`. Each hit names `test-session-start` only, so the name `test-session` is free. Cases 638, 639 and 640 of this session touch none of these pages, the Makefile, or the lint check.

> **problem:**
> The `method` of `estimate-session-phases-in-order` is a reading by hand alone. Now that `estimate-session-start-context` is checked by a test target only, `make lint` reports the MOC's Estimate on every run. Something must clear the finding without weakening the rule that stops a reading by hand on a MOC from hiding its children's pipelines.

> **recommend:**
> - **How should the finding on the session's Estimate be cleared?**
>   - Recommended: (a) a new `make test-session` target that runs the tests of each phase that has them, named first in the method of `estimate-session-phases-in-order` before the same reading by hand; the rule of lint, its tests and the promise of the Estimate do not change.
>   - Answer: agreed, (a).

> **given:**
> `estimate-session-phases-in-order` — the Estimate of the MOC whose `method` changes
> **＋** `Makefile` — gains the target `test-session`
> **＋** `rule-session` — the MOC over the five phases, whose children's pipelines the target runs
> **＋** `guppi/lint.py` — the judgment of a MOC's `method`, which constrains
> **＋** `rule-estimates-schema` — the form of the `method` field, which constrains
> **＋** `estimate-harness-make-runs-in-both-shells` — the promise on every recipe and target of the `Makefile`, which constrains
> **＋** `estimate-tests-clock-pinned` — the promise that the `test-*` targets run under the clock fixture, which constrains

> **when:**
> `uv run guppi lint` reads the `method` of `estimate-session-phases-in-order` against the `Makefile`.
> **＋** Someone runs `make test-session`.

> **then:**
> The `method` names `make test-session`, a target of the `Makefile`, and lint prints no `method` finding for `estimate-session-phases-in-order`.
> **＋** `make test-session` runs the pipelines `test-session-start`, `test-plan-mode`, `test-end-of-work` and `test-documentation`, and passes only when all of them pass.
> **＋** The tests that `make test-session` runs use the clock fixture that `estimate-tests-clock-pinned` promises for the `test-*` targets.
> **＋** The reading by hand of the marks of a session at its close stays in the `method` after the target, in the same words.
> **－** The Criterion and the status of `estimate-session-phases-in-order` do not change.
> **－** The judgment of `guppi/lint.py` on the `method` of a MOC's Estimate does not change.
> **－** `make test-session` reads no stdin of its caller and writes nothing to the working tree, as `estimate-harness-make-runs-in-both-shells` promises for every target.

```then
update:
- slug: estimate-session-phases-in-order
  set:
    method: make test-session, the pipeline over the tests of rule-session's children; then by hand at the close of a session — the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md, the librarian's commit, read in that order
  change: the method names make test-session before the reading by hand; the lint finding on a MOC's reading clears (case 641)
```

```tasks
- [x] `Makefile` — add `test-session` to `.PHONY` and a target `test-session: test-session-start test-plan-mode test-end-of-work test-documentation` with the help text `## the pipeline over rule-session's children`
- [ ] update `estimate-session-phases-in-order`
- [x] by hand in Work Mode: `make test-session` runs the four phase pipelines and passes
```

## Deferred

## Case 642 — the close of migration put off to a session of its own

```then
defer:
  - slug: entity-sprint-migration
    type: entity
    purpose: "The close of migration, a session of its own (case 628.9); put off by session 0109, whose Plan Mode holds Cases 638-641 that do not belong to the close"
```

## Case 643 — the check of the Spec as a whole put off

```then
defer:
  - slug: rule-prespec-judges-the-spec-whole
    type: rule
    purpose: "Prevents a Spec from being approved when its Cases together contradict each other or leave a question that no single Case owns, which the per-Case ask-guppi runs of case 634.1 do not judge; raised at the /pre-spec of session 0109"
```
