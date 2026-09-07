# The visual layer — implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: `superpowers:executing-plans`. This project
> writes its code in the main session — see `CLAUDE.md`, «How a slice is executed». Do **not**
> dispatch implementer subagents; the review cycle stays with agents, one reviewer per task plus
> the re-review, and the browser walk is walked here, in the main session, through the Playwright
> MCP. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** make `/vacancies` a page the owner wants to open, by growing the hand-written palette
into a small design system rather than vendoring a framework.

**Architecture:** the stylesheet moves out of `base.html` into `static/app.css` and gains a token
layer; the templates change only where the table's information design requires it. No route, no
query and no fragment address is touched, so the five AST boundary tests and the htmx
swap-target invariant must stay green **without being edited** — that is a gate on every task,
not an expectation.

**Tech stack:** Jinja2 templates, CSS custom properties, htmx 2. No new dependencies, no
JavaScript of our own.

**Spec:** `docs/superpowers/specs/2026-08-12-visual-layer-design.md`

## Global Constraints

- **No new dependencies**, Python or npm (`CLAUDE.md`). This slice vendors nothing.
- **No JavaScript of our own.** Everything here is CSS. The «presentational only» rule now in
  `CLAUDE.md` permits our own JS; this slice does not need it, and does not add the AST test that
  would pin that boundary.
- **English for everything written into the repository**; Russian only for what the owner sees on
  screen. Status values *and their visible labels* stay English identifiers.
- Line width 100 (`pyproject.toml`). `uv run ruff check src tests` and `uv run ruff format
  --check src tests` clean before every commit. Do not run `ruff format --check` over `docs/`.
- **Any change to code or templates needs `docker compose restart app`** before it is visible in
  the browser: uvicorn runs without `--reload` and Jinja `auto_reload` is off.
- **A test that scans text for a literal must be shown to fail.** Every grep-style assertion added
  here is verified by removing what it guards and quoting the failure in the task's ledger entry.
- The five AST boundary tests and `tests/integration/test_web_vacancies.py`'s swap-target
  invariant stay green **unedited**.
- The full suite is the controller's job: one run per task, in the main session, before the task
  is marked complete. ~75 s idle.

---

### Task 1: The stylesheet becomes a file

The `<style>` block in `base.html` moves to `src/jobhunt/web/static/app.css` **verbatim** — no
declaration is changed, added or removed in this task. Its only visible effect must be none. The
task exists for two reasons: every later task edits CSS, and today nothing fetches `/static/`, so
the mount can vanish while the suite stays green over unstyled pages.

**Files:**
- Create: `src/jobhunt/web/static/app.css`
- Modify: `src/jobhunt/web/templates/base.html` (the `<style>` element, lines ~76–266)
- Create test: `tests/integration/test_web_static.py`
- Modify test: `tests/integration/test_web_shell.py`

**Interfaces:**
- Produces: `/static/app.css`, the stylesheet every later task edits. The `<link>` that loads it
  is the only new markup.

- [ ] **Step 1: Write the failing tests for the served files**

Create `tests/integration/test_web_static.py`:

```python
"""The static files are served, and their absence is not silent.

Nothing fetched `/static/` before this file existed. The mount could be removed, the
directory renamed, or a file dropped from the image, and the whole suite stayed green
while every page rendered completely unstyled — which was true of `htmx.min.js` too,
and had been true since long before the stylesheet moved here.
"""

from fastapi.testclient import TestClient

from jobhunt.web.app import app


def test_the_stylesheet_is_served():
    with TestClient(app) as client:
        response = client.get("/static/app.css")

    assert response.status_code == 200
    assert response.text.strip(), "an empty stylesheet leaves the page as unstyled as a missing one"


def test_htmx_is_served():
    """htmx is the whole interaction model; a 404 here turns every control into an
    ordinary link that does nothing."""
    with TestClient(app) as client:
        response = client.get("/static/htmx.min.js")

    assert response.status_code == 200
```

- [ ] **Step 2: Run them and watch the stylesheet one fail**

Run: `uv run pytest tests/integration/test_web_static.py -q`
Expected: `test_the_stylesheet_is_served` FAILS with `assert 404 == 200`; `test_htmx_is_served`
passes (the file is already there — that assertion is a guard for the future, not a red-to-green
step).

- [ ] **Step 3: Move the stylesheet, byte for byte**

Cut everything between `<style>` and `</style>` in `base.html` into a new file
`src/jobhunt/web/static/app.css`. Do not reformat, reorder or rewrite a single declaration or
comment — the comments in that block explain decisions and travel with it. Delete the now-empty
`<style>`/`</style>` pair.

In its place, immediately after the `<script src="/static/htmx.min.js"></script>` line, put:

```html
  <link rel="stylesheet" href="/static/app.css">
```

The theme bootstrap script **stays where it is**, inline and first in `<head>`. It must run
before the first paint or the flash of the light theme returns on every load.

