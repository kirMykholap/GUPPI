# Профильная видимость, теги ролей и нормализация полей — план реализации

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Перевести сбор вакансий на профильную модель: единый словарь значений для всех источников, видимость и деактивация по профилю, теги ролей с состоянием вкл/выкл, два режима сбора и HTML-выдача dou.ua вместо RSS.

**Architecture:** Между парсерами и записью в БД появляется отдельный слой нормализации: парсер извлекает сырые строки (`RawVacancy`), нормализация переводит их в канонические значения (`VacancyDTO`), `ingest` пишет в БД. Счётчики пропусков и признак активности переезжают с объективной строки вакансии на пару «профиль ↔ вакансия». Схема меняется несколькими маленькими миграциями, каждая из которых оставляет набор тестов зелёным.

**Tech Stack:** Python 3.12, SQLAlchemy 2.0, Alembic, PostgreSQL 17, httpx, BeautifulSoup + lxml, pydantic, pytest, ruff.

**Спека:** `docs/superpowers/specs/2026-08-04-profile-scoped-collection-design.md` — числа разведки в разделе 3, обоснования решений в разделе 9.

## Global Constraints

- **Никаких молча проглоченных сбоев.** Каждый путь частичной деградации — неизвестный slug города, неразобранная карточка, недоступная детальная страница, неприменённый фильтр, отброшенная по рамке вакансия, оборванный по рубежу обход — обязан писать `logger.warning` с указанием, что именно и сколько потеряно. Это главный урок плана A: семь дефектов из тринадцати были ровно этого класса.
- **Границы под тестами, а не под договорённостью.** `src/jobhunt/parsers/` не импортирует `jobhunt.db`, `jobhunt.ingest`, `sqlalchemy`. `src/jobhunt/normalize/` — то же самое. Проверяется разбором AST.
- **Сеть только через `jobhunt.http_client`.** Включая POST: пауза между запросами к хосту, robots.txt и дисковый кеш действуют на POST так же, как на GET.
- **`uv` не в PATH на машине разработчика.** Все команды запускаются как `python -m uv run ...`, а не `uv run ...`.
- **Консоль Windows в cp1252.** Любая новая точка входа, печатающая кириллицу, обязана начинаться с `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` — иначе `print()` роняет команду уже после того, как работа сделана.
- **Все datetime — timezone-aware, UTC.** Наивных значений в проекте нет ни одного, и появиться они не должны.
- **`ruff` чист.** `python -m uv run ruff check .` проходит после каждой задачи целиком. `ruff format --check` проверяется **только на затронутых задачей файлах**: на точке старта ветки (`969e340`) в репозитории уже лежат 10 неотформатированных файлов, и приводить их в порядок — не дело этой ветки. `line-length = 100`.
- **Комментарии объясняют «почему», а не «что».** В проекте принят этот стиль, следовать ему.
- **Тесты на русском в именах и сообщениях assert**, как в существующем коде.

## Порядок и почему он такой

Задачи 1–10 не касаются базы вообще: нормализация, контракты, HTTP, парсеры. Набор тестов остаётся зелёным всё это время.

Задачи 11–18 меняют схему, но **по одной предметной области за раз**, а не по слоям. Каждая несёт свою миграцию, своих потребителей и свои тесты — и оставляет `pytest` зелёным. Задача, которая меняла бы схему отдельно от потребителей, оставила бы дерево красным на полплана и сделала бы ревью между задачами бессмысленным.

## Карта файлов

**Создаются:**

| Файл | Ответственность |
|---|---|
| `src/jobhunt/normalize/__init__.py` | `normalize(raw, today) -> VacancyDTO` — сборка из частей |
| `src/jobhunt/normalize/dto.py` | `VacancyDTO` — канонический вид вакансии |
| `src/jobhunt/normalize/salary.py` | разбор зарплаты и валюты |
| `src/jobhunt/normalize/location.py` | разбор локации на город / «любой город» / формат |
| `src/jobhunt/normalize/dates.py` | разбор дат, в том числе без года |
| `tests/unit/test_normalize_salary.py` | |
| `tests/unit/test_normalize_location.py` | |
| `tests/unit/test_normalize_dates.py` | |
| `tests/unit/test_normalize_boundaries.py` | AST-граница слоя нормализации |
| `tests/unit/test_dou_listing.py` | разбор карточки dou |
| `tests/unit/test_dou_pagination.py` | пагинация и остановка по рубежу |
| `tests/unit/test_work_ua_url.py` | построение URL с фильтрами |
| `tests/fixtures/html/dou_list.html` | живая страница выдачи dou |
| `tests/fixtures/json/dou_xhr_load.json` | ответ догрузки dou |
| `tests/fixtures/html/work_ua_list_promo.html` | выдача work.ua с промо-блоком |
| `migrations/versions/0003…0007` | по миграции на предметную область |

**Изменяются:** `src/jobhunt/parsers/base.py`, `parsers/dou.py` (переписывается), `parsers/work_ua.py`, `http_client.py`, `db/models.py`, `ingest/upsert.py`, `ingest/activity.py`, `ingest/runner.py`, `cli.py`, `web/routes/vacancies.py`, `web/templates/vacancies.html`.

**Удаляется:** `tests/unit/test_dou.py` (тесты RSS-разбора — сам разбор исчезает вместе с источником данных).

---

## Task 1: Нормализация зарплаты

**Files:**
- Create: `src/jobhunt/normalize/__init__.py` (пустой на этом шаге), `src/jobhunt/normalize/salary.py`
- Test: `tests/unit/test_normalize_salary.py`

**Interfaces:**
- Consumes: ничего
- Produces: `parse_salary(text: str | None) -> tuple[int | None, int | None, str | None]` — `(min, max, currency)`. Валюта — `"UAH"` / `"USD"` / `"EUR"`. **Если валюта не распознана, возвращается `(None, None, None)`** — суммы без единицы измерения не сохраняются.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/unit/test_normalize_salary.py`:

```python
import pytest

from jobhunt.normalize.salary import parse_salary


@pytest.mark.parametrize(
    "raw,expected",
    [
        # Пусто и «зарплата не названа»
        (None, (None, None, None)),
        ("", (None, None, None)),
        ("   ", (None, None, None)),
        ("договірна", (None, None, None)),
        ("за результатами співбесіди", (None, None, None)),
        # work.ua: разряды разделены узкими и неразрывными пробелами
        ("80 000 – 120 000 грн", (80000, 120000, "UAH")),
        ("25 000 – 28 000 грн", (25000, 28000, "UAH")),
        # Границы диапазона словами
        ("від 50 000 грн", (50000, None, "UAH")),
        ("до 80 000 грн", (None, 80000, "UAH")),
        # Точная сумма: пол равен потолку
        ("25 000 грн", (25000, 25000, "UAH")),
        # dou.ua: валюта префиксом, разряды без разделителей
        ("$1000–2000", (1000, 2000, "USD")),
        ("$3000", (3000, 3000, "USD")),
        ("€2500–4000", (2500, 4000, "EUR")),
        # Валюта словом
        ("2000 USD", (2000, 2000, "USD")),
    ],
)
def test_разбирает_известные_формулировки(raw, expected):
    assert parse_salary(raw) == expected


def test_числа_без_валюты_не_сохраняются():
    """Число в неизвестных единицах хуже пустого поля: в таблице оно
    неотличимо от гривен и молча искажает фильтр по деньгам."""
    assert parse_salary("50 000") == (None, None, None)
    assert parse_salary("від 2000") == (None, None, None)


def test_від_внутри_слова_не_считается_границей():
    """\\b в Python не считает апостроф словообразующим, поэтому «від» внутри
    «від'їзд» штатной границей слова ловится ошибочно."""
    assert parse_salary("відповідно до досвіду, 30 000 грн") == (30000, 30000, "UAH")


def test_третье_и_последующие_числа_отбрасываются():
    assert parse_salary("10 000 – 20 000 грн, бонус 5 000") == (10000, 20000, "UAH")
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/unit/test_normalize_salary.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.normalize'`

- [ ] **Step 3: Реализовать**

Создать пустой `src/jobhunt/normalize/__init__.py` и `src/jobhunt/normalize/salary.py`:

```python
import re

# Пробелы, которыми площадки разделяют разряды: узкий неразрывный ( ),
# тонкий ( ) и обычный неразрывный ( ). Глазами они неотличимы от
# обычного пробела, поэтому заданы кодами, а не литералами.
_THIN_SPACES = (" ", " ", " ")

# Буквы украинского слова: а-я/А-Я плюс і/ї/є/ґ (их нет в диапазоне а-я) и
# апостроф. Апостроф разделяет буквы ВНУТРИ слова (від'їзд), а не слова между
# собой, но \b в Python его словообразующим не считает и потому находит «від»
# внутри «від'їзд». Поэтому границы задаются явными lookaround, а не \b.
_UA_WORD_CHARS = "а-яА-ЯіїєґІЇЄҐ'’ʼ"

# Порядок важен: «uah» проверяется раньше «$», чтобы строка вида «100 UAH»
# не досталась другому маркеру; символы валют не пересекаются между собой.
_CURRENCY_MARKERS: tuple[tuple[str, str], ...] = (
    ("грн", "UAH"),
    ("uah", "UAH"),
    ("₴", "UAH"),
    ("usd", "USD"),
    ("$", "USD"),
    ("eur", "EUR"),
    ("€", "EUR"),
)


def _is_standalone_word(text: str, word: str) -> bool:
    """Встречается ли word в text отдельным словом, а не частью другого."""
    pattern = rf"(?<![{_UA_WORD_CHARS}]){word}(?![{_UA_WORD_CHARS}])"
    return re.search(pattern, text) is not None


def _detect_currency(text: str) -> str | None:
    lowered = text.lower()
    for marker, code in _CURRENCY_MARKERS:
        if marker in lowered:
            return code
    return None


def parse_salary(text: str | None) -> tuple[int | None, int | None, str | None]:
    """Разобрать строку зарплаты в диапазон и валюту.

    Валюта обязательна: суммы без распознанной единицы измерения не
    возвращаются вовсе. Число без валюты в таблице неотличимо от гривен и
    молча искажает фильтр по деньгам — пустое поле честнее.
    """
    if not text or not text.strip():
        return None, None, None

    normalized = text
    for char in _THIN_SPACES:
        normalized = normalized.replace(char, " ")

    currency = _detect_currency(normalized)
    if currency is None:
        return None, None, None

    numbers = [int(match.replace(" ", "")) for match in re.findall(r"\d[\d ]*\d|\d", normalized)]
    if not numbers:
        return None, None, currency
    if len(numbers) == 1:
        # Одно число неоднозначно: «від X» — пол, «до X» — потолок, без обоих
        # слов трактуем как точную названную сумму (пол равен потолку).
        number = numbers[0]
        if _is_standalone_word(normalized, "від"):
            return number, None, currency
        if _is_standalone_word(normalized, "до"):
            return None, number, currency
        return number, number, currency
    return numbers[0], numbers[1], currency
```

- [ ] **Step 4: Убедиться, что тест проходит**

Run: `python -m uv run pytest tests/unit/test_normalize_salary.py -q`
Expected: PASS, 18 passed

- [ ] **Step 5: Проверить ruff и закоммитить**

```bash
python -m uv run ruff check src/jobhunt/normalize tests/unit/test_normalize_salary.py
python -m uv run ruff format --check src/jobhunt/normalize tests/unit/test_normalize_salary.py
git add src/jobhunt/normalize tests/unit/test_normalize_salary.py
git commit -m "feat(normalize): разбор зарплаты с обязательной валютой"
```

---

## Task 2: Нормализация локации

**Files:**
- Create: `src/jobhunt/normalize/location.py`
- Test: `tests/unit/test_normalize_location.py`

**Interfaces:**
- Consumes: ничего
- Produces: `Location` — `@dataclass(frozen=True)` с полями `city: str | None`, `city_any: bool`, `work_format: str | None`; `parse_location(raw: str | None) -> Location`; константа `WORK_FORMATS: tuple[str, ...] = ("remote", "hybrid", "onsite")`.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/unit/test_normalize_location.py`:

```python
import pytest

from jobhunt.normalize.location import Location, parse_location


@pytest.mark.parametrize(
    "raw,expected",
    [
        # Признак удалёнки площадки кладут в тот же слот, где обычно город
        ("Дистанційно", Location(city=None, city_any=False, work_format="remote")),
        ("віддалено", Location(city=None, city_any=False, work_format="remote")),
        ("Remote", Location(city=None, city_any=False, work_format="remote")),
        # «Вся Україна» — не «город неизвестен», а «любой город»
        ("Вся Україна", Location(city=None, city_any=True, work_format="onsite")),
        # Обычный город
        ("Київ", Location(city="Київ", city_any=False, work_format="onsite")),
        ("Львів", Location(city="Львів", city_any=False, work_format="onsite")),
        # Уточнение области отбрасывается, сырое значение хранится отдельно
        (
            "Вишневе (Київська обл.)",
            Location(city="Вишневе", city_any=False, work_format="onsite"),
        ),
        # Пусто — ничего не знаем, а не «офис»
        (None, Location(city=None, city_any=False, work_format=None)),
        ("", Location(city=None, city_any=False, work_format=None)),
        ("   ", Location(city=None, city_any=False, work_format=None)),
    ],
)
def test_разбирает_локацию(raw, expected):
    assert parse_location(raw) == expected


def test_маркер_удалёнки_ищется_без_учёта_регистра_и_пробелов():
    assert parse_location("  ВІДДАЛЕНО  ").work_format == "remote"


def test_город_не_превращается_в_удалёнку_из_за_подстроки():
    """Проверка, что маркер сопоставляется целиком, а не как подстрока
    внутри названия населённого пункта."""
    assert parse_location("Ремонтне").work_format == "onsite"
    assert parse_location("Ремонтне").city == "Ремонтне"
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/unit/test_normalize_location.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.normalize.location'`

- [ ] **Step 3: Реализовать**

Создать `src/jobhunt/normalize/location.py`:

```python
import re
from dataclasses import dataclass

# Допустимые значения формата работы. hybrid заведён впрок: ни один источник
# его сейчас не различает, но допустимое значение стоит ноль работы, а
# расширение перечисления позже стоит миграции.
WORK_FORMATS: tuple[str, ...] = ("remote", "hybrid", "onsite")

# Сопоставляются как отдельные слова, а не подстроки: иначе «Ремонтне»
# поймалось бы маркером «remote».
_REMOTE_MARKERS = ("дистанційно", "дистанционно", "віддалено", "удаленно", "remote")
_ANY_CITY_MARKERS = ("вся україна", "уся україна", "вся украина", "по всій україні")

# Уточнение области в скобках: «Вишневе (Київська обл.)» -> «Вишневе».
_PARENTHETICAL = re.compile(r"\s*\([^)]*\)\s*$")


@dataclass(frozen=True)
class Location:
    """Разобранная локация. city_any значит «любой город», а не «неизвестно»."""

    city: str | None
    city_any: bool
    work_format: str | None


def _matches_marker(text: str, markers: tuple[str, ...]) -> bool:
    for marker in markers:
        if re.search(rf"(?<!\w){re.escape(marker)}(?!\w)", text):
            return True
    return False


def parse_location(raw: str | None) -> Location:
    """Разобрать поле локации в город, признак «любой город» и формат работы.

    Обе площадки кладут признак удалённой работы в тот же слот разметки, где
    обычно стоит город: work.ua пишет «Дистанційно» вместо названия, dou.ua —
    «віддалено». Поэтому одно поле источника даёт три наших.

    Указанный город трактуется как onsite. Формально площадка говорит «работа
    в Киеве», а не «в офисе», и вакансия может оказаться гибридной. Но у
    work.ua «Дистанційно» стоит ВМЕСТО города именно потому, что это его
    собственный фильтр удалёнки — значит указанный город означает привязку к
    месту. Альтернатива (оставлять None везде, где источник не сказал явно)
    честнее, но бесполезнее: фильтр «только офис» не нашёл бы ничего.
    """
    if raw is None or not raw.strip():
        return Location(city=None, city_any=False, work_format=None)

    text = raw.strip()
    lowered = text.lower()

    if _matches_marker(lowered, _REMOTE_MARKERS):
        return Location(city=None, city_any=False, work_format="remote")

    if _matches_marker(lowered, _ANY_CITY_MARKERS):
        return Location(city=None, city_any=True, work_format="onsite")

    city = _PARENTHETICAL.sub("", text).strip().rstrip(",").strip()
    if not city:
        return Location(city=None, city_any=False, work_format=None)
    return Location(city=city, city_any=False, work_format="onsite")
```

- [ ] **Step 4: Убедиться, что тест проходит**

Run: `python -m uv run pytest tests/unit/test_normalize_location.py -q`
Expected: PASS, 12 passed

- [ ] **Step 5: Проверить ruff и закоммитить**

```bash
python -m uv run ruff check src/jobhunt/normalize tests/unit/test_normalize_location.py
python -m uv run ruff format --check src/jobhunt/normalize tests/unit/test_normalize_location.py
git add src/jobhunt/normalize/location.py tests/unit/test_normalize_location.py
git commit -m "feat(normalize): разбор локации на город, «любой город» и формат работы"
```

---

## Task 3: Нормализация дат, включая дату без года

**Files:**
- Create: `src/jobhunt/normalize/dates.py`
- Test: `tests/unit/test_normalize_dates.py`

**Interfaces:**
- Consumes: ничего
- Produces: `parse_posted_at(raw: str | None, today: date) -> datetime | None` — timezone-aware UTC, полночь. `today` передаётся явно, а не берётся из `datetime.now()`, чтобы вывод года был воспроизводимо тестируем. Также `UA_MONTHS: dict[str, int]`.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/unit/test_normalize_dates.py`:

```python
from datetime import UTC, date, datetime

import pytest

from jobhunt.normalize.dates import parse_posted_at

TODAY = date(2026, 8, 4)


@pytest.mark.parametrize(
    "raw,expected",
    [
        # work.ua: год указан прямо в атрибуте title ссылки
        (
            "Web Department Team Lead, вакансія від 3 серпня 2026",
            datetime(2026, 8, 3, tzinfo=UTC),
        ),
        ("вакансія від 27 липня 2026", datetime(2026, 7, 27, tzinfo=UTC)),
        # dou.ua: года нет вовсе
        ("3 серпня", datetime(2026, 8, 3, tzinfo=UTC)),
        ("27 липня", datetime(2026, 7, 27, tzinfo=UTC)),
        # Не разобрали — None, а не «сегодня»
        (None, None),
        ("", None),
        ("нещодавно", None),
        ("32 серпня", None),
        ("3 невідомого", None),
    ],
)
def test_разбирает_дату(raw, expected):
    assert parse_posted_at(raw, TODAY) == expected


def test_дата_без_года_в_будущем_относится_к_прошлому_году():
    """Стык декабря и января: 2 января мы видим карточку «28 грудня». Год не
    указан, и если взять текущий, дата окажется на 11 месяцев в будущем."""
    assert parse_posted_at("28 грудня", date(2027, 1, 2)) == datetime(2026, 12, 28, tzinfo=UTC)


def test_дата_без_года_в_том_же_месяце_относится_к_текущему_году():
    assert parse_posted_at("1 січня", date(2027, 1, 2)) == datetime(2027, 1, 1, tzinfo=UTC)


def test_возвращает_timezone_aware():
    """Наивные datetime в проекте запрещены: вперемешку с осознанными они
    ломают сравнения и сортировку."""
    result = parse_posted_at("3 серпня", TODAY)
    assert result is not None and result.tzinfo is not None
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/unit/test_normalize_dates.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.normalize.dates'`

- [ ] **Step 3: Реализовать**

Создать `src/jobhunt/normalize/dates.py`:

```python
import re
from datetime import UTC, date, datetime

UA_MONTHS: dict[str, int] = {
    "січня": 1,
    "лютого": 2,
    "березня": 3,
    "квітня": 4,
    "травня": 5,
    "червня": 6,
    "липня": 7,
    "серпня": 8,
    "вересня": 9,
    "жовтня": 10,
    "листопада": 11,
    "грудня": 12,
}

# Год указан (work.ua: «вакансія від 3 серпня 2026»).
_WITH_YEAR = re.compile(r"(\d{1,2})\s+([а-яіїєґ]+)\s+(\d{4})", re.IGNORECASE)
# Года нет (dou.ua: «3 серпня»).
_WITHOUT_YEAR = re.compile(r"(?<!\d)(\d{1,2})\s+([а-яіїєґ]+)(?!\s+\d{4})", re.IGNORECASE)


def _build(year: int, month: int, day: int) -> datetime | None:
    try:
        # Площадки не указывают время и часовой пояс — фиксируем полночь UTC,
        # чтобы в базе не оказалось наивных дат вперемешку с осознанными.
        return datetime(year, month, day, tzinfo=UTC)
    except ValueError:
        # «32 серпня» и подобное: лучше не знать дату, чем подставить неверную.
        return None


def parse_posted_at(raw: str | None, today: date) -> datetime | None:
    """Разобрать дату публикации. Понимает обе формы: с годом и без него.

    `today` передаётся явно, а не берётся из datetime.now(), потому что вывод
    года для формы без года зависит от текущей даты — иначе тест на стык
    декабря и января было бы нечем написать.
    """
    if raw is None or not raw.strip():
        return None

    match = _WITH_YEAR.search(raw)
    if match is not None:
        day, month_name, year = match.groups()
        month = UA_MONTHS.get(month_name.lower())
        if month is None:
            return None
        return _build(int(year), month, int(day))

    match = _WITHOUT_YEAR.search(raw)
    if match is None:
        return None
    day, month_name = match.groups()
    month = UA_MONTHS.get(month_name.lower())
    if month is None:
        return None

    # Год не указан. Месяц больше текущего означает, что публикация относится к
    # прошлому году: 2 января карточка «28 грудня» — это декабрь позади, а не
    # через 11 месяцев впереди.
    year = today.year - 1 if month > today.month else today.year
    return _build(year, month, int(day))
```

- [ ] **Step 4: Убедиться, что тест проходит**

Run: `python -m uv run pytest tests/unit/test_normalize_dates.py -q`
Expected: PASS, 12 passed

- [ ] **Step 5: Проверить ruff и закоммитить**

```bash
python -m uv run ruff check src/jobhunt/normalize tests/unit/test_normalize_dates.py
python -m uv run ruff format --check src/jobhunt/normalize tests/unit/test_normalize_dates.py
git add src/jobhunt/normalize/dates.py tests/unit/test_normalize_dates.py
git commit -m "feat(normalize): разбор дат, включая форму без года"
```

---

## Task 4: Контракты слоя и сборка нормализации

