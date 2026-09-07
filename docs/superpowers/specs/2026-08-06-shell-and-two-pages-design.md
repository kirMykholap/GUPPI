# Slice 3 — the shell and two pages

**Date:** 2026-08-06
**Status:** design, approved in conversation, not yet planned
**Previous slice:** `2026-08-05-collection-from-the-browser-design.md` (merged as `0020fee`)

## 1. What this slice is

Everything the tool shows lives on one page. `/vacancies` carries the vacancy table,
its filters, the tag chips, the tags panel and the collection buttons, and the profile
selector. That was right while there was one job to do. It is no longer: collecting and
working with what was collected are different activities, done at different times, and
the page cannot say which of its controls belongs to which.

The clearest symptom is the word **тег**, which today means two different things a few
centimetres apart on the same screen. The chip row filters what is shown. The tags panel
below it writes `ProfileTag.is_enabled` and changes what the *next collection searches*.
One of them is about the past, the other about the future, and nothing on screen says so.

This slice introduces a shell with navigation, splits the page in two along that seam,
and rebuilds the tag model so that each meaning has exactly one control.

## 2. Scope

**In scope**

- A shell: navigation on the right, the profile selector inside it, two page routes.
- «Сбор данных» — the collection buttons and the tags panel.
- «Вакансии» — the filters, the chips, the table, the status control.
- A collection indicator in the shell, so a run started on one page is visible on every
  page and the table refreshes itself when the run ends wherever the user is standing.
- The rebuilt tag model of §4.
- `jobhunt tag remove` starts refusing.
- A vendored CSS layer, replacing the 172 hand-written lines.

**Not in scope, deliberately**

| Deferred | Why now is not the moment |
|---|---|
| Source checkboxes (dou.ua / work.ua on and off) | A new profile column and a migration. It belongs with the profile form, not with a layout change |
| The vacancy card — click a row, see everything | Needs a decision about where the full description comes from; `fetch_description` has no producer in production today |
| A «Профиль» page | Its content is the collection frame form, which is a slice of its own |
| A «Настройки» page | There is nothing to put on it. There is no settings table, and `config.py` reads `.env`. An empty menu item is worse than a missing one |
| Sorting by column, bulk status change | Both are server-side and small, but neither is what this slice is about |
| React | See §9. The trigger is named there, and this slice is not it |

## 3. The shell and the two pages

**Two routes, each a whole document.** `GET /vacancies` and `GET /collection`. Switching
pages is navigation: it gets its own address, its own history entry, and a link that can
be saved and reopened. Not htmx tab-swapping — the browser already does all of this, and
slice 2a's two Criticals were both about taking that work away from it and doing it worse.
The cost is a full re-render on switch: 10.1 ms measured on the production database.

**Navigation lives in `base.html`, on the right**, as the owner specified. The profile
selector moves into it: the profile is global to both pages, and today it sits inside one
of them.

**Only two items appear in the navigation.** «Вакансии» and «Сбор данных».

| Element | Today | After |
|---|---|---|
| «Проверить новое» / «Полная сверка» | `/vacancies` | `/collection` |
| Tags panel (ищется / не ищется) | `/vacancies` | `/collection` |
| Chips, filters, table, status control | `/vacancies` | `/vacancies` |
| Profile selector | inside the page | the shell |

## 4. Tags: two roles, two controls

### 4.1 Collection tags

`ProfileTag`, unchanged as an entity. Two states, and they affect **the parser only**:

- **вкл** — the next collection searches by this tag.
- **выкл** — it does not.

They live on «Сбор данных». Nothing about them hides or shows a vacancy.

### 4.2 Filter tags

**Filter tags are not an entity — they are derived from data.** A chip exists for a tag
that has at least one link to a vacancy of this profile. The user cannot add or remove
them; they are a reflection of what has actually been found.

One consequence to accept knowingly: **an enabled tag that has not yet found anything
produces no chip.** That is the definition working as intended — the chip row describes
what was found, not what is being looked for.

**A chip's initial state is inherited from its collection tag.** Open the page and a chip
is checked when its tag is enabled and unchecked when it is not. After that the filter is
independent: checking a chip does not resume searching, and unchecking one does not stop
a search.

