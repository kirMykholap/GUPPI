## Case 798 — case-guppi reads the governing rule and the last output of a check before it recommends an option

> **context:**
> `case-guppi` reads the rule that a text breaks, and judges each option of its round against it, only when the item reports a defect (case 780). On any other item, nothing tells it to read the rule that governs what an option changes, or what a check printed at its last run. Case 787 shows where this goes wrong. It was a new feature, so the defect-only sentence did not apply. The agent recommended `style`, `test` and `lint` as required checks on `main` and read neither the lint lines of the Baseline nor `rule-lint`, whose Purpose calls red a signal, not a gate. Lint was red on GitHub, no outside pull request could merge, and Case 794 replaced 787.1. `lesson-case-build-made-an-always-red-check-required` records this. With `lesson-case-build-recommended-a-trigger-that-keeps-the-defect`, it is `clustered` under `insight-case-build-recommends-without-reading-the-governing-rule`, which stands `open` in `backlog.md`.
>
> By the person's answers, Case 798.1 widens the case 780 sentence in the Render of `rule-case-build` from defect items to every item, and adds that `context` names the rule. It also replaces the Criterion and the `purpose` of `estimate-case-build-judges-options-against-the-broken-rule`. That Estimate is `passed` and its Criterion covers only an item that reports a defect. The new Criterion does not carry three lines of the old one: its `When` on an item that reports a defect, its first `Then` line on the rule the defect breaks, and its line on an option that leaves a part of the text breaking the rule. Each is replaced by a wider line that covers every item and still names the defect case, so no part of the old promise is lost. Its `method`, a reading of the new Render in the Spec at the Retro of the session, states no promise and stands. Case 798.2 adds a sentence: where an option rests on whether a check passes, `case-guppi` reads what that check printed at its last run, as the brief reports it. The new Estimate `estimate-case-build-reads-the-last-output-of-a-check` checks this. Plan Mode cannot run `make lint`. The librarian writes its last lines under `## Flags` of `vault/wiki/brief.md` and the counts of `make test` and `make lint` under `## Readings at the close`, as `rule-brief` sets. Case 798.1 sets the insight `actioned`, since the two sentences together change the step that both lessons blame. The Criteria do not state the insight, because Case 797.2 had to remove such a stale line from another Estimate of `rule-case-build`.
>
> The frame. In the Render of `rule-case-build`, the one sentence that states this behaviour is the case 780 sentence. Other sentences speak of contradictions in pages and of what done means. The change leaves them true. The Criteria of the other Estimates of `rule-case-build` speak of other behaviours, so they stand. Case 797.1 of this session adds one sentence to the frame paragraph of the same Render, and this Case changes the next paragraph. No pair of the two Cases shares a sentence. The two sentences part where another Case of the session changes the check or the pages it reads. The last output in the brief is the state at the librarian's last run. Case 797.1 judges by the state when the check runs. This session holds such Cases: Case 795.1 clears the `orphan` line of `rule-github-repository` from `make lint`, and Case 799 drops the `unread: pending` line of an Estimate whose `method` waits for a later moment. So the new sentence of Case 798.2 says that, where another Case of the session changes the check or the pages it reads, the sentence of Case 797.1 holds (pre-spec finding). Under `rule-raw-archive`, the librarian moves an applied session whole into `vault/archive/`, and the Render of `rule-case-build` opens `vault/archive/` by slug only. A handoff has no slug, so the handoff of the last session is often out of reach. The person chose the brief alone as the source of the last output. A Grep `reports a defect|rule the defect breaks|governing rule` over `vault/wiki/` and `.claude/` printed `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-judges-options-against-the-broken-rule.md`. This Case changes all three. A Grep `estimate-case-build-judges-options-against-the-broken-rule|insight-case-build-recommends-without-reading-the-governing-rule` over the repository outside `vault/raw/` and `vault/archive/` printed six files. `vault/wiki/brief.md` and `vault/wiki/log.md` were not read. `uv run guppi backlog` writes `vault/wiki/backlog.md` again from the open Insights at the librarian's run. The `estimates` list of `vault/wiki/rules/rule-case-build.md` stands. The `insight` field of the two lessons stands until the cascade of `generate` archives them. A Grep `case-guppi\.md|rule-case-build|judges-options-against-the-broken-rule` over `tests/` printed nothing, so no test reads the agent file or the pages live. The new Estimate has a `ref`, so no vault query was run. A Glob `vault/**/estimate-case-build-reads-the-last-output*` printed nothing, so the slug is free.

> **problem:**
> `case-guppi` can recommend an option that breaks the rule governing what the option changes, or that rests on a check that is red today. It reads the governing rule only on an item that reports a defect, and it never reads the last output of a check. A Case built on such a recommendation has to be replaced.

> **recommend:**
> - **What must `case-guppi` read before it recommends an option?**
>   - Recommended: (b) on every item, the rule that governs what each option changes, and, where an option rests on whether a check passes, what that check printed at its last run, as the brief reports it; `context` names both.
>   - Answer: agreed, (b).
> - **What happens to the group page of the two lessons?**
>   - Recommended: (a) this Case sets the group page `actioned`.
>   - Answer: agreed, (a).
> - **How is the new instruction checked?**
>   - Recommended: (a) two parts: widen the Criterion of the existing check to every item, and add a new check for the last output of a check.
>   - Answer: agreed, (a).
> - **When is each check read?**
>   - Recommended: (a) at this session's Retro, on the new instruction text.
>   - Answer: agreed, (a).
> - **What if the brief shows no output for the check an option rests on?**
>   - Recommended: (a) look in the brief and the handoff of the last session; where neither shows it, the `**After:**` line of the option and `context` say so, and the option may still be recommended.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by a finding of `/pre-spec`, the person agreed that `case-guppi` reads the last output of a check only in the brief, the `make lint` lines under `## Flags` and `make test` under `## Readings at the close`, since the handoff of the last session is usually moved to the archive; where the brief shows none, the option and `context` say so.
>   - Taken: Case 798.2 drops the handoff from its sentence, `given`, `then` and the `purpose` of its Estimate.
> - **Change**
>   - Asked: by a finding of `/pre-spec`, the sentence of Case 798.2 must not contradict the sentence of Case 797.1 where another Case of the session changes the check or the pages it reads.
>   - Taken: the sentence and the `then` of Case 798.2 say that, in that case, the option is judged by the state at the moment the check runs, as Case 797.1 sets it; `context` no longer claims that the last output is that state.