**Files:**
- Create: `src/jobhunt/normalize/dto.py`
- Modify: `src/jobhunt/normalize/__init__.py`, `src/jobhunt/parsers/base.py`
- Test: `tests/unit/test_normalize_boundaries.py`, `tests/unit/test_normalize.py`

**Interfaces:**
- Consumes: `parse_salary` (Task 1), `parse_location` (Task 2), `parse_posted_at` (Task 3)
- Produces:
  - `jobhunt.parsers.base.RawVacancy` — pydantic-модель: `source`, `external_id`, `title`, `url`, `description_snippet`, и необязательные `company_raw`, `location_raw`, `salary_raw`, `posted_raw` (все `str | None`)
  - `jobhunt.parsers.base.SearchFilters` — `@dataclass(frozen=True)`: `cities: tuple[str, ...] = ()`, `remote_only: bool = False`, `depth_days: int = 60`, `mode: str = "full"`
  - `jobhunt.parsers.base.ParseResult` — теперь `vacancies: list[RawVacancy]`, плюс `total_available: int | None = None` к существующим `truncated`, `ids_complete`
  - `jobhunt.normalize.dto.VacancyDTO` — pydantic-модель с полями `source`, `external_id`, `title`, `url`, `description_raw`, `description_is_full: bool`, `company`, `city`, `city_any: bool`, `work_format`, `salary_min`, `salary_max`, `salary_currency`, `location_raw`, `posted_at`
  - `jobhunt.normalize.normalize(raw: RawVacancy, today: date) -> VacancyDTO`

`VacancyDTO` переезжает из `parsers/base.py` в `normalize/dto.py`: парсеры больше не производят канонических значений, поэтому и владеть этим типом не должны.

**Важно про направление зависимостей.** `normalize/__init__.py` импортирует `RawVacancy` из `parsers.base`. Обратное запрещено. При этом `parsers/dou.py` в задаче 8 будет импортировать `normalize.dates` — это не цикл, потому что `dates.py` не импортирует ничего из проекта. Правило: листовые модули нормализации (`salary`, `location`, `dates`) доступны всем, а `normalize/__init__.py` — только слоям выше парсеров.

- [ ] **Step 1: Написать падающий тест границы**

Создать `tests/unit/test_normalize_boundaries.py`:

```python
import ast
import pathlib

NORMALIZE_DIR = pathlib.Path(__file__).resolve().parents[2] / "src" / "jobhunt" / "normalize"
FORBIDDEN = ("jobhunt.db", "jobhunt.ingest", "jobhunt.web", "sqlalchemy")


def _imported_modules(path: pathlib.Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def test_пакет_нормализации_существует():
    """Без этой проверки тест границы прошёл бы на пустом каталоге."""
    assert (NORMALIZE_DIR / "dto.py").exists(), "не создан src/jobhunt/normalize/dto.py"


def test_нормализация_не_знает_о_базе():
    """Слой нормализации — чистые функции над строками. Это позволяет
    тестировать его без БД и без HTML-фикстур."""
    offenders = []
    for path in NORMALIZE_DIR.glob("*.py"):
        for module in _imported_modules(path):
            if module.startswith(FORBIDDEN):
                offenders.append(f"{path.name} импортирует {module}")
    assert offenders == [], "нарушена граница модуля normalize: " + "; ".join(offenders)


def test_листовые_модули_не_зависят_от_парсеров():
    """salary/location/dates обязаны оставаться листьями: их импортируют сами
    парсеры (dou использует dates для остановки пагинации), и обратная связь
    создала бы цикл импорта."""
    offenders = []
    for name in ("salary.py", "location.py", "dates.py"):
        for module in _imported_modules(NORMALIZE_DIR / name):
            if module.startswith("jobhunt"):
                offenders.append(f"{name} импортирует {module}")
    assert offenders == [], "листовой модуль нормализации перестал быть листом: " + "; ".join(
        offenders
    )
```

Создать `tests/unit/test_normalize.py`:

```python
from datetime import UTC, date, datetime

from jobhunt.normalize import normalize
from jobhunt.parsers.base import RawVacancy

TODAY = date(2026, 8, 4)


def _raw(**overrides) -> RawVacancy:
    base = {
        "source": "dou.ua",
        "external_id": "363911",
        "title": "Senior SMM Specialist",
        "url": "https://jobs.dou.ua/companies/freitty/vacancies/363911/",
        "description_snippet": "ПРО КОМПАНІЮ FREITTY…",
        "company_raw": "FREITTY",
        "location_raw": "віддалено",
        "salary_raw": "$1000–2000",
        "posted_raw": "3 серпня",
    }
    base.update(overrides)
    return RawVacancy(**base)


def test_собирает_канонические_значения_из_сырых_строк():
    dto = normalize(_raw(), TODAY)

    assert dto.source == "dou.ua"
    assert dto.external_id == "363911"
    assert dto.company == "FREITTY"
    assert dto.city is None
    assert dto.city_any is False
    assert dto.work_format == "remote"
    assert (dto.salary_min, dto.salary_max, dto.salary_currency) == (1000, 2000, "USD")
    assert dto.posted_at == datetime(2026, 8, 3, tzinfo=UTC)


def test_сырая_локация_сохраняется_дословно():
    """Если правило разбора окажется неверным, переразобрать нужно будет из
    сырого значения, без повторного обхода площадок."""
    dto = normalize(_raw(location_raw="Вишневе (Київська обл.)"), TODAY)
    assert dto.location_raw == "Вишневе (Київська обл.)"
    assert dto.city == "Вишневе"


def test_описание_из_карточки_помечается_неполным():
    """Сбор приносит только сниппет: полный текст качается по требованию."""
    dto = normalize(_raw(), TODAY)
    assert dto.description_is_full is False
    assert dto.description_raw == "ПРО КОМПАНІЮ FREITTY…"


def test_пустая_компания_остаётся_пустой_а_не_строкой():
    dto = normalize(_raw(company_raw="   "), TODAY)
    assert dto.company is None
```

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/unit/test_normalize_boundaries.py tests/unit/test_normalize.py -q`
Expected: FAIL — `ImportError: cannot import name 'RawVacancy' from 'jobhunt.parsers.base'`

- [ ] **Step 3: Реализовать контракты**

Заменить содержимое `src/jobhunt/parsers/base.py`:

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, Field


class ParserStructureError(RuntimeError):
    """Разметка источника изменилась: ожидаемый элемент не найден.

    Поднимается вместо тихого возврата пустого списка — иначе поломка вёрстки
    выглядит как «сегодня вакансий нет».
    """


class RawVacancy(BaseModel):
    """Вакансия ровно в том виде, в каком её отдал источник: только строки.

    Парсер не производит канонических значений намеренно. Словарь значений
    обязан быть одним на все источники, и отдельный слой нормализации делает
    его нарушение невозможным, а не маловероятным.
    """

    source: str
    external_id: str
    title: str
    url: str
    description_snippet: str

    company_raw: str | None = None
    location_raw: str | None = None
    salary_raw: str | None = None
    posted_raw: str | None = None


@dataclass(frozen=True)
class SearchFilters:
    """Рамка одного запроса к источнику.

    Это значение, а не профиль: парсеры ничего не знают ни о профилях, ни о
    базе, и эта граница держится тестом разбора AST.

    Каждый источник применяет то, что умеет: work.ua кладёт город и признак
    удалёнки в путь URL и не умеет фильтровать по дате вовсе, dou.ua передаёт
    город и удалёнку параметрами, а глубину использует для досрочной остановки
    пагинации. Неприменённый фильтр не ошибка — ingest перепроверяет рамку
    целиком локально.
    """

    cities: tuple[str, ...] = ()
    remote_only: bool = False
    depth_days: int = 60
    mode: Literal["full", "quick"] = "full"


class ParseResult(BaseModel):
    """Результат одного запроса к источнику.

    truncated=True означает, что источник отдал не всё: выдача упёрлась в лимит.

    ids_complete говорит о другом: является ли множество external_id полной
    картиной того, что источник сейчас отдаёт по этому запросу. Оркестратор
    обязан использовать результат для отметки пропусков только при
    ids_complete=True — иначе вакансии, отсутствующие в результате не потому,
    что их сняли, а потому, что источник их не показал, будут посчитаны
    пропавшими.

    total_available — сколько источник заявил всего («Стор. 1 з 944» у work.ua,
    «1401 вакансія» у dou.ua). Нужен, чтобы предупреждение о слишком широком
    теге и строка «собрано 300 из 13 216» опирались на факт, а не на догадку.
    """

    vacancies: list[RawVacancy] = Field(default_factory=list)
    truncated: bool = False
    ids_complete: bool = True
    total_available: int | None = None


class BaseParser(ABC):
    """Единый интерфейс источника вакансий."""

    source_name: str

    @abstractmethod
    def fetch_listings(self, query: str, filters: SearchFilters) -> ParseResult:
        """Собрать карточки выдачи по одному поисковому запросу.

        Полные описания здесь не качаются: все поля, по которым идёт
        фильтрация, есть в карточке, а детальные страницы стоят сотен запросов
        ради таблицы, которая будет сужена до двух десятков строк.
        """
```

Создать `src/jobhunt/normalize/dto.py`:

```python
from datetime import datetime

from pydantic import BaseModel


class VacancyDTO(BaseModel):
    """Вакансия в каноническом виде: словарь значений одинаков для всех источников.

    О базе не знает ничего — этим занимается ingest.
    """

    source: str
    external_id: str
    title: str
    url: str

    description_raw: str
    # False означает «это сниппет из карточки выдачи». Полный текст качается по
    # требованию, и без этого флага сбор молча затирал бы его сниппетом.
    description_is_full: bool = False

    company: str | None = None

    # Сырое значение локации хранится всегда: правило разбора может оказаться
    # неверным, и тогда переразобрать нужно будет без повторного обхода площадок.
    location_raw: str | None = None
    city: str | None = None
    city_any: bool = False
    work_format: str | None = None

    salary_min: int | None = None
    salary_max: int | None = None
    salary_currency: str | None = None

    posted_at: datetime | None = None
```

Заменить содержимое `src/jobhunt/normalize/__init__.py`:

```python
"""Слой нормализации: сырые строки источника → канонические значения.

Отделён от парсеров намеренно. Словарь значений должен быть одним на все
источники — это и есть приведение типов, ради которого затевалась итерация.
Отдельный этап делает расхождение невозможным, а не маловероятным.
"""

from datetime import date

from jobhunt.normalize.dates import parse_posted_at
from jobhunt.normalize.dto import VacancyDTO
from jobhunt.normalize.location import parse_location
from jobhunt.normalize.salary import parse_salary
from jobhunt.parsers.base import RawVacancy

__all__ = ["VacancyDTO", "normalize"]


def _clean(value: str | None) -> str | None:
    """Пустая строка и строка из пробелов — это отсутствие значения, а не значение."""
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def normalize(raw: RawVacancy, today: date) -> VacancyDTO:
    """Перевести сырую вакансию источника в канонический вид."""
    location = parse_location(raw.location_raw)
    salary_min, salary_max, currency = parse_salary(raw.salary_raw)

    return VacancyDTO(
        source=raw.source,
        external_id=raw.external_id,
        title=raw.title.strip(),
        url=raw.url,
        description_raw=raw.description_snippet,
        description_is_full=False,
        company=_clean(raw.company_raw),
        location_raw=_clean(raw.location_raw),
        city=location.city,
        city_any=location.city_any,
        work_format=location.work_format,
        salary_min=salary_min,
        salary_max=salary_max,
        salary_currency=currency,
        posted_at=parse_posted_at(raw.posted_raw, today),
    )
```

- [ ] **Step 4: Починить существующие импорты `VacancyDTO`**

`VacancyDTO` больше нет в `parsers/base.py`. Найти и обновить все ссылки:

Run: `python -m uv run python -c "import subprocess; print(subprocess.run(['git','grep','-n','VacancyDTO'],capture_output=True,text=True).stdout)"`

Ожидаемые места: `src/jobhunt/ingest/upsert.py` (импорт), `src/jobhunt/parsers/work_ua.py`, `src/jobhunt/parsers/dou.py`, `tests/unit/test_work_ua_listing.py`, `tests/unit/test_dou.py`, `tests/integration/test_upsert.py`.

На этом шаге меняется только импорт в `src/jobhunt/ingest/upsert.py`:

```python
from jobhunt.normalize import VacancyDTO
```

Парсеры перейдут на `RawVacancy` в задачах 7–10, а до тех пор продолжают
производить `VacancyDTO`. Чтобы набор тестов оставался зелёным, переключить их
импорт на новое место — по одной строке в файле:

```python
# src/jobhunt/parsers/dou.py и src/jobhunt/parsers/work_ua.py
from jobhunt.normalize.dto import VacancyDTO
```

То же в `tests/unit/test_dou.py`, `tests/unit/test_work_ua_listing.py`,
`tests/integration/test_upsert.py`.

Реэкспорт `VacancyDTO` обратно в `parsers/base.py` для этого **не** заводить:
он спрятал бы временную зависимость там, где её никто не ищет, и пережил бы
задачу 10 незамеченным. Явный импорт находится поиском и исчезает вместе с
последним парсером, который перестанет производить канонические значения.

- [ ] **Step 5: Прогнать весь набор тестов**

Run: `python -m uv run pytest -q`
Expected: PASS — прежние 137 тестов плюс новые; ни одного упавшего

Если падает `tests/unit/test_parser_boundaries.py` из-за реэкспорта — это ожидаемо и означает, что `parsers/base.py` теперь импортирует `jobhunt.normalize`. Добавить в `FORBIDDEN` этого теста исключение нельзя: вместо этого убедиться, что `jobhunt.normalize` не входит в список `FORBIDDEN` (там только `jobhunt.db`, `jobhunt.ingest`, `sqlalchemy`) — тогда тест проходит без изменений.

- [ ] **Step 6: Проверить ruff и закоммитить**

```bash
python -m uv run ruff check .
python -m uv run ruff format --check .
git add src/jobhunt/normalize src/jobhunt/parsers/base.py src/jobhunt/ingest/upsert.py tests/unit/test_normalize.py tests/unit/test_normalize_boundaries.py
git commit -m "feat(normalize): контракты RawVacancy/SearchFilters/VacancyDTO и сборка normalize()"
```

---

## Task 5: HttpClient учится POST

**Files:**
- Modify: `src/jobhunt/http_client.py`
- Test: `tests/unit/test_http_client.py`

**Interfaces:**
- Consumes: ничего
- Produces: `HttpClient.post(url: str, data: dict[str, str], *, referer: str | None = None) -> str`; `HttpClient.cookies` — доступ к cookie-jar для чтения csrf-токена (`client.cookies.get("csrftoken")`).

Пагинация dou.ua работает только через POST на `/vacancies/xhr-load/` с csrf-токеном из cookie. Клиент — единственная точка выхода в сеть, обходить его нельзя, значит POST должен появиться здесь, вместе со всеми обязанностями GET: пауза между запросами к хосту, robots.txt и дисковый кеш.

- [ ] **Step 1: Написать падающие тесты**

Дописать в `tests/unit/test_http_client.py`:

```python
def test_post_отправляет_форму_и_возвращает_тело():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["method"] = request.method
        captured["url"] = str(request.url)
        captured["body"] = request.content.decode()
        return httpx.Response(200, text='{"html": "", "last": true, "num": 0}')

    client = HttpClient(transport=httpx.MockTransport(handler), delay_seconds=0)
    try:
        body = client.post(
            "https://jobs.dou.ua/vacancies/xhr-load/?search=Head+of+IT",
            data={"csrfmiddlewaretoken": "tok", "count": "20"},
        )
    finally:
        client.close()

    assert captured["method"] == "POST"
    assert "csrfmiddlewaretoken=tok" in captured["body"]
    assert "count=20" in captured["body"]
    assert body.startswith("{")


def test_post_держит_ту_же_паузу_что_и_get(monkeypatch):
    """Пауза считается на хост и обязана действовать на POST: иначе пагинация
    dou.ua обстреляла бы площадку десятками запросов подряд."""
    slept: list[float] = []
    monkeypatch.setattr("jobhunt.http_client.time.sleep", lambda s: slept.append(s))

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text="ok")

    client = HttpClient(transport=httpx.MockTransport(handler), delay_seconds=5)
    try:
        client.get("https://jobs.dou.ua/vacancies/")
        client.post("https://jobs.dou.ua/vacancies/xhr-load/", data={"count": "20"})
    finally:
        client.close()

    assert slept, "POST не выдержал паузу между запросами к тому же хосту"


def test_post_подставляет_referer_когда_он_передан():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["referer"] = request.headers.get("Referer")
        captured["requested_with"] = request.headers.get("X-Requested-With")
        return httpx.Response(200, text="ok")

    client = HttpClient(transport=httpx.MockTransport(handler), delay_seconds=0)
    try:
        client.post(
            "https://jobs.dou.ua/vacancies/xhr-load/",
            data={"count": "20"},
            referer="https://jobs.dou.ua/vacancies/?search=Head+of+IT",
        )
    finally:
        client.close()

    assert captured["referer"] == "https://jobs.dou.ua/vacancies/?search=Head+of+IT"
    assert captured["requested_with"] == "XMLHttpRequest"


def test_post_кеширует_ответ_с_учётом_тела_запроса(tmp_path):
    """Кеш нужен для отладки парсера. Ключ обязан включать тело: иначе две
    страницы пагинации, отличающиеся только смещением, слились бы в одну."""
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.content.decode())
        return httpx.Response(200, text=f"ответ {len(calls)}")

    client = HttpClient(
        transport=httpx.MockTransport(handler),
        delay_seconds=0,
        cache_enabled=True,
        cache_dir=tmp_path,
    )
    try:
        first = client.post("https://jobs.dou.ua/x/", data={"count": "20"})
        second = client.post("https://jobs.dou.ua/x/", data={"count": "60"})
        repeat = client.post("https://jobs.dou.ua/x/", data={"count": "20"})
    finally:
        client.close()

    assert first != second, "разные смещения дали одинаковый ответ — ключ кеша не учёл тело"
    assert repeat == first, "повторный запрос не взят из кеша"
    assert len(calls) == 2, "кеш не сработал: сеть дёрнута лишний раз"


def test_post_уважает_robots():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text="User-agent: *\nDisallow: /vacancies/xhr-load/")
        return httpx.Response(200, text="не должно быть запрошено")

    client = HttpClient(
        transport=httpx.MockTransport(handler), delay_seconds=0, check_robots=True
    )
    try:
        with pytest.raises(RobotsDisallowed):
            client.post("https://jobs.dou.ua/vacancies/xhr-load/", data={"count": "20"})
    finally:
        client.close()
```

Убедиться, что в начале файла есть импорты `httpx`, `pytest`, `HttpClient`, `RobotsDisallowed` — при необходимости дописать.

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/unit/test_http_client.py -q`
Expected: FAIL — `AttributeError: 'HttpClient' object has no attribute 'post'`

- [ ] **Step 3: Реализовать**

В `src/jobhunt/http_client.py` вынести общую часть и добавить POST. Заменить метод `get` и добавить `post`:

```python
    def get(self, url: str) -> str:
        cached = self._read_cache(url)
        if cached is not None:
            return cached

        self._guard(url)
        response = self._send("GET", url)
        self._write_cache(url, response.text)
        return response.text

    def post(self, url: str, data: dict[str, str], *, referer: str | None = None) -> str:
        """POST формы. Нужен для пагинации dou.ua (`/vacancies/xhr-load/`).

        Обязанности те же, что у GET: robots.txt, пауза между запросами к
        хосту и дисковый кеш. Клиент — единственная точка выхода в сеть, и
        POST не имеет права быть исключением из её правил.
        """
        cache_key = self._cache_key(url, data)
        cached = self._read_cache(cache_key)
        if cached is not None:
            return cached

        self._guard(url)
        headers = {"X-Requested-With": "XMLHttpRequest"}
        if referer is not None:
            headers["Referer"] = referer
        response = self._send("POST", url, data=data, headers=headers)
        self._write_cache(cache_key, response.text)
        return response.text

    def _guard(self, url: str) -> None:
        """Проверка robots.txt и пауза — общая часть GET и POST."""
        if self._check_robots and not self._robots_allows(url):
            raise RobotsDisallowed(f"robots.txt запрещает обход: {url}")
        self._respect_delay(url)

    def _send(self, method: str, url: str, **kwargs) -> httpx.Response:
        host = urlsplit(url).netloc
        try:
            response = self._client.request(method, url, **kwargs)
            response.raise_for_status()
        finally:
            # Метка времени пишется независимо от исхода: запрос, упавший с
            # HTTP-ошибкой, всё равно был сделан и должен учитываться в паузе.
            self._last_request_at[host] = time.monotonic()
        return response

    @property
    def cookies(self) -> httpx.Cookies:
        """Cookie-jar клиента. Нужен, чтобы прочитать csrf-токен dou.ua."""
        return self._client.cookies
```

Изменить `_cache_path` и добавить `_cache_key`:

```python
    def _cache_key(self, url: str, data: dict[str, str] | None = None) -> str:
        """Ключ кеша. Для POST включает тело: две страницы пагинации
        отличаются только смещением в теле, и без него слились бы в одну."""
        if not data:
            return url
        body = "&".join(f"{k}={v}" for k, v in sorted(data.items()))
        return f"{url}|{body}"

    def _cache_path(self, key: str) -> Path:
        # Записи кеша никогда не устаревают — допустимо, т.к. кеш нужен только
        # для отладки парсера и по умолчанию выключен.
        digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:32]
        return self._cache_dir / f"{digest}.html"
```

`_read_cache` и `_write_cache` принимают теперь ключ, а не url — переименовать параметр с `url` на `key` в обоих; тела не меняются.

- [ ] **Step 4: Убедиться, что тесты проходят**

Run: `python -m uv run pytest tests/unit/test_http_client.py -q`
Expected: PASS — прежние тесты клиента плюс 5 новых

- [ ] **Step 5: Прогнать весь набор и закоммитить**

```bash
python -m uv run pytest -q
python -m uv run ruff check . && python -m uv run ruff format --check .
git add src/jobhunt/http_client.py tests/unit/test_http_client.py
git commit -m "feat(http): POST с csrf-cookie для пагинации dou, с паузой, robots и кешем"
```

---

## Task 6: Фикстуры живых страниц

**Files:**
- Create: `tests/fixtures/html/dou_list.html`, `tests/fixtures/json/dou_xhr_load.json`, `tests/fixtures/html/work_ua_list_promo.html`
- Create: `scripts/capture_dou_xhr.py`
- Test: `tests/unit/test_fixtures_sanity.py`

**Interfaces:**
- Consumes: `HttpClient.post` (Task 5)
- Produces: файлы фикстур, на которых стоят задачи 7–10.

Существующий `scripts/capture_fixture.py` умеет только GET. Ответ догрузки dou приходит на POST, поэтому нужен отдельный маленький скрипт.

**Зачем отдельная фикстура work.ua с промо-блоком.** В закоммиченной `work_ua_list.html` класса `js-hot-block` нет ни на одной карточке, а в живой выдаче по широкому запросу им помечены все. Пока это расхождение не зафиксировано, тесты проверяют разметку, которой на площадке может уже не быть.

- [ ] **Step 1: Написать скрипт захвата ответа догрузки**

Создать `scripts/capture_dou_xhr.py`:

```python
"""Сохраняет ответ догрузки выдачи dou.ua в каталог фикстур.

Ответ приходит на POST с csrf-токеном из cookie, поэтому capture_fixture.py,
умеющий только GET, здесь не годится.

Запуск:
    python -m uv run python scripts/capture_dou_xhr.py "менеджер" 60 dou_xhr_load.json
"""

