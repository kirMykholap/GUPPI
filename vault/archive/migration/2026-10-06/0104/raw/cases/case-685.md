## Case 685 — The ledger hook reminds the agent of the mark on a decision line after an unmarked lesson

> **context:**
> When a Case of a session fixes the cause of a lesson of the same session, a mark links the two: `{addressed_by:case N}` on a lesson line written after the Case, or `{addresses:<lesson slug>}` on a decision line written after the lesson (case 379). The ledger hook writes the record lines of each reply into the session's ledger. Since case 682.1 it holds once a lesson line with no mark written after a decision line, and asks for the mark. The other order is not checked: a lesson written early in a session, then a Case that fixes it, lands with no `{addresses:...}`, and nothing notices. The librarian then does not link the lesson to its fix, so the Insight built from it stays open (`rule-insights-schema`), and a later session may take up a fixed problem again. Case 682 left this side out by the person's choice, and the handoff of session 2249 carried it on.
> The person chose three things. The hook does not hold the decision lines: it writes every line, then tells the agent. It tells the agent at the end of the same reply, so the agent goes on in the same turn and the person waits for nothing. It tells at every reply that writes decision lines after the lesson, until a mark links it. The agent adds the mark by writing one decision line of the Case again with `{addresses:<lesson slug>}`: the ledger keeps it beside the first line, `generate` takes it for a repeat and changes no page (case 673), and `lift_line` of `guppi/materialize.py` passes its mark to the lesson entry as `addressed_by`, so the way `materialize` links a lesson does not change. Case 685.1 creates `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`, checked by pytest, and updates `rule-ledger-write` and the Render of `rule-orchestration`, whose sentence lets decision lines stand only in the reply that acknowledges ratification. A `defer` line brings no reminder, since a deferred Case fixes no cause (`rule-ratification`). The hook judges which lessons no mark links to a Case by one new function of `guppi/materialize.py` over the ledger lines in their order, beside `marks_without_decision`, the one judgment of the other mark, which the hook already imports. Case 688.7 of this session (`vault/raw/2026-10-06/0104/cases/case-688.md`) makes the same hook hold a decision line that the stored Case does not hold, a `{addresses:<slug>}` mark set aside, so a decision line written again with the mark lands, and a decision line it holds is not written and brings no reminder. Both Cases change the sentence of `rule-orchestration` that names the replies that write decision lines: Case 685.1 turns it into a list of the acknowledging reply and the reply that answers the reminder, and Case 688.7 adds the reply that answers its hold as the third item, by an anchor that starts right after the text Case 685.1 replaces; the hold reply is named by Case 688.7 alone, by the person's choice at `/pre-spec`, so the two texts read as one sentence. In `rule-ledger-write` the anchor of Case 688.7 is the sentence before the one Case 685.1 changes, and the two do not overlap; Case 686 changes another sentence of `rule-orchestration`. The form of a ledger line does not change and the hook refuses no new line, so no old form is kept; until the librarian renders `vault/wiki/orchestration.md`, the hook's own stderr line tells the agent what to write.
> The frame. `estimate-ledger-write-asks-for-the-mark-of-a-lesson` says that the hook asks nothing about a lesson that precedes every decision line, and never asks for `{addresses:...}`; the reminder makes both false, so Case 685.2 replaces its Criterion whole with those two lines changed: the line on a lesson before every decision line now says the hook holds no such line, and the line on `{addresses:...}` now says the hook never holds a decision line and names the new Estimate; the other lines are carried as they stand. Its `purpose` and `method` speak of the hold of a lesson line alone and stand. Some `then` lines of Case 685.2 read like lines of Case 685.1 — the stderr line, the Cases it names, told once, no `hi` and the flag — since both behaviours use the same parts of the hook; they promise two behaviours, the hold of a lesson line and the reminder after a decision line, each checked by its own Estimate. `estimate-ledger-write-lifts` sets the told-once rule the reminder uses, and its line that a refused line does not land stays true, since the reminder refuses no line; it stands. `estimate-ledger-write-refuses-a-mark-with-no-decision-line`, `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-ledger-write-names-the-kind-of-a-user-record` and `estimate-ledger-write-exits-2-on-an-error` speak of other lines and stand. `estimate-orchestration-acknowledging-reply` speaks of the reply that acknowledges a ratification; the reply that answers the reminder comes after it, so it stands. `rule-prespec-onward` says that the agent answers a refusal of the ledger hook with a reply that writes the refused lines again, and Case 686.2 carries the same into `estimate-prespec-onward-sends-the-agent-on`; the reminder refuses no line and is answered by a marked decision line or by no `LEDGER` block, so neither stands as written, and Case 686 (`vault/raw/2026-10-06/0104/cases/case-686.md`) rewrites both. The other `Stop` hooks of `.claude/settings.json` stand: `guppi onward` follows Retro, where no decision line is written; `guppi ratified` writes a Case again from its stored text after a reply that repeats one of its lines, as at a re-ratification.
> The searches. A Grep of `\{addresses` over `vault/wiki/rules/` printed `rule-case-protocol.md`, a History line, and `rule-materialize.md`, `rule-insights-schema.md` and `rule-ratification.md`, whose sentences on the mark stay true and stand; over `guppi/` it printed `ledger.py`, whose docstring says the mark is not judged and enters Case 685.1, and `materialize.py`, which stands. A Grep of `refusal of the ledger hook|ledger hook refuses|ledger hook refused` over `vault/wiki/rules/` and `.claude/` printed `rule-ratification.md`, `rule-retro.md`, `rule-retro-onward.md`, `rule-prespec-onward.md`, `rule-session.md`, `rule-orchestration.md`, `rule-ledger-write.md` and `.claude/skills/retro/SKILL.md`: the hits in `rule-retro`, its skill and `rule-retro-onward` speak of the reply after Retro, where no decision line brings a reminder; `rule-prespec-onward` is left to Case 686, as said above; `rule-ratification` and `rule-session` name other refusals; the hits in `rule-ledger-write` and the second hit of `rule-orchestration` are History lines. A Grep of `only in the reply that acknowledges` over `vault/wiki/` printed `orchestration.md` and `rule-orchestration.md`: the Render enters Case 685.1, and the file follows at the render. A Glob of `vault/**/*reminds-of-the-mark*` printed nothing, so the new slug is free.

