## Case 541 — The supersedes row of the glossary says which defers a supersede clears

> **context:**
> The table in the `## Terms` section of `entity-glossary` gives one row per term: the term, its meaning in one line, and the page that defines it. `uv run guppi glossary` writes `vault/wiki/glossary.md` from this table at the librarian's run, and `/hi` loads that file into every working session. This session a reading of `estimate-glossary-terms-defined` came back failed on one row. The row `ref`, `slug`, `supersedes` says that each `{supersedes:case N}` block marks every entry of its Case superseded and clears its `deferred_by`. `rule-case-protocol` says that `generate` clears a defer only from the pages that the superseding Case names. The docstring of `guppi/generate.py` says the same: a target that the superseding Case does not names keeps its `deferred_by` (case 467.3). So when an old defer points at two pages and the new Case names one of them, the other page stays in the backlog, but the row says it leaves. The same reading found that the other rows agree with their pages, the rows that case 535 rewrote among them. The row `deferred_by`, the field text of `rule-rules-schema` and a sentence of `rule-entities-schema` also say that a `supersedes` clears `deferred_by`, and they do not say that the page must be named. The row copies its page word for word, so the reading counted no contradiction there. The person chose to fix only the row the reading found, so these three stay as they are. This is an `update`, so no vault query was run. The frame holds no hook. The Estimates of `rule-glossary` promise the render, the check of the file and the ticks, not the content of the rows, so they are not touched. The Criterion of `estimate-glossary-terms-defined` still says what the rows must meet, so it is not replaced. Its next reading comes at a later `/hi`, after the librarian's run writes the row. For that reason the Case holds no `read` line, as case 535 held none.

> **problem:**
> A row of the glossary, a file that every session loads, says that a supersede clears every defer of the Case it names. The code and `rule-case-protocol` clear a defer only from the pages that the new Case names. The wording of the row must change to agree with the page.

> **recommend:**
> One `update` of `entity-glossary` with one `replace` pair on the row. The new wording follows `rule-case-protocol` and the docstring of `guppi/generate.py` and adds case 467.3 as the source. The render line then writes `glossary.md` again. The Case changes no promise, so it has no sub-cases. Fixing the row `deferred_by` and the two schema pages in the same Case was rejected: they omit a condition but contradict nothing, and the failed reading does not ask for that change.

> **given:**
> `entity-glossary` — the table of terms, whose row this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, loaded by `/hi`
> **＋** `rule-glossary` — renders the table and stops the write when a row is off its form
> **＋** `rule-case-protocol` — the `where` page of the row, which says from which pages a supersede clears a defer
> **＋** `guppi/generate.py` — its docstring says which targets lose their `deferred_by` on a `supersedes`

> **when:**
> A reader reads the row `ref`, `slug`, `supersedes` of `vault/wiki/glossary.md` at `/hi`, after `uv run guppi glossary` wrote it from `entity-glossary` at the librarian's run.

> **then:**
> The row says that each `{supersedes:case N}` block marks every entry of its Case superseded, and that `generate` clears a defer only from the pages that a decision line of the superseding Case names, as `rule-case-protocol` and `guppi/generate.py` say.
> **－** No other row of `entity-glossary` changes, the row `deferred_by` included, and no row is added or removed.

> **tasks:**
> - [ ] update `entity-glossary` — the row `ref`, `slug`, `supersedes` says which defers a supersede clears
>   - old: `` each of which marks every entry of its Case superseded and clears its `deferred_by` (cases 200.2, 429) ``
>   - new: `` each of which marks every entry of its Case superseded; `generate` clears a defer only from the pages that a decision line of the superseding Case names (cases 200.2, 429, 467.3) ``
>   - change: `the row ref, slug, supersedes: a supersede clears a defer only from the pages the superseding Case names (case 541)`
> - [ ] `uv run guppi glossary`

> **ratification:**
> ```
> - decision[case 541][update][entity-glossary]{ref:entity-glossary}
> ```