import sys
from pathlib import Path
from urllib.parse import quote

from jobhunt.http_client import HttpClient

FIXTURES = Path(__file__).resolve().parents[1] / "tests" / "fixtures"
LIST_URL = "https://jobs.dou.ua/vacancies/"


def main() -> int:
    # На консолях с не-UTF-8 кодовой страницей print() кириллицы иначе роняет
    # скрипт уже ПОСЛЕ успешной записи файла — что выглядит как сбой захвата.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if len(sys.argv) != 4:
        print(__doc__)
        return 1

    query, offset, filename = sys.argv[1], sys.argv[2], sys.argv[3]
    client = HttpClient(check_robots=True)
    try:
        page_url = f"{LIST_URL}?search={quote(query)}"
        client.get(page_url)  # ради csrf-токена в cookie
        token = client.cookies.get("csrftoken")
        if not token:
            print("csrftoken не получен — площадка не выдала cookie, захват невозможен")
            return 1
        body = client.post(
            f"{LIST_URL}xhr-load/?search={quote(query)}",
            data={"csrfmiddlewaretoken": token, "count": offset},
            referer=page_url,
        )
    finally:
        client.close()

    target = FIXTURES / "json" / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8")
    print(f"сохранено {len(body)} символов -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Захватить три фикстуры**

```bash
python -m uv run python scripts/capture_fixture.py "https://jobs.dou.ua/vacancies/?search=%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80" html/dou_list.html
python -m uv run python scripts/capture_dou_xhr.py "менеджер" 60 dou_xhr_load.json
python -m uv run python scripts/capture_fixture.py "https://www.work.ua/jobs-%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80/" html/work_ua_list_promo.html
```

Смещение 60 выбрано намеренно: на нём промо-блок уже закончился, и в ответе только обычные карточки, отсортированные по дате, — именно то, на чём проверяется остановка по рубежу.

- [ ] **Step 3: Написать тест-сторож фикстур**

Создать `tests/unit/test_fixtures_sanity.py`:

```python
import json
from pathlib import Path

from bs4 import BeautifulSoup

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


def test_фикстура_выдачи_dou_содержит_карточки_и_счётчик():
    soup = BeautifulSoup((FIXTURES / "html" / "dou_list.html").read_text(encoding="utf-8"), "lxml")
    cards = soup.select("li.l-vacancy")
    assert len(cards) >= 10, f"в фикстуре dou слишком мало карточек: {len(cards)}"
    h1 = soup.select_one("h1")
    assert h1 is not None and "ваканс" in h1.get_text(" ", strip=True).lower(), (
        "в фикстуре dou нет заголовка с общим числом вакансий"
    )


def test_фикстура_догрузки_dou_это_json_с_ожидаемыми_ключами():
    data = json.loads((FIXTURES / "json" / "dou_xhr_load.json").read_text(encoding="utf-8"))
    assert set(data) >= {"html", "last", "num"}, f"неожиданные ключи ответа догрузки: {list(data)}"
    cards = BeautifulSoup(data["html"], "lxml").select("li.l-vacancy")
    assert cards, "в html догрузки нет ни одной карточки"


def test_фикстура_work_ua_содержит_промо_блок():
    """Ради этого фикстура и снималась: в старой work_ua_list.html класса
    js-hot-block нет ни на одной карточке, а в живой выдаче он на всех."""
    html = (FIXTURES / "html" / "work_ua_list_promo.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    container = soup.select_one("#pjax-jobs-list")
    assert container is not None, "в фикстуре work.ua нет контейнера #pjax-jobs-list"
    promo = [c for c in container.select("div.card.job-link") if "js-hot-block" in (c.get("class") or [])]
    assert promo, "в фикстуре нет ни одной карточки промо-блока — снимите её по широкому запросу"
```

- [ ] **Step 4: Убедиться, что тесты проходят**

Run: `python -m uv run pytest tests/unit/test_fixtures_sanity.py -q`
Expected: PASS, 3 passed

Если падает третий тест — фикстура снята по слишком узкому запросу. Пересснять по «менеджер» или другому широкому.

- [ ] **Step 5: Закоммитить**

```bash
python -m uv run ruff check scripts tests/unit/test_fixtures_sanity.py
git add tests/fixtures scripts/capture_dou_xhr.py tests/unit/test_fixtures_sanity.py
git commit -m "test(fixtures): живые выдачи dou (список и догрузка) и work.ua с промо-блоком"
```

---

## Task 7: Парсер dou — разбор карточки HTML-выдачи

**Files:**
- Modify: `src/jobhunt/parsers/dou.py` (содержимое заменяется целиком)
- Create: `tests/unit/test_dou_listing.py`
- Delete: `tests/unit/test_dou.py`, `tests/fixtures/xml/dou_feed.xml`

**Interfaces:**
- Consumes: `RawVacancy` (Task 4), фикстуры (Task 6)
- Produces:
  - `jobhunt.parsers.dou.DouCard` — `@dataclass(frozen=True)`: `vacancy: RawVacancy`, `is_promo: bool`
  - `parse_cards(html: str) -> tuple[list[DouCard], int]` — карточки и число неразобранных
  - `parse_total(html: str) -> int | None` — общее число вакансий из `h1`
  - `clean_url(raw: str) -> str`
  - константы `SOURCE_NAME = "dou.ua"`, `LIST_URL`, `XHR_URL`

RSS-разбор удаляется целиком вместе с `parse_item_title`. Причина в спеке, раздел 3.1: заголовок фида имеет вид `Роль в Компанія, Зарплата, Місто` с переменным числом частей, и деление по последней запятой превращает компанию в `Антенор, $1000–3000, Київ` на любом запросе, где указана зарплата. В HTML компания лежит отдельным тегом, и делить нечего.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/unit/test_dou_listing.py`:

```python
import json
from pathlib import Path

import pytest

from jobhunt.parsers.base import ParserStructureError
from jobhunt.parsers.dou import clean_url, parse_cards, parse_total

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


@pytest.fixture(scope="module")
def list_html() -> str:
    return (FIXTURES / "html" / "dou_list.html").read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def batch_html() -> str:
    data = json.loads((FIXTURES / "json" / "dou_xhr_load.json").read_text(encoding="utf-8"))
    return data["html"]


CARD = """
<li class="l-vacancy __hot">
  <div class="date">3 серпня</div>
  <div class="title">
    <a class="vt" href="https://jobs.dou.ua/companies/freitty/vacancies/363911/?from=list_hot">Senior SMM Specialist</a>
    <strong>в <a class="company" href="https://jobs.dou.ua/companies/freitty/vacancies/">FREITTY</a></strong>
    <span class="salary">$1000–2000</span>
    <span class="cities bi bi-geo-alt-fill"> віддалено</span>
  </div>
  <div class="sh-info">FREITTY — частина Octopos Holding.</div>
</li>
"""


def _wrap(inner: str) -> str:
    return f"<html><body><ul>{inner}</ul></body></html>"


def test_разбирает_все_поля_карточки():
    cards, skipped = parse_cards(_wrap(CARD))

    assert skipped == 0
    assert len(cards) == 1
    raw = cards[0].vacancy
    assert raw.source == "dou.ua"
    assert raw.external_id == "363911"
    assert raw.title == "Senior SMM Specialist"
    assert raw.company_raw == "FREITTY"
    assert raw.salary_raw == "$1000–2000"
    assert raw.location_raw == "віддалено"
    assert raw.posted_raw == "3 серпня"
    assert "Octopos Holding" in raw.description_snippet


def test_ссылка_очищается_от_трекинговых_параметров():
    """utm- и from-метки мешали бы дедупликации: одна и та же вакансия
    приходила бы с разными url в зависимости от того, где её показали."""
    cards, _ = parse_cards(_wrap(CARD))
    assert cards[0].vacancy.url == "https://jobs.dou.ua/companies/freitty/vacancies/363911/"
    assert clean_url("https://jobs.dou.ua/vacancies/1/?utm_source=x&from=list") == (
        "https://jobs.dou.ua/vacancies/1/"
    )


def test_отмечает_промо_карточки():
    """Промо-блок не упорядочен по дате, поэтому пагинация обязана уметь его
    отличать: остановка по рубежу считается только по обычным карточкам."""
    promo, _ = parse_cards(_wrap(CARD))
    assert promo[0].is_promo is True

    regular_card = CARD.replace('class="l-vacancy __hot"', 'class="l-vacancy"')
    regular, _ = parse_cards(_wrap(regular_card))
    assert regular[0].is_promo is False


def test_карточка_без_распознаваемой_ссылки_считается_пропущенной(caplog):
    """Тихо укоротить список нельзя: частичная поломка разметки должна быть
    видна, а не выглядеть как «вакансий сегодня меньше»."""
    broken = '<li class="l-vacancy"><div class="title"><a class="vt" href="/about/">Нет id</a></div></li>'
    with caplog.at_level("WARNING"):
        cards, skipped = parse_cards(_wrap(CARD + broken))

    assert len(cards) == 1
    assert skipped == 1
    assert any("не удалось разобрать" in r.message.lower() for r in caplog.records)


def test_ни_одной_разобранной_карточки_это_поломка_разметки():
    broken = '<li class="l-vacancy"><div class="title"><a class="vt" href="/about/">Нет id</a></div></li>'
    with pytest.raises(ParserStructureError, match="ни одна не разобрана"):
        parse_cards(_wrap(broken))


def test_пустая_выдача_это_легитимный_результат():
    """Ноль карточек означает «по запросу ничего не найдено», а не поломку:
    dou рендерит пустой список так же, как непустой."""
    cards, skipped = parse_cards("<html><body><ul></ul></body></html>")
    assert cards == []
    assert skipped == 0


def test_общее_число_вакансий_берётся_из_заголовка():
    assert parse_total('<h1>1401 вакансія  за запитом «менеджер»</h1>') == 1401
    assert parse_total('<h1>6 вакансій  за запитом «Head of IT»</h1>') == 6
    assert parse_total("<h1>Немає вакансій за запитом «щось»</h1>") is None
    assert parse_total("<html><body>нет заголовка</body></html>") is None


def test_разбирает_живую_фикстуру_выдачи(list_html):
    cards, skipped = parse_cards(list_html)
    assert len(cards) >= 10, f"на живой странице разобрано слишком мало карточек: {len(cards)}"
    assert skipped == 0, "часть карточек живой выдачи не разобралась"
    assert parse_total(list_html) is not None


def test_разбирает_живую_фикстуру_догрузки(batch_html):
    cards, skipped = parse_cards(batch_html)
    assert len(cards) >= 10
    assert skipped == 0
    assert all(not c.is_promo for c in cards), (
        "фикстура догрузки снята со смещением, где промо-блок ещё не кончился — "
        "пересснимите с большим offset"
    )
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/unit/test_dou_listing.py -q`
Expected: FAIL — `ImportError: cannot import name 'parse_cards' from 'jobhunt.parsers.dou'`

- [ ] **Step 3: Заменить содержимое `src/jobhunt/parsers/dou.py`**

На этом шаге пишется только разбор; класс парсера с пагинацией — в задаче 8.

```python
import logging
import re
from dataclasses import dataclass
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup, Tag

from jobhunt.parsers.base import ParserStructureError, RawVacancy

logger = logging.getLogger(__name__)

SOURCE_NAME = "dou.ua"
BASE_URL = "https://jobs.dou.ua"
LIST_URL = f"{BASE_URL}/vacancies/"
XHR_URL = f"{LIST_URL}xhr-load/"

_ID_RE = re.compile(r"/vacancies/(\d+)/")
# «1401 вакансія за запитом …». Число берётся только вплотную к слову, иначе
# в счётчик попало бы любое число со страницы.
_TOTAL_RE = re.compile(r"(\d[\d  ]*)\s*ваканс", re.IGNORECASE)


@dataclass(frozen=True)
class DouCard:
    """Карточка выдачи вместе с признаком, из промо-блока она или нет.

    Признак нужен пагинации: промо-блок не упорядочен по дате, и остановка по
    рубежу обязана считать только обычные карточки.
    """

    vacancy: RawVacancy
    is_promo: bool


def clean_url(raw: str) -> str:
    """Отбросить строку запроса целиком.

    dou.ua не кладёт в ссылки на вакансии ничего, что стоило бы сохранить
    (только utm- и from-метки), а трекинговые параметры мешают дедупликации:
    одна вакансия приходила бы с разными url в зависимости от места показа.
    """
    parts = urlsplit(raw.strip())
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def _text(node: Tag | None) -> str | None:
    if node is None:
        return None
    value = node.get_text(" ", strip=True)
    return value or None


def _card_to_raw(card: Tag) -> RawVacancy | None:
    link = card.select_one("a.vt")
    if link is None or not link.has_attr("href"):
        return None

    href = str(link["href"])
    match = _ID_RE.search(href)
    if match is None:
        return None

    return RawVacancy(
        source=SOURCE_NAME,
        external_id=match.group(1),
        title=link.get_text(" ", strip=True),
        url=clean_url(href),
        description_snippet=_text(card.select_one("div.sh-info")) or "",
        company_raw=_text(card.select_one("a.company")),
        location_raw=_text(card.select_one("span.cities")),
        salary_raw=_text(card.select_one("span.salary")),
        posted_raw=_text(card.select_one("div.date")),
    )


def parse_cards(html: str) -> tuple[list[DouCard], int]:
    """Разобрать карточки выдачи. Возвращает карточки и число неразобранных.

    Ноль карточек — легитимный результат «по запросу ничего не найдено»:
    площадка рендерит пустой список так же, как непустой. А вот карточки,
    которые есть, но ни одна не разобралась, — это поломка разметки.
    """
    soup = BeautifulSoup(html, "lxml")
    elements = soup.select("li.l-vacancy")
    if not elements:
        return [], 0

    cards: list[DouCard] = []
    skipped = 0
    for element in elements:
        vacancy = _card_to_raw(element)
        if vacancy is None:
            skipped += 1
            continue
        cards.append(DouCard(vacancy=vacancy, is_promo="__hot" in (element.get("class") or [])))

    if skipped:
        # Тихо укоротить список нельзя: частичная поломка разметки должна быть
        # видна, а не выглядеть как «вакансий сегодня меньше». Это же число
        # ниже не даёт объявить набор id полным.
        logger.warning(
            "dou.ua: не удалось разобрать %d из %d карточек выдачи — вероятно, "
            "изменилась разметка ссылки на вакансию",
            skipped,
            len(elements),
        )

    if not cards:
        raise ParserStructureError(
            f"dou.ua: карточки найдены ({len(elements)} шт.), но ни одна не разобрана — "
            "изменилась разметка"
        )
    return cards, skipped


def parse_total(html: str) -> int | None:
    """Общее число вакансий по запросу из заголовка выдачи.

    Единственный источник, сообщающий это число точно. «Немає вакансій» цифр
    не содержит и даёт None — отсутствие счётчика не выдумывается нулём.
    """
    soup = BeautifulSoup(html, "lxml")
    header = soup.select_one("h1")
    if header is None:
        return None
    match = _TOTAL_RE.search(header.get_text(" ", strip=True))
    if match is None:
        return None
    return int(match.group(1).replace(" ", "").replace(" ", ""))
```

- [ ] **Step 4: Удалить RSS-тесты и фикстуру**

```bash
git rm tests/unit/test_dou.py tests/fixtures/xml/dou_feed.xml
rmdir tests/fixtures/xml 2>/dev/null || true
```

Разбор, который они проверяли, удалён вместе с источником данных. Оставлять тесты несуществующего кода нельзя, а переносить их на HTML нечего: там нет ни деления заголовка, ни лимита фида.

- [ ] **Step 5: Убедиться, что тесты проходят**

Run: `python -m uv run pytest tests/unit/test_dou_listing.py -q`
Expected: PASS, 9 passed

Run: `python -m uv run pytest -q`
Expected: FAIL в `tests/integration/test_runner.py` — реестр парсеров создаёт `DouParser`, которого сейчас нет. Это ожидаемо и чинится задачей 8; временно отметить в реестре, что источник в перестройке, нельзя — вместо этого выполнить задачу 8 сразу следом.

- [ ] **Step 6: Закоммитить**

```bash
python -m uv run ruff check src/jobhunt/parsers/dou.py tests/unit/test_dou_listing.py
python -m uv run ruff format --check src/jobhunt/parsers/dou.py tests/unit/test_dou_listing.py
git add -A src/jobhunt/parsers/dou.py tests/unit/test_dou_listing.py tests/unit/test_dou.py tests/fixtures
git commit -m "feat(dou): разбор HTML-карточки вместо RSS — компания, зарплата и город отдельными полями"
```

---

## Task 8: Парсер dou — пагинация и остановка по рубежу

**Files:**
- Modify: `src/jobhunt/parsers/dou.py`
- Create: `tests/unit/test_dou_pagination.py`

**Interfaces:**
- Consumes: `parse_cards`, `parse_total` (Task 7), `SearchFilters`, `ParseResult` (Task 4), `HttpClient.post` (Task 5), `parse_posted_at` (Task 3)
- Produces: `DouParser(client, max_batches: int = 40, quick_batches: int = 3, today: date | None = None)` с методом `fetch_listings(query, filters) -> ParseResult`

**Правила остановки** (спека, раздел 6.5):
- промо-блок читается целиком — он не упорядочен, но конечен;
- дальше пачки по 40, пока **вся пачка целиком** не окажется старше рубежа. Не первая старая карточка: монотонность дат — наблюдение на 305 карточках, а не гарантия площадки, и локальный сбой порядка не должен обрывать сбор;
- либо `last=True`, либо потолок `max_batches`.

**Что означает `ids_complete`:** набор id полон *в пределах фильтров запроса*. Остановка по рубежу неполнотой не является — вакансии старше рубежа в рамку не входят и кандидатами на пропуск не станут. А вот упор в `max_batches` и режим `quick` неполноту дают.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/unit/test_dou_pagination.py`:

```python
import json
from datetime import date

import pytest

from jobhunt.parsers.base import SearchFilters
from jobhunt.parsers.dou import DouParser

TODAY = date(2026, 8, 4)


def _card(external_id: str, posted: str, promo: bool = False) -> str:
    cls = "l-vacancy __hot" if promo else "l-vacancy"
    return f"""
    <li class="{cls}">
      <div class="date">{posted}</div>
      <div class="title">
        <a class="vt" href="https://jobs.dou.ua/companies/x/vacancies/{external_id}/">Роль {external_id}</a>
        <strong>в <a class="company" href="#">Компанія</a></strong>
        <span class="cities">Київ</span>
      </div>
      <div class="sh-info">Опис</div>
    </li>
    """


def _page(cards: str, total: int = 500) -> str:
    return f"<html><body><h1>{total} вакансій за запитом «тест»</h1><ul>{cards}</ul></body></html>"


def _batch(cards: str, last: bool = False, num: int | None = None) -> str:
    html = f"<ul>{cards}</ul>"
    return json.dumps({"html": html, "last": last, "num": num if num is not None else 0})


class FakeClient:
    """Подменяет HttpClient: отдаёт заранее заготовленные ответы по порядку."""

    def __init__(self, page: str, batches: list[str]) -> None:
        self.page = page
        self.batches = list(batches)
        self.get_urls: list[str] = []
        self.post_calls: list[tuple[str, dict[str, str]]] = []
        self.cookies = {"csrftoken": "tok"}

    def get(self, url: str) -> str:
        self.get_urls.append(url)
        return self.page

    def post(self, url: str, data: dict[str, str], *, referer: str | None = None) -> str:
        self.post_calls.append((url, dict(data)))
        if not self.batches:
            return _batch("", last=True)
        return self.batches.pop(0)


def test_читает_первую_страницу_и_догружает_пачки():
    page = _page(_card("1", "3 серпня", promo=True) + _card("2", "3 серпня", promo=True))
    batches = [
        _batch(_card("3", "2 серпня") + _card("4", "1 серпня"), num=2),
        _batch("", last=True),
    ]
    client = FakeClient(page, batches)
    parser = DouParser(client, today=TODAY)

    result = parser.fetch_listings("тест", SearchFilters(depth_days=60))

    assert [v.external_id for v in result.vacancies] == ["1", "2", "3", "4"]
    assert result.total_available == 500
    assert result.ids_complete is True
    assert result.truncated is False


def test_останавливается_когда_вся_пачка_старше_рубежа():
    page = _page(_card("1", "3 серпня", promo=True))
    batches = [
        _batch(_card("2", "2 серпня") + _card("3", "1 серпня"), num=2),
        _batch(_card("4", "1 січня") + _card("5", "2 січня"), num=2),
        _batch(_card("6", "1 січня"), num=1),
    ]
    client = FakeClient(page, batches)
    parser = DouParser(client, today=TODAY)

    result = parser.fetch_listings("тест", SearchFilters(depth_days=30))

    ids = [v.external_id for v in result.vacancies]
    assert "4" in ids, "пачка, оборвавшая обход, всё равно должна попасть в результат"
    assert "6" not in ids, "обход не остановился на пачке, целиком вышедшей за рубеж"
    assert len(client.post_calls) == 2
    assert result.ids_complete is True, (
        "остановка по рубежу — это рамка запроса, а не неполнота набора id"
    )


def test_одна_старая_карточка_посреди_свежих_не_обрывает_обход():
    """Монотонность дат в обычном блоке — наблюдение на 305 карточках, а не
    гарантия площадки. Остановка считается по полной пачке."""
    page = _page(_card("1", "3 серпня", promo=True))
    batches = [
        _batch(_card("2", "2 серпня") + _card("3", "1 січня") + _card("4", "1 серпня"), num=3),
        _batch(_card("5", "31 липня"), num=1),
        _batch("", last=True),
    ]
    client = FakeClient(page, batches)
    parser = DouParser(client, today=TODAY)

    result = parser.fetch_listings("тест", SearchFilters(depth_days=30))

    assert "5" in [v.external_id for v in result.vacancies]


def test_промо_карточки_не_учитываются_при_остановке():
    """Промо-блок не упорядочен по дате: старая промо-карточка в свежей пачке
    не должна означать, что выдача кончилась."""
    page = _page(_card("1", "3 серпня", promo=True))
    batches = [
        _batch(_card("2", "1 січня", promo=True) + _card("3", "2 серпня"), num=2),
        _batch(_card("4", "1 серпня"), num=1),
        _batch("", last=True),
    ]
    client = FakeClient(page, batches)
    parser = DouParser(client, today=TODAY)

    result = parser.fetch_listings("тест", SearchFilters(depth_days=30))

    assert "4" in [v.external_id for v in result.vacancies]


def test_упор_в_потолок_пачек_делает_набор_id_неполным(caplog):
    page = _page(_card("1", "3 серпня", promo=True))
    batches = [_batch(_card(str(i), "3 серпня"), num=1) for i in range(2, 10)]
    client = FakeClient(page, batches)
    parser = DouParser(client, max_batches=2, today=TODAY)

    with caplog.at_level("WARNING"):
        result = parser.fetch_listings("тест", SearchFilters(depth_days=60))

    assert result.ids_complete is False
    assert result.truncated is True
    assert any("max_batches" in r.message for r in caplog.records)


def test_быстрый_режим_ограничен_и_всегда_неполон(caplog):
    page = _page(_card("1", "3 серпня", promo=True))
    batches = [_batch(_card(str(i), "3 серпня"), num=1) for i in range(2, 10)]
    client = FakeClient(page, batches)
    parser = DouParser(client, quick_batches=2, today=TODAY)

    result = parser.fetch_listings("тест", SearchFilters(depth_days=60, mode="quick"))

    assert len(client.post_calls) == 2
    assert result.ids_complete is False, (
        "быстрый режим читает только верхушку выдачи и не имеет права "
        "служить основанием для отметки пропусков"
    )


def test_передаёт_фильтры_города_и_удалёнки_в_запрос():
    page = _page(_card("1", "3 серпня", promo=True))
    client = FakeClient(page, [_batch("", last=True)])
    parser = DouParser(client, today=TODAY)

    parser.fetch_listings("тест", SearchFilters(cities=("Київ",), remote_only=True))

    url = client.get_urls[0]
    assert "search=" in url
    assert "city=" in url
    assert "remote" in url


def test_csrf_токен_берётся_из_cookie_клиента():
    page = _page(_card("1", "3 серпня", promo=True))
    client = FakeClient(page, [_batch("", last=True)])
    parser = DouParser(client, today=TODAY)

    parser.fetch_listings("тест", SearchFilters())

    assert client.post_calls[0][1]["csrfmiddlewaretoken"] == "tok"


def test_отсутствие_csrf_токена_не_роняет_прогон(caplog):
    """Без токена догрузка невозможна, но первая страница уже собрана —
    отдать её лучше, чем упасть. Неполнота при этом обязана быть видна."""
    page = _page(_card("1", "3 серпня", promo=True))
    client = FakeClient(page, [])
    client.cookies = {}
    parser = DouParser(client, today=TODAY)

    with caplog.at_level("WARNING"):
        result = parser.fetch_listings("тест", SearchFilters())

    assert [v.external_id for v in result.vacancies] == ["1"]
    assert result.ids_complete is False
    assert client.post_calls == []
    assert any("csrf" in r.message.lower() for r in caplog.records)
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/unit/test_dou_pagination.py -q`
Expected: FAIL — `ImportError: cannot import name 'DouParser' from 'jobhunt.parsers.dou'`

- [ ] **Step 3: Дописать `DouParser` в конец `src/jobhunt/parsers/dou.py`**

Добавить импорты в начало файла:

```python
import json
from datetime import UTC, date, datetime, timedelta
from urllib.parse import urlencode

from jobhunt.normalize.dates import parse_posted_at
from jobhunt.parsers.base import BaseParser, ParseResult, SearchFilters
```

`jobhunt.normalize.dates` — листовой модуль, не импортирующий ничего из проекта, поэтому цикла с `normalize/__init__.py` (который импортирует `parsers.base`) не возникает. Это зафиксировано тестом `test_листовые_модули_не_зависят_от_парсеров`.

Дописать класс:

```python
class DouParser(BaseParser):
    """Источник dou.ua поверх HTML-выдачи.

    Первая страница отдаёт 20 карточек обычным GET, дальше догрузка идёт
    POST-запросами на xhr-load с csrf-токеном из cookie: `count` — уже
    загруженное смещение, ответ — JSON {html, last, num} по 40 карточек.

    Обход останавливается, когда ВСЯ пачка целиком оказалась старше рубежа.
    Не на первой старой карточке: монотонность дат в обычном блоке —
    наблюдение на 305 карточках подряд, а не обещание площадки, и локальный
    сбой порядка не должен обрывать сбор раньше времени. Промо-карточки в
    решении об остановке не участвуют вовсе — их блок не упорядочен.
    """

    source_name = SOURCE_NAME

    def __init__(
        self,
        client,
        max_batches: int = 40,
        quick_batches: int = 3,
        today: date | None = None,
    ) -> None:
        self._client = client
        self._max_batches = max_batches
        self._quick_batches = quick_batches
        self._today = today

    def fetch_listings(self, query: str, filters: SearchFilters) -> ParseResult:
        today = self._today or datetime.now(UTC).date()
        cutoff = today - timedelta(days=filters.depth_days)

        params = self._build_params(query, filters)
        page_url = f"{LIST_URL}?{urlencode(params, doseq=True)}"
        page_html = self._client.get(page_url)

        cards, skipped = parse_cards(page_html)
        total = parse_total(page_html)
        collected = [card.vacancy for card in cards]
        any_skipped = skipped > 0
        offset = len(cards)

        limit = self._quick_batches if filters.mode == "quick" else self._max_batches
        hit_cap = False
        exhausted = not cards

        token = self._client.cookies.get("csrftoken")
        if not token and cards:
            # Без токена догрузка невозможна. Первая страница уже собрана —
            # отдать её лучше, чем упасть, но набор id при этом заведомо
            # неполон, и это обязано быть видно, а не выглядеть как «вакансий
            # ровно 20».
            logger.warning(
                "dou.ua: csrf-токен не получен, догрузка выдачи по запросу %r невозможна — "
                "собрана только первая страница",
                query,
            )
            return ParseResult(
                vacancies=collected, truncated=True, ids_complete=False, total_available=total
            )

        batches = 0
        while cards and not exhausted:
            if batches >= limit:
                hit_cap = True
                logger.warning(
                    "dou.ua: обход запроса %r остановлен на %d-й пачке из-за лимита "
                    "max_batches=%d — часть выдачи не прочитана",
                    query,
                    batches,
                    limit,
                )
                break

            payload = self._client.post(
                f"{XHR_URL}?{urlencode(params, doseq=True)}",
                data={"csrfmiddlewaretoken": token, "count": str(offset)},
                referer=page_url,
            )
            batch_cards, batch_skipped, is_last = self._parse_batch(payload, query)
            any_skipped = any_skipped or batch_skipped > 0
            collected.extend(card.vacancy for card in batch_cards)
            offset += len(batch_cards)
            batches += 1

            if not batch_cards or is_last:
                exhausted = True
                break

            if self._batch_entirely_older(batch_cards, cutoff, today):
                logger.info(
                    "dou.ua: обход запроса %r остановлен — пачка целиком старше рубежа %s",
                    query,
                    cutoff.isoformat(),
                )
                break

        # Остановка по рубежу неполнотой НЕ является: вакансии старше рубежа в
        # рамку сбора не входят и кандидатами на пропуск не станут. Неполноту
        # дают только упор в потолок, неразобранные карточки и быстрый режим,
        # который читает лишь верхушку выдачи.
        ids_complete = not hit_cap and not any_skipped and filters.mode != "quick"
        return ParseResult(
            vacancies=collected,
            truncated=hit_cap,
            ids_complete=ids_complete,
            total_available=total,
        )

    def _build_params(self, query: str, filters: SearchFilters) -> list[tuple[str, str]]:
        params: list[tuple[str, str]] = [("search", query)]
        if filters.remote_only:
            params.append(("remote", ""))
        # Площадка принимает только один город за запрос. Остальные отсеет
        # ingest локально — рамка перепроверяется целиком в любом случае.
        if filters.cities:
            params.append(("city", filters.cities[0]))
            if len(filters.cities) > 1:
                logger.warning(
                    "dou.ua: запрос %r сужен только по городу %r — площадка принимает "
                    "один город за запрос, остальные (%s) будут отсеяны локально",
                    query,
                    filters.cities[0],
                    ", ".join(filters.cities[1:]),
                )
        return params

    def _parse_batch(self, payload: str, query: str) -> tuple[list[DouCard], int, bool]:
        try:
            data = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise ParserStructureError(
                f"dou.ua: ответ догрузки не разбирается как JSON: {exc}"
            ) from exc
        html = data.get("html") or ""
        if not html.strip():
            return [], 0, True
        cards, skipped = parse_cards(html)
        return cards, skipped, bool(data.get("last"))

    def _batch_entirely_older(self, cards: list[DouCard], cutoff: date, today: date) -> bool:
        """Все ли обычные карточки пачки старше рубежа.

        Карточка без разобранной даты считается свежей: неизвестный возраст —
        не повод обрывать обход и терять то, что лежит дальше.
        """
        regular = [c for c in cards if not c.is_promo]
        if not regular:
            return False
        for card in regular:
            posted = parse_posted_at(card.vacancy.posted_raw, today)
            if posted is None or posted.date() >= cutoff:
                return False
        return True
```

- [ ] **Step 4: Обновить реестр парсеров**

`src/jobhunt/parsers/registry.py` создаёт парсеры вызовом `factory(client=client)`. Сигнатуры остались совместимыми, менять реестр не нужно — убедиться командой:

Run: `python -m uv run python -c "from jobhunt.parsers.registry import get_parser; print(get_parser('dou.ua', None))"`
Expected: `<jobhunt.parsers.dou.DouParser object at ...>`

- [ ] **Step 5: Убедиться, что тесты проходят**

Run: `python -m uv run pytest tests/unit/test_dou_pagination.py -q`
Expected: PASS, 9 passed

- [ ] **Step 6: Закоммитить**

```bash
python -m uv run ruff check src/jobhunt/parsers/dou.py tests/unit/test_dou_pagination.py
python -m uv run ruff format --check src/jobhunt/parsers/dou.py tests/unit/test_dou_pagination.py
git add src/jobhunt/parsers/dou.py tests/unit/test_dou_pagination.py
git commit -m "feat(dou): пагинация xhr-load с остановкой по рубежу даты"
```

---

## Task 9: work.ua — построение URL с фильтрами источника

**Files:**
- Modify: `src/jobhunt/parsers/work_ua.py`
- Create: `tests/unit/test_work_ua_url.py`

**Interfaces:**
- Consumes: `SearchFilters` (Task 4)
- Produces:
  - `CITY_SLUGS: dict[str, str]` — нижний регистр названия города → slug пути
  - `build_listing_url(query: str, filters: SearchFilters) -> tuple[str, dict[str, str], bool]` — `(url, params, city_applied)`
  - `DAYS_ONE_DAY = "122"` — значение фильтра «за 1 день»

**Почему URL, а не параметры.** work.ua кладёт город и признак удалёнки в путь: `/jobs-kyiv-менеджер/`, `/jobs-remote-менеджер/`. Фильтр по дате — параметром с непрозрачными значениями: `days=122` это «за 1 день», `123` — «за 7 днів», `124` — «за 14», `125` — «за 30». Числа проверены живыми запросами (спека, раздел 3.3): 944 страницы без фильтра превращаются в 210 при `days=122`.

Строить URL как `/jobs/?search=…` больше нельзя: площадка отвечает редиректом на `/jobs-…/`, и каждый запрос выдачи стоит лишнего round-trip.

**Ограничение, которое надо назвать вслух:** в путь помещается ровно один город. Если городов в рамке несколько или slug неизвестен, фильтр не применяется вовсе и отбор идёт локально в `ingest` — с предупреждением в лог, чтобы медленный прогон имел объяснение.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/unit/test_work_ua_url.py`:

```python
import pytest

from jobhunt.parsers.base import SearchFilters
from jobhunt.parsers.work_ua import build_listing_url


def test_запрос_без_фильтров_идёт_в_путь():
    """/jobs/?search=… отвечает редиректом на /jobs-…/ — каждый такой запрос
    стоил бы лишнего round-trip."""
    url, params, city_applied = build_listing_url("Head of IT", SearchFilters())

    assert url == "https://www.work.ua/jobs-Head+of+IT/"
    assert params == {}
    assert city_applied is False


def test_удалёнка_передаётся_отдельным_путём():
    url, _, _ = build_listing_url("менеджер", SearchFilters(remote_only=True))
    assert url.startswith("https://www.work.ua/jobs-remote-")


def test_известный_город_превращается_в_slug():
    url, _, city_applied = build_listing_url("менеджер", SearchFilters(cities=("Київ",)))

    assert url.startswith("https://www.work.ua/jobs-kyiv-")
    assert city_applied is True


def test_город_в_нижнем_и_верхнем_регистре_даёт_один_slug():
    first, _, _ = build_listing_url("тест", SearchFilters(cities=("КИЇВ",)))
    second, _, _ = build_listing_url("тест", SearchFilters(cities=("київ",)))
    assert first == second


def test_неизвестный_город_не_применяется_и_логируется(caplog):
    """Тихо отдать вакансии не того города недопустимо. Фильтр не применён,
    отбор идёт локально в ingest, и прогон честно объясняет, почему он дольше."""
    with caplog.at_level("WARNING"):
        url, _, city_applied = build_listing_url("тест", SearchFilters(cities=("Мукачево",)))

    assert "jobs-тест" in url or "jobs-%D1%82" in url
    assert city_applied is False
    assert any("Мукачево" in r.message for r in caplog.records)


def test_несколько_городов_не_применяются_и_логируются(caplog):
    """В путь помещается ровно один город. Взять первый и промолчать значило бы
    молча потерять остальные."""
    with caplog.at_level("WARNING"):
        _, _, city_applied = build_listing_url("тест", SearchFilters(cities=("Київ", "Львів")))

    assert city_applied is False
    assert any("нескольк" in r.message.lower() for r in caplog.records)


def test_удалёнка_имеет_приоритет_над_городом(caplog):
    """«Только удалённо» и «только Київ» одновременно в один путь не помещаются;
    удалёнка выигрывает как более сильное сужение, город отбирается локально."""
    with caplog.at_level("WARNING"):
        url, _, city_applied = build_listing_url(
            "тест", SearchFilters(cities=("Київ",), remote_only=True)
        )

    assert "jobs-remote-" in url
    assert city_applied is False


def test_быстрый_режим_добавляет_фильтр_за_один_день():
    _, params, _ = build_listing_url("тест", SearchFilters(mode="quick"))
    assert params == {"days": "122"}


def test_полный_режим_не_добавляет_фильтр_по_дате():
    """Площадка и так не отдаёт выдачу глубже 30 дней: days=125 даёт ровно те
    же 944 страницы, что и запрос без фильтра."""
    _, params, _ = build_listing_url("тест", SearchFilters(mode="full", depth_days=60))
    assert params == {}
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/unit/test_work_ua_url.py -q`
Expected: FAIL — `ImportError: cannot import name 'build_listing_url'`

- [ ] **Step 3: Реализовать**

Добавить в `src/jobhunt/parsers/work_ua.py` (импорт `quote_plus` уже есть, добавить `SearchFilters` к импортам из `base`):

```python
# Значения фильтра «Дата публікації» у work.ua непрозрачны: это не число дней,
# а идентификаторы пунктов меню. Проверено живыми запросами по «менеджер»:
# без фильтра 944 страницы, days=122 -> 210, 123 -> 648, 124 -> 736, 125 -> 944.
DAYS_ONE_DAY = "122"
DAYS_SEVEN_DAYS = "123"
DAYS_FOURTEEN_DAYS = "124"
DAYS_THIRTY_DAYS = "125"

# Города work.ua передаёт slug'ом в пути, а не параметром. Справочник заведомо
# неполон — площадка их нигде не публикует списком, эти получены из ссылок на
# самой выдаче. Неизвестный город не применяется на стороне источника вовсе.
CITY_SLUGS: dict[str, str] = {
    "київ": "kyiv",
    "киев": "kyiv",
    "львів": "lviv",
    "львов": "lviv",
    "харків": "kharkiv",
    "харьков": "kharkiv",
    "одеса": "odesa",
    "одесса": "odesa",
    "дніпро": "dnipro",
    "днепр": "dnipro",
    "запоріжжя": "zaporizhzhia",
    "вінниця": "vinnytsia",
    "полтава": "poltava",
    "тернопіль": "ternopil",
    "ужгород": "uzhhorod",
    "житомир": "zhytomyr",
    "чернівці": "chernivtsi",
    "івано-франківськ": "ivano-frankivsk",
    "хмельницький": "khmelnytskyi",
    "черкаси": "cherkasy",
    "суми": "sumy",
    "луцьк": "lutsk",
}


def build_listing_url(query: str, filters: SearchFilters) -> tuple[str, dict[str, str], bool]:
    """Собрать URL выдачи. Возвращает (url, параметры, применён ли фильтр города).

    Город и признак удалёнки у work.ua живут в пути, а не в параметрах, и в
    путь помещается ровно одно сужение. Поэтому:

    - «только удалённо» выигрывает у города: это более сильное сужение, а
      город всё равно перепроверяется локально;
    - несколько городов или неизвестный slug — фильтр не применяется вовсе.

    Тихо взять первый город из нескольких нельзя: остальные были бы молча
    потеряны, и пользователь увидел бы неполную выдачу как полную.
    """
    slug_query = quote_plus(query)
    params: dict[str, str] = {}
    if filters.mode == "quick":
        params["days"] = DAYS_ONE_DAY

    if filters.remote_only:
        if filters.cities:
            logger.warning(
                "work.ua: запрос %r сужается только по признаку удалённой работы — "
                "город и удалёнка не помещаются в путь одновременно; города (%s) "
                "будут отобраны локально",
                query,
                ", ".join(filters.cities),
            )
        return f"{BASE_URL}/jobs-remote-{slug_query}/", params, False

    if not filters.cities:
        return f"{BASE_URL}/jobs-{slug_query}/", params, False

    if len(filters.cities) > 1:
        logger.warning(
            "work.ua: запрос %r не сужен по городу — в путь помещается только один, "
            "а задано несколько (%s); отбор пойдёт локально и прогон будет дольше",
            query,
            ", ".join(filters.cities),
        )
        return f"{BASE_URL}/jobs-{slug_query}/", params, False

    city = filters.cities[0]
    slug = CITY_SLUGS.get(city.strip().lower())
    if slug is None:
        logger.warning(
            "work.ua: slug города %r неизвестен, фильтр на стороне источника не применён — "
            "отбор пойдёт локально и прогон будет дольше",
            city,
        )
        return f"{BASE_URL}/jobs-{slug_query}/", params, False

    return f"{BASE_URL}/jobs-{slug}-{slug_query}/", params, True
```

- [ ] **Step 4: Убедиться, что тесты проходят**

Run: `python -m uv run pytest tests/unit/test_work_ua_url.py -q`
Expected: PASS, 9 passed

- [ ] **Step 5: Закоммитить**

```bash
python -m uv run ruff check src/jobhunt/parsers/work_ua.py tests/unit/test_work_ua_url.py
python -m uv run ruff format --check src/jobhunt/parsers/work_ua.py tests/unit/test_work_ua_url.py
git add src/jobhunt/parsers/work_ua.py tests/unit/test_work_ua_url.py
git commit -m "feat(work.ua): фильтры источника в пути и параметрах вместо редиректа с ?search"
```

---

## Task 10: work.ua — RawVacancy, промо-блок, описания по требованию

**Files:**
- Modify: `src/jobhunt/parsers/work_ua.py`, `src/jobhunt/parsers/base.py` (удалить временный реэкспорт), `tests/unit/test_work_ua_listing.py`
- Test: `tests/unit/test_work_ua_listing.py`

**Interfaces:**
- Consumes: `build_listing_url` (Task 9), `RawVacancy`, `ParseResult`, `SearchFilters` (Task 4)
- Produces:
  - `parse_listing(html: str) -> list[RawVacancy]` — теперь сырые строки
  - `parse_total(html: str) -> int | None`
  - `WorkUaParser(client, max_pages: int = 25)` с `fetch_listings(query, filters) -> ParseResult`
  - `WorkUaParser.fetch_description(url: str) -> str` — полный текст по требованию
  - `CARDS_PER_PAGE = 14`

**Что уходит:** `max_details` и вытягивание описаний внутри `fetch_listings`. Все поля, по которым идёт фильтрация, есть в карточке; качать сотни детальных страниц ради таблицы, которая будет сужена до двух десятков строк, — плата вперёд за то, что почти наверняка не понадобится (спека, раздел 9). Разница на суточной сверке пяти тегов: ~1,5 минуты против ~10.

**Что остаётся без изменений:** `_block_with_icon`, `_extract_city`, `_next_page_url`, `parse_detail` — разметка карточки не менялась, менялся только тип результата.

- [ ] **Step 1: Переписать тесты разбора выдачи**

Заменить содержимое `tests/unit/test_work_ua_listing.py`:

```python
from pathlib import Path

import pytest

from jobhunt.parsers.base import ParserStructureError, SearchFilters
from jobhunt.parsers.work_ua import (
    CARDS_PER_PAGE,
    WorkUaParser,
    parse_listing,
    parse_total,
)

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "html"


@pytest.fixture(scope="module")
def listing_html() -> str:
    return (FIXTURES / "work_ua_list.html").read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def promo_html() -> str:
    return (FIXTURES / "work_ua_list_promo.html").read_text(encoding="utf-8")


def test_карточка_отдаётся_сырыми_строками(listing_html):
    """Парсер извлекает, но не нормализует: словарь значений один на все
    источники и живёт в отдельном слое."""
    vacancies = parse_listing(listing_html)

    assert vacancies, "на фикстуре не разобрано ни одной карточки"
    first = vacancies[0]
    assert first.source == "work.ua"
    assert first.external_id.isdigit()
    assert first.url.startswith("https://www.work.ua/jobs/")
    assert first.title
    # Сырые поля — строки как есть, без разбора
    assert first.posted_raw is None or "вакансія від" in first.posted_raw
    assert first.location_raw is None or isinstance(first.location_raw, str)


def test_зарплата_отдаётся_строкой_без_разбора(listing_html):
    vacancies = parse_listing(listing_html)
    with_salary = [v for v in vacancies if v.salary_raw]

    assert with_salary, "на фикстуре нет ни одной карточки с зарплатой"
    assert "грн" in with_salary[0].salary_raw


def test_промо_карточки_тоже_разбираются(promo_html):
    """Промо-блок игнорирует фильтры источника, но это настоящие вакансии:
    отбрасывать их в парсере нельзя, рамку перепроверяет ingest."""
    vacancies = parse_listing(promo_html)
    assert len(vacancies) >= 10


def test_пустой_контейнер_это_легитимный_результат():
    html = '<html><body><div id="pjax-jobs-list"></div></body></html>'
    assert parse_listing(html) == []


def test_отсутствие_контейнера_это_поломка_разметки():
    with pytest.raises(ParserStructureError, match="pjax-jobs-list"):
        parse_listing("<html><body>совсем другая страница</body></html>")


def test_общее_число_вакансий_оценивается_по_числу_страниц():
    html = '<html><body><div id="pjax-jobs-list"></div><span>Стор. 1 з 944</span></body></html>'
    assert parse_total(html) == 944 * CARDS_PER_PAGE


def test_отсутствие_пагинации_означает_одну_страницу():
    html = '<html><body><div id="pjax-jobs-list"></div></body></html>'
    assert parse_total(html) is None


class FakeClient:
    def __init__(self, pages: list[str]) -> None:
        self.pages = list(pages)
        self.urls: list[str] = []

    def get(self, url: str) -> str:
        self.urls.append(url)
        return self.pages.pop(0) if self.pages else "<html><body></body></html>"


def test_обход_пагинации_идёт_по_ссылке_наступна(listing_html):
    client = FakeClient([listing_html, listing_html])
    parser = WorkUaParser(client, max_pages=2)

    result = parser.fetch_listings("Head of IT", SearchFilters())

    assert len(client.urls) == 2
    assert result.vacancies


def test_упор_в_лимит_страниц_делает_набор_id_неполным(listing_html, caplog):
    client = FakeClient([listing_html, listing_html, listing_html])
    parser = WorkUaParser(client, max_pages=1)

    with caplog.at_level("WARNING"):
        result = parser.fetch_listings("Head of IT", SearchFilters())

    assert result.ids_complete is False
    assert result.truncated is True
    assert any("max_pages" in r.message for r in caplog.records)


def test_описания_при_сборе_не_качаются(listing_html):
    """Детальные страницы стоят по запросу на вакансию. Все поля фильтрации
    есть в карточке, полный текст качается по требованию."""
    client = FakeClient([listing_html])
    parser = WorkUaParser(client, max_pages=1)

    parser.fetch_listings("Head of IT", SearchFilters())

    assert all("/jobs/" in url and "jobs-" in url for url in client.urls), (
        "парсер сходил на детальную страницу во время сбора"
    )
    assert len(client.urls) == 1
```

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/unit/test_work_ua_listing.py -q`
Expected: FAIL — `ImportError: cannot import name 'CARDS_PER_PAGE'`

- [ ] **Step 3: Переписать разбор и класс парсера**

В `src/jobhunt/parsers/work_ua.py`:

Удалить функции `parse_salary`, `parse_posted_at`, `_is_standalone_word`, `_THIN_SPACES`, `_UA_WORD_CHARS`, `UA_MONTHS`, `_POSTED_RE` — их работа переехала в слой нормализации. Оставить `_block_with_icon`, `_extract_city`, `_next_page_url`, `parse_detail` без изменений.

Добавить и заменить:

```python
CARDS_PER_PAGE = 14
_PAGES_RE = re.compile(r"Стор[^\d]*(\d+)\s*з\s*(\d+)")


def parse_total(html: str) -> int | None:
    """Оценка общего числа вакансий по числу страниц пагинации.

    Точного счётчика в разметке нет, поэтому это именно оценка: число страниц
    умножается на размер страницы. Отсутствие пагинации означает единственную
    страницу, и оценивать там нечего — возвращается None, а не выдуманный ноль.
    """
    match = _PAGES_RE.search(BeautifulSoup(html, "lxml").get_text(" ", strip=True))
    if match is None:
        return None
    return int(match.group(2)) * CARDS_PER_PAGE
```

Заменить тело `_parse_listing_page`, чтобы карточка превращалась в `RawVacancy`:

```python
    vacancies: list[RawVacancy] = []
    skipped = 0
    for card in cards:
        link = card.select_one('h2 a[href^="/jobs/"]')
        if link is None:
            skipped += 1
            continue

        href = str(link["href"])
        external_id = href.strip("/").split("/")[-1]
        if not external_id.isdigit():
            skipped += 1
            continue

        salary_block = _block_with_icon(card, "glyphicon-hryvnia-fill")
        salary_raw = None
        if salary_block is not None:
            value = salary_block.select_one("span.strong-600")
            salary_raw = value.get_text(" ", strip=True) if value else None

        company_block = _block_with_icon(card, "glyphicon-company")
        company_raw = None
        location_raw = None
        if company_block is not None:
            name = company_block.select_one("span.strong-600")
            company_raw = name.get_text(" ", strip=True) if name else None
            location_raw = _extract_city(company_block)

        snippet = card.select_one("p.ellipsis-line-3")

        vacancies.append(
            RawVacancy(
                source=SOURCE_NAME,
                external_id=external_id,
                title=link.get_text(" ", strip=True),
                url=f"{BASE_URL}/jobs/{external_id}/",
                description_snippet=snippet.get_text(" ", strip=True) if snippet else "",
                company_raw=company_raw,
                location_raw=location_raw,
                salary_raw=salary_raw,
                posted_raw=str(link.get("title", "")) or None,
            )
        )
```

Заменить класс:

```python
class WorkUaParser(BaseParser):
    """Источник work.ua.

    Выдача постранична: по одному запросу отдаётся не более ~14 карточек.
    fetch_listings обходит страницы по ссылке «Наступна», пока она есть, и не
    более max_pages раз — страховка от аномально длинной выдачи (по широкому
    запросу вроде «менеджер» их 944).

    Описания при сборе не качаются вовсе. Все поля, по которым идёт
    фильтрация, есть в карточке; полный текст берётся отдельно через
    fetch_description, когда он действительно нужен.

    Досрочная остановка по дате здесь невозможна: выдача не упорядочена по
    дате ни на какой глубине (стр. 1 — 27.07, стр. 3 — 22.07 и 03.08, стр. 8 —
    31.07). Объём ограничивается фильтрами источника, а не обрывом обхода.
    """

    source_name = SOURCE_NAME

    def __init__(self, client, max_pages: int = 25) -> None:
        self._client = client
        self._max_pages = max_pages

    def fetch_listings(self, query: str, filters: SearchFilters) -> ParseResult:
        vacancies: list[RawVacancy] = []
        any_skipped = False
        cap_hit = False
        total: int | None = None

        url, params, _city_applied = build_listing_url(query, filters)
        suffix = f"?{urlencode(params)}" if params else ""
        next_url: str | None = f"{url}{suffix}"

        pages_read = 0
        while next_url is not None:
            html = self._client.get(next_url)
            if total is None:
                total = parse_total(html)

            page = _parse_listing_page(html)
            vacancies.extend(page.vacancies)
            any_skipped = any_skipped or page.skipped > 0
            pages_read += 1

            next_url = None
            if page.next_page_url is not None:
                if pages_read >= self._max_pages:
                    # Впереди ещё как минимум одна страница, но лимит достигнут:
                    # часть external_id физически не увидена, набор id перестаёт
                    # быть полным.
                    cap_hit = True
                    logger.warning(
                        "work.ua: запрос %r остановлен на странице %d из-за лимита "
                        "max_pages=%d — впереди ещё как минимум одна страница выдачи",
                        query,
                        pages_read,
                        self._max_pages,
                    )
                else:
                    next_url = urljoin(BASE_URL, page.next_page_url)

        return ParseResult(
            vacancies=vacancies,
            truncated=cap_hit,
            ids_complete=not cap_hit and not any_skipped,
            total_available=total,
        )

    def fetch_description(self, url: str) -> str:
        """Полный текст описания с детальной страницы — по требованию.

        Вызывается не при сборе, а когда описание действительно нужно: при
        открытии вакансии и при матчинге отфильтрованного набора.
        """
        return parse_detail(self._client.get(url))
```

Обновить импорты в начале файла: добавить `from urllib.parse import quote_plus, urlencode, urljoin` и `from jobhunt.parsers.base import BaseParser, ParseResult, ParserStructureError, RawVacancy, SearchFilters`.

- [ ] **Step 4: Снять `SkipValidation` с `ParseResult.vacancies`**

В задаче 4 поле объявлено как `list[SkipValidation[RawVacancy]]` — временный мост,
без которого старые парсеры, всё ещё производившие `VacancyDTO`, роняли
`pydantic.ValidationError`. Теперь оба парсера отдают `RawVacancy`, и мост обязан
исчезнуть:

```python
    vacancies: list[RawVacancy] = Field(default_factory=list)
```

**Это не косметика.** `SkipValidation` отключает проверку элементов целиком:
`ParseResult(vacancies=["строка", 12345, {}])` проходит без единой ошибки. Пока он
стоит, граница между парсером и нормализацией не защищает ни от чего, а регрессия
парсера всплывёт не понятным `ValidationError` в точке сборки результата, а
`AttributeError` внутри `normalize()`, где причина уже не видна.

Закрепить тестом в `tests/unit/test_normalize_boundaries.py`, чтобы мост не смог
вернуться незамеченным:

```python
def test_результат_парсера_валидирует_элементы():
    """SkipValidation на этом поле был временным мостом на время перевода
    парсеров на RawVacancy. Без валидации граница между парсером и нормализацией
    не ловит ничего, а ошибка всплывает уже внутри normalize(), где причина не видна."""
    import pytest
    from pydantic import ValidationError

    from jobhunt.parsers.base import ParseResult

    with pytest.raises(ValidationError):
        ParseResult(vacancies=["это не вакансия"])
```

- [ ] **Step 5: Убрать последнюю зависимость парсеров от нормализации**

Удалить строку `from jobhunt.normalize.dto import VacancyDTO` из
`src/jobhunt/parsers/work_ua.py` (в `dou.py` она исчезла вместе с RSS-разбором
в задаче 7) и из `tests/unit/test_work_ua_listing.py`.

Ни один парсер больше не производит канонических значений, и `parsers` снова
не зависит от `normalize` ни на уровне пакета, ни на уровне модуля. Убедиться
командой:

Run: `git grep -n "normalize" src/jobhunt/parsers/`
Expected: единственное совпадение — `from jobhunt.normalize.dates import parse_posted_at` в `dou.py` (листовой модуль, цикла не создаёт)

- [ ] **Step 6: Убедиться, что тесты проходят**

Run: `python -m uv run pytest tests/unit/ -q`
Expected: PASS — все юнит-тесты, включая границы парсеров и нормализации

Run: `python -m uv run pytest -q`
Expected: FAIL в `tests/integration/test_runner.py` и `tests/integration/test_upsert.py` — они вызывают `fetch_listings(query)` без `filters` и ожидают `VacancyDTO` от парсеров. Чинится задачей 11; здесь достаточно убедиться, что падают именно эти два файла и именно по сигнатуре.

- [ ] **Step 7: Закоммитить**

```bash
python -m uv run ruff check .
git add src/jobhunt/parsers/work_ua.py src/jobhunt/parsers/base.py tests/unit/test_work_ua_listing.py
git commit -m "feat(work.ua): сырые карточки вместо DTO, описания по требованию, оценка объёма выдачи"
```

---

## Task 11: Ingest на новом контракте парсеров

**Files:**
- Modify: `src/jobhunt/ingest/upsert.py`, `src/jobhunt/ingest/runner.py`, `tests/integration/test_upsert.py`, `tests/integration/test_runner.py`
- Test: те же

**Interfaces:**
- Consumes: `normalize` (Task 4), `ParseResult` с `RawVacancy` (Tasks 8, 10)
- Produces:
  - `jobhunt.ingest.normalize_batch(raws: list[RawVacancy], today: date) -> list[VacancyDTO]`
  - `run_source(session, source, query, client, filters, parser=None) -> SourceRunResult` — добавлен обязательный `filters`
  - `SourceRunResult` получает поле `total_available: int | None = None`

Эта задача восстанавливает зелёный набор тестов после смены контракта парсеров. Схема БД пока не трогается — только конвейер: парсер → нормализация → существующий `upsert`.

- [ ] **Step 1: Написать падающий тест**

Дописать в `tests/integration/test_upsert.py`:

```python
from datetime import date

from jobhunt.ingest import normalize_batch
from jobhunt.parsers.base import RawVacancy

TODAY = date(2026, 8, 4)


def test_нормализация_пачки_переводит_сырые_строки_в_канонические():
    raws = [
        RawVacancy(
            source="dou.ua",
            external_id="1",
            title="Head of IT",
            url="https://jobs.dou.ua/companies/x/vacancies/1/",
            description_snippet="Опис",
            company_raw="WayForPay",
            location_raw="віддалено",
            salary_raw="$1000–2000",
            posted_raw="3 серпня",
        )
    ]

    dtos = normalize_batch(raws, TODAY)

    assert len(dtos) == 1
    assert dtos[0].work_format == "remote"
    assert dtos[0].salary_currency == "USD"
    assert dtos[0].city is None
```

В `tests/integration/test_runner.py` привести все вызовы `run_source(...)` к новой сигнатуре, добавив `filters=SearchFilters()`, и заменить фальшивые парсеры так, чтобы их `fetch_listings` принимал два аргумента и возвращал `RawVacancy`. Пример замены фальшивого парсера:

```python
from jobhunt.parsers.base import ParseResult, RawVacancy, SearchFilters


class FakeParser:
    source_name = "work.ua"

    def __init__(self, result: ParseResult | None = None, error: Exception | None = None) -> None:
        self._result = result or ParseResult()
        self._error = error
        self.calls: list[tuple[str, SearchFilters]] = []

    def fetch_listings(self, query: str, filters: SearchFilters) -> ParseResult:
        self.calls.append((query, filters))
        if self._error is not None:
            raise self._error
        return self._result


def _raw(external_id: str, source: str = "work.ua") -> RawVacancy:
    return RawVacancy(
        source=source,
        external_id=external_id,
        title=f"Роль {external_id}",
        url=f"https://example.test/{external_id}/",
        description_snippet="Опис",
        company_raw="Компанія",
        location_raw="Київ",
        salary_raw="30 000 грн",
        posted_raw="3 серпня 2026",
    )
```

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/integration/test_upsert.py tests/integration/test_runner.py -q`
Expected: FAIL — `ImportError: cannot import name 'normalize_batch' from 'jobhunt.ingest'`

- [ ] **Step 3: Реализовать**

Создать `src/jobhunt/ingest/__init__.py` (если пуст — заменить содержимое):

```python
"""Единственный слой, который пишет вакансии в БД."""

from datetime import date

from jobhunt.normalize import VacancyDTO, normalize
from jobhunt.parsers.base import RawVacancy

__all__ = ["normalize_batch"]


def normalize_batch(raws: list[RawVacancy], today: date) -> list[VacancyDTO]:
    """Перевести пачку сырых вакансий в канонический вид.

    Отдельная функция, а не вызов normalize по месту, чтобы точка перехода из
    «строк источника» в «значения проекта» была ровно одна и её можно было
    найти поиском.
    """
    return [normalize(raw, today) for raw in raws]
```

В `src/jobhunt/ingest/runner.py` добавить `filters` в сигнатуру и прогон нормализации:

```python
def run_source(
    session: Session,
    source: str,
    query: str,
    client,
    filters: SearchFilters,
    parser: BaseParser | None = None,
    today: date | None = None,
) -> SourceRunResult:
    # Начало без изменений: parser = parser or get_parser(...), создание ParseRun
    # со status="running", session.add(run), session.flush().

    try:
        result = parser.fetch_listings(query, filters)
    except Exception as exc:  # noqa: BLE001 — намеренно: любая ошибка запроса
        # должна попасть в журнал и не оборвать прогон остальных тегов и
        # источников, а не только распознанный ParserStructureError.
        run.status = "failed"
        run.error_text = str(exc)
        run.finished_at = datetime.now(UTC)
        session.flush()
        logger.warning("%s: запрос %r завершился ошибкой — %s", source, query, exc)
        return SourceRunResult(run=run, seen_external_ids=set(), ok=False)

    # Единственная точка перехода из «строк источника» в «значения проекта».
    dtos = normalize_batch(result.vacancies, today or datetime.now(UTC).date())
    stats = upsert_vacancies(session, dtos)

    run.found_count = len(dtos)
    run.new_count = stats.new
    run.updated_count = stats.updated
    run.status = "truncated" if result.truncated else "success"
    run.ids_incomplete = not result.ids_complete
    run.finished_at = datetime.now(UTC)
    session.flush()

    seen_ids = {dto.external_id for dto in dtos}
    return SourceRunResult(
        run=run,
        seen_external_ids=seen_ids,
        ok=True,
        ids_complete=result.ids_complete,
        total_available=result.total_available,
    )
```

В `run_profile` собрать `SearchFilters` из умолчаний (рамка профиля появится в задаче 14) и передать в `run_source`:

```python
        filters = SearchFilters()
        for role in profile.target_roles:
            outcome = run_source(session, source, role, client=client, filters=filters, parser=parser)
```

Добавить в `SourceRunResult` поле `total_available: int | None = None` и заполнять его из `result.total_available`.

- [ ] **Step 4: Убедиться, что весь набор зелёный**

Run: `python -m uv run pytest -q`
Expected: PASS — все тесты, включая интеграционные

- [ ] **Step 5: Закоммитить**

```bash
python -m uv run ruff check . && python -m uv run ruff format --check .
git add src/jobhunt/ingest tests/integration/test_upsert.py tests/integration/test_runner.py
git commit -m "feat(ingest): нормализация пачки между парсером и записью в БД"
```

---

## Task 12: Нормализованные поля вакансии в БД

**Files:**
- Create: `migrations/versions/0003_normalized_vacancy_fields.py`
- Modify: `src/jobhunt/db/models.py`, `src/jobhunt/ingest/upsert.py`, `src/jobhunt/web/routes/vacancies.py`, `src/jobhunt/web/templates/vacancies.html`
- Test: `tests/integration/test_upsert.py`, `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: `VacancyDTO` (Task 4), `normalize_batch` (Task 11)
- Produces: `Vacancy` с полями `location_raw`, `city`, `city_any`, `work_format`, `description_is_full`, `description_changed_at`; `UpsertStats.changed_description` теперь наполняется осмысленно.

**Правило про описания** (спека, раздел 6.7). Сбор приносит только сниппет, полный текст качается по требованию. Без явного правила первая же суточная сверка перезаписала бы вытянутый полный текст коротким сниппетом, сбросила `description_is_full` и подняла ложный сигнал «работодатель поправил требования». Поэтому:

- `description_is_full = true` + входящий сниппет → входящий игнорируется целиком;
- сниппет → полный текст → это наше уточнение, а не правка работодателя: `description_changed_at` **не** ставится;
- полный → другой полный → это изменение, сигнал поднимается.

- [ ] **Step 1: Написать падающий тест**

Дописать в `tests/integration/test_upsert.py`:

```python
def test_нормализованные_поля_сохраняются(session):
    dto = VacancyDTO(
        source="work.ua",
        external_id="1",
        title="Керівник ІТ",
        url="https://www.work.ua/jobs/1/",
        description_raw="Опис",
        location_raw="Вишневе (Київська обл.)",
        city="Вишневе",
        city_any=False,
        work_format="onsite",
        salary_min=30000,
        salary_max=50000,
        salary_currency="UAH",
    )
    upsert_vacancies(session, [dto])

    stored = session.execute(select(Vacancy)).scalar_one()
    assert stored.location_raw == "Вишневе (Київська обл.)"
    assert stored.city == "Вишневе"
    assert stored.city_any is False
    assert stored.work_format == "onsite"


def test_сниппет_не_затирает_полное_описание(session):
    """Иначе первая же суточная сверка обесценивала бы вытянутые описания."""
    full = VacancyDTO(
        source="work.ua",
        external_id="1",
        title="Роль",
        url="https://www.work.ua/jobs/1/",
        description_raw="Полный текст вакансии на много строк",
        description_is_full=True,
    )
    upsert_vacancies(session, [full])

    snippet = full.model_copy(update={"description_raw": "Коротко…", "description_is_full": False})
    upsert_vacancies(session, [snippet])

    stored = session.execute(select(Vacancy)).scalar_one()
    assert stored.description_raw == "Полный текст вакансии на много строк"
    assert stored.description_is_full is True
    assert stored.description_changed_at is None


def test_подтягивание_полного_текста_не_считается_изменением(session):
    """Это наше уточнение, а не правка работодателя: план B строит на этом
    сигнале перескоринг, и ложное срабатывание стоило бы лишних вызовов модели."""
    snippet = VacancyDTO(
        source="work.ua",
        external_id="1",
        title="Роль",
        url="https://www.work.ua/jobs/1/",
        description_raw="Коротко…",
        description_is_full=False,
    )
    upsert_vacancies(session, [snippet])

    full = snippet.model_copy(
        update={"description_raw": "Полный текст", "description_is_full": True}
    )
    stats = upsert_vacancies(session, [full])

    stored = session.execute(select(Vacancy)).scalar_one()
    assert stored.description_raw == "Полный текст"
    assert stored.description_is_full is True
    assert stored.description_changed_at is None
    assert stats.changed_description == []


def test_смена_полного_текста_поднимает_сигнал(session):
    first = VacancyDTO(
        source="work.ua",
        external_id="1",
        title="Роль",
        url="https://www.work.ua/jobs/1/",
        description_raw="Требуется опыт 3 года",
        description_is_full=True,
    )
    upsert_vacancies(session, [first])

    changed = first.model_copy(update={"description_raw": "Требуется опыт 5 лет"})
    stats = upsert_vacancies(session, [changed])

    stored = session.execute(select(Vacancy)).scalar_one()
    assert stored.description_changed_at is not None
    assert stats.changed_description == ["1"]
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/integration/test_upsert.py -q`
Expected: FAIL — `AttributeError: type object 'Vacancy' has no attribute 'location_raw'`

- [ ] **Step 3: Изменить модель**

В `src/jobhunt/db/models.py`, класс `Vacancy`: удалить две строки —
`location: Mapped[str | None] = mapped_column(Text, nullable=True)` и
`remote_type: Mapped[str | None] = mapped_column(String(20), nullable=True)`
(строки между ними — `salary_min`, `salary_max`, `salary_currency` — остаются
без изменений), а на место `location` поставить

```python
    # Сырое значение локации хранится всегда: правило разбора может оказаться
    # неверным, и тогда переразобрать нужно будет без повторного обхода площадок.
    location_raw: Mapped[str | None] = mapped_column(Text, nullable=True)
    city: Mapped[str | None] = mapped_column(Text, nullable=True)
    # «Вся Україна» — не «город неизвестен», а «любой город»: такая вакансия
    # обязана попадать в выдачу по любому городу.
    city_any: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    work_format: Mapped[str | None] = mapped_column(String(20), nullable=True)
```

и добавить после `description_hash`:

```python
    # False означает «это сниппет из карточки выдачи». Полный текст качается по
    # требованию, и без флага сбор молча затирал бы его сниппетом.
    description_is_full: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="false"
    )
    # Когда работодатель последний раз правил описание. План B строит на этом
    # сигнале перескоринг, поэтому событие нужно начать сохранять до того, как
    # накопятся данные, — восстановить его задним числом нечем.
    description_changed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
```

Добавить индекс сортировки в `__table_args__`:

```python
    __table_args__ = (
        UniqueConstraint("source", "external_id", name="uq_vacancy_source_external"),
        Index("ix_vacancies_posted_at", "posted_at"),
    )
```

(добавить `Index` в импорты из `sqlalchemy`).

- [ ] **Step 4: Написать миграцию**

Создать `migrations/versions/0003_normalized_vacancy_fields.py`:

```python
"""normalized vacancy fields

Revision ID: 0003
Revises: 0002
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0003"
down_revision: str | Sequence[str] | None = "0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Сырое значение сохраняется переименованием, а не новой колонкой:
    # так данные не теряются и не дублируются.
    op.alter_column("vacancies", "location", new_column_name="location_raw")

    op.add_column("vacancies", sa.Column("city", sa.Text(), nullable=True))
    op.add_column(
        "vacancies",
        sa.Column("city_any", sa.Boolean(), nullable=False, server_default="false"),
    )
    op.add_column("vacancies", sa.Column("work_format", sa.String(length=20), nullable=True))
    op.add_column(
        "vacancies",
        sa.Column("description_is_full", sa.Boolean(), nullable=False, server_default="false"),
    )
    op.add_column(
        "vacancies",
        sa.Column("description_changed_at", sa.DateTime(timezone=True), nullable=True),
    )

    # remote_type заменён на work_format: старое поле заполнял только dou.ua,
    # и признак удалёнки у work.ua в него не попадал вовсе.
    op.drop_column("vacancies", "remote_type")

    op.create_index("ix_vacancies_posted_at", "vacancies", ["posted_at"])

    # Единственный backfill, который миграция делает сама: сниппет собирался
    # через get_text(" ") и переносов строк не содержит по построению, а текст
    # с детальной страницы — через get_text("\n"). Это не правило разбора, а
    # факт о том, каким кодом строка была получена, поэтому копии логики здесь
    # не возникает.
    op.execute(
        "UPDATE vacancies SET description_is_full = (position(chr(10) in description_raw) > 0)"
    )


def downgrade() -> None:
    op.drop_index("ix_vacancies_posted_at", table_name="vacancies")
    op.add_column("vacancies", sa.Column("remote_type", sa.String(length=20), nullable=True))
    op.drop_column("vacancies", "description_changed_at")
    op.drop_column("vacancies", "description_is_full")
    op.drop_column("vacancies", "work_format")
    op.drop_column("vacancies", "city_any")
    op.drop_column("vacancies", "city")
    op.alter_column("vacancies", "location_raw", new_column_name="location")
```

- [ ] **Step 5: Переписать `upsert_vacancies`**

В `src/jobhunt/ingest/upsert.py` заменить тело цикла и добавить помощник:

```python
def _apply_description(existing: Vacancy, dto: VacancyDTO, now: datetime, stats: UpsertStats) -> None:
    """Обновить описание по правилу «сниппет не затирает полный текст».

    Сбор приносит только сниппет из карточки, полный текст качается по
    требованию. Без этого правила первая же суточная сверка перезаписала бы
    вытянутый текст коротким и подняла ложный сигнал «описание изменилось».
    """
    if existing.description_is_full and not dto.description_is_full:
        return

    new_hash = description_hash(dto.description_raw)
    if existing.description_hash == new_hash:
        return

    was_full = existing.description_is_full
    existing.description_raw = dto.description_raw
    existing.description_hash = new_hash
    existing.description_is_full = dto.description_is_full

    # Подтягивание полного текста поверх сниппета — наше уточнение, а не правка
    # работодателя. Сигнал поднимается, только когда полный текст сменился полным.
    if was_full and dto.description_is_full:
        existing.description_changed_at = now
        stats.changed_description.append(dto.external_id)
```

В основном цикле: для новой вакансии добавить `description_is_full=dto.description_is_full`, `location_raw=dto.location_raw`, `city=dto.city`, `city_any=dto.city_any`, `work_format=dto.work_format` и убрать `remote_type`. Для существующей — заменить блок обновления описания вызовом `_apply_description(existing, dto, now, stats)` и заменить `existing.location = dto.location` на четыре новых поля.

- [ ] **Step 6: Обновить веб**

В `src/jobhunt/web/routes/vacancies.py`, в словаре строки заменить `"location": vacancy.location` на:

```python
                "city": vacancy.city,
                "city_any": vacancy.city_any,
                "work_format": vacancy.work_format,
```

В `src/jobhunt/web/templates/vacancies.html` заменить ячейку города:

```html
        <td>
          {% if row.work_format == "remote" %}Дистанційно
          {% elif row.city_any %}Вся Україна
          {% else %}{{ row.city or "—" }}{% endif %}
        </td>
```

Соответственно поправить ожидания в `tests/integration/test_web_vacancies.py`, где проверяется отображение города.

- [ ] **Step 7: Прогнать всё**

```bash
python -m uv run pytest -q
```
Expected: PASS, включая `tests/integration/test_migrations.py` (`alembic check` без расхождений)

Если `alembic check` находит расхождение — почти наверняка не совпадает `server_default` у `city_any` или `description_is_full`: в модели и в миграции он должен быть строкой `"false"` в обоих местах.

- [ ] **Step 8: Закоммитить**

```bash
python -m uv run ruff check . && python -m uv run ruff format --check .
git add migrations/versions/0003_normalized_vacancy_fields.py src/jobhunt/db/models.py src/jobhunt/ingest/upsert.py src/jobhunt/web tests/integration
git commit -m "feat(db): нормализованные поля вакансии и правило «сниппет не затирает полный текст»"
```

---

## Task 13: Профильная видимость вакансий

**Files:**
- Create: `migrations/versions/0004_profile_vacancies.py`
- Modify: `src/jobhunt/db/models.py`, `src/jobhunt/ingest/upsert.py`, `src/jobhunt/ingest/activity.py`, `src/jobhunt/ingest/runner.py`, `src/jobhunt/web/routes/vacancies.py`
- Test: `tests/integration/test_activity.py`, `tests/integration/test_upsert.py`, `tests/integration/test_runner.py`, `tests/integration/test_status_change.py`, `tests/integration/test_web_vacancies.py`, `tests/integration/test_models.py`

**Interfaces:**
- Consumes: схема после Task 12
- Produces:
  - `ProfileVacancy` (таблица `profile_vacancies`, бывшая `applications`) — плюс `first_seen_at`, `last_seen_at`, `missed_checks`, `last_missed_at`, `is_active`
  - `upsert_vacancies(session, dtos, profile_id) -> UpsertStats` — добавлен `profile_id`
  - `mark_missing(session, profile_id, source, seen_external_ids, threshold=2) -> int`
  - `ParseRun.profile_id`, `ParseRun.total_available`

**Почему `applications` расширяется, а не заводится вторая таблица** (спека, раздел 9): ключ у них совпадает, а план B добавит на ту же пару скор матчинга — иначе получилось бы три таблицы на один ключ.

**Почему флаги уходят с `vacancies` совсем:** «вакансия закрыта площадкой» объективно узнать нельзя — ни один профиль не видит всю биржу. Честная формулировка «этот профиль перестал её находить» профильная по определению.

- [ ] **Step 1: Написать падающий тест**

Заменить содержимое `tests/integration/test_activity.py`:

```python
from datetime import UTC, datetime, timedelta

from sqlalchemy import select

from jobhunt.db.models import Profile, ProfileVacancy, Vacancy
from jobhunt.ingest.activity import mark_missing


def _profile(session, name: str) -> Profile:
    profile = Profile(name=name, target_roles=["Роль"], locations=[])
    session.add(profile)
    session.flush()
    return profile


def _vacancy(session, external_id: str, source: str = "work.ua") -> Vacancy:
    now = datetime.now(UTC)
    vacancy = Vacancy(
        source=source,
        external_id=external_id,
        title=f"Роль {external_id}",
        url=f"https://example.test/{external_id}/",
        description_raw="Опис",
        description_hash="x" * 64,
        first_seen_at=now,
        last_seen_at=now,
    )
    session.add(vacancy)
    session.flush()
    return vacancy


def _pair(session, profile, vacancy, **overrides) -> ProfileVacancy:
    now = datetime.now(UTC)
    pair = ProfileVacancy(
        profile_id=profile.id,
        vacancy_id=vacancy.id,
        first_seen_at=now,
        last_seen_at=now,
        **overrides,
    )
    session.add(pair)
    session.flush()
    return pair


def test_не_найденная_вакансия_получает_пропуск(session):
    profile = _profile(session, "Кирилл")
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy)

    mark_missing(session, profile.id, "work.ua", {"999"})

    session.refresh(pair)
    assert pair.missed_checks == 1
    assert pair.is_active is True


def test_второй_пропуск_деактивирует(session):
    profile = _profile(session, "Кирилл")
    vacancy = _vacancy(session, "1")
    yesterday = datetime.now(UTC) - timedelta(days=1)
    pair = _pair(session, profile, vacancy, missed_checks=1, last_missed_at=yesterday)

    deactivated = mark_missing(session, profile.id, "work.ua", {"999"})

    session.refresh(pair)
    assert pair.missed_checks == 2
    assert pair.is_active is False
    assert deactivated == 1


def test_два_прогона_подряд_считаются_одним_пропуском(session):
    """Порог «2 сверки» обязан означать двое суток независимо от того, сколько
    раз нажата кнопка: иначе двойной клик закрыл бы вакансию за минуту."""
    profile = _profile(session, "Кирилл")
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy)

    mark_missing(session, profile.id, "work.ua", {"999"})
    mark_missing(session, profile.id, "work.ua", {"999"})

    session.refresh(pair)
    assert pair.missed_checks == 1
    assert pair.is_active is True


def test_чужой_профиль_не_трогается(session):
    """Ровно то, ради чего затевалась итерация: профиль с другими ролями не
    имеет права деактивировать вакансии соседа."""
    mine = _profile(session, "Кирилл")
    other = _profile(session, "Соседний")
    vacancy = _vacancy(session, "1")
    my_pair = _pair(session, mine, vacancy)
    other_pair = _pair(session, other, vacancy)

    mark_missing(session, mine.id, "work.ua", {"999"})

    session.refresh(my_pair)
    session.refresh(other_pair)
    assert my_pair.missed_checks == 1
    assert other_pair.missed_checks == 0


def test_пустая_выдача_не_засчитывает_пропусков(session, caplog):
    """Пустой результат почти всегда значит сломанный парсер или слишком узкий
    запрос, а не опустевшую биржу."""
    profile = _profile(session, "Кирилл")
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy)

    with caplog.at_level("WARNING"):
        assert mark_missing(session, profile.id, "work.ua", set()) == 0

    session.refresh(pair)
    assert pair.missed_checks == 0
    assert any("ноль вакансий" in r.message for r in caplog.records)


def test_другой_источник_не_трогается(session):
    profile = _profile(session, "Кирилл")
    vacancy = _vacancy(session, "1", source="dou.ua")
    pair = _pair(session, profile, vacancy)

    mark_missing(session, profile.id, "work.ua", {"999"})

    session.refresh(pair)
    assert pair.missed_checks == 0


def test_повторная_встреча_воскрешает(session):
    from jobhunt.ingest.upsert import upsert_vacancies
    from jobhunt.normalize import VacancyDTO

    profile = _profile(session, "Кирилл")
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy, missed_checks=2, is_active=False)

    upsert_vacancies(
        session,
        [
            VacancyDTO(
                source="work.ua",
                external_id="1",
                title="Роль 1",
                url="https://example.test/1/",
                description_raw="Опис",
            )
        ],
        profile_id=profile.id,
    )

    session.refresh(pair)
    assert pair.missed_checks == 0
    assert pair.last_missed_at is None
    assert pair.is_active is True
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/integration/test_activity.py -q`
Expected: FAIL — `ImportError: cannot import name 'ProfileVacancy'`

- [ ] **Step 3: Изменить модели**

В `src/jobhunt/db/models.py`:

Из `Vacancy` удалить `missed_runs` и `is_active`.

Переименовать класс `Application` в `ProfileVacancy` и переписать:

```python
class ProfileVacancy(Base):
    """Всё, что профиль знает про вакансию: и что видел её, и как на неё ответил.

    Одна таблица, а не две, потому что ключ у них совпадает, а план B добавит
    на ту же пару скор матчинга — иначе вышло бы три таблицы на один ключ.
    Объективное «профиль видел это в выдаче» и субъективное «я откликнулся»
    разводятся фильтром по статусу, а не разными таблицами.

    Строка создаётся сборщиком при первой встрече, а не пользователем при
    смене статуса: благодаря этому "new" — настоящее сохранённое состояние, а
    не «строки нет, значит new».
    """

    __tablename__ = "profile_vacancies"
    __table_args__ = (
        UniqueConstraint("profile_id", "vacancy_id", name="uq_profile_vacancy"),
        Index("ix_profile_vacancies_profile_id", "profile_id"),
    )

    id: Mapped[uuid.UUID] = _uuid_pk()
    profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("profiles.id", ondelete="CASCADE"))
    vacancy_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vacancies.id", ondelete="CASCADE"))

    status: Mapped[str] = mapped_column(String(20), default="new", server_default="new", index=True)
    applied_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    responded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    first_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    last_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    missed_checks: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    # Когда пропуск был засчитан в последний раз. Нужен, чтобы два прогона
    # подряд не сошли за двое суток: порог «2 сверки» обязан означать время, а
    # не число нажатий кнопки.
    last_missed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true", index=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
```

В `ParseRun` добавить:

```python
    profile_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("profiles.id", ondelete="CASCADE"), nullable=True
    )
    # Сколько источник заявил всего. Даёт строке «собрано 300 из 13 216»
    # опору на факт, а не на догадку.
    total_available: Mapped[int | None] = mapped_column(Integer, nullable=True)
```

- [ ] **Step 4: Написать миграцию**

Создать `migrations/versions/0004_profile_vacancies.py`:

```python
"""profile-scoped vacancy visibility

Revision ID: 0004
Revises: 0003
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0004"
down_revision: str | Sequence[str] | None = "0003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.rename_table("applications", "profile_vacancies")
    op.execute("ALTER INDEX uq_application_profile_vacancy RENAME TO uq_profile_vacancy")

    # Даты и счётчики добавляются nullable, заполняются, и только потом
    # становятся обязательными: иначе NOT NULL упал бы на существующих строках.
    op.add_column(
        "profile_vacancies", sa.Column("first_seen_at", sa.DateTime(timezone=True), nullable=True)
    )
    op.add_column(
        "profile_vacancies", sa.Column("last_seen_at", sa.DateTime(timezone=True), nullable=True)
    )
    op.add_column(
        "profile_vacancies",
        sa.Column("missed_checks", sa.Integer(), nullable=False, server_default="0"),
    )
    op.add_column(
        "profile_vacancies", sa.Column("last_missed_at", sa.DateTime(timezone=True), nullable=True)
    )
    op.add_column(
        "profile_vacancies",
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
    )
    op.create_index("ix_profile_vacancies_is_active", "profile_vacancies", ["is_active"])
    op.create_index("ix_profile_vacancies_profile_id", "profile_vacancies", ["profile_id"])

    # Backfill: строка пары на каждую уже собранную вакансию для каждого
    # профиля. Профиль в базе один, но запрос написан общо — на двух профилях
    # он даст обоим одинаковую отправную точку, что честно: обе картины
    # получены одним и тем же прогоном.
    op.execute(
        """
        INSERT INTO profile_vacancies
            (id, profile_id, vacancy_id, status, first_seen_at, last_seen_at,
             missed_checks, is_active, created_at, updated_at)
        SELECT gen_random_uuid(), p.id, v.id, 'new', v.first_seen_at, v.last_seen_at,
               v.missed_runs, v.is_active, now(), now()
        FROM vacancies v
        CROSS JOIN profiles p
        WHERE NOT EXISTS (
            SELECT 1 FROM profile_vacancies pv
            WHERE pv.profile_id = p.id AND pv.vacancy_id = v.id
        )
        """
    )
    # Строки, существовавшие до миграции (пользователь ставил статус), дат не
    # имели — берём их из самой вакансии.
    op.execute(
        """
        UPDATE profile_vacancies pv
        SET first_seen_at = COALESCE(pv.first_seen_at, v.first_seen_at),
            last_seen_at = COALESCE(pv.last_seen_at, v.last_seen_at),
            missed_checks = v.missed_runs,
            is_active = v.is_active
        FROM vacancies v
        WHERE v.id = pv.vacancy_id
        """
    )
    op.alter_column("profile_vacancies", "first_seen_at", nullable=False)
    op.alter_column("profile_vacancies", "last_seen_at", nullable=False)

    op.drop_column("vacancies", "missed_runs")
    op.drop_column("vacancies", "is_active")

    op.add_column(
        "parse_runs",
        sa.Column("profile_id", sa.UUID(as_uuid=True), nullable=True),
    )
    op.create_foreign_key(
        "fk_parse_runs_profile", "parse_runs", "profiles", ["profile_id"], ["id"],
        ondelete="CASCADE",
    )
    op.add_column("parse_runs", sa.Column("total_available", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("parse_runs", "total_available")
    op.drop_constraint("fk_parse_runs_profile", "parse_runs", type_="foreignkey")
    op.drop_column("parse_runs", "profile_id")

    op.add_column(
        "vacancies", sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true")
    )
    op.add_column(
        "vacancies", sa.Column("missed_runs", sa.Integer(), nullable=False, server_default="0")
    )
    op.drop_index("ix_profile_vacancies_profile_id", table_name="profile_vacancies")
    op.drop_index("ix_profile_vacancies_is_active", table_name="profile_vacancies")
    for column in ("is_active", "last_missed_at", "missed_checks", "last_seen_at", "first_seen_at"):
        op.drop_column("profile_vacancies", column)
    op.execute("ALTER INDEX uq_profile_vacancy RENAME TO uq_application_profile_vacancy")
    op.rename_table("profile_vacancies", "applications")
```

`gen_random_uuid()` доступен в PostgreSQL 13+ без расширений; проект стоит на 17.

- [ ] **Step 5: Переписать `mark_missing`**

Заменить `src/jobhunt/ingest/activity.py`:

```python
import logging
import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import ProfileVacancy, Vacancy

logger = logging.getLogger(__name__)

MISSED_CHECKS_THRESHOLD = 2
# Минимальный промежуток между засчитанными пропусками. Порог «2 сверки»
# обязан означать двое суток независимо от того, сколько раз запущен сбор:
# без этой защиты двойной клик по кнопке закрыл бы вакансию за минуту.
MIN_INTERVAL = timedelta(hours=20)


def mark_missing(
    session: Session,
    profile_id: uuid.UUID,
    source: str,
    seen_external_ids: set[str],
    threshold: int = MISSED_CHECKS_THRESHOLD,
    now: datetime | None = None,
) -> int:
    """Засчитать пропуск вакансиям профиля, не встреченным в этой сверке.

    Судит только про один профиль: «вакансия закрыта площадкой» объективно
    узнать нельзя — ни один профиль не видит всю биржу. Честная формулировка
    «этот профиль перестал её находить» профильная по определению.

    Сброс счётчика при повторной встрече — забота upsert_vacancies, здесь
    только движение в одну сторону.
    """
    if not seen_external_ids:
        # Полностью пустая выдача почти всегда значит поломку парсера или
        # слишком узкий запрос, а не опустевшую площадку. Если засчитывать её
        # как пропуск, несколько неудачных прогонов молча деактивировали бы
        # весь источник.
        logger.warning(
            "%s: сверка вернула ноль вакансий — пропуски не засчитаны, похоже "
            "на поломку парсера или слишком узкий запрос",
            source,
        )
        return 0

    moment = now or datetime.now(UTC)
    rows = session.execute(
        select(ProfileVacancy, Vacancy)
        .join(Vacancy, Vacancy.id == ProfileVacancy.vacancy_id)
        .where(
            ProfileVacancy.profile_id == profile_id,
            ProfileVacancy.is_active.is_(True),
            Vacancy.source == source,
        )
    ).all()

    deactivated: list[str] = []
    for pair, vacancy in rows:
        if vacancy.external_id in seen_external_ids:
            continue
        if pair.last_missed_at is not None and moment - pair.last_missed_at < MIN_INTERVAL:
            continue
        pair.missed_checks += 1
        pair.last_missed_at = moment
        if pair.missed_checks >= threshold:
            pair.is_active = False
            deactivated.append(vacancy.external_id)

    if deactivated:
        # Деактивация — тихое, но значимое изменение: без лога о нём узнают
        # только выборочным просмотром базы.
        logger.warning(
            "%s: деактивировано %d вакансий после %d пропущенных сверок: %s",
            source,
            len(deactivated),
            threshold,
            ", ".join(deactivated),
        )

    session.flush()
    return len(deactivated)
```

- [ ] **Step 6: Провести `profile_id` через upsert, runner и веб**

`upsert_vacancies(session, dtos, profile_id)`: после вставки/обновления вакансии находит или создаёт `ProfileVacancy` и ставит `last_seen_at = now`, `missed_checks = 0`, `last_missed_at = None`, `is_active = True`; для новой пары `first_seen_at = now`.

`runner.run_source` и `run_profile` передают `profile.id` в `upsert_vacancies` и `mark_missing`, а также заполняют `run.profile_id` и `run.total_available`.

`web/routes/vacancies.py`: `Application` → `ProfileVacancy`, а фильтр активности переезжает на пару:

```python
    query = (
        select(Vacancy, ProfileVacancy.status)
        .join(ProfileVacancy, ProfileVacancy.vacancy_id == Vacancy.id)
        .where(ProfileVacancy.profile_id == profile_id)
        .order_by(Vacancy.posted_at.desc().nulls_last(), Vacancy.first_seen_at.desc())
    )
    if not include_inactive:
        query = query.where(ProfileVacancy.is_active.is_(True))
```

Внешнее соединение больше не нужно: строка пары теперь есть у каждой видимой профилю вакансии.

Обновить `tests/integration/test_status_change.py`, `test_web_vacancies.py`, `test_models.py`, `test_runner.py`, `test_upsert.py` под новые имена и сигнатуры. В `test_migrations.py` заменить `EXPECTED_TABLES` на `{"profiles", "vacancies", "profile_vacancies", "parse_runs"}`.

- [ ] **Step 7: Прогнать всё**

```bash
python -m uv run pytest -q
```
Expected: PASS

- [ ] **Step 8: Закоммитить**

```bash
python -m uv run ruff check . && python -m uv run ruff format --check .
git add -A
git commit -m "feat(db): видимость и деактивация вакансий по профилю вместо привязки к источнику"
```

---

## Task 14: Теги ролей и связь «каким тегом найдена вакансия»

**Files:**
- Create: `migrations/versions/0005_profile_tags.py`, `tests/integration/test_tags.py`
- Modify: `src/jobhunt/db/models.py`, `src/jobhunt/ingest/upsert.py`, `src/jobhunt/ingest/runner.py`, `src/jobhunt/web/routes/vacancies.py`, `src/jobhunt/web/templates/vacancies.html`

**Interfaces:**
- Consumes: схема после Task 13
- Produces:
  - `ProfileTag` (таблица `profile_tags`): `id`, `profile_id`, `text`, `is_enabled`, `created_at`; уникальность `(profile_id, text)`
  - `ProfileVacancyTag` (таблица `profile_vacancy_tags`): `profile_vacancy_id`, `tag_id` — составной первичный ключ, обе ссылки `ondelete="CASCADE"`
  - `upsert_vacancies(session, dtos, profile_id, tag_id) -> UpsertStats` — добавлен `tag_id`
  - `jobhunt.ingest.tags.link_tag(session, profile_vacancy_id, tag_id) -> None` — идемпотентно

**Почему тег — строка таблицы, а не элемент массива:** вакансии на него ссылаются, а строковая ссылка ломается при первом переименовании.

**Почему каскад:** удалили тег → связки исчезли → у вакансии не осталось тегов → она сирота и уходит в псевдо-фильтр «Найденные ранее». Отдельного кода для сирот писать не нужно.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/integration/test_tags.py`:

```python
from datetime import UTC, datetime

from sqlalchemy import select

from jobhunt.db.models import Profile, ProfileTag, ProfileVacancy, ProfileVacancyTag
from jobhunt.ingest.upsert import upsert_vacancies
from jobhunt.normalize import VacancyDTO


def _profile(session) -> Profile:
    profile = Profile(name="Кирилл", locations=[])
    session.add(profile)
    session.flush()
    return profile


def _tag(session, profile, text: str, enabled: bool = True) -> ProfileTag:
    tag = ProfileTag(profile_id=profile.id, text=text, is_enabled=enabled)
    session.add(tag)
    session.flush()
    return tag


def _dto(external_id: str = "1") -> VacancyDTO:
    return VacancyDTO(
        source="work.ua",
        external_id=external_id,
        title=f"Роль {external_id}",
        url=f"https://www.work.ua/jobs/{external_id}/",
        description_raw="Опис",
    )


def test_вакансия_связывается_с_тегом_которым_найдена(session):
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT")

    upsert_vacancies(session, [_dto()], profile_id=profile.id, tag_id=tag.id)

    links = session.execute(select(ProfileVacancyTag)).scalars().all()
    assert len(links) == 1
    assert links[0].tag_id == tag.id


def test_одна_вакансия_двумя_тегами_даёт_одну_строку_и_две_связки(session):
    """Это норма, а не дубликат: выключите один тег — вакансия останется
    видна по второму."""
    profile = _profile(session)
    first = _tag(session, profile, "Head of IT")
    second = _tag(session, profile, "IT Director")

    upsert_vacancies(session, [_dto()], profile_id=profile.id, tag_id=first.id)
    upsert_vacancies(session, [_dto()], profile_id=profile.id, tag_id=second.id)

    pairs = session.execute(select(ProfileVacancy)).scalars().all()
    links = session.execute(select(ProfileVacancyTag)).scalars().all()
    assert len(pairs) == 1
    assert {link.tag_id for link in links} == {first.id, second.id}


def test_повторный_сбор_тем_же_тегом_не_дублирует_связку(session):
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT")

    upsert_vacancies(session, [_dto()], profile_id=profile.id, tag_id=tag.id)
    upsert_vacancies(session, [_dto()], profile_id=profile.id, tag_id=tag.id)

    links = session.execute(select(ProfileVacancyTag)).scalars().all()
    assert len(links) == 1


def test_удаление_тега_делает_вакансию_сиротой_а_не_удаляет_её(session):
    """Удаление необратимо, скрытие — нет. У вакансии может быть отклик и
    история наблюдений: это данные пользователя, а не площадки."""
    profile = _profile(session)
    tag = _tag(session, profile, "Head of IT")
    upsert_vacancies(session, [_dto()], profile_id=profile.id, tag_id=tag.id)

    session.delete(tag)
    session.flush()

    assert session.execute(select(ProfileVacancyTag)).scalars().all() == []
    assert len(session.execute(select(ProfileVacancy)).scalars().all()) == 1


def test_уникальность_тега_в_пределах_профиля(session):
    import pytest
    from sqlalchemy.exc import IntegrityError

    profile = _profile(session)
    _tag(session, profile, "Head of IT")
    with pytest.raises(IntegrityError):
        _tag(session, profile, "Head of IT")
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/integration/test_tags.py -q`
Expected: FAIL — `ImportError: cannot import name 'ProfileTag'`

- [ ] **Step 3: Добавить модели**

В `src/jobhunt/db/models.py`:

```python
class ProfileTag(Base):
    """Тег предпочитаемой роли: он же поисковый запрос к источникам.

    Отдельная строка с идентификатором, а не элемент массива в профиле:
    вакансии ссылаются на тег, а строковая ссылка ломается при первом же
    переименовании.

    Выключенный тег не удаляется и по нему не ищут: найденные им вакансии
    просто перестают быть видимыми и никогда не попадают в кандидаты на
    пропуск — мы по нему не искали и не имеем оснований судить.
    """

    __tablename__ = "profile_tags"
    __table_args__ = (UniqueConstraint("profile_id", "text", name="uq_profile_tag_text"),)

    id: Mapped[uuid.UUID] = _uuid_pk()
    profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("profiles.id", ondelete="CASCADE"))
    text: Mapped[str] = mapped_column(Text)
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class ProfileVacancyTag(Base):
    """Каким тегом найдена вакансия у этого профиля.

    Каскадное удаление с обеих сторон даёт бесплатную обработку сирот: удалили
    тег — связки исчезли — у вакансии не осталось тегов — она попадает в
    псевдо-фильтр «Найденные ранее».
    """

    __tablename__ = "profile_vacancy_tags"

    profile_vacancy_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("profile_vacancies.id", ondelete="CASCADE"), primary_key=True
    )
    tag_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("profile_tags.id", ondelete="CASCADE"), primary_key=True
    )
