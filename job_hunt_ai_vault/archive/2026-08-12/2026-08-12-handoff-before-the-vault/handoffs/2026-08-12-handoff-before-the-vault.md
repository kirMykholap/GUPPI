# State handoff — Job Hunt AI

**Date:** 2026-08-12
**Branch:** `main`. **The visual slice is merged** — `57ffc72`, `--no-ff`, 8 commits from
`20a7552`; the merged tree is identical to the branch tip and the 605-test run was repeated
on `main` after the merge. `feature/visual-layer` is kept as the record of the slice; there
is no remote, so nothing was pushed. Slice 3 is merged — `6a7bff4`, `--no-ff`, 26 commits
from
`033e5e0`; the merged tree is identical to the branch tip, so the 598-test run that
preceded the merge still describes `main`. Slice 2b was merged on 2026-08-05 (`0020fee`,
26 commits from `98f887e`, `--no-ff`) and 2a earlier the same day (`51bd4dd`, 38 commits
from `be5de2b`).
**State:** slice 3 (the shell and two pages) is **complete and on `main`**: seven tasks,
six of which shipped, each reviewed by an independent reviewer; the live check walked 9
browser scenarios of 9 (section 5е); the full suite is green at **598 tests**,
`ruff check` and `ruff format --check` are clean, the working tree is clean, and the
whole-branch review — three reviewers with different lenses — found one Critical and
fourteen Important, all fixed in two waves (code and tests in `dd1b446`, documentation in
`3ba285f`). Task 6, the vendored stylesheet, was dropped by the owner and is a slice of
its own.

> **The Critical's fixes were never re-reviewed by an agent, and will not be.** The
> session ended before that round could run; on 2026-08-11 the second opinion was given
> instead by the controller reading `dd1b446` in the main session — the whole chain, code
> and templates — and it found nothing. What was checked: the chain is causal rather than
> raced (one listener on `jobhunt-collected`, the rows waiting on the chips response's own
> `HX-Trigger-After-Swap`); `from:body` is right because `outerHTML` removes the
> requesting element before htmx fires the event, which is also why `#collected-refresh`
> sits outside the chip row; `vacancy_chips` re-renders the same template, so the new row
> brings its own trigger and a second run behaves like the first; and
> `hx-include="#filters, .chips"` loses nothing, because the search field is inside the
> form. Add to that the removal checks quoted in `.superpowers/sdd/final-review-fixes.md`.
> **This is the first application of the rule section 0.6 is about**: a 5–35 minute agent
> round trip bought nothing here that reading the diff did not.

> **The process was recalibrated on 2026-08-11 and the rules now live in `CLAUDE.md`,
> section «How a slice is executed».** Section 0.6 below is kept as the reasoning and the
> measurements behind that decision, not as a list of open proposals. Read `CLAUDE.md`
> for what to do; read 0.6 for why.

## ▶ What the next session does first

**Split this file.** The owner's diagnosis, 2026-08-12: `docs/HANDOFF.md` has become a
knowledge base wearing a handoff's name, and an agent has to read all of it before it can
start. It is ~120 KB. That cost is paid at the beginning of every session, by every agent,
whatever the task.

The shape he asked for:

- **`docs/HANDOFF.md` stays a handoff and nothing else** — what was done last session, what
  was not, what is handed over, what to watch. One page. If it does not change between
  sessions, it does not belong here.
- **Everything else becomes a knowledge base of several documents.** The material is already
  sorted by kind and only needs homes: §6 «Известные ограничения» (deliberately deferred,
  each with its consequence), §7 «Уроки процесса» (classes of failure, not incidents), §0.1
  environment, §0.6 process measurements, the invariants scattered through §1–§5, and the
  decisions-not-to-relitigate that currently live in three places.
- The owner wants to run this through **Obsidian**, and named «second brain by Karpathy» as
  the method. **Ask him what he means before designing the layout** — the widely known
  «Building a Second Brain» is Tiago Forte's PARA, and Karpathy's writing on notes is a
  different thing. The answer decides whether the split is by kind, by project phase, or by
  a linking convention, and that is the whole design.
- Note that `CLAUDE.md` already holds the rules that are *enforced* (boundaries, commands,
  how a slice runs). The knowledge base holds what is *known*. Do not duplicate: a fact in
  both places will disagree with itself within two slices — this file has done it three
  times already, each one recorded in §7.

**Then ask him whether he has started opening `/vacancies`.** That is the success criterion
the visual slice was built against, and nothing else measures it.

---

This is the entry point for the next session. Read top to bottom.

> **Language note.** Section 0 is in English per `CLAUDE.md`; sections 1–8 predate that
> rule and stay in Russian until something substantially rewrites them. Do not
> mass-translate them.

## 0. Where to start in the next session

**Slice 3 is merged and needs nothing further.** The closing pass ran in full: 598 tests
green, `ruff check` and `ruff format --check` clean, a whole-branch review by three
reviewers with different lenses, and their findings fixed in two waves — code and tests
first (`dd1b446`, report `.superpowers/sdd/final-review-fixes.md`), then the documents
(`3ba285f`, report `.superpowers/sdd/final-review-doc-fixes.md`). Do **not** re-run that
pass. The merge is `6a7bff4`; the suite and both `ruff` commands were re-run against the
branch tip immediately before it, and the merged tree is byte-identical to that tip.
`feature/shell-and-two-pages` is kept as the record of the slice — there is no remote, so
nothing was pushed.

**The process question 0.6 raised is settled**, on 2026-08-11: the code is written in the
main session against the plan (`superpowers:executing-plans`), review stays with agents and
keeps its whole cycle, the final three-lens review stays, the browser walk stays per task
but is walked here rather than inside an agent, and a Minor finding is never dispatched.
The rules are in `CLAUDE.md`; 0.6 keeps the measurements that produced them.

**The visual layer was the next slice and it is built**, on `feature/visual-layer`, seven
tasks, spec and plan under `docs/superpowers/`. It did **not** vendor a framework — the
approach chosen was to grow the hand-written palette into a small design system, because
slice 3's Task 6 had already implemented, reviewed, walked and reverted a vendored one, and
three of the owner's four complaints are not what a framework fixes. What it changed:

- the stylesheet is a file, `src/jobhunt/web/static/app.css`, and a token layer (spacing,
  type, radii, an accent kept separate from `--link`, the row tints, one hue per status)
  lives in all three theme blocks;
- titles are weight rather than link-blue, the header has a bottom edge, the navigation
  moved left **in CSS with `order`** — document order stays content-before-navigation for
  the screen reader — and rows alternate instead of being ruled;
- seven columns became six: «Теги» joined the source on one muted line under the title;
- the status keeps its native `select` and gains `data-status`, which colours it;
- the filters became one panel of three rows, and «показать вакансии, у которых нет тега
  фильтра» became «без тега фильтра» with the sentence moved into `title`;
- the chips lost the native checkbox and are pills coloured from `:has(:checked)`, with an
  `@supports` fallback that puts the box back.

The success criterion the owner set is not «it looks designed» — it is **that he starts
opening `/vacancies`**. That is the thing to ask him about next.

**The final review was skipped, by the owner's decision on 2026-08-12.** `CLAUDE.md` asks
for three reviewers with different lenses at the end of a slice, and that step is what found
slice 3's Critical. It did not run here. What did run: an independent test cycle per task
with every literal-scanning assertion shown red by breaking exactly what it guards, a full
suite per task, and a browser walk per task in the main session. Treat the slice as
unreviewed by a second party, and weigh that if something in the interface behaves oddly.

Note that the spec Task 6 pointed at, `2026-08-06-shell-and-two-pages-design.md` §6, carries
a banner saying it is history: the reasoning inside it chose Pico's classless build for a
property this markup cannot use, and that is exactly what the abandoned implementation
disproved.

**What slice 3 changed.** The single `/vacancies` page became a shell — navigation and a
profile selector in `base.html` — with two pages behind it, «Вакансии» and «Сбор данных»,
and the tag model was rebuilt so that «искать впредь» and «показывать сейчас» stop sharing
one word.

- `jobhunt tag remove` **refuses** and names how many `profile_vacancy_tags` links it would
  have destroyed, pointing at `tag disable` instead. Soft deletion does not exist yet.
- Two page routes; `GET /collection/panel` and `POST /collection/start` replacing the old
  `/vacancies/...` fragment addresses; and two fragment routes that are new rather than
  renamed, `GET /collection/indicator` and `GET /vacancies/chips`. The tag toggle no longer
  carries the filter chips out of band: the two controls are now on different pages, so the
  fragment could never find its target and htmx would have written an out-of-band error to
  the console.
- A compact collection indicator in the shell, so a run started on «Сбор данных» stays
  visible on «Вакансии» and refreshes the table there when it ends.
- `list_filter_tags` — the chips are derived from what has actually been found, not from
  the tag list.
- The filter model: a hidden `tags_set` marker so that «снял все чипы» and «только открыл
  страницу» stop arriving identically, one `include_unchipped` checkbox replacing two, and
  the chip row inheriting its initial state from `ProfileTag.is_enabled`.
- **The end of a collection resets the chip row and only then re-reads the table** — the
  whole-branch review's Critical, fixed in `dd1b446`. `#tag-chips` asks `GET
  /vacancies/chips` for a fresh row, that response announces its own swap with
  `HX-Trigger-After-Swap: jobhunt-chips-reset`, and a small stable element
  (`#collected-refresh`) hears the announcement and requests the rows. The filters form no
  longer listens for `jobhunt-collected` at all: two listeners on one event raced, and the
  losing order hid what the run had just found. The refresh is answered with
  `HX-Replace-Url`, not `HX-Push-Url` — see the paragraph below.

**M8 is closed, and it is not a limitation of this slice.** The ledger's M8 was «the end
of a collection writes a browser-history entry with no user action», measured live during
Task 7 at `history.length` 44 → 45. The fix is not a tighter string comparison: the
collection-end refresh sends `after_collection=true` and `vacancy_rows` answers it with
**`HX-Replace-Url`**. The address still has to follow the screen — the chips have just
been reset, so leaving the old address means the next reload restores the stale set, the
same defect from the other side — but nobody navigated, and `replaceState` is exactly that
pair. Measured after the fix, in Edge on the production database on 2026-08-06:
`history.length` **50 → 50** with the address rewritten to the reset chip set. §5е still
records the pre-fix measurement as the state Task 7 found; the row there now says so.

**The slice has seven tasks, not the eight this section used to claim.** Tasks 5 and 6 of
the plan were one atomic change split across two commits — the commit in between is one
where `/vacancies` answers 500 — so they were merged before execution and the old Tasks 7
and 8 became 6 and 7.

**Task 6, the vendored stylesheet, was dropped and is now a slice of its own.** It was
implemented against Pico CSS, reviewed, walked in a browser and then reverted whole
(`c8cc50f`, reverted by `7abf211`); the plan's separability clause is what made that cost
almost nothing. The interface therefore still wears the hand-written palette in
`base.html`, unchanged from before the slice. Three things the abandoned implementation
established, so the visual slice starts from evidence rather than from scratch — all three
verified against the downloaded files, not from blog copy:

- **The build was chosen for a property this markup cannot use.** Pico's *classless* build
  was picked because it switches themes on `data-theme`, which the existing toggle already
  writes — but its distinguishing feature, `header`/`main`/`footer` acting as containers,
  is **inert here**, because `<main>` is not a direct child of `<body>`. What it costs is
  real: it has no `.secondary` opt-out (all 53 occurrences of the word in the file are
  variable names), so every button rendered primary-blue, «Показать ещё» and the theme
  toggle included. Pico's *default* build has `.secondary`, `.outline` and `.contrast` and
  the same `[data-theme]` switching, at 83 KB against 71 KB.
- **No table library leaves a server-rendered `<table>` on screen** — see the section 6
  row. This is what turned the styling task into its own slice: the owner asked what a
  larger component library would give, and the answer changed the question.
