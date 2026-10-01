## Case 552 — A ledger line that the parser cannot read no longer stops the ledger hook

> **context:**
> At the end of each reply of the main agent, the `Stop` hook `guppi ledger` reads every record line inside a `LEDGER` block of the session's transcript. It checks each fresh line with `parse_line` of `guppi/materialize.py` and appends the lines to the session's `ledger.md`. In session 2026-09-30/1736 the main agent wrote a reading with a space between its brackets: `estimate[estimate-spec-write-copies-the-ratified-case] [passed]`. For that line, the estimate branch of `parse_line` cut the first bracket off and then matched the second bracket at the start of the rest. The rest opened with a space, so the match was None and `.end()` raised `AttributeError`. The lesson branch had the same two steps. The hook caught every exception, printed `ledger: ledger.md not written: <error>` to stderr and exited 0, so nobody saw the failure. It reads the whole session again at each `Stop`, so this one line kept every later line of the session out of the ledger. A dry run of `ledger.run` gave rc 0 and that stderr line. `guppi ratified` failed on the same reply and did not write the short form of Case 551 under `## Deferred`. It reads only the finished reply, so Case 551 must be shown again, and this Case does not change `guppi ratified`. The person chose two fixes. First, `parse_line` returns None where it would raise, and a test covers this. Second, the ledger hook exits 2 on an error. With the person's consent, the main agent built the code of 552.1 before the Spec and outside Work Mode, to unblock the ledger: `parse_line` and its tests in `tests/test_materialize.py`. At 19:47:50 the hook wrote the 20 waiting lines. Line 29 of `vault/raw/2026-09-30/1736/ledger.md` is the line with the space, which now reads as a reading. Line 30 is its corrected copy. `guppi/ledger.py` is unchanged. The tasks of 552.1 stand, and Work Mode ticks them after it checks them. The rounds settled the choices inside the two fixes. `parse_line` reads a space between brackets for every kind of line, as the decision branch already does (552.1). The hook refuses a line that `parse_line` cannot read (552.2). That refusal makes the Criterion of `estimate-ledger-write-lifts` false, because it says every record line lands, so the Criterion is replaced whole with one more `－` line (552.3). The crash exit gets its own Estimate (552.4). The hook reads `stop_hook_active` from the payload inside the same `try`. So an error while it reads the payload exits 0 with the error on stderr: the hook cannot tell a re-fire then, and exit 2 could loop. Only an error after the payload is read exits 2. The other `Stop` hooks in `.claude/settings.json` (`guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward`) each catch their own errors and exit 0. They stay as they are, and a change to them is a later item. The Criterion of `estimate-materialize-assembles` already says that a line the grammar does not parse goes under `unparsed` and the run goes on. The crash broke that promise, and 552.1 restores it, so that Estimate is not touched. Its readings taken this session stand. A Grep of `parse_line|does not parse|cannot parse` over the live pages of `vault/wiki/` outside `decisions/` found `rule-ledger-tail`, `rule-raw-archive`, `rule-prespec`, `estimate-ledger-tail`, `estimate-raw-archive`, `estimate-prespec-checks-the-plan`, `estimate-spec-write-checks-the-written-case` and `estimate-render-harness-reproduces`, the latter about JSON files. It also found the actioned `insight-ledger-line-written-unchecked` and `insight-materialize-lift-loses-a-schema-field`. Each one reads record lines through `parse_line`, says that a line that does not parse is no finding of its check, or tells the history of a line that did not parse. A wider grammar shared by one function keeps each of them true. The Estimates of `rule-ledger-write` that refuse a reading, a lesson without its prefix and a mark with no decision line judge only lines that `parse_line` reads, so they stand. The check of the answer noted that `then` lines of 552.2, 552.3 and 552.4 share words. The sub-cases stay separate because they make different promises. 552.3 copies the Criterion of `estimate-ledger-write-lifts` as it stands and names the refusal of 552.2 only by its slug. 552.4 exits 2 on an error of the hook, not on a refused line. The ledger hook refuses a reading of an Estimate that a decision line of the session creates or updates (case 428.1). So a reading of `estimate-ledger-write-lifts` taken this session is refused once 552.3 is ratified, and it waits for a later session. Each new Estimate has a `ref`, so this Case runs no vault query. Grep shows that neither new slug exists.

> **problem:**
> An estimate or lesson line with a space between its brackets made `parse_line` raise instead of return. The ledger hook swallowed the error and exited 0, so the line and every later line of the session went unwritten, and nobody was told. The question was how `parse_line` reads such a line, what the hook does with a line it cannot read, how the hook reports its own error, and how these promises are recorded.

