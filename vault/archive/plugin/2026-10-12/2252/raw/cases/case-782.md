## Case 782 — Pre-spec asks whether a Criterion needs a later session

> **context:**
> `/pre-spec` checks a plan in two ways. Code judges the `method` of an Estimate and reports one that waits for a later session, the librarian or `/hi`, unless a part of it waits for an event it names (cases 670.4, 781). One `ask-guppi` run at the first `/pre-spec` of a session answers open questions over the plan. Nothing asks the same of the `When` and `Then` of a Criterion. In session 1449 the `When` that Case 777 gave `estimate-sprint-close-next-session-opens-the-sprint` asked someone to read the Frontier, the ledger and the pages of the session after the close, while its method ran tests and read skill texts. The `ask-guppi` run caught it only through its question on contradictions, and the Case was built again as Case 779. Cases 780 and 781 left a check of this out. The person chose a judgment over a word list, since a word list cannot tell a Criterion that describes a later session from one that needs to observe it: the fixed `When` of Case 779 still names the librarian's run and the session that closes a sprint. So the `/pre-spec` skill, the Render of `rule-prespec`, asks `ask-guppi` one more question. The `ask-guppi` agent file, the Render of `rule-ask`, stops listing the questions and answers each question the skill sets, in its order, so the list stands in one place. Case 782.1 replaces the Criterion of `estimate-prespec-reconciles`, whose `method` reads the new Renders of both rules at the Retro of the session that changes them and stands. Case 782.2 replaces the Criterion of `estimate-ask-finds` and sets its `method` anew as a reading that waits for an event, since its old one waits for a `/hi` of a later session and `/pre-spec` reports a kept method of that kind. A Case built again after the first `/pre-spec` is not asked the new question: the person chose to keep this Case to `/pre-spec`, and `case-guppi` already judges each option for a reported defect against the rule it breaks (case 780). No code changes, and no `create` stands, so no vault query was run.
>
> In `rule-prespec` the sentence of the questions changes; the sentence on what the run reads already names the `when` and `then` of each Case, and the sentence that a later run dispatches no `ask-guppi` stays true. In `rule-ask` the sentence that lists the questions changes; the paragraph on the confirmation of findings and the line on what the agent did not check stay true. A Grep for `bear out|does not bear|speaks of the thing` over the repository with the glob `!vault/{archive,raw}/**` printed `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/rules/rule-prespec.md`, `vault/wiki/rules/rule-ask.md`, `vault/wiki/estimates/estimate-prespec-reconciles.md` and `vault/wiki/estimates/estimate-ask-finds.md`. The two `.claude/` files of the skill and the agent follow their rules by the render. In `rule-case-build` and its Render `case-guppi.md` the words define what a contradiction is for `case-guppi`, not a question of `/pre-spec`, so they stand. No other Estimate of `rule-prespec` or `rule-ask` lists the questions; `estimate-ask-searches-at-prespec` names only the questions of the skill file, which stays true. In both replaced Criteria the line that listed the questions is rewritten, so the check notes it as not carried. The check also notes `then` lines of the two sub-cases that share most of their words; they stand, since one side sets what the main agent dispatches and reports and the other what `ask-guppi` answers. A Grep for `skills/pre-spec|skills" / "pre-spec|ask-guppi\.md|"ask-guppi"|rule-prespec\.md|rule-ask\.md|estimate-prespec-reconciles|estimate-ask-finds` over `tests/` printed `tests/test_casecheck.py`, whose hit passes the agent name `ask-guppi` with a made-up answer and reads none of these files, so no test reads a file this Case changes.

> **problem:**
> A Criterion whose `When` or `Then` needs a reading that only a later session can take passes `/pre-spec` unless the `ask-guppi` run happens to see it as a contradiction, since nothing asks about it by name.

> **recommend:**
> - **What form, if any, should a check on the `When` and `Then` take?**
>   - Recommended: (c) a fourth question for the `ask-guppi` run, a judgment of meaning, since a word list cannot tell describing a later session from needing to observe one.
>   - Answer: (c).
> - **How does the `ask-guppi` side learn about the fourth question?**
>   - Recommended: (b) name the questions only in the skill; `rule-ask` and `estimate-ask-finds` say the agent answers each question the skill sets, in its order.
>   - Answer: agreed, (b).
> - **How is the rewritten `estimate-ask-finds` read?**
>   - Recommended: (a) wait for a named event: a `/pre-spec` run after the render, its answer read in the agent transcript.
>   - Answer: agreed, (a).
> - **Does the builder of a Case also judge this, for Cases built again after the first `/pre-spec`?**
>   - Recommended: (a) no, the Case covers `/pre-spec` only.
>   - Answer: agreed, (a).

