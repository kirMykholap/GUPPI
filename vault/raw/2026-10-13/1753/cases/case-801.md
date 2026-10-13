## Case 801 — case-guppi quotes the last output of a check with its source

> **context:**
> Where an option of a round rests on whether a check passes, such as `make lint`, `case-guppi` reads what that check printed at its last run, as the brief reports it, before it recommends the option. Case 798.2 put this into the Render of `rule-case-build` and created `estimate-case-build-reads-the-last-output-of-a-check`. The two texts part on one word. The Render says that `context` names that output. The first Then line of the Criterion says that `case-guppi` quotes it with its source in the `context`. At the Retro of session 1426 the reading of the new Render against the Criterion was `failed` for this gap (ledger line 28 of session 1426). The brief reports the last `make lint` under `## Flags` as two lines, one of them `estimates/estimate-case-build-reads-the-last-output-of-a-check: unread: failed`. By the person's answers, the Render takes the word of the Criterion, and the Criterion stands as it is written.
>
> The governing rule is `rule-agent-writing`: a claim names a real source, and is no wider than the output it rests on. Quoting the output with its source keeps to it. A bare name of the output would also name a source, but the person could not see what the output said. This Case replaces one sentence of the Render, the sentence of case 798.2, and adds case 801 to its source mark. The other sentences of the Render that speak of reading before a recommendation stand. The sentence of case 798.1 says that `context` names the rule, not an output. The sentence of case 797.1 sets the state at the moment a check runs, which the sentence of case 798.2 still points to. Case 800.1 of this session adds a sentence to the same Render, after the sentence of case 561.11. Its `old` and this Case's `old` share no words, and the two new texts speak of different things. The update of the Estimate writes its Criterion back whole as this Case's `when` and `then`, the same text as now, so that it is `pending` again. Its `purpose` says that `case-guppi` names the output, so the update sets it anew. Its `method`, a reading of the new Render in the Spec at the Retro of the session, stands. The `## Result` keeps the failed reading until the next reading. A Grep `names that output|last output of a check|reads-the-last-output` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `.claude/agents/case-guppi.md`, `vault/wiki/log.md`, `vault/wiki/insights/insight-case-build-recommends-without-reading-the-governing-rule.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-reads-the-last-output-of-a-check.md`. The hit in the insight is a History line, and the brief and the log are not read. The render writes the agent file again. A Grep `case-guppi\.md|rule-case-build|reads-the-last-output` over `tests/` printed nothing, so no test reads the agent file or the two pages live.

> **problem:**
> The instruction of `case-guppi` and the Estimate that checks it disagree. The instruction lets `context` only name the last output of a check, while the Criterion asks that `context` quotes it with its source. The reading failed, and `make lint` flags the Estimate.

> **recommend:**
> - **Which text changes: the instruction or the check?**
>   - Recommended: (a) the instruction says that `context` quotes the output with its source; the Criterion stands.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) set the same Estimate back to `pending`, and read it again at the Retro of this session against the new instruction text.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`; one sentence of its Render changes.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `vault/wiki/brief.md`: its `## Flags` and `## Readings at the close` hold the last output of `make lint` and `make test`.
> **＋** `estimate-case-build-reads-the-last-output-of-a-check`: its Criterion is written again whole and its `purpose` is set anew.
> **＋** `rule-agent-writing`: a claim names a real source.
> **＋** `rule-case-protocol`: the form of `context`.
> **＋** `vault/raw/2026-10-13/1753/cases/case-800.md`: Case 800.1 changes another sentence of the same Render.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub.

> **then:**
> Before it recommends that option, it reads what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, judges the option against that output, and quotes it with its source in the `context`.
> **＋** Where another Case of the same session changes that check or the pages it reads, it judges the option by the state at the moment the check runs, as `rule-case-build` sets it for such a Case, and not by the last output alone.
> **＋** Where the brief does not report that output, the `**After:**` line of the option and the `context` say that its last output was not read.
> **－** An option whose last output was not read may still be recommended.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: ``` `context` names that output, and where the brief does not report it, the `**After:**` line of the option and `context` say that its last output was not read, and the option may still be recommended (case 798.2). ```
>   - new: ``` `context` quotes that output with its source, and where the brief does not report it, the `**After:**` line of the option and `context` say that its last output was not read, and the option may still be recommended (cases 798.2, 801). ```
>   - change: `context quotes the last output of a check with its source, as the Criterion of estimate-case-build-reads-the-last-output-of-a-check asks (case 801)`
> - [ ] update `estimate-case-build-reads-the-last-output-of-a-check`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi, before it recommends an option that rests on whether a check passes, reads what that check printed at its last run, from the brief, judges the option against it, or by the state at the moment the check runs where another Case of the session changes the check or the pages it reads, and quotes it with its source in context, or says in the After line and context that the output was not read"
>     ```
>   - change: `the Criterion written again whole and the purpose set to quote the output with its source, after the failed reading of session 1426 (case 801)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-reads-the-last-output-of-a-check`

> **ratification:**
> ```
> - decision[case 801][update][rule-case-build]{ref:rule-case-build}
> - decision[case 801][update][estimate-case-build-reads-the-last-output-of-a-check]{ref:rule-case-build}
> ```