**Unchecking every chip empties the list.** This is the defect that started the slice.
Today "no chip selected" means "no filter" and shows everything; it will mean "show
nothing", because a chip is a unit of visibility and turning all of them off is a
coherent thing to ask for.

### 4.3 The distinction the server cannot see for free

A form submits only its **checked** boxes. So "the user unchecked everything" and "the
user has just opened the page" arrive at the server identically — as a request with no
`tag` values at all — and they must mean opposite things.

**A hidden marker field inside the chips container resolves it.** `hx-include=".chips"`
carries it along with the chips:

| Request | Meaning | Predicate |
|---|---|---|
| no marker | fresh page — inherit from the collection tags | `EXISTS (link to a tag with is_enabled)` |
| marker, some chips | show what these tags found | `EXISTS (link to a tag in the set)` |
| marker, no chips | show nothing | false |

The marker must also reach `_page_url`, so that "I deliberately hid everything" survives a
reload and a saved link. The address describes the state of the display; this is part of
that state.

The repository already has a close relative of this problem and solves it the same way: a
cleared text filter arrives as `""`, which filters like the default but does not compare
equal to it.

### 4.4 One checkbox instead of two

Today there are two: `include_disabled_tags` («вакансии выключенных тегов») and
`include_untagged` («найденные ранее»). Under the new model both answer one question —
*show me what no chip can reach* — and they collapse into a single `include_unchipped`.

The label must not use the word «активные», which the chips have already claimed for
"checked". **«показать вакансии, у которых нет тега фильтра»** — a pair reaches this
category when it has no tag link at all, or its only links point to tags that are no
longer collection tags.

It is an **added term, not an override**: the predicate is `(chip condition) OR
(no reachable tag)`, so ticking it never widens what the chips themselves say. With every
chip unchecked and this box ticked, exactly the unchipped vacancies show.

The second half of the category is empty until soft deletion exists (§4.6). It is named
anyway, because the checkbox has to mean something stable rather than change meaning later.

### 4.5 Query parameters and filters

`VacancyFilters` gains `tags_set: bool` (the marker) and renames the two booleans of §4.4
into one. Both `/vacancies` and `/vacancies/rows` accept them, both build filters through
`_load_page` as they already must, and `_page_url` carries `tags_set` so the state
survives a reload.

### 4.6 Deletion, and why it now refuses

`jobhunt tag remove` is `session.delete(tag)`, and `profile_vacancy_tags.tag_id` carries
`ON DELETE CASCADE`. Deleting a tag therefore destroys every record of which query found
which vacancy — 1766 links in one live test during a previous iteration.

The filter model of §4.2 stands on those links. A filter tag whose collection tag is gone
is only meaningful if the link survived; after a hard delete the vacancy has no tag at
all, and no chip and no checkbox can bring it back.

**So `tag remove` starts refusing**, naming the number of links it would destroy and
saying that soft deletion does not exist yet. Five lines, and the model has no hole in it.
Soft deletion is a later slice; until then the "tags that are no longer collection tags"
category is honestly empty rather than deceptively reachable.

## 5. The collection indicator in the shell

**The requirement.** Start a big collection on «Сбор данных», walk over to «Вакансии»
without waiting. The run must stay visible, and when it ends the table must refresh
itself — on whichever page the user is standing.

**Why this is not client state.** The run already survives page navigation, tab closing
and a container restart, because it is a `parse_batches` row rather than anything in a
browser. That was slice 2b's central decision. What is missing is only that every page
should ask.

**The mechanism, which already exists and only moves.** While a batch is running the
fragment carries `hx-trigger="every 3s"`; the first response after it ends does not, and
htmx stops polling by itself. That last response carries `HX-Trigger: jobhunt-collected`,
which the filters form on «Вакансии» hears and re-requests the rows with the current
filters.

**Exactly one poller at a time, chosen by the page.** Two routes over one shared reader:

- `GET /collection/panel` — the full panel: buttons and progress. Rendered by «Сбор данных».
- `GET /collection/indicator` — a compact line for the shell. Rendered by every other page.

Both read `load_state`, both attach `HX-Trigger` by the same rule, and the context is built
by one function so the two cannot drift — the same discipline `panel_context` already
follows for the page and the fragment.

