## Case 752 — case-guppi searches the code for a judgment a task would copy

> **context:**
> `CLAUDE.md` holds `rule-one-judgment-one-implementation`: where code judges the same text in two places, the pattern or the predicate lives in one module and both sides import it. `case-guppi` reads that file like every agent, but its own instructions, rendered from `rule-case-build`, never tell it to search the code before it writes a task that adds such a judgment. The first check is the vault search of `ask-guppi` at `/pre-spec`, after the Case is ratified. In session 0200 of 2026-10-09, Case 748.1 had materialize fill the type of a page by a map of its own, while `SINGULAR` of `guppi/generate.py` already held that map and `guppi/prespec.py` imported it; the pre-spec run found the second copy and the Case was built again (`lesson-case-build-task-copies-an-existing-judgment`). The lesson joined `insight-workflow-case-written-without-reading-the-pages-it-changes`, which the synthesis opened again from `actioned` for this lesson alone. The person chose a step in the instructions of `case-guppi`, a search over `guppi/` judged by what the code does, a new Estimate of its own, and the group of lessons marked handled by this Case. The new sentence stands in the paragraph of `rule-case-build` on the frame, after the sentence on the tests that read a live file (case 736.1). The sentence of that page on reading a module of code in parts, by its functions and the places that call them, stands: the new search reads each hit around its line, which is a read in parts. For the same reason `estimate-case-build-reads-by-need-and-in-parts` stands: its Criterion has a module of code read in parts, by a Grep with lines of context or a Read with `offset` and `limit`, and the hits of the new search are read that way, in a module the Case changes or not. Its Criterion forbids no read of another module, and the search of the finished Case for a slug in the code already reads hits around their lines in modules the Case may not change. The Purpose of `rule-case-build` stands, since it already says that the agent builds the Case against its frame. The sentence that `context` names a search only when the Case rests on it stands too: the claim that a task adds no second copy rests on the new search. `estimate-one-judgment-one-implementation-followed` stands: its Criterion speaks of the code the agent writes and says that no script refuses a second copy, which stays true, since the new step is a reading by `case-guppi` and no script. `estimate-case-build-checks-the-finished-case` stands, since its Criterion speaks of the check of the finished Case and not of the frame before a task is written. A Glob `vault/**/estimate-case-build-finds-an-existing-judgment.md` printed nothing, so the slug is free.

> **problem:**
> A task of a Case can add a second copy of a judgment the code already holds, and nothing catches it before `/pre-spec`, after the person has ratified the Case.

> **recommend:**
> - **Where does the step that catches a second copy stand?**
>   - Recommended: (a) a step in the instructions of `case-guppi`: before a task adds code that judges a text, it searches the code for an existing implementation, and the task imports it or moves it into one module.
>   - Answer: agreed, (a).
> - **How wide is the search for an existing copy?**
>   - Recommended: (a) the code under `guppi/`, judged by what it does, with a test over both sides where they cannot share the code.
>   - Answer: agreed, (a).
> - **How is the new step checked?**
>   - Recommended: (a) a new Estimate of its own, read by hand at the Retro of this session against the new Render in the Spec.
>   - Answer: agreed, (a).
> - **What happens to the lesson cluster this lesson belongs to?**
>   - Recommended: (a) the Case sets the group to `actioned`, with this Case as the fix.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render is the instructions of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-finds-an-existing-judgment`: the new check of the search.
> **＋** `rule-one-judgment-one-implementation`: the rule in `CLAUDE.md` that the task keeps.
> **＋** `guppi/`: the code the search runs over.
> **＋** `insight-workflow-case-written-without-reading-the-pages-it-changes`: the group of lessons this Case actions.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds code under `guppi/` that judges a text — a pattern, a map or a predicate.

> **then:**
> Before it writes the task, `case-guppi` searches `guppi/` for the words of what the code judges, such as the field, the category or the form of the line, and reads each hit around its line.
> **＋** Where code under `guppi/` already makes that judgment, the task imports it, or moves it into one module that both sides import, as `rule-one-judgment-one-implementation` sets it.
> **＋** Where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike.
> **＋** The `context` of the Case names that search, its pattern, its paths and what it printed.
> **－** A Case whose tasks add no code that judges a text takes no such search.
> **－** `insight-workflow-case-written-without-reading-the-pages-it-changes` stands `actioned` with `addressed_by: decision-case-752` and leaves the backlog.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1). ``
>   - new: `` each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1). When a task of the Case adds code that judges a text — a pattern, a map or a predicate — Grep `guppi/` before you write the task for the words of what it judges, such as the field, the category or the form of the line, and read each hit around its line; where code there already makes that judgment, the task imports it, or moves it into one module that both sides import, and where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike, as `rule-one-judgment-one-implementation` sets it; `context` names that search, since the claim that the task adds no second copy rests on it (case 752). ``
>   - change: `case-guppi searches guppi/ for an existing implementation of a judgment before a task adds one (case 752)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-finds-an-existing-judgment`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi searches guppi/ for an existing implementation of a judgment before a task of its Case adds code that judges a text, and the task imports it or moves it into one module`
>   - method: `by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, and the findings of ask-guppi at the /pre-spec of this session read for a task of a Case built by case-guppi that adds a second copy of a judgment, the count in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] update `insight-workflow-case-written-without-reading-the-pages-it-changes`
>   - set: `{status: actioned, addressed_by: decision-case-752}`
>   - change: `actioned: case-guppi searches guppi/ for an existing implementation of a judgment before a task adds one (case 752)`
> - [ ] read `estimate-case-build-finds-an-existing-judgment`

> **ratification:**
> ```
> - decision[case 752][update][rule-case-build]{ref:rule-case-build}
> - decision[case 752][create][estimate-case-build-finds-an-existing-judgment]{ref:rule-case-build}{tags:session,workflow,harness}
> - decision[case 752][update][insight-workflow-case-written-without-reading-the-pages-it-changes]{ref:insight-workflow-case-written-without-reading-the-pages-it-changes}
> ```
