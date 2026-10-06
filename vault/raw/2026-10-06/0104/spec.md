<!-- approved 03:57:23 · session d769de32 -->

# Spec — session 0104, 2026-10-06

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

```then
create:
- slug: estimate-ledger-write-reminds-of-the-mark-on-a-decision-line
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session, then reminds the agent once a stretch of the addresses mark, and stops once a decision line carries it
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: 'It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1).'
    new: 'It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1). It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and then reminds the agent once a stretch: the Case that fixed the cause writes one of its decision lines again with `{addresses:<lesson slug>}` (case 685.1).'
  change: the hook writes the decision lines after an unmarked lesson and reminds the agent of the addresses mark (case 685.1)
- slug: rule-orchestration
  replace:
  - old: Write the `- decision[...]` lines only in the reply that acknowledges ratification;
    new: Write the `- decision[...]` lines only in the reply that acknowledges ratification, in the reply that answers the ledger hook's reminder of a lesson with no mark, which, when a Case of the reply fixed the cause, holds only a `LEDGER` block with one decision line of that Case or sub-case written again with `{addresses:<lesson slug>}`, and otherwise no block (case 685.1);
  change: the reply that answers the ledger hook's reminder writes one decision line again with the addresses mark (case 685.1)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] create `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
- [ ] update `rule-orchestration`
- [x] `guppi/materialize.py`: beside `marks_without_decision`, one function judges over ledger lines in their order which lesson lines no mark links to a Case — no `{addressed_by:...}` on the line and no decision line after it with `{addresses:<slug>}` — each line read by `parse_line`.
- [x] `guppi/ledger.py`: a function takes, from that function of `guppi/materialize.py` over the session's ledger followed by the lines the `Stop` writes, each unlinked lesson that fresh decision lines of the reply just finished follow; `run` writes the lines first, then prints its reminder by `untold`, and the docstring says so.
- [x] `tests/test_ledger.py`: tests of the reminder after the write, of the Cases it names, of the repeat told once, of the decision line written again with the mark, of a `defer` line, of a lesson after every decision line, of a lesson already marked, of a fresh lesson the same `Stop` holds back, without `hi` and with the flag and an unreadable transcript.
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
```

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

```then
update:
- slug: estimate-ledger-write-asks-for-the-mark-of-a-lesson
  set:
    status: pending
  change: the Criterion replaced whole — a decision line after an unmarked lesson is written and left to the reminder (case 685.2)