**The existing routes move with them.** `GET /vacancies/collection` becomes
`GET /collection/panel`, and `POST /vacancies/collect` becomes `POST /collection/start`:
the collection buttons no longer live under `/vacancies`, and an address that says
otherwise would be the only remaining claim that they do. Both are fragment endpoints
that nothing bookmarks, so there is nothing to redirect — but the panel template, the
error-handler path and the tests that name them all move together, and the swap-target
invariant is what catches a half-finished rename.

**What remains uncovered, and is not a defect of this slice.** An idle page still does not
poll, so a page left open will not notice a run started afterwards in another tab or from
the terminal. The owner's scenario is covered, because walking to another page is a full
page load and the new page renders the run in progress. Constant idle polling is a price
the design has twice declined to pay; the limitation is recorded in `HANDOFF.md` §6.

## 6. The CSS layer — **NOT BUILT IN THIS SLICE, 2026-08-06**

> **Dropped by the owner, and this section is history rather than a prescription.**
> The plan's Task 6 carries the same banner; this one was added after the whole-branch
> review noticed the section had none, while `docs/HANDOFF.md` §0 points the next
> session here for the visual slice. Read the rest of this section as the state of the
> question **before** the work, not as the design to implement.
>
> **The build below was chosen for a property this markup cannot use.** Pico's
> *classless* build was picked because it switches themes on `data-theme` — true, and
> not distinguishing: its actual distinguishing feature, `header`/`main`/`footer`
> acting as containers, is **inert here**, because `<main>` is not a direct child of
> `<body>` and Pico's `body>main` rules never match. What it costs is real: the
> classless build has **no `.secondary` opt-out** (verified — all 53 occurrences of the
> word in the vendored file are variable names), so every button rendered primary-blue,
> «Показать ещё» and the theme toggle included. Pico's *default* build has
> `.secondary`, `.outline` and `.contrast` and the same `[data-theme]` switching, at
> 83 KB against 71 KB. All of this was established by implementing the task
> (`c8cc50f`) and reverting it whole (`7abf211`); the separability clause at the end of
> this section is what made that cost almost nothing.
>
> **What the visual slice should start from instead:** **Bulma** matches this project's
> theme toggle exactly — `data-theme` on any element **plus** a `prefers-color-scheme`
> fallback inside its own CSS, so the three-state toggle needs no change — and ships
> **no JavaScript at all**, which removes the htmx re-initialisation question rather
> than answering it. And **no table library leaves a server-rendered `<table>` on
> screen**: seven were verified by download, all render rows from JSON once
> initialised, free server-side modes included. That is evidence **for** §9, not
> against it — see the `docs/HANDOFF.md` §6 row. The owner's decision: the server keeps
> rendering the table, and the visual layer becomes a slice with its own design
> document.

172 lines of hand-written CSS become a vendored stylesheet, served from
`web/static/` exactly as `htmx.min.js` already is — a file, a link tag, no build step and
no package manager. The prohibition in `CLAUDE.md` is on dependency managers, and htmx is
the precedent for vendored assets.

**Pico.css is the candidate**, for a specific reason: it switches themes with
`data-theme="light|dark"` on `<html>`, which is exactly the attribute the existing theme
toggle already writes. The dark theme that was built and checked in a browser survives
almost unchanged.

**The known risk.** This changes the appearance of everything at once, and slice 2a's live
check already found once that new elements had been left without styles. The chips, the
collection panel and the status cells must be reconciled against the framework's variables
and walked in a browser, in both themes.

This task is separable from the rest of the slice if it needs to be dropped.

## 7. Errors and edge cases

**No profile.** Both pages render with their controls disabled and say why. The collection
panel already distinguishes "no profile" from "no enabled tags" as of the last review.

**A profile with no collected vacancies.** «Вакансии» shows the empty state; the chip row
is empty because there are no links to derive chips from. The **container** still has to
be present — the filters and the search collect their fields from it by class
(`hx-include=".chips"`), and no invariant covers that. The **marker inside it must not**:
a row that never offered a chip cannot have had one cleared, and sending the marker anyway
makes every filter interaction on such a page answer «отметьте хотя бы один тег выше»,
pointing at an empty row. (Corrected during the review of task 5. The earlier reason —
"or the swap-target invariant breaks" — was wrong: nothing declares `hx-target` on the
chips container, and the invariant reads only `hx-target` and `hx-swap-oob`.)

