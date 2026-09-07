# «Вакансии» как инструмент (слайс 2a) — план реализации

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Превратить `/vacancies` из плоского списка в рабочее место: показывать по умолчанию только то, что сейчас ищется и висит на площадке, сужать список шестью фильтрами и чипами тегов, переключать теги мышью, листать пачками и выбирать профиль.

**Architecture:** Весь SQL уезжает из роутов в новый пакет `web/data/` — он один знает про БД, и это закрепляется AST-тестом. Страница обновляется htmx-фрагментами: фильтры и чипы делают `hx-get` на `/vacancies/rows`, который возвращает готовые `<tr>`; состояние живёт в адресной строке. Клиентского JavaScript не добавляется вовсе, кроме уже подключённого htmx.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0 (императивный `select()`), Jinja2, htmx 2 (уже в `/static/htmx.min.js`), PostgreSQL 17, pytest.

**Спека:** `docs/superpowers/specs/2026-08-05-vacancies-as-a-tool-design.md`. Номера разделов ниже (§4.1, §5.2 и т.д.) ссылаются на неё.

## Global Constraints

- `uv` **не** в PATH. Все команды — `python -m uv run ...`, а не `uv run ...`.
- Тесты: `python -m uv run pytest`. Линтер: `python -m uv run ruff check src tests`, формат: `python -m uv run ruff format src tests`. Оба обязаны быть чистыми перед каждым коммитом. `ruff format --check .` на каталоге `docs/` шумит на markdown-блоках — это известно, проверяйте только `src tests`.
- Ширина строки 100 (`pyproject.toml`, `[tool.ruff]`).
- Новых зависимостей не добавлять: ни Python-пакетов, ни npm. htmx уже лежит в репозитории.
- Веб-роуты берут сессию только через `Depends(get_session)`, никогда через `session_scope()`.
- Вакансии пишет только `ingest/upsert.py`; веб-слой не создаёт `Vacancy` и не пишет её поля (граница `tests/unit/test_vacancy_write_boundary.py` это ловит). `ProfileVacancy.status` веб писать вправе.
- Интерфейс на русском; значения статусов остаются английскими идентификаторами (`new`, `applied`, …) — переименование в объём слайса не входит.
- Консоль хоста cp1252: любая новая точка входа, печатающая кириллицу, начинается с `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`.
- Docker Desktop часто не запущен. Признак — `cannot find the path ... dockerDesktopLinuxEngine`. Поднимается через `Start-Process "$env:LOCALAPPDATA\Programs\DockerDesktop\Docker Desktop.exe"`, дальше опрашивать `docker info`, а не спать вслепую.
- Тестовая БД задаётся `TEST_DATABASE_URL` (см. `tests/conftest.py`); прогон тестов на боевой БД запрещён.
- Размер пачки — 50 строк, константа `PAGE_SIZE` в `web/data/vacancies.py`, ни в одном другом месте не дублируется.

**Замечание о порядке задач.** Раздел 13 спеки требует начинать с задачи «запрос в SQL + фрагмент + замер» и одновременно требует, чтобы разделение `web/` прошло **до** того, как в файлы поедет новая логика. Эти два требования конфликтуют, поэтому механический перенос вынесен в задачу 1 (поведение не меняется ни на байт, страховка — существующие 407 тестов), а запрос, фрагмент и замер идут задачей 2 — до любой работы над интерфейсом. Число из замера вписывается в этот файл в шаге 8 задачи 2.

---

## Структура файлов

| Файл | Ответственность |
|---|---|
| `src/jobhunt/web/data/__init__.py` | пустой, помечает пакет |
| `src/jobhunt/web/data/vacancies.py` | `VacancyFilters`, построение запроса, выборка строк, чтение и запись статуса |
| `src/jobhunt/web/data/tags.py` | теги профиля для чипов и панели, переключение `is_enabled` |
| `src/jobhunt/web/data/profiles.py` | список профилей, разрешение выбранного |
| `src/jobhunt/web/routes/vacancies.py` | обработчики: страница, фрагмент строк, POST статуса |
| `src/jobhunt/web/routes/tags.py` | обработчик переключателя тега |
| `src/jobhunt/web/templates/vacancies.html` | каркас страницы |
| `src/jobhunt/web/templates/_filters.html` | форма фильтров |
| `src/jobhunt/web/templates/_tag_chips.html` | чипы тегов (фильтр показа) |
| `src/jobhunt/web/templates/_tags_panel.html` | панель тегов с переключателем `is_enabled` |
| `src/jobhunt/web/templates/_rows.html` | строки таблицы + строка «показать ещё» |
| `tests/unit/test_web_boundary.py` | AST-граница: роуты не обращаются к БД |
| `tests/integration/test_vacancy_filters.py` | фильтры и состав списка |
| `tests/integration/test_vacancy_paging.py` | пачки и устойчивость порядка |
| `tests/integration/test_web_tags.py` | чипы и переключатель тега |
| `tests/integration/test_web_profiles.py` | выбор профиля |

---

### Task 1: Доступ к данным переезжает в `web/data/`

Механический перенос без изменения поведения. Делается до новой логики: иначе разделять придётся вдвое больший файл.

**Files:**
- Create: `src/jobhunt/web/data/__init__.py`
- Create: `src/jobhunt/web/data/vacancies.py`
- Modify: `src/jobhunt/web/routes/vacancies.py`
- Create: `tests/unit/test_web_boundary.py`
- Modify: `tests/integration/test_web_vacancies.py:9`
- Modify: `tests/integration/test_status_change.py:9`

**Interfaces:**
- Consumes: ничего (первая задача).
- Produces: `jobhunt.web.data.vacancies` с `STATUSES: tuple[str, ...]`, `RESPONDED_STATUSES: tuple[str, ...]`, `list_vacancies(session, profile_id, status=None, source=None, include_inactive=False) -> list[dict]`, `set_status(session, profile_id, vacancy_id, status) -> ProfileVacancy`, `effective_status(session, profile_id, vacancy_id) -> str`, `pair_exists(session, profile_id, vacancy_id) -> bool`.

- [ ] **Step 1: Завести пакет и перенести код без правок**

Создать `src/jobhunt/web/data/__init__.py` пустым файлом.

Создать `src/jobhunt/web/data/vacancies.py` и перенести в него из `web/routes/vacancies.py` **дословно**, вместе с докстрингами и комментариями: константы `STATUSES` и `RESPONDED_STATUSES`, функции `_tags_by_pair`, `list_vacancies`, `set_status`, `_effective_status` (переименовать в `effective_status` — она перестаёт быть приватной для модуля роутов). Импорты в начале файла:

```python
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import ProfileTag, ProfileVacancy, ProfileVacancyTag, Vacancy
```

Добавить туда же функцию, забирающую из роута последний прямой запрос к БД:

```python
def pair_exists(session: Session, profile_id: uuid.UUID, vacancy_id: uuid.UUID) -> bool:
    """Видел ли этот профиль эту вакансию.

    Проверка идёт по паре, а не по Vacancy.id: последнее не различает
    «вакансии не существует вовсе» и «вакансия есть, но этот профиль её
    никогда не видел». Во втором случае фолбэк set_status создал бы пару с
    is_active=True и сделал бы вакансию видимой задним числом.
    """
    return (
        session.execute(
            select(ProfileVacancy.id).where(
                ProfileVacancy.profile_id == profile_id,
                ProfileVacancy.vacancy_id == vacancy_id,
            )
        ).scalar_one_or_none()
        is not None
    )
```

- [ ] **Step 2: Переписать роуты на новый модуль**

В `web/routes/vacancies.py` удалить перенесённое и импортировать:

```python
from jobhunt.web.data.vacancies import (
    STATUSES,
    effective_status,
    list_vacancies,
    pair_exists,
    set_status,
)
```

Выбор профиля в `vacancies_page` и `change_status` пока остаётся прямым `select(Profile)` — он уедет в задаче 8, граница в шаге 4 это учитывает.

- [ ] **Step 3: Починить импорты в тестах**

`tests/integration/test_web_vacancies.py:9` и `tests/integration/test_status_change.py:9`:

```python
from jobhunt.web.data.vacancies import list_vacancies   # было jobhunt.web.routes.vacancies
from jobhunt.web.data.vacancies import set_status       # во втором файле
```

- [ ] **Step 4: Написать падающую границу**

Создать `tests/unit/test_web_boundary.py`:

```python
"""Граница «веб-роуты не обращаются к БД напрямую».

Роуты разбирают запрос и рендерят ответ; запросы живут в web/data/. Без
этой границы SQL расползается обратно по обработчикам, и одинаковый по
смыслу фильтр начинает существовать в двух редакциях — ровно то, что уже
произошло со статусом: он фильтровался в Python в роуте, хотя источник и
активность фильтровались в SQL.

profiles.py временно в исключениях: выбор профиля переезжает в web/data
задачей 8 этого же плана. Исключение обязано исчезнуть вместе с ней.
"""

import ast
import pathlib

ROUTES_DIR = pathlib.Path(__file__).resolve().parents[2] / "src" / "jobhunt" / "web" / "routes"
FORBIDDEN_CALLS = {"select", "insert", "update", "delete", "text"}
FORBIDDEN_METHODS = {"execute", "scalars", "scalar", "add", "add_all", "flush", "query"}


def violations(source: str, name: str) -> list[str]:
    """Обращения к БД в одном файле роутов."""
    offenders: list[str] = []
    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Name) and func.id in FORBIDDEN_CALLS:
            offenders.append(f"{name}:{node.lineno}: строит запрос {func.id}(...)")
        if isinstance(func, ast.Attribute) and func.attr in FORBIDDEN_METHODS:
            offenders.append(f"{name}:{node.lineno}: вызывает session.{func.attr}(...)")
    return offenders


def test_роуты_не_обращаются_к_бд():
    offenders: list[str] = []
    for path in sorted(ROUTES_DIR.glob("*.py")):
        offenders.extend(violations(path.read_text(encoding="utf-8"), path.name))
    assert offenders == [], "SQL вернулся в роуты: " + "; ".join(offenders)


def test_граница_ловит_обе_формы():
    """Проверка на синтетическом источнике: прогон по заведомо чистым файлам
    ничего не доказывает — он был бы зелёным и при пустой реализации."""
    assert violations("rows = session.execute(select(Vacancy)).all()", "x.py") == [
        "x.py:1: строит запрос select(...)",
        "x.py:1: вызывает session.execute(...)",
    ]
    assert violations("session.add(pair)", "x.py") == ["x.py:1: вызывает session.add(...)"]
    assert violations("rows = list_vacancies(session, profile_id)", "x.py") == []
```