```

```tasks
- [ ] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
- [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
```

## Case 686 — The hook of Plan Mode tells the loop after the findings from its end

> **context:**
> The `Stop` hook `uv run guppi onward --plan` sends the agent on in Plan Mode where no person is needed. It acts at a reply that carries a `LEDGER` block, when no line under `## Cases` of the Frontier is open and no Case is out. Before `/pre-spec` it sends the agent to `/pre-spec`. After it, it says that the Cases built again on the findings are ratified, and sends the agent to the check and the exit. It cannot see whether the loop after the findings has started. So any reply with a `LEDGER` block after `/pre-spec` gets that message, a defer or a lesson in answer to the report too. At the `/pre-spec` of session 0109 the hook said so after the reply of the defer 643, before any Case had gone back to its `case-guppi`. Case 648 put the page `rule-prespec-onward` off on this; its `deferred_by` names `decision-case-648`, so a decision line of Case 686.1 that names the page carries `{supersedes:case 648}`.
> The person chose three things. The hook reads the files under `cases/`: after `/pre-spec`, it sends the agent to the check and the exit only when a Case file was written after the last `prespec` line and no Case is out; when no file was written after that line, it sends the agent on with the loop, to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to the check and the exit. The `/pre-spec` skill, the Render of `rule-prespec`, gains a sentence on what the hook says inside the loop; Case 687, the other item of the batch, closes its Insight with no change of the skill, so the two Cases do not meet there. The new judgment gets its own Estimate, `estimate-prespec-onward-tells-the-loop-from-its-end`, in Case 686.1, and Case 686.2 replaces the Criterion of `estimate-prespec-onward-sends-the-agent-on`, whose line on the reason after `/pre-spec` the change makes false.
> The frame. The time of the `prespec` line is a second reading of the line that `window` of `guppi/prespec.py` finds, so both take it from one function there. The `purpose` of `estimate-prespec-onward-sends-the-agent-on` names only the check and the exit after `/pre-spec`, so Case 686.2 sets it anew; its `method` asks for a reading by hand at a Plan Mode that closes its last Case, which in this session reads the old hook, since the code lands in Work Mode, so it is set to the tests alone, which run in this session (case 670.4); the new Estimate is read the same way. Its exception on an error of the hook keeps its advice, which already holds only when no Case is left open. `estimate-prespec-onward-reads-the-decisions-of-the-session` judges whether a Case is out, which does not change; it stands. The other `Stop` hooks of `.claude/settings.json` stand: `guppi ledger` writes the lines before this hook judges them, and Case 685 adds its reminder at the same `Stop`, which this Case does not touch; `guppi ratified`, `guppi casecheck` and `guppi context` judge other things of the reply; `guppi onward` follows Retro.
> The ledger hook sends a reply back in three ways now: a line it refuses, the reminder of a lesson with no mark that Case 685.1 adds, and the hold of a decision line that the stored Case does not hold, which Case 688.7 adds. The page `rule-prespec-onward` and the Criterion of `estimate-prespec-onward-sends-the-agent-on` said that the agent answers each refusal by writing the refused lines again, which the reminder does not fit, since it is answered by a decision line written again with its mark or by no `LEDGER` block. So Case 686.1 rewrites those sentences of the page, and Case 686.2 does not carry the line of the Criterion on when its own refusal is spent as it stood: it writes it anew, its first sentence kept and its second fitted to the three ways, as it writes anew the line on the reason after `/pre-spec`; `spent` already counts any exit 2 of the ledger hook as its refusal, so the code does not change for it. A pre-spec finding on this Case asked for the fix; the `context` of Case 685 says that `rule-prespec-onward` stands, and that claim goes to its own builder. Case 688.7 changes another sentence of `rule-orchestration` than this Case, and the two new texts do not touch. The judgment of this Case leans on the condition that no Case is out, which `estimate-prespec-onward-reads-the-decisions-of-the-session` sets: a decision line in a `LEDGER` block of a reply counts there, a line that Case 688.7 holds too. That Estimate stands, as the `context` of Case 688 says: a Case is out only until the person ratifies it, the reply that carries a held line acknowledges that ratification, and the held line is a wrong copy that the ledger hook refuses at the same `Stop`, so this hook sends the agent on again after the line is written again. No Estimate and no `then` line of this Case changes for it.
> The searches. A Grep of `rule-prespec-onward` over `vault/wiki/` printed `brief.md`, `backlog.md` and `log.md`, not read, and `orchestration.md`, `rule-orchestration.md`, `rule-prespec.md`, `rule-plan-mode.md`, `estimate-prespec-confirms-the-findings-once.md`, `estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `estimate-prespec-onward-sends-the-agent-on.md`, `estimate-orchestration-defers-in-one-reply.md`, `estimate-prespec-onward-reads-the-decisions-of-the-session.md`, `estimate-orchestration-acknowledging-reply.md` and `estimate-orchestration-shows-the-frontier-after-a-closed-line.md`. The sentence of `rule-orchestration` on the defer reply says the hook sends the agent on to `/pre-spec`, which a defer after `/pre-spec` makes false, so Case 686.1 changes it; Case 685 changes another sentence of that page, and the two new texts do not touch. `orchestration.md` follows at the render. The sentence of `rule-prespec` enters Case 686.1. `rule-plan-mode` names the page as a child. The other sentences of `rule-orchestration` and the three Estimates of orchestration say only that the hook sends the agent on, and `estimate-prespec-confirms-the-findings-once` says it sends the agent to the check and the exit after the ratification of the Cases built again; all stay true and stand. `estimate-retro-onward-sends-the-agent-to-the-handoff` says the hook keeps its own judgment; it stands. A Grep of `rule-prespec-onward` over `guppi/`, `tests/` and `.claude/` printed `.claude/skills/pre-spec/SKILL.md`, which follows at the render, `guppi/prespec.py`, whose docstring names the open lines the hook waits on and stands, and `guppi/onward.py`, whose docstring enters Case 686.1. A Glob of `vault/**/*tells-the-loop*` printed nothing, so the new slug is free.

> **problem:**
> After `/pre-spec`, the hook of `rule-prespec-onward` tells the agent that the Cases built again on the findings are ratified at any reply with a `LEDGER` block, before any Case has gone back to be built again, and sends it to the exit of Plan Mode.

> **recommend:**
> - **How the hook tells the start of the loop after the findings from its end**
>   - Recommended: (a) look for files of rebuilt Cases: the check and the exit only when a Case file was written after the `/pre-spec` run and every such Case is ratified; otherwise on with the loop.
>   - Answer: agreed, (a).
> - **Where this Case stops beside the item on the loop after the findings**
>   - Recommended: (a) only the hook, its rule page and its checks; the text of the `/pre-spec` skill left to the other item.
>   - Answer: (b) the hook and one sentence of the `/pre-spec` skill on what the hook says inside the loop.
> - **What checks the new judgment of the hook**
>   - Recommended: (b) a new check for the new judgment, and the line of `estimate-prespec-onward-sends-the-agent-on` on the message after `/pre-spec` rewritten to point to it; two sub-cases.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: bring the `context` in line with Case 688 on `estimate-prespec-onward-reads-the-decisions-of-the-session`: the Estimate stands, for the reason Case 688 gives; no Estimate and no `then` line changes.
>   - Taken: the `context` says that the Estimate stands and gives that reason; nothing else changed.

### Case 686.1 — The hook sends the agent on with the loop until a Case is built again

> **given:**
> `rule-prespec-onward`: the rule of the hook.
> **＋** `guppi/onward.py`: the `Stop` hook `uv run guppi onward --plan`.
> **＋** `guppi/prespec.py`: the judgment of the `prespec` line of the event log.
> **＋** `tests/test_onward.py`: the tests of the hook.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the new check of the judgment.
> **＋** `rule-prespec`: the `/pre-spec` skill, which names the hook after the loop.
> **＋** `rule-orchestration`: the defer reply, which names the hook.
> **＋** `vault/raw/2026-10-06/0104/cases/case-685.md`: Case 685, which changes another sentence of `rule-orchestration` and adds a reminder at the same `Stop`.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the files of the Cases of the session, whose times the hook reads.
> **＋** `vault/raw/2026-10-06/0104/cases/case-688.md`: Case 688, whose Case 688.7 makes the ledger hook hold a decision line and changes another sentence of `rule-orchestration`.

> **when:**
> The `Stop` hook `uv run guppi onward --plan` of `guppi/onward.py` receives the end of a reply of the main agent that carries a `LEDGER` block, the event log holds a `prespec` line of this session after its `hi`, and every other condition holds under which the hook sends the agent on.

> **then:**
> When a file under `raw/<date>/<hi HHMM>/cases/` was written after the last `prespec` line of the session, the hook exits 2 and tells the agent that the Cases built again on the findings of `/pre-spec` are ratified, to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
> **＋** When no file under `cases/` was written after that line, the hook exits 2 and tells the agent to go on with the loop after the findings of `/pre-spec`: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit as above.
> **＋** The hook reads the time of the `prespec` line, on the date of the event log that holds it, through the one function of `guppi/prespec.py` that `window` uses to find the line.
> **－** A reply that writes a defer or a lesson after `/pre-spec` and before any Case is built again never gets the message that the Cases built again are ratified.
> **－** A Case built again and not yet ratified keeps the hook silent, as before.

```then
create:
- slug: estimate-prespec-onward-tells-the-loop-from-its-end
  ref: rule-prespec-onward
  kind: QA
  purpose: Whether guppi onward --plan, after /pre-spec, sends the agent to the check and the exit only when a file under cases/ was written after the last prespec line of the session, and on with the loop after the findings when none was
  method: uv run pytest tests/test_onward.py — piped payloads, an event log with a prespec line and files under cases/ in a temp vault
  tags:
  - session
  - workflow
  - hooks
  - harness
update:
- slug: rule-prespec-onward
  replace:
  - old: the files under `cases/` against the times of the decision lines
    new: the files under `cases/` against the time of the last `prespec` mark (case 686.1) and the times of the decision lines
  - old: With no `prespec` line it sends the agent to `/pre-spec`; with the line it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding.
    new: 'With no `prespec` line it sends the agent to `/pre-spec`. With the line, when a file under `cases/` was written after the last `prespec` mark, it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. When no file under `cases/` was written after that mark, no Case has been built again on the findings yet — the reply wrote a defer or a lesson in answer to the report — and it sends the agent on with the loop after the findings: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit (case 686.1).'
  - old: 'It fires once a stretch, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end.'
    new: 'It fires once a stretch, and once more after each reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark (cases 685.1, 688.7): the agent answers with a reply that writes a line again, a reply that must end; an answer with no `LEDGER` block gets no second reason, since the reason given at the same `Stop` as the ledger hook''s already stands (case 686.1).'
  - old: The ledger hook tells each refused line once a stretch, so the hook cannot loop.
    new: The ledger hook tells each refused or held line and each reminder once a stretch, so the hook cannot loop.
  set:
    implementation_ref:
    - guppi/onward.py
    - guppi/prespec.py
    - guppi/ledger.py
    - guppi/casecheck.py
    - tests/test_onward.py
    - tests/test_ledger.py
    - .claude/settings.json
  change: after /pre-spec the hook sends the agent to the check and the exit only when a Case file was written after the prespec mark, and on with the loop after the findings otherwise; it sends the agent on again after a line the ledger hook held and after its reminder of a lesson with no mark, as after a refused line; the defer of case 648 retired (case 686.1)
- slug: rule-prespec
  replace:
  - old: The hook of `rule-prespec-onward` sends you on after the reply that acknowledges the ratification, and the hook of `rule-prespec-hook` refuses the exit while the check prints a finding (cases 561.3, 561.5).
    new: 'The hook of `rule-prespec-onward` sends you on after the reply that acknowledges the ratification, and the hook of `rule-prespec-hook` refuses the exit while the check prints a finding (cases 561.3, 561.5). A reply with a `LEDGER` block inside the loop before any Case is built again — a defer or a lesson in answer to the report — is sent on by the same hook too: on with the loop, or, when no Case goes back, to the check and the exit (case 686.1).'
  change: the hook of rule-prespec-onward sends the agent on with the loop after a reply with a LEDGER block before any Case is built again (case 686.1)
- slug: rule-orchestration
  replace:
  - old: the hook of `rule-prespec-onward` sends the agent on to `/pre-spec` (case 561.7)
    new: the hook of `rule-prespec-onward` sends the agent on to `/pre-spec`, or, after it, on with the loop after its findings (cases 561.7, 686.1)
  change: a defer after /pre-spec is sent on with the loop after its findings (case 686.1)
```

```tasks
- [ ] update `rule-prespec-onward`
- [ ] create `estimate-prespec-onward-tells-the-loop-from-its-end`
- [ ] update `rule-prespec`
- [ ] update `rule-orchestration`
- [x] `guppi/prespec.py`: one function gives the date and time of the last `prespec` line of the session after its `hi`; `window` finds the line through it.
- [x] `guppi/onward.py`: `plan_onward` sends `TO_EXIT` when a file under `cases/` is newer than that moment, and a new reason that sends the agent on with the loop otherwise; the docstring says so.
- [x] `tests/test_onward.py`: tests of a reply with a `LEDGER` block after `/pre-spec` with no file under `cases/` written after the `prespec` line, with one written after it and ratified, with one written after it and not ratified, with only files older than the line, of a session across midnight, and of the reply after a reminder of the ledger hook with a `LEDGER` block and with none.
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-prespec-onward-tells-the-loop-from-its-end`
```

### Case 686.2 — The check of the hook points to the new judgment after /pre-spec

> **given:**
> `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `guppi/onward.py`: the `Stop` hook `uv run guppi onward --plan`.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the check of the reason after `/pre-spec`.
> **＋** `rule-prespec-onward`: the rule of the hook, which judges whether a Case is out.
> **＋** `guppi/ledger.py`: the judgment of the refusals in the transcript.
> **＋** `.claude/settings.json`: the registration of the hook on `Stop`.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec, whose presence silences the hook.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose open lines silence the hook.

> **when:**
> The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block; no Case is still out, as `rule-prespec-onward` judges it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward --plan`, and the command of the ledger hook is `uv run guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply that carries a `LEDGER` block, the one that writes a line again; an answer with no `LEDGER` block gets no second reason, since its reason at the same `Stop` as the ledger hook's already stands.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** With no `prespec` line of this session after its `hi` in the event log, its reason on stderr tells the agent to call `/pre-spec` now. With that line, its reason sends the agent to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
> **－** An error of its own after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to call `/pre-spec`, or to run the check and exit Plan Mode, when no Case is left open. It does so at most once a stretch, judged by its own refusal in the stretch alone. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run guppi onward` without `--plan` keeps its own judgment.

```then
update:
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    status: pending
    purpose: Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec, or after it to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise
    method: uv run pytest tests/test_onward.py tests/test_ledger.py, which cover a refusal of the ledger hook
  change: the Criterion replaced whole — after /pre-spec the reason sends the agent to the check and the exit, or on with the loop, as estimate-prespec-onward-tells-the-loop-from-its-end sets it; purpose and method set anew (case 686.2)
```

```tasks
- [ ] update `estimate-prespec-onward-sends-the-agent-on`
- [ ] read `estimate-prespec-onward-sends-the-agent-on`
```

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

```then
update:
- slug: insight-prespec-after-findings-loop-unruled
  set:
    status: actioned
    addressed_by: decision-case-687
  change: 'actioned again: the skill of rule-prespec sets the loop after the findings (cases 561.2, 595.1, 634.2); the report lists what the one ask-guppi run did not check and the person kept one run (cases 674.1, 675); the confirmation message asks only whether each finding is closed (case 638) (case 687)'
```

```tasks
- [ ] update `insight-prespec-after-findings-loop-unruled`
```

## Case 688 — The checks catch a showing and a ledger line copied wrong after a refusal

> **context:**
> `case-guppi` writes a Case into its file. The main agent sends the file to the person and writes in the chat a heading, a short list and the ledger lines, copied by hand from the summary of `case-guppi`. The `Stop` hook `uv run guppi casecheck` compares those lines with the Case the check of `rule-case-check` stored, and refuses a reply where they differ. It skips its whole run while `stop_hook_active` is set, and Claude Code keeps that flag set from a refusal of any `Stop` hook until the person's next message (case 644.1). So the showing written again after a refusal is not checked, and a second wrong copy reaches the person; only the Spec hook compares it again, at ratification. When the person ratifies, the agent copies the decision lines into its `LEDGER` block again, and `uv run guppi ledger` writes them as they stand: no hook compares them with the stored Case, though `generate` takes the ref and the tags of a `create` from that line. `insight-case-show-built-case-retyped-by-hand` names this. Case 452.4 put the Case into a file the agent sends, and case 662 gave the heading a name line that the check compares with the file, so a whole retyped Case and a heading of the agent's own are gone; the copied ledger lines are what is left.
> The person chose that the check of a showing stops trusting the flag (Q1), that the decision lines of the acknowledging reply come into this Case (Q2), and the recommended answer of each of Q3–Q7. The person also asked whether the agent could show the ledger lines first, in a reply of their own, so that a wrong line is caught before the rest; told that a `Stop` hook runs only at the end of a turn and that a showing is already short, the person dropped it. Case 688.1 makes the whole `Stop` run of `guppi casecheck` judge every reply, its loop guarded by its own refusals in the transcript as the Spec hook guards its own (case 644.8), with a limit of three per Case; it creates `estimate-case-check-judges-a-showing-after-a-refusal`. Cases 688.2 to 688.6 replace the Criterion of each Estimate of `rule-case-check` whose line says the run exits 0 on the re-fire; each new Criterion carries the old lines but that one, and the line of 688.4 on an error that blocks at every `Stop`, which the limit makes false. Their `then` lines share words with each other and with 688.1, since the five Estimates already shared them and each promises a part of one run; each stays its own Estimate. Case 688.7 makes the ledger hook hold a decision line that is not a line of the stored `ratification`, every time, and creates `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`. Case 688.8 sets the Insight `actioned`; `estimate-backlog-renders` checks it, since its Criterion lists an Insight under `## Deferred` only while it is `open`, and it stands.
> The frame. Case 685 changes the same ledger hook at the same `Stop`: it reminds the agent of a lesson with no mark after the hook writes fresh decision lines, and asks for a decision line written again with `{addresses:<lesson slug>}`. Case 688.7 sets that mark aside before it compares, so the line the reminder asks for lands; a held line is not written, so it brings no reminder, as the `when` of Case 685.1 reads. Case 685.1 replaces another sentence of `rule-ledger-write` than Case 688.7 does. In `rule-orchestration` it turns the sentence on where decision lines are written into a list of the acknowledging reply and the reply that answers its reminder; Case 688.7 adds the reply that answers a hold as the third item of that list, by an anchor that starts right after the text Case 685.1 replaces, so the two texts read as one list whichever applies first. At `/pre-spec` both Cases named that reply; by the person's choice the clause of Case 688.7 is the one place that names it, and Case 685.1 drops its mention, so the sentence names it once. Case 688.7 also changes the sentence of the same paragraph that says the ledger hook has written the block when another `Stop` hook refuses, since a held line is not written, and Case 688.9 replaces the Criterion of `estimate-orchestration-acknowledging-reply`, whose line says the same. Case 686 changes another sentence of `rule-orchestration`, and its hook `guppi onward --plan` sends the agent on again after a reply the ledger hook refused, which a hold is. `estimate-prespec-onward-reads-the-decisions-of-the-session` counts the decision lines of each reply in the transcript, a held line too; it stands, since a Case is out only until the person ratifies it, and the reply that carries a held line acknowledges that ratification; the held line is a wrong copy, which the ledger hook refuses at the same `Stop`, so Case 686 needs no change. The Estimates of `rule-ledger-write`, judged against Case 688.7: `estimate-ledger-write-lifts` keeps a refused line out while its refusal holds and tells each refused line once a stretch, which the hold keeps, and stands. `estimate-ledger-write-refuses-a-line-it-cannot-read` says a line `parse_line` cannot read gets no other refusal; Case 688.7 compares only a line `parse_line` reads, so it stands. `estimate-ledger-write-exits-2-on-an-error` covers an error while the hook judges the lines, the comparison included, and stands. `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` speaks of `estimate[...]` lines, `estimate-ledger-write-names-the-kind-of-a-user-record` of the records of the transcript, and `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-ledger-write-refuses-a-mark-with-no-decision-line` and `estimate-ledger-write-asks-for-the-mark-of-a-lesson` of lesson lines; none of them speaks of a decision line it would write, and they stand. The `purpose` of `estimate-case-check-shows-only-the-checked-case` and the `purpose` field of `rule-case-check` state that a wrong showing is never shown, which the limit of three makes false, so Cases 688.2 and 688.1 set them anew. `estimate-case-check-sends-back-a-faulty-case` speaks of the `--subagent` run, which keeps its guard; it stands. The store and the ledger lines keep their form, so no reader needs an old form kept.
> The searches. A Grep of `re-fire|stop_hook_active` over `vault/wiki/estimates/` with the glob `estimate-case-check-*.md` printed `estimate-case-check-refuses-a-changed-case-file.md`, `estimate-case-check-sends-back-a-faulty-case.md`, `estimate-case-check-exits-2-on-an-error.md`, `estimate-case-check-refuses-text-before-a-round.md`, `estimate-case-check-refuses-text-outside-the-list.md` and `estimate-case-check-shows-only-the-checked-case.md`; all but the second enter this Case. The same pattern over `vault/wiki/rules/` printed `rule-prespec-onward.md`, `rule-retro-onward.md`, `rule-case-check.md`, `rule-ledger-write.md` and `rule-spec-write.md`: the hits in `rule-case-check` and `rule-ledger-write` are History lines, and the others speak of their own hooks and stand. Over `.claude/` it printed nothing, so no harness file says the check of a showing is silent after a refusal. A Grep of `ledger hook (refuses|holds)|the hook refuses and says so` over `vault/wiki/rules/` printed `rule-ledger-write.md`, a History line, and `rule-orchestration.md`, `rule-ratification.md` and `rule-session.md`, whose sentences name other refusals or a refusal by another hook, and stand; two other sentences of the paragraph of `rule-orchestration` that holds the hit enter Case 688.7. A Grep of `insight-case-show-built-case-retyped-by-hand` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 7 files: `brief.md`, `backlog.md` and `log.md`, not read; the two lessons, whose `insight` field stays true; and `estimate-synthesis-clusters.md` and `estimate-synthesis-keeps-actioned-by-the-mark.md`, whose hits stand in `## Result`, a past reading. A Glob of `vault/**/*after-a-refusal*` and of `vault/**/*off-the-stored-case*` printed nothing, so both new slugs are free.

> **problem:**
> A showing copied wrong a second time, after the check of a showing refused the first, reaches the person unchecked, and a decision line copied wrong into the acknowledging reply lands in the ledger, where pages are made from it.

> **recommend:**
> - **What this Case changes about the copied showing**
>   - Recommended: (b) the showing check stops trusting the flag: it runs on every reply and guards its loop by its own refusals in the transcript, as the Spec hook does.
>   - Answer: (b). The person added that the person seeing a wrong version first cannot be avoided, and asked whether the agent could show the ledger lines first, in a reply of their own; after the answer that a check runs only at the end of a turn, the person said no separate question on it is needed.
> - **Whether the ledger lines written when you ratify come into this Case**
>   - Recommended: (a) leave them out.
>   - Answer: (b) bring them in.
> - **How often the showing check refuses the same wrong showing**
>   - Recommended: (b) up to three times for the same Case since the person's last message, then let it through with a line that says it is unchecked.
>   - Answer: agreed, (b).
> - **Which parts of the end-of-reply check stop trusting the flag**
>   - Recommended: (a) all four: the comparison, the sending of the file, the layout of a showing and the opening of a round.
>   - Answer: agreed, (a).
> - **How often the ledger hook holds back a wrong decision line**
>   - Recommended: (b) every time it is still wrong.
>   - Answer: agreed, (b).
> - **What the ledger comparison sets aside**
>   - Recommended: (a) an added lesson mark and the lines that put a decision off; a line of a Case with no stored text is held.
>   - Answer: agreed, (a).
> - **How the work is split and checked**
>   - Recommended: (a) sub-cases, a new check for each hook.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec` the sentence of `rule-orchestration` on where decision lines are written named the reply that answers a hold twice, in Case 685.1 and in Case 688.7; the person chose that Case 685.1 drops its mention and Case 688.7 keeps its clause.
>   - Taken: the clause of Case 688.7 stays as written, its anchor apart from the text of Case 685.1, and the context says it is the one place that names that reply.

### Case 688.1 — The check of a showing judges every reply and stops after three refusals

> **given:**
> `rule-case-check`: the rule of the check of a Case and of its showing.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck`.
> **＋** `tests/test_casecheck.py`: the tests of the hook.
> **＋** `guppi/ledger.py`: the reading of the stretch and of the refusals of a `Stop` hook.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the new check of the loop guard.
> **＋** `<plan>.checked.json`: the store of the Cases `case-guppi` built.

> **when:**
> The `Stop` hook `uv run guppi casecheck` of `guppi/casecheck.py` fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, whose file was not sent or differs from the store, a text of the agent's own outside the list of a showing or before a round, or an error of its own after it read the payload.

> **then:**
> The hook judges the reply the same whether `stop_hook_active` is set or not.
> **＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
> **＋** It exits 2 while a reason is left to give, with those reasons on stderr.
> **＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi casecheck]: `, judged by the function of `guppi/ledger.py` that `guppi onward` calls.
> **－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
> **－** The run `uv run guppi casecheck --subagent` keeps its own guard, the store.

```then
create:
- slug: estimate-case-check-judges-a-showing-after-a-refusal
  ref: rule-case-check
  kind: QA
  purpose: Whether the Stop run of the Case check judges a reply after a refusal of any Stop hook as before it, gives a reason of one Case at most three times since the person's last message, and then lets the reply through with a line on stderr
  method: uv run pytest tests/test_casecheck.py — piped payloads and transcripts with refusals of the hook in a temp vault
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: the person judges the text (cases 449, 537).
    new: 'the person judges the text (cases 449, 537). The `Stop` run judges every reply whether `stop_hook_active` is set or not, since Claude Code keeps the flag set from a refusal of any `Stop` hook until the person''s next message, and guards its own loop by its refusals in the transcript since that message: a reason of one Case is given at most three times, and a showing still wrong after that passes with a line on stderr, the Spec hook comparing it at ratification (case 688.1).'
  - old: or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them, a round
    new: or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own, a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
  change: the Stop run judges every reply whatever stop_hook_active says, a reason of one Case given at most three times a stretch; purpose set anew (case 688.1)