- [ ] **Step 4: Run the tests and watch them pass**

Run: `uv run pytest tests/integration/test_web_static.py -q`
Expected: 2 passed.

- [ ] **Step 5: Write the failing test that the pages ask for it**

A served file nobody links is as unstyled as a missing one. In
`tests/integration/test_web_shell.py`, after `test_both_pages_carry_the_navigation`:

```python
def test_both_pages_link_the_stylesheet(client, session):
    """The mount answering 200 is half the guarantee; the other half is that the
    document asks for the file."""
    _profile(session)

    for path in ("/vacancies", "/collection"):
        html = client.get(path).text
        assert '<link rel="stylesheet" href="/static/app.css">' in html, path
```

- [ ] **Step 6: Run it, then prove it can fail**

Run: `uv run pytest tests/integration/test_web_shell.py::test_both_pages_link_the_stylesheet -q`
Expected: PASS.

Then delete the `<link>` line from `base.html`, run the same command, and quote the failure in
the ledger. Restore the line. This is the Global Constraint on literal-scanning tests, and this
plan's first instance of it.

- [ ] **Step 6b: Two tests read the palette off the rendered page, and must be pointed at the file**

`tests/integration/test_web_vacancies.py` has two tests that grep the *page* for CSS, because the
CSS used to be in it: `test_page_declares_explicit_palette_for_both_themes` (five assertions, all
of them declarations) and `test_theme_toggle_ships_all_three_icons` (half markup — the SVGs — and
half stylesheet — the `[data-mode=…] [data-icon=…]` show rules). Both go red the moment the
stylesheet moves.

**What they guard did not move; only where it lives did.** Add a helper next to them and change
*where they look*, not what they assert:

```python
def _stylesheet(client) -> str:
    response = client.get("/static/app.css")
    assert response.status_code == 200, "таблица стилей должна отдаваться, иначе проверять нечего"
    return response.text
```

The icons test keeps both halves and takes them from both places — an icon with no show rule
never appears, a show rule with no icon shows nothing, and either can be lost alone.

Then prove both can fail: change `background: var(--bg);` to `background: white;` in `app.css`
and delete one `[data-mode="dark"] [data-icon="dark"]` rule, run the two tests, quote both
failures, restore.

- [ ] **Step 7: Prove the move changed no pixel**

`docker compose restart app`, then in the main session through the Playwright MCP: open
`http://localhost:8000/vacancies` at 1440×900 and screenshot it.

**Do not compare against a screenshot taken earlier in the session.** That criterion is too weak
to be worth anything: the theme toggle is `hidden` in the markup and unhidden by script, so a shot
taken before that script runs differs from one taken after, and the difference has nothing to do
with this task. It happened on the first attempt and cost ten minutes of suspicion.

Compare **old code against new code, both rendered now**:

```bash
git stash push -- src/jobhunt/web/templates/base.html   # the inline <style> comes back
docker compose restart app                              # auto_reload is off; this is required
# screenshot -> old.png
git stash pop
docker compose restart app
# screenshot -> new.png
```

The two files must be byte-identical. Take two shots of the same state first to confirm the
comparison is deterministic at all before trusting a difference.

- [ ] **Step 8: Full suite, lint, commit**

```
uv run pytest -q
uv run ruff check src tests
uv run ruff format --check src tests
```

```bash
git add .gitignore src/jobhunt/web/static/app.css src/jobhunt/web/templates/base.html \
        tests/integration/test_web_static.py tests/integration/test_web_shell.py \
        tests/integration/test_web_vacancies.py
git commit -m "refactor(web): the stylesheet becomes a file that something finally fetches"
```

`.gitignore` gains `.playwright-mcp/`: the browser walk writes its screenshots and page snapshots
into the repository — the MCP server refuses paths outside it — and they are one session's
working material, not an artefact of the project.

---

### Task 2: The token layer and the page's voice — **owner's approval gate**

The first task with a visible result, and the one the whole slice is bet on. It introduces the
tokens every later task uses, and applies them to the three things that make the page read flat:
the titles' colour, the absence of a top edge, and the table's rhythm.

**Stop at the end of this task and show the owner the screenshot.** The rest of the plan runs
only after he approves the direction. This is what makes a wrong direction cost one task instead
of a slice.

**Files:**
- Modify: `src/jobhunt/web/static/app.css`

**Interfaces:**
- Produces the tokens every later task consumes: `--sp-1…--sp-8`, `--text-xs…--text-lg`,
  `--radius-sm`, `--radius-md`, `--radius-pill`, `--accent`, `--accent-fg`, `--accent-soft`,
  `--row-tint`, `--row-hover`.

- [ ] **Step 1: Add the token block**

At the top of `app.css`, inside the existing `:root`, after the palette that moved in Task 1:

