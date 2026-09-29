## Case 514 — Generate applies a Case to a page once

> **context:**
> When a Case is approved a second time in its session, its decision lines are written into the ledger again. The ledger hook skips a line only when it is word for word the same as a stored one. So a line that gained a `{supersedes:case N}` mark at the second approval is stored a second time. `materialize` makes one entry per line, and `generate` applies every entry, so the same change of one Case to one page runs twice. In session 1134 this happened to Case 508.2. L15–L16 stood without the mark and L67–L68 with it. L15 applied the `replace` pairs to `rule-skill-hi`, so L67 did not find its anchor and failed. L68 applied the Criterion of `estimate-hi-writes-frontier` a second time and wrote its History line twice, and `vault/wiki/log.md` holds that line twice too. `generate` tries an unapplied entry again at every run (case 53.3), so L67 fails again at each librarian run. The person chose these points in the rounds. The fix lives in `generate`, not in `materialize`: `materialize` never rewrites an entry it wrote, so a merge there would leave L67 failed. The doubled History and `log.md` lines stay as a record. `case-schema.md` stays as it is, because its sentence that the hook does not append a line it already holds stays true. The promise joins the Criterion of `estimate-generate-fails-alone`, whose trigger already covers an entry already handled. With the change, L67 finds L15 applied at the next librarian run, gets `applied` and loses its `failed` mark, with no one-off migration. The mark the repeated line carries still reaches the yaml, since `materialize` handles each line's `{supersedes}` as it does today. The Case creates no page, so no vault query was needed. Four texts in the frame stay true. `estimate-generate-ticks-the-spec` stands: the repeat is marked `applied` and its tick finds no open line, which is no error. `estimate-generate-writes` stands, because its trigger is an entry applied to a page and a repeat changes no page. `estimate-materialize-assembles` stands, because every line still has its entry. The dedupe sentence of `rule-ledger-write` stands. W15, the reading of `estimate-generate-fails-alone` on this session's Frontier, waits for a later session, because the ledger hook refuses a reading of a page the session changes (case 428.1).

> **problem:**
> A Case approved again in its session, with a mark added to its lines, is applied twice to each page it names. The second application fails a text edit, or writes the same History line again, and a failed entry fails again at every run.

> **recommend:**
> `generate` treats an entry whose Case, kind and slug match an entry of the same yaml that already applied as done. It marks the entry `applied`, drops a stale `failed` mark, changes no page and prints one line. This is one check in one script, and it heals the failed L67 of session 1134 by itself. A merge of the repeated line in `materialize` was rejected: it would leave existing failed entries failed.

> **given:**
> `guppi/generate.py` — applies the entries of a yaml to the pages
> **＋** `materialize.yaml` — the entries `generate` reads
> **＋** `vault/wiki/log.md` — the log `generate` appends per entry
> **＋** `rule-page-generation` — the rule of `generate`
> **＋** `estimate-generate-fails-alone` — the promise on failed, skipped and marked entries
> **＋** `tests/test_generate.py` — the tests of `generate`

> **when:**
> `uv run guppi generate` meets an entry of `materialize.yaml` it cannot apply, or one already handled.

> **then:**
> An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
> **＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
> **＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
> **＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
> **＋** An `update` with no content prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, changes no page and is marked applied.
> **＋** A `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` marked `applied` is marked `applied`, loses a stale `failed` mark, changes no page, appends nothing to `vault/wiki/log.md` and prints `generate: <slug>: line N repeats line M of case C; nothing applied` on stdout, whichever of the two lines stands first in the ledger.
> **－** The failure of one entry changes no other page: `vault/wiki/log.md` after it is level with the pages.
> **－** An `update` with `sections.Criterion` on an Estimate page does not fail for want of a `method` field.
> **－** An `estimate` or a `lesson` entry is never taken for a repeat: it carries no `case`.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `reported, and the rest apply (case 47).`
>   - new: `reported, and the rest apply (case 47). An entry whose Case, kind and slug match an entry of the same yaml that already applied is marked applied and changes no page, so a Case approved again in its session, its lines written again with a mark added, changes each page once (case 514).`
>   - change: `an entry whose Case, kind and slug match an applied entry of the same yaml is marked applied and changes no page (case 514)`
> - [ ] update `estimate-generate-fails-alone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an entry that repeats an applied entry of its Case, kind and slug is marked applied, changes no page and prints one line`
> - [ ] `guppi/generate.py`: in `apply`, before an entry of kind `create`, `update`, `delete` or `defer` is applied, look for an entry of the same yaml with the same `case`, `kind` and `slug` marked `applied`; when found, mark the entry `applied`, drop its `failed`, print the stdout line and apply nothing; the docstring says so beside the no-content update
> - [ ] `tests/test_generate.py`: a repeated `update` whose `replace` anchor the first entry consumed is marked applied, fails nothing, changes no page, adds no History or `log.md` line and prints the stdout line; the same with the first entry failed and the second applied, on the rerun; a repeat of a `create` writes no collision; an `estimate` entry of the same slug is applied as before
> - [ ] read `estimate-generate-fails-alone`

> **ratification:**
> ```
> - decision[case 514][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 514][update][estimate-generate-fails-alone]{ref:estimate-generate-fails-alone}
> ```
