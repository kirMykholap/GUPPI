## Case 697 — On an empty Frontier the agent asks before it goes on to `/pre-spec`

> **context:**
> When the last open line under `## Cases` of the Frontier closes, `orchestration.md` lets the reply end with no question. The reply that acknowledges a ratification and the reply that carries a defer end with the Frontier. A reply that closes a line with no `LEDGER` block calls `/pre-spec` itself (cases 561.6, 561.7, 561.8). Then the `Stop` hook `uv run guppi onward --plan` of `rule-prespec-onward` sends the agent to `/pre-spec` in the same turn, by the reason `TO_PRESPEC` of `guppi/onward.py`. In this session the reply that acknowledged Case 696 closed the last line. The hook sent the agent on, and the person, who had a question, had to cancel the run to ask it. The person chose four things. Before `/pre-spec`, the reply asks whether to go on, in the plain form of the question which item is next, and the agent calls `/pre-spec` only on the person's word. All three kinds of reply that can leave no line open ask the same question. After `/pre-spec` the steps stay automatic: the hook still sends the agent on with the loop after the findings, or to the check and the exit. The reply that takes a conserved Spec at `/hi` goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it, since the person's choice of that Spec is the word to go on. The hook must also stop sending the agent to `/pre-spec`. That change is not in this Case. A Case that replaces a Criterion that another Case of the session replaces is a finding of `check_same_target` of `guppi/prespec.py`, and Case 696.2 replaces the Criterion of `estimate-prespec-onward-sends-the-agent-on`. So, by the person's choice, Case 696 is built again so that its new text of the hook and of that Estimate drops the reason that sends the agent to `/pre-spec`; it joins this batch. This Case changes only what the replies of the agent say, in the Render of `rule-orchestration`, by one sub-case per Estimate: 697.1 the acknowledging reply, 697.2 the reply that closes a line with no ratification and no defer, 697.3 the defer reply, 697.4 the list of questions that keep their own form. Each sub-case replaces the Criterion of its Estimate: `estimate-orchestration-acknowledging-reply`, `estimate-orchestration-shows-the-frontier-after-a-closed-line`, `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-asks-in-the-grill-me-shape`, whose `－` line lists the questions that keep their own form. Their `purpose` and `method` state no promise that changes, so they stand. The findings of `/pre-spec`, which the person agreed to, brought two changes. The list of questions in their own form became a sub-case of its own, 697.4, since one sub-case replaces one Criterion. The reply of 697.2 with no `LEDGER` block after `/pre-spec` now goes on by itself. The old words had it call `/pre-spec`, which `rule-prespec` forbids after the loop. And Case 696.2 gives no reason to a reply with no `LEDGER` block after a reply that the ledger hook did not send back, so without its own step that reply would stop Plan Mode where no person is needed. The hook runs from the working tree once Work Mode changes it under Case 696, and `orchestration.md` changes at the librarian's render after the session. In between, the hook stays silent before `/pre-spec`, while the old text has the reply end with the Frontier and no question. The turn then passes to the person, who can say to go on. No hook refuses anything there and nothing is lost, so no old form is kept. A Grep `prespec-onward` over `vault/wiki/` with the glob `!**/{log,brief}.md` printed `orchestration.md`, `rules/rule-orchestration.md`, `rules/rule-prespec.md`, `rules/rule-prespec-onward.md`, `rules/rule-plan-mode.md`, `lessons/lesson-case-build-related-cases-same-sentence-missed.md`, `lessons/lesson-prespec-onward-a-reminder-answer-ends-the-run.md`, `estimates/estimate-orchestration-defers-in-one-reply.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimates/estimate-prespec-onward-tells-the-loop-from-its-end.md`, `estimates/estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `estimates/estimate-prespec-onward-sends-the-agent-on.md`, `estimates/estimate-prespec-onward-reads-the-decisions-of-the-session.md` and `estimates/estimate-prespec-confirms-the-findings-once.md`. Outside History lines: `orchestration.md`, `rule-orchestration` and the three Estimates of the replies change here. `rule-prespec-onward` and its Estimates are the frame of Case 696. `rule-prespec` and `estimate-prespec-confirms-the-findings-once` say that the hook sends the agent on after the ratification in the loop after `/pre-spec`, which stays true. `estimate-retro-onward-sends-the-agent-to-the-handoff` keeps the judgment of `--plan` apart. `rule-plan-mode` and the two lessons only name the page. A Grep `/pre-spec` over `.claude/` printed `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/ask-guppi.md`. The `/hi` skill goes on to `/pre-spec` after a conserved Spec is taken, which stands by the person's choice. The `/pre-spec` skill sets the steps after `/pre-spec`, which stay. `ask-guppi.md` names the moment of its run only. A Grep `TO_PRESPEC|Call /pre-spec|call /pre-spec` over `*.py` printed `guppi/onward.py` and `tests/test_onward.py`, the code and the tests of the hook. Case 696 built again changes them, and this Case changes no code.

> **problem:**
> On an empty Frontier, the hook sends the agent on to `/pre-spec` in the same turn as the reply that closed the last line. So the person has no turn to ask a question before `/pre-spec` runs.

> **recommend:**
> - **How the agent stops to ask before `/pre-spec`**
>   - Recommended: (a) the reply asks whether to go on, in the plain form of the question which item is next, and the hook no longer sends the agent to `/pre-spec`; a yes makes the agent call `/pre-spec`, and a question of the person gets an answer and the question again.
>   - Answer: agreed, (a).
> - **Which replies ask the question**
>   - Recommended: (a) all three ask: the acknowledging reply, the defer reply and the reply that closes a line with no ratification; no reply calls `/pre-spec` on its own.
>   - Answer: agreed, (a).
> - **The steps after `/pre-spec`**
>   - Recommended: (a) the steps after `/pre-spec` stay automatic.
>   - Answer: agreed, (a).
> - **How this Case and Case 696 share the hook's text**
>   - Recommended: (a) this Case builds on top of Case 696 and rewrites the hook's promise and rule text again, Case 696 untouched.
>   - Answer: agreed, (a); the check of the Case then showed that this cannot hold, and the question was asked again as "How this Case and Case 696 share the hook's text (asked again)".
> - **When you take a saved plan from an earlier session at `/hi`**
>   - Recommended: (a) the reply that takes a conserved Spec goes on to `/pre-spec` with no question, as `/hi` sets it.
>   - Answer: agreed, (a).
> - **How this Case and Case 696 share the hook's text (asked again)**
>   - Recommended: (a) Case 696 is built again with the change, and this Case changes only the replies.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`, agreed to by the person: after `/pre-spec`, a reply with no `LEDGER` block that leaves no line under `## Cases` open goes on by itself, to the check and the exit or with the loop after the findings.
>   - Taken: Case 697.2 says so in its new text of `rule-orchestration` and in its `then`.
> - **Change**
>   - Asked: a finding of `/pre-spec`, agreed to by the person: the Criterion of `estimate-orchestration-asks-in-the-grill-me-shape` gains the question whether to go on to `/pre-spec` in its list of questions that keep their own form.
>   - Taken: Case 697.4 replaces that Criterion and carries the pair of `rule-orchestration` that adds the question to the list, moved from Case 697.1, since one sub-case replaces one Criterion.

