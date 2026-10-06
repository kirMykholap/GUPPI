## Case 691 — The ledger hook refuses aloud a line of a LEDGER block that is no record

> **context:**
> The `Stop` hook `uv run guppi ledger` takes from a block tagged `LEDGER` only the lines that open with `- decision[`, `- estimate[` or `- lesson[`, by `ledger_lines` of `guppi/ledger.py`, and skips every other line of the block without a word. In session 0104 a reading line of Retro was written as `- estimate-` with no `[`; it was lost unseen and written again as line 49 of that session's ledger, which holds it. The lesson `lesson-ledger-block-written-with-a-placeholder-line` records an earlier stub line of a block that the hook skipped the same way. The person chose that every non-blank line of a `LEDGER` block that is no record line is refused aloud, with its own stderr line, told only when it stands in the reply just finished, as a line the grammar cannot read is told (case 552.2), and checked by a new Estimate. The hook judges such lines also when the reply holds no fresh record line, since it returns early today when it has none. `ledger_lines` itself does not change: a Grep `\bledger_lines\(` over `guppi/` printed `guppi/ledger.py`, `guppi/onward.py` and `guppi/ratified.py`, and the two other hooks read the record lines through it as before; the new judgment lives beside it and reads `PREFIXES` of the same module. A Grep `LEDGER_LINE = ` over `guppi/` printed `guppi/casecheck.py`, which holds `LEDGER_LINE`, a second copy of `PREFIXES` for the `ratification` of a Case file; by the finding of `/pre-spec`, Case 692 of this session, which changes `guppi/casecheck.py`, imports `PREFIXES` from `guppi/ledger.py` and drops `LEDGER_LINE`, so this Case does not touch that module. This Case sets only what the ledger hook does with a line at `Stop`, not the form of a reply that shows a round or a Case, which Case 692 sets. A Grep `LEDGER.{0,200}(skipped|dropped|ignored|silently)` over `vault/wiki/`, `.claude/` and `guppi/` printed `vault/wiki/brief.md`, not read, `vault/wiki/lessons/lesson-ledger-block-written-with-a-placeholder-line.md` and `vault/wiki/lessons/lesson-ledger-ratification-with-a-new-item-lost-its-block.md`; both lessons tell what happened in a past session and stay true. The sentence of `rule-ratification` that a record is such a line inside a `LEDGER` block, and a line elsewhere a preview, stays true. `rule-orchestration` sets a line written again only for the reminder of a lesson with no mark (case 685.1) and for a held decision line (case 688.7), which this Case does not touch; the general sentence that the answer to a refusal of the ledger hook writes the refused lines again stands only in the Render of `rule-retro`, for the answer after the reply that ends Retro. The Criterion of `estimate-ledger-write-lifts` speaks only of record lines that land, and that of `estimate-ledger-write-refuses-a-line-it-cannot-read` only of lines that open with the bracket, so both stand.

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
>   - Answer: not answered yet.

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
>   - new: `` `{addresses:<lesson slug>}` (case 685.1). It refuses aloud a line of a `LEDGER` block that is no record — a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`, which it skipped without a word before — so a record with a broken opening is not lost unseen (case 691). ``
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
> - decision[case 691][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 691][create][estimate-ledger-write-refuses-a-line-that-is-no-record]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```