```

```tasks
- [ ] update `rule-case-check`
- [ ] create `estimate-case-check-judges-a-showing-after-a-refusal`
- [x] `guppi/casecheck.py`: `stop` no longer returns at `stop_hook_active`; it reads its own refusals in the stretch by `refusals` of `guppi/ledger.py` and keeps each reason under the count; the error path of `run` keeps the same count; the docstring says so.
- [x] `tests/test_casecheck.py`: tests of a showing refused after a refusal of another `Stop` hook, of the same wrong showing refused three times and let through the fourth time with its stderr line, of two Cases counted apart, of a reason with no Case, of an error repeated, and of the flag with an unreadable transcript; the tests of the re-fire changed to the count.
- [ ] read `estimate-case-check-judges-a-showing-after-a-refusal`
```

### Case 688.2 — The comparison of a showing runs after a refusal

> **given:**
> `estimate-case-check-shows-only-the-checked-case`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck`.
> **＋** `guppi/ratified.py`: the Spec hook, which imports the comparison.
> **＋** `<plan>.checked.json`: the store of the Cases `case-guppi` built.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a top-level Case of the session.
> **＋** `estimate-case-check-refuses-a-changed-case-file`: the check of the file of a shown Case.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
> **＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
> **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the stored text and `raw/<date>/<hi HHMM>/cases/case-<N>.md` equals the store, as `estimate-case-check-refuses-a-changed-case-file` sets it.
> **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
> **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, a Case whose file differs from the store, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
> **－** With `stop_hook_active` set the comparison runs the same, so a Case shown again after a refusal is compared again; its reasons are given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.