> **recommend:**
> - **How the promise of the crash exit is recorded**
>   Recommended: (a) a new Estimate of `rule-ledger-write` for the crash exit; `estimate-ledger-write-lifts` keeps its text.
>   Answer: (a) a new Estimate.
> - **Change**
>   Asked: correct the facts of `context`: the full list of Grep hits, and the ledger as it stands after the code of 552.1 was built and the waiting lines were written.
>   Taken: `context` names the three missing hits and says that none of them is made false. It tells the failure in the past tense, and it says that the code of 552.1 was built before the Spec, that the hook wrote the 20 waiting lines at 19:47:50 with the line with the space at line 29 and its corrected copy at line 30, and that `guppi/ledger.py` is unchanged.

### Case 552.1 — `parse_line` reads a space between brackets and never raises

> **recommend:**
> - **What `parse_line` does with a space between the brackets**
>   Recommended: (b) read it as a decision line is read; return None only for a line it still cannot read.
>   Answer: (b) read it, like a decision line.

> **given:**
> `rule-materialize` — the rule of the lift of the ledger, whose code holds the one parse of a ledger line
> **＋** `guppi/materialize.py` — `parse_line`, the one parse of a ledger line
> **＋** `tests/test_materialize.py` — the tests of the lift and of `parse_line`
> **＋** `estimate-materialize-assembles` — its Criterion sends a line the grammar does not parse to `unparsed`

> **when:**
> A caller passes one ledger line to `parse_line` of `guppi/materialize.py`.

> **then:**
> A `decision`, `estimate` or `lesson` line gives the same record with or without spaces between two of its brackets that follow each other.
> **＋** A line that `parse_line` cannot read returns None, and no exception leaves `parse_line`.
> **－** A line with no space between its brackets gives the same record as before.

> **tasks:**
> - [ ] update `rule-materialize`
>   - old: `of the ledger is an entry.`
>   - new:
>     ````
>     of the ledger is an entry. `parse_line` reads a record line with or without spaces between its brackets, and returns None, never an error, for a line it cannot read (case 552.1).
>     ````
>   - change: `parse_line reads a space between brackets and returns None, never an error, for a line it cannot read (case 552.1)`
> - [ ] `guppi/materialize.py`: `parse_line` reads an `estimate` or a `lesson` line with spaces between its brackets, and returns None for a line it cannot read; the docstring says so
> - [ ] `tests/test_materialize.py`: an `estimate` line and a `lesson` line with a space between the brackets give the record of the same line without it; a broken line of each kind returns None; a line without spaces gives the record it gave before

> **ratification:**
> ```
> - decision[case 552.1][update][rule-materialize]{ref:rule-materialize}
> ```

### Case 552.2 — The ledger hook refuses a line it cannot read

> **recommend:**
> - **What the ledger hook does with a line `parse_line` cannot read**
>   Recommended: (b) refuse it at once: not written, exit 2 with one stderr line when it stands in the reply just finished.
>   Answer: (b) refuse it at once.