```css
    /* The scales. Everything below this line spends these and invents no new
       numbers: a spacing value that appears once is a value nothing else can be
       aligned to. */
    --sp-1: .25rem;
    --sp-2: .5rem;
    --sp-3: .75rem;
    --sp-4: 1rem;
    --sp-6: 1.5rem;
    --sp-8: 2rem;

    --text-xs: .78rem;
    --text-sm: .875rem;
    --text-base: 1rem;
    --text-lg: 1.25rem;

    --radius-sm: .35rem;
    --radius-md: .5rem;
    --radius-pill: 999px;

    /* The accent is separate from --link on purpose. --link is what a hyperlink
       is; --accent is what THIS interface emphasises — focus, the current page,
       a selected chip. They happen to share a value in the light theme and must
       still be spendable apart. */
    --accent: #0b57d0;
    --accent-fg: #ffffff;
    --accent-soft: #e8f0fe;

    --row-tint: rgba(0, 0, 0, .025);
    --row-hover: rgba(11, 87, 208, .07);
```

Add the dark counterparts to **both** dark blocks — the `prefers-color-scheme` one and the
`:root[data-theme="dark"]` one. They are separate blocks by design (system default versus a
manual choice) and a token added to one only would make the two themes disagree:

```css
      --accent: #8ab4f8;
      --accent-fg: #16181c;
      --accent-soft: #1e2a3d;
      --row-tint: rgba(255, 255, 255, .03);
      --row-hover: rgba(138, 180, 248, .10);
```

- [ ] **Step 2: Give the page a top edge and move the navigation left**

```css
    .page-header {
      align-items: center;
      border-bottom: 1px solid var(--border);
      display: flex;
      gap: var(--sp-4);
      justify-content: space-between;
      margin-bottom: var(--sp-6);
      padding-bottom: var(--sp-3);
    }

    /* The navigation is LEFT of the content visually and AFTER it in the
       document. That split is deliberate and predates this slice: the comment in
       base.html explains that document order is screen-reader and keyboard order,
       where the page's own content outranks the list of pages. `order` moves the
       column without touching that. Do not "fix" this by moving the markup. */
    .nav { order: -1; }
```

- [ ] **Step 3: Take the blue out of the titles**

```css
    /* A table of forty vacancies whose titles are all link-blue and underlined is
       a wall, and the accent stops meaning anything because everything wears it.
       The title is the row's subject: it gets weight, not colour. */
    td .row-title {
      color: var(--fg);
      font-weight: 600;
      text-decoration: none;
    }
    td .row-title:hover { text-decoration: underline; }
    td .row-title:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

In `src/jobhunt/web/templates/_rows.html`, add the class to the anchor — this is the one markup
edit in this task:

```html
    <a class="row-title" href="{{ row.url }}" target="_blank" rel="noopener">{{ row.title }}</a>
```

- [ ] **Step 4: Give the rows a rhythm**

```css
    /* Alternation is what makes rows scannable; heavier rules just make the page
       look like a spreadsheet. So the separator gets quieter and the tint does the
       work. */
    th, td {
      border-bottom: 1px solid var(--border);
      line-height: 1.35;
      padding: var(--sp-2) var(--sp-3);
      text-align: left;
      vertical-align: top;
    }
    th {
      color: var(--muted);
      font-size: var(--text-xs);
      font-weight: 600;
      letter-spacing: .04em;
      text-transform: uppercase;
    }
    tbody tr:nth-child(even) { background: var(--row-tint); }
    tbody tr:hover { background: var(--row-hover); }

    /* The currency belongs to the number. Left to itself the column breaks
       "48400–55000 UAH" and drops UAH onto a second line, which is also what makes
       neighbouring rows different heights. */
    .cell-salary {
      font-variant-numeric: tabular-nums;
      white-space: nowrap;
    }
```

In `_rows.html`, add the class to the salary cell: `<td class="cell-salary">`.

- [ ] **Step 5: Restart, screenshot, calibrate density**

`docker compose restart app`, then screenshot `/vacancies` at 1440×900.

Measure, do not judge — count the rows that fit and the median row height with
`browser_evaluate`, because «looks tighter» is not a result anyone can check later.

**Done, and the answer was not the target.** `var(--sp-2) var(--sp-3)` left the median at 58px and
nine rows; tightening the rows to `var(--sp-1) var(--sp-3)` while giving `th` back its `var(--sp-2)`
— the header is one line and is what the eye returns to — gives a median of 52px and ten rows. The
target of fifteen does not survive contact with the page: 227px of the viewport sits above the
table, and the tall rows are wrapping titles, not padding. **The owner ruled on 2026-08-12 that
density is not critical and the meta line stays.** Stop here; do not buy rows with anything else.

- [ ] **Step 6: Screenshot both themes and the empty state**

Screenshot `/vacancies` with `data-theme="dark"` (click the theme toggle twice), and
`/vacancies?status=offer` — a filter that matches nothing — to see the empty row in the new type.

- [ ] **Step 7: Full suite, lint**

```
uv run pytest -q
uv run ruff check src tests
uv run ruff format --check src tests
```

Nothing new is asserted in this task, and that is honest rather than lazy: nothing it changes is
observable from the server. Its gate is the screenshot and the fact that **the existing suite
stays green unedited** — the boundary tests and the swap-target invariant included.

- [ ] **Step 8: Commit, then STOP and show the owner**

```bash
git add src/jobhunt/web/static/app.css src/jobhunt/web/templates/_rows.html
git commit -m "style(web): the page gets a top edge, a rhythm, and titles that are not links"
```

Show him the three screenshots — light, dark, empty — and ask whether the direction is right
before starting Task 3.

---

### Task 3: Six columns

«Теги» leaves its column and joins the source on one muted line under the title. A tag belongs
to the vacancy, and in a column it repeats in every row or in half of them.

**Files:**
- Modify: `src/jobhunt/web/templates/_rows.html`
- Modify: `src/jobhunt/web/templates/vacancies.html` (the `<thead>`)
- Modify: `src/jobhunt/web/static/app.css`
- Modify test: `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: `--text-xs`, `--muted`, `--sp-1` from Task 2.
- Produces: the `.row-meta` class, and a table of **six** columns — `{% set columns = 6 %}`.