- **Bulma matches this project's theme toggle exactly** — `data-theme` on any element plus
  a `prefers-color-scheme` fallback inside its own CSS, so the three-state toggle needs no
  change — and ships **no JavaScript**, which removes the htmx re-initialisation question
  rather than answering it. daisyUI's plain CDN file is already compiled and uses the same
  `data-theme`, at 1.1 MB. Icons are a separate, cheap decision: individual SVGs in a Jinja
  macro, `currentColor` already baked in, rather than a 0.5–1.8 MB sprite for twenty glyphs.

**A review finding that outlived the revert: no test fetched `/static/`. Closed on
2026-08-12 by the visual slice.** The whole suite stayed green if the static mount was
removed, the directory renamed, or a file dropped from the image — and every page then
rendered completely unstyled. Three assertions close it, and they are three because the
guarantee has two halves: `tests/integration/test_web_static.py` holds that
`/static/app.css` and `/static/htmx.min.js` each answer 200, and
`test_both_pages_link_the_stylesheet` in `test_web_shell.py` holds that the document asks
for the stylesheet at all. A served file nobody links is as unstyled as a missing one.

**Four things from this slice worth carrying past it, because each is a class rather than
an incident:**

- **The swap-target invariant was vacuous for a slice and a half.** `base.html` carries the
  literal `<div id="collection">` in prose inside a `<script>` comment, and the id-presence
  check searched the whole response, so the target counted as satisfied on every page. The
  invariant that exists because htmx fails silently was itself failing silently. A test
  that scans text for a literal must be shown to fail — section 7 already says this twice
  in other words, and this is the third time it was paid for.
- **The collection indicator hung on one value with no test at all.** `"page": "vacancies"`
  in the fragment route's context: flip it and the whole suite stays green while the
  indicator goes blank mid-run and the table never learns the run ended. The only request
  to that route in the tests used a *finished* batch, so the running response — the one the
  feature is — was never rendered. Closed by one test, proven by injecting exactly that flip.
- **Four chip tests were green for the wrong reason.** Without the marker `tag_ids` was
  ignored, so each had silently become a test of the enabled-tag predicate instead of the
  chip set. Third instance of this failure mode in the project's history.
- **The empty state pointed at a control that could not help, in three different
  situations**, each found by a different pass: every tag disabled *and* every chip cleared
  (the cure is the chip row directly above the table, not the far page); a profile whose
  chip row is empty (the marker claimed a chip set had been cleared, pointing at nothing);
  and the same page reached by a hand-typed `?tags_set=true`. The lesson is that an empty
  state is a branch like any other and needs its cases enumerated, not one message written
  for the case that prompted it.

**Decisions from the design conversation that the next session should not relitigate**,
all recorded with their reasoning in spec §9: the stack stays htmx (a filter change costs
5.9 ms against a 250 ms debounce; server cost is bounded by `PAGE_SIZE` while client cost
grows with the total); React arrives as islands, and only when a screen's state must live
in a tab rather than in the database — the resume editor and the AI interview qualify,
matching with live re-ranking does not and would mean moving that page wholesale; no table
library, because they all want to own the data client-side; and a vendored stylesheet is
not a dependency, which is how `htmx.min.js` already ships.

> **This slice's research strengthens spec §9 rather than correcting it.** Seven table
> libraries were verified by downloading and grepping the files, and **none of them leaves
> a server-rendered `<table>` on screen** after initialisation — free server-side modes
> included. That is the same objection §9 already raised, now measured: they «want to own
> the data and render it client-side, which contradicts the invariant that every condition
> goes to the database and only `PAGE_SIZE` rows come back». See the section 6 row.
>
> **Corrected 2026-08-06.** This block used to say §9 «rejected table libraries on the
> ground that they cannot filter server-side» and that the ground was wrong. **§9 says no
> such thing** — the paragraph two above summarises it correctly, and the two contradicted
> each other on the same screen. The false attribution came from the plan's Task 7 and was
> copied into three documents; all three now say this. What is true and narrow: several of
> the seven *do* filter server-side, for free, and it does not help.

**Two follow-ups the 2b review left as rows in section 6**, neither blocking: the progress
heartbeat is written once per source+tag pair rather than per request, which is why
`STALE_AFTER` had to be widened to half an hour instead of tightened — the real fix needs
a progress signal in the `BaseParser` contract; and the test database is built from the
models by `Base.metadata.create_all` and therefore never follows a migration, which
already cost a hand-written `ALTER TABLE` during 2b and will recur on the next migration.

**Ledgers.** `.superpowers/sdd/progress.md` is the ledger of the **current** slice — read
its Minor list before deciding a finding is new, and its «Task 6 dropped» section before
picking up the visual slice. `.superpowers/sdd/progress-collection-from-the-browser.md` is
2b's, renamed when slice 3 started its own.

### 0.1 Environment

- **`uv` is on PATH.** `uv.exe` lives in the per-user scripts directory
  (`%APPDATA%\Python\Python314\Scripts`), which was added to the user PATH.
  Commands are plain `uv run ...`; `python -m uv run ...` still works everywhere and
  stays documented as the fallback.
- **Playwright MCP now points at Edge — it takes effect in the next Claude Code
  process.** As installed it defaulted to the `chrome` channel and failed with
  `Chromium distribution 'chrome' is not found`: this machine has no Chrome, and Edge
  is what the owner actually uses. The user-scope entry was rewritten to
  `npx -y @playwright/mcp@latest --browser msedge` on 2026-08-05; a server already
  running keeps its old arguments, which was confirmed rather than assumed.
  Playwright drives that Edge (engine 151.0.4129.59, checked against the running app:
  page, htmx swap, one search request).
  The fallback that needs no MCP at all is a direct Playwright script —
  `npm i playwright` in a scratch directory, browsers come from the cache. That is how
  the 5в checklist was walked.
  **Read the harness traps in 5в, 5г and 5е before writing another browser check.** They
  have now cost three slices between them: Cyrillic typed through `insertText` fires no
  `keyup` and the search looks dead; a first batch of 50 is not a full list; collection
  runs are shorter than hand timing; and one tool call's observation of the *previous*
  tool call's page state is seven-plus seconds late, which is half a run. The single rule
  that covers the last two: **issue the action and its observation in the same call, or
  record the timeline in the page and read the recording afterwards.**
- **`/favicon.ico` returns 404 and Edge writes it to the console** (chromium stays
  quiet about it). No route serves an icon. Cosmetic, but it means «ошибок в консоли
  нет» has to be read as «кроме favicon» in Edge.
- **Docker Desktop is often not running** — see the Russian section 2 for the symptom
  and the way up.

### 0.2 What slice 2a ended with

Merged as `51bd4dd`. The three items the previous session left open are all closed:
the browser checklist (10 of 10, section 5в), the double request on search (the
filters form's trigger now names its sources instead of catching a bubbled `change`;
guarded by `test_filter_form_does_not_fire_on_a_bubbled_change`, which fails on the
old markup), and section 7 of the 2a design, reconciled with the code — including the
`hx-push-url` prescription that had caused Critical C1, so that a design read later
cannot re-prescribe it.

**A loose end for the first live collection after this merge:** one
`parse --mode full` was already done on 2026-08-05 for the salary re-parse (see the
end of section 0.5) — do not repeat it. Nothing else is pending on the data side.

### 0.3 What the final whole-branch review found

Worth reading before touching htmx again: two Criticals, invisible from inside any
single task, both at the seam between htmx and the templates.

- **A saved link did not open.** `hx-push-url="true"` puts the *actual request URL* in
  the address bar, so after the first filter change the address became
  `/vacancies/rows?…`, and reopening it returned a bare set of `<tr>` with no page
  around it. A defect of the **spec and the plan**, not of the implementation: both
  prescribed the attribute on a wrong reading of its semantics. Fixed with an
  `HX-Push-Url` header from the fragment route; the now-dead attributes were removed
  rather than left, because a future branch returning 200 without the header would have
  resurrected the defect silently. A later guard also redirects a fragment URL opened as
  a page, since the header cannot undo addresses already in bookmarks and restored tabs.
- **On an empty list the filters were dead silently.** `<tbody id="rows">` sat inside
  `{% if rows %}` while the form, the chips and the search all target `#rows`. No rows,
  no target — htmx raised `htmx:targetError` and sent no request at all: nothing on
  screen, nothing in the network panel. For a profile with every tag disabled, the
  "вакансии выключенных тегов" checkbox — the remedy that state exists for — did
  nothing. The other side of the same bug: narrowing a filter to zero left the table
  header with no explanation, because all four empty-state messages lived in
  `vacancies.html` while htmx swaps `_rows.html`.

An invariant test now guards the class: **every htmx swap target declared in a template
exists in the rendered page**, checked for a profile with vacancies and for one without.
This matters directly for 2b, which adds new fragments.

### 0.4 What slice 2b built, and what it decided along the way

Every open question section 0.4 used to list is now answered in the spec. The short
version, because the next session will act on it before it reads anything longer:

- **The container talks to the internet.** A press on `/vacancies` starts a daemon
  thread in the app process which calls the same `run_profile` the CLI calls.
- **A restart interrupts a run rather than resuming it** — the owner's decision, and
  it is what makes a thread sufficient and a job queue unnecessary.
- **The state of a run lives in the database, never in process memory.** A new table
  `parse_batches`, one row per run; a **partial unique index** permits one `running`
  batch per profile. That is the guard against a second press, and it is also why a
  run started from the terminal disables the buttons on the page: `jobhunt parse`
  opens a batch of its own.
- **Progress is read from rows the runner already commits.** `run_source` now commits
  its journal row as `running` *before* the request — that is what made "идёт прямо
  сейчас" observable at all. The cost is dangling rows after a crash, closed by the
  staleness rule (half an hour, see `STALE_AFTER`) and by `jobhunt sweep-batches` at container start.
- **The batch is closed by `run_profile` and by nobody else**, and a crashed run
  closes as `interrupted`, not `finished` — a review caught the panel reporting a
  completed collection for a run that had exploded.
- **The table refreshes itself** through `HX-Trigger: jobhunt-collected` on the
  panel's last poll; the **filters form** hears it and re-requests the rows, because
  the form is what knows the current filters and the panel is not.

Deliberately not built, and still open for later: the «условия изменились» banner
(needs a snapshot of tags and frame at run time), a schedule (that is the day the
queue becomes worth its cost), resuming an interrupted run, and cancelling a run from
the page.

This paragraph used to forecast slice 3 as «adding and removing tags from the browser,
web forms for the profile and the collection frame». **Slice 3 did none of that.** It
built the shell, the two pages and the tag model instead, and it made adding and removing
tags from the browser *harder* to reach rather than nearer: `tag remove` now refuses even
from the CLI, because deleting a tag destroys the links the chip row is built from, and a
browser button for it would need soft deletion first. Web forms for the profile and the
collection frame remain unbuilt and unplanned.

### 0.5 Records

**One ledger per slice, each renamed when the next slice starts its own.** `progress.md`
is always the ledger of the slice in flight — today, slice 3 — so a reference to it ages
the moment a slice ends. That is what happened to the four references this file used to
carry; they are corrected below and in sections 5д and 8. Newest first:

- `.superpowers/sdd/progress.md` — slice 3, the shell and two pages (**current**).
- `.superpowers/sdd/progress-collection-from-the-browser.md` — slice 2b.
- `.superpowers/sdd/progress-vacancies-as-a-tool.md` — slice 2a: every finding, every
  owner decision, and the Minor findings deliberately left to live. Read the
  "Minor-находки" section before deciding they are new.
- `.superpowers/sdd/progress-profile-scoped-collection.md` — profile-scoped collection.
- `.superpowers/sdd/progress-plan-a.md` — plan A.
- `CLAUDE.md` — language rule, commands, the five enforced boundaries, and the
  invariants worth knowing before editing.

**One `parse --mode full`** — done 2026-08-05, the previous iteration's last loose end.
Four source+tag pairs, 103 cards, 0 new, 103 updated. No salary changed: upsert
overwrites `salary_min/max/currency` on every encounter (`ingest/upsert.py`), so the
parse really was replayed by the new code, and the "currency before the number" pattern
simply does not occur in the current live cards. Do not repeat it.

### 0.6 Why the process was recalibrated — the measurements behind `CLAUDE.md`