```

Из `Profile` удалить `target_roles`.

- [ ] **Step 4: Написать миграцию**

Создать `migrations/versions/0005_profile_tags.py`:

```python
"""role tags and vacancy-tag links

Revision ID: 0005
Revises: 0004
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0005"
down_revision: str | Sequence[str] | None = "0004"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "profile_tags",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "profile_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("profiles.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("is_enabled", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.UniqueConstraint("profile_id", "text", name="uq_profile_tag_text"),
    )
    op.create_table(
        "profile_vacancy_tags",
        sa.Column(
            "profile_vacancy_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("profile_vacancies.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "tag_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("profile_tags.id", ondelete="CASCADE"),
            primary_key=True,
        ),
    )

    # Каждый элемент target_roles становится включённым тегом.
    op.execute(
        """
        INSERT INTO profile_tags (id, profile_id, text, is_enabled, created_at)
        SELECT gen_random_uuid(), p.id, role, true, now()
        FROM profiles p, unnest(p.target_roles) AS role
        """
    )
    # Какой тег какую вакансию нашёл, мы не знаем — связываем со всеми.
    # Это заведомое приближение, и оно самоисправляется после первой полной
    # сверки: она пересобирает связки того тега, по которому шла (см. задачу 17).
    op.execute(
        """
        INSERT INTO profile_vacancy_tags (profile_vacancy_id, tag_id)
        SELECT pv.id, t.id
        FROM profile_vacancies pv
        JOIN profile_tags t ON t.profile_id = pv.profile_id
        ON CONFLICT DO NOTHING
        """
    )

    op.drop_column("profiles", "target_roles")


def downgrade() -> None:
    op.add_column(
        "profiles",
        sa.Column("target_roles", sa.ARRAY(sa.Text()), nullable=False, server_default="{}"),
    )
    op.execute(
        """
        UPDATE profiles p
        SET target_roles = COALESCE(
            (SELECT array_agg(t.text) FROM profile_tags t WHERE t.profile_id = p.id), '{}'
        )
        """
    )
    op.drop_table("profile_vacancy_tags")
    op.drop_table("profile_tags")
```

- [ ] **Step 5: Проставлять связку в `ingest`**

Создать `src/jobhunt/ingest/tags.py`:

```python
import uuid

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from jobhunt.db.models import ProfileVacancyTag


def link_tag(session: Session, profile_vacancy_id: uuid.UUID, tag_id: uuid.UUID) -> None:
    """Отметить, что вакансия найдена этим тегом.

    Идемпотентно: одна и та же вакансия находится одним тегом при каждом
    сборе, и это норма, а не ошибка. Вставка с игнорированием конфликта
    дешевле предварительного SELECT на каждую вакансию.
    """
    session.execute(
        insert(ProfileVacancyTag)
        .values(profile_vacancy_id=profile_vacancy_id, tag_id=tag_id)
        .on_conflict_do_nothing()
    )
```

В `upsert_vacancies` добавить параметр `tag_id: uuid.UUID | None = None` и вызывать `link_tag(session, pair.id, tag_id)` после создания/обновления пары, если `tag_id` задан.

В `runner.run_profile` итерировать по `session.execute(select(ProfileTag).where(ProfileTag.profile_id == profile.id, ProfileTag.is_enabled.is_(True)))` вместо `profile.target_roles`, передавая `tag.text` как запрос и `tag.id` в `upsert_vacancies`.

- [ ] **Step 6: Показать теги в таблице**

В `web/routes/vacancies.py` добавить в строку список текстов тегов этой пары (подзапросом или отдельной выборкой связок по всем показанным парам — одним запросом, а не по строке на вакансию), в шаблоне — колонку «Теги».

- [ ] **Step 7: Прогнать всё и закоммитить**

```bash
python -m uv run pytest -q
python -m uv run ruff check . && python -m uv run ruff format --check .
git add -A
git commit -m "feat(db): теги ролей отдельной сущностью и связь «каким тегом найдена вакансия»"
```

---

## Task 15: Рамка сбора в настройках профиля

**Files:**
- Create: `migrations/versions/0006_collection_scope.py`, `tests/integration/test_scope_filter.py`
- Modify: `src/jobhunt/db/models.py`, `src/jobhunt/ingest/__init__.py`, `src/jobhunt/ingest/runner.py`

**Interfaces:**
- Consumes: `SearchFilters` (Task 4), `VacancyDTO` (Task 4)
- Produces:
  - `Profile.collection_cities: list[str]`, `Profile.collection_remote_only: bool`, `Profile.collection_depth_days: int` (по умолчанию 60)
  - `jobhunt.ingest.scope.filters_for(profile, mode) -> SearchFilters`
  - `jobhunt.ingest.scope.within_scope(dto, profile, today) -> bool`
  - `jobhunt.ingest.scope.select_in_scope(dtos, profile, today) -> list[VacancyDTO]` — отбирает и логирует, сколько отброшено

**Ключевое правило** (спека, раздел 6.3): фильтры источника — только способ уменьшить объём, **истиной является локальная проверка**. `ingest` применяет всю рамку целиком независимо от того, что парсер передал сайту. Причина: промо-блок work.ua приходит мимо любых фильтров, а сам фильтр `days` при первой проверке выглядел неработающим. Ошибиться можно в обе стороны, и вторая ошибка — счесть фильтр применённым, когда он молча не сработал — тихая.

- [ ] **Step 1: Написать падающий тест**

Создать `tests/integration/test_scope_filter.py`:

```python
from datetime import UTC, date, datetime, timedelta

from jobhunt.db.models import Profile
from jobhunt.ingest.scope import filters_for, select_in_scope, within_scope
from jobhunt.normalize import VacancyDTO

TODAY = date(2026, 8, 4)


def _profile(**overrides) -> Profile:
    base = {
        "name": "Кирилл",
        "locations": [],
        "collection_cities": [],
        "collection_remote_only": False,
        "collection_depth_days": 60,
    }
    base.update(overrides)
    return Profile(**base)


def _dto(**overrides) -> VacancyDTO:
    base = {
        "source": "work.ua",
        "external_id": "1",
        "title": "Роль",
        "url": "https://www.work.ua/jobs/1/",
        "description_raw": "Опис",
        "city": "Київ",
        "city_any": False,
        "work_format": "onsite",
        "posted_at": datetime(2026, 8, 3, tzinfo=UTC),
    }
    base.update(overrides)
    return VacancyDTO(**base)


def test_пустая_рамка_пропускает_всё():
    assert within_scope(_dto(), _profile(), TODAY) is True


def test_рамка_по_городу_отсекает_чужие_города():
    profile = _profile(collection_cities=["Київ"])
    assert within_scope(_dto(city="Київ"), profile, TODAY) is True
    assert within_scope(_dto(city="Львів"), profile, TODAY) is False


def test_любой_город_проходит_любой_фильтр_города():
    """«Вся Україна» означает «любой город», а не «город неизвестен»."""
    profile = _profile(collection_cities=["Львів"])
    assert within_scope(_dto(city=None, city_any=True), profile, TODAY) is True


def test_неизвестное_не_отсекается():
    """Фильтр отсекает то, что противоречит запросу, а не то, что его просто
    не подтверждает."""
    profile = _profile(collection_remote_only=True)
    assert within_scope(_dto(work_format=None), profile, TODAY) is True
    assert within_scope(_dto(work_format="onsite"), profile, TODAY) is False
    assert within_scope(_dto(work_format="remote"), profile, TODAY) is True


def test_вакансия_старше_глубины_не_попадает_в_рамку():
    profile = _profile(collection_depth_days=30)
    old = datetime.now(UTC) - timedelta(days=40)
    assert within_scope(_dto(posted_at=old), profile, TODAY) is False


def test_вакансия_без_даты_остаётся_в_рамке():
    profile = _profile(collection_depth_days=30)
    assert within_scope(_dto(posted_at=None), profile, TODAY) is True


def test_отбор_считает_и_логирует_отброшенные(caplog):
    profile = _profile(collection_cities=["Київ"])
    dtos = [_dto(external_id="1", city="Київ"), _dto(external_id="2", city="Львів")]

    with caplog.at_level("WARNING"):
        kept = select_in_scope(dtos, profile, TODAY)

    assert [d.external_id for d in kept] == ["1"]
    assert any("вне рамки" in r.message for r in caplog.records)


def test_фильтры_запроса_строятся_из_профиля():
    profile = _profile(collection_cities=["Київ"], collection_remote_only=True, collection_depth_days=45)
    filters = filters_for(profile, mode="quick")

    assert filters.cities == ("Київ",)
    assert filters.remote_only is True
    assert filters.depth_days == 45
    assert filters.mode == "quick"
```

- [ ] **Step 2: Убедиться, что тест падает**

Run: `python -m uv run pytest tests/integration/test_scope_filter.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.ingest.scope'`

- [ ] **Step 3: Реализовать**

В `Profile` добавить:

```python
    collection_cities: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    collection_remote_only: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="false"
    )
    # Граница сбора, а не обязательство следить за вакансией столько дней.
    # У work.ua упрётся в 30: глубже площадка в выдаче не показывает.
    collection_depth_days: Mapped[int] = mapped_column(Integer, default=60, server_default="60")
```

Создать `src/jobhunt/ingest/scope.py`:

```python
import logging
from datetime import UTC, date, datetime, timedelta

from jobhunt.db.models import Profile
from jobhunt.normalize import VacancyDTO
from jobhunt.parsers.base import SearchFilters

logger = logging.getLogger(__name__)


def filters_for(profile: Profile, mode: str = "full") -> SearchFilters:
    """Собрать фильтры запроса из рамки профиля."""
    return SearchFilters(
        cities=tuple(profile.collection_cities or ()),
        remote_only=bool(profile.collection_remote_only),
        depth_days=int(profile.collection_depth_days),
        mode=mode,
    )


def within_scope(dto: VacancyDTO, profile: Profile, today: date) -> bool:
    """Попадает ли вакансия в рамку сбора профиля.

    Правило одно на все оси: рамка отсекает то, что ей ПРОТИВОРЕЧИТ, но не то,
    что её просто не подтверждает. Неизвестный формат работы или отсутствующая
    дата — не повод прятать вакансию.
    """
    if profile.collection_remote_only and dto.work_format not in (None, "remote"):
        return False

    cities = profile.collection_cities or []
    if cities and not dto.city_any:
        # city_any («Вся Україна») означает «любой город» и проходит любой
        # фильтр города. None означает «не знаем» и тоже не отсекается.
        if dto.city is not None and dto.city not in cities:
            return False

    if dto.posted_at is not None:
        cutoff = datetime.now(UTC) - timedelta(days=int(profile.collection_depth_days))
        if dto.posted_at < cutoff:
            return False

    return True


def select_in_scope(dtos: list[VacancyDTO], profile: Profile, today: date) -> list[VacancyDTO]:
    """Отобрать вакансии внутри рамки, сообщив, сколько отброшено.

    Проверка делается локально всегда, даже если парсер уже передал фильтры
    источнику. Промо-блок work.ua приходит мимо любых фильтров, а сам фильтр
    может молча не сработать — и такая ошибка тихая. Двойная проверка стоит
    одного условия на вакансию.
    """
    kept = [dto for dto in dtos if within_scope(dto, profile, today)]
    dropped = len(dtos) - len(kept)
    if dropped:
        logger.warning(
            "отброшено %d из %d вакансий вне рамки сбора профиля %r "
            "(города: %s, только удалённо: %s, глубина: %d дн.)",
            dropped,
            len(dtos),
            profile.name,
            ", ".join(profile.collection_cities) or "любые",
            profile.collection_remote_only,
            profile.collection_depth_days,
        )
    return kept
```

Создать `migrations/versions/0006_collection_scope.py`:

```python
"""profile collection scope