**Every chip unchecked.** The table explains itself — «все теги фильтра сняты» with a way
back — rather than showing a bare header. Silence on an empty list was slice 2a's second
Critical and the class is guarded by a test.

**A run in progress during a page switch.** The new page renders the panel or the
indicator in its running state and resumes polling. No state is carried between pages.

**A run that ends while the user is on «Сбор данных».** `jobhunt-collected` fires and
nothing listens, because there is no table on that page. Walking to «Вакансии» afterwards
is a full page load, so the table is fresh regardless.

## 8. Testing

**The swap-target invariant now covers two pages.** Every htmx target declared in a
template must exist in the rendered document — checked for «Вакансии» and «Сбор данных»,
with vacancies and without, and with a run in progress (that last state is the only one in
which the panel declares a target on itself).

**The tag model needs tests that fail on the old behaviour**, or they prove nothing:

- no marker → the list matches the enabled tags;
- marker with an empty chip set → empty list, with the explanation rather than a bare header;
- marker with chips → those tags' vacancies, regardless of `is_enabled`;
- a chip's initial state follows `is_enabled`;
- a tag with no links produces no chip;
- the marker reaches the pushed address.

**`tag remove` refuses**, and the test asserts the tag and its links are still there
afterwards — a refusal that does not actually refuse is the failure mode.

**Web tests move with the fragments they cover.** The tests that fetch the collection panel
from `/vacancies` move to `/collection`.

**A browser pass**, in the shape of §5в and §5г of `HANDOFF.md`: switching pages keeps the
selected profile; a run started on «Сбор данных» is visible on «Вакансии» and refreshes
the table there when it ends; unchecking every chip empties the list and one click brings
it back; both themes are legible after the CSS layer lands.

## 9. Decisions and rationale

**Why not React.** Measured on the production database: a filter change costs 5.9 ms, a
search 6.0 ms, the whole page 10.1 ms. The search field already debounces at 250 ms — forty
times the cost of the request it delays. Client-side filtering is genuinely faster per
keystroke and the difference is imperceptible, because the wait is dominated by a delay we
chose.

The scaling argument is the real one, and it points the other way from the intuition:
server-side cost is bounded by `PAGE_SIZE`, client-side cost grows with the total. At 1000
rows the server still renders 50; the client must ship and hold all 1000. Client-side
filtering and server-side pagination are mutually exclusive, and this project already
paginates because one broad tag on work.ua reported 13 342 vacancies.

What React actually offers is a component model for managing **client state** — state that
lives in a tab and dies with it. Both scenarios raised against this design were server
state: a running collection (already in the database, already surviving restarts) and a
setting that must outlive a restart (which is a database row under any framework). Neither
is made cheaper by React.

**The named trigger for revisiting it**, so that this is a decision and not an indefinite
deferral: the first screen whose state must live in a tab. The resume editor and the AI
interview qualify and would fit as islands. Matching with live re-ranking does not fit as
an island — it drives the main table — and would mean moving that page wholesale.

**Why islands are not an antipattern, and when they become one.** Islands are a named
pattern, and they hold while an island is a leaf: local state, no say over the address, no
shared state with the page. They become the antipattern the owner suspected when an island
starts driving the page, when islands multiply until routing is the only server-side part
left, or when the same data is serialised twice. Two or three islands is a design; half a
page is a mistake.

**Why no table library.** Grid.js, Tabulator and DataTables want to own the data and render
it client-side, which contradicts the invariant that every condition goes to the database
and only `PAGE_SIZE` rows come back. The features one might want from them — column
sorting, bulk selection — are server-side and small. Virtual scrolling is meaningless at
this size.

**Why the profile selector moves to the shell.** It applies to both pages. Leaving it on
one of them would make that page the implicit owner of a global choice.

**Why chips inherit rather than mirror.** Inheriting gives the collection state a voice in
what the page shows first, without coupling the two: the chip is visible and one click
away, so nothing disappears silently — which was the objection to the old behaviour, where
a disabled tag hid rows with no visible control to bring them back.

## 10. Open questions

None blocking. Two worth a decision when the next slice is planned:

- **Soft deletion of tags**, which turns §4.4's second category from empty into real.
- **Sorting and bulk status change** — both server-side, both small, neither belongs here.