> **Settled on 2026-08-11.** What was decided is in `CLAUDE.md`, section «How a slice is
> executed». This section is now the record of why: the numbers below are what the
> decision was made on, and they are worth keeping because the next such argument will
> want them. The proposals near the end are marked with what became of each.

**Slice 3 cost a session of eight to ten hours and the owner considers that
unacceptable for what it produced.** Their words: «столько времени тратить на отсутствие
результата — это просто ужасно». That was the sentence this recalibration answers.

**Where the time actually went**, measured from this session rather than guessed:

- Every task ran the full cycle the `subagent-driven-development` skill prescribes —
  implementer → review → fix wave → re-review. **A single agent round trip costs 5 to
  35 minutes.** Seven tasks × three or four round trips is the session.
- **Fix waves are the most expensive step**: 35 minutes for one, 30 for a task that was
  then thrown away.
- Minor findings were dispatched to agents. A 10–35 minute round trip for a one-line
  comment happened several times. The skill says to record Minor findings in the ledger,
  not to fix them with an agent — that one was the controller's own doing.
- The final whole-branch review ran **three** reviewers where the skill says one. The
  precedent came from §5д of this file, describing slice 2b. It did find a real Critical.
- A browser walk stood in almost every task's steps, written into the plan by the
  previous session.

**Where those rules come from**, since the owner asked and the answer is not "the
assistant invented them":

| Rule | Source |
|---|---|
| implementer → review → fix → **re-review**, per task | `superpowers:subagent-driven-development` — «Don't skip the re-review» |
| a broad whole-branch review at the end, most capable model | the same skill |
| full suite once per task, in the main session | **this repository's `CLAUDE.md`**, section «Tests» |
| execute slice 3 with subagents at all | **§0 of this file**, as written by the previous session |
| three reviewers with different lenses | **§5д of this file**, describing how 2b ran |

So the process is prescribed by the skill and by this project's own documents. Changing
it means changing those documents — which is entirely allowed, and is the point of this
section.

**The proposals as they were put to the owner, and what became of each:**

- **Adopted** — fix Minor findings inline in the main session; never dispatch an agent
  for one.
- **Adopted, in a stronger form** — `superpowers:executing-plans`: the same plan executed
  in the main session with no implementer subagents. This was the proposal listed last and
  it is the one that carries the saving, because it removes two of the three or four round
  trips per task rather than trimming what happens inside them.
- **Rejected** — one review per task with re-review only when a fix changes behaviour.
  Re-review stays unconditional: what the owner cut is who writes the code, not who checks
  it.
- **Rejected** — one final reviewer instead of three. Three lenses found slice 3's
  Critical, and with the implementer trips gone there is room for them.
- **Rejected** — one browser walk per slice. It stays per task, but is walked in the main
  session through the Playwright MCP, where it costs minutes rather than a round trip.
- **Rejected** — no review at all for small or mechanical tasks.

Whatever is agreed, **write it into `CLAUDE.md`** so it is a project rule rather than a
per-session judgement call.

**Two questions the owner raised there, both settled on 2026-08-12.** Their reasoning is
kept because it is what the answers were built on:

1. **Dropping the «no JavaScript of our own» rule** — **settled: allowed, presentational
   only.** The rule in `CLAUDE.md` now draws the line at what the code can affect: our own
   JS may do anything no query depends on, and may not participate in which rows are on
   screen. The reason is not the one the old rule gave; it is that **no test here executes
   JavaScript**, and a JS runner would mean npm. The boundary is the kind an AST test can
   pin, like the five that already exist, and no such test is written yet — write it with
   the first piece of JS that needs it. The owner's original argument, which stands and is
   a fair one: silent breakage is something to watch for and cover with tests, not to
   architect around. An honest correction to what this session
   claimed — of the four silent defects it found, **three were plain test-coverage gaps
   that any architecture would have had**; only the stale-chips one was genuinely
   htmx-shaped, because request state is collected from a live DOM.
2. **Whether the vacancies table should stay server-rendered** — **settled: deferred on
   purpose, and revisited after the visual slice**, against a dressed table rather than
   against an argument. Nothing is decided against a grid; the question is simply not
   ripe while the interface still wears the palette it was prototyped in. When it is
   reopened, the cheap alternative to weigh first is that sorting is an `order_by`, so a
   link in a column header buys the main thing a grid is taken for without touching the
   htmx target invariant, the per-row status control, or the HTML the fragment routes
   return. The owner's framing, which stands:
   a grid owning *presentation* is not a grid owning *data*, and the free server-side
   modes keep the database as the only filter. That is right, and the case this session
   presented against a grid was stronger than the facts support. The real cost is
   narrower than «htmx ends»: the fragment route returns JSON instead of HTML, and the
   per-row status control moves from Jinja into a cell renderer. §6 of this file carries
   the researched detail on the seven libraries.

---

## 1. Что изменилось в этой итерации

Инструмент собирает вакансии с work.ua и dou.ua в PostgreSQL, дедуплицирует их,
отслеживает исчезнувшие и показывает в локальной веб-таблице, где ведутся статусы
откликов. Матчинга с резюме ещё нет — это план B.

Итерация «профильная видимость, теги ролей, нормализация полей» сделала пять вещей:

**Отдельный слой нормализации.** Парсер извлекает только сырые строки источника
(`RawVacancy`), `jobhunt.normalize` переводит их в канонические значения
(`VacancyDTO`), `ingest` пишет в БД. Словарь значений теперь один на все источники,
и разойтись он не может — граница держится разбором AST.

**dou.ua переехал с RSS на HTML-выдачу.** Заголовок фида имел вид
`Роль в Компанія, Зарплата, Місто` с переменным числом частей, и деление по последней
запятой превращало компанию в «Антенор, $1000–3000, Київ» на любом запросе с
зарплатой. В HTML компания лежит отдельным тегом. Пагинация идёт POST-запросами на
`/vacancies/xhr-load/` с csrf-токеном из cookie.

**Видимость и деактивация стали профильными.** `missed_checks` и `is_active` уехали с
объективной строки `vacancies` на пару «профиль ↔ вакансия» (`profile_vacancies`,
бывшая `applications`). Причина: «вакансия закрыта площадкой» объективно узнать
нельзя — ни один профиль не видит всю биржу. Честная формулировка «этот профиль
перестал её находить» профильная по определению.

**Поисковые формулировки стали тегами.** `profile_tags` с признаком включённости,
`profile_vacancy_tags` хранит, каким тегом найдена вакансия. Выключенный тег перестаёт
искать; удалённый уносит связки каскадом, и вакансия становится сиротой.

**Рамка сбора и два режима.** У профиля есть города, признак удалёнки и глубина по
дате. Фильтры источника — только способ уменьшить объём; **истиной является локальная
перепроверка**, потому что промо-блок work.ua приходит мимо любых фильтров. Полная
сверка судит и пересобирает связки, быстрое обновление только собирает.

---

## 2. Как запустить

```bash
docker compose up -d --build          # БД и приложение, миграции применяются сами
python -m uv run python -m jobhunt.cli profile create --name "Кирилл"
python -m uv run python -m jobhunt.cli tag add --profile "Кирилл" --text "Head of IT"
python -m uv run python -m jobhunt.cli parse --profile "Кирилл" --mode full
```

Открыть http://localhost:8000/vacancies

**Команды целиком:**

```
jobhunt profile create --name N [--city Київ]... [--remote-only] [--depth-days 60]
jobhunt profile update --name N [--city ...]... [--remote-only/--no-remote-only] [--depth-days N]
jobhunt profile list
jobhunt tag add|remove|enable|disable --profile N --text "Head of IT"
jobhunt tag list --profile N
jobhunt parse --profile N --mode full|quick
jobhunt renormalize
```

`renormalize` перевычисляет `city`, `city_any`, `work_format` из сохранённого
`location_raw` **тем же модулем нормализации**, что и обычный сбор. Правила разбора
внутрь миграций не попали намеренно: копия правил разошлась бы с живым кодом молча.
Запускать после миграции и каждый раз, когда правило разбора поправлено, — перекрывать
площадки заново не нужно.

### Ловушки окружения

- **`uv` в PATH с 2026-08-05** (см. раздел 0.1). Обычная форма — `uv run ...`;
  `python -m uv run ...` работает везде и остаётся запасной. Подсказки пустых
  состояний на `/vacancies` намеренно печатают длинную форму: их копируют в
  терминал, который может быть старше текущего окружения.
- **Docker Desktop часто не запущен.** Признак — `cannot find the path ... dockerDesktopLinuxEngine`.
  Поднимается через `Start-Process "$env:LOCALAPPDATA\Programs\DockerDesktop\Docker Desktop.exe"`,
  дальше опрашивать `docker info`, а не спать вслепую.
- **Консоль cp1252.** Любая точка входа, печатающая кириллицу, обязана начинаться с
  `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`.
- **Переводы строк.** `docker-entrypoint.sh` с CRLF ломает запуск контейнера
  (`no such file or directory` на entrypoint) — заведён `.gitattributes` с `*.sh text eol=lf`.
  Этот дефект был в репозитории с плана A и обнаружился только сейчас: задокументированный
  способ запуска через compose не работал.
- **PowerShell в неинтерактивном режиме:** `Invoke-WebRequest` без `-UseBasicParsing`
  падает на попытке инициализировать движок IE.

---

## 3. Что где лежит

```
src/jobhunt/
├── config.py            настройки (pydantic-settings, читает .env)
├── logging_config.py    настройка логирования
├── http_client.py       ЕДИНСТВЕННЫЙ выход в сеть: GET и POST, паузы, robots.txt, кеш
├── cli.py               profile / tag / parse / renormalize
├── renormalize.py       перевычисление канонических полей из сырой локации
├── db/
│   ├── base.py          движок, session_scope, get_session_factory
│   └── models.py        Profile, ProfileTag, Vacancy, ProfileVacancy,
│                        ProfileVacancyTag, ParseRun
├── normalize/           сырые строки → канонические значения, о БД не знает
│   ├── salary.py        разбор зарплаты, валюта обязательна
│   ├── location.py      город / «любой город» / формат работы
│   ├── dates.py         даты, в том числе без года
│   ├── dto.py           VacancyDTO
│   └── __init__.py      normalize(raw, today)
├── parsers/             о БД не знает, канонических значений не производит
│   ├── base.py          RawVacancy, SearchFilters, ParseResult, BaseParser
│   ├── work_ua.py       HTML-выдача, фильтры в пути URL, пагинация
│   ├── dou.py           HTML-выдача, пагинация xhr-load, остановка по рубежу
│   └── registry.py      имя источника → парсер
├── ingest/              ЕДИНСТВЕННЫЙ, кто пишет вакансии в БД
│   ├── normalize_batch  точка перехода из сырого в канон
│   ├── scope.py         рамка сбора: filters_for / within_scope / select_in_scope
│   ├── upsert.py        вставка, дедупликация, правило про описания
│   ├── activity.py      четыре условия кандидата на пропуск, деактивация
│   ├── tags.py          связка «найдена этим тегом», пересборка связок
│   ├── runner.py        оркестрация, режимы, границы транзакции
│   ├── batches.py       ЕДИНСТВЕННЫЙ, кто пишет parse_batches: open_batch/finish_batch/touch/sweep_interrupted
│   └── summary.py       is_broad_tag, RunSummary — общее для CLI и панели определение «проблемы с прогоном»
└── web/
    ├── deps.py               get_session — FastAPI-зависимость (не session_scope!)
    ├── templating.py         ЕДИНСТВЕННОЕ окружение Jinja, auto_reload выключен
    ├── collection_runner.py  фоновый поток: start() отдаёт run_profile в daemon-поток
    ├── data/                 ВЕСЬ SQL веб-слоя; роуты в БД не ходят (граница держится тестом)
    │   ├── vacancies.py      build_vacancy_query, list_vacancies, PAGE_SIZE = 50
    │   ├── collection.py     читает parse_batches для панели: CollectionState, load_state
    │   ├── tags.py           теги профиля, переключение is_enabled, list_filter_tags
    │   └── profiles.py       resolve_profile: адрес → cookie → самый ранний; list_profiles
    ├── routes/
    │   ├── vacancies.py      GET /vacancies (страница), GET /vacancies/rows (фрагмент),
    │   │                     GET /vacancies/chips (фрагмент), POST /vacancies/{id}/status
    │   ├── collection.py     GET /collection (страница), GET /collection/panel,
    │   │                     GET /collection/indicator, POST /collection/start,
    │   │                     panel_context — единственный сборщик контекста панели
    │   │                     (в _common.py его нет и не было — там разбор параметров)
    │   ├── tags.py           POST /tags/{tag_id}/enabled
    │   └── _common.py        общее для обеих страниц: remembered_profile_id, parse_tag_ids,
    │                         resolve_page_profile, remember_page_profile
    └── templates/
        ├── base.html                 оболочка: палитра, тема, индикатор сбора, .layout
        ├── _nav.html                 навигация и селектор профиля (на каждой странице)
        ├── _collection_indicator.html компактная строка «идёт сбор» для оболочки
        ├── vacancies.html            страница «Вакансии»
        ├── _filters.html, _tag_chips.html, _rows.html, _status_cell.html
        ├── collection.html           страница «Сбор данных»
        └── _collection.html, _tags_panel.html, _tags_toggle.html
```