Revision ID: 0006
Revises: 0005
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0006"
down_revision: str | Sequence[str] | None = "0005"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column("profiles", "locations", new_column_name="collection_cities")
    op.add_column(
        "profiles",
        sa.Column("collection_remote_only", sa.Boolean(), nullable=False, server_default="false"),
    )
    op.add_column(
        "profiles",
        sa.Column("collection_depth_days", sa.Integer(), nullable=False, server_default="60"),
    )
    # Эти три колонки не читала ни одна строка кода. План B заведёт то, что
    # ему понадобится, своей миграцией — держать пустые заготовки незачем.
    op.drop_column("profiles", "remote_types")
    op.drop_column("profiles", "stop_words")
    op.drop_column("profiles", "languages")


def downgrade() -> None:
    for name in ("languages", "stop_words", "remote_types"):
        op.add_column(
            "profiles",
            sa.Column(name, sa.ARRAY(sa.Text()), nullable=False, server_default="{}"),
        )
    op.drop_column("profiles", "collection_depth_days")
    op.drop_column("profiles", "collection_remote_only")
    op.alter_column("profiles", "collection_cities", new_column_name="locations")
```

В `runner.run_source` вставить `select_in_scope` между `normalize_batch` и `upsert_vacancies`, а в `run_profile` строить фильтры через `filters_for(profile, mode)`.

- [ ] **Step 4: Прогнать всё и закоммитить**

```bash
python -m uv run pytest -q
python -m uv run ruff check . && python -m uv run ruff format --check .
git add -A
git commit -m "feat(ingest): рамка сбора в профиле и обязательная локальная перепроверка"
```

---

## Task 16: Четыре условия кандидата на пропуск

**Files:**
- Modify: `src/jobhunt/ingest/activity.py`, `tests/integration/test_activity.py`

**Interfaces:**
- Consumes: теги (Task 14), рамка (Task 15)
- Produces: `mark_missing(session, profile_id, source, seen_external_ids, ran_tag_ids, profile, today, threshold=2, now=None) -> int`

Кандидатом становится строка `profile_vacancies`, для которой верно **всё** (спека, раздел 5.3):

1. вакансия этого источника, `is_active = true`;
2. связана хотя бы с одним тегом, **реально отработавшим** в этом прогоне;
3. попадает в текущую рамку сбора профиля;
4. с `last_missed_at` прошло не меньше 20 часов.

Условия 1 и 4 уже реализованы в задаче 13. Здесь добавляются 2 и 3.

- [ ] **Step 1: Написать падающий тест**

Дописать в `tests/integration/test_activity.py`:

```python
def test_вакансия_выключенного_тега_не_судится(session):
    """Мы по нему не искали — значит не имеем оснований судить, жива ли она."""
    profile = _profile(session, "Кирилл")
    enabled = _tag(session, profile, "Head of IT")
    disabled = _tag(session, profile, "IT Director", enabled=False)
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy)
    _link(session, pair, disabled)

    mark_missing(
        session, profile.id, "work.ua", {"999"}, ran_tag_ids={enabled.id}, profile=profile,
        today=TODAY,
    )

    session.refresh(pair)
    assert pair.missed_checks == 0