```then
update:
- slug: estimate-case-check-shows-only-the-checked-case
  set:
    status: pending
    purpose: Whether the Stop check refuses a showing of a Case that differs from the answer of case-guppi or that the checks did not pass, after a refusal of any Stop hook too, while fewer than three refusals of that Case stand since the person's last message
  change: the Criterion replaced whole — the comparison runs whatever stop_hook_active says, its reasons given as the loop guard sets it; purpose set anew (case 688.2)
```

```tasks
- [ ] update `estimate-case-check-shows-only-the-checked-case`
- [ ] read `estimate-case-check-shows-only-the-checked-case`
```

### Case 688.3 — The check of the file of a shown Case runs after a refusal

> **given:**
> `estimate-case-check-refuses-a-changed-case-file`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its one comparison of a file with the store.
> **＋** `guppi/ratified.py`: the Spec hook, which imports that comparison.
> **＋** `guppi/materialize.py`: the reading of the Cases of a file.
> **＋** `<plan>.checked.json`: the store of the Cases `case-guppi` built.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a top-level Case of the session.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, and `uv run guppi casecheck` reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook reads the Cases of that file by `split_cases` of `guppi/materialize.py` and compares each with the entry of the store under its id alone, line ends and trailing spaces aside.
> **＋** A Case of the file whose text differs from its entry, or that the store does not hold, exits 2 with a reason that names the Case and the file, joined with the other reasons of the hook.
> **＋** The comparison is one function of `guppi/casecheck.py`, which the Spec hook `guppi/ratified.py` imports.
> **－** A heading with no section, a fence tagged `DIFF` and a deferred decision in the short form are not compared, and no file is read for them.
> **－** With `stop_hook_active` set the file is compared the same, as by the other checks of the same run, and its reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.