**Две страницы за одной оболочкой.** `base.html` держит навигацию, селектор профиля и
индикатор сбора; страницы дают только `{% block content %}`. Адреса фрагментов сбора
переехали в слайсе 3: было `GET /vacancies/collection` и `POST /vacancies/collect`,
стало `GET /collection/panel` и `POST /collection/start`. Кроме переименованных, слайс 3
завёл два **новых** фрагмента: `GET /collection/indicator` — компактная строка сбора для
оболочки, опрашивается со всякой страницы, кроме «Сбор данных», где опрашивает панель; и
`GET /vacancies/chips` — ряд чипов, который перерисовывает сам себя по окончании сбора
(см. раздел 6, строку про сброс чипов).

**Границы, которые держатся тестами, а не договорённостью:**

- `parsers/` и `normalize/` не импортируют `jobhunt.db`, `jobhunt.ingest`, `jobhunt.web`,
  `sqlalchemy` — проверяется разбором AST (`tests/unit/test_parser_boundaries.py`,
  `tests/unit/test_normalize_boundaries.py` — один и тот же список `FORBIDDEN` в обоих);
- сеть только через `http_client.py` — проверяется разбором AST
  (`tests/unit/test_network_boundary.py`: ни один модуль, кроме самого `http_client.py`,
  не импортирует `httpx`/`requests`/`urllib.request`/`http.client`);
- миграции не расходятся с моделями — `alembic check` с `compare_server_default`,
  плюс круг `upgrade → downgrade → upgrade` для каждой ревизии начиная с 0004;
- вакансии пишет только `ingest/upsert.py` — проверяется разбором AST
  (`tests/unit/test_vacancy_write_boundary.py`). Единственное узкое исключение —
  `renormalize_all`, который перевычисляет три производных поля
  (`city`/`city_any`/`work_format`) у уже сохранённых строк; ширина исключения
  закреплена тестом на синтетическом источнике, а не прогоном по заведомо
  чистому файлу (так было до ре-ревью, и расширить исключение можно было, не
  уронив ни одного теста).

**Чего границы записи и сети не ловят** — формулировка выше не должна звучать
сильнее реализации. Ловятся: конструктор по имени и по псевдониму импорта,
конструктор через атрибут модуля (`models.Vacancy`), присваивание полю (в том
числе `+=` и с аннотацией), `setattr` со строковым литералом, запись через
`update()`/`insert()`/`delete()`, импорт запрещённого модуля в любой форме,
включая `from urllib import request`. Не ловятся и не могут: вычисленное имя
поля (`setattr` с переменной), сырой SQL-текст, запись из другого процесса.
Списки исключений заданы путём от корня пакета, а не именем файла — новый
`web/upsert.py` границу не проходит.

---

## 4. Правила, которые нельзя нарушить, не сломав главное

Цикл деактивации — самая опасная логика в проекте. За две итерации его чинили пять раз,
и каждый раз дефект был одного класса: что-то тихо переставало судиться или,
наоборот, судилось без оснований.

**Четыре условия кандидата на пропуск.** Кандидатом становится пара, для которой верно
всё: вакансия этого источника и активна; связана хотя бы с одним тегом, **реально
отработавшим** в этом прогоне; попадает в текущую рамку сбора; с прошлого засчитанного
пропуска прошло не меньше 20 часов.

«Реально отработал» ≠ «включён»: тег, чей запрос упал, отработавшим не считается.

**Четыре правила самого вызова.** Пропуски отмечаются раз на источник за прогон
профиля, по объединению всех запросов. Провал любого запроса отменяет отметку для
всего источника. Пустая выдача не считается пропуском. Неполный набор идентификаторов
запрещает отмечать пропуски.

Каждое из восьми закрыто тестом, который **падает** при снятии именно этой защиты.
Если правите этот код — перепроверьте снятием защиты, а не только зелёным прогоном:
дважды за эту итерацию правка молча обнуляла доказательную силу тестов, и они
проходили по посторонней причине.

**Пересборка связок не имеет права осиротнять пару.** Связка снимается, только если у
пары остаётся связка с **другим тегом, отработавшим в этом прогоне**. Иначе пара
выпадает из-под условия 2 навсегда, порог в два пропуска становится недостижим, и
пропавшая вакансия висит в списке вечно. Этот дефект возникал дважды подряд: сначала с
предикатом «есть хоть какая-нибудь связка», потом — когда выяснилось, что связка
выключенного тега не спасает.

**Сниппет никогда не затирает полное описание.** При `description_is_full = true`
входящий сниппет игнорируется целиком. Обратный переход — подтягивание полного текста
поверх сниппета — изменением описания **не** считается: это наше уточнение, а не правка
работодателя. Смена сниппета на другой сниппет считается. Правило держится тестами
(`tests/integration/test_upsert.py`) и корректно уже сегодня — но описывает случай,
которого обычный сбор пока не создаёт: `description_is_full=true` в БД взяться
неоткуда, пока ничто в продакшен-коде не вызывает `fetch_description` (см. раздел 6,
строка про отсутствующего производителя признака полноты).

**Отсутствующее значение не затирает известное.** `posted_at` обновляется при каждой
встрече (площадка кладёт туда дату обновления карточки, а не первой публикации), но
`None` сохранённую дату не переписывает: «в этот раз дату не разобрали» — пробел в
данных, а не заявление площадки. Восстановить затёртую нечем, сырой строки даты в схеме
нет. То же правило, что и у описания, только про дату.

**Рамка сбора сверяется со всеми городами сырой строки.** dou.ua перечисляет их через
запятую («Київ, Варшава (Польща)»), и какой из них главный — источник не сообщает.
`dto.city` — первый, это поле для показа; `_violates_city` смотрит на все части
(`normalize.location.city_candidates`). Иначе профиль с рамкой «Варшава» молча терял бы
вакансию, которая рамке не противоречит, а подтверждает её непервой частью. Правило
разбиения строки живёт в одном экземпляре, в слое нормализации: копия в `ingest`
разошлась бы с ним молча.

**`applied_at` не задним числом.** Если отмечен «звонок» без отметки «откликнулся»,
поле остаётся пустым — иначе мы выдумываем событие отклика.

**Веб-роуты берут сессию через `Depends(get_session)`**, а не `session_scope()`.

---

## 5. Что проверено на живых данных 2026-08-04

Прогоны шли по боевой БД; дамп до начала снят. Профиль «Кирилл», теги «Head of IT» и
«IT Director». Опыты с широким тегом и деактивацией проводились на отдельном временном
профиле, чтобы не засорять боевые данные; после — прибрано.

| Что | Результат |
|---|---|
| Миграции 0003→0007 на данных плана A | Накатились; 55 вакансий, все пары созданы, строка отклика с `responded_at` уцелела с тем же id |
| Переразбор | 55 из 55, изменено 55, **не разобрано 0**; вакансий с непустой сырой локацией и пустым форматом работы — 0 |
| Распределение форматов | 43 офис, 11 удалёнка, 1 «вся Україна» |
| Полная сверка | `mode=full`, `total_available` заполнен у обоих источников, порядок записей журнала — теги снаружи, источники внутри |
| Быстрое обновление | Счётчики пропусков, активность и связки не сдвинулись ни на единицу |
| Широкий тег «менеджер» | work.ua заявил **13 342** вакансии, отдал 350 и упёрся в лимит 25 страниц → `truncated`, `ids_incomplete=true`, отметка пропусков **и** пересборка связок для источника пропущены с предупреждением. dou.ua: **1416** заявлено, 1416 собрано, набор полон |
| Удаление тега | 1766 связок ушли каскадом, пары и вакансии остались — осиротели, а не исчезли |
| Цикл деактивации | Пропуск 1 → отмотка метки на 30 ч → пропуск 2 → `is_active=false`, идентификатор назван в предупреждении. Возвращение в выдачу → снова активна, счётчик обнулён, метка сброшена |
| Защита от осиротения | Сработала на живых данных ровно в целевом сценарии и объяснила себя в логе |
| Выключенный тег | Вакансия, связанная только с ним, не судится — счётчик остался нулём |
| Вакансия вне рамки | Сужение рамки до «Львів» — 39 пар не оценивались, счётчик киевской вакансии остался нулём; выдача источника тоже сузилась (11 вместо 46) |
| Веб-таблица | HTTP 200, колонка «Теги» заполнена, «Дистанційно» в 13 строках, «Вся Україна» в 1, элементы смены статуса на каждой строке |

**Числа разведки из спеки подтвердились**: план предсказывал порядка 13 000 у work.ua
и порядка 1400 у dou — фактически 13 342 и 1416.

**Гипотеза спеки о порядке выдачи work.ua подтвердилась.** На живой первой странице по
запросу «менеджер»: первые 7 карточек — промо-блок, по дате не упорядочен; дальше
обычная выдача строго по убыванию. Но среди карточек с сегодняшней датой есть
идентификаторы `5549009` и `6068175` — заметно более старые, чем соседний `8379984`.
Значит **«вакансія від» — это дата обновления, а не первой публикации**. Следствие:
фильтр глубины отсекает по «когда последний раз обновляли», а не «когда впервые
опубликовали». Для поиска работы это скорее полезно (обновляют то, на что реально
ищут), но считать это датой публикации нельзя.

### Живая проверка интерактива — сделана 2026-08-05

Headless Chromium через Playwright (`npx playwright`, установлен во временном каталоге
сессии — в зависимости проекта не попал: узла сборки в проекте нет и заводить его ради
одной проверки не стали). 11 проверок из 11:

| Сценарий | Результат |
|---|---|
| Смена статуса кликом | HTTP 200, ячейка подменена htmx, документ не перезагружался (маркер в `window` пережил обмен), `new → ignored` |
| Ошибка: неизвестная вакансия | 404, в ячейке сообщение «вакансия не найдена…». Селект исчезает — пары нет, показывать нечего |
| Ошибка: недопустимый статус | 400, сообщение с недопустимым значением, селект остался и показывает настоящий сохранённый статус |
| Галочка «показывать неактивные» | На реально деактивированной паре (`is_active=false` руками): по умолчанию 56 строк, с галочкой 57, скрытая — именно она |
| Переключатель темы | Цикл `auto → light → dark → auto`, `data-theme` и `localStorage` совпадают на каждом шаге, выбор переживает перезагрузку; тёмная тема отрисована целиком |
| Фильтр по статусу | Сузил список до одной строки |
| Консоль браузера | Ни одной непредвиденной ошибки (четыре 4xx — вызваны намеренно в двух пунктах выше) |

Данные возвращены в исходное состояние: статус вакансии обратно `new`, пара снова
активна, `missed_checks` не сдвинулся.

Замечание для слайса 2a: на пути 404 ячейка теряет `<select>` до перезагрузки
страницы — сообщение прямо просит её обновить. Это следствие того, что пары нет и
подставить в селект нечего; при 400 селект остаётся.

---

## 5б. Что проверено на живых данных 2026-08-05 (слайс 2a, серверная половина)

