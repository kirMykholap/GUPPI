## Case 483 — Retro writes the end of a frontier item only in What is not done

> **context:**
> At `/retro`, the agent writes a report in two parts. The frontier is a numbered list of what still needs an end. The close has three blocks: Ratified, What got done and What is not done. The rule of case 468.1 puts each fact in one part: the frontier holds the text of each item, and What is not done holds each number with its end. The Retro of session 1318 wrote the whole report in one reply. It gave every frontier item its proposed end, and What is not done gave the same ends again. Item 3 read "Result: short defer, Case 481", and What is not done read "3 — defer, Case 481". So `estimate-retro-report-holds-each-fact-once` failed for the second time (L39 of `raw/2026-09-28/1318/ledger.md`). The Render of `rule-retro` never says that a frontier item carries no end. It also asks What is not done for "its ledger line number where it has one", and those lines are not yet written when the report is written. That Retro said so in its own close: "the ledger lines and Case 481 are not written yet".
> This Case changes a page and does not create one, so no vault query was needed. The new Criterion keeps every line of the old one word for word except one. The line on What is not done is replaced on purpose: the end becomes the one the agent proposes, and the ledger line number is dropped. Two lines are added: a frontier item names no end, and the close stands in the same reply as the frontier. The frame holds no contradiction. `rule-handoff` and `estimate-handoff-holds-each-fact-once` rebuild What is not done in words from the items and their ends. They name no ledger line number of the Retro close, so this Case leaves them true. Of the other Estimates of `rule-retro`, `estimate-retro-loads` speaks of readings, and `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` and `estimate-retro-red-in-the-baseline-is-not-charged` speak of red checks. None of the three speaks of the layout of the report, so they are not touched. The person chose: the end only in What is not done, one reply without line numbers, a skeleton of the report in the skill, and the Criterion replaced whole.

> **problem:**
> The Retro report writes the end of each frontier item twice: once on the item and once in What is not done. A Case that ends an item is then named in two parts. The Render allows this because it does not forbid an end on an item. It also asks What is not done for ledger line numbers that do not exist when the report is written.

> **recommend:**
> Say in the Render that a frontier item is its text alone, and that its end, with the Case id of a defer, stands only in What is not done. Drop the ledger line number from What is not done, and state that the frontier and the close stand in one reply, where the person approves or changes the ends. Add a skeleton of the report to the skill, so that the agent fills in a fixed layout instead of recalling a rule. Replace the Criterion of `estimate-retro-report-holds-each-fact-once` whole. Putting the end on the item and dropping What is not done was rejected, because it would make `rule-handoff` false and change a second promise. A hook that checks the reply was rejected, because it would judge free text in the chat language and adds code to a rule enforced by render only.

> **given:**
> `rule-retro` — its Render: the sentences on the frontier and on the close
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `estimate-retro-report-holds-each-fact-once` — its Criterion replaced whole
> **＋** `uv run guppi tail` — the decision lines and ledger lines the report counts from
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the unticked boxes the frontier sorts
> **＋** `rule-handoff` — rebuilds What is not done from the items and their ends; unchanged

> **when:**
> The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes, and the agent writes the frontier and the close.

> **then:**
> The frontier is one numbered list of what needs an end in this Retro: each unticked box that is debt, and what the agent noticed during Work Mode.
> **＋** A `read` line without its line in the Tail, whose slug this session neither creates nor updates, is debt, and so is a box of code, a test, a command or a migration left unticked.
> **＋** Under the list stand two lines, not numbered: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it.
> **－** The frontier names no box that waits for the librarian one by one, and holds no list of the ratifications.
> **－** An item of the frontier is its text alone: it names no end, and no Case, reading or lesson that ends it.
> **＋** The close has three parts. Ratified is one line with the ids of the Cases ratified, from `uv run guppi tail`, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page.
> **＋** The close stands in the same reply as the frontier.
> **＋** What got done holds the commit, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier.
> **＋** What is not done holds each number of the frontier with the end the agent proposes, a short defer with its Case id, and the person approves or changes the ends there; it holds no text of an item, no ledger line number and no repeat of the two lines under the frontier.
> **－** No Case, box, reading or lesson is named in two parts of the report.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1).`
>   - new: `The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1). An item of the frontier is its text alone: it names no end, and no Case, reading or lesson that ends it; its end stands only in What is not done (case 483).`
>   - old: `What is not done: each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier.`
>   - new: `What is not done: each number of the frontier with the end you propose, a short defer with its Case id, with no text of the item, no ledger line number and no repeat of the two lines under the frontier. The frontier and the close stand in one reply, and the person approves or changes the ends there; the lines of the ends are written after it (case 483).`
>   - old: `No Case, box, reading or lesson is named in two parts of the report (case 468.1).`
>   - new:
>     ````
>     No Case, box, reading or lesson is named in two parts of the report (case 468.1). The report has this form, its labels in the language of the chat (case 483):
>
>     ```
>     1. <text of the item>
>     2. <text of the item>
>
>     <N> boxes wait for the librarian.
>     Read in a later session: `<slug>`, `<slug>`.
>
>     Ratified: <ids of the Cases>.
>     What got done: <commit>; <code files and tests>; make test <result>; make style <result>; <readings and lessons by L<n>>.
>     What is not done:
>     - 1 — <end>
>     - 2 — <end>
>     ```
>     ````
>   - change: `a frontier item is its text alone; its end, with the Case id of a defer, stands only in What is not done, with no ledger line number; the frontier and the close stand in one reply, in the form of a skeleton (case 483)`
> - [ ] update `estimate-retro-report-holds-each-fact-once`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a frontier item names no end; What is not done holds the proposed end of each number with no ledger line number; the frontier and the close stand in one reply (case 483)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-report-holds-each-fact-once` — by hand, at the first `/retro` after the render

> **ratification:**
> ```
> - decision[case 483][update][rule-retro]{ref:rule-retro}
> - decision[case 483][update][estimate-retro-report-holds-each-fact-once]{ref:estimate-retro-report-holds-each-fact-once}
> ```
