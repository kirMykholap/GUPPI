## Case 785 — case-guppi reads the function each side calls before it names a shared judgment

> **context:**
> When a task of a Case adds code that judges a text, such as whether a page exists, `case-guppi` searches `guppi/` for code that already makes that judgment and has the task import it (case 752). It does not read the function that the other side of the pipeline calls today for the same judgment, so it can name a function as shared when it answers differently. In session 2252 Case 783 had `/pre-spec` reuse the page test of `guppi/materialize.py` for a defer that `guppi generate` judges by its own lookup in `guppi/generate.py`. The two answered differently for an Estimate archived outside a folder `estimates/`. The `ask-guppi` run at `/pre-spec` found it, and the Case was built again around a new shared `has_page` (handoff of session 2252; `lesson-case-build-reused-judgment-not-checked-against-the-other-side`). Case 784 added a search for changed field names, not a check of a shared judgment in code (handoff of session 2252, For the next session).
>
> The person chose four things. A new sentence in the Render of `rule-case-build` has `case-guppi` read whole the function each side calls and judge whether they answer alike, and no script or `/pre-spec` question is added. Where the functions part, `case-guppi` asks the person in a round which answer both sides share. Where they parted, the task adds one test over that input. The Criterion of `estimate-case-build-finds-an-existing-judgment` is replaced whole, and no new Estimate is created. The new sentence stands right after the sentence of case 752 in the Render. Its `purpose` and `method` state the old promise, so the same `update` sets them anew. The old Criterion's last `－` line on `insight-workflow-case-written-without-reading-the-pages-it-changes` was the bookkeeping of case 752 and is not carried.
>
> In `rule-case-build`, read whole, the sentence of case 752 is the one sentence on this behaviour. It stays true, because the new sentence adds a step before the import. The sentence that `case-guppi` decides nothing the person has not decided agrees with the round the new sentence asks for. The text of `rule-one-judgment-one-implementation` asks for a test only where the two sides cannot share code. The new test, where the old functions parted, adds to that rule and makes no sentence of it false. The Criterion of `estimate-one-judgment-one-implementation-followed` speaks of the code of a session, not of how `case-guppi` builds a Case, so it stands. The other Estimates of `rule-case-build` speak of other steps of the build, so they stand. A Grep for `existing judgment|already makes that judgment|second copy of a judgment` over `vault/wiki/` and `.claude/` printed `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-finds-an-existing-judgment.md`, all three changed by this Case. A Grep for `case-guppi\.md|rule-case-build` over `tests/` printed no match, so no test reads the changed files. The Case changes no code and adds no hook. It takes no `{addresses:...}` mark, because the lesson stands in the ledger of another session (case 284.2).

> **problem:**
> `case-guppi` can name an existing function as the judgment that both sides share without reading the function the other side calls, so the two sides may still answer differently.

> **recommend:**
> - **Where should the fix go?**
>   - Recommended: (a) a new sentence in the instructions of `case-guppi` only: it reads the function each side calls and judges whether they answer alike, and `context` names both and what it found.
>   - Answer: agreed, (a).
> - **What should `case-guppi` do when the two functions answer differently?**
>   - Recommended: (a) ask the person which answer is right: name neither function as shared, and show in a round the input where they part and what each answers there.
>   - Answer: agreed, (a).
> - **Should a test prove that both sides agree?**
>   - Recommended: (a) a test over the input where they parted, which runs both sides and asserts they answer alike.
>   - Answer: agreed, (a).
> - **Which check confirms the fix?**
>   - Recommended: (a) rewrite the Criterion of `estimate-case-build-finds-an-existing-judgment` whole, its purpose with it.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render gains the sentence on the function each side calls.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-finds-an-existing-judgment`: its Criterion, `purpose` and `method` are set anew.
> **＋** `guppi/`: the code that `case-guppi` searches and reads.
> **＋** `rule-one-judgment-one-implementation`: the rule that a judgment lives in one module.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds code under `guppi/` that judges a text — a pattern, a map or a predicate.

> **then:**
> Before it writes the task, `case-guppi` searches `guppi/` for the words of what the code judges, such as the field, the category or the form of the line, and reads each hit around its line.
> **＋** Where code under `guppi/` already makes that judgment, the task imports it, or moves it into one module that both sides import, as `rule-one-judgment-one-implementation` sets it.
> **＋** Where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike.
> **＋** Before it names a function as the judgment both sides share, `case-guppi` reads whole the function each side calls today for that judgment, the side the Case does not change included, and judges whether they answer alike on each input where they could part.
> **＋** Where they part, `case-guppi` names neither as the shared judgment and asks the person in a round which answer both sides share, with the input and what each answers there.
> **＋** Where they parted, the task adds one test that runs both sides over that input and asserts they answer alike.
> **＋** The `context` of the Case names that search, its pattern, its paths and what it printed.
> **＋** The `context` of the Case names each function it read for the judgment both sides share, and what it found.
> **－** A Case whose tasks add no code that judges a text takes no such search.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` where code there already makes that judgment, the task imports it, or moves it into one module that both sides import, and where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike, as `rule-one-judgment-one-implementation` sets it; `context` names that search, since the claim that the task adds no second copy rests on it (case 752). ``
>   - new: `` where code there already makes that judgment, the task imports it, or moves it into one module that both sides import, and where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike, as `rule-one-judgment-one-implementation` sets it; `context` names that search, since the claim that the task adds no second copy rests on it (case 752). Before you name a function as the judgment both sides share, find the function each side calls today for that judgment, the side your Case does not change included, read each one whole, and judge whether they answer alike on each input where they could part, such as a page in a folder of another category or a line in an older form; `context` names each function and what you found. Where they part, name neither as the shared judgment: ask in a round which answer both sides share, with the input where they part and what each answers there; and the task adds one test that runs both sides over that input and asserts they answer alike (case 785). ``
>   - change: `case-guppi reads whole the function each side calls before it names a shared judgment, asks the person where they part, and has a test run both sides over that input (case 785)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-finds-an-existing-judgment`
>   - set:
>     ```
>     status: pending
>     purpose: Whether case-guppi searches guppi/ for an existing implementation of a judgment before a task of its Case adds code that judges a text, reads whole the function each side calls for it, asks the person where they answer differently, and the task imports one judgment and tests both sides where they parted
>     method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, and the findings of ask-guppi at the /pre-spec of this session read for a task of a Case built by case-guppi that adds a second copy of a judgment or names as shared a function that answers differently from the one the other side calls, the count in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — case-guppi reads the function each side calls before it names a shared judgment, asks the person where they part, and a test runs both sides over that input (case 785)`
> - [ ] read `estimate-case-build-finds-an-existing-judgment`

> **ratification:**
> ```
> - decision[case 785][update][rule-case-build]{ref:rule-case-build}
> - decision[case 785][update][estimate-case-build-finds-an-existing-judgment]{ref:rule-case-build}
> ```
