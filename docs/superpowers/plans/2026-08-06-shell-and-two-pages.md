# Shell and Two Pages — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the single `/vacancies` page into a shell with two pages — «Вакансии» and «Сбор данных» — and rebuild the tag model so that «искать впредь» and «показывать сейчас» each have exactly one control.

**Architecture:** Two page routes, each a whole document; navigation and the profile selector live in `base.html`. The collection panel and the tags panel move to `/collection`; a compact indicator in the shell keeps a running collection visible on every page and refreshes the table when it ends. Filter chips stop being a projection of the tag list and become a projection of the data: a chip exists for a tag that has actually found something, its initial state is inherited from `ProfileTag.is_enabled`, and a hidden marker lets the server tell «снял все чипы» from «только открыл страницу».

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0 (imperative `select()`), Jinja2, htmx 2, PostgreSQL 17, pytest.

**Spec:** `docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md` — read §4 before touching tags.

## Global Constraints

- **English for everything written into the repository**: code, identifiers, docstrings, comments, test names, plans, commit messages, and any brief handed to a subagent. **Russian only** for what the owner sees: template copy, CLI `print()`, `HTTPException(detail=…)`, `ParseRun.error_text`. Status values stay English identifiers.
- **Logs in new modules are English** (owner decision, 2026-08-05).
- **Do not mass-translate or rename anything written before 2026-08-05.** Existing Russian test names stay.
- **Add no new dependencies** — no Python packages, no npm. A vendored file in `web/static/` is not a dependency; that is how `htmx.min.js` already ships, and it is the only mechanism Task 6, the stylesheet task, may use. (Said «Task 7» until 2026-08-06: the renumbering in the amendments below made the stylesheet Task 6 and the live check Task 7.)
- **Line width 100** (`pyproject.toml`). `uv run ruff check src tests` and `uv run ruff format src tests` must be clean before every commit.
- **A subagent runs only the tests that cover its own change** — the files named in its task. The full suite is the controller's job, once, at the end.
- **Web routes take a session only through `Depends(get_session)`**, never `session_scope()`.
- **The web layer may write `ProfileVacancy.status` and `ProfileTag.is_enabled`, nothing else.**
- **`PAGE_SIZE` is defined once**, in `web/data/vacancies.py`. Never repeat the literal.
- **Every htmx swap target declared in a template must exist in the rendered document.** This is an enforced invariant (`tests/integration/test_web_vacancies.py`); it now has to hold for two pages.
- **The test database comes from `TEST_DATABASE_URL`.** Never run the suite against the production database.
- **`docker compose restart app`** is required for any template or code change to become visible: uvicorn runs without `--reload` and Jinja `auto_reload` is off.

---

## File Structure

**Created**

| File | Responsibility |
|---|---|
| `src/jobhunt/web/templates/collection.html` | The «Сбор данных» page: collection panel + tags panel |
| `src/jobhunt/web/templates/_nav.html` | Navigation and the profile selector, rendered by the shell |
| `src/jobhunt/web/templates/_collection_indicator.html` | The compact running-collection line for the shell |
| `tests/integration/test_web_shell.py` | Navigation, the two pages, the profile selector in the shell |

> **Corrected 2026-08-06.** This table used to list
> `src/jobhunt/web/static/pico.min.css`, «Vendored stylesheet (Task 7)» — wrong twice
> over. The stylesheet is **Task 6** after the renumbering below, and the file **does
> not exist**: Task 6 was dropped by the owner and its implementation reverted whole
> (`c8cc50f`, reverted by `7abf211`), so nothing under `web/static/` but
> `htmx.min.js` shipped in this slice. The row is removed rather than annotated in
> place, because a «Created» table is read as a list of what to expect at HEAD.

**Modified**

| File | What changes |
|---|---|
| `src/jobhunt/cli.py` | `cmd_tag_remove` refuses |
| `src/jobhunt/web/data/tags.py` | `list_filter_tags` — tags derived from links |
| `src/jobhunt/web/data/vacancies.py` | `VacancyFilters` gains `tags_set`, loses two booleans for one; `build_vacancy_query` chip logic |
| `src/jobhunt/web/routes/vacancies.py` | `_load_page`, `_filter_pairs`, `_empty_reason`, both handlers, the page context |
| `src/jobhunt/web/routes/collection.py` | Route renames, the indicator route, shared `collected_trigger` |
| `src/jobhunt/web/templates/base.html` | Navigation block, the indicator, the stylesheet link |
| `src/jobhunt/web/templates/vacancies.html` | Loses the collection panel, the tags panel and the profile picker |
| `src/jobhunt/web/templates/_tag_chips.html` | The marker field, inherited initial state, always-rendered container |
| `src/jobhunt/web/templates/_filters.html` | One checkbox instead of two |
| `src/jobhunt/web/templates/_collection.html` | New route addresses |
| `src/jobhunt/web/templates/_tags_toggle.html` | Loses the OOB chips include — the chips are on the other page now |
| `src/jobhunt/web/routes/tags.py` | Loses everything that existed only to carry the chips through the toggle |
| `tests/integration/test_web_vacancies.py` | The swap-target invariant becomes per-page |
| `CLAUDE.md` | The early-`return` invariant disappears; new boundaries |
| `docs/HANDOFF.md` | §6 rows: the stale pagination row, the new limitation |

## Amendments made before execution (2026-08-06)

Three conflicts found in the pre-flight scan, resolved by the owner. They are
written into the tasks below; this list exists so a later reader knows the plan
was amended rather than mis-implemented.

1. **The swap-target invariant breaks the moment the pages split, and no task
   fixed it.** Its OOB half is global: `hx-swap-oob` targets are collected from
   *every* template and required in *every* rendered page. Splitting the pages
   leaves `/vacancies` without `#collection`, so three existing tests go red on
   Task 2. Reworking it is now Task 2, Step 9 — the task where it breaks.
2. **The tag toggle's OOB chips become undeliverable.** The tags panel moves to
   «Сбор данных», the chips stay on «Вакансии», so the fragment can never find
   its target: htmx logs an OOB error, which contradicts Task 7's «в консоли
   ничего, кроме favicon». They are removed in Task 2, Step 8 — the same task
   that separates the two panels. The consistency they protected cannot break
   any more: the two controls are never on screen together, and walking to
   «Вакансии» is a full page load that re-inherits `is_enabled`.
3. **Tasks 5 and 6 were one atomic change split in two.** Task 5 removed two
   `VacancyFilters` fields and committed, while their callers in
   `routes/vacancies.py` were only fixed by Task 6 — a commit in which
   `/vacancies` answers 500 and `test_web_vacancies.py` is red, which Task 5's
   own Step 5 told the implementer to run. They are merged into one Task 5.
   The old Tasks 7 and 8 are renumbered 6 and 7; the slice has **seven** tasks.

---

### Task 1: `jobhunt tag remove` refuses

The filter model of spec §4.2 stands on `profile_vacancy_tags` rows. `cmd_tag_remove` is `session.delete(tag)` and the FK carries `ON DELETE CASCADE`, so one command destroys exactly the data the model needs — 1766 links in one live test during a previous iteration. Until soft deletion exists, the command must not run.

**Files:**
- Modify: `src/jobhunt/cli.py:261-273`
- Test: `tests/integration/test_cli.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: nothing later tasks depend on. This task is independent and may be done first or last.

- [ ] **Step 1: Write the failing test**

Add to `tests/integration/test_cli.py`:

```python
def test_tag_remove_refuses_and_keeps_the_links(session, capsys):
    """Hard deletion cascades the links the tag filter is built from.

    The filter chips of the vacancies page are derived from
    profile_vacancy_tags rows: a chip exists for a tag that has found
    something. Deleting a tag drops those rows, so the vacancies it found
    become unreachable by any chip — and no soft deletion exists yet to put
    them anywhere. The command refuses until one does.
    """
    profile = Profile(name="Кирилл", collection_cities=[])
    session.add(profile)
    session.flush()
    tag = ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True)
    session.add(tag)
    session.flush()
    vacancy = _vacancy(session, "1")
    pair = ProfileVacancy(
        profile_id=profile.id, vacancy_id=vacancy.id, first_seen_at=NOW, last_seen_at=NOW
    )
    session.add(pair)
    session.flush()
    session.add(ProfileVacancyTag(profile_vacancy_id=pair.id, tag_id=tag.id))
    session.commit()

    code = main(["tag", "remove", "--profile", "Кирилл", "--text", "Head of IT"])

    assert code == 1
    out = capsys.readouterr().out
    assert "1" in out, "the refusal must name how many links it would have destroyed"
    assert "disable" in out, "the refusal must point at the thing to do instead"
    session.expire_all()
    assert session.execute(select(func.count()).select_from(ProfileVacancyTag)).scalar_one() == 1
    assert session.get(ProfileTag, tag.id) is not None