def test_вакансия_вне_рамки_не_судится(session):
    """Сузили рамку до Киева — львовские вакансии перестают быть кандидатами,
    а не объявляются закрытыми. «Мы перестали её собирать» и «её сняли» —
    разные вещи."""
    profile = _profile(session, "Кирилл")
    profile.collection_cities = ["Київ"]
    tag = _tag(session, profile, "Head of IT")
    vacancy = _vacancy(session, "1")
    vacancy.city = "Львів"
    pair = _pair(session, profile, vacancy)
    _link(session, pair, tag)
    session.flush()

    mark_missing(
        session, profile.id, "work.ua", {"999"}, ran_tag_ids={tag.id}, profile=profile,
        today=TODAY,
    )

    session.refresh(pair)
    assert pair.missed_checks == 0


def test_вакансия_отработавшего_тега_внутри_рамки_судится(session):
    profile = _profile(session, "Кирилл")
    tag = _tag(session, profile, "Head of IT")
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy)
    _link(session, pair, tag)

    mark_missing(
        session, profile.id, "work.ua", {"999"}, ran_tag_ids={tag.id}, profile=profile,
        today=TODAY,
    )

    session.refresh(pair)
    assert pair.missed_checks == 1


def test_вакансия_без_тегов_сирота_не_судится(session):
    """Сирота скрыта и не судится: искать её нечем."""
    profile = _profile(session, "Кирилл")
    tag = _tag(session, profile, "Head of IT")
    vacancy = _vacancy(session, "1")
    pair = _pair(session, profile, vacancy)

    mark_missing(
        session, profile.id, "work.ua", {"999"}, ran_tag_ids={tag.id}, profile=profile,
        today=TODAY,
    )

    session.refresh(pair)
    assert pair.missed_checks == 0