- [ ] **Step 1: Write the failing test that header and colspan agree**

The `columns` literal and the `<th>` count must match, and nothing checks it today. When they
drift the layout does not break — the page simply stops being a table, silently. Add to
`tests/integration/test_web_vacancies.py`:

```python
def test_the_header_and_the_colspan_agree(client, session):
    """`{% set columns = N %}` in _rows.html spans the empty-state row and the
    «показать ещё» row; the <thead> in vacancies.html declares the real width. They
    are two literals in two files with nothing holding them together, and when they
    disagree the page keeps rendering — it just stops being a table."""
    profile = _profile_with_tag(session)
    _vacancy(session, profile)

    html = client.get("/vacancies?status=offer").text  # a filter that matches nothing

    header = html.split("<thead>", 1)[1].split("</thead>", 1)[0]
    columns = header.count("<th>")
    spans = re.findall(r'colspan="(\d+)"', html)

    assert columns == 6, f"the table is meant to have six columns, the header declares {columns}"
    assert spans, "the empty-state row has to span the table, and it declares no colspan at all"
    assert all(int(span) == columns for span in spans), (
        f"header says {columns}, rows span {sorted(set(spans))}"
    )
```

Add `import re` at the top of the file if it is not already there. Use the file's existing
helpers for the profile and the vacancy — **do not invent new ones**; read the neighbouring
tests and reuse the names they use. A pair with no tag link is an orphan and is hidden by
default, so the profile fixture must attach an enabled tag, or the table will be empty for the
wrong reason.

- [ ] **Step 2: Run it and watch it fail**

Run: `uv run pytest tests/integration/test_web_vacancies.py::test_the_header_and_the_colspan_agree -q`
Expected: FAIL — `the table is meant to have six columns, the header declares 7`.

- [ ] **Step 3: Move the tags under the title**

In `_rows.html`, change the literal and the two cells:

```jinja
{% set columns = 6 %}
```

```jinja
  <td>
    <a class="row-title" href="{{ row.url }}" target="_blank" rel="noopener">{{ row.title }}</a>
    {# Source and tags on one line under the title. The tags used to be a column of
       their own, where they repeated in every row — a tag belongs to the vacancy,
       not to a column. The separator is a middle dot with spaces, and the tags are
       joined with commas, so "work.ua · Head of IT, Team Lead" reads as two facts
       rather than three. #}
    <div class="row-meta">
      {{ row.source }}{% if row.tags %} · {{ row.tags | join(", ") }}{% endif %}
    </div>
  </td>
```

and delete the whole `<td>{{ row.tags | join(", ") if row.tags else "—" }}</td>` cell.

In `vacancies.html`, delete `<th>Теги</th>` from the header row.

- [ ] **Step 4: Style the meta line**

```css
    /* The second line of the title cell: what found this vacancy and where it came
       from. Quiet by construction — it is context, not content. */
    .row-meta {
      color: var(--muted);
      font-size: var(--text-xs);
      margin-top: var(--sp-1);
    }
```

Delete the now-unused `.muted` rule **only if** nothing else uses it — `grep -rn "muted" src/jobhunt/web/templates/`
first. It is used by the tags panel and the collection status, so it almost certainly stays.

- [ ] **Step 5: Run the test and the neighbouring file**

Run: `uv run pytest tests/integration/test_web_vacancies.py -q`
Expected: all pass. If a test that asserted on the tags column fails, read it before touching it:
it may be asserting something true that has moved, in which case it is updated, or something that
no longer exists, in which case it is rewritten to assert the new place.

- [ ] **Step 6: Prove the new test can fail the other way**

Set `{% set columns = 5 %}` in `_rows.html`, run the test, quote the failure, restore. A test that
only ever failed for the state it was written against has not been shown to catch drift.