> **given:**
> `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger lines
> **＋** `guppi/ledger.py` — `run` and the refusals of fresh lines
> **＋** `guppi/materialize.py` — `parse_line`, the one parse of a ledger line
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `estimate-ledger-write-refuses-a-line-it-cannot-read` — the promise this sub-case creates

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh line `- decision[`, `- estimate[` or `- lesson[` in a `LEDGER` block of the session, and `parse_line` of `guppi/materialize.py` returns None for it.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in case-schema.md."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A refused line gets no other refusal of the hook and no other stderr line.
> **－** A line already in the ledger of any session is not judged again.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old:
>     ````
>     A refused line from an earlier text is judged again at every `Stop`, without a word, until a decision line of its Case stands before it, and is written then.
>     ````
>   - new:
>     ````
>     A refused line from an earlier text is judged again at every `Stop`, without a word, until a decision line of its Case stands before it, and is written then. A line that `parse_line` of `guppi/materialize.py` cannot read is not written, since `materialize` would put it under `unparsed` and the record it holds would be lost (case 552.2); it is judged before the other refusals and gets no other; as for a refused reading, the hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, skips an older one without a word, and writes the other lines as before.
>     ````
>   - change: `the hook refuses a line that parse_line cannot read (case 552.2)`
> - [ ] create `estimate-ledger-write-refuses-a-line-it-cannot-read`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses a record line that parse_line cannot read, and says why only for the reply just finished`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] `guppi/ledger.py`: `run` sets apart each fresh line that `parse_line` cannot read before the other refusals, does not write it, and prints its stderr line when it stands in the reply just finished; the docstring says so
> - [ ] `tests/test_ledger.py`: a broken line in the reply just finished (exit 2, one stderr line, the other lines written); the same line from an earlier text (exit 0, no word, not written); a broken lesson line gets no refusal for its prefix or mark
> - [ ] read `estimate-ledger-write-refuses-a-line-it-cannot-read` — in a later session

> **ratification:**
> ```
> - decision[case 552.2][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 552.2][create][estimate-ledger-write-refuses-a-line-it-cannot-read]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```

### Case 552.3 — The main promise of the ledger hook names the new refusal

> **recommend:**
> - **Should the ledger hook's main promise change to allow for the new refusal?**
>   Recommended: (a) add the new refusal to the main promise; it goes back to unchecked.
>   Answer: (a) add the new refusal to the main promise.

> **given:**
> `estimate-ledger-write-lifts` — the promise whose Criterion this sub-case replaces
> **＋** `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger lines
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — a refusal the Criterion names
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — a refusal the Criterion names
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — a refusal the Criterion names
> **＋** `estimate-ledger-write-refuses-a-line-it-cannot-read` — the refusal of 552.2, which the Criterion now names

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** A line the hook refuses by `estimate-ledger-write-refuses-a-line-it-cannot-read` does not land.
> **－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-lesson-without-its-prefix` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-mark-with-no-decision-line` does not land while that refusal holds.
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

> **tasks:**
> - [ ] update `estimate-ledger-write-lifts`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a line the hook cannot read does not land (case 552.3)`
> - [ ] read `estimate-ledger-write-lifts` — in a later session

> **ratification:**
> ```
> - decision[case 552.3][update][estimate-ledger-write-lifts]{ref:estimate-ledger-write-lifts}
> ```

### Case 552.4 — The ledger hook exits 2 on its own error

> **recommend:**
> - **Which hooks stop the agent when they crash**
>   Recommended: (a) the ledger hook only; the same change for the other hooks is its own item in a later session.
>   Answer: (a) the ledger hook only.
> - **Change**
>   Asked: the sub-case contradicted itself, because an error while the payload is read comes before the hook knows it is a re-fire, and exit 2 there could loop; an error while reading the payload exits 0 with the error on stderr, and an error after the payload is read exits 2.
>   Taken: `when` names an error after the payload is read; `then` exits 2 for it, and a `－` line exits 0 with the error on stderr for an error while the payload is read; the new text of `rule-ledger-write` and the tests say the same.

> **given:**
> `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger lines
> **＋** `guppi/ledger.py` — `run` and its handler of an error
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `estimate-ledger-write-exits-2-on-an-error` — the promise this sub-case creates

> **when:**
> The `Stop` hook `uv run guppi ledger` fires, and an exception rises in `run` of `guppi/ledger.py` after it has read the payload: while it reads the transcript, the event log or the ledger, or while it judges or appends the lines.

> **then:**
> The hook exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees the error at the end of that reply.
> **＋** A line not yet appended when the error rose waits for the next `Stop` of the session, which reads the transcript again.
> **＋** While the cause stands, the error comes back at every `Stop`.
> **－** An error while the hook reads the payload exits 0 with the error on stderr: the hook cannot tell a re-fire then, and exit 2 could loop.
> **－** With `stop_hook_active` (the re-fire after a block) the hook exits 0 and writes nothing, so it cannot loop.
> **－** A refusal of the hook with no error — no `hi`, or a refused line — keeps its own stderr line and exit.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old:
>     ````
>     and writes nothing, so it cannot loop.
>     ````
>   - new:
>     ````
>     and writes nothing, so it cannot loop. An error of the hook itself after it has read the payload — an exception while it reads the transcript, the event log or the ledger, or judges or appends the lines — exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees it at the end of that reply; a line not yet appended waits for the next `Stop`, and while the cause stands the error comes back at every `Stop`. An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then (case 552.4).
>     ````
>   - change: `the hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 552.4)`
> - [ ] create `estimate-ledger-write-exits-2-on-an-error`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, and exits 0 on an error while reading the payload and on the re-fire`
>   - method: `uv run pytest tests/test_ledger.py — piped payloads, a function of the hook patched to raise`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] `guppi/ledger.py`: `run` reads the payload in its own guard that prints the error and returns 0, and the handler of the rest prints the error and returns 2; the docstring says so
> - [ ] `tests/test_ledger.py`: a patched `append` that raises gives exit 2 and the stderr line; the same payload with `stop_hook_active` gives exit 0 and writes nothing; a payload that cannot be read gives exit 0 and the stderr line
> - [ ] read `estimate-ledger-write-exits-2-on-an-error` — in a later session

> **ratification:**
> ```
> - decision[case 552.4][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 552.4][create][estimate-ledger-write-exits-2-on-an-error]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```