> **problem:**
> A Case that fixes the cause of a lesson written earlier in the same session can be ratified with no `{addresses:...}` on its decision lines, and nothing tells the agent, so the librarian never links the lesson to its fix.

> **recommend:**
> - **Where the missing mark on a decision line is caught**
>   - Recommended: (a) the ledger hook holds the decision lines once and asks.
>   - Answer: no hold by the hook. The hook should look at the reply and tell the agent after the lines are written. The person does not want the agent to stop to work out whether to mark the lesson again, and asked whether the agent stops or goes on.
> - **When the agent hears about a possible missing mark**
>   - Recommended: (a) at the end of the same reply, after the lines are written.
>   - Answer: agreed, (a).
> - **Which ratifications bring the reminder**
>   - Recommended: (a) every ratification after the lesson, until a mark links it.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec` the main agent sent back findings, with no word of the person needed: the sentence of `rule-orchestration` left out the reply of Case 688.7; a `－` line of Case 685.1 read as excluding a lesson already in the ledger; the link was judged on two sides with a test instead of by one function; and the context said `rule-prespec-onward` stands.
>   - Taken: the sentence names the acknowledging reply and the reply that answers the reminder; the `－` line names a fresh lesson the same `Stop` holds back or refuses; one function of `guppi/materialize.py` judges the link and the hook imports it; the context leaves `rule-prespec-onward` to Case 686, and `given` names the case files of Cases 686 and 688.
> - **Change**
>   - Asked: the confirming check of `/pre-spec` found the reply that answers the hold of Case 688.7 named twice in the sentence of `rule-orchestration`, by both Cases; the person chose that Case 685.1 drops its mention and Case 688.7 keeps its own clause.
>   - Taken: the new text of Case 685.1 names the acknowledging reply and the reply that answers the reminder alone, and the context says the hold reply is named by Case 688.7.

### Case 685.1 — The ledger hook writes the decision lines and reminds of an unmarked lesson

> **given:**
> `rule-ledger-write`: the rule of the ledger hook.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger` that writes the lines and reminds.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `guppi/materialize.py`: the one judgment of the link of a lesson to its Case, which the hook imports.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: the new check of the reminder.
> **＋** `rule-orchestration`: the moment the agent writes a decision line.
> **＋** `vault/raw/2026-10-06/0104/cases/case-688.md`: Case 688.7, which holds a decision line at the same `Stop` and changes the same sentence of `rule-orchestration`.
> **＋** `vault/raw/2026-10-06/0104/cases/case-686.md`: Case 686, which rewrites what `rule-prespec-onward` says of the answer to a refusal of the ledger hook.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line stands before them, in the session's ledger or among the lines the same `Stop` writes, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