- [ ] **Step 7: Restart, look**

`docker compose restart app`, screenshot `/vacancies`. The company column should no longer wrap
to two lines on the rows where it did.

- [ ] **Step 8: Full suite, lint, commit**

```bash
git add src/jobhunt/web/templates/_rows.html src/jobhunt/web/templates/vacancies.html \
        src/jobhunt/web/static/app.css tests/integration/test_web_vacancies.py
git commit -m "style(web): the tags join the source under the title and the table loses a column"
```

---

### Task 4: The status pill

The row's most important state is drawn with the most anonymous control available. It stays a
native `select` — htmx's post hangs on it, and so does the manual error-swap in `base.html` — and
gains a `data-status` that CSS colours by attribute.

**Files:**
- Modify: `src/jobhunt/web/templates/_status_cell.html`
- Modify: `src/jobhunt/web/static/app.css`
- Modify test: `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: `--radius-pill`, `--text-sm`, `--sp-1`, `--sp-2` from Task 2.
- Produces: `<select class="status" data-status="…">` in `_status_cell.html`, rendered identically
  by the page and by the fragment that answers `POST /vacancies/{id}/status`.

- [ ] **Step 1: Write the failing tests**

Both halves matter: the page must render the attribute, and so must the fragment returned after a
change — otherwise the colour is right until the user uses the control, and then resets.

```python
def test_the_status_control_carries_its_value_as_an_attribute(client, session):
    """The colour of the status pill is chosen by a CSS attribute selector. Without
    data-status every status renders in the same neutral colour and the fourth
    complaint this slice exists for comes straight back."""
    profile = _profile_with_tag(session)
    vacancy = _vacancy(session, profile)
    _set_status(session, profile, vacancy, "applied")

    html = client.get("/vacancies").text

    assert 'data-status="applied"' in html


def test_the_status_fragment_carries_the_new_value_too(client, session):
    """The cell is replaced by htmx after every change. A fragment without the
    attribute would leave the pill coloured by the OLD status until a full reload."""
    profile = _profile_with_tag(session)
    vacancy = _vacancy(session, profile)

    response = client.post(f"/vacancies/{vacancy.id}/status", data={"status": "offer"})

    assert response.status_code == 200
    assert 'data-status="offer"' in response.text
```

Use the file's existing helpers and its existing way of setting a status and of posting — read
the neighbouring tests first. `_set_status` above is a placeholder for whatever that file already
calls it; if there is no such helper, set `ProfileVacancy.status` directly in the fixture, the way
its neighbours do.

- [ ] **Step 2: Run them and watch both fail**

Run: `uv run pytest tests/integration/test_web_vacancies.py -k status_control or status_fragment -q`
Expected: both FAIL on the missing attribute.

- [ ] **Step 3: Add the attribute**

`_status_cell.html`:

```jinja
<select class="status" data-status="{{ row.status }}"
        name="status"
        hx-post="/vacancies/{{ row.id }}/status"
        hx-target="closest td"
        hx-swap="innerHTML">
```

- [ ] **Step 4: Colour it**

```css
    /* The status keeps the NATIVE select appearance on purpose. `appearance: none`
       would take the arrow with it, and drawing our own means a background image
       that cannot follow currentColor — a control that lies about the theme. The
       chips can afford that trade (see `.chip`) because their whole visual is
       replaced and there is a fallback; a dropdown with no arrow is just broken. */
    .status {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-pill);
      color: var(--fg);
      font: inherit;
      font-size: var(--text-sm);
      padding: var(--sp-1) var(--sp-2);
    }
    .status:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

    /* One hue per status, tinted for the background. The plain declaration comes
       first so a browser without color-mix keeps a readable pill instead of an
       unpainted one. */
    .status[data-status="applied"]   { color: var(--st-applied); }
    .status[data-status="call"]      { color: var(--st-call); }
    .status[data-status="interview"] { color: var(--st-interview); }
    .status[data-status="offer"]     { color: var(--st-offer); }
    .status[data-status="rejected"]  { color: var(--st-rejected); }
    .status[data-status="ignored"]   { color: var(--muted); }

    .status[data-status="applied"]   { background: color-mix(in srgb, var(--st-applied) 12%, var(--bg)); }
    .status[data-status="call"]      { background: color-mix(in srgb, var(--st-call) 12%, var(--bg)); }
    .status[data-status="interview"] { background: color-mix(in srgb, var(--st-interview) 12%, var(--bg)); }
    .status[data-status="offer"]     { background: color-mix(in srgb, var(--st-offer) 14%, var(--bg)); }
    .status[data-status="rejected"]  { background: color-mix(in srgb, var(--st-rejected) 10%, var(--bg)); }
```

`new` is deliberately absent: it is the default state of every row and must be the quiet one, so
it keeps `--surface` and `--fg` from the base rule. Add the hues to `:root` and to **both** dark
blocks:

```css
    --st-applied: #0b57d0;
    --st-call: #b06000;
    --st-interview: #6b3fa0;
    --st-offer: #1a7f37;
    --st-rejected: #b3261e;
