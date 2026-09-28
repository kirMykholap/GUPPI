## Case 468 — One standard for the account of a session: each fact once in the Retro report and in the handoff

> **context:**
> `/retro` opens with a numbered list of what is not done. The list holds every unticked box of `raw/<date>/<hi HHMM>/spec.md`, per Case, each marked as waiting for the librarian, waiting for a later session, or debt. At Retro most of these boxes are the page and render lines of the session's own Cases, so the list names each Case and its pages. The close then names every ratification per Case with the same pages, and "what got done" and "what is not done" repeat parts of the opening list. At the `/retro` of session 1819, `estimate-retro-report-holds-each-fact-once` was read `failed` for this reason (line 39 of `raw/2026-09-27/1819/ledger.md`), and the person asked for one standard. `handoff.md` has the same defect. The handoff of session 1819 named the failed reading both in `## Notes from memory` and in `## What actually got done`, and named the next-session items in the notes and again in the instructions to the librarian.
> The person chose one standard for both documents. The frontier numbers only what needs an end in this Retro. The librarian's boxes are one count line, and the later-session `read` lines are one line of slugs. The close has three parts, each fact in one part only. A reading or a lesson that ends an item of the frontier is named under What is not done, not under What got done. The handoff's `## What actually got done` carries the close. The librarian does not read the chat, so this is the one repeat, across two documents for two readers. Inside `handoff.md` each fact stands in one section. The handoff's What is not done differs from the close in three ways, because the file has no frontier. It names each open item in a few words. The text of a note for the handoff, one of the four ends that `rule-retro` allows, stands there as that item's end. The two lines under the frontier stand under it, because the paragraph of `rule-retro` on the readings already sends the later-session Estimates to the handoff.
> What the frame changes: the frontier paragraph and the close paragraph of the Render of `rule-retro`, the `purpose` of `estimate-retro-report-holds-each-fact-once`, and the section list of the Render of `rule-handoff`. The section names stay, so `rule-brief` still reads "Where things stand" from `## What actually got done`. `estimate-brief-written` still finds its "handoff flag with a question" in the notes or among the open items. `estimate-retro-loads` promises the readings, not the form of the report, so it is not touched. `estimate-handoff-dispatches` promises the three sections, the dispatch and no commit, which still hold, so it is not touched. `estimate-end-of-work-order` promises the order of the steps, which does not change. The Purpose of `rule-handoff` ("what actually got done") still holds. The one `create` has a `ref`, so no vault query ran. A Glob of `vault/**/` finds no page for `estimate-handoff-holds-each-fact-once`.
> Not done: the form of `brief.md` does not change.

> **problem:**
> The account of a session repeats itself. The Retro report names the same Cases, pages and open items in the frontier and in each part of the close. The handoff names the same facts in more than one section. The person reads everything several times, and no text of the vault says which part holds which fact.

> **recommend:**
> Two sub-cases, one per promise. 468.1 sets the form of the Retro report in the Render of `rule-retro` and replaces the Criterion and the `purpose` of `estimate-retro-report-holds-each-fact-once`. 468.2 makes the handoff's `## What actually got done` the Retro close, with the differences a file without a frontier needs. It keeps the other two sections to their own facts and creates `estimate-handoff-holds-each-fact-once`. The standard is written once, in `rule-retro`, and `rule-handoff` refers to it, so the two texts cannot drift apart. The rejected option was to drop `## What actually got done` from the handoff, because `rule-brief` reads it.

### Case 468.1 — The Retro report holds each fact once

> **given:**
> `rule-retro` — its Render, the frontier and the close of `/retro`
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `estimate-retro-report-holds-each-fact-once` — the promise of the report, its Criterion replaced whole and its `purpose` rewritten
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, with its unticked boxes
> **＋** `uv run guppi tail` — the Tail of the session's ledger
> **＋** `make test` and `make style` — the checks the skill loads before the first turn
> **＋** `estimate-retro-loads` — the promise of the readings at Retro, unchanged

> **when:**
> The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes, and the agent writes the frontier and the close.