Проверка шла запросами к поднятому приложению на боевой БД (профиль «Кирилл», 57
вакансий, теги «Head of IT» и «IT Director»). Данные, которые проверка меняла, возвращены
в исходное состояние и сверены.

| Что | Результат |
|---|---|
| Страница открывается на боевых данных | 200, строки на месте |
| Чип сужает список | строк меньше, все связаны с этим тегом (сверено с БД) |
| Выбранный чип отмечен `checked`, остальные — нет | верно |
| Кнопка «показать ещё», `offset` в её URL, отсутствие на последней пачке | верно |
| Число строк под фильтрами города и `work_format=remote` | сходится с прямым `SELECT` |
| Чип не отменяет остальные фильтры | результат — пересечение, сверено с БД |
| Кнопка не теряет чип и фильтр | оба параметра в её URL |
| Переключатель тега меняет БД и отдаёт только панель | верно, таблица не приходит |
| Пусто по фильтрам объясняет себя | «ничего не найдено» + ссылка сброса |
| `?profile=<чужой uuid>` | 404 **с объяснением**, не 500 и не подмена |
| `?tag=не-uuid` → 400, `?offset=-1` → 422 | верно |
| Смена статуса возвращает только ячейку | `<select` есть, `<tr` и `<html` нет |

Отдельно перепроверено после правок финального ревью: заголовок
`HX-Push-Url: /vacancies?status=applied` при `offset=0`; заголовка **нет** при
`offset>0`; `id="rows"` присутствует на странице; пустой фрагмент объясняет себя;
догрузка за пределами выборки возвращает пустоту без ложного пустого состояния;
мёртвых `hx-push-url` в шаблонах не осталось.

Единственный дефект, найденный этой проверкой, — отсутствие CSS у элементов,
введённых задачами 3–8 (чипы, панель тегов, кнопка, селектор профиля). Закрыт:
стили описаны существующими переменными палитры, поэтому обе темы работают сами.

## 5в. Browser checklist — **walked 2026-08-05, 10 of 10**

Headless Chromium (Playwright, browser from the cache the previous session left; the
project still has no Node dependency of its own) against the running app on the
production database. The script and its output live in the session scratchpad, not in
the repository. Profile «Кирилл», 57 pairs, tags «Head of IT» (53) and «IT Director»
(51). A second profile `TMP-check` with one synthetic pair was created for scenarios 6
and 9 and deleted afterwards; tag and pair state was compared against a snapshot taken
before the run and came back **identical** (0 differences, 104 tag links).

| # | Сценарий | Результат |
|---|---|---|
| 1 | Клик по чипу сужает таблицу, адрес меняется, перезагрузки нет | 57 → 51 строки, адрес `?tag=…`, ни одного document-запроса |
| 2 | Повторный клик возвращает полный список | 51 → 57, `tag` из адреса ушёл |
| 3 | «Показать ещё» дописывает строки, кнопка исчезает, `offset` в адрес не попадает | 50 → 57, кнопки нет, первая строка не сдвинулась, адрес без `offset` |
| 4 | Поиск шлёт один запрос после паузы | 8 нажатий → **1** запрос, +1 запись истории, blur второго не добавил |
| 5 | Переключатель тега меняет подпись, таблицу не трогает | «не ищется», чип «(выключен)», 0 запросов за строками, метка на строке уцелела |
| 6 | Смена профиля перезагружает страницу целиком | документ перезагружен, чипы и панель — от `TMP-check`, 1 строка |
| 7 | Сохранённая ссылка | вторая вкладка: полная страница, тот же чип, тот же формат, те же 8 строк |
| 8 | Пустой список объясняет себя и возвращается | «ничего не найдено» + ссылка сброса; снятие фильтра вернуло 57 строк без перезагрузки |
| 9 | Смена статуса у удалённой пары | HTTP 404, в ячейке сообщение, селект исчез |
| 10 | Тёмная тема | палитра применена (`#16181c` фон), таблица, чипы, панель и кнопка читаемы, переключатель на месте, фокус виден на кнопке темы, чипе и строке тега |

Ошибок в консоли, кроме двух намеренных 404 из сценария 9, нет.

**Двойной запрос при поиске починен и подтверждён обеими сторонами.** Со старым
`hx-trigger="change"` на форме потеря фокуса поля поиска давала `htmx:trigger from
FORM` и **второй** запрос; после сужения триггера до
`change from:(#filters select, #filters input[type=checkbox])` blur не даёт ничего.
Тест `test_filter_form_does_not_fire_on_a_bubbled_change` проверен снятием защиты:
на прежней разметке он падает.

**Две ловушки харнесса, стоившие двух ложных «дефектов»** — записаны, потому что
следующая браузерная проверка наступит на них снова:

- **Кириллицу Playwright вводит через `Input.insertText`, а он не шлёт `keyup`.**
  Триггер поиска — `keyup changed delay:250ms`, поэтому набор «директор» не давал
  вообще ни одного запроса и выглядел как мёртвый поиск. Латиница идёт настоящими
  нажатиями. Проверять поиск только латиницей — или посылать клавиши поштучно.
- **Сравнивать полные списки, а не первые пачки.** `PAGE_SIZE = 50`, и полный
  список (57) с суженным по чипу (51) начинаются одинаковыми 50 строками: «чип
  ничего не сузил» было артефактом сравнения первых пачек.

Ещё одно наблюдение, не дефект: выбранный профиль запоминается cookie
(`jobhunt-profile`, см. `resolve_profile`), поэтому `/vacancies` без параметра после
смены профиля открывает **запомненный**, а не самый ранний.

## 5г. Collection from the browser — **walked 2026-08-05, 11 of 11** (slice 2b, task 12)

Playwright MCP against Edge (engine 151.0.4129.59) and the running app on the production
database. The MCP server pointed at Edge does start in a fresh process, so slice 2a's
fallback — a hand-written Playwright script — was not needed this time. Profile «Кирилл»,
57 vacancies, tags «Head of IT» and «IT Director».

**The measured number the plan asked for.** `GET /vacancies/collection`, ten requests
each time: **median 3.7 ms idle** (908 bytes) and **4.3 ms during a run** (1112 bytes),
max 22 ms after the first cold request. The threshold the plan set was ~150 ms, so three
seconds of polling is affordable and **the interval stays at three seconds**. For scale,
slice 2a's numbers on the same database were ~4 ms of data access and 6.4 ms of page
render.

| # | Сценарий | Результат |
|---|---|---|
| 1 | «Проверить новое» starts a run | Status line switched to «Собираю: 0 из 4 запросов, найдено 0.», no page reload — a `window` marker survived and no document request was made |
| 2 | Buttons disabled, counter moves | Both `disabled`; the counter walked 0 → 1 → 2 → 3 of 4 with the source and tag named at each step («сейчас dou.ua „Head of IT“, найдено 17») |
| 3 | One poll every ~3 s, no row requests during the run | Polls at 3047 / 3041 / 3058 ms apart; **zero** `/vacancies/rows` requests while the run was going |
| 4 | Polling stops, the table is re-requested once | `hx-trigger` gone from the fragment, no further polls in the following 12 s; `/vacancies/rows` requested **exactly once**, 6 ms after the last poll |
| 5 | The refresh keeps the filters | Chip «Head of IT» + `work_format=remote` + `status=new`: 13 rows before and after, same first row, address unchanged |
| 6 | A second start is impossible | Button `disabled`; three `curl -X POST` in a row during a live run → **409** each time, body is the panel with live progress, exactly one `#collection` |
| 7 | A run started from the terminal | **Only after a reload or a press** — see the finding below. On reload during a CLI run: buttons disabled, «…Прогон запущен из терминала», polling on |
| 8 | `docker compose restart app` mid-run | Startup sweep reported «прерванных прогонов помечено: 1», batch closed as `interrupted`, its journal row got «прогон прерван перезапуском приложения», panel said «Прошлый сбор прерван перезапуском. Собранное до обрыва сохранено.», buttons enabled again, table intact |
| 9 | A profile with every tag disabled | Both buttons `disabled`, «Собирать нечем: у профиля нет ни одного включённого тега.» |
| 10 | Dark theme | Body `#16181c`, buttons `#23262c` under `#e6e6e6` text, status line `#a0a4ab`, focus ring `solid 2px #8ab4f8` visible on both buttons; the disabled state (`opacity: .55`) stays legible |
| 11 | **A refusal replaces the panel, not nests one inside it** | 409 → exactly one `#collection`, `#collection #collection` empty, no reload. The scenario the ledger added: `f3929f8` fixed this and no server-side test can see it |

Console over the whole walk: the documented `/favicon.ico` 404 plus the two entries Edge
writes for the deliberate 409. Nothing else.

**The `stale` branch was rendered live for the first time.** The ledger lists as a Minor
that no test renders it. A synthetic `running` batch with `last_progress_at` 20 minutes
old produced «Прогон не подаёт признаков жизни с 19:55 — похоже, он оборвался. Можно
запустить заново.», with the buttons **enabled** and no polling — correct on both counts.
The row was deleted afterwards. It also showed that `load_state` reads the profile's
**latest** batch by `started_at`: a stale batch older than a newer closed one is invisible
to the panel, which is why the synthetic row had to be moved to the end.

### What the check found that the plan did not predict

**The panel printed UTC — fixed in this session.** The columns are `timestamptz` and
arrive as aware UTC datetimes, and `strftime` on an aware datetime prints its own zone
instead of converting. The owner was shown «05.08 17:06» for a run their own clock had at
20:06. This is the first and only place the interface shows a **time of day** — the table
prints dates only — so nothing else was affected. Fixed with `TZ: Europe/Kyiv` for the app
service in `docker-compose.yml` and `.astimezone()` before both `strftime` calls in
`_collection.html`. Verified after the change: 20:16 on the wall clock renders as
«05.08 20:16». **This changes no logic:** every clock read in the code is an explicit
`datetime.now(UTC)` and `func.now()` is server-side, so `TZ` reaches only `.astimezone()`
and the container's log timestamps.

**Scenario 7 of the plan over-promised, and the spec is the one that is right.** The plan
said a terminal run «disables the buttons in an already-open page within one poll». It
cannot: spec §6 says polling «lives exactly as long as the run does… No timer of ours»,
so an **idle** page does not poll at all. Verified with a real CLI run against an
untouched open page — buttons stayed enabled, zero requests. The state is honest
everywhere it is read: a reload during the CLI run shows «Прогон запущен из терминала»,
and pressing on a stale page sends a POST that comes back 409 and heals the panel in the
same swap. No code defect; the plan's scenario text was corrected instead, and §6 below
now carries the consequence as a known limitation.

**A harness trap for the next browser check: the runs are shorter than hand timing.**
A `quick` run over this profile takes ~14 s and a `full` one ~23 s. Three separate
attempts to hit a live run with a `curl` from another tool call landed **after** it had
closed — once by 160 ms — and each miss silently started a *new* collection instead of
being refused. Anything that must happen during a run has to be issued in the same command
that starts it, or synchronised against `select … from parse_batches where status='running'`.

### What the check changed in the production data

Nine batches were opened (seven from the browser, two from the terminal), two of them
`full`. **The data moved, and it moved correctly** — this was a real collection, not a
simulation, so nothing was reverted:

| | До | После |
|---|---|---|
| Пары / активные | 57 / 57 | 57 / **56** |
| Сумма `missed_checks` | 1 | **3** |
| Связки с тегами | 104 | **105** |
| Вакансии / статусы не-`new` | 57 / 0 | 57 / 0 |

The deactivation cycle fired on live data exactly as designed: `work.ua/4054039`
«Директор школи» took its **second** miss and went inactive; `dou.ua/365719` «Head of IT»
took its first. The second `full` run, 9 minutes after the first, did **not** double-count
either of them — the 20-hour rule held. Both tags were disabled for scenario 9 and are
enabled again; the two synthetic `stale` rows were deleted.

Also confirmed, and expected rather than a defect: a `quick` run reports «неполный набор
id — деактивация вакансий и пересборка их связок для этого запроса пропущены» for
**every** request, so deactivation is skipped for the whole run. That is exactly what the
button's own subtitle promises: «верхушка выдачи за сутки; пропавших не трогает».