```

```css
      --st-applied: #8ab4f8;
      --st-call: #e8a33d;
      --st-interview: #c9a7f0;
      --st-offer: #6fcf87;
      --st-rejected: #ff8a80;
```

`STATUSES` in `web/data/vacancies.py` is the list of seven — `new`, `applied`, `call`,
`interview`, `offer`, `rejected`, `ignored`. Every one is accounted for above. **Do not translate
the labels**: the owner decided on 2026-08-12 that they stay English and colour does the work.

- [ ] **Step 5: Run the tests and the file**

Run: `uv run pytest tests/integration/test_web_vacancies.py -q`
Expected: all pass.

- [ ] **Step 6: Prove they can fail**

Remove `data-status="{{ row.status }}"` from the template, run both tests, quote both failures,
restore.

- [ ] **Step 7: Restart, walk it in the browser**

`docker compose restart app`. Open `/vacancies`, change one row's status to `offer` through the
control, and confirm **without reloading** that the pill takes the new colour — this is the half
that the fragment test predicts and the browser confirms. Screenshot.

- [ ] **Step 8: Full suite, lint, commit**

```bash
git add src/jobhunt/web/templates/_status_cell.html src/jobhunt/web/static/app.css \
        tests/integration/test_web_vacancies.py
git commit -m "style(web): the status says what it is by its colour, not only by its word"
```

---

### Task 5: The filters get a panel

Nine controls in one wrapping row on the bare page background, selects and long checkbox labels
interleaved. Three groups inside one surface.

**Files:**
- Modify: `src/jobhunt/web/templates/_filters.html`
- Modify: `src/jobhunt/web/static/app.css`
- Modify test: `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: `--surface`, `--border`, `--radius-md`, `--sp-2…--sp-4` from Task 2.
- Produces: `.filters` as a panel with `.filters-row` groups. **The form's id, its `hx-*`
  attributes and every field's `name` are unchanged** — the filter model is not in this slice.

- [ ] **Step 1: Write the failing test for the shortened label**

```python
def test_the_unchipped_checkbox_is_labelled_short_and_explains_itself_in_full(client, session):
    """«показать вакансии, у которых нет тега фильтра» was longer than the rest of
    the filter row put together. The short label is what is read; the sentence that
    says what it actually does moves to the title, where it is still reachable."""
    _profile_with_tag(session)

    html = client.get("/vacancies").text

    assert "без тега фильтра" in html
    assert "у которых нет тега фильтра" in html, "the full explanation must survive in the title"
```

- [ ] **Step 2: Run it and watch it fail**

Expected: FAIL on `без тега фильтра`.

- [ ] **Step 3: Regroup the form**

Keep the `<form>` open tag exactly as it is — id, `hx-get`, `hx-include`, `hx-target`,
`hx-swap`, `hx-trigger`. **The trigger selector is scoped to `#filters` and must stay that way**:
unscoped, it also matches the profile picker, which reloads the page. Wrap the fields in three
rows, search first:

```jinja
  <div class="filters-row filters-search">
    <label>Поиск
      <input type="search" name="query" value="{{ current.query or '' }}"
             hx-get="/vacancies/rows" hx-include="#filters, .chips"
             hx-target="#rows" hx-swap="innerHTML"
             hx-trigger="keyup changed delay:250ms, search">
    </label>
  </div>
  <div class="filters-row">
    … the four selects: Статус, Источник, Город, Формат …
  </div>
  <div class="filters-row">
    <label><input type="checkbox" name="include_inactive" value="true"
           {% if current.include_inactive %}checked{% endif %}> показывать неактивные</label>
    <label title="Показать и те вакансии, у которых нет ни одного тега фильтра — найденные до тегов и осиротевшие"><input
           type="checkbox" name="include_unchipped" value="true"
           {% if current.include_unchipped %}checked{% endif %}> без тега фильтра</label>
    <label><input type="checkbox" name="with_salary" value="true"
           {% if current.with_salary %}checked{% endif %}> только с зарплатой</label>
  </div>
```

Move the four `<select>` labels into the second row **unchanged** — every `name`, every
`{% if %}`, every option. This step reorders markup and rewrites one label; it changes no
behaviour, and the existing filter tests are what prove that.

`_rows.html` quotes the old label in its `no_chips` empty state — «Поставьте галочку "показать
вакансии, у которых нет тега фильтра" выше». Update that sentence to the new short label, or it
will point at a control whose words are gone.

- [ ] **Step 4: Style the panel**

```css
    .filters {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      display: flex;
      flex-direction: column;
      gap: var(--sp-3);
      margin-bottom: var(--sp-4);
      padding: var(--sp-3) var(--sp-4);
    }
    .filters-row { display: flex; flex-wrap: wrap; gap: var(--sp-4); align-items: center; }
    .filters-search input[type="search"] { width: 100%; }
    .filters-search { display: block; }
```

