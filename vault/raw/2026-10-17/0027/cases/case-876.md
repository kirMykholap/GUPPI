## Case 876 — The old defers of a Lesson and a Decision page move to the backlog or retire

> **context:**
> When a Case puts an item off, `guppi generate` writes the Decision page of that Case into the `deferred_by` field of the page the `defer` line names, and `guppi backlog` lists each live page whose `deferred_by` is not empty, so a later session sees the item. The `defer` method of `.guppi/guppi/generate.py` writes `deferred_by` only on a page of a folder of `DEFERRABLE` of `.guppi/guppi/materialize.py`: rules, entities, insights and estimates. On a Lesson or a Decision page an older defer left only a History line. Case 865 refuses such a defer from now on, at both `Stop` hooks, at `/pre-spec` and at `generate`, and its message `DEFER_OF_A_RECORD` asks for a defer of the rule or entity page whose change settles the matter; it left the old defers as they stand. Two live Decision pages hold them, read by their paths because this Case retires them: `decision-case-836` defers `lesson-ledger-window-stops-at-a-resume-on-the-next-day` and `lesson-case-build-agent-context-grows-on-every-resume`, and `decision-case-863` defers `decision-case-855`, which stands archived under `vault/archive/`. A Grep of `^- \S+ deferred` over `vault/wiki/lessons/` printed those two lesson files alone. `backlog.md` holds no line for any of them.
>
> The person chose: each lesson's cause moves to a defer of the rule page whose change would fix it, and `decision-case-863` retires with nothing in its place, since in session 2104 the person chose no Case for the out-of-date sentence of `decision-case-855` (handoff of session 2104, Notes from memory). `session_event_logs` of `.guppi/guppi/ledger.py`, read whole, walks the event logs back from today and stops at the first date that holds a `session-start` of the stamp, so a resume on the next day hides the `/hi` of the day before; `rule-ledger-write` lists that module in `implementation_ref`. The Render of `rule-orchestration` sends the person's answers and changes to the same `case-guppi` by `SendMessage`, which is where its context grows. Each defer line carries `{supersedes:case 836}`, and the first carries `{supersedes:case 863}` too. `decision` of `.guppi/guppi/generate.py`, read whole, sets each page a `supersedes` names `superseded`, and `clear_deferred_by` clears `deferred_by` only on a target that holds it, so the lesson pages and `decision-case-855` do not change; `cascade` then archives each `superseded` Decision page by `archived_by_cascade`. The rule that governs the choice is `rule-backlog`, whose Purpose prevents a deferred item from dropping out of sight. The causes of the two lessons stay not fixed: this Case only puts them where the list shows them.
>
> No new Estimate is created. `estimate-backlog-renders` already checks that `backlog.md` holds one line per live page with a `deferred_by` that is not empty, with the page's `purpose`, and `estimate-generate-cascades` already checks that a Decision page standing `superseded` becomes `archived`; both Criteria speak of the mechanism this Case uses and not of any one page, so they stand. The text of `rule-ledger-write` and `rule-orchestration` does not change, so no Estimate of either page is touched.

> **problem:**
> Two live Decision pages put off two lessons and one Decision page, and since neither kind of page carries `deferred_by`, no line of `backlog.md` shows the three items.

> **recommend:**
> - **What happens to the two lessons that were put off?**
>   - Recommended: (a) move each put-off to the rule that would fix it.
>   - Answer: agreed, (a).
> - **What happens to the Decision page that was put off?**
>   - Recommended: (a) retire the put-off with nothing in its place.
>   - Answer: agreed, (a).
> - **How is this Case checked?**
>   - Recommended: (a) name the two Estimates that already check it.
>   - Answer: agreed, (a).

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, deferred for the walk of the event logs.
> **＋** `rule-orchestration`: the rule that sends each round to the same `case-guppi`, deferred for its growing context.
> **＋** `decision-case-836`: the Decision page that deferred the two lessons, retired.
> **＋** `decision-case-863`: the Decision page that deferred `decision-case-855`, retired.
> **＋** `vault/wiki/backlog.md`: the list of put-off items that `guppi backlog` writes.
> **＋** `rule-backlog`: the rule that no put-off item drops out of sight.

> **when:**
> The librarian runs `uv run --project .guppi guppi generate` and then `uv run --project .guppi guppi backlog` over the Spec that holds this Case.

> **then:**
> `vault/wiki/backlog.md` holds a line for `rule-ledger-write` and a line for `rule-orchestration`, each with the cause of its lesson.
> **＋** `decision-case-836` and `decision-case-863` stand `archived`.
> **－** The two lesson pages and `decision-case-855` do not change.

> **tasks:**
> - [ ] defer `rule-ledger-write`
>   - type: `rule`
>   - purpose: `session_event_logs of .guppi/guppi/ledger.py walks the event logs back from today and stops at the first date that holds a session-start of the stamp, so after a resume on the next day the ledger hook finds no /hi and refuses the decision lines (lesson-ledger-window-stops-at-a-resume-on-the-next-day); moved here from the defer of the lesson by Case 836`
> - [ ] defer `rule-orchestration`
>   - type: `rule`
>   - purpose: `Each round and each rebuild resumes the same case-guppi by SendMessage with its whole transcript, so its context only grows, and nothing caps it or hands a rebuild to a fresh agent with the case file and the reason alone (lesson-case-build-agent-context-grows-on-every-resume); moved here from the defer of the lesson by Case 836`

> **ratification:**
> ```
> - decision[case 876][defer][rule-ledger-write]{ref:rule-ledger-write}{supersedes:case 836}{supersedes:case 863}
> - decision[case 876][defer][rule-orchestration]{ref:rule-orchestration}{supersedes:case 836}
> ```