### Case 697.1 — The acknowledging reply asks before `/pre-spec`

> **given:**
> `rule-orchestration`: its Render sets the acknowledging reply and the questions that keep their own form.
> **＋** `estimate-orchestration-acknowledging-reply`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the skill that checks the plan.
> **＋** `rule-prespec-onward`: the `Stop` hook that sends the agent on.
> **＋** `vault/raw/2026-10-07/0211/cases/case-696.md`: Case 696, built again, which stops the hook sending the agent to `/pre-spec`.
> **＋** `rule-ledger-write`: the ledger hook, which writes the `LEDGER` block and holds a decision line.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: sets when the ledger hook holds a decision line.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
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
> - [ ] update `rule-orchestration`
>   - old: `` and, last, the question which item is next, or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8) ``
>   - new: `` and, last, the question which item is next, or, when no line under `## Cases` is open, before `/pre-spec` the question whether to go on to `/pre-spec`: the agent calls `/pre-spec` only when the person says to go on, and a reply that answers a question of the person instead ends with the same question again (case 697.1); after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8) ``
>   - change: `before /pre-spec the acknowledging reply on an empty Frontier asks whether to go on, and the agent calls /pre-spec only on the person's word (case 697.1)`
> - [ ] update `estimate-orchestration-acknowledging-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — on an empty Frontier before /pre-spec the reply asks whether to go on`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-acknowledging-reply`

> **ratification:**
> ```
> - decision[case 697.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 697.1][update][estimate-orchestration-acknowledging-reply]{ref:rule-orchestration}
> ```

### Case 697.2 — A reply that closes the last line with no ratification asks before `/pre-spec`

> **given:**
> `rule-orchestration`: its Render sets the reply that closes a Frontier line with no ratification and no defer.
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-acknowledging-reply`: sets the form of the Frontier checklist.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the skill that checks the plan.
> **＋** `rule-prespec-onward`: the `Stop` hook that sends the agent on.
> **＋** `rule-skill-hi`: sets the first reply of `/hi` and the taking of a conserved Spec.
> **＋** `rule-prespec`: sets the loop after the findings of `/pre-spec`, the check and the exit.

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-orchestration-acknowledging-reply` sets.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
> **＋** The open `W` lines are folded into one line that lists their ids.
> **＋** Each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply, with a `LEDGER` block or without one. The agent calls `/pre-spec` only after the person says to go on.
> **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows the Frontier. A reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on. A reply with no `LEDGER` block goes on by itself after the Frontier, to the check and the exit or on with the loop after the findings, as `rule-prespec` sets it.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** The reply that takes a conserved Spec and closes the other lines goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-orchestration-acknowledging-reply` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` when no line under `## Cases` is open, it asks nothing: a reply with no `LEDGER` block calls `/pre-spec` after the Frontier, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on (case 561.6) ``
>   - new: `` when no line under `## Cases` is open, before `/pre-spec` it asks instead whether to go on to `/pre-spec`, with a `LEDGER` block or without one, and the agent calls `/pre-spec` only when the person says to go on, but for the reply that takes a conserved Spec, which goes on to `/pre-spec` with no question, as `rule-skill-hi` sets it, since the person's choice of that Spec is the word to go on (case 697.2); after `/pre-spec` it asks nothing: a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on (case 561.6), and a reply with no `LEDGER` block goes on by itself after the Frontier, to the check and the exit or on with the loop after the findings, as `rule-prespec` sets it (case 697.2) ``
>   - change: `before /pre-spec a reply that closes the last Cases line with no ratification asks whether to go on, a conserved Spec taken at /hi excepted (case 697.2)`
> - [ ] update `estimate-orchestration-shows-the-frontier-after-a-closed-line`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — on an empty Frontier before /pre-spec the reply asks whether to go on`
> - [ ] read `estimate-orchestration-shows-the-frontier-after-a-closed-line`

> **ratification:**
> ```
> - decision[case 697.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 697.2][update][estimate-orchestration-shows-the-frontier-after-a-closed-line]{ref:rule-orchestration}
> ```

### Case 697.3 — The defer reply asks before `/pre-spec`

> **given:**
> `rule-orchestration`: its Render sets the reply that carries a short-form defer.
> **＋** `estimate-orchestration-defers-in-one-reply`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line`: sets the reply that closes a line with no ratification and no defer.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session.
> **＋** `/pre-spec`: the skill that checks the plan.
> **＋** `rule-prespec-onward`: the `Stop` hook that sends the agent on.
> **＋** `rule-spec-write`: the `Stop` hook that writes the short Case into the plan file.