```

Reuse the file's existing `_vacancy` helper and `NOW`; if the file has no `_vacancy`, copy the one from `tests/integration/test_web_vacancies.py` — a copied helper is this repository's established pattern for test files with no shared conftest.

- [ ] **Step 2: Run it and watch it fail**

```
uv run pytest tests/integration/test_cli.py::test_tag_remove_refuses_and_keeps_the_links -v
```

Expected: FAIL — the tag is deleted, so `session.get(ProfileTag, tag.id)` is `None` and the link count is 0.

- [ ] **Step 3: Make it refuse**

Replace the body of `cmd_tag_remove` in `src/jobhunt/cli.py`:

```python
def cmd_tag_remove(profile_name: str, text: str) -> int:
    """Refuse: a hard delete destroys the links the tag filter is built from.

    profile_vacancy_tags.tag_id carries ON DELETE CASCADE, so deleting a tag
    drops every record of which query found which vacancy. The vacancies page
    derives its filter chips from exactly those rows, and there is no soft
    deletion yet to hold the ones a removed tag would orphan.

    Disabling is what the user almost always means anyway: it stops the
    searching, which is the tag's only other effect.
    """
    with session_scope() as session:
        profile = _find_profile(session, profile_name)
        if profile is None:
            print(f"профиль {profile_name!r} не найден")
            return 1
        tag = _find_tag(session, profile, text)
        if tag is None:
            print(f"тег {text!r} не найден у профиля {profile.name!r}")
            return 1
        links = session.execute(
            select(func.count())
            .select_from(ProfileVacancyTag)
            .where(ProfileVacancyTag.tag_id == tag.id)
        ).scalar_one()
        print(
            f"удаление тега {text!r} отменено: оно унесло бы каскадом "
            f"{links} связок с вакансиями, а по ним строится фильтр тегов "
            f"на странице «Вакансии». Мягкого удаления пока нет.\n"
            f"Чтобы перестать искать по этому тегу:\n"
            f"  jobhunt tag disable --profile {profile.name!r} --text {text!r}"
        )
        return 1
```

Add to the imports at the top of `cli.py` if they are not already there:

```python
from sqlalchemy import func, select

from jobhunt.db.models import ProfileVacancyTag
```

Check the existing import lines first — `cli.py` already imports several names from `jobhunt.db.models` and from `sqlalchemy`; extend those lines rather than adding duplicates.

- [ ] **Step 4: Run the test and the file around it**

```
uv run pytest tests/integration/test_cli.py -v
```

Expected: PASS, including any pre-existing test that asserted removal worked. **If one does, it must be rewritten, not deleted** — replacing a test file wholesale has silently dropped regressions three times in this repository. Rename the old test to `test_tag_remove_no_longer_deletes` and assert the new behaviour.

- [ ] **Step 5: Lint and commit**

```bash
uv run ruff check src tests && uv run ruff format src tests
git add src/jobhunt/cli.py tests/integration/test_cli.py
git commit -m "fix(cli): tag remove refuses instead of cascading away the tag links"
```

---

### Task 2: The shell — navigation, the profile selector, two pages

**Files:**
- Create: `src/jobhunt/web/templates/_nav.html`
- Create: `src/jobhunt/web/templates/collection.html`
- Create: `tests/integration/test_web_shell.py`
- Modify: `src/jobhunt/web/templates/base.html`
- Modify: `src/jobhunt/web/templates/vacancies.html`
- Modify: `src/jobhunt/web/routes/collection.py`
- Modify: `src/jobhunt/web/routes/vacancies.py` (page context only)
- Modify: `src/jobhunt/web/templates/_collection.html` (route addresses)
- Modify: `src/jobhunt/web/templates/_tags_toggle.html`, `_tag_chips.html`, `_tags_panel.html`,
  `src/jobhunt/web/routes/tags.py` (the OOB chips go away — Step 8)
- Modify: `tests/integration/test_web_vacancies.py` (the invariant becomes per-page — Step 9)

**Interfaces:**
- Consumes: nothing from Task 1.
- Produces: `resolve_page_profile(request, session, requested)` in `routes/_common.py`, returning `(profile | None, profiles, error | None)`. Every page context now carries `page: str` (`"vacancies"` or `"collection"`) and `page_path: str` (`"/vacancies"` or `"/collection"`). Task 3 reads `page`. The routes `GET /collection/panel` and `POST /collection/start` replace `GET /vacancies/collection` and `POST /vacancies/collect`.

- [ ] **Step 1: Write the failing tests**

Create `tests/integration/test_web_shell.py`:

```python
"""The shell: navigation, the profile selector, and the two pages."""

import pytest
from fastapi.testclient import TestClient

from jobhunt.db.models import Profile, ProfileTag
from jobhunt.web.app import app
from jobhunt.web.deps import get_session


@pytest.fixture
def client(session):
    def _override_get_session():
        yield session

    app.dependency_overrides[get_session] = _override_get_session
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _profile(session, name="Кирилл") -> Profile:
    profile = Profile(name=name, collection_cities=[])
    session.add(profile)
    session.commit()
    return profile


def test_both_pages_carry_the_navigation(client, session):
    _profile(session)

    for path in ("/vacancies", "/collection"):
        html = client.get(path).text
        assert 'href="/vacancies"' in html, path
        assert 'href="/collection"' in html, path


def test_the_current_page_is_marked_in_the_navigation(client, session):
    """Without aria-current the navigation cannot say where the user is, and
    a screen reader has no way at all."""
    _profile(session)

    vacancies = client.get("/vacancies").text
    collection = client.get("/collection").text

    assert 'href="/vacancies" aria-current="page"' in vacancies
    assert 'href="/collection" aria-current="page"' in collection


def test_the_collection_page_carries_the_buttons_and_the_tags_panel(client, session):
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    session.commit()

    html = client.get("/collection").text

    assert "Проверить новое" in html
    assert "Полная сверка" in html
    assert 'id="tags-panel"' in html


def test_the_vacancies_page_no_longer_carries_them(client, session):
    """They moved. Two homes for one control is the confusion this slice exists
    to remove."""
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    session.commit()

    html = client.get("/vacancies").text

    assert "Полная сверка" not in html
    assert 'id="tags-panel"' not in html


def test_the_profile_selector_lives_in_the_shell_and_returns_to_the_same_page(client, session):
    """It applies to both pages, so it belongs to neither of them. Its form has
    to submit back to the page the user is standing on, or picking a profile
    would also navigate."""
    _profile(session, "Кирилл")
    _profile(session, "Второй")

    assert 'action="/vacancies"' in client.get("/vacancies").text
    assert 'action="/collection"' in client.get("/collection").text
