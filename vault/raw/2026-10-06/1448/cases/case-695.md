## Case 695 — The ledger hook refuses aloud a line of a LEDGER block that is no record

> **context:**
> The `Stop` hook `uv run guppi ledger` takes from a block tagged `LEDGER` only the lines that open with `- decision[`, `- estimate[` or `- lesson[`, by `ledger_lines` of `guppi/ledger.py`, and skips every other line of the block without a word. In session 0104 a reading line of Retro was written as `- estimate-` with no `[`; it was lost unseen and written again as line 49 of that session's ledger, which holds it. The lesson `lesson-ledger-block-written-with-a-placeholder-line` records an earlier stub line of a block that the hook skipped the same way. The person chose that every non-blank line of a `LEDGER` block that is no record line is refused aloud, with its own stderr line, told only when it stands in the reply just finished, as a line the grammar cannot read is told (case 552.2), and checked by a new Estimate: Case 695.1. The hook judges such lines also when the reply holds no fresh record line, since it returns early today when it has none. This Case replaces Case 691, which was ratified whole and is built again with sub-cases after the findings of `/pre-spec` and the person's answer to a further round; its decision lines carry `{supersedes:case 691}`.
>
> `ledger_lines` itself does not change: a Grep `\bledger_lines\(` over `guppi/` printed `guppi/ledger.py`, `guppi/onward.py` and `guppi/ratified.py`, and the two other hooks read the record lines through it as before; the new judgment lives beside it and reads `PREFIXES` of the same module. A Grep `LEDGER_LINE = ` over `guppi/` printed `guppi/casecheck.py`, which holds `LEDGER_LINE`, a second copy of `PREFIXES` for the `ratification` of a Case file; by the finding of `/pre-spec`, Case 692 of this session, which changes `guppi/casecheck.py`, imports `PREFIXES` from `guppi/ledger.py` and drops `LEDGER_LINE`, so this Case does not touch that module. This Case sets only what the ledger hook does with a line at `Stop` and how Retro answers its refusal, not the form of a reply that shows a round or a Case, which Case 692 sets. A Grep `LEDGER.{0,200}(skipped|dropped|ignored|silently)` over `vault/wiki/`, `.claude/` and `guppi/` printed `vault/wiki/brief.md`, not read, `vault/wiki/lessons/lesson-ledger-block-written-with-a-placeholder-line.md` and `vault/wiki/lessons/lesson-ledger-ratification-with-a-new-item-lost-its-block.md`; both lessons tell what happened in a past session and stay true. The sentence of `rule-ratification` that a record is such a line inside a `LEDGER` block, and a line elsewhere a preview, stays true. The Criterion of `estimate-ledger-write-lifts` speaks only of record lines that land, and that of `estimate-ledger-write-refuses-a-line-it-cannot-read` only of lines that open with the bracket, so both stand.
>
> `rule-orchestration` sets a line written again only for the reminder of a lesson with no mark (case 685.1) and for a held decision line (case 688.7), which this Case does not touch; the general sentence that the answer to a refusal of the ledger hook writes the refused lines again stands only in the Render of `rule-retro`, for the answer after the reply that ends Retro. There a refused note written again would be refused again, while the new stderr line asks to leave it out; the person chose that Retro leaves such a line out and goes on to `/handoff` when nothing is left to write: Case 695.2, which changes the Render of `rule-retro`, replaces the Criterion of `estimate-retro-runs-on-to-the-handoff` and sets its `purpose` anew, since it names the refused line written again; its `method`, a run read by hand, names no such promise and stands. A Grep `refused lines? (written )?again|writes the refused|lines written again` over `vault/wiki/`, `.claude/` and `guppi/` printed `vault/wiki/log.md`, not read, `vault/wiki/rules/rule-page-generation.md`, `vault/wiki/rules/rule-retro-onward.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/estimates/estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `vault/wiki/estimates/estimate-retro-runs-on-to-the-handoff.md`, `.claude/skills/retro/SKILL.md`, `guppi/generate.py` and `guppi/onward.py`. The hit in `rule-page-generation` and in `guppi/generate.py` is about decision lines written again with a mark, another thing; the hit in `rule-retro` at its History stays. The Purpose of `rule-retro-onward` says the agent answers a refusal with a reply that writes the refused lines again and must end, which Case 695.2 corrects. The Criterion of `estimate-retro-onward-sends-the-agent-to-the-handoff` and the docstrings of `guppi/onward.py` say the hook sends the agent on again at the end of the next reply, which writes the refused lines again; the hook's judgment does not change, and an answer that writes no line and calls `/handoff` leaves `handoff.md` standing at its `Stop`, where that Criterion already has the hook exit 0, so they stand.

> **problem:**
> A line of a `LEDGER` block whose opening is broken is no record, and the hook drops it with no message, so a reading or a lesson can be lost while the agent believes it was written.

> **recommend:**
> - **Which lines in a LEDGER block are refused aloud**
>   - Recommended: (b) every non-blank line inside a `LEDGER` block that does not open with `- decision[`, `- estimate[` or `- lesson[`; blank lines and blocks with another tag or none stay as now.
>   - Answer: agreed, (b).
> - **Which replies the hook tells about**
>   - Recommended: (a) as for a line the grammar cannot read: told only when it stands in the reply just finished, a line of an earlier text skipped silently.
>   - Answer: agreed, (a).
> - **The message and the check that proves it**
>   - Recommended: (b) its own stderr line, which names the three openings, and a new Estimate on `rule-ledger-write`; the passed Estimate stays as it is.
>   - Answer: agreed, (b).
> - **What the reply after Retro does with a refused line that is no record**
>   - Recommended: (a) the Retro rule and `estimate-retro-runs-on-to-the-handoff` change: a refused record line is written again, a refused line that is no record is left out, and with nothing left the agent goes on to commit and call `/handoff`.
>   - Answer: agreed, (a).

### Case 695.1 — The ledger hook refuses aloud a line of a LEDGER block that is no record

> **given:**
> `guppi/ledger.py`: the ledger hook, which reads the lines of `LEDGER` blocks.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `rule-ledger-write`: the rule of the ledger hook, whose Purpose names the new refusal.
> **＋** `estimate-ledger-write-refuses-a-line-that-is-no-record`: the new check of the refusal.
> **＋** `rule-ratification`: the form of a ledger line.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py`, in a session with a `hi`, finds in a `LEDGER` block of a text of the main agent a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`.

> **then:**
> The line is not written to the ledger.
> **＋** The record lines of the same `Stop` are written and judged as before.
> **＋** When the line stands in the reply just finished, the hook exits 2 with one stderr line per such line: "ledger: line not written — a LEDGER block holds only lines that open with - decision[, - estimate[ or - lesson[: <line>. Write it again with that opening, or leave it out."
> **＋** A reply whose `LEDGER` block holds no record line gets the same stderr line for each such line.
> **＋** Each stderr line is told once until the person's next message; a repeat of the same line stays silent.
> **－** A line from an earlier text of the transcript is skipped at every later `Stop` without a word.
> **－** A blank line, and a line in a block with another tag or with none, is not refused.
> **－** Without a `hi` the hook judges no such line.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` `{addresses:<lesson slug>}` (case 685.1). ``
>   - new: `` `{addresses:<lesson slug>}` (case 685.1). It refuses aloud a line of a `LEDGER` block that is no record — a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`, which it skipped without a word before — so a record with a broken opening is not lost unseen (case 695.1). ``
>   - change: `the hook refuses aloud a non-blank line of a LEDGER block that is no record line`
> - [ ] create `estimate-ledger-write-refuses-a-line-that-is-no-record`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses aloud a non-blank line of a LEDGER block that does not open with a record prefix, and says why only for the reply just finished`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] `guppi/ledger.py`: one function beside `ledger_lines`, judged by its `PREFIXES` and the fence functions of `guppi/materialize.py`, gives the non-blank lines of `LEDGER` blocks that are no record; the hook judges them after the `hi` check, also when no fresh record line stands, and prints the stderr line through `untold`; the docstring gains a paragraph.
> - [ ] `tests/test_ledger.py`: a near-miss line and a note in the reply just finished are refused aloud, a block with only such a line too; a line of an earlier text is silent; the record lines beside it land; a blank line and a line of an untagged block pass; a repeat already told is silent.
> - [ ] read `estimate-ledger-write-refuses-a-line-that-is-no-record`

> **ratification:**
> ```
> - decision[case 695.1][update][rule-ledger-write]{ref:rule-ledger-write}{supersedes:case 691}
> - decision[case 695.1][create][estimate-ledger-write-refuses-a-line-that-is-no-record]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```

### Case 695.2 — Retro leaves out a refused line that is no record

> **given:**
> `rule-retro`: the rule of `/retro`, whose Render `.claude/skills/retro/SKILL.md` changes.
> **＋** `estimate-retro-runs-on-to-the-handoff`: its Criterion is replaced whole.
> **＋** `rule-retro-onward`: the hook that sends the agent on to `/handoff`, whose Purpose names the change.
> **＋** `rule-ledger-write`: the ledger hook, whose refusal the answer meets.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the session that Retro reads and writes.
> **＋** `vault/wiki/where-to-stop.md`: the conditions of a stop.
> **＋** `rule-ratification`: the form of a ledger line.

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

> **then:**
> Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
> **＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
> **＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
> **＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
> **－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
> **＋** When the ledger hook refuses a line of that reply, the agent answers with a reply that holds only a `LEDGER` block with each refused record line written again; a refused line of the block that is no record, one that does not open with `- decision[`, `- estimate[` or `- lesson[`, is left out. No other `LEDGER` block follows the reply that ends Retro.
> **＋** When no refused line is left to write, that answer holds no `LEDGER` block, and in it the agent commits the session folder and calls `/handoff`.
> **＋** After that reply, or after the reply that answers a refusal of the ledger hook, in the same turn, the agent commits the session folder and calls `/handoff`.
> **－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead. The answer to a refusal of the ledger hook is no stop.
> **－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `` that reply holds only a `LEDGER` block with the refused lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596). ``
>   - new: `` that reply holds only a `LEDGER` block with the refused record lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596). A refused line of the block that is no record — one that does not open with `- decision[`, `- estimate[` or `- lesson[` — is left out; when no line is left to write, that reply holds no `LEDGER` block, and in it you commit the session folder and call `/handoff` (case 695.2). ``
>   - change: `the answer to a refusal of the ledger hook after Retro leaves out a refused line that is no record, and goes on to /handoff when nothing is left to write`
> - [ ] update `rule-retro-onward`
>   - old: `the agent answers that refusal with a reply that writes the refused lines again, a reply that must end,`
>   - new: `` the agent answers that refusal with a reply that writes the refused record lines again, a reply that must end — or, when only lines that are no record were refused, with a reply that writes none and calls `/handoff` itself (case 695.2) —, ``
>   - change: `the answer to a refusal of the ledger hook may write no line and call /handoff itself when only lines that are no record were refused`
> - [ ] update `estimate-retro-runs-on-to-the-handoff`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply and each refused record line of a refusal of the ledger hook again in one reply that holds only them, a refused line that is no record left out, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
>     ```
>   - change: `the Criterion replaced whole — a refused line that is no record is left out of the answer to a refusal of the ledger hook, and with nothing left the answer calls /handoff`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-runs-on-to-the-handoff`

> **ratification:**
> ```
> - decision[case 695.2][update][rule-retro]{ref:rule-retro}{supersedes:case 691}
> - decision[case 695.2][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 695.2][update][estimate-retro-runs-on-to-the-handoff]{ref:rule-retro}
> ```