```

Добавить в начало файла помощники `_tag` и `_link` (по образцу `tests/integration/test_tags.py`) и константу `TODAY = date(2026, 8, 4)`. Существующие тесты задачи 13 привести к новой сигнатуре, добавив `ran_tag_ids` и `profile`.

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/integration/test_activity.py -q`
Expected: FAIL — `TypeError: mark_missing() got an unexpected keyword argument 'ran_tag_ids'`

- [ ] **Step 3: Реализовать**

В `mark_missing` расширить выборку кандидатов связкой с отработавшими тегами и добавить проверку рамки:

```python
    rows = session.execute(
        select(ProfileVacancy, Vacancy)
        .join(Vacancy, Vacancy.id == ProfileVacancy.vacancy_id)
        .join(ProfileVacancyTag, ProfileVacancyTag.profile_vacancy_id == ProfileVacancy.id)
        .where(
            ProfileVacancy.profile_id == profile_id,
            ProfileVacancy.is_active.is_(True),
            Vacancy.source == source,
            # Судим только то, что искали: вакансия, найденная выключенным
            # тегом, кандидатом не становится никогда.
            ProfileVacancyTag.tag_id.in_(ran_tag_ids),
        )
        .distinct()
    ).all()
```

и внутри цикла, перед инкрементом:

