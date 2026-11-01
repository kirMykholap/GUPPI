## Case 992 — After /pre-spec, a STOP: line opens only a reply with a LEDGER block

> **context:**
> This Case replaces Case 990 whole after the check of `/pre-spec`. After `/pre-spec`, the `Stop` hook of `rule-prespec-onward`, `uv run --project .guppi guppi onward --plan`, sends the agent on at the end of a reply. Each of its three reasons — `to_out`, `TO_EXIT` and `TO_LOOP` of `.guppi/guppi/onward.py` — ends with the same text, `ONLY_THE_PERSON`: when a Case waits only for the person's word, open the reply with `STOP:`. The check of `rule-case-check` wants nothing before a shown Case but a horizontal rule, and a round must open with its first question or its Context label. In session 2026-11-01/1721 the hook sent this text after a ratification (transcript `cb575daf-7b4e-455c-a22c-1fcffcbdc234.jsonl`, line 1148). Case 987 was then built again on a finding of the check of the plan and shown with a first line that opened with `STOP:` and said, in Russian, that Case 987 waited for ratification (line 1173). `uv run --project .guppi guppi casecheck --prompt` noted that text before the Case at the person's next message (line 1182). No refusal of the hook stands after that showing in the transcript. `plan_onward` of `.guppi/guppi/onward.py`, read whole, returns no reason for a reply that opens with `STOP:`, and none for a reply when `ledger_lines` of `.guppi/guppi/ledger.py` finds no `LEDGER` block in it and `sent_back_last` finds no refusal of the ledger hook on the reply that ended just before it. `outside_the_list` and `round_opening` of `.guppi/guppi/casecheck.py`, read whole, take any line before the first Case heading, and any first line of a shown round that opens neither with the question mark nor with a bold label, as a fault. A showing or a round carries no `LEDGER` block, so only the text of the reasons asked for the `STOP:` line there.
>
> Case 990 narrowed that text, as the person chose. The check of `/pre-spec` then found two faults. First, after `/pre-spec` the reply that acknowledges a ratification carries a `LEDGER` block, and when it waits for the person it must open with `STOP:`, while `## The acknowledging reply` of `rule-orchestration` puts the `LEDGER` block first, and Case 990 named neither that page nor `estimate-orchestration-acknowledging-reply`. The person chose that such a reply opens with the `STOP:` line and puts the `LEDGER` block right after it, with the hook unchanged. Second, the new text of the Purpose of `rule-prespec-onward` followed the sentence on a Case still out alone, while `ONLY_THE_PERSON` ends each of the three reasons. The new Purpose text now names each reason. The person chose one Case with two parts in place of Case 990, so each decision line carries `{supersedes:case 990}`, and the file of Case 990 stands.
>
> Case 992.1 changes the text the hook adds and replaces the Criterion of `estimate-prespec-onward-sends-the-agent-on`. Two lines of the old Criterion are not carried word for word on purpose: the line on what each reason adds, and the line on a reply with no `LEDGER` block, which now names a shown Case among such replies. Its `purpose` and `method` do not state the old text, so they stand. The Criterion of `estimate-prespec-onward-tells-the-loop-from-its-end` points to that Estimate for the added text, so it stands. A Grep of `waits only for the person|open (your|the|its) reply with ``?STOP` over `vault/wiki/`, `.claude/` and `.guppi/guppi/` printed 7 files: `.guppi/guppi/onward.py`, `rule-prespec-onward.md` and `estimate-prespec-onward-sends-the-agent-on.md`, which tasks change; the lesson of L35, a record that stands; and `.claude/skills/retro/SKILL.md`, `rule-retro.md` and `estimate-retro-onward-sends-the-agent-to-the-handoff.md`, which set `STOP:` for the reply that ends Retro, where no Case is shown, so they stand, as does `REASON` of `.guppi/guppi/onward.py` for `rule-retro-onward`. A Grep of `ONLY_THE_PERSON|STOP` over `.guppi/tests/` printed one file, `.guppi/tests/test_onward.py`; its tests assert that `ONLY_THE_PERSON` holds `STOP:`, `orchestration.md`, `case-guppi has not answered` and `waits only for the person's word`, and the new text keeps each of them.
>
> Case 992.2 changes `## The acknowledging reply` of `rule-orchestration` and replaces the Criterion of `estimate-orchestration-acknowledging-reply`. The first line of the old Criterion is not carried word for word on purpose, since it put the `LEDGER` block first with nothing before it. Its `purpose`, four parts in order, still holds, and its `method`, a reading of an acknowledging reply, reads the new line too, so both stand. `estimate-orchestration-acknowledges-the-opening-with-the-frontier` keeps the four parts for the reply of `/sprint-open`, which comes before `/pre-spec`, so it stands. A Grep of `four parts|block first|asks nothing|ends with the Frontier` over `vault/wiki/` printed 11 files: `orchestration.md` and `rule-orchestration.md`, whose section this Case changes and whose defer reply and reply that closes a Frontier line after `/pre-spec` ask nothing and wait for nobody, so they stand; the two Estimates above; `estimate-orchestration-shows-the-frontier-after-a-closed-line` and `estimate-orchestration-defers-in-one-reply`, on replies that wait for nobody, which stand; `log.md` and History lines of `rule-case-protocol.md`, not read; and `rule-case-build.md`, `rule-ledger-write.md` and `estimate-guppi-package-is-ready-after-the-install.md`, whose hits speak of a lesson or an install, not of this reply. Case 991.1 of this session, built at the same time, changes `rule-orchestration` in the closers of Frontier lines in `## Plan Mode and the Frontier`, `## The short form — deferred decisions` and the take-back sentence of `## Showing and signing a Case`; its finished file was read. This Case touches only `## The acknowledging reply`, whose old text matches once on the page, and no `old` of either Case falls in the text of the other. The new texts agree: the closers of lines put off that the acknowledging reply lists are those Case 991.1 gives a line whose Case ends nothing, and the defer reply and the take-back reply that Cases 991.3 and 991.4 keep ask nothing after `/pre-spec` and wait for nobody, so they need no `STOP:` line. No test reads `rule-prespec-onward`, the two Estimates or that section live: `.guppi/tests/test_orchestration.py` reads only the blocks tagged `showing` and `defer` of `orchestration.md`, which this Case leaves alone. The line of Case 992.2 that no tool call follows the `LEDGER` block shares words with the line of Case 992.1 on a spent refusal, but the two state different behaviours of different texts, the order of a reply and the judgment of a hook, so both stand.
>
> In `.guppi/links.md`, the blocks of `rule-prespec-onward`, `rule-orchestration`, both Estimates, `.guppi/guppi/onward.py` and `.guppi/tests/test_onward.py` name `rule-ledger-write`, `rule-spec-write`, `rule-case-check`, `rule-prespec`, `rule-retro-onward` and the other Estimates of `rule-orchestration` among their neighbours; none sets a `STOP:` line before a showing or a `LEDGER` block, so none is made false. The last `uv run --project .guppi guppi test` printed 1896 passed, 6 skipped, 1 deselected (`brief.md`, `## Readings at the close`). The lesson L35 belongs to session 2026-11-01/1721, so this Case gives it no mark; the ledger of this session holds no `error` lesson.

