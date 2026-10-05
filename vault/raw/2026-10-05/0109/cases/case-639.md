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

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `and a question with no finding says "none" (case 626.1).`
>   - new: `and a question with no finding says "none" (case 626.1). Under a question stand only its numbered findings, or "none" alone: no sentence on what you checked and found sound, a clash with another Case you did not find included (case 639).`
>   - old: `"none" when you checked all of it, and then the list of the paths of the files you read;`
>   - new: `` "none" when you checked all of it and your searches broke no rule of this file or of `.claude/rules/search-leaves-out-decisions.md`; its last lines name each rule of those files that a search of yours broke, one line each, and say whether a finding rests on what that search printed (case 639); and then the list of the paths of the files you read; ``
>   - change: `under a question of the first answer at /pre-spec stand only its findings or "none", no sentence on what holds; the list of what was not checked ends with a line per search rule broken, of the frame or of .claude/rules/search-leaves-out-decisions.md (case 639)`
> - [ ] update `estimate-ask-finds`
>   - set:
>     ```
>     status: pending
>     purpose: 'Whether ask-guppi answers the questions of /pre-spec with one line on what it read, one numbered list of findings under each question and nothing else under it, each finding naming its Case and the page or Cases it bears on, then a list of what it did not check ending with a line per search rule it broke, of its frame or of .claude/rules/search-leaves-out-decisions.md, and a list of the paths of the files it read, and nothing else'
>     method: 'by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 639, read in its agent transcript against the event log, recorded in the estimate line'
>     ```
>   - change: `the Criterion replaced whole — only findings or "none" under a question, no sentence on a clash not found; the list of what was not checked ends with a line per search rule broken, of the frame or of .claude/rules/search-leaves-out-decisions.md (case 639)`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-ask-finds`

> **ratification:**
> ```
> - decision[case 639][update][rule-ask]{ref:rule-ask}
> - decision[case 639][update][estimate-ask-finds]{ref:rule-ask}
> ```