The old `.filters { display: flex; gap: .75rem; margin-bottom: 1rem; flex-wrap: wrap; }` rule is
replaced, not supplemented — delete it.

- [ ] **Step 5: Run the vacancies and filters test files**

Run: `uv run pytest tests/integration/test_web_vacancies.py tests/integration/test_vacancy_filters.py -q`
Expected: all pass. **If a filter stops working, the cause is in this step's markup, not in the
filter model** — check that no `name` was lost in the move.

- [ ] **Step 6: Prove the label test can fail**

Restore the long label, run the test, quote the failure, put the short one back.

- [ ] **Step 7: Restart, walk every control**

`docker compose restart app`. Move each of the four selects, tick each of the three checkboxes,
type in the search box, and confirm the table answers each time. The search box is the one with
its own `hx-include="#filters, .chips"` — confirm that typing still respects a selected chip.
Screenshot.

- [ ] **Step 8: Full suite, lint, commit**

```bash
git add src/jobhunt/web/templates/_filters.html src/jobhunt/web/templates/_rows.html \
        src/jobhunt/web/static/app.css tests/integration/test_web_vacancies.py
git commit -m "style(web): the filters become one panel of three rows, and one label stops shouting"
```

---

### Task 6: The chips become pills

The native checkbox goes, and the pill carries the state — read by the browser from the same
field, so there is no second source of truth to drift.

**Files:**
- Modify: `src/jobhunt/web/static/app.css`
- Modify: `src/jobhunt/web/templates/_tag_chips.html` (the comment only)

**Interfaces:**
- Consumes: `--accent`, `--accent-fg`, `--accent-soft`, `--radius-pill` from Task 2.
- Produces: nothing other tasks consume. **No markup changes** beyond the comment — the input,
  its `name`, its `value` and its `checked` are untouched, which is what keeps every existing chip
  test green and meaningful.

- [ ] **Step 1: Rewrite the comment that defends the old choice**

Two comments argue that the native checkbox stays visible so that selectedness needs no second
signal: the one above `.chips` in `app.css` (it began life in `base.html` and moved in Task 1),
and the template's own note at the top of `_tag_chips.html`. Both are now wrong for the same
reason, and both are corrected rather than deleted — the reasoning is worth keeping, it just
reaches a different conclusion now:

```
   Нативный квадратик спрятан, но поле на месте: выбранность рисует сама пилюля
   через :has(:checked). Это не второй источник правды — браузер читает то же
   самое поле снаружи, расходиться тут нечему. Прежний комментарий защищал выбор
   из двух плохих вариантов (видимый квадратик либо класс, который надо держать в
   согласии с полем), и :has() этот выбор отменил.
```

- [ ] **Step 2: Hide the box, keep the field**

```css
    /* Visually gone, still a field: focusable, still toggled by its label, still
       the only thing that says what is selected. `display: none` would take it out
       of the tab order and out of the form. */
    .chip input[type="checkbox"] {
      height: 1px;
      margin: 0;
      opacity: 0;
      position: absolute;
      width: 1px;
    }

    /* The check has a permanent slot, hidden rather than absent, so a chip does not
       change width when it is selected. */
    .chip::before {
      content: "✓";
      font-size: var(--text-xs);
      visibility: hidden;
    }
    .chip:has(:checked)::before { visibility: visible; }

    .chip:has(:checked) {
      background: var(--accent-soft);
      border-color: var(--accent);
      color: var(--accent);
      font-weight: 600;
    }

    /* Two independent facts, two independent signals: the dash says "no longer
       searched", the fill says "shown right now". A dashed filled pill is both, and
       has to stay readable as both. */
    .chip-off { border-style: dashed; color: var(--muted); }

    /* Without :has() the pill cannot know, so the box comes back rather than the
       state going invisible. Anything older than December 2023 lands here. */
    @supports not (selector(:has(*))) {
      .chip input[type="checkbox"] {
        height: auto;
        opacity: 1;
        position: static;
        width: auto;
      }
      .chip::before { content: none; }
    }
```

- [ ] **Step 3: Run the chip tests**

Run: `uv run pytest tests/integration/test_web_vacancies.py -k чип -q`
Expected: all pass, **unedited**. That they still pass is the point: the field they assert on is
exactly the field that still carries the truth.

- [ ] **Step 4: Restart, walk the chips**

`docker compose restart app`. Tick and untick chips and confirm the table follows; confirm a
disabled tag's chip is dashed and still selectable; **tab to a chip with the keyboard** and
confirm the focus ring appears (`.chip:focus-within`, which predates this task) and that space
toggles it. Screenshot with one chip selected and one not.

- [ ] **Step 5: See the fallback with your own eyes**

