## Case 535 — Five glossary rows agree with the pages that define them

> **context:**
> The table in the `## Terms` section of `entity-glossary` gives one row per term: the term, its meaning in one line, and the page that defines it. `uv run guppi glossary` writes `vault/wiki/glossary.md` from this table at the librarian's run, and `/hi` loads that file into every working session. At the `/hi` of this session, a reading of `estimate-glossary-terms-defined` came back failed. Its ledger line counts three rows that contradict the page they point to. First, the `Decision page` row gives `## Context` only to a Case without `given`, but `rule-decisions-schema` also gives it to the two-line body of a Case superseded in its own session (case 299.4). Second, the `Main agent, Subagent` row has the main agent write ledger lines "until the Retro commit", but `rule-retro` ends Retro with one `LEDGER` block in the reply after that commit (case 531.8). Third, the `Plan Mode` row covers only Cases ratified or deferred. But `rule-case-protocol` also closes an item that needs no decision without a Case, leaves an item of the sprint for later, and keeps a backlog item as it stands (cases 356.1, 356.2, 421.4, 451.1). The subagent that took the reading also noted two more false rows, which the ledger line does not count, since neither contradicts its `where` page. The `Types` row says a `delete` sets `status: deleted`, but no page schema allows that status, and the docstring of `guppi/generate.py` sets `archived` with a History line `deleted`. The `CLAUDE.md, case-schema.md` row names two of the rules spliced into `CLAUDE.md`, while `rule-claude-md` names three (case 360). The person chose to fix all five rows, to keep the promise as it stands, and to have the `Plan Mode` row name every way an item closes. This is an `update`, so no vault query was run. The frame holds no hook. The Estimates of `rule-glossary` promise the render, the check of the file and the ticks, not the content of the rows, so they are not touched. The Criterion of `estimate-glossary-terms-defined` still says what the rows must meet, so it is not replaced. Its next reading comes at a later `/hi`, after the librarian's run writes the rows. For that reason the Case holds no `read` line, since Retro would count one as debt.

> **problem:**
> Five rows of the glossary, a file loaded into every session, say something that a page of the vault or the code contradicts. The words of those rows must change to agree with the pages.

> **recommend:**
> One `update` of `entity-glossary` with one `replace` pair per row. Each new wording follows the page or file that defines the thing, and the render line writes `glossary.md` again. The Case changes no promise, so it has no sub-cases. Widening the Criterion to any live page was rejected: the reading would have no bound, and the fix of the `Types` row does not need it.

> **given:**
> `entity-glossary` — the table of terms, whose rows this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, loaded by `/hi`
> **＋** `rule-glossary` — renders the table and stops the write when a row is off its form
> **＋** `rule-decisions-schema` — defines the body of a Decision page
> **＋** `rule-retro` — defines where the last ledger lines of a session stand
> **＋** `rule-case-protocol` — defines Plan Mode, the close of a Frontier item and the types of a decision
> **＋** `rule-claude-md` — defines what `CLAUDE.md` holds
> **＋** `guppi/generate.py` — its docstring defines what a `delete` sets

> **when:**
> A reader reads a row of `vault/wiki/glossary.md` at `/hi`, after `uv run guppi glossary` wrote it from `entity-glossary` at the librarian's run.

> **then:**
> The row `Decision page` gives `## Context` also to the two-line body of a Case superseded in its own session, as `rule-decisions-schema` does.
> **＋** The row `Main agent, Subagent` puts the last ledger lines in the one reply that ends Retro, after its commit, as `rule-retro` does.
> **＋** The row `Plan Mode` names each way a Frontier item closes, as `rule-case-protocol` does: a Case that is ratified or deferred, an item that needs no decision and closes with no Case, an item of the sprint left for later, and a backlog item kept as it stands.
> **＋** The row `Types` says a `delete` sets `archived` with a History line `deleted`, as the docstring of `guppi/generate.py` does.
> **＋** The row `CLAUDE.md, case-schema.md` names the three rules spliced into `CLAUDE.md`, as `rule-claude-md` does.
> **－** No other row of `entity-glossary` changes, and no row is added or removed.

> **tasks:**
> - [ ] update `entity-glossary` — five rows agree with the pages that define them
>   - old: `` `## Context` only for a Case without `given`, such as the short form of a deferred decision, and never `## Given` ``
>   - new: `` `## Context` only for a Case without `given`, such as the short form of a deferred decision, and in the two-line body of a Case superseded in its own session (case 299.4), never `## Given` ``
>   - old: `Runs Cases and writes ledger lines, until the Retro commit`
>   - new: `Runs Cases and writes ledger lines, the last of them in the one reply that ends Retro, after its commit (case 531.8)`
>   - old: `Frontier items discussed as Cases until each is ratified or deferred`
>   - new: `The Frontier worked item by item: an item that needs a decision is a Case until it is ratified or deferred, an item that needs none closes with no Case, an item of the sprint may be left for later and a backlog item kept as it stands; it ends when no item of the Cases list is open (cases 356.1, 356.2, 421.4, 451.1)`
>   - old: `` `delete` sets `status: deleted` after an impact analysis, the librarian archives ``
>   - new: `` `delete` sets `status: archived` with a History line `deleted`, after an impact analysis, and `guppi cleanup` moves the file to the archive ``
>   - old: `` `rule-language` and `rule-agent-writing` in their markers (cases 59.8, 272, 288.3) ``
>   - new: `` `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers (cases 59.8, 272, 288.3, 360) ``
>   - change: `the rows Decision page, Main agent, Plan Mode, Types and CLAUDE.md agree with the pages that define them (case 535)`
> - [ ] `uv run guppi glossary`

> **ratification:**
> ```
> - decision[case 535][update][entity-glossary]{ref:entity-glossary}
> ```