> **then:**
> The frontier is one numbered list of what needs an end in this Retro: each unticked box that is debt, and what the agent noticed during Work Mode.
> **＋** A `read` line without its line in the Tail, whose slug this session neither creates nor updates, is debt, and so is a box of code, a test, a command or a migration left unticked.
> **＋** Under the list stand two lines, not numbered: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it.
> **－** The frontier names no box that waits for the librarian one by one, and holds no list of the ratifications.
> **＋** The close has three parts. Ratified is one line with the ids of the Cases ratified, from `uv run guppi tail`, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page.
> **＋** What got done holds the commit, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier.
> **＋** What is not done holds each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier.
> **－** No Case, box, reading or lesson is named in two parts of the report.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `` Open with the frontier, in one message and with no read call: the list of what is not done, numbered: the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), per Case — a `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above listed as waiting for the librarian, whose scripts tick them (cases 226, 250, 270), not as debt — a `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, listed as waiting for a later session, neither debt nor the librarian's (case 428.4) — another `read` line without its line in the Tail is debt, and the lines of a Case a `{supersedes:case N}` line of the Tail names are not counted at all, its work stands under the superseding Case (case 282); what you noticed during Work Mode, in the same list — bugs, forks, a contract that turned out imprecise. ``
>   - new: `` Open with the frontier, in one message and with no read call. First sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73). A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above wait for the librarian, whose scripts tick them (cases 226, 250, 270); they are not debt. A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian's (case 428.4). Another `read` line without its line in the Tail is debt, and so is a box of code, a test, a command or a migration left unticked. The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all; its work stands under the superseding Case (case 282). The frontier is one numbered list of what needs an end in this Retro: each box that is debt, and what you noticed during Work Mode — bugs, forks, a contract that turned out imprecise. Under the list write two lines, not numbered: the count of the boxes that wait for the librarian, with no list of them, and the slugs of the `read` lines that wait for a later session. The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1). ``
>   - old: `` Close with three lists: every ratification of this session, one line per Case, by the Tail above grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted; what got done; what is not done — the opening list by its numbers, each item with the end it took. ``
>   - new: `` Close with three parts, each fact in one part only. Ratified: one line with the ids of the Cases ratified, by the Tail above, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page. What got done: only what no other part holds — the commit, the code files and tests changed, the result of `make test` and `make style`, the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier; no Case and no item of the frontier restated. What is not done: each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier. No Case, box, reading or lesson is named in two parts of the report (case 468.1). ``
>   - change: `the report of /retro holds each fact once — the frontier numbers only what needs an end, the librarian's boxes one count line, the close three parts: the Case ids, what got done, the numbers with their ends (case 468.1)`
> - [ ] update `estimate-retro-report-holds-each-fact-once`
>   - set: `{status: pending, purpose: "Whether the report of /retro holds each fact once — the frontier numbers only what needs an end, the boxes that wait for the librarian one count line and the read lines that wait for a later session one line of slugs; the close holds the Case ids, what got done and the numbers of the frontier with their ends"}`
>   - change: `the Criterion replaced whole and the purpose rewritten — the frontier numbers only what needs an end; the close holds the Case ids, what got done and the numbers with their ends (case 468.1)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-report-holds-each-fact-once` — by hand, at the first `/retro` after the render

> **ratification:**
> ```
> - decision[case 468.1][update][rule-retro]{ref:rule-retro}
> - decision[case 468.1][update][estimate-retro-report-holds-each-fact-once]{ref:estimate-retro-report-holds-each-fact-once}
> ```

### Case 468.2 — The handoff holds each fact once, its account the Retro close

> **given:**
> `rule-handoff` — its Render, the sections of `handoff.md`
> **＋** `.claude/skills/handoff/SKILL.md` — the skill rendered from `rule-handoff`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the document the skill writes
> **＋** `rule-retro` — the close of the Retro, which the handoff carries, and the four ends of an item, a note for the handoff among them
> **＋** `rule-brief` — reads "Where things stand" from `## What actually got done` by name, unchanged
> **＋** `estimate-handoff-dispatches` — the promise of the three sections, the dispatch and no commit, unchanged
> **＋** `estimate-handoff-holds-each-fact-once` — the new promise

> **when:**
> The person invokes `/handoff` after the Retro of the session, on a clean tree, and the agent writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `## What actually got done` holds the three parts of the close of the Retro of `rule-retro`: Ratified and What got done as the person approved them, and What is not done in the form below.
> **＋** What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in the file, and the text of a note for the handoff stands there as the end of its item.
> **＋** Under What is not done stand the two lines under the frontier: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats.
> **＋** `## Direct instructions to the librarian` holds only what to check first and what may duplicate what.
> **－** No Case, reading, lesson or open item is named in two sections of `handoff.md`.
> **－** The three section names stay as they are, so `rule-brief` reads `## What actually got done` as before.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` `## Direct instructions to the librarian` (what to check first, what may duplicate what), `## What actually got done` (which Cases closed, where the code landed, what is not done). ``
>   - new: `` `## Direct instructions to the librarian` (what to check first, what may duplicate what), `## What actually got done` (the three parts of the close of the Retro: Ratified and What got done as the person approved them; What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in this file, the text of a note for the handoff standing there as the end of its item, and under it the two lines under the frontier — the count of the boxes that wait for the librarian and the slugs of the `read` lines whose slug this session creates or updates). A fact stands in one section only: a Case, a reading, a lesson or an open item named in one section is not named in another (case 468.2). ``
>   - change: `the handoff holds each fact once — What actually got done carries the Retro close, a note for the handoff stands as the end of its item, the notes and the instructions hold only their own facts (case 468.2)`
> - [ ] create `estimate-handoff-holds-each-fact-once`
>   - type: `estimate`
>   - ref: `rule-handoff`
>   - kind: `QA`
>   - purpose: `Whether handoff.md holds each fact once — the Retro close in What actually got done, each open item named once with its end, the notes and the instructions to the librarian only their own facts`
>   - method: `one reading by hand at the first /handoff after the render, against the close of its Retro, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] read `estimate-handoff-holds-each-fact-once` — by hand, at the first `/handoff` after the render

> **ratification:**
> ```
> - decision[case 468.2][update][rule-handoff]{ref:rule-handoff}
> - decision[case 468.2][create][estimate-handoff-holds-each-fact-once]{ref:rule-handoff}{tags:session,workflow,harness}
> ```