### Case 782.1 — The skill asks whether a Criterion needs a later session

> **given:**
> `rule-prespec`: the rule rendered into `.claude/skills/pre-spec/SKILL.md`, which sets the questions of the `ask-guppi` run.
> **＋** `estimate-prespec-reconciles`: its Criterion is replaced whole.
> **＋** `rule-ask`: the rule rendered into `.claude/agents/ask-guppi.md`, which the run follows.
> **＋** `rule-case-protocol`: sets in `vault/wiki/case-schema.md` what a `method` holds, a part that waits for an event it names, and the Estimate of a sprint page `entity-sprint-<id>`.
> **＋** `rule-spec-write`: the hook that writes a Case built again into the plan.
> **＋** `rule-skill-hi` and `/hi`: set the title line of the plan that names a conserved Spec; a `/hi` is one of the moments the new question names.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose findings the agent fixes itself.
> **＋** `estimate-prespec-notes-a-page-another-case-defers`: the check of the note on a page another Case defers.

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then` and `then` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** The questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out; and whether the `When` or `Then` of a Criterion a Case sets asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session.
> **＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** The last question finds nothing where a part of the `method` waits for an event it names that brings that reading, nor in the Criterion of an Estimate whose target is a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint.
> **－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read, and `ask-guppi` is not asked whether a Case changes a page that another Case of the plan defers: `uv run guppi prespec --check` notes such a pair at every run, as `estimate-prespec-notes-a-page-another-case-defers` sets it.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `Three questions: which of these contradict`
>   - new: `The questions: which of these contradict`
>   - old: `` the vault does not bear out (case 388). A later run in the session dispatches no `ask-guppi` ``
>   - new: `` the vault does not bear out (case 388); and whether the `When` or `Then` of a Criterion a Case sets — its `when` and `then`, or the Criterion its item writes — asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session; a part of the `method` that waits for an event it names and brings that reading, and the Estimate of a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint, are no such finding, as `case-schema.md` sets it (case 782). A later run in the session dispatches no `ask-guppi` ``
>   - change: `the ask-guppi run at pre-spec is also asked whether the When or Then of a Criterion needs a reading only a later session can take (case 782)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] update `estimate-prespec-reconciles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — ask-guppi is also asked whether the When or Then of a Criterion needs a reading only a later session can take`
> - [ ] read `estimate-prespec-reconciles`

> **ratification:**
> ```
> - decision[case 782.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 782.1][update][estimate-prespec-reconciles]{ref:rule-prespec}
> ```

### Case 782.2 — Ask-guppi answers each question the skill sets

> **given:**
> `rule-ask`: the rule rendered into `.claude/agents/ask-guppi.md`, whose answer at `/pre-spec` changes.
> **＋** `estimate-ask-finds`: its Criterion is replaced whole and its `method` set anew.
> **＋** `rule-prespec`: the rule rendered into `.claude/skills/pre-spec/SKILL.md`, which sets the questions.
> **＋** `rule-case-protocol`: sets in `vault/wiki/case-schema.md` a `method` that waits for an event it names.
> **＋** `vault/raw/<date>/event_log.md`: the event log that records the dispatch.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the search rule whose breaks the answer names.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question that `.claude/skills/pre-spec/SKILL.md` sets, in the order of that file.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** `.claude/agents/ask-guppi.md` does not list the questions of `/pre-spec` itself.
> **－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `` and asks which Case of the plan contradicts a page of the vault, a rule of the vault or another Case, which Estimate a Case does not name speaks of the thing the Case changes, and which fact of a `context` the vault does not bear out, answer instead with one numbered list of findings under each question, in that order: ``
>   - new: `` and asks the questions that `.claude/skills/pre-spec/SKILL.md` sets, answer instead with one numbered list of findings under each question, in the order of that file (case 782): ``
>   - change: `at pre-spec ask-guppi answers each question the skill sets, in its order, and the agent file lists them no more (case 782)`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] update `estimate-ask-finds`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md as rendered by case 782: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — one list of findings under each question the skill sets, in its order; the method waits for a /pre-spec after the render`
> - [ ] read `estimate-ask-finds`

> **ratification:**
> ```
> - decision[case 782.2][update][rule-ask]{ref:rule-ask}
> - decision[case 782.2][update][estimate-ask-finds]{ref:rule-ask}
> ```