## 5д. What the final whole-branch review found — 2026-08-05

Three reviewers against `main`, with different lenses: plan and spec alignment, the
htmx/template seam, and concurrency and data. **No Critical from any of them**, and the
concurrency lens explicitly could not construct a path to two `running` batches, a lost
batch or a double close. Nine Important findings; all are closed, and the Minor list in
`.superpowers/sdd/progress-collection-from-the-browser.md` was triaged with none promoted.

The four worth carrying forward, because each is a class rather than a one-off:

**A control the interface itself points at was a dead end.** With every tag disabled the
empty table says «Включите хотя бы один в панели тегов выше». Doing exactly that left
both collection buttons disabled: `can_collect` is read at render time, the tag toggle
redrew the tags panel and the chips but not the collection panel, and an idle panel does
not poll — so a disabled button raises no click and the page had no way back to itself.
Reproduced in the browser, then fixed by bringing the panel along out of band, the same
technique the chips already used and for the same stated reason. **The live check
missed it** because scenario 9 re-enabled the tags through the CLI rather than through
the page.

**A clause that always says the same thing stops being read.** `has_problems` is true
when any of four counters is non-zero, and the summary line named two of them. Every
quick run marks its id set incomplete — that is what «пропавших не трогает» means — so
«Проверить новое» *always* ended with «с ошибкой 0, усечено 0»: two zeros and no reason.
That is exactly the drift `ingest/summary.py` was extracted to prevent, reintroduced one
layer up in the template. Now only non-zero counters are named.

**The staleness window was under the runner's own ceiling.** The comment justified 15
minutes with «25 pages against 2 s pacing — under two minutes». Both halves were wrong:
the stamp is written once per source+tag pair, dou.ua issues up to 41 requests in one
pair, and each is bounded by the 30 s timeout rather than by the pacing — ≈ 21 minutes.
This rule does more than colour a line: the next run supersedes a stale batch and starts
collecting, so declaring a live runner dead puts two threads on one profile.
`STALE_AFTER` is now 30 minutes with the arithmetic written down. **The fix the reviewer
prescribed would not have worked** — it proposed a stamp per request inside `run_source`,
but `run_source` is called once per pair and `fetch_listings` paginates inside it, and
`touch()` does not commit. The real per-request heartbeat needs a progress signal in the
`BaseParser` contract; it is a row in section 6 rather than something half-built.

**Fixing a nesting bug made a rare failure unrecoverable.** Honouring `hx-swap` in the
global error handler was right for the 409 refusal, but `outerHTML` also applies to an
error body that is *not* a fragment: an `HTTPException` answers JSON and an unhandled 500
answers plain text, and either one replaced the whole `<div id="collection">` — its
`hx-trigger` included. The panel then never polled again. The `innerHTML` it replaced had
healed itself on the next poll. The swap is now gated on `Content-Type: text/html`, with
a non-vacuity test in the shape of its sibling.

Also closed: the auto-refresh wrote a browser-history entry with no user action (the
header is now skipped when the address is already that URL); web tests could start a real
collection against the developer's database because the guard was opt-in where the CLI
tests make it `autouse`; migration 0008 had no `upgrade → downgrade → upgrade` round trip,
the only check that compares it to the ORM models, since the test database is built from
the models and never from the migrations; the `interrupted` line blamed a restart that may
not have happened; the no-profile panel reported the wrong reason; and `README.md` still
said «контейнер `app` — это только веб-интерфейс», which this slice made false.

Thirteen tests were added with the fixes, including the two the reviewers named as the
gaps that let these through: one that renders the `finished` branch with a real summary,
and one that runs the swap-target invariant against a **running** panel — the only state
in which the panel declares a target on itself.

## 5е. The shell and two pages — **walked 2026-08-06, 9 of 9** (slice 3, task 7)

Playwright MCP against Edge and the running app on the production database. Profile
«Кирилл», 67 vacancies and 115 tag links at the start. A second profile `TMP-slice3` with
one tag and no vacancies was created for scenario 1 and deleted afterwards.

| # | Сценарий | Результат |
|---|---|---|
| 1 | Навигация переходит между страницами, отмечает текущую, сохраняет выбранный профиль | Полная загрузка документа в обе стороны, `aria-current="page"` переезжает, `<h1>` и `<title>` соответствуют. Профиль держится **cookie**: ссылки навигации голые (`/collection` без параметров), и после выбора `TMP-slice3` панель тегов на «Сбор данных» показала «QA Lead», а селектор — `TMP-slice3`. Форма селектора submit'ится на `page_path`: на «Вакансии» её `action="/vacancies"`, на «Сбор данных» — `/collection` |
| 2 | Прогон, запущенный на «Сбор данных», виден после перехода на «Вакансии»; в конце таблица перезапрашивается ровно один раз | **Проверено двумя прогонами, потому что одним не выходит — см. ловушку харнесса ниже.** Полная сверка (22.9 с), настоящий переход на «Вакансии» посреди прогона: опросы `/collection/indicator` на 3063 и 6108 мс от загрузки (3.05 с врозь), **0** запросов `/collection/panel`; последний опрос совпал с концом прогона до долей секунды, и `/vacancies/rows` ушёл **ровно один раз**, через 8 мс после него. Дальше 20 с тишины. Саму разметку индикатора снял второй прогон (проверка нового), запросом `/vacancies` из того же вызова, что нажал кнопку: `hx-get="/collection/indicator"`, `hx-trigger="every 3s"`, `hx-target="#collection-indicator"`, `hx-swap="outerHTML"`, строка «Собираю: 1 из 4 запросов», и **ни одного** `#collection` на этой странице |
| 3 | На «Сбор данных» ровно один опрашивающий | `/collection/panel` на 3048 и 6087 мс (3.04 с врозь) и **ни одного** `/collection/indicator`. Элемент индикатора на странице есть — цель обмена обязана существовать, — но без `hx-trigger` и без строки |
| 4 | Снятие всех чипов опустошает таблицу с объяснением; в адресе `tags_set=true`; перезагрузка держит пусто; один чип возвращает строки | 75 → **0** строк, «Сняты все теги фильтра — показывать нечего. Отметьте хотя бы один тег выше, чтобы вернуть список.», адрес `/vacancies?tags_set=true`. Перезагрузка по этому адресу — снова 0 строк и то же сообщение. Один чип «IT Director» → **51** строка (полный список, а не первая пачка), сверено с БД: 51 активная пара с этим тегом |
| 5 | Начальное состояние чипа следует за тегом сбора | «IT Director» выключён на «Сбор данных» → на «Вакансии» чип **на месте, но не отмечен**, класс `chip-off`, пунктирная рамка, подпись «(не ищется)». Список по умолчанию 75 → **72** (= активные пары «Head of IT», сверено с БД). Клик по выключенному чипу возвращает 75: чип фильтрует показ и не зависит от того, ищется ли тег |
| 6 | `jobhunt tag remove` отказывает и называет число связок; `tag list` показывает тег на месте | «удаление тега 'IT Director' отменено: оно унесло бы каскадом 52 связок…», подсказка `jobhunt tag disable`, код выхода **1**. `tag list` до и после — идентичен |
| 7 | Переключение тега на «Сбор данных» обновляет панель и кнопки сбора и ничего не пишет в консоль | Один `POST /tags/<id>/enabled` на переключение и больше ничего. Подпись «ищется»/«не ищется» и панель сбора меняются одним обменом: при обоих выключенных тегах кнопки `disabled` и «Собирать нечем: у профиля нет ни одного включённого тега.», при возврате одного — снова активны. Ровно один `#collection`, вложенных нет. **В консоли пусто** — чипы теперь на другой странице и больше не едут out-of-band |
| 8 | Обе темы, обе страницы, фокус с клавиатуры виден везде | Цикл `dark → auto → light → dark` кнопкой: `data-theme`, `localStorage` и показанная иконка совпадают на каждом шаге, `color-scheme` едет следом, `aria-label` меняется. Цвета сняты `getComputedStyle` в обеих темах для `body`, чипа, `th`, селекта статуса и «Показать ещё» — все переезжают. Скриншоты: «Сбор данных» целиком в обеих темах; «Вакансии» — низ страницы в тёмной и верх (фильтры, чипы, шапка таблицы) в светлой, то есть вся страница просмотрена глазами, но не каждая её часть в каждой теме. Фокус виден на всём: свои кольца `solid 2px #8ab4f8` на кнопке темы, чипе, «Показать ещё» и кнопках сбора; штатное кольцо браузера на селектах фильтров, поле поиска и ссылках навигации — на скриншоте тёмной темы читается |
| 9 | В консоли только задокументированный 404 `/favicon.ico` | За всю проверку — этот 404 и один 409, вызванный намеренно (попытка второго старта при живом прогоне). Больше ничего: ни одной ошибки htmx о ненайденной цели обмена |

### What the check found that the plan did not predict

**The end of a collection writes a browser-history entry with no user action — again, and
this slice is what reopened it.** Slice 2b closed exactly this finding (§5д) by skipping
`HX-Push-Url` when the pushed address already equals the current one. The guard compares
strings, and it still works — but this slice changed what the default address *is*. The
chips are now checked by default (inherited from `ProfileTag.is_enabled`) and the
`tags_set` marker rides along with them, so the filters form's serialisation of an
untouched page is no longer empty: it is `?tags_set=true&tag=…&tag=…`. On a freshly opened
bare `/vacancies` that does not equal the current address, so the header is sent.

Measured, by dispatching `jobhunt-collected` on `body` exactly as the indicator's last
response does: `history.length` **44 → 45** and the address bar rewritten from `/vacancies`
to `/vacancies?tags_set=true&tag=…&tag=…`. Doing it a second time changes neither — the 2b
guard catches it now that the addresses match. So the defect is **self-limiting: the first
collection to end on a freshly opened page costs one history entry, every later one is
silent.**

Consequence, and it is the one `_current_page_url`'s docstring says the guard exists to
prevent: after a collection ends on an untouched page, one press of «назад» goes to bare
`/vacancies` — restored from the back-forward cache, showing the table as it was **before**
the collection. Severity Minor: one user, one tab, and the address it writes is a truthful
description of the current filter state. **Not fixed by this task** — the walk documents
and hands it to the whole-branch review's triage.

> **CLOSED 2026-08-06 by the whole-branch review's fix wave (`dd1b446`).** Everything
> above is the state Task 7 found and is kept as the record of the measurement; it no
> longer describes HEAD. The fix is neither of the two shapes guessed at here. The
> collection-end refresh now sends `after_collection=true` and `vacancy_rows` answers it
> with **`HX-Replace-Url`** instead of `HX-Push-Url`: the address must still follow the
> screen, because the same wave made the refresh reset the chip row and an address
> describing the old set would be restored by the next reload — but nobody navigated, so
> nothing is written to the history. Re-measured in Edge on the production database the
> same day: `history.length` **50 → 50**, address rewritten to the reset chip set. The two
> headers are mutually exclusive in htmx (`HX-Push-Url` is read first and short-circuits),
> hence a branch rather than both.

**A harness trap, and the generalisation is worth more than the trap.** §5г recorded that
runs are shorter than hand timing. This walk hit the same wall in a new shape: a
`browser_navigate` and the `browser_evaluate` after it are **seven or more seconds apart**,
which is half a `quick` run. A live read of «is the indicator polling right now», issued in
the call after the navigation, came back `null` — which looks exactly like «the indicator
does not poll on «Вакансии»», a false defect of the kind that has cost this project a slice
before. What saved it was reading a **record** instead of a live state:
`performance.getEntriesByType('resource')` timestamps every request relative to page load
and can be read long after the fact. **Rule for the next browser check: never observe a
short-lived state with a live read from a separate tool call. Either issue the action and
the observation in one call, or record the timeline in the page and read the recording.**

**Two counts that differ and are both right.** `tag remove` refuses naming **52** links
while the «IT Director» chip shows **51** rows. The difference is the one deactivated pair:
the refusal counts links, the chip counts *active* pairs. Written down because a future
reader comparing the two numbers would reasonably suspect one of them.