> **when:**
> In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply. The agent calls `/pre-spec` only after the person says to go on.
> **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after the findings.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows the question, or the Frontier when no question stands.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line, and a reply that closes only such lines is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on to `/pre-spec`, or, after it, on with the loop after its findings (cases 561.7, 686.1) ``
>   - new: `` or, when no line under `## Cases` is open, before `/pre-spec` the question whether to go on to `/pre-spec`, with no text after it, and the agent calls `/pre-spec` only when the person says to go on (case 697.3); after `/pre-spec` no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after its findings (cases 561.7, 686.1) ``
>   - change: `before /pre-spec the defer reply on an empty Frontier asks whether to go on (case 697.3)`
> - [ ] update `estimate-orchestration-defers-in-one-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — on an empty Frontier before /pre-spec the defer reply asks whether to go on`
> - [ ] read `estimate-orchestration-defers-in-one-reply`

> **ratification:**
> ```
> - decision[case 697.3][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 697.3][update][estimate-orchestration-defers-in-one-reply]{ref:rule-orchestration}
> ```

### Case 697.4 — The question whether to go on keeps its own form

> **given:**
> `rule-orchestration`: its Render lists the questions of the main agent that keep their own form.
> **＋** `estimate-orchestration-asks-in-the-grill-me-shape`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `.claude/skills/grill-me/SKILL.md`: sets the question shape.
> **＋** `/pre-spec`: the skill that checks the plan, whose report holds questions.
> **＋** `/hi`: the skill that opens the session.
> **＋** `rule-spec-capture`: sets the choice between `/work` and `/carry`.

> **when:**
> The main agent puts a question to the person itself, outside a round of `case-guppi`. The question is one of these:
> - a decision it needs in the report of `/pre-spec`;
> - a question at `/hi`;
> - a question at a stop of Work Mode;
> - the question whether another Case of the session is built again after a Case was bounded around a clash with it;
> - at `/pre-spec`, after the `ask-guppi` runs confirm their findings, the question whether each finding not closed is fixed or left.
>
> This is with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
> **＋** It stands in Russian, and its labels may stand translated.
> **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` keep their own form (case 561.13) ``
>   - new: `` the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open (case 697.4), and the choice between `/work` and `/carry` keep their own form (case 561.13) ``
>   - change: `the question whether to go on to /pre-spec on an empty Frontier keeps its own form (case 697.4)`
> - [ ] update `estimate-orchestration-asks-in-the-grill-me-shape`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the question whether to go on to /pre-spec keeps its own form`
> - [ ] read `estimate-orchestration-asks-in-the-grill-me-shape`

> **ratification:**
> ```
> - decision[case 697.4][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 697.4][update][estimate-orchestration-asks-in-the-grill-me-shape]{ref:rule-orchestration}
> ```
