# The visual layer — design

**Date:** 2026-08-12
**Slice:** the visual layer, the work Task 6 of slice 3 became when it was dropped
**Status:** designed, not yet planned

## Why this slice exists, and how it will be judged

The owner does not use the tool. Asked what keeps him from it, he chose «смотреть неприятно,
не тянет открывать» over «мало данных», «не хватает функций» and «руки не дошли». That answer
is the whole brief, and it gives the slice a success criterion better than «it looks designed»:

> **The slice succeeds if the owner starts opening `/vacancies`.**

Asked what is wrong with the page today, he selected **all four** offered complaints: everything
carries one visual weight, the table reads badly, the controls look unfinished, and the statuses
cannot be read at a glance. So this is a full pass over the interface, not a targeted repair.

He also said he barely uses the page yet. That is a constraint on the design, not just context:
**nothing here may be fitted to an imagined daily workflow.** No triage mode, no reading modes,
no affordances justified by a habit that does not exist. The design earns its decisions from
what is on screen — what repeats, what competes, what cannot be scanned — and nothing else.

## What the page looks like today

Measured from a live screenshot at 1440×900, production data, one enabled tag:

- **Three of seven columns are constant down the page.** «Теги» is `Head of IT` in every row,
  «Обновлена» is `06.08.2026` in every row, and `work.ua` sits under every title. Together they
  hold roughly a third of the width and separate no row from its neighbour.
- **The status — the row's most important state — is drawn with the most anonymous control
  available**, a column of ten identical native `select`s.
- **Rows vary in height** because company names and salaries wrap (`48400–55000 UAH` breaks with
  the currency on its own line), and they are separated by a hairline. Where one vacancy ends is
  genuinely hard to see.
- **Every title is link-blue and underlined**, so the widest column reads as a wall of blue.
- **Nine filter controls sit in one wrapping row directly on the page background**, selects and
  long checkbox labels interleaved: it reads as prose with holes in it.
- **Navigation is on the right**, while the page title is on the left.
- Ten rows fit on screen.

## Approach: grow our own stylesheet

Three approaches were weighed. **A — grow the hand-written palette into a small design system**
is chosen. **B — vendor a CSS framework (Bulma) and re-mark the templates** is rejected, and the
reason is empirical rather than aesthetic: slice 3's Task 6 already implemented, reviewed,
browser-walked and then reverted a vendored framework whole, and **three of the owner's four
complaints are not what a framework fixes.** Hierarchy, table density and status legibility are
decisions about this project's own information; Bulma would supply competent form controls and
stop there. **C — a framework for the primitives, hand-written for the rest** takes the markup
churn of B and still leaves the table and the statuses to be designed by hand.

The research from Task 6 stays on the record in `docs/HANDOFF.md` §0 and is not repeated here:
if a framework is ever revisited, Bulma matches this project's three-state theme toggle exactly
and ships no JavaScript.

## 1. Structure

**The stylesheet moves out of the template.** The `<style>` block in `base.html` becomes
`src/jobhunt/web/static/app.css`, linked with `<link rel="stylesheet">`. The theme bootstrap
script **stays inline in `<head>`**: it must run before the first paint, or the flash of the
light theme returns on every load. Only the declarations move; the custom properties move with
them.

**That move closes a review finding that outlived Task 6's revert.** Today no test fetches
`/static/` at all: the mount can be removed, the directory renamed or the file dropped from the
image, and the whole suite stays green while every page renders unstyled. Once the stylesheet
lives in that directory, two assertions — `GET /static/app.css` and `GET /static/htmx.min.js`
each answer 200 — make the omission fail loudly.

**Out of scope, deliberately:**

- every route, every fragment, `web/data/`, and every query — the slice touches no SQL;
- the five AST boundary tests and the htmx swap-target invariant, which must stay green **with
  no edits to them**. That is a criterion of the slice, not a hope;
- the question of whether the table should become a client-side grid — the owner deferred it on
  2026-08-12 to be reopened after this slice, against a dressed table rather than an argument;
- our own JavaScript. On this design nothing needs it: the row highlight, the chip fill and every
  control state are CSS. The AST test that would pin the new «presentational only» boundary
  therefore belongs to the first slice that writes JavaScript, not to this one;
- **a sticky table header**, which is worth naming so that a later session does not add it and
  wonder. The table sits inside `<div class="scroll">` with `overflow-x: auto`, and CSS computes
  `overflow-y` to `auto` alongside it: the div is its own scroll container, as tall as its
  content, so a `position: sticky` `<thead>` has nothing to stick to. Making it work means
  deciding what horizontal overflow should do instead, and that decision is not this slice's.

**In scope:** `base.html`, the new `app.css`, and the templates' markup as far as the table's
information design requires — which is not zero, because «reads badly» is not cured by colour.

## 2. The table

**Six columns instead of seven.** «Теги» leaves its column and joins the source on one muted
line under the vacancy title: `work.ua · Head of IT`. A tag belongs to the vacancy rather than
to a column of its own, where it either repeats in every row (as today) or in half of them. The
freed width goes to «Компания», which currently wraps to two lines. The `{% set columns = 7 %}`
literal in `_rows.html` and the seven `<th>` in `vacancies.html` change together — the comment
above that literal already says they must agree, and it is right.