- [ ] **Step 5: Прогнать границу — она обязана упасть**

Run: `python -m uv run pytest tests/unit/test_web_boundary.py -q`
Expected: FAIL — `test_роуты_не_обращаются_к_бд` показывает `vacancies.py:NNN: строит запрос select(...)` (выбор профиля).

- [ ] **Step 6: Внести временное исключение для выбора профиля**

> **Как сделано на самом деле** (ревью задачи 1). Сверка множеством, как ниже, пропускает молча любое **новое** вхождение того же вида: ключ без номера строки у всех вхождений одинаков. В коде исключение сверяет `Counter` с базой известных (по 2 на каждый из трёх видов, включая `session.scalars(...)`, которого в наброске ниже нет), логика вынесена в функцию `unexpected(offenders, allowed)`, а константа названа `ALLOWED_UNTIL_TASK_7`. Набросок ниже оставлен как запись замысла.

В `tests/unit/test_web_boundary.py` заменить тело `test_роуты_не_обращаются_к_бд`:

```python
# Строки выбора профиля: уезжают в web/data/profiles.py задачей 8. Исключение
# именованное и узкое — по тексту нарушения, а не по файлу целиком, иначе оно
# накрыло бы и любой новый запрос, который в этот файл добавят.
ALLOWED_UNTIL_TASK_8 = {"vacancies.py: строит запрос select(...)", "vacancies.py: вызывает session.execute(...)"}


def test_роуты_не_обращаются_к_бд():
    offenders: list[str] = []
    for path in sorted(ROUTES_DIR.glob("*.py")):
        offenders.extend(violations(path.read_text(encoding="utf-8"), path.name))
    unexpected = [
        o for o in offenders if f"{o.split(':')[0]}: {o.split(': ', 1)[1]}" not in ALLOWED_UNTIL_TASK_8
    ]
    assert unexpected == [], "SQL вернулся в роуты: " + "; ".join(unexpected)
```

- [ ] **Step 7: Прогнать всё**

Run: `python -m uv run pytest -q`
Expected: PASS, 409 passed (407 прежних + 2 новых). Ни один существующий тест не менял ожиданий — если что-то упало, перенос был не дословным.

Run: `python -m uv run ruff check src tests` и `python -m uv run ruff format src tests`
Expected: чисто.

- [ ] **Step 8: Коммит**

```bash
git add src/jobhunt/web/data tests/unit/test_web_boundary.py src/jobhunt/web/routes/vacancies.py tests/integration/test_web_vacancies.py tests/integration/test_status_change.py
git commit -m "refactor(web): доступ к данным вынесен в web/data, граница под AST-тестом"
```

---

### Task 2: Фильтры в SQL, фрагмент строк, замер отклика

**Files:**
- Modify: `src/jobhunt/web/data/vacancies.py`
- Modify: `src/jobhunt/web/routes/vacancies.py`
- Create: `src/jobhunt/web/templates/_rows.html`
- Modify: `src/jobhunt/web/templates/vacancies.html`
- Create: `tests/integration/test_vacancy_filters.py`

**Interfaces:**
- Consumes: `list_vacancies`, `STATUSES` из задачи 1.
- Produces: `PAGE_SIZE: int`, `VacancyFilters` (frozen dataclass), `build_vacancy_query(profile_id, filters) -> Select`, `list_vacancies(session, profile_id, filters) -> VacancyPage` где `VacancyPage` — `dataclass(rows: list[dict], has_more: bool)`; роут `GET /vacancies/rows`.

- [ ] **Step 1: Написать падающий тест на фильтр статуса в SQL**

Создать `tests/integration/test_vacancy_filters.py`:

```python
import uuid
from datetime import UTC, datetime, timedelta

from jobhunt.db.models import Profile, ProfileVacancy, Vacancy
from jobhunt.web.data.vacancies import VacancyFilters, build_vacancy_query, list_vacancies

NOW = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)


def _profile(session, name="Кирилл") -> Profile:
    profile = Profile(name=name, collection_cities=[])
    session.add(profile)
    session.flush()
    return profile


def _vacancy(session, external_id: str, **overrides) -> Vacancy:
    base = {
        "source": "work.ua",
        "external_id": external_id,
        "title": f"Роль {external_id}",
        "company": "Garvis",
        "url": f"https://www.work.ua/jobs/{external_id}/",
        "description_raw": "Опис",
        "description_hash": f"h{external_id}",
        "city": "Київ",
        "city_any": False,
        "work_format": "onsite",
        "posted_at": NOW,
        "first_seen_at": NOW,
        "last_seen_at": NOW,
    }
    base.update(overrides)
    vacancy = Vacancy(**base)
    session.add(vacancy)
    session.flush()
    return vacancy


def _pair(session, profile: Profile, vacancy: Vacancy, **overrides) -> ProfileVacancy:
    base = {
        "profile_id": profile.id,
        "vacancy_id": vacancy.id,
        "first_seen_at": NOW,
        "last_seen_at": NOW,
    }
    base.update(overrides)
    pair = ProfileVacancy(**base)
    session.add(pair)
    session.flush()
    return pair


def test_фильтр_статуса_считается_в_бд(session):
    """До этой правки статус отбирался в Python после загрузки ВСЕХ строк
    профиля: ради показа 50 строк из базы приезжали все. Проверяется не
    только результат, но и то, что условие ушло в SQL, — результат был бы
    одинаковым в обеих реализациях."""
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1"), status="applied")
    _pair(session, profile, _vacancy(session, "2"), status="new")

    page = list_vacancies(session, profile.id, VacancyFilters(status="applied"))

    assert [row["external_id"] for row in page.rows] == ["1"]
    sql = str(build_vacancy_query(profile.id, VacancyFilters(status="applied")))
    assert "profile_vacancies.status" in sql, f"статус обязан фильтроваться в SQL, запрос: {sql}"


def test_фильтры_складываются_а_не_затирают_друг_друга(session):
    """Два условия сразу — классическая ошибка построителя запросов: второй
    where() перезаписывает первый или теряется вовсе."""
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1", source="work.ua"), status="applied")
    _pair(session, profile, _vacancy(session, "2", source="dou.ua"), status="applied")
    _pair(session, profile, _vacancy(session, "3", source="dou.ua"), status="new")

    page = list_vacancies(session, profile.id, VacancyFilters(status="applied", source="dou.ua"))

    assert [row["external_id"] for row in page.rows] == ["2"]


def test_неактивные_показываются_только_с_флагом(session):
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1"))
    _pair(session, profile, _vacancy(session, "2"), is_active=False)

    assert [r["external_id"] for r in list_vacancies(session, profile.id, VacancyFilters()).rows] == ["1"]
    both = list_vacancies(session, profile.id, VacancyFilters(include_inactive=True)).rows
    assert sorted(r["external_id"] for r in both) == ["1", "2"]
```

- [ ] **Step 2: Прогнать — обязан упасть на импорте**

Run: `python -m uv run pytest tests/integration/test_vacancy_filters.py -q`
Expected: FAIL — `ImportError: cannot import name 'VacancyFilters'`.

- [ ] **Step 3: Реализовать фильтры и запрос**

В `src/jobhunt/web/data/vacancies.py` добавить сверху (после существующих импортов дописать `from dataclasses import dataclass, field` и `from sqlalchemy import Select`):

```python
# Размер пачки. Единственное место, где это число задано: шаблон и роут
# берут его отсюда, иначе «показать ещё» и запрос разъезжаются на единицу и
# кнопка либо пропадает раньше времени, либо остаётся навсегда.
PAGE_SIZE = 50


@dataclass(frozen=True)
class VacancyFilters:
    """Разобранные параметры страницы. Один объект на страницу и на фрагмент:
    иначе они разойдутся в понимании одних и тех же параметров запроса."""

    status: str | None = None
    source: str | None = None
    include_inactive: bool = False
    offset: int = 0
    limit: int = PAGE_SIZE


@dataclass(frozen=True)
class VacancyPage:
    """Строки пачки и признак «есть ещё» — без отдельного COUNT(*)."""

    rows: list[dict]
    has_more: bool


def build_vacancy_query(profile_id: uuid.UUID, filters: VacancyFilters) -> Select:
    """Запрос списка вакансий, видимых профилю.

    Внутреннее соединение, а не внешнее: строка ProfileVacancy есть у каждой
    вакансии, которую профиль когда-либо видел (её ставит upsert_vacancies при
    первой встрече) — вакансия без такой строки этому профилю не видна.

    Все условия складываются через where() и уходят в базу. Ни одно из них не
    выполняется после выборки: ради показа PAGE_SIZE строк не должны
    приезжать все строки профиля.
    """
    query = (
        select(Vacancy, ProfileVacancy.id, ProfileVacancy.status)
        .join(ProfileVacancy, ProfileVacancy.vacancy_id == Vacancy.id)
        .where(ProfileVacancy.profile_id == profile_id)
        # Третий ключ сортировки добавляется задачей 3 — там же, где появляются
        # пачки, которым он нужен, и тест, который его требует.
        .order_by(Vacancy.posted_at.desc().nulls_last(), Vacancy.first_seen_at.desc())
    )
    if not filters.include_inactive:
        query = query.where(ProfileVacancy.is_active.is_(True))
    if filters.source:
        query = query.where(Vacancy.source == filters.source)
    if filters.status:
        query = query.where(ProfileVacancy.status == filters.status)
    return query
```

Переписать `list_vacancies` (сигнатура меняется, тело — прежнее, кроме отбора):