```then
update:
- slug: estimate-case-check-refuses-a-changed-case-file
  set:
    status: pending
  change: the Criterion replaced whole — the file is compared whatever stop_hook_active says, its reason given as the loop guard sets it (case 688.3)
```

```tasks
- [ ] update `estimate-case-check-refuses-a-changed-case-file`
- [ ] read `estimate-case-check-refuses-a-changed-case-file`
```

### Case 688.4 — An error of the check of a showing blocks at most three times

> **given:**
> `estimate-case-check-exits-2-on-an-error`: its Criterion is replaced whole, its `purpose` set anew.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its `--subagent` run.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> The `Stop` hook `uv run guppi casecheck` fires, and an exception rises in `guppi/casecheck.py` after the hook has read the payload: while it reads the transcript, the event log or the store, or while it compares a shown Case or reads a sending.

> **then:**
> `guppi casecheck` exits 2. Its stderr holds `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed, so the agent sees the error at the end of that reply.
> **＋** While the cause stands, `guppi casecheck` blocks with the same error at each `Stop`, whether `stop_hook_active` is set or not, until three of its own refusals since the person's last message hold that error; then it exits 0, as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** An empty or unreadable payload of `guppi casecheck` exits 0 with its line on stderr.
> **－** With `stop_hook_active` set and a transcript it cannot read, `guppi casecheck` exits 0 and prints nothing, so it cannot loop.
> **－** The run `uv run guppi casecheck --subagent` on `SubagentStop` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop.
> **－** A refusal of `guppi casecheck` with no error keeps its own reason on stderr and its exit 2.

```then
update:
- slug: estimate-case-check-exits-2-on-an-error
  set:
    status: pending
    purpose: Whether the Stop run of the Case check exits 2 with the error on stderr when it raises after reading the payload, at most three times for one error since the person's last message, and exits 0 on an empty payload and in the --subagent run
  change: the Criterion replaced whole — an error blocks whatever stop_hook_active says, at most three times a stretch; purpose set anew (case 688.4)
```

```tasks
- [ ] update `estimate-case-check-exits-2-on-an-error`
- [ ] read `estimate-case-check-exits-2-on-an-error`
```

### Case 688.5 — The check of how a round opens runs after a refusal

> **given:**
> `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole, its `method` set anew.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its one test of a round.
> **＋** `guppi/ledger.py`: the reading of the person's message and of a returned answer.
> **＋** `/pre-spec`: the skill whose `prespec` line ends the judgment of text before the last tool call.
> **＋** `/hi`: the skill whose `hi` line opens the session's window.
> **＋** `rule-prespec`: the text the main agent writes in the loop after the findings.
> **＋** `.claude/skills/wait-what/SKILL.md`: the re-pitch, which is not judged.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** With `stop_hook_active` set a round shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

```then
update:
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
    method: uv run pytest tests/test_casecheck.py -k round
  change: the Criterion replaced whole — a round shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.5)
```

```tasks
- [ ] update `estimate-case-check-refuses-text-before-a-round`
- [ ] read `estimate-case-check-refuses-text-before-a-round`
```

### Case 688.6 — The check of the layout of a showing runs after a refusal

> **given:**
> `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole, its `method` set anew.
> **＋** `guppi/casecheck.py`: the `Stop` hook `uv run guppi casecheck` and its judgment of the text before the last tool call.
> **＋** `.claude/settings.json`: the registration of the hook on `Stop`.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the check of the loop guard.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

> **then:**
> `uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
> **＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
> **＋** It exits 2 when the main agent wrote text in the turn of the reply before its last tool call, judged by `texts_before_last_call` of `guppi/casecheck.py`, the judgment the check of a round uses.
> **＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with that text moved after the horizontal rule.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
> **－** Text after the horizontal rule is not judged.
> **－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
> **－** With `stop_hook_active` set a Case shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

```then
update:
- slug: estimate-case-check-refuses-text-outside-the-list
  set:
    status: pending
    method: uv run pytest tests/test_casecheck.py
  change: the Criterion replaced whole — a Case shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.6)
```

```tasks
- [ ] update `estimate-case-check-refuses-text-outside-the-list`
- [ ] read `estimate-case-check-refuses-text-outside-the-list`
```

### Case 688.7 — The ledger hook holds a decision line that the stored Case does not hold