```

- [ ] **Step 2: Run them and watch them fail**

```
uv run pytest tests/integration/test_web_shell.py -v
```

Expected: FAIL — `/collection` returns 404, and the navigation does not exist.

- [ ] **Step 3: Extract the navigation into its own template**

Create `src/jobhunt/web/templates/_nav.html`:

```jinja
{# Navigation and the profile selector, on the right of every page.

   The profile selector lives here rather than on a page because it applies to
   both of them; leaving it on one would make that page the implicit owner of a
   global choice. Its form submits back to page_path — to the page the user is
   already on — so that picking a profile changes the profile and nothing else. #}
<nav class="nav">
  <ul class="nav-pages">
    <li><a href="/vacancies"
           {% if page == "vacancies" %}aria-current="page"{% endif %}>Вакансии</a></li>
    <li><a href="/collection"
           {% if page == "collection" %}aria-current="page"{% endif %}>Сбор данных</a></li>
  </ul>
  {% if profiles | length > 1 %}
  <form class="profile-picker" method="get" action="{{ page_path }}">
    <label>Профиль
      <select name="profile" onchange="this.form.submit()">
        {% for p in profiles %}
          <option value="{{ p.id }}"
                  {% if p.id == current_profile_id %}selected{% endif %}>{{ p.name }}</option>
        {% endfor %}
      </select>
    </label>
  </form>
  {% endif %}
</nav>
```

- [ ] **Step 4: Put the navigation in the shell**

In `src/jobhunt/web/templates/base.html`, inside the `<body>`, wrap the existing content block so that the navigation sits beside it. Find the element that currently holds `{% block content %}` and restructure it to:

```jinja
<div class="layout">
  <main class="page">
    {% block content %}{% endblock %}
  </main>
  {% include "_nav.html" %}
</div>
```

The navigation comes **after** `<main>` in the document and is placed on the right by CSS (`flex-direction: row` on `.layout`). Source order puts the page's own content first for a screen reader and for keyboard order, which is what matters; the visual side is a stylesheet decision. Add to the `<style>` block in `base.html`:

```css
.layout { display: flex; gap: 1.5rem; align-items: flex-start; }
.page { flex: 1; min-width: 0; }
.nav { flex: 0 0 12rem; position: sticky; top: 1rem; }
.nav-pages { list-style: none; margin: 0 0 1rem; padding: 0; }
.nav-pages a { display: block; padding: .4rem .6rem; border-radius: .4rem; text-decoration: none; }
.nav-pages a[aria-current="page"] { background: var(--panel); font-weight: 600; }
```

Use the palette variable names already defined in `base.html` — read the `:root` block and match them; do not invent new colour literals.

- [ ] **Step 5: Create the collection page**

Create `src/jobhunt/web/templates/collection.html`:

```jinja
{% extends "base.html" %}
{% block title %}Сбор данных — Job Hunt AI{% endblock %}
{% block header %}<h1>Сбор данных</h1>{% endblock %}
{% block content %}
{% if profile_error %}
  <p class="empty">{{ profile_error }}</p>
{% elif not has_profile %}
  <p class="empty">Профиль не создан. Выполните в терминале:<br>
  <code>python -m uv run python -m jobhunt.cli profile create --name "Имя"</code></p>
{% else %}
  {% include "_collection.html" %}
  {% include "_tags_panel.html" %}
{% endif %}
{% endblock %}
```

The empty-state hints deliberately print the longer `python -m uv run …` form: the user may paste them into a terminal older than the current environment.

- [ ] **Step 6: Add the page route and rename the fragment routes**

In `src/jobhunt/web/routes/collection.py`, rename the two existing routes and add the page:

```python
@router.get("/collection", response_class=HTMLResponse)
def collection_page(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    profile: Annotated[uuid.UUID | None, Query()] = None,
) -> HTMLResponse:
    """The collection page: the buttons and the tags panel, nothing else.

    Profile resolution follows the vacancies page exactly — a profile named in
    the ADDRESS that does not exist is a 404 with an explanation, and a missing
    cookie profile falls back to the earliest. Two rules for one question would
    diverge.
    """
```

**Extract the profile-resolution block from `vacancies_page` into `routes/_common.py` and call it from both pages** — do not copy it. Two pages answering the same question about the same address is exactly where a copy drifts, and the answers must be identical for all three cases: no profile at all, `?profile=<unknown uuid>` (404 with an explanation), `?profile=<not a uuid>` (**422**, corrected during Task 2 — see below). Give it this signature so both callers get everything the shell needs:

> **Corrected 2026-08-06, during Task 2.** This parenthesis said 400 and was wrong
> about behaviour that already existed. `profile` is declared
> `Annotated[uuid.UUID | None, Query()]`, so FastAPI rejects a malformed value with
> 422 before any handler runs — exactly as `?offset=-1` already does, which
> `docs/HANDOFF.md` §5б records as correct. 400 is the answer of the parameters this
> project parses by hand (`parse_tag_ids`), and making `profile` an exception to that
> would special-case one query parameter against a convention its neighbour follows.
> What the requirement is actually for — both pages answering the same address
> identically — holds either way, and a test asserts it.

```python
def resolve_page_profile(
    request: Request, session: Session, requested: uuid.UUID | None
) -> tuple[Profile | None, list[dict], str | None]:
    """The profile for a page, the list for the selector, and the error to show.

    Shared by both pages rather than copied into each: the rules for a profile
    named in the address, a profile remembered in a cookie and no profile at
    all are one set of rules, and two copies of them would answer the same
    address differently the first time one of them changed.
    """
```

Returns `(resolved_profile_or_None, profiles_for_the_picker, profile_error_or_None)`. Move the existing body from `vacancies_page` and have that handler call it too, so there is one implementation from the moment this task lands.

The context must include `page="collection"`, `page_path="/collection"`, `profiles`, `current_profile_id`, `has_profile`, `profile_error`, plus `**panel_context(session, resolved_id, profile)`.

Then rename:

```python
@router.get("/collection/panel", response_class=HTMLResponse)   # was /vacancies/collection
@router.post("/collection/start", response_class=HTMLResponse)  # was /vacancies/collect
```

Update every reference: `_collection.html` (`hx-get` and both `hx-post`), and the tests that name the old addresses. `grep -rn "vacancies/collect" src tests` must come back empty when this step is done.

- [ ] **Step 7: Slim the vacancies page and give both pages the shell context**

In `vacancies.html`, delete the profile-picker form (it lives in `_nav.html` now) and the two includes that moved:

```jinja
  {% include "_collection.html" %}   ← delete
  {% include "_tags_panel.html" %}   ← delete
```

In `routes/vacancies.py`, add `"page": "vacancies"` and `"page_path": "/vacancies"` to the `vacancies_page` context.

- [ ] **Step 8: Remove the OOB chips from the tag toggle**

The toggle's response carries three fragments: the tags panel (its real target),
the collection panel out of band, and the chip row out of band. The chip row was
there because a chip's «(выключен)» mark and the panel's «не ищется» render one
database field, and while both stood on one page they were not allowed to
disagree between two swaps.

This task moves the panel to «Сбор данных» and leaves the chips on «Вакансии».
They are never on screen together again, so they cannot disagree; and the
fragment now has no target to land in, which htmx reports as an OOB error in the
console — the thing Task 7's browser pass says must not be there. The collection
panel stays out of band: it is on the same page as the toggle and its buttons
read the same field.

Remove the chip row from the toggle path, and with it everything that existed
only to carry the chips' selection through that round trip:

- `_tags_toggle.html` — the `{% include "_tag_chips.html" %}` line, and the
  paragraph of the comment that explains it. Say instead why it is gone, so the
  next reader does not restore it as a missing feature.
- `_tag_chips.html` — the `{% if chips_oob %} hx-swap-oob="true"{% endif %}`
  attribute. Keep `id="tag-chips"`.

  > **Corrected 2026-08-06, after the whole-branch review.** This line used to end
  > «: it stays a regular swap target», which was **false when written** — after this
  > step nothing on either page declared `hx-target="#tag-chips"`, so the id was a
  > handle for `hx-include` and for the tests, not a target. It is **true now, for a
  > different reason**: closing the whole-branch review's Critical gave the container
  > `hx-get="/vacancies/chips"`, `hx-target="#tag-chips"`, `hx-swap="outerHTML"` and
  > `hx-trigger="jobhunt-collected from:body"`, so the chip row re-derives itself when
  > a collection ends and *is* an ordinary swap target. Keep the id either way; do not
  > read the old clause as evidence that the target already existed at this step.
- `_tags_panel.html` — `hx-include=".chips"` on the toggle. There are no
  `.chips` on this page to include.
- `routes/tags.py` — the `tag` Form parameter, the `parse_tag_ids` call, and the
  `selected_tag_ids` / `chips_oob` context entries. `parse_tag_ids` itself stays:
  the vacancies routes still use it. Rewrite the docstring — most of it is about
  the chips.
- `tests/integration/test_web_tags.py` — any test asserting the toggle answers
  with chips. **Rewrite each one to assert the new contract** (the response
  carries the panel and the collection panel and *no* chips), do not delete it:
  wholesale test replacement has silently dropped regressions three times here.

- [ ] **Step 9: Make the swap-target invariant per-page**

In `tests/integration/test_web_vacancies.py`. Read `_цели_без_адресата` and
`test_проверка_целей_htmx_не_вырождена` before changing anything — the invariant
has two halves and only one of them is broken.

**What breaks.** Regular targets (`hx-target`) are read from the rendered page
and keep working unchanged: a target is required exactly when something on that
page aims at it. The out-of-band half is global — every `hx-swap-oob` literal
found in **any** template is required in **every** page — and that assumption
dies with the split. After Step 8 there is one OOB target left, `#collection`,
and it belongs to «Сбор данных» only. Three tests go red on `/vacancies`
without this step.

**What to build.** Each page test declares the OOB targets that page must carry,
and the check takes that set instead of the union of all templates:

- `/vacancies` declares none.
- `/collection` declares `#collection` — the tag toggle lives there and answers
  with the collection panel out of band.

**And a non-vacuity guard, which is the point of the change.** A separate test
must assert that the union of the pages' declared sets equals the set of OOB
targets actually present in the templates. Without it a new `hx-swap-oob` added
later is simply unowned, and an invariant that loses coverage without failing is
precisely what this one exists to prevent — the reason its own docstring gives
for scanning templates recursively.

Extend `test_проверка_целей_htmx_не_вырождена` rather than replacing it: it
hardcodes both of today's OOB targets, and it is the test that proves the regular
half is not green for any implementation.

Run the same invariant against `/collection` too — with a profile, and with a
run in progress, which is the only state in which the panel targets itself.

- [ ] **Step 10: Run the tests this task covers**

```
uv run pytest tests/integration/test_web_shell.py tests/integration/test_web_vacancies.py tests/integration/test_web_collection.py tests/integration/test_web_tags.py -v
```

Expected: PASS.

- [ ] **Step 11: Look at it in a browser**

```bash
docker compose restart app
```

Open `http://localhost:8000/vacancies`, click «Сбор данных», click back. Both pages must render, the navigation must mark the current one, and the profile selector must be present when more than one profile exists. Toggle a tag on «Сбор данных» with the console open: the panel and the buttons must update and the console must stay empty — an OOB error there means Step 8 is unfinished.

- [ ] **Step 12: Lint and commit**

```bash
uv run ruff check src tests && uv run ruff format src tests
git add src tests
git commit -m "feat(web): a shell with navigation, and collection moves to its own page"
```

---

### Task 3: The collection indicator in the shell

Start a long collection on «Сбор данных» and walk to «Вакансии» without waiting: the run must stay visible, and when it ends the table must refresh itself wherever the user is standing.

**Files:**
- Create: `src/jobhunt/web/templates/_collection_indicator.html`
- Modify: `src/jobhunt/web/templates/base.html`
- Modify: `src/jobhunt/web/routes/collection.py`
- Test: `tests/integration/test_web_shell.py`

**Interfaces:**
- Consumes: `page` from Task 2; `panel_context(session, profile_id, requested)` and `load_state` as they exist.
- Produces: `GET /collection/indicator`, and a shared helper `collected_trigger(response, state, is_htmx)` used by both fragment routes.

- [ ] **Step 1: Write the failing tests**

Add to `tests/integration/test_web_shell.py`:

```python
from datetime import UTC, datetime

from jobhunt.ingest.batches import finish_batch, open_batch

NOW = datetime.now(UTC)


def test_a_running_collection_is_visible_on_the_vacancies_page(client, session):
    """The run is a database row, so every page can ask about it. Without this
    the user who starts a collection and walks away has no way to know it is
    still going, and the table never learns that it ended."""
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    open_batch(session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW)
    session.commit()

    html = client.get("/vacancies").text

    assert 'id="collection-indicator"' in html
    assert "Собираю" in html
    assert "every 3s" in html


def test_the_indicator_is_present_but_idle_when_nothing_runs(client, session):
    """The element has to exist even when it says nothing: htmx throws
    htmx:targetError on a missing target and sends no request at all."""
    _profile(session)
    session.commit()

    html = client.get("/vacancies").text

    assert 'id="collection-indicator"' in html
    assert "every 3s" not in html


def test_the_collection_page_does_not_poll_twice(client, session):
    """The panel is the poller there. Two pollers for one batch would double
    the requests and race each other's swaps."""
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    open_batch(session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW)
    session.commit()

    html = client.get("/collection").text

    assert html.count("every 3s") == 1
    assert 'id="collection-indicator"' in html, "the target must exist even when idle"


def test_the_end_of_a_run_asks_the_indicator_to_reload_the_table(client, session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW
    )
    finish_batch(session, batch.id, now=NOW)
    session.commit()

    response = client.get("/collection/indicator", headers={"HX-Request": "true"})

    assert response.headers["HX-Trigger"] == "jobhunt-collected"
    assert "every 3s" not in response.text
```

- [ ] **Step 2: Run them and watch them fail**

```
uv run pytest tests/integration/test_web_shell.py -v -k "indicator or poll"
```

Expected: FAIL — no such element, and `/collection/indicator` is 404. The `-k`
expression must be quoted: unquoted, the shell reads `or` as its own operator.

- [ ] **Step 3: Create the indicator fragment**

Create `src/jobhunt/web/templates/_collection_indicator.html`:

```jinja
{# The compact «a collection is running» line for the shell.

   It exists on every page, including «Сбор данных» — an htmx target must be in
   the document whenever anything aims at it, and this element aims at itself.
   What is conditional is only the polling: on the collection page the full
   panel is the poller, and two pollers for one batch would double the requests
   and race each other's swaps.

   The polling rule is the panel's rule, and for the same reason: the attribute
   arrives while the batch runs and is absent from the first response after it
   ends, so htmx stops on its own. There is no timer of ours. #}
<div class="collection-indicator" id="collection-indicator"
     {% if collection.status == "running" and page != "collection" %}
     hx-get="/collection/indicator{{ profile_query }}"
     hx-target="#collection-indicator" hx-swap="outerHTML"
     hx-trigger="every 3s"
     {% endif %}>
  {% if collection.status == "running" %}
    <span class="collecting">Собираю: {{ collection.done }} из {{ collection.planned }} запросов</span>
  {% endif %}
</div>
```

- [ ] **Step 4: Put it in the shell**

In `base.html`, inside `_nav.html`'s sibling area — directly above `{% block content %}` inside `<main>` is fine — add:

```jinja
{% include "_collection_indicator.html" %}
```

It needs `collection`, `profile_query` and `page` in the context of **both** pages. `panel_context` already produces the first two and Task 2 added `page`; confirm `vacancies_page` spreads `**panel_context(...)` into its context, and add it if it does not.

- [ ] **Step 5: Add the route and share the trigger rule**

In `routes/collection.py`, extract the `HX-Trigger` decision the panel route already makes into a helper, then use it from both:

```python
def collected_trigger(response: HTMLResponse, state: CollectionState, request: Request) -> None:
    """Ask the page to reload its table, once, on the first response after a run ends.

    Gated on HX-Request because only htmx can hear the header: on a plain page
    load there is nobody on the other end, and the page is fresh anyway.

    Shared by the panel and the indicator rather than written twice: the two
    fragments answer the same question about the same batch, and a rule copied
    into both would drift the day one of them changes.
    """
```

Then:

```python
@router.get("/collection/indicator", response_class=HTMLResponse)
def collection_indicator(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    profile: Annotated[uuid.UUID | None, Query()] = None,
) -> HTMLResponse:
```

It resolves the profile the same way the panel route does, renders `_collection_indicator.html` with `**panel_context(...)` plus `page="vacancies"` (any value other than `"collection"` — the fragment is only ever requested by a page that is not the collection page), and calls `collected_trigger`.

- [ ] **Step 6: Run the tests**

```
uv run pytest tests/integration/test_web_shell.py tests/integration/test_web_collection.py -v
```

Expected: PASS.

- [ ] **Step 7: Prove it end to end in a browser**

```bash
docker compose restart app
```

On «Сбор данных» press «Проверить новое», then immediately click «Вакансии». The indicator must show the run and keep counting; when it ends the table must re-request itself once. Check the network panel: one `GET /collection/indicator` roughly every three seconds, then one `GET /vacancies/rows`, then silence.

- [ ] **Step 8: Lint and commit**

```bash
uv run ruff check src tests && uv run ruff format src tests
git add src tests
git commit -m "feat(web): a running collection stays visible on every page"
```

---

### Task 4: Filter tags derived from data

**Files:**
- Modify: `src/jobhunt/web/data/tags.py`
- Test: `tests/integration/test_web_tags.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `list_filter_tags(session, profile_id) -> list[dict]` with keys `id` (str), `text`, `is_enabled` — the same shape `list_tags` already returns, so templates can take either.

- [ ] **Step 1: Write the failing test**

Add to `tests/integration/test_web_tags.py`:

```python
def test_фильтр_теги_берутся_из_данных_а_не_из_списка_тегов(session):
    """Чип существует для тега, которым что-то НАЙДЕНО, а не для всякого
    заведённого тега.

    Ряд чипов описывает прошлое: что уже собрано и чем именно оно найдено.
    Тег, только что заведённый и ещё ничего не нашедший, чипа не даёт — иначе
    фильтр предлагал бы сузить список по признаку, которого нет ни у одной
    строки, и всегда давал бы пусто.
    """
    from jobhunt.web.data.tags import list_filter_tags

    profile = _profile(session)
    found = _tag(session, profile, "Head of IT", enabled=True)
    _tag(session, profile, "IT Director", enabled=True)  # ничего не нашёл
    _link(session, profile, _vacancy(session, "1"), found)
    session.commit()

    assert [t["text"] for t in list_filter_tags(session, profile.id)] == ["Head of IT"]


def test_фильтр_теги_включают_выключенный_тег_если_он_что_то_нашёл(session):
    """Выключенный тег больше не ищет, но найденное им никуда не делось, и
    добраться до этих вакансий можно только его чипом."""
    from jobhunt.web.data.tags import list_filter_tags

    profile = _profile(session)
    off = _tag(session, profile, "Head of IT", enabled=False)
    _link(session, profile, _vacancy(session, "1"), off)
    session.commit()

    tags = list_filter_tags(session, profile.id)
    assert [t["text"] for t in tags] == ["Head of IT"]
    assert tags[0]["is_enabled"] is False


def test_фильтр_теги_не_дублируются_на_нескольких_вакансиях(session):
    """Тег, нашедший три вакансии, — один чип, а не три."""
    from jobhunt.web.data.tags import list_filter_tags

    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    for external_id in ("1", "2", "3"):
        _link(session, profile, _vacancy(session, external_id), tag)
    session.commit()

    assert len(list_filter_tags(session, profile.id)) == 1


def test_фильтр_теги_чужого_профиля_не_видны(session):
    from jobhunt.web.data.tags import list_filter_tags

    mine = _profile(session, "Кирилл")
    theirs = _profile(session, "Второй")
    their_tag = _tag(session, theirs, "Head of IT", enabled=True)
    _link(session, theirs, _vacancy(session, "1"), their_tag)
    session.commit()

    assert list_filter_tags(session, mine.id) == []
```

- [ ] **Step 2: Run and watch them fail**

```
uv run pytest tests/integration/test_web_tags.py -v -k фильтр_теги
```

Expected: FAIL with `ImportError: cannot import name 'list_filter_tags'`.

- [ ] **Step 3: Implement it**

Add to `src/jobhunt/web/data/tags.py`:

```python
def list_filter_tags(session: Session, profile_id: uuid.UUID) -> list[dict]:
    """Tags that have actually found something for this profile.

    This is the chip row, and it is a projection of the DATA rather than of the
    tag list: a chip means "vacancies were found by this", so a tag that has
    found nothing yet has no chip. Disabled tags are included — they no longer
    search, but what they found is still in the table and their chip is the only
    way to reach it.

    Distinct on the tag: a tag that found thirty vacancies is one chip.
    """
    rows = session.execute(
        select(ProfileTag)
        .join(ProfileVacancyTag, ProfileVacancyTag.tag_id == ProfileTag.id)
        .join(ProfileVacancy, ProfileVacancy.id == ProfileVacancyTag.profile_vacancy_id)
        .where(ProfileVacancy.profile_id == profile_id)
        .distinct()
        .order_by(ProfileTag.created_at, ProfileTag.id)
    ).scalars()
    return [{"id": str(tag.id), "text": tag.text, "is_enabled": tag.is_enabled} for tag in rows]
```

Extend the existing imports in the file with `ProfileVacancy` and `ProfileVacancyTag`.

- [ ] **Step 4: Run the tests**

```
uv run pytest tests/integration/test_web_tags.py -v
```

Expected: PASS, all of them.

- [ ] **Step 5: Lint and commit**

```bash
uv run ruff check src tests && uv run ruff format src tests
git add src/jobhunt/web/data/tags.py tests/integration/test_web_tags.py
git commit -m "feat(web): filter tags are derived from what was found, not from the tag list"
```

---

### Task 5: The filter model — the marker, one checkbox, and the chips UI

Merged from what were Tasks 5 and 6, because they are one change: removing two
`VacancyFilters` fields breaks their callers in `routes/vacancies.py` and
`_filters.html` in the same instant, and a commit between the two halves is one
where `/vacancies` answers 500. The TDD cycle is run twice inside the task —
once for the query (Steps 1–4), once for the interface (Steps 5–9).

**Files:**
- Modify: `src/jobhunt/web/data/vacancies.py:22-38` (`VacancyFilters`) and `:99-150` (`build_vacancy_query`)
- Modify: `src/jobhunt/web/templates/_tag_chips.html`, `_filters.html`
- Modify: `src/jobhunt/web/routes/vacancies.py` (`_load_page`, `_filter_pairs`, `_empty_reason`, both handlers)
- Modify: `src/jobhunt/web/templates/_rows.html` (the new empty-state message)
- Test: `tests/integration/test_vacancy_filters.py`, `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: `list_filter_tags` (Task 4).
- Produces: `VacancyFilters(tags_set: bool = False, include_unchipped: bool = False, …)`. The fields `include_disabled_tags` and `include_untagged` are **gone**. The page and rows contexts carry `filter_tags` (from `list_filter_tags`) in addition to `tags` (from `list_tags`, still needed by `_empty_reason` and by the tags panel on the other page).

- [ ] **Step 1: Write the failing tests for the query**

Add to `tests/integration/test_vacancy_filters.py`:

```python
def test_без_маркера_список_наследует_включённые_теги(session):
    """Страница только открыта: чипы ещё никто не трогал, и список показывает
    то, что нашли ищущие теги, — прежнее поведение по умолчанию."""
    profile = _profile(session)
    on = _tag(session, profile, "Head of IT", enabled=True)
    off = _tag(session, profile, "IT Director", enabled=False)
    _link(session, profile, _vacancy(session, "1"), on)
    _link(session, profile, _vacancy(session, "2"), off)
    session.commit()

    rows = list_vacancies(session, profile.id, VacancyFilters()).rows

    assert [r["external_id"] for r in rows] == ["1"]


def test_маркер_с_пустым_набором_чипов_даёт_пустой_список(session):
    """Снять все чипы — осмысленная просьба «не показывай ничего», и раньше
    она означала ровно обратное: пустой набор читался как «фильтра нет».

    Маркер — единственное, чем эти два случая отличаются: форма шлёт только
    отмеченные галочки, поэтому «снял все» и «только открыл» приходят на
    сервер одинаково.
    """
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    session.commit()

    rows = list_vacancies(session, profile.id, VacancyFilters(tags_set=True)).rows

    assert rows == []


def test_маркер_с_чипами_показывает_найденное_этими_тегами(session):
    """И включённость тега тут ни при чём: чип — прямое «покажи это»."""
    profile = _profile(session)
    off = _tag(session, profile, "IT Director", enabled=False)
    _link(session, profile, _vacancy(session, "2"), off)
    session.commit()

    filters = VacancyFilters(tags_set=True, tag_ids=(uuid.UUID(str(off.id)),))
    rows = list_vacancies(session, profile.id, filters).rows

    assert [r["external_id"] for r in rows] == ["2"]


def test_чекбокс_вне_чипов_добавляет_вакансии_без_связок(session):
    """Один чекбокс вместо двух: он показывает то, до чего не дотягивается ни
    один чип. Это добавляемое условие, а не отмена чипов."""
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    _link(session, profile, _vacancy(session, "2"), None)  # сирота
    session.commit()

    default = list_vacancies(session, profile.id, VacancyFilters()).rows
    with_unchipped = list_vacancies(
        session, profile.id, VacancyFilters(include_unchipped=True)
    ).rows

    assert [r["external_id"] for r in default] == ["1"]
    assert sorted(r["external_id"] for r in with_unchipped) == ["1", "2"]


def test_снятые_чипы_плюс_чекбокс_дают_только_бестеговые(session):
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    _link(session, profile, _vacancy(session, "2"), None)
    session.commit()

    filters = VacancyFilters(tags_set=True, include_unchipped=True)
    rows = list_vacancies(session, profile.id, filters).rows

    assert [r["external_id"] for r in rows] == ["2"]


def test_чип_не_отменяет_остальные_фильтры(session):
    """Регрессия прежнего дефекта: блок чипов раньше делал ранний return, и
    условия, дописанные после него, тихо отменялись выбором чипа. Раннего
    return больше нет — этот тест держит его отсутствие."""
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1", city="Київ"), tag)
    _link(session, profile, _vacancy(session, "2", city="Львів"), tag)
    session.commit()

    filters = VacancyFilters(tags_set=True, tag_ids=(uuid.UUID(str(tag.id)),), city="Київ")
    rows = list_vacancies(session, profile.id, filters).rows

    assert [r["external_id"] for r in rows] == ["1"]
```

Check the helpers already in this file — `_profile`, `_tag`, `_vacancy`, `_link` — and match their signatures. If `_link` does not accept `None` for the tag, extend it rather than writing a second helper.

- [ ] **Step 2: Run and watch them fail**

```
uv run pytest tests/integration/test_vacancy_filters.py -v
```

Expected: FAIL — `VacancyFilters` has no `tags_set` or `include_unchipped`.

- [ ] **Step 3: Change the filters dataclass**

In `src/jobhunt/web/data/vacancies.py`, replace the two booleans with the marker and the single checkbox:

```python
    status: str | None = None
    source: str | None = None
    include_inactive: bool = False
    # Маркер «набор чипов задан пользователем». Форма шлёт только отмеченные
    # галочки, поэтому «снял все чипы» и «только открыл страницу» приходят
    # одинаково — пустым tag_ids, — а означают противоположное. Без маркера
    # различить их нечем (спека 2026-08-06, раздел 4.3).
    tags_set: bool = False
    # Показать то, до чего не дотягивается ни один чип: пары без единой связки
    # и пары, чьи теги больше не теги сбора. Заменяет прежние
    # include_disabled_tags и include_untagged — в новой модели у них была
    # одна работа на двоих.
    include_unchipped: bool = False
    tag_ids: tuple[uuid.UUID, ...] = ()
```

- [ ] **Step 4: Rewrite the tail of `build_vacancy_query`**

Replace everything from the `if filters.tag_ids:` block to the end of the function with:

```python
    # Ни одного раннего return: условия выше и условие по тегам теперь
    # складываются, а не исключают друг друга. Прежняя версия выходила из
    # функции внутри блока чипов, и любое условие, дописанное ПОСЛЕ него,
    # тихо отменялось выбором чипа — ошибка, которую не видно ни в одном
    # тесте, где чип и другие фильтры не проверяются вместе.
    chosen_link = (
        select(1)
        .select_from(ProfileVacancyTag)
        .where(
            ProfileVacancyTag.profile_vacancy_id == ProfileVacancy.id,
            ProfileVacancyTag.tag_id.in_(filters.tag_ids),
        )
        .exists()
    )
    enabled_link = (
        select(1)
        .select_from(ProfileVacancyTag)
        .join(ProfileTag, ProfileTag.id == ProfileVacancyTag.tag_id)
        .where(
            ProfileVacancyTag.profile_vacancy_id == ProfileVacancy.id,
            ProfileTag.is_enabled.is_(True),
        )
        .exists()
    )
    any_link = (
        select(1)
        .select_from(ProfileVacancyTag)
        .where(ProfileVacancyTag.profile_vacancy_id == ProfileVacancy.id)
        .exists()
    )
    if filters.tags_set:
        # Набор задан пользователем и авторитетен, в том числе когда он пуст.
        chips = chosen_link if filters.tag_ids else false()
    else:
        # Страница открыта как есть: начальное состояние чипов наследуется от
        # тегов сбора, и список обязан совпасть с тем, что покажут чипы.
        chips = enabled_link
    if filters.include_unchipped:
        return query.where(or_(chips, ~any_link))
    return query.where(chips)
```

Add `false` to the `sqlalchemy` import line at the top of the file.

- [ ] **Step 5: Run the query tests, and rewrite what the rename broke**

```
uv run pytest tests/integration/test_vacancy_filters.py -v
```

Expected: the new tests PASS. Existing tests that name `include_disabled_tags` or `include_untagged` will fail — **rewrite each one to the new field**, do not delete it. Every one of them encodes a behaviour that still has to hold.

The rest of the application does not compile against the new dataclass yet: `routes/vacancies.py` still passes the two removed fields, so `/vacancies` answers 500 and `test_web_vacancies.py` is red. That is expected in the middle of this task and must **not** be committed — Steps 6–9 close it, and the single commit at the end covers both halves.

- [ ] **Step 6: Write the failing tests for the interface**

Add to `tests/integration/test_web_vacancies.py`:

```python
def test_чип_отмечен_если_его_тег_ищется(client, session):
    """Начальное состояние чипа наследуется от тега сбора — это единственная
    связь между двумя ролями тега, и она односторонняя: чип не меняет сбор."""
    profile = _profile(session)
    on = _tag(session, profile, "Head of IT", enabled=True)
    off = _tag(session, profile, "IT Director", enabled=False)
    _link(session, profile, _vacancy(session, "1"), on)
    _link(session, profile, _vacancy(session, "2"), off)
    session.commit()

    html = client.get("/vacancies").text

    assert "checked" in _chip_snippet(html, on.id)
    assert "checked" not in _chip_snippet(html, off.id)


def test_ряд_чипов_несёт_маркер(client, session):
    """Без маркера снятые чипы неотличимы от неоткрытой страницы."""
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    session.commit()

    html = client.get("/vacancies").text

    assert 'name="tags_set"' in html


def test_контейнер_чипов_есть_даже_без_единого_тега(client, session):
    """Цель htmx-подмены обязана быть в документе всегда: на отсутствующую
    цель htmx не шлёт запрос вовсе и молчит об этом. Раньше весь контейнер
    стоял под {% if tags %}."""
    _profile(session)
    session.commit()

    assert 'id="tag-chips"' in client.get("/vacancies").text


def test_снятые_чипы_объясняют_пустоту(client, session):
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    session.commit()

    html = client.get("/vacancies/rows?tags_set=true").text

    assert "<tr" in html, "пустой ответ обязан быть строкой таблицы, а не пустотой"
    assert "теги" in html.lower()


def test_маркер_попадает_в_адрес(client, session):
    """«Я нарочно всё скрыл» обязано пережить перезагрузку и сохранённую
    ссылку: адрес описывает состояние показа."""
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    session.commit()

    response = client.get("/vacancies/rows?tags_set=true")

    assert "tags_set=true" in response.headers["HX-Push-Url"]
```

`_chip_snippet` already exists in `tests/integration/test_web_tags.py`; copy it into this file if it is not here — a copied helper is the repository's established pattern.

- [ ] **Step 7: Run and watch them fail**

```
uv run pytest tests/integration/test_web_vacancies.py -v -k "чип or маркер"
```

Expected: FAIL. The `-k` expression must be quoted: unquoted, the shell reads `or` as its own operator.

- [ ] **Step 8: Rewrite the chips template**

Replace `src/jobhunt/web/templates/_tag_chips.html` entirely:

> **Corrected 2026-08-06, during Task 5.** The sample below carried two defects,
> both found in review and both fixed in the code that shipped. It is corrected here
> so that a re-run of this plan cannot reintroduce them.
>
> **`chips_oob` is gone.** Task 2 removed the out-of-band chips from the tag
> toggle — the two controls now live on different pages and the fragment can never
> find its target. Keeping the attribute would also **fail** the out-of-band
> ownership guard Task 2 added: `OOB_TAG` matches across a Jinja `{% if %}` because
> that tag contains no `>`, so the literal alone declares `#tag-chips` as an OOB
> target that no page owns.
>
> **The marker is gated on there being a chip.** Rendering it unconditionally means
> a profile whose chip row is empty sends `tags_set` on every filter interaction,
> gets an empty table by construction, and is told «отметьте хотя бы один тег выше»
> pointing at a row with nothing in it. The **container** stays unconditional; only
> the input inside it is gated. The comment's stated reason for that was also wrong
> and is corrected below: the container is required by `hx-include=".chips"`, not by
> the swap-target invariant.
>
> **Amended 2026-08-06, after the whole-branch review.** That correction ended «— and
> nothing tests it», which was already false when it was written and is further from
> true now. Two tests added by this very task hold the container:
> `test_контейнер_чипов_есть_даже_без_единого_тега` (a profile with no tags still gets
> the container) and `test_маркера_нет_когда_чипов_нет` (the container is there while
> the marker is not). What was genuinely unguarded is the **`hx-include` pickup** — the
> `class="chips"` on this container against the `.chips` selector in `_filters.html`,
> either of which could have moved alone — and the review closed that with
> `test_the_chips_selector_matches_the_chip_row`, which reads the selector out of the
> form and holds it against the container as rendered. The spec's own wording is the
> accurate shape of the claim: **no *invariant* covers that**, which stays true even
> now that `#tag-chips` is a real `hx-target`, because a container that stopped
> rendering would take its own `hx-target` declaration with it.
>
> The sample below is Task 5's markup and is left as Task 5 wrote it. The container it
> renders later gained `hx-get="/vacancies/chips"`, `hx-target="#tag-chips"`,
> `hx-swap="outerHTML"` and `hx-trigger="jobhunt-collected from:body"` when the
> whole-branch review's Critical was closed — the chip row re-derives itself at the end
> of a collection, or a tag that found its first vacancy *during* the run has no chip,
> rides along in no request, and is filtered out of the table that just refreshed to
> show it. A re-run of this plan gets a correct Task 5 and then needs that fix.

```jinja
{# The chip row: one chip per tag that has actually found something.

   The container renders even when there is no chip in it, and NOT because of the
   swap-target invariant: that invariant reads declarations out of the rendered
   page, so a container that stopped rendering would take its own declaration with
   it and the check would still pass. It renders because the filters form and the
   search field both carry hx-include=".chips" — an element that is not in the
   document is not included, and the marker below would silently stop riding along.
   Two tests hold the container itself: test_контейнер_чипов_есть_даже_без_единого_
   тега and test_маркера_нет_когда_чипов_нет. What no test held until the final
   review is the CLASS and the selector that reads it — see
   test_the_chips_selector_matches_the_chip_row.

   tags_set is the marker. A form submits only its CHECKED boxes, so "the user
   unchecked everything" and "the user has just opened the page" reach the
   server identically — as a request with no `tag` values — and they must mean
   opposite things. The hidden field rides along with the chips through
   hx-include=".chips" and separates them.

   It is rendered only when a chip exists: a page that never offered a chip has no
   business claiming one was cleared, and without this gate a profile that has
   collected nothing yet is told to tick a chip that is not there.

   A chip's initial state is inherited from its collection tag, and only its
   initial state: once the marker is present, what the user checked is
   authoritative and is_enabled has no further say. #}
<div class="chips" id="tag-chips">
  {% if filter_tags %}<input type="hidden" name="tags_set" value="true">{% endif %}
  {% for tag in filter_tags %}
    <label class="chip {% if not tag.is_enabled %}chip-off{% endif %}">
      <input type="checkbox" name="tag" value="{{ tag.id }}"
             {% if current.tags_set %}{% if tag.id in selected_tag_ids %}checked{% endif %}
             {% elif tag.is_enabled %}checked{% endif %}
             hx-get="/vacancies/rows" hx-include="#filters, .chips"
             hx-target="#rows" hx-swap="innerHTML">
      {{ tag.text }}{% if not tag.is_enabled %} (не ищется){% endif %}
    </label>
  {% endfor %}
</div>
```

- [ ] **Step 9: Collapse the two checkboxes into one**

In `_filters.html`, delete both of these lines:

```jinja
  <label><input type="checkbox" name="include_disabled_tags" value="true"
         {% if current.include_disabled_tags %}checked{% endif %}> вакансии выключенных тегов</label>
  <label><input type="checkbox" name="include_untagged" value="true"
         {% if current.include_untagged %}checked{% endif %}> найденные ранее</label>
```

and put one in their place:

```jinja
  <label><input type="checkbox" name="include_unchipped" value="true"
         {% if current.include_unchipped %}checked{% endif %}> показать вакансии, у которых нет тега фильтра</label>
```

- [ ] **Step 10: Thread the parameters through the routes**

In `routes/vacancies.py`:

1. `_load_page` — replace the `include_disabled_tags` and `include_untagged` parameters with `tags_set: bool` and `include_unchipped: bool`, and pass them into `VacancyFilters`.
2. Both handlers — replace the two `Query` parameters with `tags_set: Annotated[bool, Query()] = False` and `include_unchipped: Annotated[bool, Query()] = False`. Follow the existing pattern for boolean query parameters in this file exactly; do not introduce a second convention.
3. `_filter_pairs` — replace the two entries with:

```python
        "tags_set": "true" if filters.tags_set else "",
        "include_unchipped": "true" if filters.include_unchipped else "",
```

4. The page context — add `"filter_tags": list_filter_tags(session, resolved.id) if resolved else []`. Keep `tags` as it is: `_empty_reason` needs it to tell «тегов нет вовсе» from «все выключены», and the tags panel on the other page still uses it.
5. The rows context in `vacancy_rows` — add the same `filter_tags`.
6. `_empty_reason` — add a branch **before** the «фильтры заданы» branch:

```python
    if filters.tags_set and not filters.tag_ids and not filters.include_unchipped:
        return "chips_cleared"
```

and add the matching message to `_rows.html`:

```jinja
{% elif empty_reason == "chips_cleared" %}
<tr><td class="empty" colspan="{{ columns }}">Сняты все теги фильтра — показывать нечего.
  Отметьте хотя бы один тег выше, чтобы вернуть список.</td></tr>
```

Put it beside the existing branches, matching their shape. The order matters for the same reason the docstring already gives: a reason that is true and specific must be reported before a reason that is true and vague.

`routes/tags.py` needs nothing here: Task 2 removed the chips from the toggle's response, so the toggle no longer renders `_tag_chips.html` and has no chip context to keep current.

- [ ] **Step 11: Run the tests**

```
uv run pytest tests/integration/test_web_vacancies.py tests/integration/test_web_tags.py tests/integration/test_vacancy_filters.py -v
```

Expected: PASS. The swap-target invariant is in the first file and must stay green.

- [ ] **Step 12: Walk it in a browser**

```bash
docker compose restart app
```

Uncheck every chip: the table must empty and explain itself, and the address must carry `tags_set=true`. Reload: the list must still be empty. Check one chip: the rows come back. Disable a tag on «Сбор данных», return to «Вакансии»: that chip is now unchecked by default but present, and one click brings its vacancies back.

- [ ] **Step 13: Lint and commit**

One commit for the whole task — the query and its callers change together.

```bash
uv run ruff check src tests && uv run ruff format src tests
git add src tests
git commit -m "feat(web): chips are a visibility set, and clearing them empties the list"
```

---

### Task 6: The vendored stylesheet — **DROPPED, 2026-08-06**

> **Not done, by the owner's decision, and the separability clause below is what
> made that cheap.** The task was implemented against Pico CSS and reverted
> (`c8cc50f`, reverted by `7abf211`) after the review and the browser walk raised
> questions the task could not settle on its own.
>
> **What the implementation established, and it is worth keeping:** Pico's
> *classless* build has no `.secondary` opt-out — verified, all 53 occurrences of
> the word in the vendored file are variable names — so every button rendered
> primary-blue, including «Показать ещё» and the theme toggle, which are secondary
> actions. Pico's *default* build does have `.secondary`, `.outline` and
> `.contrast`, the same `[data-theme]` switching, at 83 KB against 71 KB — and the
> classless build's distinguishing feature, `header`/`main`/`footer` acting as
> containers, is **inert in this markup**, because `<main>` is not a direct child
> of `<body>`. The slice chose a build for a property it cannot use and paid for it
> with the button variants.
>
> **Why it became its own slice rather than a fix here.** The owner asked what a
> larger component library would give, and the research changed the question:
> **no table library leaves a server-rendered `<table>` on screen.** All seven
> investigated — Tabulator, AG Grid Community, Grid.js, DataTables 3, Frappe
> DataTable, RevoGrid, Vaadin Grid — render rows from JSON once initialised, free
> server-side modes included. Adopting one ends htmx's role on the main page. The
> owner's decision: **the server keeps rendering the table**, and the visual layer
> becomes a slice of its own with its own design document.
>
> Carried into that slice: Bulma matches this project's theme toggle exactly
> (`data-theme` on any element, plus a `prefers-color-scheme` fallback in its own
> CSS, so the three-state toggle needs no change) and ships **no JavaScript at
> all**, which removes the htmx re-initialisation question entirely. Icons are a
> separate, cheap decision — individual SVGs in a Jinja macro, `currentColor`
> already baked in, rather than a 0.5–1.8 MB sprite for twenty glyphs.
>
> The steps below are left as written, for whoever picks the visual slice up.

Separable — if it goes wrong, drop this task and the slice still stands.

**Files:**
- Create: `src/jobhunt/web/static/pico.min.css`
- Modify: `src/jobhunt/web/templates/base.html`

**Interfaces:**
- Consumes: `page`, and the class names introduced in Tasks 2, 3 and 5.
- Produces: nothing other tasks read.

- [ ] **Step 1: Vendor the file**

Download Pico.css v2 (classless build) and save it as `src/jobhunt/web/static/pico.min.css`. This is a vendored asset, exactly as `htmx.min.js` already is: a file in `static/`, a link tag, no package manager and no build step. Record the version and the source URL in a comment at the top of the file.

- [ ] **Step 2: Link it before our own styles**

In `base.html`, above the existing `<style>` block:

```jinja
  <link rel="stylesheet" href="/static/pico.min.css">
```

Order matters: ours must come second so it can override.

- [ ] **Step 3: Delete what the framework now provides**

Go through the 172 lines of the existing `<style>` block and remove every rule the framework already covers — base typography, table borders and padding, form controls, focus rings. **Keep** everything the framework knows nothing about: `.chip`, `.chip-off`, `.collection`, `.collection-status`, `.collecting`, `.nav`, `.nav-pages`, `.layout`, `.page`, `.empty`, `.muted`, `.scroll`.

> **Corrected 2026-08-06, after Task 3's review.** This list used to name
> `.collection-indicator`, which is the indicator's outer element and carries **no
> rule at all** — it is a hook the markup declares and nothing styles. What actually
> carries the indicator's spacing, size and colour is `.collecting`, the span inside
> it (`base.html`), and the list did not mention it. A mechanical pass over the old
> list would have kept the empty hook and deleted the live rule, and the indicator
> would have gone unstyled on every page — the precise failure this task's Step 4
> exists to catch, arrived at by following the plan rather than by ignoring it.
> Keep `.collection-indicator`'s *markup* as it is; it is the swap target and the
> class stays as a styling seam.

Pico switches themes with `data-theme="light|dark"` on `<html>`, which is the attribute the existing theme toggle already writes — check that the toggle still lines up rather than assuming it.

- [ ] **Step 4: Walk both themes in a browser**

```bash
docker compose restart app
```

Both pages, both themes. Check specifically: the chip row (checked, unchecked, `chip-off`), both collection buttons (enabled and disabled), the status line, the status `<select>` in a table row, the navigation with `aria-current`, the empty state, and keyboard focus on every interactive element. Slice 2a's live check already found once that new elements had been left with no styles at all — that is the failure mode here.

- [ ] **Step 5: Run the web tests**

```
uv run pytest tests/integration/test_web_vacancies.py tests/integration/test_web_shell.py -v
```

Expected: PASS. Nothing in this task should touch behaviour; if a test fails, you deleted markup rather than styles.

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/web/static/pico.min.css src/jobhunt/web/templates/base.html
git commit -m "style(web): a vendored stylesheet replaces the hand-written palette"
```

---

### Task 7: Live check and documentation

**Files:**
- Modify: `docs/HANDOFF.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Walk the browser checklist**

Against the running app on the production database, recording each result. Read `docs/HANDOFF.md` §5в first — the two harness traps are still live: Cyrillic typed through `insertText` fires no `keyup`, and a first batch of 50 is not a full list. Add the trap §5г recorded: collection runs are ~14 s and ~23 s, shorter than hand timing, so anything that must happen during a run has to be issued in the same command that starts it.

1. Navigation moves between the pages, marks the current one, and keeps the selected profile.
2. A run started on «Сбор данных» stays visible after walking to «Вакансии»; when it ends the table re-requests itself exactly once.
3. On «Сбор данных» there is exactly one poller — one `GET /collection/panel` every three seconds and no `GET /collection/indicator`.
4. Unchecking every chip empties the table with an explanation; the address carries `tags_set=true`; a reload keeps it empty; one chip brings the rows back.
5. A chip's initial state follows its collection tag: disable a tag on «Сбор данных», return, and it is unchecked but present.
6. `jobhunt tag remove` refuses and names the link count; `jobhunt tag list` shows the tag still there afterwards.
7. Toggling a tag on «Сбор данных» updates the panel and the collection buttons, and writes nothing to the console — the chips are on the other page now and no longer ride along out of band.
8. Both themes, both pages, keyboard focus visible throughout.
9. The browser console has nothing in it but the documented `/favicon.ico` 404.

- [ ] **Step 2: Record the results**

Add a section to `docs/HANDOFF.md` in the shape of §5в and §5г: a table of scenario and result, the numbers, and anything the check found that the plan did not predict. If production data changed, say what and what was compared afterwards.

- [ ] **Step 3: Correct what the slice made false**

In `CLAUDE.md`:
- The invariant «In `build_vacancy_query`, the chip filter (`tag_ids`) does an early `return`» is **gone** — Task 5 removed the early return. Replace it with the rule that replaced it: every tag condition is combined at the end, and `tags_set` distinguishes an empty chip set from an untouched page.
- Add: the web layer now has two pages, and the swap-target invariant covers both.

In `docs/HANDOFF.md` §6:
- The row «Веб-таблица без пагинации | Фильтр по статусу считается в Python после загрузки всех строк» is wrong on both counts and has been for two slices: `PAGE_SIZE = 50` with «показать ещё», and status is a `where()` clause. Delete it.
- Add the limitation this slice keeps: an idle page still does not poll, so a page left open does not notice a collection started afterwards in another tab or from the terminal. Walking to another page is a full load and does notice.
- Add: `jobhunt tag remove` refuses until soft deletion exists, and the «tags that are no longer collection tags» half of the unchipped checkbox is empty until then.
- The file points at `.superpowers/sdd/progress.md` in four places as the ledger of slice 2b. That ledger was renamed to `.superpowers/sdd/progress-collection-from-the-browser.md` when this slice started its own; correct every reference, or the next session reads slice 3's ledger looking for 2b's Minor findings.
- The slice has **seven** tasks, not eight — Tasks 5 and 6 were merged before execution (see the plan's amendments section). Section 0 says eight. **Six of the seven shipped**: Task 6, the vendored stylesheet, was dropped by the owner and is now a slice of its own. Record why, and record what its abandoned implementation established, so the next slice starts from evidence rather than from scratch — the plan's Task 6 section carries it.
- Add a §6 row: **no table library leaves a server-rendered `<table>` on screen.** Seven were investigated and all of them render rows from JSON once initialised, free server-side modes included, so adopting one ends htmx's role on the vacancies page. This **strengthens** the design's §9 rather than correcting it: §9 rejected the libraries because they «want to own the data and render it client-side, which contradicts the invariant that every condition goes to the database and only `PAGE_SIZE` rows come back» — which is exactly what the seven downloads confirmed. The owner's decision stands: the server keeps rendering the table.

  > **Corrected 2026-08-06, after the whole-branch review.** This bullet used to say
  > §9 «rejected table libraries on a narrower and partly wrong ground — that they
  > cannot do server-side filtering». **No document says that.** §9 of
  > `docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md` gives the
  > client-side-rendering reason quoted above, and it is correct. The false
  > attribution was written here and copied into `docs/HANDOFF.md` and the ledger; all
  > three are corrected. The seven verified downloads are new **evidence for** §9.

- [ ] **Step 4: Commit**

```bash
git add docs/HANDOFF.md CLAUDE.md
git commit -m "docs: live check of the shell and the two pages"
```

---

## Controller's checklist after the last task

- [ ] `uv run pytest -q` — the whole suite, once, in the main session
- [ ] `uv run ruff check src tests` and `uv run ruff format --check src tests`
- [ ] `docker compose restart app` and one manual look at both pages
- [ ] `superpowers:requesting-code-review` — whole branch against `main`, pointed at the ledger's Minor list
- [ ] `superpowers:finishing-a-development-branch`