```python
def list_vacancies(
    session: Session, profile_id: uuid.UUID, filters: VacancyFilters
) -> VacancyPage:
    """Пачка вакансий профиля со статусом отклика и тегами.

    Запрашивается на одну строку больше, чем показывается: лишняя отвечает на
    вопрос «есть ли ещё» и заменяет отдельный COUNT(*).
    """
    query = build_vacancy_query(profile_id, filters).limit(filters.limit + 1).offset(filters.offset)
    matched = list(session.execute(query).all())
    has_more = len(matched) > filters.limit
    matched = matched[: filters.limit]

    tags_by_pair = _tags_by_pair(session, [pair_id for _, pair_id, _ in matched])

    rows = []
    for vacancy, pair_id, pair_status in matched:
        rows.append(
            {
                "id": str(vacancy.id),
                "source": vacancy.source,
                "external_id": vacancy.external_id,
                "title": vacancy.title,
                "company": vacancy.company,
                "url": vacancy.url,
                "city": vacancy.city,
                "city_any": vacancy.city_any,
                "work_format": vacancy.work_format,
                "salary_min": vacancy.salary_min,
                "salary_max": vacancy.salary_max,
                "salary_currency": vacancy.salary_currency,
                "posted_at": vacancy.posted_at,
                "status": pair_status,
                "tags": tags_by_pair.get(pair_id, []),
            }
        )
    return VacancyPage(rows=rows, has_more=has_more)
```

- [ ] **Step 4: Прогнать новый тест**

Run: `python -m uv run pytest tests/integration/test_vacancy_filters.py -q`
Expected: PASS, 3 passed.

- [ ] **Step 5: Починить старый тест списка под новую сигнатуру**

`tests/integration/test_web_vacancies.py` вызывает `list_vacancies(session, profile.id, status=...)`. Привести вызовы к новому виду: `list_vacancies(session, profile.id, VacancyFilters(status="applied")).rows`. Ожидания не трогать — они проверяют поведение, которое не менялось.

Run: `python -m uv run pytest tests/integration/test_web_vacancies.py -q`
Expected: PASS.

- [ ] **Step 6: Вынести строки в отдельный шаблон и завести фрагмент**

Создать `src/jobhunt/web/templates/_rows.html` — перенести в него содержимое цикла `{% for row in rows %}` из `vacancies.html` дословно, добавив в конец строку «показать ещё»:

```html
{% for row in rows %}
<tr id="row-{{ row.id }}">
  <td>
    <a href="{{ row.url }}" target="_blank" rel="noopener">{{ row.title }}</a>
    <div class="muted">{{ row.source }}</div>
  </td>
  <td>{{ row.company or "—" }}</td>
  <td>
    {% if row.work_format == "remote" %}Дистанційно
    {% elif row.city_any %}Вся Україна
    {% else %}{{ row.city or "—" }}{% endif %}
  </td>
  <td>
    {% if row.salary_min %}
      {{ row.salary_min }}{% if row.salary_max %}–{{ row.salary_max }}{% endif %}
      {{ row.salary_currency or "" }}
    {% else %}—{% endif %}
  </td>
  <td>{{ row.posted_at.strftime("%d.%m.%Y") if row.posted_at else "—" }}</td>
  <td>{{ row.tags | join(", ") if row.tags else "—" }}</td>
  <td>{% include "_status_cell.html" %}</td>
</tr>
{% endfor %}
```

В `vacancies.html` заменить тело `<tbody>` на `<tbody id="rows">{% include "_rows.html" %}</tbody>`.

- [ ] **Step 7: Добавить роут фрагмента**

В `src/jobhunt/web/routes/vacancies.py`:

```python
def _or_none(value: str | None) -> str | None:
    """Очищенное поле формы приходит как пустая строка, а не как отсутствие.

    Разница не косметическая: `VacancyFilters(status="")` фильтрует ровно так
    же, как `VacancyFilters()`, но НЕ РАВЕН ему, а задача 9 отличает «фильтры
    заданы» от «страница открыта как есть» именно сравнением с умолчанием.
    Без этой нормализации сброс всех фильтров формой даёт пустому списку
    объяснение «по выбранным фильтрам ничего не найдено» со ссылкой
    «сбросить» — при уже сброшенных фильтрах.
    """
    return value or None


@router.get("/vacancies/rows", response_class=HTMLResponse)
def vacancy_rows(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    status: str | None = Query(default=None),
    source: str | None = Query(default=None),
    include_inactive: bool = Query(default=False),
) -> HTMLResponse:
    """Фрагмент строк таблицы: то же, что рендерит страница внутри <tbody>.

    Отдельный роут, а не параметр страницы: htmx подменяет только строки, и
    возвращать ради этого целую страницу с <head> и формой значило бы
    перерисовывать и то, чем пользователь сейчас управляет.
    """
    profile = session.execute(select(Profile).order_by(Profile.created_at)).scalars().first()
    filters = VacancyFilters(
        status=_or_none(status), source=_or_none(source), include_inactive=include_inactive
    )
    page = (
        list_vacancies(session, profile.id, filters)
        if profile
        else VacancyPage(rows=[], has_more=False)
    )
    return TEMPLATES.TemplateResponse(
        request=request,
        name="_rows.html",
        context={"rows": page.rows, "statuses": STATUSES},
    )
```

`vacancies_page` привести к тому же построению фильтров и передать `rows=page.rows`. Каждый строковый параметр, который добавят задачи 4–6 (`city`, `work_format`, `query`), проходит через `_or_none` по той же причине.

- [ ] **Step 8: Замерить отклик и вписать число сюда**

Поднять приложение и снять 20 замеров фрагмента:

```powershell
docker compose up -d --build
$u = "http://localhost:8000/vacancies/rows"
1..20 | ForEach-Object { (Measure-Command { Invoke-WebRequest -UseBasicParsing $u }).TotalMilliseconds } |
  Measure-Object -Average -Maximum -Minimum
```

Записать результат в раздел «Замер отклика» **в конце этого файла** — заглушка там одна, второй нет.

Порог решения: если среднее ниже 100 мс, клиентская фильтрация не нужна и задачи 5–6 делаются целиком на сервере, как и запланировано. Если выше — остановиться и обсудить с владельцем, прежде чем что-то оптимизировать.

- [ ] **Step 9: Прогон и коммит**

Run: `python -m uv run pytest -q` — Expected: PASS.
Run: `python -m uv run ruff check src tests` и `ruff format src tests` — Expected: чисто.

```bash
git add src/jobhunt/web tests/integration/test_vacancy_filters.py tests/integration/test_web_vacancies.py docs/superpowers/plans/2026-08-05-vacancies-as-a-tool.md
git commit -m "feat(web): фильтрация в SQL и фрагмент строк для htmx"
```

---

### Task 3: Пачки и кнопка «показать ещё»

**Files:**
- Modify: `src/jobhunt/web/templates/_rows.html`
- Modify: `src/jobhunt/web/routes/vacancies.py`
- Create: `tests/integration/test_vacancy_paging.py`

**Interfaces:**
- Consumes: `VacancyFilters(offset, limit)`, `VacancyPage.has_more` из задачи 2.
- Produces: контекст шаблона `_rows.html` пополняется `has_more: bool`, `next_offset: int`, `query_string: str`.

- [ ] **Step 1: Написать падающие тесты пачек**

Создать `tests/integration/test_vacancy_paging.py`:

```python
from datetime import UTC, datetime

from jobhunt.db.models import Profile, ProfileVacancy, Vacancy
from jobhunt.web.data.vacancies import (
    PAGE_SIZE,
    VacancyFilters,
    build_vacancy_query,
    list_vacancies,
)

NOW = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)


def _seed(session, count: int) -> Profile:
    """count вакансий С ОДИНАКОВОЙ датой: это не редкий случай, а норма —
    площадка отдаёт дату с точностью до дня."""
    profile = Profile(name="Кирилл", collection_cities=[])
    session.add(profile)
    session.flush()
    for i in range(count):
        vacancy = Vacancy(
            source="work.ua",
            external_id=str(i),
            title=f"Роль {i}",
            url=f"https://www.work.ua/jobs/{i}/",
            description_raw="Опис",
            description_hash=f"h{i}",
            posted_at=NOW,
            first_seen_at=NOW,
            last_seen_at=NOW,
        )
        session.add(vacancy)
        session.flush()
        session.add(
            ProfileVacancy(
                profile_id=profile.id,
                vacancy_id=vacancy.id,
                first_seen_at=NOW,
                last_seen_at=NOW,
            )
        )
    session.flush()
    return profile


def test_ровно_страница_не_обещает_продолжения(session):
    profile = _seed(session, PAGE_SIZE)
    page = list_vacancies(session, profile.id, VacancyFilters())
    assert len(page.rows) == PAGE_SIZE
    assert page.has_more is False, "кнопка «показать ещё» на последней пачке не нужна"


def test_страница_с_хвостом_обещает_продолжение(session):
    profile = _seed(session, PAGE_SIZE + 1)
    page = list_vacancies(session, profile.id, VacancyFilters())
    assert len(page.rows) == PAGE_SIZE, "лишняя строка запрашивается, но не показывается"
    assert page.has_more is True


def test_порядок_задан_полностью(session):
    """У всех вакансий одинаковый posted_at, а first_seen_at ставится одной
    транзакцией — то есть первые два ключа сортировки вырождены, и порядок
    внутри группы БД не гарантирует вовсе. Проверяется сам ORDER BY, а не его
    следствие: наблюдаемый порядок на маленькой таблице может совпасть с
    верным случайно, и тогда тест был бы зелёным при любой реализации."""
    profile = _seed(session, 3)
    sql = str(build_vacancy_query(profile.id, VacancyFilters()))
    order_by = sql.split("ORDER BY", 1)[1]
    assert "vacancies.id" in order_by, (
        f"без третьего ключа OFFSET не гарантирует устойчивости пачек; ORDER BY: {order_by}"
    )


def test_пачки_не_дублируют_и_не_теряют_строки(session):
    """Следствие предыдущего теста, проверенное на данных."""
    profile = _seed(session, PAGE_SIZE + 10)
    first = list_vacancies(session, profile.id, VacancyFilters())
    second = list_vacancies(session, profile.id, VacancyFilters(offset=PAGE_SIZE))

    ids = [r["id"] for r in first.rows] + [r["id"] for r in second.rows]
    assert len(ids) == PAGE_SIZE + 10
    assert len(set(ids)) == len(ids), "строка попала в обе пачки"


def test_offset_за_пределами_выборки_даёт_пустую_пачку(session):
    profile = _seed(session, 3)
    page = list_vacancies(session, profile.id, VacancyFilters(offset=500))
    assert page.rows == []
    assert page.has_more is False
```

