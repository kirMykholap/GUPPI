## Case 993 — The STOP: line of an acknowledging reply gets an Estimate of its own

> **context:**
> `estimate-orchestration-acknowledging-reply` checks the form of the reply that acknowledges a ratification. Case 992.2 added to its Criterion the line that an acknowledging reply after `/pre-spec` that waits for the person's word opens with `STOP:`, the `LEDGER` block right after it. The reading of ledger line 22 of session 2038 then set the page `passed`, but it was taken on the replies of that session, on the Render before Case 992.2, and its Result says that the `STOP:` line was not exercised (brief, Flags; handoff of session 2038, Observations). Such a reply comes only in a session where, after `/pre-spec`, an acknowledging reply still waits for the person, so the line needs a reading of its own. `rule-estimates-schema` sets that the `＋` and `－` lines stay in one Criterion while one run checks them, and that a line with a test or a reading of its own is split off, on the axis of the promise. The person chose the split: Case 993.1 replaces the Criterion of the old Estimate whole without that line, which only points to the new Estimate, and the old Estimate goes `pending` and is read at the Retro of this session; Case 993.2 creates `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`, whose `method` waits for that event, as case 781 sets for a part that opens with `by hand, after`. The text of `rule-orchestration` and of `vault/wiki/orchestration.md` does not change, since the behaviour stays as Case 992.2 set it; only the Estimates that check it change. The `purpose` and `method` of the old Estimate state the four parts in order and the replies it reads, not the `STOP:` line, so they stand. The block of the old Estimate in `.guppi/links.md` names as neighbours `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`, `rule-ledger-write`, `rule-orchestration`, `rule-prespec-onward` and `estimate-orchestration-shows-the-frontier-after-a-closed-line`; none of their purpose lines speaks of the `STOP:` line of an acknowledging reply. A Grep of `vault/wiki/` for `estimate-orchestration-acknowledging-reply`, `log.md` and `brief.md` left out, printed `rules/rule-orchestration.md` (its `estimates` list and a History line) and `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`; the two lines of the second say that the checklist and the own form of the acknowledging reply are as the old Estimate sets them, and both stay true, since the checklist and the four parts do not change. A Grep of `.guppi/tests/` for `acknowledging-reply` printed a count of 0, so no test reads the old page live. A Glob `vault/**/estimate-orchestration-acknowledging-reply-*.md` printed nothing, so the new slug is free. The promise of `estimate-prespec-onward-sends-the-agent-on`, that the hook stays silent on a reply that opens with `STOP:`, is not signed again in Case 993.2. The new Criterion of Case 993.1 drops the `STOP:` line of the old one and rewrites its first line to point to the new Estimate, since that line moves to Case 993.2; the lines of Case 993.2 share words with those of Case 993.1 because both describe parts of the same reply, but each promise stands in one Criterion only. Finding 1.1 of `ask-guppi` at the `/pre-spec` of this session found that the first `when` of Case 993.2 covered only a reply that waits while another Case shown waits for the person, though the old line and `vault/wiki/orchestration.md` speak of any reply after `/pre-spec` that waits for the person's word, and line 26 of `estimate-prespec-onward-sends-the-agent-on` names a second reason to wait, a question the person must answer; the `when` now names both, so no part of the old line is left with no Criterion. A Grep of the ledger of this session for `lesson\[error\]` and for `\{addresses:` printed nothing, so no lesson is addressed.

> **problem:**
> `estimate-orchestration-acknowledging-reply` stands `passed` while the `STOP:` line of its Criterion has had no reading, and that line can be read only in a session that has the event it needs.

> **recommend:**
> - **How the unread STOP: line gets a reading**
>   - Recommended: (a) split the `STOP:` line into its own Estimate, whose `method` waits for an acknowledging reply after `/pre-spec` that waits for the person's word; the old Criterion is replaced whole without it, points to the new Estimate, goes `pending` and is read at the Retro of this session.
>   - Answer: agreed, (a).

### Case 993.1 — The acknowledging reply keeps its four parts without the STOP: line

> **given:**
> `estimate-orchestration-acknowledging-reply`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the Estimate that checks the `STOP:` line.
> **＋** `rule-orchestration`: the rule that sets the acknowledging reply.
> **＋** `vault/wiki/orchestration.md`: the Render of that rule.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier the reply shows.
> **＋** `rule-prespec-onward`: the hook that sends the agent on after `/pre-spec`.
> **＋** `rule-ledger-write`: the ledger hook.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the check of a decision line the ledger hook holds.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block, before which stands nothing but the `STOP:` line that `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` checks. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply.
> **＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
> **＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

> **tasks:**
> - [ ] update `estimate-orchestration-acknowledging-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the STOP: line after /pre-spec split off into its own Estimate`
> - [ ] read `estimate-orchestration-acknowledging-reply`

> **ratification:**
> ```
> - decision[case 993.1][update][estimate-orchestration-acknowledging-reply]{ref:rule-orchestration}
> ```

### Case 993.2 — An acknowledging reply that waits for the person after /pre-spec opens with STOP:

> **given:**
> `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the new check of the `STOP:` line.
> **＋** `estimate-orchestration-acknowledging-reply`: the check of the other parts of the reply.
> **＋** `rule-orchestration`: the rule that sets the acknowledging reply.
> **＋** `vault/wiki/orchestration.md`: the Render of that rule.
> **＋** `rule-estimates-schema`: the rule that splits off a line with a reading of its own.
> **＋** `/pre-spec`: the check of the Spec after which the reply stands.

> **when:**
> After `/pre-spec`, the person ratifies a Case, and the agent writes the reply that acknowledges it while that reply waits for the person's word, because another Case shown waits for the person or because a question the person must answer is open, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply opens with a line that opens with `STOP:`.
> **＋** The `LEDGER` block stands right after that line.
> **＋** The other parts follow in the order that `estimate-orchestration-acknowledging-reply` checks.
> **＋** The reply ends with its question to the person.

> **tasks:**
> - [ ] create `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether an acknowledging reply after /pre-spec that waits for the person opens with STOP:, the LEDGER block right after it, and ends with its question`
>   - method: `by hand, after an acknowledging reply after /pre-spec that waits for the person's word: that reply read against the Criterion in the transcript of its session under ~/.claude/projects/`
>   - tags: `[session, workflow, ledger]`
> - [ ] read `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`

> **ratification:**
> ```
> - decision[case 993.2][create][estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec]{ref:rule-orchestration}{tags:session,workflow,ledger}
> ```