**A confirmation, not a finding: the empty-state fix holds on live data.** `TMP-slice3`, a
profile with a tag but no vacancies, rendered **no chips and no marker**, and its empty
state read «Вакансий пока нет. Запустите сбор: python -m uv run python -m jobhunt.cli parse
…» — pointing at the terminal rather than at a chip row that holds nothing. That is the
second of the three empty-state defects Task 5 closed, seen working outside its test.

**A harness artefact, recorded so it is not reported as a defect next time.** Setting
`data-theme` on `<html>` by hand leaves the theme button's icon stale: the icon follows
`data-mode` on the button, which only the button's own click handler writes. Clicking the
button cycles both correctly (scenario 8). Drive the theme by clicking, not by setting the
attribute.

### What the check changed in the production data

Two real collections were run from the page — one `full` (22.9 s) and one `quick` (10.9 s)
— so **the data moved, and it moved correctly; nothing was reverted.** Compared afterwards
against a snapshot taken before the walk, row by row:

| | До | После |
|---|---|---|
| Вакансии / пары | 67 / 67 | **76 / 76** |
| Активные пары | 66 | **75** |
| Связки с тегами | 115 | **124** |
| Сумма `missed_checks` | 3 | **14** |
| Пары со статусом не-`new` | 0 | 0 |
| Теги и их включённость | 2, обе включены | идентично |

Verified by comparison rather than by counting: **no pair was lost** (every pair present
before is present after), **no pair changed activity** (the single inactive pair before is
the single inactive pair after — the eleven new misses are all first misses, and the
threshold is two), **no status changed**, and the tag list is byte-identical. The `full`
run rebuilt tag links and removed exactly one: `work.ua/8124939` is no longer found by
«Head of IT» — and it **kept** its «IT Director» link, so the orphan-protection rule
(section 4) held on live data. The whole database has **0** orphan pairs.

`TMP-slice3` and its tag were deleted; the profile list is back to «Кирилл» alone, and the
«Кирилл» tag state is identical to the snapshot. «IT Director» was disabled and re-enabled
during scenarios 5–7 and is enabled again.

## 6. Известные ограничения

Всё ниже осознанно отложено, не забыто.

| Что | Последствие | Насколько срочно |
|---|---|---|
| Сирота никогда не деактивируется | Пара без связки с отработавшим тегом не оценивается вовсе и остаётся активной навсегда. Так же ведут себя пары, созданные до тегов. **Из списка она при этом не «висит», а наоборот — скрыта:** без маркера `build_vacancy_query` применяет `enabled_link`, а у сироты связок нет ни одной, поэтому по умолчанию её не видно. Достать её можно только галочкой «показать вакансии, у которых нет тега фильтра» (`include_unchipped`) — см. строку ниже. Формулировка «просто висят в общем списке» держалась здесь с прежнего слайса и была перевёрнута ровно наоборот; заодно строка называла нереализованным псевдо-фильтр «Найденные ранее», который на самом деле существовал — это был чекбокс `include_untagged`, — и который слайс 3 удалил, передав его работу `include_unchipped`. Исправлено 2026-08-06 финальным ревью | Заметно после первого же удаления тега |
| Мягкого удаления тега нет | `jobhunt tag remove` **отказывает** и называет, сколько связок `profile_vacancy_tags` унесло бы каскадом, потому что по ним строится ряд чипов на «Вакансии»: удалить тег — значит стереть историю «чем это было найдено». Единственный путь сегодня — `tag disable`. Следствие второе: половина чекбокса «показать вакансии, у которых нет тега фильтра», отвечающая за теги, **переставшие** быть тегами сбора, пока пуста — перестать быть им нечем, пока тег нельзя удалить мягко. Чекбокс при этом не бесполезен: он показывает сирот (пары без единой связки), а они появляются | Пока не мешает: отказ громкий и называет замену. Настоящее решение — признак «удалён» у тега вместо `DELETE` |
| `Profile.name` не уникален в схеме | CLI отказывает при повторном создании, но это проверка приложения. Строка, заведённая до правки или в обход CLI, даст молчаливое резолвение в первый профиль | Теоретическое на одном пользователе |
| Прерванный прогон оставляет запись `running` | Запись коммитится до запроса нарочно (задача 3 слайса 2b) — это и делает «идёт прямо сейчас» видимым снаружи. Если процесс убит между этим коммитом и следующим (после пары источник+тег), строка виснет, пока её не закроет один из **трёх** путей в `ingest/batches.py` — все ищут записи по `ParseRun.batch_id`, который `run_source` проставляет с задачи 4. Третий — `finish_batch`, и на практике он и срабатывает чаще всех: прогон, упавший исключением при живом процессе, закрывает свою запись сразу, в `finally` у `run_profile`, не дожидаясь ни рестарта, ни правила застоя. Подметание при старте контейнера (`sweep_interrupted`, вызывается `jobhunt sweep-batches` из `docker-entrypoint.sh` сразу после миграций, задача 6) закрывает только прогоны с `started_by='web'` — терминальный процесс рестарт контейнера не касается и может быть ещё жив где-то ещё. Правило застоя (`_supersede_stale`, полчаса) такой разницы не делает: оно срабатывает при открытии следующего сбора **того же профиля**, кто бы его ни открыл, если `last_progress_at` не двигался дольше `STALE_AFTER`. Перед вторым механизмом терминальный и браузерный прогоны равны, перед первым — нет | До первого сработавшего механизма панель и CLI показывают несуществующий «идёт прямо сейчас». Для прогона из браузера это обычно секунды до следующего перезапуска контейнера; для прогона из терминала — до следующего сбора того же профиля, не раньше чем через полчаса после того, как он замер. Знать про это нужно при отладке |
| `stats.new` объективен, а не профилен | Второму профилю, впервые увидевшему известную вакансию, CLI напечатает «новых 0» | Проявится при втором профиле |
| `first_seen_at` / `last_seen_at` пары не читаются | Сортировка идёт по объективным полям вакансии: «давно висит у меня» и «давно висит на бирже» разъехались, а сортировка знает только второе | Заведены под план B |
| Рамка сверяется по сохранённой строке | Если вакансия вышла за рамку из-за правки на площадке, пропуск ей засчитается | Ущерб низкий: она профилю уже не нужна |
| Кеш HTTP и csrf-токен dou | При `HTTP_CACHE_ENABLED=true` тело отдаётся с диска, cookie-jar не наполняется, и сбор dou деградирует до первой страницы с предупреждением | Только при отладке |
| Выбранный профиль живёт в cookie, а не в адресе | `resolve_profile` берёт профиль из адреса, затем из cookie `jobhunt-profile`, затем самый ранний. Ссылки навигации — голые `/vacancies` и `/collection` без параметров, поэтому переход между страницами держится **только** на cookie: браузер без него (инкогнито, другая машина) откроет самый ранний профиль, а не выбранный. Сохранённая ссылка со страницы «Вакансии» несёт `profile=` **только если профиль пришёл из адреса** (`_page_url` кладёт его в `HX-Push-Url` лишь в этом случае — профиль из cookie не выбор пользователя, а память браузера). А поставить его в адрес умеет только селектор профиля, который рисуется при **более чем одном** профиле (`_nav.html`). На одном профиле — обычный случай сегодня — сохранённая ссылка `profile=` не несёт и переносимой не является, как и навигационная. Формулировка «несёт и потому переносима» была безусловной до 2026-08-06 | Осознанно: cookie — память конкретного браузера, и адрес не должен нести того, чего пользователь не выбирал (см. `_page_url`). Проверено живьём, раздел 5е, сценарий 1 |
| У `description_is_full` нет производителя в проде | Полный текст умеет качать только `WorkUaParser.fetch_description` — метод не объявлен в контракте `BaseParser` и не вызывается ничем в продакшен-коде (только в тестах). `description_is_full=true` в БД сегодня взяться неоткуда: guard «сниппет не затирает полный текст» (раздел 4) верен и держится тестом, но описывает случай, которого обычный сбор не создаёт. Легитимная заготовка под план B | Не мешает уже сегодня — заготовка, а не дефект |
| Пустая выдача work.ua глушит деактивацию источника | Площадка **не рендерит** контейнер `#pjax-jobs-list`, когда по запросу ничего не найдено (живая проверка ре-ревью: `/jobs-zqxwcvbnmlkjhgfd/` — HTTP 200, 140 КБ, контейнера нет). Легитимно пустая выдача поэтому уходит не в guard «счётчик обещает N, карточек 0», а в `ParserStructureError` → `run.status="failed"` → `mark_missing` и `rebuild_tag_links` пропускаются для **всего источника**, для всех тегов сразу. Один узкий тег, который сегодня ничего не находит, останавливает деактивацию work.ua в каждом прогоне | Чинится фикстурой страницы «нічого не знайдено» и явным её распознаванием — отдельная работа |
| Зарплату нечем переразобрать | `renormalize` чинит только `city`/`city_any`/`work_format` из `location_raw`. Сырой строки зарплаты в схеме нет (`salary_raw` не хранится, в отличие от `location_raw`), поэтому строки, разобранные старым правилом, исправляются **только** при повторной встрече вакансии в выдаче, а ушедшая с площадки остаётся с прежним разбором навсегда | После слияния этой ветки нужен один `parse --mode full`: правка «валюта перед числом» коснулась сумм. Симметричный `salary_raw` — кандидат в план B |
| «за кордоном» становится городом | `parse_location("за кордоном")` без маркера удалёнки даёт `city="за кордоном"`. Для рамки сбора это случайно верно (ни с одним городом справочника не совпадёт), в веб-таблице показывается как название города | Косметика; решение осознанное, тест это фиксирует |
| Многочастная локация показывается первым городом | `dto.city` — первая часть строки источника («Київ» из «Київ, Варшава (Польща)»), потому что колонка одна. Рамка сбора при этом сверяется со всеми частями, так что вакансия не теряется | Проявится только в отображении |
| Простаивающая страница не узнаёт о чужом сборе | Панель и индикатор опрашивают сервер **только пока идёт прогон**: `hx-trigger="every 3s"` приходит с фрагментом и исчезает с ним же (спека §6, «no timer of ours»). Значит открытая и ничем не тронутая вкладка не заметит ни сбор, запущенный из терминала, ни сбор из другой вкладки — кнопки на ней останутся активными. **Слайс 3 этого не изменил и не пытался:** оболочка добавила индикатор на обе страницы, но он подчиняется тому же правилу. Зато переход по навигации — это полная загрузка страницы, и она замечает всё: уходя с «Сбор данных» на «Вакансии» посреди прогона, пользователь получает живой индикатор, который досчитает прогон и перезапросит таблицу в конце (проверено живьём, раздел 5е, сценарий 2). Состояние честно на любом перечитывании: перезагрузка показывает «Прогон запущен из терминала», а нажатие на устаревшей странице уходит в 409 и тем же обменом чинит панель (раздел 5г, сценарий 7) | Косметика на одном пользователе с одной вкладкой. Постоянный опрос вхолостую — цена, которую спека сознательно не платит |
| Отметка «прогон жив» ставится раз на пару, а не раз на запрос | `run_profile` зовёт `touch()` после каждой пары «источник+тег», а внутри пары `fetch_listings` может сделать до 41 запроса (dou.ua, `max_batches=40`), каждый под таймаутом 30 с. Отсюда `STALE_AFTER = 30 минут`: окно обязано перекрывать самую длинную пару, иначе живой прогон объявляется мёртвым и следующее нажатие вытесняет его — два потока на один профиль, и `upsert_vacancies` (read-then-insert без `ON CONFLICT`) роняет проигравшего. Правильная форма — отметка на каждый запрос, но для неё нужно, чтобы штамп доходил до БД изнутри `fetch_listings`: сегодня этого не умеют ни `touch()` (не коммитит), ни парсеры (им нельзя знать про БД). Понадобится сигнал прогресса в контракт `BaseParser` | Не мешает: до потолка доходит только источник, отвечающий на пределе таймаута десятками запросов подряд. Но если поднять `max_batches`, `max_pages` или таймаут — арифметику `STALE_AFTER` надо пересчитать |
| Подметание при старте есть только под Docker | `jobhunt sweep-batches` зовёт `docker-entrypoint.sh`. Разработчик, поднявший `uvicorn` напрямую, подметания не получает, и веб-пачки, умершие с тем процессом, ждут `STALE_AFTER` | Только в разработке; лечится ручным `jobhunt sweep-batches` |
| Вежливость к площадкам считается на процесс | У сбора из браузера и у `jobhunt parse` с хоста — свои `HttpClient`, свои паузы между запросами, свои кеши robots.txt и HTTP. Профили независимы по построению (спека §7), поэтому два сбора разных профилей могут идти одновременно и стучаться на work.ua вдвое чаще, чем думает каждый из них. Слайс 2b это не создал, но сделал заметно проще | Проявится только со вторым профилем или при сборе из браузера и терминала разом |
| На странице два разных часа | Панель сбора переводит время в местное (`.astimezone()`), а колонка «Обновлена» печатает `posted_at` как есть. Дат это почти не касается — `posted_at` приходит датой без времени, — но около полуночи колонка и панель могут назвать один момент разными сутками | Косметика; замечено финальным ревью |
| Ни одна табличная библиотека не оставляет `<table>` на сервере | Проверено скачиванием и грепом самих файлов, а не по описаниям: **все семь** — Tabulator, AG Grid Community, Grid.js, DataTables 3, Frappe DataTable, RevoGrid, Vaadin Grid — после инициализации рисуют строки из JSON, включая **бесплатные** серверные режимы. Гибрида нет. Значит взять любую из них — это закончить роль htmx на главной странице и переписать её на клиентскую отрисовку. Это **подтверждение** раздела 9 спеки слайса 3 (`2026-08-06-shell-and-two-pages-design.md`), а не поправка к нему: раздел 9 отвергает библиотеки потому, что они «хотят владеть данными и рисовать их на клиенте, что противоречит инварианту: всякое условие уходит в базу, а обратно приезжает только `PAGE_SIZE` строк». До 2026-08-06 здесь стояло, будто раздел 9 отвергал их по неверному основанию «не умеют фильтровать на сервере» — **ни один документ такого не пишет**, и ссылка вдобавок вела на спеку 2a, где раздел 9 вообще про тестирование. Верным и узким остаётся только замечание: несколько библиотек фильтровать на сервере умеют, бесплатно, и это не помогает | Решение владельца: **таблицу продолжает рисовать сервер**. Строка нужна, чтобы вопрос не открывали заново по неверному основанию |
| Конец сбора сбрасывает ряд чипов | Когда прогон заканчивается, «Вакансии» сначала перерисовывают ряд чипов (`GET /vacancies/chips`, свежий `list_filter_tags` и `VacancyFilters()` по умолчанию), и только потом перезапрашивают строки. Каждый чип возвращается в состояние, унаследованное от `ProfileTag.is_enabled`, — ровно как при обычном открытии страницы. **Снятая руками галочка прогон не переживает**, и это видно на экране. Почему так, а не «оставить чипы как есть»: сервер не отличает «пользователь снял этот чип» от «этого чипа не было, когда страницу рисовали», — форма шлёт только отмеченные галочки. Значит тег, нашедший первую вакансию **во время** прогона, чипа не имел, в запрос обновления не уезжал, и его новые строки отфильтровывались из той самой таблицы, которая только что обновилась, чтобы их показать. Альтернатива — маркер побогаче, несущий весь отрисованный набор, — это правка модели фильтров, а не починка дефекта | Решение владельца: показать собранное важнее, чем сохранить ручной выбор чипов. Заведено финальным ревью слайса 3 (`dd1b446`) |
| Статусы английскими идентификаторами | `new`, `applied`, `call` в русском интерфейсе | Косметика |
| `CREATE EXTENSION vector` не выполнен | Образ `pgvector/pgvector:pg17` стоит, расширение не включено | Первая миграция плана B обязана включить его до `VECTOR(1024)` |