- [ ] **Step 2: Прогнать — обязан упасть тест порядка**

Run: `python -m uv run pytest tests/integration/test_vacancy_paging.py -q`
Expected: FAIL на `test_порядок_задан_полностью` — задача 2 оставила два ключа сортировки. Остальные три теста проходят: `limit`/`offset` появились там же. Так и задумано — пачки уже работают, не хватает только устойчивости их границ.

- [ ] **Step 3: Добавить третий ключ сортировки**

В `build_vacancy_query` заменить `order_by`:

```python
        # Третий ключ обязателен: первые два вырождены (дата у площадки с
        # точностью до дня, first_seen_at ставится одной транзакцией), а без
        # полного порядка OFFSET не гарантирует, что строка не попадёт в две
        # пачки сразу или не пропадёт из обеих.
        .order_by(Vacancy.posted_at.desc().nulls_last(), Vacancy.first_seen_at.desc(), Vacancy.id)
```

Run: `python -m uv run pytest tests/integration/test_vacancy_paging.py -q`
Expected: PASS, 5 passed.

- [ ] **Step 4: Кнопка в шаблоне**

В конец `_rows.html` дописать:

```html
{% if has_more %}
<tr id="more-row">
  <td colspan="7">
    <button type="button" class="more"
            hx-get="/vacancies/rows?{{ query_string }}&offset={{ next_offset }}"
            hx-target="#more-row" hx-swap="outerHTML">
      Показать ещё
    </button>
  </td>
</tr>
{% endif %}
```

Строка-кнопка подменяет саму себя (`outerHTML`), поэтому новая пачка встаёт на её место вместе со своей кнопкой. Адресную строку она не трогает: `offset=50` в URL означал бы, что открытая заново страница показывает вторую пачку вместо первой.

В `web/routes/vacancies.py` в обоих обработчиках собрать контекст:

```python
def _rows_context(page: VacancyPage, filters: VacancyFilters) -> dict:
    """Общий контекст строк для страницы и для фрагмента: разойтись они не
    имеют права, иначе кнопка «показать ещё» на странице и во фрагменте
    считают offset по-разному."""
    params = {
        "status": filters.status or "",
        "source": filters.source or "",
        "include_inactive": "true" if filters.include_inactive else "",
    }
    return {
        "rows": page.rows,
        "statuses": STATUSES,
        "has_more": page.has_more,
        "next_offset": filters.offset + filters.limit,
        "query_string": urlencode({k: v for k, v in params.items() if v}),
    }
```

Импорт: `from urllib.parse import urlencode`.

- [ ] **Step 5: Тест на кнопку через HTTP**

Дописать в `tests/integration/test_vacancy_paging.py`:

```python
def test_фрагмент_отдаёт_кнопку_только_когда_есть_продолжение(client, session):
    profile = _seed(session, PAGE_SIZE + 1)
    session.commit()

    body = client.get("/vacancies/rows").text
    assert 'id="more-row"' in body
    assert f"offset={PAGE_SIZE}" in body

    tail = client.get(f"/vacancies/rows?offset={PAGE_SIZE}").text
    assert 'id="more-row"' not in tail, "на последней пачке кнопки быть не должно"
```

Фикстура `client` — как в `tests/integration/test_web_vacancies.py` (TestClient с `app.dependency_overrides[get_session]`). Скопировать её оттуда в этот файл, если общей фикстуры в `conftest.py` нет.

- [ ] **Step 6: Прогон и коммит**

Run: `python -m uv run pytest -q` — Expected: PASS.

```bash
git add src/jobhunt/web tests/integration/test_vacancy_paging.py
git commit -m "feat(web): пачки по 50 строк и кнопка «показать ещё»"
```

---

### Task 4: Три состояния тега и переключатели видимости

Закрывает таблицу §5.2 спеки: по умолчанию видны только вакансии живых тегов.

**Files:**
- Modify: `src/jobhunt/web/data/vacancies.py`
- Modify: `src/jobhunt/web/routes/vacancies.py`
- Modify: `src/jobhunt/web/templates/_filters.html` (создаётся здесь же)
- Modify: `tests/integration/test_vacancy_filters.py`

**Interfaces:**
- Consumes: `VacancyFilters` из задачи 2.
- Produces: поля `include_disabled_tags: bool`, `include_untagged: bool` в `VacancyFilters`.

- [ ] **Step 1: Написать падающие тесты на все пять сочетаний**

Дописать в `tests/integration/test_vacancy_filters.py`:

```python
from jobhunt.db.models import ProfileTag, ProfileVacancyTag


def _tagged(session, profile, external_id: str, *, enabled: bool | None) -> str:
    """Пара с тегом (enabled=True/False) или вовсе без связки (enabled=None —
    сирота: тег удалили, связки ушли каскадом)."""
    vacancy = _vacancy(session, external_id)
    pair = _pair(session, profile, vacancy)
    if enabled is not None:
        tag = ProfileTag(profile_id=profile.id, text=f"тег-{external_id}", is_enabled=enabled)
        session.add(tag)
        session.flush()
        session.add(ProfileVacancyTag(profile_vacancy_id=pair.id, tag_id=tag.id))
        session.flush()
    return external_id


def _visible(session, profile, filters) -> list[str]:
    return sorted(row["external_id"] for row in list_vacancies(session, profile.id, filters).rows)


def test_по_умолчанию_видны_только_вакансии_включённых_тегов(session):
    profile = _profile(session)
    _tagged(session, profile, "live", enabled=True)
    _tagged(session, profile, "off", enabled=False)
    _tagged(session, profile, "orphan", enabled=None)

    assert _visible(session, profile, VacancyFilters()) == ["live"]


def test_переключатель_показывает_вакансии_выключенных_тегов(session):
    profile = _profile(session)
    _tagged(session, profile, "live", enabled=True)
    _tagged(session, profile, "off", enabled=False)
    _tagged(session, profile, "orphan", enabled=None)

    assert _visible(session, profile, VacancyFilters(include_disabled_tags=True)) == ["live", "off"]


def test_переключатель_показывает_сирот(session):
    """Сирота не деактивируется никогда: mark_missing судит только пары,
    связанные с отработавшим тегом. Без этого переключателя она исчезает из
    списка навсегда, а работа по ней уже сделана."""
    profile = _profile(session)
    _tagged(session, profile, "live", enabled=True)
    _tagged(session, profile, "off", enabled=False)
    _tagged(session, profile, "orphan", enabled=None)

    assert _visible(session, profile, VacancyFilters(include_untagged=True)) == ["live", "orphan"]


def test_оба_переключателя_снимают_условие_по_тегам(session):
    profile = _profile(session)
    _tagged(session, profile, "live", enabled=True)
    _tagged(session, profile, "off", enabled=False)
    _tagged(session, profile, "orphan", enabled=None)

    filters = VacancyFilters(include_disabled_tags=True, include_untagged=True)
    assert _visible(session, profile, filters) == ["live", "off", "orphan"]
```

- [ ] **Step 2: Прогнать — обязаны упасть**

Run: `python -m uv run pytest tests/integration/test_vacancy_filters.py -q -k тег`
Expected: FAIL — `VacancyFilters` не знает `include_disabled_tags`.

- [ ] **Step 3: Реализовать условия по тегам**

В `web/data/vacancies.py` добавить поля в `VacancyFilters`:

```python
    include_disabled_tags: bool = False
    include_untagged: bool = False
```

и в `build_vacancy_query` перед `return`:

```python
    # Три состояния пары различаются одним и тем же EXISTS с разным условием
    # на is_enabled (спека, раздел 5.2). Комбинации сведены к трём случаям:
    # оба флага сняты — условия по тегам нет вовсе; только выключенные —
    # достаточно любой связки; только сироты — либо живой тег, либо связок нет.
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
    if filters.include_disabled_tags and filters.include_untagged:
        pass
    elif filters.include_disabled_tags:
        query = query.where(any_link)
    elif filters.include_untagged:
        query = query.where(or_(enabled_link, ~any_link))
    else:
        query = query.where(enabled_link)
```

Импорт: `from sqlalchemy import Select, or_, select`.

- [ ] **Step 4: Прогнать**

Run: `python -m uv run pytest tests/integration/test_vacancy_filters.py -q`
Expected: PASS.

- [ ] **Step 5: Перенести форму фильтров в отдельный шаблон и добавить два переключателя**

Создать `src/jobhunt/web/templates/_filters.html`, перенести туда `<form class="filters">` из `vacancies.html` и дописать две галочки, а всю форму перевести на htmx:

```html
<form class="filters" id="filters"
      hx-get="/vacancies/rows" hx-include=".chips"
      hx-target="#rows" hx-swap="innerHTML"
      hx-trigger="change" hx-push-url="true">
  <label>Статус
    <select name="status">
      <option value="">все</option>
      {% for s in statuses %}
        <option value="{{ s }}" {% if s == current.status %}selected{% endif %}>{{ s }}</option>
      {% endfor %}
    </select>
  </label>
  <label>Источник
    <select name="source">
      <option value="">все</option>
      {% for src in sources %}
        <option value="{{ src }}" {% if src == current.source %}selected{% endif %}>{{ src }}</option>
      {% endfor %}
    </select>
  </label>
  <label><input type="checkbox" name="include_inactive" value="true"
         {% if current.include_inactive %}checked{% endif %}> показывать неактивные</label>
  <label><input type="checkbox" name="include_disabled_tags" value="true"
         {% if current.include_disabled_tags %}checked{% endif %}> вакансии выключенных тегов</label>
  <label><input type="checkbox" name="include_untagged" value="true"
         {% if current.include_untagged %}checked{% endif %}> найденные ранее</label>
</form>
```

`hx-include=".chips"` у формы обязателен, хотя чипы появляются только задачей 5: без него смена любого фильтра отправляет запрос без выбранных тегов и молча сбрасывает выбор — чипы лежат **вне** формы, и сами по себе в её запрос не попадают. Пока чипов нет, селектор не находит ничего и ни на что не влияет.

В `vacancies.html` заменить прежнюю форму на `{% include "_filters.html" %}`. В контекст обоих обработчиков добавить `current: VacancyFilters` и `sources: ["work.ua", "dou.ua"]` (в задаче 6 список источников станет вычисляемым).