> **then:**
> The hook writes every line of the `Stop` as it would without the reminder, and holds back no line for the mark.
> **＋** After the write, for each such lesson the hook exits 2 and prints: "ledger: lesson[<slug>] has no mark — did case <N> or case <M> fix its cause? Then write the decision line of the Case or sub-case that fixed it again with {addresses:<slug>} added, alone in a LEDGER block; otherwise go on without it."
> **＋** The Cases the stderr line names are those of the fresh decision lines after the lesson, in the order first seen.
> **＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
> **＋** A decision line written again with `{addresses:<slug>}` lands beside the first line, the hook reminds of that lesson no more, and `guppi materialize` gives the lesson entry `addressed_by`.
> **＋** The hook judges which lessons no mark links to a Case by one function of `guppi/materialize.py`, over the ledger lines in their order.
> **－** A lesson that carries `{addressed_by:...}`, that a decision line after it marks, or that stands after every fresh decision line brings no reminder; nor does a fresh lesson line that the same `Stop` holds back or refuses.
> **－** A `defer` line, and a decision line from an earlier text of the transcript, bring no reminder.
> **－** A session with no `hi` gets no reminder. With `stop_hook_active` set and a transcript the hook cannot read, the lines land and the hook prints nothing.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1). ``
>   - new: `` It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1). It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and then reminds the agent once a stretch: the Case that fixed the cause writes one of its decision lines again with `{addresses:<lesson slug>}` (case 685.1). ``
>   - change: `the hook writes the decision lines after an unmarked lesson and reminds the agent of the addresses mark (case 685.1)`
> - [ ] create `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session, then reminds the agent once a stretch of the addresses mark, and stops once a decision line carries it`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] update `rule-orchestration`
>   - old: `` Write the `- decision[...]` lines only in the reply that acknowledges ratification; ``
>   - new: `` Write the `- decision[...]` lines only in the reply that acknowledges ratification, in the reply that answers the ledger hook's reminder of a lesson with no mark, which, when a Case of the reply fixed the cause, holds only a `LEDGER` block with one decision line of that Case or sub-case written again with `{addresses:<lesson slug>}`, and otherwise no block (case 685.1); ``
>   - change: `the reply that answers the ledger hook's reminder writes one decision line again with the addresses mark (case 685.1)`
> - [ ] `guppi/materialize.py`: beside `marks_without_decision`, one function judges over ledger lines in their order which lesson lines no mark links to a Case — no `{addressed_by:...}` on the line and no decision line after it with `{addresses:<slug>}` — each line read by `parse_line`.
> - [ ] `guppi/ledger.py`: a function takes, from that function of `guppi/materialize.py` over the session's ledger followed by the lines the `Stop` writes, each unlinked lesson that fresh decision lines of the reply just finished follow; `run` writes the lines first, then prints its reminder by `untold`, and the docstring says so.
> - [ ] `tests/test_ledger.py`: tests of the reminder after the write, of the Cases it names, of the repeat told once, of the decision line written again with the mark, of a `defer` line, of a lesson after every decision line, of a lesson already marked, of a fresh lesson the same `Stop` holds back, without `hi` and with the flag and an unreadable transcript.
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`

> **ratification:**
> ```
> - decision[case 685.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 685.1][create][estimate-ledger-write-reminds-of-the-mark-on-a-decision-line]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> - decision[case 685.1][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 685.2 — The hold of a lesson leaves the decision line to the reminder

> **given:**
> `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: its Criterion is replaced whole.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger` that holds a lesson line.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: the check of the reminder on a decision line.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did case <N> or case <M> fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
> **＋** The Cases the stderr line names are those whose decision lines stand before the lesson line, in the order first seen.
> **＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook holds no lesson line that precedes every decision line of the session, no line it refuses for its prefix or cannot parse, and no line that the ledger of some session already holds.
> **－** The hook never holds a decision line for its `{addresses:...}`: it writes it, and the reminder after the write is `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`.
> **－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

> **tasks:**
> - [ ] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a decision line after an unmarked lesson is written and left to the reminder (case 685.2)`
> - [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`

> **ratification:**
> ```
> - decision[case 685.2][update][estimate-ledger-write-asks-for-the-mark-of-a-lesson]{ref:rule-ledger-write}
> ```