> **given:**
> `rule-ledger-write`: the rule of the ledger hook.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger`.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `guppi/casecheck.py`: the store and its reading of the ledger lines of a `ratification`.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the new check of the hold.
> **＋** `rule-orchestration`: what the agent does when the ledger hook refuses.
> **＋** `vault/raw/2026-10-06/0104/cases/case-685.md`: Case 685, which adds a reminder to the same hook at the same `Stop` and the reply that answers it to `rule-orchestration`.
> **＋** `guppi/materialize.py`: the grammar of a ledger line, whose refusal comes first.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a decision line of a kind other than `defer` that no ledger holds yet.

> **then:**
> The hook compares the line, a `{addresses:<slug>}` block and trailing spaces set aside, with the ledger lines of the `ratification` of the entry stored under its Case id alone in `<plan>.checked.json`, read by the function of `guppi/casecheck.py` by which the `Stop` check of a showing reads them.
> **＋** A line equal to one of them lands as before.
> **＋** A line equal to none of them, a line of a Case the store holds no text for, and a line of a session with no plan file is not written; the other lines of the `Stop` land.
> **＋** For such a line of the reply just finished, the hook exits 2 and prints: "ledger: decision[case <N>] not written — it is not a line of the ratification case-guppi stored for case <N>: copy it again as the summary of case-guppi holds it, alone in a LEDGER block, or send the Case back to its case-guppi when the stored line is wrong."
> **＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
> **＋** A held line is judged again at every `Stop` while it stands in a text of the transcript, and never lands while it differs; a line written again that equals a stored line lands.
> **＋** A line written again with `{addresses:<slug>}` added, as Case 685 asks, lands when the line without the mark equals a stored line.
> **－** A `defer` line, an `estimate` line and a `lesson` line are not compared.
> **－** A line that `parse_line` of `guppi/materialize.py` cannot read, and a line the hook refuses while no live sprint page stands, get that refusal alone and are not compared.
> **－** With `stop_hook_active` set the hook judges the line the same; with the flag set and a transcript it cannot read, the line does not land and the hook prints nothing.

```then
create:
- slug: estimate-ledger-write-holds-a-decision-line-off-the-stored-case
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook holds a decision line other than a defer that is not a line of the stored ratification of its Case, an addresses mark set aside, tells the agent once a stretch, and writes it once a copy equal to a stored line stands
  method: uv run pytest tests/test_ledger.py — piped payloads, a session ledger and a store beside a plan file in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3).
    new: so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). It holds a decision line other than a `defer` that is not a line of the `ratification` of the Case `case-guppi` stored for it, a `{addresses:<slug>}` mark set aside, and tells the agent once a stretch to copy it again from the summary of `case-guppi`; the line never lands while it differs, since `generate` takes the ref and the tags of a page from it (case 688.7).
  set:
    implementation_ref:
    - guppi/ledger.py
    - guppi/materialize.py
    - guppi/gate.py
    - guppi/casecheck.py
    - tests/test_ledger.py
    - tests/test_gate.py
    - .claude/settings.json
  change: the hook holds a decision line that is not a line of the stored ratification of its Case, every time it differs (case 688.7)
- slug: rule-orchestration
  replace:
  - old: '`- estimate[...]` and `- lesson[...]` lines the moment'
    new: 'and in the reply that answers the ledger hook''s hold of a decision line that is not a line of the `ratification` of the Case `case-guppi` stored: that reply holds only a `LEDGER` block with the line written again as the summary of `case-guppi` holds it, or, when the stored line itself is wrong, no block, and the Case goes back to its `case-guppi` to be shown and ratified again (case 688.7); `- estimate[...]` and `- lesson[...]` lines the moment'
  - old: the ledger hook has written the block at that same `Stop`
    new: the ledger hook has written the block at that same `Stop`, but for a decision line it holds (case 688.7)
  change: the reply that answers a held decision line copies it again from the summary of case-guppi, and a held line is not written at the Stop that another hook refuses (case 688.7)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] create `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`
- [ ] update `rule-orchestration`
- [x] `guppi/ledger.py`: a function judges each fresh decision line other than a `defer` against the stored `ratification` of its Case, read through `guppi/casecheck.py` inside the function; `run` keeps a held line out and prints its reason by `untold`; the docstring says so.
- [x] `tests/test_ledger.py`: tests of a line equal to the store, of a line that differs, of a Case with no stored text, of no plan file, of a line written again equal, of a line with `{addresses:<slug>}` added, of a `defer` line, of a held line from an earlier text, of the reason told once, and of the flag with an unreadable transcript.
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`
```

### Case 688.8 — The Insight on the retyped showing closes

> **given:**
> `insight-case-show-built-case-retyped-by-hand`: the Insight this Case closes.
> **＋** `rule-insights-schema`: the form of an Insight and of its `actioned` status.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-case-show-built-case-retyped-by-hand` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `clustered` lessons become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.

```then
update:
- slug: insight-case-show-built-case-retyped-by-hand
  set:
    status: actioned
    addressed_by: decision-case-688.8
  change: 'actioned: the check of a showing judges every reply and stops after three refusals of one Case (case 688.1), and the ledger hook holds a decision line that is not a line of the stored ratification (case 688.7); the heading of a showing comes from the checked Case line (case 662) (case 688.8)'
```

```tasks
- [ ] update `insight-case-show-built-case-retyped-by-hand`
```

### Case 688.9 — The acknowledging reply keeps a held decision line out of the ledger

> **given:**
> `estimate-orchestration-acknowledging-reply`: its Criterion is replaced whole.
> **＋** `rule-orchestration`: the reply that acknowledges a ratification.
> **＋** `vault/wiki/orchestration.md`: the Render the agent follows.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier the reply shows.
> **＋** `rule-ledger-write`: the ledger hook, which writes the `LEDGER` block.
> **＋** `rule-prespec-onward`: the hook that sends the agent on.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the check of a held decision line.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

```then
update:
- slug: estimate-orchestration-acknowledging-reply
  set:
    status: pending
  change: the Criterion replaced whole — the LEDGER block stands written after a refusal of another hook, but for a decision line the ledger hook holds (case 688.9)
```

```tasks
- [ ] update `estimate-orchestration-acknowledging-reply`
- [ ] read `estimate-orchestration-acknowledging-reply`
```

## Case 689 — /hi loads the stop rules of the run after Plan Mode

> **context:**
> A session holds only the texts it loads: `CLAUDE.md`, the skills, the agent frames and the files `/hi` imports. A fact elsewhere in the vault reaches the agent only through a read the agent must first think to make. `insight-session-vault-knowledge-not-loaded` gathers the lessons where this went wrong; each earlier child was closed on its own, by moving the fact into a loaded text or a hook, and a general list of lessons on Rule pages was rejected (case 134). The Insight is `open` again with two live children. `lesson-carry-short-brief-drops-the-work-list` is already fixed: since case 538.1 the short brief keeps the Work and Ask lists of Next session. `lesson-work-mode-a-staged-moment-promised-inside-a-run-with-no-stop` is not: at the close of Plan Mode the agent told the person to ask for a change in Work Mode, while `vault/wiki/where-to-stop.md` runs everything from the approved Spec to the librarian in one turn with no stop for the person; only `/work` and `/box` import that file, so Plan Mode did not hold it.
> The person chose that `/hi` imports `where-to-stop.md` right after `orchestration.md`, so Plan Mode holds the same list of stops as Work Mode, and the Insight is set `actioned` by this Case. The check is `estimate-internal-context-loaded`, whose Criterion lists the files `/hi` loads in order; the change makes that list incomplete, so Case 689.1 replaces it whole and sets its `purpose` anew. Its `method`, a reading by hand at a `/hi`, waits for a later session, which case 670.4 forbids; the person chose the two-part method of the other rendered skills, the new Render in the Spec read at Retro of this session, or the rendered skill file read by hand; the check of the Case file refuses a method that names a later `/hi`, so the second part reads the skill file, as the other skills' checks do. That `/hi` turns an `@` line into loaded text was read at the `/hi` of session 2049. Case 689.2 sets the Insight `actioned`; `estimate-backlog-renders` checks the effect on `backlog.md`, since its Criterion lists an Insight under `## Deferred` only while its `status` is `open`, and it stands.
> The frame. `rule-where-to-stop` says in its Purpose that `/work` and `/box` load its text; Case 689.1 adds `/hi` there. Its Estimate `estimate-where-to-stop-stops-only-on-its-conditions` speaks of the context of `/work` and `/box` and of the run after them, which stay true; it stands. `estimate-orchestration-loaded` and `estimate-ratification-loaded` promise that their file is repeated in no other file the session holds, and their `－` line names `CLAUDE.md`, `vault/wiki/case-schema.md` and the other of the two; the set of files a session holds grows by `where-to-stop.md` in Plan Mode, but those lines never named every file a session holds — the glossary, the brief and the sprint page are held and not named, and `where-to-stop.md` has stood in the context of every Work Mode since case 531.7 without being named — and the text of `where-to-stop.md` repeats no paragraph of either file: a Grep of `` Nothing else is a stop|From the approved Spec to the librarian|end the reply with the question|open that reply with `STOP:` `` over `CLAUDE.md`, `vault/wiki/orchestration.md`, `vault/wiki/ratification.md` and `vault/wiki/case-schema.md` printed nothing. Both Criteria stay true, and both stand. `guppi/recall.py` takes the paths it reads back after a compaction from the `@` lines of the skill file, never from a copy, so it needs no change. Cases 685, 686 and 688 change other sentences of the Render of `rule-orchestration`; the sentence Case 689.1 changes, the opening line that names the files loaded with `orchestration.md`, is in none of them, and the new texts do not touch. No reader refuses on the old list, so no old form is kept.
> The searches. A Grep of `rule-internal-context|estimate-internal-context-loaded` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed 11 files: `log.md`, not read; `.claude/skills/hi/SKILL.md`, which follows at the render; `rule-internal-context.md` and `estimate-internal-context-loaded.md`, which enter Case 689.1; `guppi/recall.py` and `tests/test_recall.py`, which read the skill file or a fixture of their own and stand; `rule-skill-hi.md`, whose hit is the marker of the block; `rule-claude-md.md`, which names three files that arrive with `/hi` and no full list, and stands; `estimate-hi-no-read-calls.md`, which names the files of the block without a list, and stands; `schema.yaml` and `rule-rules-schema.md`, whose hits are examples of the schema, and stand. A Grep of `` loaded by `/hi` with `` over `vault/wiki/` printed `orchestration.md` and `rule-orchestration.md`: the list of the files loaded with `orchestration.md` enters Case 689.1, and the file follows at the render. A Grep of `where-to-stop` over `vault/wiki/rules/` printed `rule-retro.md`, `rule-case-protocol.md`, `rule-work-mode.md`, `rule-where-to-stop.md`, `rule-spec-box.md`, `rule-retro-onward.md` and `rule-retro-commit.md`: the Purpose of `rule-where-to-stop` enters Case 689.1, and the others speak of the run after Plan Mode or of a task that opens with `stop:`, stay true, and stand.