### Case 798.1 — case-guppi reads the governing rule on every item

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, widens the sentence on the rule a defect breaks.
> **＋** `estimate-case-build-judges-options-against-the-broken-rule`: its Criterion and `purpose` are replaced.
> **＋** `insight-case-build-recommends-without-reading-the-governing-rule`: set `actioned`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of the `**After:**` line of an option.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case on a Frontier item and writes a round with options.

> **then:**
> Before it recommends an option, it finds the rule that governs what each option changes, or the rule the defect breaks where the item reports a defect, and reads the passage of that rule, which it names in the `context`.
> **＋** It judges each option of the round against that rule over the whole text the option leaves; for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes.
> **＋** An option that breaks that rule, or leaves a part of that text breaking it, may stand in the round; its `**After:**` line names that part, and `case-guppi` does not recommend that option.
> **－** The `**After:**` line keeps the form of `.claude/skills/grill-me/SKILL.md`: the part left is a plain sentence inside its text.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` When the item reports a defect — a text that breaks a rule — find the rule it breaks and read its passage, and judge each option of your round against that rule over the whole text the option leaves: for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes; an option that leaves a part of that text breaking the rule may stand, its `**After:**` line names that part in a plain sentence, and you do not recommend it (case 780). ``
>   - new: `` On every item, before you recommend an option, find the rule that governs what each option changes — where the item reports a defect, a text that breaks a rule, the rule it breaks — and read its passage, and judge each option of your round against that rule over the whole text the option leaves: for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes; an option that breaks the rule, or leaves a part of that text breaking it, may stand, its `**After:**` line names that part in a plain sentence, and you do not recommend it; `context` names the rule (cases 780, 798.1). ``
>   - change: `case-guppi reads the rule that governs what each option changes on every item, not only on an item that reports a defect, and context names it (case 798.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-judges-options-against-the-broken-rule`
>   - set:
>     ```
>     status: pending
>     purpose: Whether case-guppi, on every item, finds the rule that governs what each option of its round changes, the rule a defect breaks where the item reports one, judges each option against it over the whole text the option leaves, names in the After line of an option the part it leaves breaking the rule without recommending it, and names that rule in context
>     ```
>   - change: `the Criterion and purpose replaced whole — the rule that governs what an option changes is read on every item, not only on an item that reports a defect (case 798.1)`
> - [ ] update `insight-case-build-recommends-without-reading-the-governing-rule`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-798.1
>     ```
>   - change: `actioned: case-guppi reads the rule that governs what each option changes on every item, and the last output of a check an option rests on (cases 798.1, 798.2)`
> - [ ] read `estimate-case-build-judges-options-against-the-broken-rule`

> **ratification:**
> ```
> - decision[case 798.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 798.1][update][estimate-case-build-judges-options-against-the-broken-rule]{ref:rule-case-build}
> - decision[case 798.1][update][insight-case-build-recommends-without-reading-the-governing-rule]{ref:insight-case-build-recommends-without-reading-the-governing-rule}
> ```

### Case 798.2 — case-guppi reads the last output of a check an option rests on

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence on the last output of a check.
> **＋** `estimate-case-build-reads-the-last-output-of-a-check`: the new check of the sentence.
> **＋** `vault/wiki/brief.md`: its `## Flags` and `## Readings at the close` hold the last output of `make lint` and `make test`.
> **＋** `rule-brief`: the rule that writes those sections at the librarian's run.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of the `**After:**` line of an option.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub.

> **then:**
> Before it recommends that option, it reads what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, judges the option against that output, and quotes it with its source in the `context`.
> **＋** Where another Case of the same session changes that check or the pages it reads, it judges the option by the state at the moment the check runs, as `rule-case-build` sets it for such a Case, and not by the last output alone.
> **＋** Where the brief does not report that output, the `**After:**` line of the option and the `context` say that its last output was not read.
> **－** An option whose last output was not read may still be recommended.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `Each Case and sub-case answers what done means and how it is checked:`
>   - new: `` Where an option rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub, read before you recommend it what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, and judge the option against that output; where another Case of the session changes that check or the pages it reads, judge the option by the state at the moment the check runs, as the paragraph on the frame sets it (case 797.1); `context` names that output, and where the brief does not report it, the `**After:**` line of the option and `context` say that its last output was not read, and the option may still be recommended (case 798.2). Each Case and sub-case answers what done means and how it is checked: ``
>   - change: `case-guppi reads what a check printed at its last run, from the brief, before it recommends an option that rests on that check (case 798.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-the-last-output-of-a-check`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, before it recommends an option that rests on whether a check passes, reads what that check printed at its last run, from the brief, judges the option against it, or by the state at the moment the check runs where another Case of the session changes the check or the pages it reads, and names it in context, or says in the After line and context that the output was not read`
>   - method: `by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] read `estimate-case-build-reads-the-last-output-of-a-check`

> **ratification:**
> ```
> - decision[case 798.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 798.2][create][estimate-case-build-reads-the-last-output-of-a-check]{ref:rule-case-build}{tags:session,workflow,harness}
> ```