```python
        if not within_scope(_dto_from(vacancy), profile, today):
            # Вне рамки — значит мы там не искали. Сужение рамки не имеет права
            # выглядеть как «вакансию сняли с площадки».
            continue
```

Добавить приватный `_dto_from(vacancy) -> VacancyDTO`, собирающий из строки БД минимальный DTO с полями, которые проверяет рамка (`city`, `city_any`, `work_format`, `posted_at`), — чтобы правило рамки существовало ровно в одном месте, а не дублировалось SQL-условием.

Пустой `ran_tag_ids` обрабатывается как пустая выдача: ничего не судим, пишем предупреждение.

- [ ] **Step 4: Прогнать всё и закоммитить**

```bash
python -m uv run pytest -q
python -m uv run ruff check . && python -m uv run ruff format --check .
git add -A
git commit -m "feat(ingest): кандидат на пропуск ограничен отработавшими тегами и рамкой сбора"
```

---

## Task 17: Два режима сбора, порядок обхода и границы транзакции

**Files:**
- Create: `migrations/versions/0007_parse_run_mode.py`
- Modify: `src/jobhunt/ingest/runner.py`, `src/jobhunt/db/models.py`, `tests/integration/test_runner.py`

**Interfaces:**
- Consumes: всё предыдущее
- Produces:
  - `ParseRun.mode: str | None`
  - `run_profile(session_factory, profile_id, client, mode="full", sources=ALL_SOURCES, parser_factory=get_parser, today=None) -> list[ParseRun]` — принимает фабрику сессий, а не сессию: коммит после каждой пары «источник + тег»
  - `rebuild_tag_links(session, profile_id, source, tag_id, seen_external_ids) -> int` — снимает связки тега у вакансий, которых он больше не находит

**Три правила этой задачи:**

*Только полная сверка судит.* Быстрое обновление собирает и обновляет, но не двигает счётчик пропусков и не снимает связки. Это снимает проблему «3 прогона = 3 часа»: порог привязан к суточной сверке, а не к числу нажатий.

*Полная сверка пересобирает связки того тега, по которому шла.* Тег отработал полностью — вакансии, которых он не нашёл, теряют связку с ним. Правило симметрично отметке пропусков: право убирать имеет только полный проход. Оно же чинит приближение backfill'а из задачи 14.

*Теги снаружи, источники внутри.* Пауза держится на хост: ожидание work.ua накладывается на запрос к dou, и общее время падает почти вдвое.

- [ ] **Step 1: Написать падающий тест**

Добавить в `tests/conftest.py` фабрику сессий — `run_profile` теперь коммитит сам:

```python
@pytest.fixture
def session_factory(engine, session):
    """Фабрика сессий для кода, который коммитит сам (run_profile).

    Зависит от `session` не ради самой сессии, а ради очистки таблиц: без неё
    закоммиченные прогоны утекали бы из теста в тест.
    """
    return sessionmaker(bind=engine, expire_on_commit=False)
```

Дописать в `tests/integration/test_runner.py`:

```python
from datetime import UTC, date, datetime

from sqlalchemy import select

from jobhunt.db.models import (
    ParseRun,
    Profile,
    ProfileTag,
    ProfileVacancy,
    ProfileVacancyTag,
    Vacancy,
)
from jobhunt.ingest.runner import run_profile
from jobhunt.ingest.tags import rebuild_tag_links
from jobhunt.parsers.base import ParseResult, RawVacancy, SearchFilters

TODAY = date(2026, 8, 4)


class RecordingParser:
    """Парсер, запоминающий порядок вызовов и отдающий заданные карточки."""

    def __init__(self, source: str, by_query: dict[str, list[str]], calls: list) -> None:
        self.source_name = source
        self._by_query = by_query
        self._calls = calls

    def fetch_listings(self, query: str, filters: SearchFilters) -> ParseResult:
        self._calls.append((self.source_name, query, filters.mode))
        ids = self._by_query.get(query, [])
        return ParseResult(
            vacancies=[
                RawVacancy(
                    source=self.source_name,
                    external_id=external_id,
                    title=f"Роль {external_id}",
                    url=f"https://example.test/{self.source_name}/{external_id}/",
                    description_snippet="Опис",
                    company_raw="Компанія",
                    location_raw="Київ",
                    posted_raw="3 серпня 2026",
                )
                for external_id in ids
            ],
            total_available=len(ids),
        )


def _make_profile(session, tags: list[str]) -> Profile:
    profile = Profile(name="Кирилл", locations=[], collection_cities=[])
    session.add(profile)
    session.flush()
    for text in tags:
        session.add(ProfileTag(profile_id=profile.id, text=text))
    session.commit()
    return profile


def test_обход_идёт_тегами_снаружи_источниками_внутри(session, session_factory):
    """Пауза держится на хост: чередование источников почти вдвое сокращает
    общее время прогона, потому что ожидание одной площадки накладывается на
    запрос к другой."""
    profile = _make_profile(session, ["Head of IT", "IT Director"])
    calls: list = []

    def factory(source: str, client):
        return RecordingParser(source, {"Head of IT": ["1"], "IT Director": ["2"]}, calls)

    run_profile(
        session_factory,
        profile.id,
        client=None,
        mode="full",
        parser_factory=factory,
        today=TODAY,
    )

    assert calls == [
        ("work.ua", "Head of IT", "full"),
        ("dou.ua", "Head of IT", "full"),
        ("work.ua", "IT Director", "full"),
        ("dou.ua", "IT Director", "full"),
    ]


def test_выключенный_тег_не_запрашивается(session, session_factory):
    profile = _make_profile(session, ["Head of IT", "IT Director"])
    disabled = session.execute(
        select(ProfileTag).where(ProfileTag.text == "IT Director")
    ).scalar_one()
    disabled.is_enabled = False
    session.commit()

    calls: list = []
    run_profile(
        session_factory,
        profile.id,
        client=None,
        mode="full",
        parser_factory=lambda source, client: RecordingParser(source, {"Head of IT": ["1"]}, calls),
        today=TODAY,
    )

    assert {query for _, query, _ in calls} == {"Head of IT"}


def test_быстрый_режим_не_двигает_счётчик_пропусков(session, session_factory):
    """Быстрое обновление читает только верхушку выдачи. Судить по неполной
    картине нельзя, поэтому счётчик оно не трогает вовсе."""
    profile = _make_profile(session, ["Head of IT"])
    calls: list = []
    # Первый прогон заводит вакансию, второй её уже не находит.
    run_profile(
        session_factory,
        profile.id,
        client=None,
        mode="full",
        parser_factory=lambda source, client: RecordingParser(source, {"Head of IT": ["1"]}, calls),
        today=TODAY,
    )
    run_profile(
        session_factory,
        profile.id,
        client=None,
        mode="quick",
        parser_factory=lambda source, client: RecordingParser(source, {"Head of IT": ["9"]}, calls),
        today=TODAY,
    )

    session.expire_all()
    pairs = session.execute(select(ProfileVacancy)).scalars().all()
    assert all(pair.missed_checks == 0 for pair in pairs), (
        "быстрое обновление засчитало пропуск, хотя видит лишь часть выдачи"
    )


def test_каждая_пара_источник_тег_коммитится_отдельно(session, session_factory):
    """Обрыв на середине суточной сверки не должен терять всё собранное вместе
    с журналом, который объяснил бы, что произошло."""
    profile = _make_profile(session, ["Head of IT", "IT Director"])

    class ExplodingParser(RecordingParser):
        def fetch_listings(self, query: str, filters: SearchFilters) -> ParseResult:
            if query == "IT Director":
                raise KeyboardInterrupt("прервано пользователем")
            return super().fetch_listings(query, filters)

    calls: list = []
    try:
        run_profile(
            session_factory,
            profile.id,
            client=None,
            mode="full",
            parser_factory=lambda source, client: ExplodingParser(
                source, {"Head of IT": ["1"]}, calls
            ),
            today=TODAY,
        )
    except KeyboardInterrupt:
        pass

    session.expire_all()
    saved = session.execute(select(Vacancy)).scalars().all()
    runs = session.execute(select(ParseRun)).scalars().all()
    assert saved, "вакансии первого тега потеряны обрывом на втором"
    assert runs, "журнал прогонов потерян вместе с данными"


def test_полная_сверка_снимает_связку_у_ненайденных(session):
    """Иначе приближение backfill'а («все вакансии всеми тегами») осталось бы
    навсегда, и выключение тега перестало бы что-либо прятать."""
    profile = _make_profile(session, ["Head of IT"])
    tag = session.execute(select(ProfileTag)).scalar_one()
    now = datetime.now(UTC)
    for external_id in ("1", "2"):
        vacancy = Vacancy(
            source="work.ua",
            external_id=external_id,
            title=f"Роль {external_id}",
            url=f"https://example.test/{external_id}/",
            description_raw="Опис",
            description_hash="x" * 64,
            first_seen_at=now,
            last_seen_at=now,
        )
        session.add(vacancy)
        session.flush()
        pair = ProfileVacancy(
            profile_id=profile.id,
            vacancy_id=vacancy.id,
            first_seen_at=now,
            last_seen_at=now,
        )
        session.add(pair)
        session.flush()
        session.add(ProfileVacancyTag(profile_vacancy_id=pair.id, tag_id=tag.id))
    session.flush()

    removed = rebuild_tag_links(session, profile.id, "work.ua", tag.id, seen_external_ids={"1"})

    assert removed == 1
    links = session.execute(select(ProfileVacancyTag)).scalars().all()
    assert len(links) == 1


def test_пустое_множество_увиденного_связок_не_снимает(session, caplog):
    """Пустая выдача почти всегда значит поломку парсера, а не то, что тег
    перестал что-либо находить. Снять все связки разом означало бы спрятать
    всю выдачу профиля одним неудачным прогоном."""
    profile = _make_profile(session, ["Head of IT"])
    tag = session.execute(select(ProfileTag)).scalar_one()

    with caplog.at_level("WARNING"):
        removed = rebuild_tag_links(session, profile.id, "work.ua", tag.id, seen_external_ids=set())

    assert removed == 0
    assert any("ноль" in r.message.lower() for r in caplog.records)
```

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/integration/test_runner.py -q`
Expected: FAIL — `TypeError: run_profile() got an unexpected keyword argument 'mode'`

- [ ] **Step 3: Реализовать**

Добавить `ParseRun.mode` (nullable — у прошлых записей режим неизвестен, и выдумывать его нельзя) и миграцию `0007_parse_run_mode.py`.

Переписать `run_profile`: внешний цикл по включённым тегам, внутренний по источникам, коммит после каждой пары; накопление `seen_ids` и `ran_tag_ids` по источникам; после всех тегов — `mark_missing` для каждого источника, но **только при `mode == "full"`** и только если все запросы источника отработали и вернули полный набор id.

Добавить `rebuild_tag_links` в `src/jobhunt/ingest/tags.py`:

```python
def rebuild_tag_links(
    session: Session,
    profile_id: uuid.UUID,
    source: str,
    tag_id: uuid.UUID,
    seen_external_ids: set[str],
) -> int:
    """Снять связки тега у вакансий источника, которых он больше не находит.

    Вызывается только после полной сверки по этому тегу: право убирать имеет
    лишь проход, видевший всю картину. Быстрое обновление читает верхушку
    выдачи и связки не снимает никогда.

    Возвращает число снятых связок.
    """
```

- [ ] **Step 4: Прогнать всё и закоммитить**

```bash
python -m uv run pytest -q
python -m uv run ruff check . && python -m uv run ruff format --check .
git add -A
git commit -m "feat(ingest): режимы full/quick, пересборка связок тегов и коммит по паре источник+тег"
```

---

## Task 18: CLI профилей, тегов, сбора и переразбора

**Files:**
- Modify: `src/jobhunt/cli.py`, `tests/integration/test_cli.py`
- Create: `src/jobhunt/renormalize.py`

**Interfaces:**
- Consumes: всё предыдущее
- Produces: команды `profile create|update|list`, `tag add|remove|enable|disable|list`, `parse --profile … --mode full|quick`, `renormalize`

```
jobhunt profile create --name "Кирилл" [--city Київ]... [--remote-only] [--depth-days 60]
jobhunt profile update --name "Кирилл" [--city ...]... [--remote-only/--no-remote-only] [--depth-days N]
jobhunt profile list
jobhunt tag add|remove|enable|disable --profile "Кирилл" --text "Head of IT"
jobhunt tag list --profile "Кирилл"
jobhunt parse --profile "Кирилл" --mode full|quick
jobhunt renormalize
```

`renormalize` перевычисляет `city`, `city_any`, `work_format` из `location_raw` **тем же модулем нормализации**, что и обычный сбор. Правила разбора внутрь миграции не попали намеренно: копия правил разошлась бы с живым кодом молча. Запускается один раз после миграции и каждый раз, когда правило разбора поправлено — перекрывать площадки заново не нужно.

- [ ] **Step 1: Написать падающий тест**

Дописать в `tests/integration/test_cli.py`:

```python
from sqlalchemy import select

from jobhunt.cli import main
from jobhunt.db.models import Profile, ProfileTag, Vacancy


def test_создание_профиля_с_рамкой(session, capsys):
    code = main(
        [
            "profile", "create",
            "--name", "Кирилл",
            "--city", "Київ",
            "--remote-only",
            "--depth-days", "45",
        ]
    )

    assert code == 0
    profile = session.execute(select(Profile)).scalar_one()
    assert profile.collection_cities == ["Київ"]
    assert profile.collection_remote_only is True
    assert profile.collection_depth_days == 45


def test_глубина_по_умолчанию_шестьдесят_дней(session):
    main(["profile", "create", "--name", "Кирилл"])
    profile = session.execute(select(Profile)).scalar_one()
    assert profile.collection_depth_days == 60


def test_добавление_и_выключение_тега(session, capsys):
    main(["profile", "create", "--name", "Кирилл"])
    assert main(["tag", "add", "--profile", "Кирилл", "--text", "Head of IT"]) == 0

    tag = session.execute(select(ProfileTag)).scalar_one()
    assert tag.text == "Head of IT"
    assert tag.is_enabled is True

    assert main(["tag", "disable", "--profile", "Кирилл", "--text", "Head of IT"]) == 0
    session.refresh(tag)
    assert tag.is_enabled is False


def test_повторное_добавление_тега_не_падает_и_сообщает(session, capsys):
    """Уникальность в пределах профиля — ограничение БД, но пользователю нужно
    внятное сообщение, а не трассировка IntegrityError."""
    main(["profile", "create", "--name", "Кирилл"])
    main(["tag", "add", "--profile", "Кирилл", "--text", "Head of IT"])

    code = main(["tag", "add", "--profile", "Кирилл", "--text", "Head of IT"])

    assert code == 1
    assert "уже есть" in capsys.readouterr().out.lower()


def test_сбор_без_включённых_тегов_возвращает_единицу(session, capsys):
    """Молчаливого «всё ок» при нечего-собирать быть не должно."""
    main(["profile", "create", "--name", "Кирилл"])

    code = main(["parse", "--profile", "Кирилл", "--mode", "full"])

    assert code == 1
    assert "тег" in capsys.readouterr().out.lower()


def test_сбор_для_несуществующего_профиля_возвращает_единицу(session, capsys):
    code = main(["parse", "--profile", "Нет такого", "--mode", "full"])

    assert code == 1
    assert "не найден" in capsys.readouterr().out.lower()


def test_переразбор_заполняет_производные_поля_из_сырой_локации(session, capsys):
    """Правила разбора в миграцию намеренно не попали: копия правил разошлась
    бы с живым кодом молча. Переразбор пользуется тем же модулем, что и сбор."""
    from datetime import UTC, datetime

    now = datetime.now(UTC)
    session.add(
        Vacancy(
            source="work.ua",
            external_id="1",
            title="Роль",
            url="https://www.work.ua/jobs/1/",
            description_raw="Опис",
            description_hash="x" * 64,
            location_raw="Дистанційно",
            first_seen_at=now,
            last_seen_at=now,
        )
    )
    session.commit()

    code = main(["renormalize"])

    assert code == 0
    session.expire_all()
    stored = session.execute(select(Vacancy)).scalar_one()
    assert stored.work_format == "remote"
    assert stored.city is None
    assert "1" in capsys.readouterr().out


def test_переразбор_на_пустой_базе_не_падает(session, capsys):
    assert main(["renormalize"]) == 0
```

Тесты вызывают `main` напрямую, а не через подпроцесс: так виден код возврата и печать, а `capsys` не требует возни с кодировкой консоли.

- [ ] **Step 2: Убедиться, что тесты падают**

Run: `python -m uv run pytest tests/integration/test_cli.py -q`
Expected: FAIL — `SystemExit: 2` (неизвестная подкоманда `profile`)

- [ ] **Step 3: Реализовать**

Перестроить `build_parser` на вложенные подкоманды. Сохранить `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` в `main` — без него любая печать кириллицы роняет команду уже после того, как работа сделана.

Коды возврата: `0` — все запросы отработали; `1` — профиль не найден, у профиля нет включённых тегов, либо хотя бы один запрос завершился ошибкой. Сохранить существующее правило: усечение выдачи не считается сбоем, но печатается предупреждением, и неполный набор id печатается отдельной строкой.

Создать `src/jobhunt/renormalize.py` с функцией `renormalize_all(session, today) -> int`, перебирающей вакансии с непустым `location_raw` и переписывающей производные поля через `parse_location`.

- [ ] **Step 4: Прогнать всё и закоммитить**

```bash
python -m uv run pytest -q
python -m uv run ruff check . && python -m uv run ruff format --check .
git add -A
git commit -m "feat(cli): управление профилями и тегами, режимы сбора, команда переразбора"
```

---

## Task 19: Проверка на живых данных

**Files:** изменений кода не предполагается; всё найденное оформляется отдельными задачами.

Тесты стоят на фикстурах. Ниже — то, чего фикстуры не ловят.

- [ ] **Step 1: Применить миграции и переразобрать накопленное**

```bash
docker compose up -d --build
python -m uv run python -m jobhunt.cli renormalize
```

Проверить, что все 55 записей получили производные поля:

```sql
SELECT work_format, city_any, count(*) FROM vacancies GROUP BY 1, 2 ORDER BY 1;
SELECT count(*) FROM vacancies WHERE location_raw IS NOT NULL AND work_format IS NULL;
```

Второй запрос обязан вернуть 0: непустая сырая локация, из которой ничего не вывелось, означает формулировку, которой словарь не знает.

- [ ] **Step 2: Полная сверка**

```bash
python -m uv run python -m jobhunt.cli parse --profile "Кирилл" --mode full
```

```sql
SELECT source, mode, query_params->>'query' AS тег, found_count, new_count,
       total_available, status, ids_incomplete
FROM parse_runs ORDER BY started_at DESC LIMIT 20;
```

На что смотреть: `total_available` заполнен у обоих источников; `mode = 'full'`; порядок записей — теги снаружи, источники внутри.

- [ ] **Step 3: Быстрое обновление**

```bash
python -m uv run python -m jobhunt.cli parse --profile "Кирилл" --mode quick
```

Убедиться запросом, что `missed_checks` не изменился ни у одной строки и что связки тегов не исчезли.

- [ ] **Step 4: Широкий тег**

Добавить тег «менеджер», прогнать полную сверку, убедиться, что упор в лимит страниц даёт `ids_incomplete = true`, отметку пропусков для источника пропускает, и `total_available` показывает масштаб (порядка 13 000 у work.ua, порядка 1400 у dou). Затем тег удалить и проверить, что вакансии стали сиротами, а не исчезли.

- [ ] **Step 5: Цикл деактивации**

Выключить тег, по которому найдена конкретная вакансия, прогнать полную сверку дважды с интервалом больше 20 часов (либо подставить `now` в вызов) и убедиться, что вакансия **не** деактивировалась: по выключенному тегу мы не искали.

Затем сузить рамку профиля до города, которого у вакансии нет, и убедиться, что она тоже не деактивировалась.

Наконец, вернуть тег и рамку, вручную удалить вакансию из выдачи (сузив запрос) и убедиться, что после двух сверок `is_active` стал `false`, а после возвращения — снова `true` с обнулённым счётчиком.

- [ ] **Step 6: Интерфейс**

Открыть `http://localhost:8000/vacancies`. Проверить: колонка города показывает «Дистанційно» и «Вся Україна» там, где они есть; колонка тегов заполнена; смена статуса работает; галочка «показывать неактивные» работает.

- [ ] **Step 7: Записать найденное**

Всё расхождение между ожиданием и наблюдением оформить задачами. Отдельно проверить гипотезу из спеки (раздел 10): отсортирована ли выдача work.ua по дате **обновления**, а не публикации. Если подтвердится — записать в известные ограничения; если нет — выяснить настоящий порядок.

- [ ] **Step 8: Обновить документы**

Переписать `docs/HANDOFF.md` под новое состояние: схема, режимы сбора, команды CLI, что проверено живьём и что осталось открытым.

```bash
git add docs/HANDOFF.md
git commit -m "docs: передача состояния после итерации профильного сбора"
```
