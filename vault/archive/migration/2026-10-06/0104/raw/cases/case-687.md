## Case 687 — The Insight on the loop after the pre-spec findings is answered again

> **context:**
> `insight-prespec-after-findings-loop-unruled` says that the rules of pre-spec stop at its report, so the main agent improvises what follows the findings. Case 600 set it `actioned` on the loop that cases 561.1 and 561.2 wrote into the skill of `rule-prespec`. Synthesis then reopened it with two lessons. `lesson-prespec-one-ask-guppi-run-samples-the-spec` records that one `ask-guppi` run over a large Spec returns only part of the findings; case 674.1 has the report list what the run did not check and never say the whole Spec is checked, and case 675 dropped the open question of more help for that run by the person's choice. `lesson-prespec-confirmation-prompt-invites-a-new-finding` records a confirmation message that invited new findings; case 638 has step 6 of the skill ask only whether each finding is closed, and the reading of `estimate-prespec-confirms-the-findings-once` at the `/pre-spec` of session 1343 found the message kept to it. Since cases 595.1 and 634.2 the skill also holds the answers until the person has answered the report, and has the same runs confirm their findings once. So the Insight is open only for causes already fixed, and it stands in the backlog. The person chose to set it `actioned` again, naming the Decision of this Case, the latest, as `rule-insights-schema` asks and as case 678 did. Its `pattern` states the cause as it stood when it was found, and stays.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Insight carries no `deferred_by`, so no line carries a `{supersedes:...}` mark. The frame. This Case does not change `rule-prespec`; Case 686.1 of this session replaces one sentence of its skill on what the hook of `rule-prespec-onward` says inside the loop, and this Case does not touch that sentence or that moment. The Insight carries no Estimate. `estimate-backlog-renders` lists an Insight under `## Deferred` only while it is `open`, `estimate-generate-cascades` archives each `clustered` child of an `actioned` Insight, and `estimate-insights-schema-checked` requires `addressed_by` on an `actioned` Insight; their Criteria speak of this change and stay true, so they stand and check this Case. `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-confirms-the-findings-once` check the loop itself, which does not change, so they stand. A Grep `insight-prespec-after-findings-loop-unruled` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 5 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/lessons/lesson-prespec-confirmation-prompt-invites-a-new-finding.md` and `vault/wiki/lessons/lesson-prespec-one-ask-guppi-run-samples-the-spec.md`. The librarian writes `brief.md` and `backlog.md` from the pages, and `log.md` is history, so they were not read and stand. The two lessons name the Insight in their `insight` field, which stays true, and the cascade archives them.

> **problem:**
> The Insight stays open in the backlog, but the skill of pre-spec now sets each step after the findings, and both lessons that reopened it have their fixes there.

> **recommend:**
> - **What to do with the open note on the loop after the pre-spec findings**
>   - Recommended: (a) close it now, naming this Case as its answer; no rule and no check changes.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the pre-spec report found that the `then` line saying `rule-prespec` does not change is false of the plan, since Case 686.1 replaces a sentence of that rule; the fix needs no word of the person.
>   - Taken: the line now says that this Case does not change `rule-prespec`.

> **given:**
> `insight-prespec-after-findings-loop-unruled`: the Insight that this Case sets `actioned`.
> **＋** `rule-insights-schema`: the shape of an Insight, which asks for one `addressed_by`, the latest.
> **＋** `lesson-prespec-one-ask-guppi-run-samples-the-spec`: a `clustered` child that reopened the Insight.
> **＋** `lesson-prespec-confirmation-prompt-invites-a-new-finding`: the other `clustered` child that reopened it.
> **＋** `rule-prespec`: the rule of the skill whose loop answers the pattern.
> **＋** `rule-page-generation`: the rule of `guppi generate` and its cascade.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case and runs its cascade, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-prespec-after-findings-loop-unruled` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** `lesson-prespec-one-ask-guppi-run-samples-the-spec` and `lesson-prespec-confirmation-prompt-invites-a-new-finding` become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists the Insight under `## Deferred`.
> **－** This Case does not change `rule-prespec`.

> **tasks:**
> - [ ] update `insight-prespec-after-findings-loop-unruled`
>   - set:
>     ```
>     {status: actioned, addressed_by: decision-case-687}
>     ```
>   - change: `actioned again: the skill of rule-prespec sets the loop after the findings (cases 561.2, 595.1, 634.2); the report lists what the one ask-guppi run did not check and the person kept one run (cases 674.1, 675); the confirmation message asks only whether each finding is closed (case 638) (case 687)`

> **ratification:**
> ```
> - decision[case 687][update][insight-prespec-after-findings-loop-unruled]{ref:insight-prespec-after-findings-loop-unruled}
> ```