> **problem:**
> The main agent in Plan Mode does not hold the stops of the run from the approved Spec to the librarian, so it can promise the person a turn inside that run that never comes.

> **recommend:**
> - **How far the Case goes**
>   - Recommended: (a) fix the open instance by importing the stop rules into `/hi`; the Insight marked as dealt with by this Case.
>   - Answer: agreed, (a).
> - **What checks that the fix works**
>   - Recommended: (a) only the loading is checked: the Criterion of `estimate-internal-context-loaded` replaced to name `where-to-stop.md`.
>   - Answer: agreed, (a).
> - **Where the stop rules stand in the `/hi` list**
>   - Recommended: (a) right after `orchestration.md`.
>   - Answer: agreed, (a).
> - **When the check of the loading is read**
>   - Recommended: (a) the two-part method of the other rendered skills: the new Render in the Spec at Retro of this session, or the context of a later `/hi`.
>   - Answer: agreed, (a).

### Case 689.1 — /hi loads where-to-stop.md after orchestration.md

> **given:**
> `rule-internal-context`: the list of the files `/hi` imports.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-internal-context-loaded`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-where-to-stop`: the stops of the run after Plan Mode, rendered into `vault/wiki/where-to-stop.md`.
> **＋** `rule-orchestration`: the main agent's rules, whose opening line names the files loaded with them.
> **＋** `guppi/recall.py`: the paths read back after a compaction, taken from the skill file.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/ratification.md`, `vault/wiki/glossary.md` and `vault/wiki/case-schema.md`: the files `/hi` loads beside `where-to-stop.md`, and the schema it does not load.

> **when:**
> The person invokes `/hi`, with `.claude/skills/hi/SKILL.md` rendered from `rule-internal-context`.

> **then:**
> The text of `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/where-to-stop.md`, `vault/wiki/ratification.md` and `vault/wiki/glossary.md` is in the context of the first turn, in that order, without a read call.
> **＋** `vault/wiki/case-schema.md` is not in it.
> **＋** The glossary and the backlog reach a session through this block alone. After a compaction, the paths of these files are in the list of `guppi recall`.
> **－** A subagent, such as `librarian-guppi`, `ask-guppi` or one of Work Mode, carries none of these texts. Its prompt names what it needs.

```then
update:
- slug: rule-internal-context
  replace:
  - old: '@vault/wiki/orchestration.md'
    new: |-
      @vault/wiki/orchestration.md
      @vault/wiki/where-to-stop.md
  - old: prints the paths of these lines back (case 287).
    new: 'prints the paths of these lines back (case 287). `where-to-stop.md` is listed after `orchestration.md` since case 689.1: the run from the approved Spec to the librarian stops for the person only on its conditions, and Plan Mode, which plans that run with the person, holds the same list, so the main agent promises no turn of the person inside it.'
  change: /hi loads where-to-stop.md after orchestration.md (case 689.1)
- slug: estimate-internal-context-loaded
  set:
    status: pending
    purpose: The text of sprint.md, backlog.md, brief.md, orchestration.md, where-to-stop.md, ratification.md and glossary.md is present in the first turn's context after /hi, without a read call, and case-schema.md is not
    method: by hand, the text of .claude/skills/hi/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-internal-context in the Spec, read against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — where-to-stop.md loaded after orchestration.md; purpose and method set anew (case 689.1)
- slug: rule-where-to-stop
  replace:
  - old: '`/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591),'
    new: '`/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591), `/hi` loads it for Plan Mode too, so the main agent promises the person no turn the run does not give (case 689.1),'
  change: /hi loads the file for Plan Mode (case 689.1)
- slug: rule-orchestration
  replace:
  - old: loaded by `/hi` with `sprint.md`, `backlog.md`, `brief.md`, `ratification.md` and `glossary.md`,
    new: loaded by `/hi` with `sprint.md`, `backlog.md`, `brief.md`, `where-to-stop.md`, `ratification.md` and `glossary.md`,
  change: the opening line names where-to-stop.md among the files /hi loads (case 689.1)
```

```tasks
- [ ] update `rule-internal-context`
- [ ] update `estimate-internal-context-loaded`
- [ ] update `rule-where-to-stop`
- [ ] update `rule-orchestration`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-internal-context-loaded`
```

### Case 689.2 — The Insight on vault knowledge not loaded closes

> **given:**
> `insight-session-vault-knowledge-not-loaded`: the Insight this Case closes.
> **＋** `rule-insights-schema`: the form of an Insight and of its `actioned` status.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-session-vault-knowledge-not-loaded` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `clustered` lessons become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.

```then
update:
- slug: insight-session-vault-knowledge-not-loaded
  set:
    status: actioned
    addressed_by: decision-case-689.2
  change: 'actioned: /hi loads where-to-stop.md, so Plan Mode holds the stops of the run after it (case 689.1); the short brief keeps the Work list since case 538.1 (case 689.2)'