In the browser devtools, temporarily rename `:has(:checked)` to `:has(:checkedX)` in the loaded
stylesheet — or simpler, add `.chip input[type="checkbox"] { position: static; opacity: 1; }` in
the devtools and confirm the row is still usable. The point is to know what a browser without
`:has()` gets, not to ship a change.

- [ ] **Step 6: Full suite, lint, commit**

```bash
git add src/jobhunt/web/static/app.css src/jobhunt/web/templates/_tag_chips.html
git commit -m "style(web): a chip is a pill whose fill the browser reads from the field itself"
```

---

### Task 7: «Сбор данных» catches up, and the slice is walked whole

Everything so far has been aimed at `/vacancies`. The second page shares the shell and most of
the classes, so it has been changing underneath without being looked at.

**Files:**
- Modify: `src/jobhunt/web/static/app.css`
- Possibly modify: `src/jobhunt/web/templates/_collection.html`,
  `_tags_panel.html`, `_collection_indicator.html`, `_tags_toggle.html` — **only** if the token
  pass exposes something the CSS cannot reach.

- [ ] **Step 1: Spend the tokens on the collection page's own classes**

`.collection`, `.collection-buttons`, `.collect`, `.collection-status`, `.tags-panel`,
`.tag-row`, `.collecting`, `.more`, `.theme-toggle` still carry hand-written values from before
Task 2 — `.4rem`, `.5rem`, `1px solid var(--border)`, `.9rem`. Replace those literals with the
scale (`--sp-*`, `--text-*`, `--radius-*`) **without changing what they look like** except where
the scale rounds them. A value that appears once is a value nothing can be aligned to, which is
the whole reason the scale exists.

- [ ] **Step 2: Restart and walk «Сбор данных»**

`docker compose restart app`. On `/collection`: the buttons, the tags panel with its toggles, the
panel while nothing is running. Screenshot.

- [ ] **Step 3: Walk a real collection end to end**

Start a collection from the page and watch: the panel while it runs, the compact indicator, the
navigation to `/vacancies` mid-run with the indicator still counting, and the moment it ends —
**the chip row resets first and the table refreshes after**. That chain is slice 3's Critical and
this slice must not have disturbed it. Confirm `history.length` does not grow across the refresh
(devtools console, before and after).

- [ ] **Step 4: Walk every empty state**

They are branches like any other and each has its own words:
`/vacancies` with no profile; with a profile but no vacancies; with every tag disabled; with every
chip cleared; with a hand-typed `?tags_set=true` on a profile that has no chips; and a filter that
matches nothing. Each must render in the new type with its advice still readable and its links
still working.

- [ ] **Step 5: Both themes, and the system default**

Toggle through all three modes — auto, light, dark — on both pages. The toggle writes
`data-theme` or removes it; confirm the tokens added in Tasks 2 and 4 answer in **all three**,
which is what the two separate dark blocks exist for.

- [ ] **Step 6: Full suite, lint, commit**

```
uv run pytest -q
uv run ruff check src tests
uv run ruff format --check src tests
```

```bash
git add src/jobhunt/web/static/app.css src/jobhunt/web/templates/
git commit -m "style(web): «Сбор данных» spends the same scale as «Вакансии»"
```

- [ ] **Step 7: Update the documents**

`docs/HANDOFF.md`: the «no test fetches `/static/`» finding is closed — say so and say which two
assertions closed it. §6's row about the vendored stylesheet and the seven table libraries stays,
because the grid question is still open and reopens after this slice. Add whatever this slice
learned to §7 if it is a class of failure rather than an incident.

`CLAUDE.md`: the intro says the interface is «two pages behind one shell» — check whether the
stylesheet's new home belongs in «Where things are».

---

## Self-review

**Spec coverage.** Every section of the spec has a task: structure and the `/static/` finding →
Task 1; the token layer, titles, row rhythm, salary, the header edge and the navigation → Task 2;
six columns → Task 3; the status pill and its English labels → Task 4; the filters panel and the
shortened label → Task 5; the chips with the `@supports` fallback and the retired comment →
Task 6; the collection page, the empty states, both themes and the documents → Task 7. The spec's
«sticky header is out of scope» is honoured by not appearing anywhere. The spec's approval gate is
Task 2's Step 8.

**Placeholders.** One knowingly remains: Task 4 Step 1 names `_set_status` and Task 3 Step 1 names
`_profile_with_tag` and `_vacancy` as *whatever `tests/integration/test_web_vacancies.py` already
calls its helpers*. Inventing new fixtures beside existing ones is how a test file grows two ways
of saying the same thing; the instruction to read the neighbours and reuse their names is
deliberate and is not a gap to fill in later.

**Type consistency.** `.row-title` (Task 2) is used by Task 3's rewritten cell. `.row-meta`
(Task 3) is defined where it is first used. `--st-*` (Task 4) are defined in the same step that
spends them. `.filters-row` (Task 5) replaces the old `.filters` flex rule rather than layering on
it. The `columns` literal is 6 in Task 3 and the test that pins it asserts 6.
