## Case 780 — Each option is judged against the rule the defect breaks

> **context:**
> When an item reports a defect, `case-guppi` builds the options of its round from the item's own words. It does not look up the rule the defect breaks, so an option can fix the quoted words and leave the same defect in the rest of the text. In session 1449, Case 777 dropped only the transcript words from the `When` of `estimate-sprint-close-next-session-opens-the-sprint`, as `case-guppi` recommended. `/pre-spec` then found that the rest of that line still named readings of a later session, which the method cannot take since a method holds only what runs in the Case's own session (case 670.4). The Case was built again as Case 779. `lesson-case-build-recommended-a-trigger-that-keeps-the-defect`, line 10 of that session's ledger, records this cause. The person chose a sentence in the Render of `rule-case-build`, in the paragraph on forks: when an item reports a defect, `case-guppi` finds the rule it breaks and judges each option of its round against that rule over the whole text the option leaves. An option that fixes only part of the defect may still stand, but its `**After:**` line names the part left and `case-guppi` does not recommend it. A check in `/pre-spec` over the `When` and `Then` of a Criterion is left out: that would cover only this one rule, and Frontier item C2 of this session reopens the part of `rule-case-protocol` on case 670.4, which this Case does not change. A new Estimate, `estimate-case-build-judges-options-against-the-broken-rule`, checks the new step. The method reads the new Render in the Spec at the Retro of this session, since no Case of this session is built under the new text before Work Mode renders it. A Glob `vault/wiki/**/estimate-case-build-judges-options-against-the-broken-rule.md` printed nothing, so the slug is free; the Estimate has a `ref`, so no vault query was run. A Grep for `\*\*After:\*\*` over `vault/wiki/rules/` printed `rule-orchestration.md` and `rule-skill-grill-me.md`, and over `.claude/` printed `.claude/skills/grill-me/SKILL.md`. `rule-orchestration` sets only how the main agent translates and shows a round. The grill-me template says that a cost, when it matters, is a plain sentence inside the `**After:**` text, so the new sentence keeps its form. The other Estimates of `rule-case-build` stand. The fork line of the `Then` of `estimate-case-build-writes-the-case` stays true. `estimate-case-build-checks-the-finished-case` checks the finished Case against the person's choices, after the round. No sentence of the page becomes false: the new sentence adds a step to the paragraph on forks. The lesson was written in another session, so the decision line carries no `addresses` mark.

> **problem:**
> `case-guppi` judges an option for a defect against the item's own words, not against the rule the defect breaks. So it can recommend an option that keeps the same defect in the rest of the text.

> **recommend:**
> - **Where the fix lives**
>   - Recommended: (a) one sentence in `rule-case-build`: when an item reports a defect, `case-guppi` finds the rule it breaks and judges each option against that rule over the whole text the option leaves; no check in `/pre-spec`, which item C2 may take up.
>   - Answer: agreed, (a).
> - **How a round shows an option that fixes only part of the defect**
>   - Recommended: (a) the option may stand; its `**After:**` line names the part that still breaks the rule, and the agent does not recommend it.
>   - Answer: agreed, (a).
> - **How we check that the fix works**
>   - Recommended: (a) a new Estimate, `estimate-case-build-judges-options-against-the-broken-rule`, read at the Retro of this session against the new Render in the Spec.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` looks for the forks of an item.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-judges-options-against-the-broken-rule`: the new check of the step.
> **＋** `rule-skill-grill-me`, rendered into `.claude/skills/grill-me/SKILL.md`: the form of a question of a round and of its `**After:**` line.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case on a Frontier item that reports a defect: a text that breaks a rule.

> **then:**
> Before it writes its round, it finds the rule the defect breaks and reads the passage of that rule.
> **＋** It judges each option of the round against that rule over the whole text the option leaves; for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes.
> **＋** An option that leaves a part of that text breaking the rule may stand in the round; its `**After:**` line names that part, and `case-guppi` does not recommend that option.
> **－** The `**After:**` line keeps the form of `.claude/skills/grill-me/SKILL.md`: the part left is a plain sentence inside its text.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` the exceptions — the `－` lines of `then`; and what is left not done. ``
>   - new: `` the exceptions — the `－` lines of `then`; and what is left not done. When the item reports a defect — a text that breaks a rule — find the rule it breaks and read its passage, and judge each option of your round against that rule over the whole text the option leaves: for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes; an option that leaves a part of that text breaking the rule may stand, its `**After:**` line names that part in a plain sentence, and you do not recommend it (case 780). ``
>   - change: `case-guppi judges each option of a round against the rule the defect of the item breaks, over the whole text the option leaves (case 780)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-judges-options-against-the-broken-rule`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, on an item that reports a defect, judges each option of its round against the rule the defect breaks over the whole text the option leaves, and names in the After line of an option the part it leaves breaking the rule, without recommending it`
>   - method: `by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] read `estimate-case-build-judges-options-against-the-broken-rule`

> **ratification:**
> ```
> - decision[case 780][update][rule-case-build]{ref:rule-case-build}
> - decision[case 780][create][estimate-case-build-judges-options-against-the-broken-rule]{ref:rule-case-build}{tags:session,workflow,harness}
> ```