Роут `vacancy_rows` и `vacancies_page` получают два новых `Query`-параметра `include_disabled_tags: bool = Query(default=False)` и `include_untagged: bool = Query(default=False)` и кладут их в `VacancyFilters`; `_rows_context` дополняется ими в `params`.

- [ ] **Step 6: Прогон и коммит**

Run: `python -m uv run pytest -q` — Expected: PASS.

```bash
git add src/jobhunt/web tests/integration/test_vacancy_filters.py
git commit -m "feat(web): состав списка по тегам и два переключателя видимости"
```

---

### Task 5: Чипы тегов — фильтр показа

**Files:**
- Create: `src/jobhunt/web/data/tags.py`
- Create: `src/jobhunt/web/templates/_tag_chips.html`
- Modify: `src/jobhunt/web/data/vacancies.py`, `src/jobhunt/web/routes/vacancies.py`, `src/jobhunt/web/templates/vacancies.html`
- Create: `tests/integration/test_web_tags.py`

**Interfaces:**
- Consumes: `VacancyFilters` из задач 2 и 4.
- Produces: `VacancyFilters.tag_ids: tuple[uuid.UUID, ...]`; `jobhunt.web.data.tags.list_tags(session, profile_id) -> list[dict]` с ключами `id: str`, `text: str`, `is_enabled: bool`.

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_web_tags.py` (хелперы `_profile`, `_vacancy`, `_pair` скопировать из `test_vacancy_filters.py` — общего conftest для них нет):

```python
def test_чип_показывает_вакансии_только_выбранного_тега(session):
    profile = _profile(session)
    a = _tag(session, profile, "Head of IT", enabled=True)
    b = _tag(session, profile, "IT Director", enabled=True)
    _link(session, profile, _vacancy(session, "1"), a)
    _link(session, profile, _vacancy(session, "2"), b)

    page = list_vacancies(session, profile.id, VacancyFilters(tag_ids=(a.id,)))

    assert [row["external_id"] for row in page.rows] == ["1"]


def test_несколько_чипов_складываются_по_или(session):
    profile = _profile(session)
    a = _tag(session, profile, "Head of IT", enabled=True)
    b = _tag(session, profile, "IT Director", enabled=True)
    _link(session, profile, _vacancy(session, "1"), a)
    _link(session, profile, _vacancy(session, "2"), b)
    _link(session, profile, _vacancy(session, "3"), None)

    page = list_vacancies(session, profile.id, VacancyFilters(tag_ids=(a.id, b.id)))

    assert sorted(row["external_id"] for row in page.rows) == ["1", "2"]


def test_чип_выключенного_тега_показывает_его_вакансии(session):
    """Выбор чипа — прямое «покажи это». Если бы условие по включённости
    продолжало действовать, чип выключенного тега давал бы пустой список:
    формально верно, по смыслу абсурд."""
    profile = _profile(session)
    off = _tag(session, profile, "менеджер", enabled=False)
    _link(session, profile, _vacancy(session, "1"), off)

    page = list_vacancies(session, profile.id, VacancyFilters(tag_ids=(off.id,)))

    assert [row["external_id"] for row in page.rows] == ["1"]


def test_список_тегов_отдаёт_и_выключенные(session):
    profile = _profile(session)
    _tag(session, profile, "Head of IT", enabled=True)
    _tag(session, profile, "менеджер", enabled=False)

    tags = list_tags(session, profile.id)

    assert [(t["text"], t["is_enabled"]) for t in tags] == [
        ("Head of IT", True),
        ("менеджер", False),
    ]
```

Хелперы:

```python
def _tag(session, profile, text: str, *, enabled: bool) -> ProfileTag:
    tag = ProfileTag(profile_id=profile.id, text=text, is_enabled=enabled)
    session.add(tag)
    session.flush()
    return tag


def _link(session, profile, vacancy, tag) -> None:
    pair = _pair(session, profile, vacancy)
    if tag is not None:
        session.add(ProfileVacancyTag(profile_vacancy_id=pair.id, tag_id=tag.id))
    session.flush()
```

- [ ] **Step 2: Прогнать — обязаны упасть**

Run: `python -m uv run pytest tests/integration/test_web_tags.py -q`
Expected: FAIL — нет `tag_ids` и нет модуля `jobhunt.web.data.tags`.

- [ ] **Step 3: Реализовать**

В `VacancyFilters` добавить `tag_ids: tuple[uuid.UUID, ...] = ()`.

В `build_vacancy_query` — **перед** блоком трёх состояний, и так, чтобы выбранные чипы этот блок заменяли:

```python
    if filters.tag_ids:
        # Выбранные чипы — прямое «покажи это»: условие по включённости тега
        # ниже не применяется вовсе (спека, раздел 4.3), иначе чип
        # выключенного тега давал бы заведомо пустой список.
        chosen_link = (
            select(1)
            .select_from(ProfileVacancyTag)
            .where(
                ProfileVacancyTag.profile_vacancy_id == ProfileVacancy.id,
                ProfileVacancyTag.tag_id.in_(filters.tag_ids),
            )
            .exists()
        )
        return query.where(chosen_link)
```

Создать `src/jobhunt/web/data/tags.py`:

```python
"""Теги профиля для веб-слоя: чипы фильтра и панель управления сбором."""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import ProfileTag


def list_tags(session: Session, profile_id: uuid.UUID) -> list[dict]:
    """Все теги профиля, включая выключенные, в порядке создания.

    Выключенные нужны и чипам, и панели: спрятать их значило бы спрятать
    единственный способ снова включить тег.
    """
    rows = session.execute(
        select(ProfileTag)
        .where(ProfileTag.profile_id == profile_id)
        .order_by(ProfileTag.created_at, ProfileTag.id)
    ).scalars()
    return [{"id": str(tag.id), "text": tag.text, "is_enabled": tag.is_enabled} for tag in rows]
```

Создать `src/jobhunt/web/templates/_tag_chips.html`:

```html
{% if tags %}
<div class="chips">
  {% for tag in tags %}
    <label class="chip {% if not tag.is_enabled %}chip-off{% endif %}">
      <input type="checkbox" name="tag" value="{{ tag.id }}"
             {% if tag.id in selected_tag_ids %}checked{% endif %}
             hx-get="/vacancies/rows" hx-include="#filters, .chips"
             hx-target="#rows" hx-swap="innerHTML" hx-push-url="true">
      {{ tag.text }}{% if not tag.is_enabled %} (выключен){% endif %}
    </label>
  {% endfor %}
</div>
{% endif %}
```

`selected_tag_ids` — отдельный ключ контекста со **строками**: `VacancyFilters.tag_ids` хранит `uuid.UUID`, а `tag.id` в шаблоне — строка, и прямое сравнение молча давало бы «ни один чип не выбран».

В `vacancies.html` вставить `{% include "_tag_chips.html" %}` между фильтрами и таблицей.

В обоих роутах принять повторяющийся параметр, разобрать его и положить в контекст:

```python
    tag: Annotated[list[str] | None, Query()] = None,
    ...
    # Невалидный UUID приходит из адресной строки, то есть от пользователя, и
    # обязан давать 400, а не 500.
    try:
        tag_ids = tuple(uuid.UUID(value) for value in (tag or []))
    except ValueError:
        raise HTTPException(status_code=400, detail="некорректный идентификатор тега") from None
    ...
    context["tags"] = list_tags(session, profile.id)
    context["selected_tag_ids"] = [str(value) for value in tag_ids]
```

Импорты: `from fastapi import HTTPException`, `from jobhunt.web.data.tags import list_tags`.

В `_rows_context` добавить чипы в `params`, чтобы кнопка «показать ещё» их не теряла:

```python
    params_multi = [("tag", str(value)) for value in filters.tag_ids]
    ...
    "query_string": urlencode([*((k, v) for k, v in params.items() if v), *params_multi]),
```

- [ ] **Step 4: Прогнать и добавить тест на невалидный UUID**

```python
def test_некорректный_тег_в_адресе_даёт_400(client, session):
    _profile(session)
    session.commit()
    assert client.get("/vacancies/rows?tag=не-uuid").status_code == 400
```

Run: `python -m uv run pytest tests/integration/test_web_tags.py -q`
Expected: PASS, 5 passed.

- [ ] **Step 5: Коммит**

```bash
git add src/jobhunt/web tests/integration/test_web_tags.py
git commit -m "feat(web): чипы тегов как фильтр показа"
```

---

### Task 6: Остальные фильтры и значения списков из данных

**Files:**
- Modify: `src/jobhunt/web/data/vacancies.py`, `src/jobhunt/web/routes/vacancies.py`, `src/jobhunt/web/templates/_filters.html`
- Modify: `tests/integration/test_vacancy_filters.py`

**Interfaces:**
- Consumes: `VacancyFilters` из задач 2, 4, 5.
- Produces: поля `city: str | None`, `work_format: str | None` (`"remote"` | `"onsite"` | `"any_city"`), `with_salary: bool`, `query: str | None`; функция `filter_values(session, profile_id) -> dict` с ключами `cities: list[str]`, `sources: list[str]`.

- [ ] **Step 1: Написать падающие тесты**

Дописать в `tests/integration/test_vacancy_filters.py`:

```python
def test_фильтр_по_городу(session):
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1", city="Київ"))
    _pair(session, profile, _vacancy(session, "2", city="Львів"))

    assert _visible(session, profile, VacancyFilters(city="Львів")) == ["2"]


def test_фильтр_формата_работы_различает_три_случая(session):
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "office", city="Київ", work_format="onsite"))
    _pair(session, profile, _vacancy(session, "remote", city=None, work_format="remote"))
    _pair(
        session,
        profile,
        _vacancy(session, "any", city=None, city_any=True, work_format="onsite"),
    )

    assert _visible(session, profile, VacancyFilters(work_format="remote")) == ["remote"]
    assert _visible(session, profile, VacancyFilters(work_format="any_city")) == ["any"]
    assert _visible(session, profile, VacancyFilters(work_format="onsite")) == ["office"], (
        "«вся Україна» — не офис в конкретном городе и в этот фильтр попадать не должна"
    )