```

```tasks
- [ ] update `insight-session-vault-knowledge-not-loaded`
```

## Case 690 — A fact of a dispatch prompt and a ratified render change are no longer claimed unchecked

> **context:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` gathers the slips where a sentence claims more than the check behind it. Case 359 set the general rule in `rule-agent-writing`, case 388 had `ask-guppi` check a fact of a `context` at `/pre-spec`, and cases 544.1 and 636 added checks to the build of a Case by `case-guppi`; each time a new lesson reopened the Insight. Its two live lessons come from the main agent. In `lesson-orchestration-dispatch-prompt-carried-counts-not-from-a-run` the prompt that dispatched `case-guppi` described an answer by sentence counts taken from a glance at a transcript; `case-guppi` copied them into the `context`, and `ask-guppi` at `/pre-spec` found them not borne out, which sent the Case back. In `lesson-orchestration-a-ratified-render-change-claimed-live-before-the-render` the main agent told the person, in the reply that acknowledged a ratification, that the change would already run at the `/pre-spec` of the same session, while the skill file changes only at the librarian's `uv run guppi render` after the session.
> The person chose that `case-guppi` reads at its source each fact its prompt states besides the person's words, and keeps out of the Case a fact it cannot read there (Case 690.1, in the Render of `rule-case-build`); that the paragraph `Changes:` of the acknowledging reply says that a change of a file rendered from a Rule page takes effect at the librarian's render, so the reply claims no new behaviour of that file for the rest of the session (Case 690.2, in the Render of `rule-orchestration`); two new Estimates, each read at the Retro of this session from the new Render in the Spec, since the files change only after the session and case 670.4 keeps a reading in the session of the Case; and the Insight set `actioned` by this Case (Case 690.3). `estimate-backlog-renders` checks the effect on `backlog.md`, since its Criterion lists an Insight under `## Deferred` only while it is `open`, and it stands.
> The frame. `estimate-case-build-checks-the-finished-case` speaks of the claims of `context` that rest on a search, and `estimate-case-build-writes-the-case` of what the prompt holds; the new sentence adds a reading of the prompt's facts and makes no line of either false, so both stand, and the new Estimate of Case 690.1 checks the change. `estimate-orchestration-acknowledging-reply` says the paragraph `Changes:` says what changes in one or two sentences; the new text keeps that, so it stands, and the new Estimate of Case 690.2 checks the change. The sentence of `rule-orchestration` on the prompt of the dispatch lists what the prompt holds and stays true. Cases 685, 686, 688 and 689 change other sentences of `rule-orchestration`: 685 sets the reply that answers the ledger hook's reminder, which comes after the acknowledging reply, and none of them changes the sentence on the paragraph `Changes:`; the new texts do not touch. No reader in code refuses on the old texts, so no old form is kept.
> The searches. A Grep of `caller's prompt|prompt of (the|its) call` over `vault/wiki/rules/` and `.claude/` printed `rule-orchestration.md` and `rule-case-build.md`, and `.claude/agents/case-guppi.md`: the Render of `rule-case-build` enters Case 690.1 and the agent file follows at the render; the sentence of `rule-orchestration` stands, as said above. A Grep of `Changes:` over `vault/wiki/rules/` printed `rule-orchestration.md`, whose sentence on the acknowledging reply enters Case 690.2 and whose sentence on Cases ratified in one answer, which names one paragraph `Changes:`, stands; over `.claude/` it printed nothing. A Grep of `Changes` over `guppi/` printed nothing, so no code judges the paragraph. A Grep of `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed `brief.md`, `backlog.md` and `log.md`, not read, and the two lessons, whose `insight` field stays true. A Glob of `vault/**/*prompt-fact*` and of `vault/**/*rendered-change*` printed nothing, so both new slugs are free.

> **problem:**
> A fact the main agent writes into a dispatch prompt enters a Case unchecked, and the reply that acknowledges a ratification can tell the person that a change of a rendered harness file already runs in the session, while it changes only at the librarian's render.

> **recommend:**
> - **A fact in the prompt that sends out a Case build**
>   - Recommended: (a) the builder's frame says that a fact the prompt states, apart from the person's words, enters a Case only after the builder reads it at its source, and a fact it cannot read stays out.
>   - Answer: agreed, (a).
> - **A ratified change claimed to work before the render**
>   - Recommended: (a) the paragraph `Changes:` of the acknowledging reply says that a change to a file rendered from a Rule page takes effect at the librarian's render, after the session, and the reply claims no new behaviour for the rest of the session.
>   - Answer: agreed, (a).
> - **What checks the two fixes**
>   - Recommended: (a) two new Estimates, one per fix, each read at the Retro of this session from the new text in the Spec; the two existing Estimates stand.
>   - Answer: agreed, (a).
> - **What becomes of the backlog item after this Case**
>   - Recommended: (a) marked as dealt with by this Case; it leaves the backlog and its two lessons are archived.
>   - Answer: agreed, (a).

### Case 690.1 — case-guppi reads a fact of its prompt at its source

> **given:**
> `rule-case-build`: the frame of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-reads-a-prompt-fact-at-its-source`: the new check of the reading.
> **＋** `rule-orchestration`: the dispatch, which sets what the prompt holds.
> **＋** `estimate-case-build-checks-the-finished-case`: the check of the claims of `context`, which stands.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case, and the prompt of its call or a later message states a fact besides the person's words: a count, or what a page, a file or a reply says.

> **then:**
> The fact enters the Case only after `case-guppi` reads it at its source.
> **＋** A fact that `case-guppi` cannot read at its source stays out of the Case.
> **－** The person's words enter `recommend` as the person's answer, with no source to read.

```then
create:
- slug: estimate-case-build-reads-a-prompt-fact-at-its-source
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi lets a fact its prompt states besides the person's words into a Case only after it reads it at its source, and keeps out a fact it cannot read there
  method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: the person's question or change on the Case you built. The person's words reach you in
    new: the person's question or change on the Case you built. A fact the prompt or a message states besides the person's words — a count, or what a page, a file or a reply says — enters the Case only after you read it at its source; a fact you cannot read there stays out of the Case (case 690.1). The person's words reach you in
  change: a fact of the prompt besides the person's words enters the Case only after case-guppi reads it at its source (case 690.1)
```

```tasks
- [ ] update `rule-case-build`
- [ ] create `estimate-case-build-reads-a-prompt-fact-at-its-source`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-reads-a-prompt-fact-at-its-source`
```

### Case 690.2 — The acknowledging reply says when a rendered change lands

> **given:**
> `rule-orchestration`: the main agent's rules, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-says-when-a-rendered-change-lands`: the new check of the paragraph.
> **＋** `estimate-orchestration-acknowledging-reply`: the check of the form of the reply, which stands.
> **＋** `vault/raw/2026-10-06/0104/cases/case-685.md`: Case 685, which sets the reply after the acknowledging reply.

> **when:**
> The person ratifies a Case that changes a file rendered from a Rule page, and the main agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The paragraph `Changes:` says that the change of that file takes effect at the librarian's render, after the session.
> **＋** The reply claims no new behaviour of that file for the rest of the session.

```then
create:
- slug: estimate-orchestration-says-when-a-rendered-change-lands
  ref: rule-orchestration
  kind: QA
  purpose: Whether the reply that acknowledges a Case that changes a file rendered from a Rule page says that the file changes at the librarian's render, and claims no new behaviour of it for the rest of the session
  method: by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-orchestration
  replace:
  - old: a paragraph **Changes:** — what changes, in one or two sentences;
    new: a paragraph **Changes:** — what changes, in one or two sentences, and, when the change touches a file rendered from a Rule page, that the file changes at the librarian's render after the session, so the reply claims no new behaviour of that file for the rest of the session (case 690.2);
  change: 'the paragraph Changes: says that a rendered file changes at the librarian''s render (case 690.2)'
```

```tasks
- [ ] update `rule-orchestration`
- [ ] create `estimate-orchestration-says-when-a-rendered-change-lands`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-says-when-a-rendered-change-lands`
```

### Case 690.3 — The Insight on facts signed from a narrower check closes

> **given:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`: the Insight this Case closes.
> **＋** `rule-insights-schema`: the form of an Insight and of its `actioned` status.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `clustered` lessons become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.

```then
update:
- slug: insight-workflow-fact-signed-from-a-check-that-does-not-cover-it
  set:
    status: actioned
    addressed_by: decision-case-690.3
  change: 'actioned: case-guppi reads a fact of its prompt at its source (case 690.1), and the acknowledging reply says that a rendered file changes at the librarian''s render (case 690.2) (case 690.3)'
```

```tasks
- [ ] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
```