---

## 7. Уроки процесса, которые стоит унести в план B

### Из визуального среза (2026-08-12), три штуки — все про браузерную прогулку

**Сравнение скриншота с ранее снятым ничего не доказывает, если хоть часть страницы
показывает скрипт.** Кнопка темы лежит в разметке с `hidden` и раскрывается скриптом,
поэтому снимок «до того, как он отработал» отличается от снимка «после» безо всякой связи
с правкой. На переезде стилей это стоило десяти минут подозрений. Настоящая проверка —
**старый код против нового, снятые в одну минуту**: `git stash` шаблона, перезапуск,
снимок, `git stash pop`, перезапуск, снимок. И прежде чем верить разнице, снимите два
кадра одного состояния подряд: если различаются они, метод шумит и разница ничего не
значит.

**Правило CSS может быть мёртвым по весу селектора и выглядеть обязательным.**
`.chip-off:has(:checked)` писалось под композицию «выключен и отмечен» и не делало ничего:
`.chip:has(:checked)` весит 0-2-0 против 0-1-0 у `.chip-off`. Проверяется мгновенно и в
живой странице: удалить правило через CSSOM и прочитать вычисленное значение. Оно не
изменилось ни на бит. Способ применим к любому «на всякий случай» правилу.

**Playwright печатает текст, но не приводит в действие htmx-триггеры на `keyup`.**
`pressSequentially` заполняет поле, значение в DOM верное — и запрос не уходит, то есть
поиск во время прогулки выглядит сломанным. Одно настоящее нажатие клавиши, и всё
работает. Вывод общий: **на браузерной прогулке смотрите список сетевых запросов, а не
экран** — экран показывает следствие, а нужен факт отправки.

### Из более ранних срезов

**Заведён снимочный тест «фикстура → нормализатор»** (`tests/unit/test_normalize_fixtures_snapshot.py`).
Он прогоняет **все** карточки **всех** фикстур через нормализацию и фиксирует разобранные
значения. Оба Critical финального ревью нашлись ровно этой одной командой, и оба прошли
мимо задачных ревью, потому что те смотрели в диф, а дефект был виден только при
сопоставлении фикстуры с поведением кода:

- `'Київ, Варшава (Польща)'` давало город `'Київ, Варшава'`, и профиль с рамкой «Київ»
  **молча выбрасывал киевскую вакансию** — она не попадала в базу вовсе;
- `'від $1600'` давало `(1600, 1600)` вместо `(1600, None)`: у dou символ валюты стоит
  перед числом и разрывал поиск слова-границы.

Урок общий: **условие отложенной находки надо проверять, когда оно наступило.** Первый
из этих Critical лежал в журнале как отложенный пункт с формулировкой «перепроверить при
подключении парсеров». Парсеры подключили, фикстуры сняли, перепроверку не сделали.

**Образец кода в плане — отправная точка, а не истина.** За итерацию исполнители нашли
в брифах порядка двадцати расхождений: неиспользуемые импорты, ронявшие линтер (пять
раз); списки изменяемых файлов без реальных потребителей меняемой сигнатуры; неполные
`downgrade`, терявшие данные молча; забытое переименование индекса, которое ловит
`alembic check`. Если образец спорит с тестом из того же брифа — прав тест.

**Литералы невидимых символов проверять побайтово.** Самый дорогой дефект ветки:
`_THIN_SPACES = (" ", " ", " ")` в слое нормализации содержал три обычных ASCII-пробела
под комментарием «заданы кодами, а не литералами». Замена была пустой операцией, и на
живой фикстуре work.ua «80 000 – 120 000 грн» разбиралось в `(80, 0)`. Дефект пережил
три ревью, потому что символы визуально неотличимы, а тест-кейс с комментарием «узкие и
неразрывные пробелы» сам содержал обычные.

**Замена тестового файла целиком уносит регрессии.** Случалось трижды. Один раз это
скрыло дефект на четыре задачи вперёд. Перед заменой сверяйте старое покрытие с новым и
восстанавливайте всё, чему нет замены.

**Тест, зелёный при любой реализации, хуже отсутствующего.** Дважды правка молча
обнуляла доказательную силу тестов деактивации: пара заводилась без связки и отсеивалась
новым условием раньше, чем срабатывала проверяемая защита. Проверяйте снятием защиты.

**Многосессионность делает тесты лживыми.** После перехода `run_profile` на фабрику
сессий тесты, читавшие состояние своей сессией, возвращали объект из кеша и были
зелёными при любой реализации. Лечится явным `session.expire_all()`.

**Проверка, прогнанная по заведомо чистому настоящему файлу, не доказывает ничего.**
Тест «renormalize не превращается в разрешено всем» вызывал ту же функцию на том же
файле, что и соседний тест, который этот файл и так обходит: расширить исключение можно
было, не уронив ни одного теста. Лечится синтетическим источником — текст плюс путь
передаются в проверку, а не читаются с диска. Тот же приём годится любой границе,
которая описывает «что было бы, если бы кто-то написал вот так».

**Граница, описанная сильнее реализации, опаснее отсутствующей.** Обе AST-границы волны 2
пропускали `Vacancy as V`, `models.Vacancy(...)`, `setattr`, `update(Vacancy)` и
`from urllib import request`, а раздел 3 этого файла утверждал, что «ни один файл не
пишет её объективные поля». Следующая сессия доверяла бы границе больше, чем она стоит.
Теперь рядом с формулировкой стоит явный список того, чего границы не ловят.

**Докстринг расходится с кодом внутри собственного коммита.** Ре-ревью нашло пять таких
мест в одной волне: подпись колонки переименовали, а комментарий рядом с ней — нет;
источник числа сменился с оценки на точный счётчик, а докстринг остался про оценку;
появился второй лимит страниц, а класс о нём не знает. Проверять докстринги затронутых
функций — часть правки, а не отдельная уборка.

**Предупреждение, которое кричит всегда, перестают читать.** Принятая конвенция:
штатный исход — `logger.info` с числами; `warning` — когда произошло то, чего быть не
должно, в частности когда условие отсеяло **весь** набор, к которому применялось.

---

## 8. Документы проекта

| Файл | Что в нём |
|---|---|
| `docs/job-hunt-ai-plan.pdf` | Исходный замысел, все четыре этапа |
| `docs/superpowers/specs/2026-08-03-job-hunt-ai-iteration-1-design.md` | Дизайн итерации 1 |
| `docs/superpowers/plans/2026-08-03-plan-a-foundation-and-collection.md` | План A, 13 задач |
| `docs/superpowers/specs/2026-08-04-profile-scoped-collection-design.md` | Дизайн этой итерации: числа разведки в разделе 3, обоснования в разделе 9 |
| `docs/superpowers/plans/2026-08-04-profile-scoped-collection.md` | План этой итерации, 19 задач |
| `docs/superpowers/specs/2026-08-05-vacancies-as-a-tool-design.md` | Дизайн слайса 2a: страница «Вакансии» как инструмент. Раздел 12 — что известно про 2b (сбор из браузера), у которого спеки ещё нет |
| `docs/superpowers/specs/2026-08-05-collection-from-the-browser-design.md` | Дизайн слайса 2b: сбор из браузера |
| `docs/superpowers/plans/2026-08-05-collection-from-the-browser.md` | План слайса 2b, 12 задач |
| `docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md` | Дизайн слайса 3: оболочка и две страницы. Раздел 4 — модель тегов, раздел 9 — обоснование стека |
| `docs/superpowers/plans/2026-08-06-shell-and-two-pages.md` | План слайса 3, 7 задач (раздел задачи 6 — почему стили стали отдельным слайсом) |
| `.superpowers/sdd/progress.md` | Журнал прогресса **текущего** слайса: что сделано, какие дефекты найдены, какие решения приняты. Журналы прошлых слайсов переименованы — полный список в разделе 0.5 |
| `docs/HANDOFF.md` | этот файл |

**Долг документации закрыт** (2026-08-05): раздел 6.7 спеки утверждал, что сигнал
изменения описания ставится только при переходе полный текст → полный текст, — там
теперь записано принятое более широкое правило (см. раздел 4), с оговоркой, почему
узкая формулировка означала бы «сигнал не поднимается никогда».

Планы B (резюме, тезисы, матчинг) и C (измерение, автоматизация) ещё не написаны.