def test_фильтр_только_с_зарплатой(session):
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1", salary_min=50000, salary_currency="UAH"))
    _pair(session, profile, _vacancy(session, "2"))

    assert _visible(session, profile, VacancyFilters(with_salary=True)) == ["1"]


def test_поиск_по_заголовку_и_компании_без_учёта_регистра(session):
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1", title="Head of IT", company="Garvis"))
    _pair(session, profile, _vacancy(session, "2", title="Бухгалтер", company="ІТ-Консалт"))

    assert _visible(session, profile, VacancyFilters(query="head")) == ["1"]
    assert _visible(session, profile, VacancyFilters(query="консалт")) == ["2"]


def test_поиск_не_ломается_на_символах_шаблона(session):
    """'%' и '_' в ILIKE — метасимволы. Без экранирования запрос «100%»
    превращался бы в «покажи всё»."""
    profile = _profile(session)
    _pair(session, profile, _vacancy(session, "1", title="Знание Excel 100%"))
    _pair(session, profile, _vacancy(session, "2", title="Бухгалтер"))

    assert _visible(session, profile, VacancyFilters(query="100%")) == ["1"]


def test_значения_фильтров_берутся_из_данных_профиля(session):
    profile = _profile(session)
    other = _profile(session, name="Второй")
    _pair(session, profile, _vacancy(session, "1", city="Київ", source="work.ua"))
    _pair(session, profile, _vacancy(session, "2", city="Дніпро", source="dou.ua"))
    _pair(session, other, _vacancy(session, "3", city="Одеса", source="work.ua"))

    values = filter_values(session, profile.id)

    assert values["cities"] == ["Дніпро", "Київ"]
    assert values["sources"] == ["dou.ua", "work.ua"]
    assert "Одеса" not in values["cities"], "город чужого профиля в списке не нужен"
```

- [ ] **Step 2: Прогнать — обязаны упасть**

Run: `python -m uv run pytest tests/integration/test_vacancy_filters.py -q -k "город or формат or зарплат or поиск or значения"`
Expected: FAIL.

- [ ] **Step 3: Реализовать**

В `VacancyFilters` добавить:

```python
    city: str | None = None
    work_format: str | None = None
    with_salary: bool = False
    query: str | None = None
```

В `build_vacancy_query` дописать перед блоком тегов:

```python
    if filters.city:
        query = query.where(Vacancy.city == filters.city)
    if filters.work_format == "remote":
        query = query.where(Vacancy.work_format == "remote")
    elif filters.work_format == "any_city":
        query = query.where(Vacancy.city_any.is_(True))
    elif filters.work_format == "onsite":
        # «Вся Україна» — не офис в конкретном городе: у неё city_any=True при
        # work_format='onsite', и в фильтр «офис» она попадать не должна.
        query = query.where(Vacancy.work_format == "onsite", Vacancy.city_any.is_(False))
    if filters.with_salary:
        query = query.where(Vacancy.salary_min.isnot(None))
    if filters.query:
        # % и _ — метасимволы ILIKE: без экранирования запрос «100%» стал бы
        # «покажи всё», а «_» — «любой символ».
        escaped = filters.query.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
        pattern = f"%{escaped}%"
        query = query.where(
            or_(
                Vacancy.title.ilike(pattern, escape="\\"),
                Vacancy.company.ilike(pattern, escape="\\"),
            )
        )
```

Добавить функцию:

```python
def filter_values(session: Session, profile_id: uuid.UUID) -> dict:
    """Значения выпадающих списков — из данных этого профиля.

    Список городов, половина пунктов которого ничего не находит, хуже
    короткого; и город чужого профиля в нём не нужен вовсе.
    """
    rows = session.execute(
        select(Vacancy.city, Vacancy.source)
        .join(ProfileVacancy, ProfileVacancy.vacancy_id == Vacancy.id)
        .where(ProfileVacancy.profile_id == profile_id)
        .distinct()
    ).all()
    return {
        "cities": sorted({city for city, _ in rows if city}),
        "sources": sorted({source for _, source in rows if source}),
    }
```

- [ ] **Step 4: Прогнать**

Run: `python -m uv run pytest tests/integration/test_vacancy_filters.py -q`
Expected: PASS.

- [ ] **Step 5: Довести форму**

В `_filters.html` добавить город, формат работы, галочку зарплаты и поиск:

```html
  <label>Город
    <select name="city">
      <option value="">все</option>
      {% for city in cities %}
        <option value="{{ city }}" {% if city == current.city %}selected{% endif %}>{{ city }}</option>
      {% endfor %}
    </select>
  </label>
  <label>Формат
    <select name="work_format">
      <option value="">любой</option>
      <option value="onsite" {% if current.work_format == 'onsite' %}selected{% endif %}>офис</option>
      <option value="remote" {% if current.work_format == 'remote' %}selected{% endif %}>удалённо</option>
      <option value="any_city" {% if current.work_format == 'any_city' %}selected{% endif %}>вся Україна</option>
    </select>
  </label>
  <label><input type="checkbox" name="with_salary" value="true"
         {% if current.with_salary %}checked{% endif %}> только с зарплатой</label>
  <label>Поиск
    <input type="search" name="query" value="{{ current.query or '' }}"
           hx-get="/vacancies/rows" hx-include="#filters, .chips"
           hx-target="#rows" hx-swap="innerHTML" hx-push-url="true"
           hx-trigger="keyup changed delay:250ms, search">
  </label>
```

Поле поиска несёт собственный `hx-trigger` с задержкой: без неё запрос уходил бы на каждую букву. Остальные элементы формы работают от `hx-trigger="change"` самой формы.

Роуты принимают новые `Query`-параметры, кладут их в `VacancyFilters`, добавляют в контекст `cities` и `sources` из `filter_values(...)` и дополняют `params` в `_rows_context`.

- [ ] **Step 6: Прогон и коммит**

Run: `python -m uv run pytest -q` — Expected: PASS.

```bash
git add src/jobhunt/web tests/integration/test_vacancy_filters.py
git commit -m "feat(web): фильтры по городу, формату, зарплате и тексту"
```

---

### Task 7: Переключатель «искать по этому тегу»

Меняет `is_enabled` в БД — в отличие от чипов, влияет на следующий сбор.

**Files:**
- Create: `src/jobhunt/web/routes/tags.py`
- Create: `src/jobhunt/web/templates/_tags_panel.html`
- Modify: `src/jobhunt/web/data/tags.py`, `src/jobhunt/web/app.py`, `src/jobhunt/web/templates/vacancies.html`
- Modify: `tests/integration/test_web_tags.py`

**Interfaces:**
- Consumes: `list_tags` из задачи 5.
- Produces: `set_tag_enabled(session, profile_id, tag_id, enabled) -> bool` (False — тега у профиля нет); роут `POST /tags/{tag_id}/enabled`.

- [ ] **Step 1: Написать падающие тесты**

```python
def test_переключатель_меняет_is_enabled(session):
    profile = _profile(session)
    tag = _tag(session, profile, "менеджер", enabled=True)

    assert set_tag_enabled(session, profile.id, tag.id, False) is True
    session.flush()
    session.refresh(tag)
    assert tag.is_enabled is False


def test_переключатель_чужого_тега_отказывает(session):
    """Тег адресуется идентификатором из адреса запроса. Без проверки
    принадлежности профилю можно было бы выключить тег другого профиля."""
    profile = _profile(session)
    other = _profile(session, name="Второй")
    tag = _tag(session, other, "менеджер", enabled=True)

    assert set_tag_enabled(session, profile.id, tag.id, False) is False
    session.flush()
    session.refresh(tag)
    assert tag.is_enabled is True


def test_роут_переключателя_возвращает_обновлённую_панель(client, session):
    profile = _profile(session)
    tag = _tag(session, profile, "менеджер", enabled=True)
    session.commit()

    response = client.post(f"/tags/{tag.id}/enabled", data={"enabled": "false"})

    assert response.status_code == 200
    assert "менеджер" in response.text
    assert "следующий сбор" in response.text, "последствие переключения обязано быть на экране"


def test_роут_переключателя_неизвестного_тега_даёт_404(client, session):
    _profile(session)
    session.commit()
    response = client.post(
        "/tags/00000000-0000-4000-8000-000000000000/enabled", data={"enabled": "false"}
    )
    assert response.status_code == 404
```

- [ ] **Step 2: Прогнать — обязаны упасть**

Run: `python -m uv run pytest tests/integration/test_web_tags.py -q -k переключател`
Expected: FAIL — нет `set_tag_enabled`.

- [ ] **Step 3: Реализовать данные**

В `src/jobhunt/web/data/tags.py`:

```python
def set_tag_enabled(
    session: Session, profile_id: uuid.UUID, tag_id: uuid.UUID, enabled: bool
) -> bool:
    """Включить или выключить тег профиля. False — такого тега у профиля нет.

    Принадлежность профилю проверяется здесь, а не в роуте: идентификатор
    приходит из адреса запроса, и без проверки можно было бы выключить тег
    другого профиля.
    """
    tag = session.execute(
        select(ProfileTag).where(ProfileTag.id == tag_id, ProfileTag.profile_id == profile_id)
    ).scalar_one_or_none()
    if tag is None:
        return False
    tag.is_enabled = enabled
    session.flush()
    return True
```

- [ ] **Step 4: Реализовать роут и панель**

Создать `src/jobhunt/web/routes/tags.py`. Свой `Jinja2Templates` здесь **не создаётся** — окружение шаблонов общее и живёт в `src/jobhunt/web/templating.py` (заведено при правке замера задачи 2, с выключенным `auto_reload`). Второй экземпляр уронит границу `tests/unit/test_web_templating_boundary.py`, и правильно уронит: он вернул бы `auto_reload=True` для панели тегов.

```python
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from jobhunt.web.data.profiles import earliest_profile
from jobhunt.web.data.tags import list_tags, set_tag_enabled
from jobhunt.web.deps import get_session
from jobhunt.web.templating import TEMPLATES

router = APIRouter()