> **problem:**
> After `/pre-spec`, the hook of `rule-prespec-onward` tells the agent to open with `STOP:` any reply in which a Case waits for the person's word, while the check of `rule-case-check` notes any line before a shown Case, and `rule-orchestration` puts the `LEDGER` block first in the acknowledging reply. No text says which one holds, so the agent broke the layout of a showing.

> **recommend:**
> - **Which side gives way when a reply shows a Case and waits for the person**
>   - Recommended: (a) narrow the hook's message: `STOP:` opens only a reply the hook would send back, one with a `LEDGER` block; a reply that shows a Case or a round keeps the layout of `orchestration.md` with no `STOP:` line; the hook's judgment is unchanged.
>   - Answer: (a).
> - **Change**
>   - Asked: at the check of `/pre-spec`, the person agreed that an acknowledging reply after `/pre-spec` that waits for the person opens with the `STOP:` line and puts the `LEDGER` block right after it, with an update of `rule-orchestration` and the Criterion of `estimate-orchestration-acknowledging-reply` replaced whole, the hook unchanged; and the Purpose of `rule-prespec-onward` was to cover each reason of the hook.
>   - Taken: Case 992.2 sets the order of that reply; the new Purpose text of Case 992.1 names each of the three reasons.
> - **Where the change to the acknowledging reply goes**
>   - Recommended: (a) Case 990 built again under a new number, with two parts, `{supersedes:case 990}` on its decision lines.
>   - Answer: agreed, (a).

### Case 992.1 — The hook asks for STOP: only on a reply with a LEDGER block