**Titles stop being link-blue.** They take the foreground colour, semibold, underlined on hover
only. The accent colour is reserved for what is actually an accent: focus rings, the current
navigation item, a selected chip. This is the cheapest large win against «no hierarchy».

**The status becomes a coloured pill.** The control stays a native `select` — htmx's post hangs
on it, and so does the manual error-swap in `base.html` — but it gains `data-status="{{ row.status }}"`
and is coloured by an attribute selector. No JavaScript is involved: htmx swaps the cell, and the
replacement arrives carrying the new `data-status`.

**The status labels stay English.** `new`, `applied`, `call` remain both the values and the
visible text; colour and shape do the work of making them scannable. Decided by the owner on
2026-08-12, against translating the visible labels while keeping the identifiers.

**Row rhythm.** Even rows take a barely-there surface tint and hover takes a slightly stronger
one; the separators get quieter rather than heavier, because alternation is what makes rows
scannable and lines are what make a table look like a spreadsheet. Salary stops breaking before
its currency (`white-space: nowrap`) and uses tabular figures.

**Density was a target and is now a measurement, and the owner has ruled on it.** «About fifteen
rows where ten fit» was written here before anything was measured; on the built page the median
row went 58px to 52px and ten rows fit where nine did. What stands in the way is not padding:
227px of a 900px viewport is spent above the table, and the tallest rows are titles wrapping to
three lines. Task 3 gives the title the width the tags column held, and Task 5 may recover some of
the 227px — but on 2026-08-12 the owner chose the muted «work.ua · tag» line under the title over
the rows it costs, and **density is explicitly not critical**. Twelve to thirteen rows is the
honest expectation. Do not spend further work buying rows.

The empty-state rows and the «Показать ещё» button inherit the new type and spacing; neither
grows an appearance of its own.

## 3. Filters, chips, and the shell

**The filters get a panel.** One surface with a border, matching the tags panel already on «Сбор
данных», so the page has a single zone of controls above the table. Inside it, three groups:
the search field first and wide, then the row of selects, then the row of checkboxes.

**One label is shortened.** «показать вакансии, у которых нет тега фильтра» becomes «без тега
фильтра», with the full sentence moved into `title`. It is currently longer than the rest of its
row put together.

**The chips lose the native checkbox.** The template's comment defends keeping it visible, on the
ground that a hidden box needs a second signal of selectedness which must then be kept in
agreement with the field. **`:has(:checked)` retires that argument:** a pill coloured from
`:has(:checked)` is not a second source of truth — it is the browser reading the same field from
outside, and there is nothing there to drift. The comment is rewritten along with the styles so
that it stops defending a decision that no longer exists.

- The input keeps its place in the flow with `appearance: none` — not `display: none` — so it
  stays focusable and reachable by keyboard; the focus ring already hangs on `.chip:focus-within`.
- An unselected chip is a quiet outline; a **selected** chip is filled with the accent and carries
  a check glyph before its label. Fill and shape, not colour alone.
- `chip-off` — the tag is disabled for the next collection — stays a dashed outline and composes
  with the fill independently: a dashed filled pill means «shown now, no longer searched». Two
  facts, two signals, no collision.
- `@supports not (selector(:has(*)))` restores the native box. A browser without `:has()` — which
  means older than December 2023 — sees today's appearance rather than pills with no sign of
  selection. There is no arrangement in which the selected state becomes invisible.

**Navigation moves to the left**, and the page header gains a bottom border. Today the eye starts
at the title in one corner and must cross the page to change pages; and the title floats with no
edge above the content.

## Testing

**What the suite can hold**, and therefore must:

- `/static/app.css` and `/static/htmx.min.js` each answer 200 — the finding above;
- the status cell renders `data-status` equal to the row's status, so the colouring cannot be
  silently unhooked;
- the column count: the `<thead>` and the `colspan` used by the empty-state and «Показать ещё»
  rows agree, which is what the existing comment demands and nothing currently checks;
- the five boundary tests and the swap-target invariant stay green **unedited**.

**What no test here can hold:** whether it looks good, and whether the density is right. That is
what the browser walk is for. Per `CLAUDE.md` the walk stays in every task and is walked in the
main session through the Playwright MCP.

**A test that scans text for a literal must be shown to fail** before it is trusted — the lesson
slice 3 paid for twice. Any assertion added here that greps rendered markup is verified by
removing what it guards and quoting the failure.

## Risks

- **Taste does not survive being written down.** The owner's own reason for this slice is that
  the page is unpleasant, and no paragraph here can settle what «pleasant» is. The plan must put
  a screenshot of the running application in front of him **early** — the first task produces a
  dressed `/vacancies` to look at, and the rest of the plan proceeds only after that is
  approved. This is what makes a wrong direction cost one task instead of a slice; it is the
  same separability that made Task 6's revert cheap.
- **The column literal and the header can drift silently.** Layout does not break — the page
  simply stops being a table. Hence the assertion above.
- **Density is empirical.** «Fifteen rows» is a target to aim at with real rows of real lengths,
  not a number to implement.

## Decisions this slice does not reopen

- The table is rendered by the server. The grid question is deferred to after this slice.
- Status identifiers, and now their visible labels, stay English.
- No new dependencies, Python or npm. A vendored stylesheet would not have been one either —
  that is how `htmx.min.js` already ships — but this design vendors nothing.