@router.post("/tags/{tag_id}/enabled", response_class=HTMLResponse)
def toggle_tag(
    request: Request,
    tag_id: uuid.UUID,
    session: Annotated[Session, Depends(get_session)],
    enabled: str = Form(...),
) -> HTMLResponse:
    """Включить или выключить тег и вернуть обновлённую панель тегов.

    Таблица вакансий в ответ НЕ перерисовывается: переключатель влияет на
    следующий сбор, а не на текущий список (спека, раздел 4.3). Перерисовка
    создавала бы впечатление, что список уже пересобран.
    """
    profile = earliest_profile(session)
    if profile is None:
        raise HTTPException(status_code=400, detail="профиль не создан")
    if not set_tag_enabled(session, profile.id, tag_id, enabled == "true"):
        raise HTTPException(status_code=404, detail="тег не найден у этого профиля")
    return TEMPLATES.TemplateResponse(
        request=request,
        name="_tags_panel.html",
        context={"tags": list_tags(session, profile.id)},
    )
```

Здесь же создать `src/jobhunt/web/data/profiles.py` с единственной функцией — тем же выбором профиля, что сейчас зашит в роутах вакансий:

```python
"""Выбор профиля для веб-слоя."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import Profile


def earliest_profile(session: Session) -> Profile | None:
    """Самый ранний профиль — текущее поведение всех веб-роутов.

    Задача 8 добавит рядом выбор из адреса и из cookie; эта функция останется
    последним звеном разрешения.
    """
    return session.execute(select(Profile).order_by(Profile.created_at)).scalars().first()
```

Роуты вакансий из задач 2–6 тоже перевести на неё: прямых `select(Profile)` в `routes/` не остаётся совсем. **Решение принято — исключение границы снимается здесь, а не в задаче 8.** В этой же задаче удалить из `tests/unit/test_web_boundary.py` константу `ALLOWED_UNTIL_TASK_7` (так она названа в коде — переименована при исправлении находки ревью задачи 1), вернув тело `test_роуты_не_обращаются_к_бд` к строгому виду из шага 4 задачи 1. Вместе с ней уходят функция `unexpected`, тест `test_счётчик_ловит_новую_копию_уже_известного_нарушения` (он проверяет исключение, которого больше нет) и абзац про временное исключение в докстринге файла. Шаг 5 задачи 8 после этого — проверка, а не правка.

Создать `src/jobhunt/web/templates/_tags_panel.html`:

```html
<div class="tags-panel" id="tags-panel">
  <h2>Теги</h2>
  <p class="muted">Переключатель влияет на следующий сбор, а не на список ниже.</p>
  {% for tag in tags %}
    <label class="tag-row">
      <input type="checkbox" name="enabled" value="true"
             {% if tag.is_enabled %}checked{% endif %}
             hx-post="/tags/{{ tag.id }}/enabled"
             hx-vals='{"enabled": "{{ "false" if tag.is_enabled else "true" }}"}'
             hx-target="#tags-panel" hx-swap="outerHTML">
      {{ tag.text }} — {% if tag.is_enabled %}ищется{% else %}не ищется{% endif %}
    </label>
  {% else %}
    <p class="empty">Тегов нет. Добавьте: <code>jobhunt tag add --profile "Имя" --text "Роль"</code></p>
  {% endfor %}
</div>
```

Подключить роутер в `web/app.py`: `from jobhunt.web.routes import tags` и `app.include_router(tags.router)`.

В `vacancies.html` вставить `{% include "_tags_panel.html" %}` после чипов.

- [ ] **Step 5: Прогнать**

Run: `python -m uv run pytest tests/integration/test_web_tags.py -q`
Expected: PASS.

- [ ] **Step 6: Коммит**

```bash
git add src/jobhunt/web tests/integration/test_web_tags.py
git commit -m "feat(web): переключатель «искать по этому тегу»"
```

---

### Task 8: Выбор профиля

**Files:**
- Modify: `src/jobhunt/web/data/profiles.py`, `src/jobhunt/web/routes/vacancies.py`, `src/jobhunt/web/routes/tags.py`, `src/jobhunt/web/templates/vacancies.html`
- Modify: `tests/unit/test_web_boundary.py` (снять временное исключение)
- Create: `tests/integration/test_web_profiles.py`

**Interfaces:**
- Consumes: ничего нового.
- Produces: `list_profiles(session) -> list[dict]`, `resolve_profile(session, requested_id, remembered_id) -> Profile | None`, `PROFILE_COOKIE = "jobhunt-profile"`.

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_web_profiles.py`:

```python
def test_профиль_из_адреса_имеет_приоритет(session):
    first = _profile(session, name="Первый")
    second = _profile(session, name="Второй")

    chosen = resolve_profile(session, requested_id=second.id, remembered_id=first.id)

    assert chosen.id == second.id


def test_без_адреса_берётся_запомненный(session):
    first = _profile(session, name="Первый")
    second = _profile(session, name="Второй")

    chosen = resolve_profile(session, requested_id=None, remembered_id=second.id)

    assert chosen.id == second.id


def test_без_адреса_и_памяти_берётся_самый_ранний(session):
    first = _profile(session, name="Первый")
    _profile(session, name="Второй")

    chosen = resolve_profile(session, requested_id=None, remembered_id=None)

    assert chosen.id == first.id


def test_несуществующий_профиль_не_подменяется_молча(session):
    """Молчаливый показ чужого списка — худший исход: пользователь работает
    не с тем профилем и не может этого заметить."""
    _profile(session, name="Первый")

    assert resolve_profile(session, requested_id=uuid.uuid4(), remembered_id=None) is None


def test_забытый_профиль_не_ломает_страницу(session):
    """Профиль из cookie мог быть удалён между заходами. Это не ошибка
    пользователя — просто память устарела, и берётся самый ранний."""
    first = _profile(session, name="Первый")

    chosen = resolve_profile(session, requested_id=None, remembered_id=uuid.uuid4())

    assert chosen.id == first.id


def test_страница_запоминает_выбор_в_cookie(client, session):
    _profile(session, name="Первый")
    second = _profile(session, name="Второй")
    session.commit()

    response = client.get(f"/vacancies?profile={second.id}")

    assert response.status_code == 200
    assert response.cookies.get("jobhunt-profile") == str(second.id)


def test_страница_с_несуществующим_профилем_объясняется(client, session):
    _profile(session, name="Первый")
    session.commit()

    response = client.get(f"/vacancies?profile={uuid.uuid4()}")

    assert response.status_code == 404
    assert "профиль" in response.text.lower()
```

- [ ] **Step 2: Прогнать — обязаны упасть**

Run: `python -m uv run pytest tests/integration/test_web_profiles.py -q`
Expected: FAIL — нет `resolve_profile`.

- [ ] **Step 3: Реализовать разрешение профиля**

`src/jobhunt/web/data/profiles.py`:

```python
"""Выбор профиля для веб-слоя."""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import Profile

PROFILE_COOKIE = "jobhunt-profile"


def list_profiles(session: Session) -> list[dict]:
    rows = session.execute(select(Profile).order_by(Profile.created_at, Profile.id)).scalars()
    return [{"id": str(p.id), "name": p.name} for p in rows]


def resolve_profile(
    session: Session, requested_id: uuid.UUID | None, remembered_id: uuid.UUID | None
) -> Profile | None:
    """Профиль страницы: из адреса, затем из cookie, затем самый ранний.

    Разные исходы для двух похожих случаев. Профиль, названный в АДРЕСЕ и не
    найденный, — это None: пользователь пришёл по конкретной ссылке, и
    молчаливая подмена другим профилем означала бы работу не с теми данными
    без единого признака этого. Профиль из COOKIE, который не нашёлся, —
    просто устаревшая память (профиль удалили между заходами), и она молча
    уступает самому раннему.
    """
    if requested_id is not None:
        return session.get(Profile, requested_id)
    if remembered_id is not None:
        remembered = session.get(Profile, remembered_id)
        if remembered is not None:
            return remembered
    return session.execute(select(Profile).order_by(Profile.created_at)).scalars().first()
```

- [ ] **Step 4: Подключить к роутам**

В `vacancies_page` и `vacancy_rows`: читать `profile` из `Query`, `remembered` из `request.cookies.get(PROFILE_COOKIE)`, вызывать `resolve_profile`. При `None` и непустом `profile` — вернуть страницу с сообщением и кодом 404:

```python
    if requested_id is not None and profile is None:
        # Контекст полный, а не из четырёх ключей: к этой задаче vacancies.html
        # включает фильтры, чипы, панель тегов и селектор профиля, а
        # `{% if profiles | length > 1 %}` на неопределённом `profiles` роняет
        # рендер — вместо 404 пользователь получил бы 500.
        return TEMPLATES.TemplateResponse(
            request=request,
            name="vacancies.html",
            context={
                "rows": [],
                "statuses": STATUSES,
                "has_more": False,
                "next_offset": 0,
                "query_string": "",
                "current": VacancyFilters(),
                "tags": [],
                "selected_tag_ids": [],
                "cities": [],
                "sources": [],
                "profiles": list_profiles(session),
                "current_profile_id": None,
                "empty_reason": None,
                "profile_error": "Профиль не найден — возможно, он был удалён. "
                                 "Выберите профиль заново.",
            },
            status_code=404,
        )
```

После успешного рендера страницы поставить cookie:

```python
    response = TEMPLATES.TemplateResponse(...)
    response.set_cookie(PROFILE_COOKIE, str(profile.id), max_age=60 * 60 * 24 * 365, samesite="lax")
    return response
```

В `vacancies.html` добавить селектор, показываемый только при нескольких профилях:

```html
{% if profiles | length > 1 %}
<form class="profile-picker" method="get" action="/vacancies">
  <label>Профиль
    <select name="profile" onchange="this.form.submit()">
      {% for p in profiles %}
        <option value="{{ p.id }}" {% if p.id == current_profile_id %}selected{% endif %}>{{ p.name }}</option>
      {% endfor %}
    </select>
  </label>
</form>
{% endif %}
```

Смена профиля меняет всё на странице (чипы, панель тегов, значения фильтров), поэтому здесь обычная перезагрузка, а не htmx-фрагмент.

`routes/tags.py` переводится с `earliest_profile` на `resolve_profile` с теми же двумя источниками.

- [ ] **Step 5: Проверить, что граница осталась строгой**

Исключение `ALLOWED_UNTIL_TASK_7` снято задачей 7 — правок здесь нет, есть проверка, что задача 8 не вернула запрос в роуты.

Run: `python -m uv run pytest tests/unit/test_web_boundary.py -q`
Expected: PASS — в роутах не осталось ни одного `select(`. Если тест упал, `resolve_profile` подключён не через `web/data`, а прямым запросом.

Убедиться также, что `earliest_profile` из задачи 7 удалена вместе с её импортом в `routes/tags.py`: этот шаг переводит tags.py на `resolve_profile`, и оставленная функция станет мёртвым кодом.

- [ ] **Step 6: Прогон и коммит**

Run: `python -m uv run pytest -q` — Expected: PASS.

```bash
git add src/jobhunt/web tests/integration/test_web_profiles.py tests/unit/test_web_boundary.py
git commit -m "feat(web): выбор профиля из адреса и cookie, граница роутов замкнута"
```

---

### Task 9: Сообщения пустых состояний

**Files:**
- Modify: `src/jobhunt/web/templates/vacancies.html`, `src/jobhunt/web/routes/vacancies.py`
- Modify: `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: `VacancyFilters`, `list_tags` из предыдущих задач.
- Produces: ключи контекста `empty_reason: str | None`.

- [ ] **Step 1: Написать падающие тесты**

```python
def test_пусто_по_фильтрам_отличается_от_пусто_вообще(client, session):
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    _link(session, profile, _vacancy(session, "1"), tag)
    session.commit()

    empty_filter = client.get("/vacancies?status=offer").text
    assert "ничего не найдено" in empty_filter.lower()
    assert "сбросить" in empty_filter.lower()

    no_data = client.get("/vacancies?status=&source=").text
    assert "ничего не найдено" not in no_data.lower()


def test_смена_статуса_не_перерисовывает_таблицу(client, session):
    """Строка обязана остаться на месте, даже если после смены статуса она
    перестала подходить под текущий фильтр: исчезновение строки под курсором
    в момент клика читается как сбой, а не как результат.

    Гарантия структурная: обработчик статуса возвращает ТОЛЬКО ячейку. Если
    он когда-нибудь начнёт возвращать строки или страницу, этот тест упадёт.
    """
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=True)
    vacancy = _vacancy(session, "1")
    _link(session, profile, vacancy, tag)
    session.commit()

    body = client.post(f"/vacancies/{vacancy.id}/status", data={"status": "applied"}).text

    assert "<select" in body
    assert "<tr" not in body, "ответ обязан быть ячейкой, а не строкой или страницей"


def test_сброшенные_формой_фильтры_не_считаются_заданными(client, session):
    """Форма шлёт очищенное поле как пустую строку. Если её не приводить к
    None, пустой список объясняется «по выбранным фильтрам ничего не
    найдено» со ссылкой «сбросить фильтры» — при уже сброшенных фильтрах."""
    profile = _profile(session)
    _tag(session, profile, "Head of IT", enabled=True)
    session.commit()

    body = client.get("/vacancies?status=&source=&city=&query=").text

    assert "ничего не найдено" not in body.lower()


def test_все_теги_выключены_объясняются(client, session):
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT", enabled=False)
    _link(session, profile, _vacancy(session, "1"), tag)
    session.commit()

    body = client.get("/vacancies").text

    assert "все теги выключены" in body.lower(), (
        "пустая таблица без объяснения выглядит как поломка сбора"
    )
```

- [ ] **Step 2: Прогнать — обязаны упасть**

Run: `python -m uv run pytest tests/integration/test_web_vacancies.py -q -k "пусто or выключен or сброшенные"`
Expected: FAIL.

Хелперы `_profile`, `_vacancy`, `_pair`, `_tag`, `_link` в этом файле не определены — скопировать их из `tests/integration/test_web_tags.py`, как это уже сделано между другими файлами тестов (общего conftest для них нет).

- [ ] **Step 3: Реализовать**

В `vacancies_page` после получения страницы:

```python
    tags = list_tags(session, profile.id)
    empty_reason = None
    if not page.rows:
        if tags and not any(tag["is_enabled"] for tag in tags):
            empty_reason = "all_tags_disabled"
        elif filters != VacancyFilters():
            empty_reason = "filters"
        elif not tags:
            empty_reason = "no_tags"
        else:
            empty_reason = "no_data"
```

Сравнение `filters != VacancyFilters()` работает, потому что `VacancyFilters` — frozen dataclass со значениями по умолчанию: «фильтры заданы» и «страница открыта как есть» различаются без перечисления полей.

В `vacancies.html` вместо текущего `{% elif current_status or current_source %}`:

```html
  {% elif empty_reason == "all_tags_disabled" %}
    <p class="empty">Все теги выключены — искать нечем. Включите хотя бы один в панели тегов выше.</p>
  {% elif empty_reason == "filters" %}
    <p class="empty">По выбранным фильтрам ничего не найдено.
      <a href="/vacancies">Сбросить фильтры</a></p>
  {% elif empty_reason == "no_tags" %}
    <p class="empty">Тегов нет. Добавьте:
      <code>jobhunt tag add --profile "Имя" --text "Роль"</code></p>
  {% else %}
    <p class="empty">Вакансий пока нет. Запустите сбор:
      <code>python -m uv run python -m jobhunt.cli parse --profile "Имя" --mode full</code></p>
```

- [ ] **Step 4: Прогон и коммит**

Run: `python -m uv run pytest -q` — Expected: PASS.

```bash
git add src/jobhunt/web tests/integration/test_web_vacancies.py
git commit -m "feat(web): пустые состояния объясняют себя"
```

---

### Task 10: Живая проверка в браузере

Отдельная задача, а не пункт внутри последней: в слайсе 1 именно этот шаг остался незакрытым, потому что стоял последним подпунктом.

**Files:**
- Modify: `docs/HANDOFF.md`

- [ ] **Step 1: Поднять приложение на боевых данных**

```powershell
docker compose up -d --build
Invoke-WebRequest -UseBasicParsing http://localhost:8000/vacancies | Select-Object StatusCode
```
Expected: 200.

- [ ] **Step 2: Пройти сценарии**

Проверить в браузере и записать результат по каждому:

1. клик по чипу тега сужает таблицу, адресная строка меняется, перезагрузки не происходит;
2. повторный клик по тому же чипу возвращает полный список;
3. «показать ещё» добавляет строки в конец, кнопка исчезает на последней пачке, адрес не получает `offset`;
4. ввод в поиск не шлёт запрос на каждую букву (в сетевой панели — один запрос после паузы);
5. переключатель тега в панели меняет подпись «ищется/не ищется» и **не** перерисовывает таблицу;
6. смена профиля в селекторе перезагружает страницу целиком, чипы и панель тегов соответствуют новому профилю;
7. открытие сохранённой ссылки со всеми фильтрами восстанавливает то же состояние;
8. путь ошибки: сменить статус вакансии, у которой удалена пара, — должно появиться сообщение, а не молчаливое «как будто сохранилось»;
9. тёмная тема: таблица, чипы и панель тегов читаемы, переключатель на месте;
10. выбрать чип, затем сменить статус в фильтрах — чип остаётся выбранным и продолжает действовать (`hx-include=".chips"` у формы; в HTML это не видно, а в сетевой панели у запроса обязан быть параметр `tag`).

- [ ] **Step 3: Записать результат в передачу состояния**

В `docs/HANDOFF.md` добавить раздел с таблицей проверок по образцу раздела «Живая проверка интерактива» слайса 1: сценарий, результат, дата.

- [ ] **Step 4: Коммит**

```bash
git add docs/HANDOFF.md
git commit -m "docs: живая проверка страницы «Вакансии» после слайса 2a"
```

---

## Замер отклика

Снято 2026-08-05 задачей 2, шаг 8: `docker compose up -d --build`, затем 20
запросов `GET http://localhost:8000/vacancies/rows` через
`Measure-Command { Invoke-WebRequest -UseBasicParsing $u }` (PowerShell, как в
брифе). Строк в базе на момент замера — 57 (профиль «Кирилл», снято
`SELECT count(*) ... JOIN profile_vacancies`, не с чужих слов).

Среднее — **112.31 мс**, максимум — **147.79 мс**, минимум — 93.37 мс.

Порог решения: среднее ниже 100 мс — задачи 5–6 делаются целиком на сервере,
как запланировано; выше — остановиться и обсудить с владельцем. Среднее
оказалось выше порога, работа была остановлена, и число разложено по слоям
прежде, чем что-либо оптимизировать.

**Разложение (2026-08-05, та же база из 57 строк):**

| слой | время |
|---|---|
| весь доступ к данным: запрос, теги, сборка строк, со свежей сессией | 4 мс |
| статика `/static/htmx.min.js` снаружи (PowerShell + сеть Docker) | 32 мс |
| рендер `_rows.html` на 50 строк | **89 мс** |
| `/vacancies/rows` изнутри контейнера (без PowerShell и сети Windows) | 94 мс |

Причина найдена и к объёму данных отношения не имеет: у Jinja2 было
`auto_reload=True`, и на каждый из 50 `{% include "_status_cell.html" %}` за
запрос он делал `stat()` файла, а `src/` примонтирован в контейнер
бинд-маунтом с Windows-хоста, где такой вызов дорог. Тот же рендер с
`auto_reload=False` — 0.75 мс.

**Решение владельца:** выключить `auto_reload`. Цена нулевая: uvicorn запущен
без `--reload` (`docker-entrypoint.sh`), то есть перезапуск контейнера и так
нужен на любую правку кода — шаблоны просто перестали быть исключением.
Сделано отдельным коммитом (`08b9878`), окружение шаблонов вынесено в
`src/jobhunt/web/templating.py` и закреплено двумя AST-границами: `auto_reload`
не включить обратно молча, второй `Jinja2Templates` в веб-слое не создать.

**После правки: 6.4 мс** изнутри контейнера вместо 94 мс.

**Вывод для задач 5–6: клиентская фильтрация не нужна.** Отбор в SQL стоит
4 мс, и порог был превышен не им. Индексы под новые фильтры (§5.5 спеки) на
этих объёмах тоже не нужны.

## Что этот план не делает

Запуск сбора из браузера и прогресс, плашка «условия изменились» — слайс 2b (раздел 12 спеки, своей спеки у него ещё нет). Добавление и удаление тегов из браузера, веб-формы профиля и рамки сбора — слайс 3. Индексы под новые фильтры — только если замер задачи 2 покажет, что они нужны (§5.5 спеки).
