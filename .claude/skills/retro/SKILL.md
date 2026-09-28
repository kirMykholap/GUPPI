---
name: retro
description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
---


Tests: !`make test`

Style: !`make style`

Ledger: !`uv run guppi tail`

Retro is an analysis of this session, not planning. Open with the frontier, in one message and with no read call but the Read of `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3). First sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73). A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above wait for the librarian, whose scripts tick them (cases 226, 250, 270); they are not debt. A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian's (case 428.4). Another `read` line without its line in the Tail is debt, and so is a box of code, a test, a command or a migration left unticked. The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all; its work stands under the superseding Case (case 282). The frontier is one numbered list of what needs an end in this Retro: each box that is debt, and what you noticed during Work Mode — bugs, forks, a contract that turned out imprecise. Under the list write two lines, not numbered: the count of the boxes that wait for the librarian, with no list of them, and the slugs of the `read` lines that wait for a later session. The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1). An item of the frontier is its text alone: it names no end, and no Case, reading or lesson that ends it; its end stands only in What is not done (case 483). The person adds their own observations. Every item, theirs or
yours, ends in one of four ways: a `- lesson[...]` line; a `- estimate[...]` line, a
reading of an Estimate whose work is finished; a short defer; or a note for the
handoff. Retro ratifies no other decision: a `create`, `update` or `delete` waits for
the next Plan Mode.

A short defer is a Case in the short form, appended to `vault/raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before its ledger line: `## Case N`, `context`, `problem`,
and a `defer` block with `purpose`; no `recommend`, `given`, `when` or `then`. A defer
line without its Case is marked incomplete by materialize.

Edit code only when the edit finishes work that traces to a line of this session's ledger.
Red tests: fix now when the fix finishes ratified work; otherwise save the change
with `git diff` into `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session's folder, revert it, and write a short
defer naming the patch. Either way write a `- lesson[error][...]` line whose root
cause says why Retro was reached with a regression; the handoff still needs green. A failing test or a lint finding line that `## Baseline` of `work.md` already holds was red before the work, whatever `## Expected red` names: it is an item of the frontier that ends as a note for the handoff, named as red before the work; it is not debt, nothing is fixed or reverted for it, and no lesson is written for it (case 479.4).
`gh` is not available: name a deferred bug in the handoff, so the brief carries it.
Do not run `make lint` here: the vault is written after handoff, by the librarian. A check that reads a page or a governed file this session's Spec updates — `make lint` or one of its steps, or a hook of the working tree — is red or refuses in Work Mode until the librarian's run writes the page or renders the file, and the `make lint` of that run is its reading: `/work` marks such a red under `## Expected red` of `work.md` when the task that changes the check runs, one line naming the check and the page or file it waits for. A red or a refusal of that check on a page or file a line names is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt; a red or a refusal on a page or file no line names is debt, even when another line names the same check, unless `## Baseline` holds its line. In a session with no `work.md`, such a red ends as a note for the handoff by your judgment, as before. A red test is never an expected red: it is fixed or reverted as above (cases 473.1, 479.3).

Take the readings of the Estimates whose work is finished and that this session neither creates nor updates — by a decision line of its slug, or by an `update` that renames a page to it — and write their lines; name in the handoff any Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built. What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3).

Close with three parts, each fact in one part only. Ratified: one line with the ids of the Cases ratified, by the Tail above, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page. What got done: only what no other part holds — the commit, the code files and tests changed, the result of `make test` and `make style`, the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier; no Case and no item of the frontier restated. What is not done: each number of the frontier with the end you propose, a short defer with its Case id, with no text of the item, no ledger line number and no repeat of the two lines under the frontier. The frontier and the close stand in one reply, and the person approves or changes the ends there; the lines of the ends are written after it (case 483). No Case, box, reading or lesson is named in two parts of the report (case 468.1). The report has this form, its labels in the language of the chat (case 483):

```
1. <text of the item>
2. <text of the item>

<N> boxes wait for the librarian.
Read in a later session: `<slug>`, `<slug>`.

Ratified: <ids of the Cases>.
What got done: <commit>; <code files and tests>; make test <result>; make style <result>; <readings and lessons by L<n>>.
What is not done:
- 1 — <end>
- 2 — <end>
```

When the person approves, commit (`make style` clean, `make test` green but for the tests that `## Baseline` of `work.md` holds), then call `/handoff`.