> **given:**
> `rule-prespec-onward`: the hook that sends the agent on after `/pre-spec`; its Purpose states the text each of its reasons adds.
> **＋** `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: sets the reasons the hook gives; it stands.
> **＋** `.guppi/guppi/onward.py`: `ONLY_THE_PERSON`, the text each reason of `--plan` adds, and the docstring.
> **＋** `.guppi/tests/test_onward.py`: the tests of the reasons.
> **＋** `.guppi/guppi/ledger.py`: `refusals`, by which the hook reads the refusals of the stretch.
> **＋** `.claude/settings.json`: registers the hook on `Stop`.
> **＋** `vault/wiki/orchestration.md`: the layout of a showing and of a round, which the reason points to.
> **＋** `rule-case-check`: the check that notes a text of the agent's own before a showing or a round.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session, whose presence silences the hook.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose open lines under `## Cases` silence the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run --project .guppi guppi onward --plan`, and the command of the ledger hook is `uv run --project .guppi guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `.guppi/guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Its reason on stderr sends the agent on with the Cases still out, to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a question the person must answer, or a Case that waits only for the person's word — the agent opens with `STOP:` a reply that carries a `LEDGER` block, or that answers a reply the ledger hook sent back, and asks the person instead; that a reply that shows a Case or a round of `case-guppi` carries no `LEDGER` block and opens with no `STOP:` line, in the layout `vault/wiki/orchestration.md` sets; and that while a `case-guppi` has not answered the agent ends the turn as `vault/wiki/orchestration.md` sets it for a Case out and goes on in the turn that the answer opens.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript. `.claude/settings.json` registers it on `Stop`, after `uv run --project .guppi guppi onward`.
> **－** A Case still out, as `rule-prespec-onward` judges it, does not keep it silent: it changes only its reason.
> **－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
> **－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason, a reply that shows a Case with no line before its first Case heading among them.
> **－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run --project .guppi guppi onward` without `--plan` keeps its own judgment.

> **tasks:**
> - [ ] update `rule-prespec-onward`
>   - old: `` and to open the reply with `STOP:` and ask the person when each waits only for the person's word (as set in case 889.2). ``
>   - new: `` and to open the reply with `STOP:` and ask the person when each waits only for the person's word (as set in case 889.2). Each of its reasons — the one that names the Cases still out, the one that sends the agent to the check and the exit, and the one that sends it on with the loop after the findings — adds the same text: when only the person can go on, by a question the person must answer or a Case that waits only for the person's word, open with `STOP:` a reply that carries a `LEDGER` block, or that answers a reply the ledger hook sent back, and ask the person; a reply that shows a Case or a round of `case-guppi` carries no `LEDGER` block and opens with no `STOP:` line, in the layout that `orchestration.md` sets, since the check of `rule-case-check` notes a line before a showing; and while a `case-guppi` has not answered, end the turn as `orchestration.md` sets it for a Case out (as set in case 992.1). ``
>   - change: `each reason asks for STOP: only on a reply with a LEDGER block; a shown Case or round opens with no STOP: line`
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — STOP: only on a reply with a LEDGER block, a shown Case or round with no STOP: line`
> - [ ] `.guppi/guppi/onward.py`: `ONLY_THE_PERSON` asks for `STOP:` on a reply that carries a `LEDGER` block, or that answers a reply the ledger hook sent back, and says that a reply that shows a Case or a round of `case-guppi` carries no `LEDGER` block and opens with no `STOP:` line, in the layout `vault/wiki/orchestration.md` sets; the module docstring says the same where it describes what each reason adds.
> - [ ] `.guppi/tests/test_onward.py`: a test asserts that `ONLY_THE_PERSON` names the `LEDGER` block, the reply that shows a Case or a round and its missing `STOP:` line, and that `TO_EXIT`, `TO_LOOP` and the reason of `to_out` each end with it; a test runs, after a `prespec` line with a Case still out, a reply that shows a Case with nothing before its heading and no `LEDGER` block through `plan_onward`, which returns no reason, and through `outside_the_list` of `.guppi/guppi/casecheck.py`, which returns None.
> - [ ] read `estimate-prespec-onward-sends-the-agent-on`

> **ratification:**
> ```
> - decision[case 992.1][update][rule-prespec-onward]{ref:rule-prespec-onward}{supersedes:case 990}
> - decision[case 992.1][update][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}{supersedes:case 990}
> ```

### Case 992.2 — An acknowledging reply that waits for the person opens with STOP:

> **given:**
> `rule-orchestration`: its `## The acknowledging reply` sets the parts of that reply and their order.
> **＋** `estimate-orchestration-acknowledging-reply`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the Render of `rule-orchestration`, which the main agent reads.
> **＋** `rule-prespec-onward`: the hook that lets a reply after `/pre-spec` end when it opens with `STOP:`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier the reply shows.
> **＋** `rule-ledger-write`: the ledger hook that writes the `LEDGER` block.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: sets the decision line the ledger hook holds.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block, before which stands only the `STOP:` line of a reply that waits for the person's word after `/pre-spec`. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply.
> **＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
> **＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** But a reply after `/pre-spec` that waits for the person's word, such as one that acknowledges some Cases while another Case shown waits for the person, opens with a line that opens with `STOP:`, puts the `LEDGER` block right after that line, and ends with its question to the person, so that the hook lets it end.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; ``
>   - new: `` The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first, before which stands only the `STOP:` line of a reply that waits for the person's word after `/pre-spec`, as set below; ``
>   - old: `` after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8); ``
>   - new: `` after `/pre-spec`, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8); but a reply after `/pre-spec` that waits for the person's word, such as one that acknowledges some Cases while another Case shown waits for the person, opens with a line that opens with `STOP:`, puts the `LEDGER` block right after that line and ends with its question to the person, so that the hook lets it end (as set in case 992.2); ``
>   - change: `an acknowledging reply after /pre-spec that waits for the person opens with STOP:, the LEDGER block right after it`
> - [ ] update `estimate-orchestration-acknowledging-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — after /pre-spec, a reply that waits for the person opens with STOP:, the LEDGER block right after it`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-acknowledging-reply`

> **ratification:**
> ```
> - decision[case 992.2][update][rule-orchestration]{ref:rule-orchestration}{supersedes:case 990}
> - decision[case 992.2][update][estimate-orchestration-acknowledging-reply]{ref:rule-orchestration}{supersedes:case 990}
> ```
