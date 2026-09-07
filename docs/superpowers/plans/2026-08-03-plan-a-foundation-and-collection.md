# План A: фундамент и сбор вакансий — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Работающий трекер вакансий: парсеры work.ua и dou.ua собирают вакансии по параметрам профиля в PostgreSQL без дублей, веб-таблица показывает их и позволяет менять статус отклика.

**Architecture:** Слоистая структура с жёсткими границами. Парсеры делают HTTP и разбор разметки, возвращают DTO и ничего не знают о базе. Модуль `ingest` — единственный, кто пишет вакансии в БД: он отвечает за дедупликацию, счётчик пропусков и отслеживание изменений текста. Веб-слой на FastAPI + Jinja2 + HTMX отдаёт серверный HTML без отдельного фронтенд-проекта.

**Tech Stack:** Python 3.12, FastAPI, Jinja2, HTMX, SQLAlchemy 2.0, Alembic, PostgreSQL 17 с pgvector, httpx, BeautifulSoup4 + lxml, pytest, uv, Docker Compose.

**Спек:** `docs/superpowers/specs/2026-08-03-job-hunt-ai-iteration-1-design.md` — реализуются шаги 1–5 раздела 12.

## Global Constraints

- Python `>=3.12,<3.13`. На хосте стоит 3.14 — использовать её нельзя, окружение создаётся через `uv venv --python 3.12`.
- Образ БД: `pgvector/pgvector:pg17`. Обычный `postgres` не подходит — расширение `vector` понадобится в плане B.
- Каждый парсер реализует интерфейс `BaseParser` из `src/jobhunt/parsers/base.py`. Прямые HTTP-вызовы вне `src/jobhunt/http_client.py` запрещены.
- Модули `parsers/` не импортируют ничего из `db/` и `ingest/`. Проверяется тестом в Task 4.
- Все тесты парсеров работают на сохранённых фикстурах из `tests/fixtures/`. Сеть в тестах не используется.
- User-Agent для всех запросов: `JobHuntAI/0.1 (+personal job search tool)`. Пауза между запросами к одному хосту — не меньше `settings.request_delay_seconds` (по умолчанию 2.0 секунды).
- Даты в БД хранятся в UTC, тип `TIMESTAMP WITH TIME ZONE`.
- Сообщения об ошибках и комментарии в коде — на русском, идентификаторы — на английском.
- Никаких «тихих» усечений: если источник вернул неполную выдачу, прогон помечается `status='truncated'` в `parse_runs`.

## Проверенные факты об источниках

Собраны обращением к живым страницам 2026-08-03. Селекторы ниже не предположения — они сняты с реальной разметки.

**work.ua** — серверный рендеринг, JavaScript не нужен.

| Что | Как достать |
|---|---|
| URL поиска | `https://www.work.ua/jobs/?search=<urlencoded>` |
| Контейнер списка | `div#pjax-jobs-list` |
| Карточка | `div.card.job-link` (полный класс `card card-hover card-visited wordwrap job-link`) |
| Ссылка и заголовок | `h2 a[href^="/jobs/"]`, href вида `/jobs/8294127/` |
| `external_id` | последний сегмент href: `8294127` |
| Дата публикации | атрибут `title` той же ссылки: `«…, вакансія від 3 серпня 2026»` |
| Зарплата | `div.text-indent`, содержащий `.glyphicon-hryvnia-fill` → внутри `span.strong-600` |
| Компания | `div.text-indent`, содержащий `.glyphicon-company` → внутри `span.strong-600` |
| Город | в блоке компании — первый `span` после `ul` с бейджами |
| Сниппет | `p.ellipsis-line-3` |
| Пагинация | `ul.pagination` |
| Детальная страница | `https://www.work.ua/jobs/<id>/`: `h1` — заголовок, `div#job-description` — полный текст |
| Карточек на странице | 14 |

**dou.ua** — основной путь RSS, разбор HTML не нужен.

| Что | Как достать |
|---|---|
| URL фида | `https://jobs.dou.ua/vacancies/feeds/?search=<urlencoded>` |
| Элемент | `channel/item` |
| `<title>` | `«Head of IT в WayForPay, віддалено»` — заголовок, компания и город одной строкой |
| `<link>` | `https://jobs.dou.ua/companies/wayforpay/vacancies/311967/?utm_source=jobsrss` |
| `external_id` | число из пути: `/vacancies/(\d+)/` → `311967` |
| `<description>` | **полный HTML описания вакансии**, а не сниппет |
| `<pubDate>` | RFC-822, разбирается `email.utils.parsedate_to_datetime` |
| Лимит выдачи | 25 элементов на поисковый фид, 50 на общий; пагинации нет |

Из-за полного описания в фиде для dou.ua не нужен отдельный запрос детальной страницы: один HTTP-запрос вместо N+1. Ограничение в 25 элементов для точечных запросов вроде «IT Director» (2 результата) не мешает, но упор в лимит обязан фиксироваться в журнале прогона.

`robots.txt` обоих сайтов для `User-agent: *` не запрещает страницы вакансий: work.ua закрывает личные кабинеты и служебные эндпоинты, dou.ua — служебные AJAX-ручки.

---

## Структура файлов

| Файл | Ответственность |
|---|---|
| `pyproject.toml` | Зависимости, конфигурация pytest и ruff |
| `docker-compose.yml` | Сервисы `db` и `app` |
| `Dockerfile` | Образ приложения |
| `.env.example` | Шаблон переменных окружения |
| `alembic.ini`, `migrations/` | Миграции |
| `src/jobhunt/config.py` | Настройки через pydantic-settings |
| `src/jobhunt/db/base.py` | `Base`, движок, фабрика сессий |
| `src/jobhunt/db/models.py` | ORM-модели |
| `src/jobhunt/http_client.py` | HTTP с паузами, кешем и проверкой robots.txt |
| `src/jobhunt/parsers/base.py` | `BaseParser`, DTO `VacancyDTO`, `ParserStructureError` |
| `src/jobhunt/parsers/work_ua.py` | Парсер work.ua |
| `src/jobhunt/parsers/dou.py` | Парсер dou.ua |
| `src/jobhunt/parsers/registry.py` | Реестр парсеров по имени источника |
| `src/jobhunt/ingest/upsert.py` | Вставка и обновление вакансий |
| `src/jobhunt/ingest/activity.py` | `missed_runs`, `is_active`, хеш описания |
| `src/jobhunt/ingest/runner.py` | Оркестрация прогона, журнал `parse_runs` |
| `src/jobhunt/cli.py` | Команды `parse`, `init-profile` |
| `src/jobhunt/web/app.py` | Сборка приложения FastAPI |
| `src/jobhunt/web/routes/vacancies.py` | Роуты таблицы и смены статуса |
| `src/jobhunt/web/templates/` | Шаблоны Jinja2 |
| `scripts/capture_fixture.py` | Сохранение живых страниц в фикстуры |
| `tests/` | Тесты и фикстуры |

---

## Task 1: Каркас проекта и запуск

**Files:**
- Create: `pyproject.toml`, `Dockerfile`, `docker-compose.yml`, `.env.example`, `README.md`
- Create: `src/jobhunt/__init__.py`, `src/jobhunt/config.py`, `src/jobhunt/web/app.py`
- Test: `tests/test_health.py`

**Interfaces:**
- Consumes: ничего
- Produces: `jobhunt.config.settings` — объект `Settings` с полями `database_url: str`, `user_agent: str`, `request_delay_seconds: float`, `http_cache_dir: Path`, `http_cache_enabled: bool`, `tracing_enabled: bool`; `jobhunt.web.app.app` — экземпляр `FastAPI`

- [ ] **Step 1: Создать `pyproject.toml`**

```toml
[project]
name = "jobhunt"
version = "0.1.0"
description = "Job Hunt AI — интеллектуальный поиск работы"
requires-python = ">=3.12,<3.13"
dependencies = [
    "fastapi>=0.115",
    "uvicorn[standard]>=0.32",
    "jinja2>=3.1",
    "python-multipart>=0.0.12",
    "httpx>=0.27",
    "beautifulsoup4>=4.12",
    "lxml>=5.3",
    "sqlalchemy>=2.0.36",
    "alembic>=1.14",
    "psycopg[binary]>=3.2",
    "pydantic>=2.9",
    "pydantic-settings>=2.6",
]

[dependency-groups]
dev = ["pytest>=8.3", "pytest-asyncio>=0.24", "ruff>=0.8"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/jobhunt"]

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"

[tool.ruff]
line-length = 100
target-version = "py312"
```

- [ ] **Step 2: Создать окружение и установить зависимости**

```bash
python -m pip install --user uv
uv venv --python 3.12
uv sync
```

`uv sync` ставит и зависимости проекта, и группу `dev` — она подхватывается по умолчанию.

Ожидается: создан каталог `.venv`, установка завершается без ошибок.

Если `uv` не находится в PATH после установки, использовать `python -m uv` вместо `uv`.

- [ ] **Step 3: Написать падающий тест health-check**

Создать `tests/test_health.py`:

```python
from fastapi.testclient import TestClient

from jobhunt.web.app import app


def test_health_returns_ok():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

- [ ] **Step 4: Запустить тест и убедиться, что он падает**

Run: `uv run pytest tests/test_health.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.web'`

- [ ] **Step 5: Создать конфигурацию**

Создать `src/jobhunt/__init__.py` (пустой) и `src/jobhunt/config.py`:

```python
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения. Читаются из переменных окружения и файла .env."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://jobhunt:jobhunt@localhost:5432/jobhunt"

    user_agent: str = "JobHuntAI/0.1 (+personal job search tool)"
    request_delay_seconds: float = 2.0
    request_timeout_seconds: float = 30.0

    http_cache_enabled: bool = False
    http_cache_dir: Path = Path(".cache/http")

    ollama_base_url: str = "http://host.docker.internal:11434"
    tracing_enabled: bool = False


settings = Settings()
```

- [ ] **Step 6: Создать приложение FastAPI**

Создать `src/jobhunt/web/__init__.py` (пустой) и `src/jobhunt/web/app.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Job Hunt AI")


@app.get("/health")
def health() -> dict[str, str]:
    """Проверка живости — используется healthcheck-ом Docker."""
    return {"status": "ok"}
```

- [ ] **Step 7: Запустить тест и убедиться, что он проходит**

Run: `uv run pytest tests/test_health.py -v`
Expected: PASS, 1 passed

- [ ] **Step 8: Создать Dockerfile**

```dockerfile
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -e .

EXPOSE 8000
CMD ["uvicorn", "jobhunt.web.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

- [ ] **Step 9: Создать `docker-compose.yml`**

```yaml
services:
  db:
    image: pgvector/pgvector:pg17
    environment:
      POSTGRES_USER: jobhunt
      POSTGRES_PASSWORD: jobhunt
      POSTGRES_DB: jobhunt
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U jobhunt -d jobhunt"]
      interval: 5s
      timeout: 3s
      retries: 10

  app:
    build: .
    depends_on:
      db:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql+psycopg://jobhunt:jobhunt@db:5432/jobhunt
      OLLAMA_BASE_URL: http://host.docker.internal:11434
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src
    extra_hosts:
      - "host.docker.internal:host-gateway"

volumes:
  pgdata:
```

- [ ] **Step 10: Создать `.env.example` и `README.md`**

`.env.example`:

```dotenv
# Подключение к БД. Для запуска тестов с хоста — localhost, внутри compose — db.
DATABASE_URL=postgresql+psycopg://jobhunt:jobhunt@localhost:5432/jobhunt
TEST_DATABASE_URL=postgresql+psycopg://jobhunt:jobhunt@localhost:5432/jobhunt_test

# Вежливость к площадкам: пауза между запросами к одному хосту, секунды
REQUEST_DELAY_SECONDS=2.0

# Кеш HTTP-ответов на диск. Включать при отладке парсеров,
# чтобы не обращаться к живому сайту при каждом прогоне.
HTTP_CACHE_ENABLED=false

# Локальная модель
OLLAMA_BASE_URL=http://host.docker.internal:11434

# Наблюдаемость выключена по умолчанию — данные не покидают машину
TRACING_ENABLED=false
```

`README.md`:

```markdown
# Job Hunt AI

Инструмент для интеллектуального поиска работы: сбор вакансий с work.ua и dou.ua,
сопоставление с банком тезисов из резюме, анализ разрывов и накопление статистики
по откликам.

Работает локально. Резюме и история откликов не покидают вашу машину.

## Требования

- Docker Desktop (должен быть запущен)
- Python 3.12 через [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com) на хосте с моделью `bge-m3` — понадобится начиная с плана B

## Запуск

```bash
cp .env.example .env
docker compose up -d
```

Приложение: http://localhost:8000

## Тесты

```bash
uv run pytest
```
```

- [ ] **Step 11: Проверить, что стек поднимается**

```bash
docker compose up -d --build
docker compose ps
curl http://localhost:8000/health
```

Expected: оба сервиса в состоянии `running`, у `db` — `healthy`; curl возвращает `{"status":"ok"}`.

Если Docker Desktop не запущен, команда завершится ошибкой `cannot find the path ... dockerDesktopLinuxEngine` — запустить Docker Desktop и повторить.

- [ ] **Step 12: Commit**

```bash
git add pyproject.toml Dockerfile docker-compose.yml .env.example README.md src tests
git commit -m "feat: каркас проекта, конфигурация и health-check"
```

---

## Task 2: Схема БД и первая миграция

**Files:**
- Create: `src/jobhunt/db/__init__.py`, `src/jobhunt/db/base.py`, `src/jobhunt/db/models.py`
- Create: `alembic.ini`, `migrations/env.py`, `migrations/versions/0001_initial.py`
- Test: `tests/conftest.py`, `tests/integration/test_models.py`

**Interfaces:**
- Consumes: `jobhunt.config.settings.database_url`
- Produces: `jobhunt.db.base.Base`, `jobhunt.db.base.get_engine()`, `jobhunt.db.base.session_scope()`; модели `Profile`, `Vacancy`, `Application`, `ParseRun` из `jobhunt.db.models`

- [ ] **Step 1: Создать базовые объекты SQLAlchemy**

Создать `src/jobhunt/db/__init__.py` (пустой) и `src/jobhunt/db/base.py`:

```python
from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from jobhunt.config import settings


class Base(DeclarativeBase):
    pass


_engine = None
_session_factory = None


def get_engine():
    """Ленивая инициализация движка — чтобы импорт модуля не требовал живой БД."""
    global _engine
    if _engine is None:
        _engine = create_engine(settings.database_url, pool_pre_ping=True)
    return _engine


def get_session_factory() -> sessionmaker[Session]:
    global _session_factory
    if _session_factory is None:
        _session_factory = sessionmaker(bind=get_engine(), expire_on_commit=False)
    return _session_factory


@contextmanager
def session_scope() -> Iterator[Session]:
    """Сессия с автоматическим commit при успехе и rollback при исключении."""
    session = get_session_factory()()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
```

- [ ] **Step 2: Написать падающий тест моделей**

Создать `tests/conftest.py`:

```python
import os

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from jobhunt.db import models  # noqa: F401  — регистрирует таблицы в Base.metadata
from jobhunt.db.base import Base

TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL",
    "postgresql+psycopg://jobhunt:jobhunt@localhost:5432/jobhunt_test",
)


@pytest.fixture(scope="session")
def engine():
    """Движок к тестовой БД. Создаёт её, если она ещё не существует."""
    admin_url = TEST_DATABASE_URL.rsplit("/", 1)[0] + "/postgres"
    admin = create_engine(admin_url, isolation_level="AUTOCOMMIT")
    db_name = TEST_DATABASE_URL.rsplit("/", 1)[1]
    with admin.connect() as conn:
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :n"), {"n": db_name}
        ).scalar()
        if not exists:
            conn.execute(text(f'CREATE DATABASE "{db_name}"'))
    admin.dispose()

    eng = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(eng)
    yield eng
    eng.dispose()


@pytest.fixture
def session(engine):
    """Чистая сессия на каждый тест: таблицы очищаются перед началом."""
    factory = sessionmaker(bind=engine, expire_on_commit=False)
    with factory() as s:
        for table in reversed(Base.metadata.sorted_tables):
            s.execute(text(f'TRUNCATE TABLE "{table.name}" CASCADE'))
        s.commit()
        yield s
```

Создать `tests/integration/__init__.py` (пустой) и `tests/integration/test_models.py`:

```python
from datetime import UTC, datetime

import pytest
from sqlalchemy.exc import IntegrityError

from jobhunt.db.models import Profile, Vacancy


def _vacancy(external_id: str = "8294127") -> Vacancy:
    now = datetime.now(UTC)
    return Vacancy(
        source="work.ua",
        external_id=external_id,
        title="Керівник відділу розробки",
        company="Garvis",
        url=f"https://www.work.ua/jobs/{external_id}/",
        description_raw="Повна зайнятість.",
        description_hash="abc123",
        first_seen_at=now,
        last_seen_at=now,
    )


def test_profile_stores_array_fields(session):
    profile = Profile(name="Кирилл", target_roles=["IT Director"], locations=["Київ"])
    session.add(profile)
    session.commit()

    assert profile.id is not None
    assert profile.target_roles == ["IT Director"]


def test_vacancy_defaults(session):
    vacancy = _vacancy()
    session.add(vacancy)
    session.commit()

    assert vacancy.id is not None
    assert vacancy.is_active is True
    assert vacancy.missed_runs == 0


def test_duplicate_source_and_external_id_is_rejected(session):
    session.add(_vacancy())
    session.commit()

    session.add(_vacancy())
    with pytest.raises(IntegrityError):
        session.commit()
    session.rollback()
```

- [ ] **Step 3: Запустить тест и убедиться, что он падает**

Run: `uv run pytest tests/integration/test_models.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.db.models'`

- [ ] **Step 4: Создать модели**

Создать `src/jobhunt/db/models.py`:

```python
import uuid
from datetime import datetime

from sqlalchemy import (
    ARRAY,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from jobhunt.db.base import Base


def _uuid_pk() -> Mapped[uuid.UUID]:
    return mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class Profile(Base):
    """Кто ищет работу. В итерации 1 профиль один, но схема готова к нескольким."""

    __tablename__ = "profiles"

    id: Mapped[uuid.UUID] = _uuid_pk()
    name: Mapped[str] = mapped_column(String(200))
    target_roles: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    locations: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    remote_types: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    stop_words: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    languages: Mapped[list[str]] = mapped_column(ARRAY(Text), default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Vacancy(Base):
    """Объективные данные площадки. Скор и статус отклика сюда не попадают."""

    __tablename__ = "vacancies"
    __table_args__ = (UniqueConstraint("source", "external_id", name="uq_vacancy_source_external"),)

    id: Mapped[uuid.UUID] = _uuid_pk()
    source: Mapped[str] = mapped_column(String(50), index=True)
    external_id: Mapped[str] = mapped_column(String(100))

    title: Mapped[str] = mapped_column(Text)
    company: Mapped[str | None] = mapped_column(Text, nullable=True)
    url: Mapped[str] = mapped_column(Text)
    description_raw: Mapped[str] = mapped_column(Text)
    description_hash: Mapped[str] = mapped_column(String(64), index=True)

    location: Mapped[str | None] = mapped_column(Text, nullable=True)
    salary_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_currency: Mapped[str | None] = mapped_column(String(10), nullable=True)
    remote_type: Mapped[str | None] = mapped_column(String(20), nullable=True)

    posted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    first_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    last_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    missed_runs: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true", index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Application(Base):
    """Воронка откликов: субъективное отношение профиля к вакансии."""

    __tablename__ = "applications"
    __table_args__ = (
        UniqueConstraint("profile_id", "vacancy_id", name="uq_application_profile_vacancy"),
    )

    id: Mapped[uuid.UUID] = _uuid_pk()
    profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("profiles.id", ondelete="CASCADE"))
    vacancy_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vacancies.id", ondelete="CASCADE"))

    status: Mapped[str] = mapped_column(String(20), default="new", server_default="new", index=True)
    applied_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    responded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class ParseRun(Base):
    """Журнал прогонов парсера. Нужен для отладки и для отметки усечённой выдачи."""

    __tablename__ = "parse_runs"

    id: Mapped[uuid.UUID] = _uuid_pk()
    source: Mapped[str] = mapped_column(String(50), index=True)
    query_params: Mapped[dict] = mapped_column(JSONB, default=dict)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    found_count: Mapped[int] = mapped_column(Integer, default=0)
    new_count: Mapped[int] = mapped_column(Integer, default=0)
    updated_count: Mapped[int] = mapped_column(Integer, default=0)

    status: Mapped[str] = mapped_column(String(20), default="running")
    error_text: Mapped[str | None] = mapped_column(Text, nullable=True)
```

Допустимые значения `Application.status`: `new`, `applied`, `call`, `interview`, `offer`,
`rejected`, `ignored`. Допустимые значения `ParseRun.status`: `running`, `success`,
`truncated`, `failed`.

- [ ] **Step 5: Поднять БД и запустить тест**

```bash
docker compose up -d db
uv run pytest tests/integration/test_models.py -v
```

Expected: PASS, 3 passed

- [ ] **Step 6: Настроить Alembic**

```bash
uv run alembic init migrations
```

Шаблон нужен обычный, синхронный: драйвер `psycopg` используется в синхронном режиме.
Флаг `-t async` здесь применять нельзя — он сгенерирует несовместимый `env.py`.

Затем заменить содержимое `migrations/env.py` на:

```python
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from jobhunt.config import settings
from jobhunt.db.base import Base
from jobhunt.db import models  # noqa: F401  — регистрирует модели в metadata

config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=settings.database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

- [ ] **Step 7: Сгенерировать и применить миграцию**

```bash
uv run alembic revision --autogenerate -m "initial: profiles, vacancies, applications, parse_runs"
uv run alembic upgrade head
```

Expected: в `migrations/versions/` появился файл с четырьмя `op.create_table`; `upgrade head` завершается без ошибок.

Открыть сгенерированный файл и проверить глазами, что созданы именно четыре таблицы и оба
уникальных ограничения. Автогенерация иногда пропускает `server_default` — если в файле нет
`server_default="0"` у `missed_runs` и `server_default="true"` у `is_active`, дописать вручную.

- [ ] **Step 8: Commit**

```bash
git add src/jobhunt/db alembic.ini migrations tests
git commit -m "feat: схема БД и первая миграция"
```

---

## Task 3: HTTP-клиент с паузами, кешем и проверкой robots.txt

**Files:**
- Create: `src/jobhunt/http_client.py`
- Create: `scripts/capture_fixture.py`
- Test: `tests/unit/test_http_client.py`

**Interfaces:**
- Consumes: `jobhunt.config.settings`
- Produces: `jobhunt.http_client.HttpClient` с методами `get(url: str) -> str` и `close() -> None`; исключение `RobotsDisallowed`

- [ ] **Step 1: Написать падающий тест на паузу между запросами**

Создать `tests/unit/__init__.py` (пустой) и `tests/unit/test_http_client.py`:

```python
import time

import httpx
import pytest

from jobhunt.http_client import HttpClient, RobotsDisallowed


def _transport(handler):
    return httpx.MockTransport(handler)


def test_get_returns_body():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text="<html>ok</html>")

    client = HttpClient(transport=_transport(handler), delay_seconds=0)
    assert client.get("https://example.com/jobs/") == "<html>ok</html>"
    client.close()


def test_waits_between_requests_to_same_host():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text="ok")

    client = HttpClient(transport=_transport(handler), delay_seconds=0.2)
    client.get("https://example.com/a")

    start = time.monotonic()
    client.get("https://example.com/b")
    elapsed = time.monotonic() - start
    client.close()

    assert elapsed >= 0.2, "второй запрос к тому же хосту не выдержал паузу"


def test_raises_when_robots_disallows():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text="User-agent: *\nDisallow: /secret/\n")
        return httpx.Response(200, text="body")

    client = HttpClient(transport=_transport(handler), delay_seconds=0, check_robots=True)
    with pytest.raises(RobotsDisallowed):
        client.get("https://example.com/secret/page")
    client.close()


def test_allows_when_robots_permits():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/robots.txt":
            return httpx.Response(200, text="User-agent: *\nDisallow: /secret/\n")
        return httpx.Response(200, text="body")

    client = HttpClient(transport=_transport(handler), delay_seconds=0, check_robots=True)
    assert client.get("https://example.com/jobs/1/") == "body"
    client.close()
```

- [ ] **Step 2: Запустить тест и убедиться, что он падает**

Run: `uv run pytest tests/unit/test_http_client.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.http_client'`

- [ ] **Step 3: Реализовать клиент**

Создать `src/jobhunt/http_client.py`:

```python
import hashlib
import time
import urllib.robotparser
from pathlib import Path
from urllib.parse import urlsplit

import httpx

from jobhunt.config import settings


class RobotsDisallowed(RuntimeError):
    """Площадка запрещает обход этого пути в robots.txt."""


class HttpClient:
    """HTTP-клиент, вежливый к площадкам.

    Держит паузу между запросами к одному хосту, умеет проверять robots.txt
    и кешировать ответы на диск, чтобы при отладке парсера не дёргать живой сайт.
    """

    def __init__(
        self,
        transport: httpx.BaseTransport | None = None,
        delay_seconds: float | None = None,
        check_robots: bool = False,
        cache_dir: Path | None = None,
        cache_enabled: bool | None = None,
    ) -> None:
        self._delay = settings.request_delay_seconds if delay_seconds is None else delay_seconds
        self._check_robots = check_robots
        self._cache_enabled = (
            settings.http_cache_enabled if cache_enabled is None else cache_enabled
        )
        self._cache_dir = cache_dir or settings.http_cache_dir
        self._last_request_at: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser] = {}
        self._client = httpx.Client(
            transport=transport,
            timeout=settings.request_timeout_seconds,
            follow_redirects=True,
            headers={
                "User-Agent": settings.user_agent,
                "Accept-Language": "uk,ru;q=0.8,en;q=0.6",
            },
        )

    def get(self, url: str) -> str:
        cached = self._read_cache(url)
        if cached is not None:
            return cached

        if self._check_robots and not self._robots_allows(url):
            raise RobotsDisallowed(f"robots.txt запрещает обход: {url}")

        self._respect_delay(url)
        response = self._client.get(url)
        response.raise_for_status()
        self._last_request_at[urlsplit(url).netloc] = time.monotonic()

        self._write_cache(url, response.text)
        return response.text

    def close(self) -> None:
        self._client.close()

    def _respect_delay(self, url: str) -> None:
        host = urlsplit(url).netloc
        previous = self._last_request_at.get(host)
        if previous is None or self._delay <= 0:
            return
        remaining = self._delay - (time.monotonic() - previous)
        if remaining > 0:
            time.sleep(remaining)

    def _robots_allows(self, url: str) -> bool:
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        parser = self._robots.get(origin)
        if parser is None:
            parser = urllib.robotparser.RobotFileParser()
            try:
                body = self._client.get(f"{origin}/robots.txt").text
                parser.parse(body.splitlines())
            except httpx.HTTPError:
                # robots.txt недоступен — трактуем как разрешение, но паузы соблюдаем
                parser.parse(["User-agent: *", "Allow: /"])
            self._robots[origin] = parser
        return parser.can_fetch(settings.user_agent, url)

    def _cache_path(self, url: str) -> Path:
        digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:32]
        return self._cache_dir / f"{digest}.html"

    def _read_cache(self, url: str) -> str | None:
        if not self._cache_enabled:
            return None
        path = self._cache_path(url)
        return path.read_text(encoding="utf-8") if path.exists() else None

    def _write_cache(self, url: str, body: str) -> None:
        if not self._cache_enabled:
            return
        path = self._cache_path(url)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/unit/test_http_client.py -v`
Expected: PASS, 4 passed

- [ ] **Step 5: Создать скрипт захвата фикстур**

Создать `scripts/capture_fixture.py`:

```python
"""Сохраняет живую страницу в каталог фикстур.

Запуск:
    uv run python scripts/capture_fixture.py <url> <имя-файла>

Пример:
    uv run python scripts/capture_fixture.py \
        "https://www.work.ua/jobs/?search=IT+director" work_ua_list.html
"""

import sys
from pathlib import Path

from jobhunt.http_client import HttpClient

FIXTURES = Path(__file__).resolve().parents[1] / "tests" / "fixtures"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1

    url, filename = sys.argv[1], sys.argv[2]
    client = HttpClient(check_robots=True)
    try:
        body = client.get(url)
    finally:
        client.close()

    target = FIXTURES / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8")
    print(f"сохранено {len(body)} символов -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Захватить фикстуры**

```bash
uv run python scripts/capture_fixture.py "https://www.work.ua/jobs/?search=%D0%BA%D0%B5%D1%80%D1%96%D0%B2%D0%BD%D0%B8%D0%BA+it" html/work_ua_list.html
uv run python scripts/capture_fixture.py "https://www.work.ua/jobs/8294127/" html/work_ua_detail.html
uv run python scripts/capture_fixture.py "https://jobs.dou.ua/vacancies/feeds/?search=IT%20Director" xml/dou_feed.xml
```

Expected: три файла в `tests/fixtures/`. Размеры порядка 280 КБ, 120 КБ и 11 КБ соответственно.

Если вакансия `8294127` уже закрыта и вернулся 404 — взять любой другой `href` вида
`/jobs/<id>/` из захваченного `work_ua_list.html` и использовать его; имя файла фикстуры
оставить тем же.

- [ ] **Step 7: Commit**

```bash
git add src/jobhunt/http_client.py scripts tests
git commit -m "feat: HTTP-клиент с паузами, кешем и проверкой robots.txt"
```

---

## Task 4: Интерфейс парсеров и DTO

**Files:**
- Create: `src/jobhunt/parsers/__init__.py`, `src/jobhunt/parsers/base.py`
- Test: `tests/unit/test_parser_boundaries.py`

**Interfaces:**
- Consumes: ничего
- Produces: `VacancyDTO` (pydantic-модель с полями `source`, `external_id`, `title`, `company`, `url`, `description_raw`, `location`, `salary_min`, `salary_max`, `salary_currency`, `remote_type`, `posted_at`); `BaseParser` с абстрактными `source_name: str`, `fetch_listings(query: str) -> list[VacancyDTO]`; `ParserStructureError`; `ParseResult` (поля `vacancies: list[VacancyDTO]`, `truncated: bool`)

- [ ] **Step 1: Написать тест границы модуля**

Создать `tests/unit/test_parser_boundaries.py`:

```python
import ast
import pathlib

PARSERS_DIR = pathlib.Path(__file__).resolve().parents[2] / "src" / "jobhunt" / "parsers"
FORBIDDEN = ("jobhunt.db", "jobhunt.ingest", "sqlalchemy")


def _imported_modules(path: pathlib.Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def test_parsers_package_exists():
    """Без этой проверки тест границы прошёл бы на пустом каталоге и ничего не значил."""
    assert (PARSERS_DIR / "base.py").exists(), "не создан src/jobhunt/parsers/base.py"


def test_parsers_do_not_import_persistence_layer():
    """Парсеры не знают о базе. Это позволяет тестировать их на фикстурах."""
    offenders = []
    for path in PARSERS_DIR.glob("*.py"):
        for module in _imported_modules(path):
            if module.startswith(FORBIDDEN):
                offenders.append(f"{path.name} импортирует {module}")
    assert offenders == [], "нарушена граница модуля parsers: " + "; ".join(offenders)
```

- [ ] **Step 2: Запустить тест и убедиться, что он падает**

Run: `uv run pytest tests/unit/test_parser_boundaries.py -v`
Expected: FAIL — `test_parsers_package_exists` падает с сообщением «не создан src/jobhunt/parsers/base.py»

- [ ] **Step 3: Создать DTO и базовый класс**

Создать `src/jobhunt/parsers/__init__.py` (пустой) и `src/jobhunt/parsers/base.py`:

```python
from abc import ABC, abstractmethod
from datetime import datetime

from pydantic import BaseModel, Field


class ParserStructureError(RuntimeError):
    """Разметка источника изменилась: ожидаемый элемент не найден.

    Поднимается вместо тихого возврата пустого списка — иначе поломка вёрстки
    выглядит как «сегодня вакансий нет».
    """


class VacancyDTO(BaseModel):
    """Вакансия в том виде, в каком её отдал источник. О базе ничего не знает."""

    source: str
    external_id: str
    title: str
    url: str
    description_raw: str

    company: str | None = None
    location: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    salary_currency: str | None = None
    remote_type: str | None = None
    posted_at: datetime | None = None


class ParseResult(BaseModel):
    """Результат прогона одного источника.

    truncated=True означает, что источник отдал не всё: выдача упёрлась в лимит.
    Это состояние обязано доходить до журнала прогонов, а не теряться.
    """

    vacancies: list[VacancyDTO] = Field(default_factory=list)
    truncated: bool = False


class BaseParser(ABC):
    """Единый интерфейс источника вакансий."""

    source_name: str

    @abstractmethod
    def fetch_listings(self, query: str) -> ParseResult:
        """Собрать вакансии по поисковому запросу, включая полный текст описания."""
```

- [ ] **Step 4: Запустить тест и убедиться, что он проходит**

Run: `uv run pytest tests/unit/test_parser_boundaries.py -v`
Expected: PASS, 2 passed

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/parsers tests
git commit -m "feat: интерфейс BaseParser и DTO вакансии"
```

---

## Task 5: Парсер work.ua — разбор списка

**Files:**
- Create: `src/jobhunt/parsers/work_ua.py`
- Test: `tests/unit/test_work_ua_listing.py`

**Interfaces:**
- Consumes: `VacancyDTO`, `ParseResult`, `ParserStructureError` из `jobhunt.parsers.base`
- Produces: `jobhunt.parsers.work_ua.parse_listing(html: str) -> list[VacancyDTO]`, `parse_salary(text: str) -> tuple[int | None, int | None, str | None]`, `parse_posted_at(title_attr: str) -> datetime | None`

- [ ] **Step 1: Написать падающие тесты разбора списка**

Создать `tests/unit/test_work_ua_listing.py`:

```python
from datetime import UTC, datetime
from pathlib import Path

import pytest

from jobhunt.parsers.base import ParserStructureError
from jobhunt.parsers.work_ua import parse_listing, parse_posted_at, parse_salary

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "html" / "work_ua_list.html"


@pytest.fixture(scope="module")
def listing_html() -> str:
    return FIXTURE.read_text(encoding="utf-8")


def test_parses_all_cards(listing_html):
    vacancies = parse_listing(listing_html)
    assert len(vacancies) >= 10, "на странице work.ua ожидается около 14 карточек"


def test_first_card_has_core_fields(listing_html):
    first = parse_listing(listing_html)[0]
    assert first.source == "work.ua"
    assert first.external_id.isdigit()
    assert first.title
    assert first.url.startswith("https://www.work.ua/jobs/")
    assert first.url.endswith(f"/{first.external_id}/")


def test_external_id_is_unique_across_cards(listing_html):
    ids = [v.external_id for v in parse_listing(listing_html)]
    assert len(ids) == len(set(ids))


def test_raises_when_container_missing():
    with pytest.raises(ParserStructureError):
        parse_listing("<html><body>ничего похожего</body></html>")


@pytest.mark.parametrize(
    "text,expected",
    [
        ("80 000 – 120 000 грн", (80000, 120000, "UAH")),
        ("від 50 000 грн", (50000, None, "UAH")),
        ("", (None, None, None)),
    ],
)
def test_parse_salary(text, expected):
    assert parse_salary(text) == expected


def test_parse_posted_at():
    result = parse_posted_at("Керівник відділу, вакансія від 3 серпня 2026")
    assert result == datetime(2026, 8, 3, tzinfo=UTC)


def test_parse_posted_at_returns_none_when_absent():
    assert parse_posted_at("Керівник відділу") is None
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/unit/test_work_ua_listing.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.parsers.work_ua'`

- [ ] **Step 3: Реализовать разбор списка**

Создать `src/jobhunt/parsers/work_ua.py`:

```python
import re
from datetime import UTC, datetime
from urllib.parse import quote_plus

from bs4 import BeautifulSoup, Tag

from jobhunt.parsers.base import BaseParser, ParseResult, ParserStructureError, VacancyDTO

SOURCE_NAME = "work.ua"
BASE_URL = "https://www.work.ua"

# Пробелы, которыми work.ua разделяет разряды в зарплате: узкий неразрывный (&#8239;),
# тонкий (&thinsp;) и обычный неразрывный (&nbsp;). Глазами они неотличимы от обычного
# пробела, поэтому заданы кодами, а не литералами.
_THIN_SPACES = (" ", " ", " ")

UA_MONTHS = {
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

_POSTED_RE = re.compile(r"вакансія від (\d{1,2})\s+([а-яіїєґ]+)\s+(\d{4})", re.IGNORECASE)


def parse_salary(text: str) -> tuple[int | None, int | None, str | None]:
    """Разобрать строку зарплаты в диапазон и валюту."""
    if not text.strip():
        return None, None, None

    normalized = text
    for char in _THIN_SPACES:
        normalized = normalized.replace(char, " ")

    numbers = [int(match.replace(" ", "")) for match in re.findall(r"\d[\d ]*\d|\d", normalized)]
    currency = "UAH" if "грн" in normalized else None

    if not numbers:
        return None, None, currency
    if len(numbers) == 1:
        return numbers[0], None, currency
    return numbers[0], numbers[1], currency


def parse_posted_at(title_attr: str) -> datetime | None:
    """Достать дату публикации из атрибута title ссылки на вакансию."""
    match = _POSTED_RE.search(title_attr)
    if match is None:
        return None
    day, month_name, year = match.groups()
    month = UA_MONTHS.get(month_name.lower())
    if month is None:
        return None
    # Площадка не указывает время и часовой пояс — фиксируем полночь UTC,
    # чтобы в базе не оказалось наивных дат вперемешку с осознанными.
    return datetime(int(year), month, int(day), tzinfo=UTC)


def _block_with_icon(card: Tag, icon_class: str) -> Tag | None:
    for block in card.select("div.text-indent"):
        if block.select_one(f".{icon_class}") is not None:
            return block
    return None


def _extract_city(company_block: Tag) -> str | None:
    """Город лежит в блоке компании — первым span-ом после списка бейджей."""
    badges = company_block.find("ul")
    candidates = badges.next_siblings if badges is not None else company_block.children
    for sibling in candidates:
        if getattr(sibling, "name", None) != "span":
            continue
        text = sibling.get_text(" ", strip=True)
        if text and "км" not in text:
            return text.rstrip(", ").strip() or None
    return None


def parse_listing(html: str) -> list[VacancyDTO]:
    """Разобрать страницу выдачи work.ua в список вакансий без полного описания."""
    soup = BeautifulSoup(html, "lxml")
    container = soup.select_one("#pjax-jobs-list")
    if container is None:
        raise ParserStructureError(
            "work.ua: не найден контейнер #pjax-jobs-list — вероятно, изменилась вёрстка"
        )

    vacancies: list[VacancyDTO] = []
    for card in container.select("div.card.job-link"):
        link = card.select_one('h2 a[href^="/jobs/"]')
        if link is None:
            continue

        href = str(link["href"])
        external_id = href.strip("/").split("/")[-1]
        if not external_id.isdigit():
            continue

        salary_block = _block_with_icon(card, "glyphicon-hryvnia-fill")
        salary_text = ""
        if salary_block is not None:
            value = salary_block.select_one("span.strong-600")
            salary_text = value.get_text(" ", strip=True) if value else ""
        salary_min, salary_max, currency = parse_salary(salary_text)

        company_block = _block_with_icon(card, "glyphicon-company")
        company = None
        location = None
        if company_block is not None:
            name = company_block.select_one("span.strong-600")
            company = name.get_text(" ", strip=True) if name else None
            location = _extract_city(company_block)

        snippet = card.select_one("p.ellipsis-line-3")

        vacancies.append(
            VacancyDTO(
                source=SOURCE_NAME,
                external_id=external_id,
                title=link.get_text(" ", strip=True),
                url=f"{BASE_URL}/jobs/{external_id}/",
                description_raw=snippet.get_text(" ", strip=True) if snippet else "",
                company=company,
                location=location,
                salary_min=salary_min,
                salary_max=salary_max,
                salary_currency=currency,
                posted_at=parse_posted_at(str(link.get("title", ""))),
            )
        )

    if not vacancies:
        raise ParserStructureError(
            "work.ua: контейнер найден, но ни одна карточка не разобрана — изменилась вёрстка"
        )
    return vacancies
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/unit/test_work_ua_listing.py -v`
Expected: PASS, 9 passed

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/parsers/work_ua.py tests
git commit -m "feat: разбор страницы выдачи work.ua"
```

---

## Task 6: Парсер work.ua — детальная страница и сборка

**Files:**
- Modify: `src/jobhunt/parsers/work_ua.py`
- Test: `tests/unit/test_work_ua_detail.py`

**Interfaces:**
- Consumes: `jobhunt.http_client.HttpClient`, `parse_listing` из Task 5
- Produces: `jobhunt.parsers.work_ua.parse_detail(html: str) -> str`, класс `WorkUaParser(BaseParser)` с `source_name = "work.ua"`, конструктором `__init__(self, client, max_details: int = 25)` и методом `fetch_listings(query: str) -> ParseResult`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/unit/test_work_ua_detail.py`:

```python
from pathlib import Path

import pytest

from jobhunt.parsers.base import ParserStructureError
from jobhunt.parsers.work_ua import WorkUaParser, parse_detail

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "html"


def test_parse_detail_extracts_description():
    html = (FIXTURES / "work_ua_detail.html").read_text(encoding="utf-8")
    description = parse_detail(html)
    assert len(description) > 200, "полное описание вакансии должно быть заметно длиннее сниппета"


def test_parse_detail_raises_when_block_missing():
    with pytest.raises(ParserStructureError):
        parse_detail("<html><body><h1>Заголовок</h1></body></html>")


def test_fetch_listings_combines_listing_and_details():
    listing = (FIXTURES / "work_ua_list.html").read_text(encoding="utf-8")
    detail = (FIXTURES / "work_ua_detail.html").read_text(encoding="utf-8")

    class FakeClient:
        def __init__(self):
            self.urls: list[str] = []

        def get(self, url: str) -> str:
            self.urls.append(url)
            return listing if "search=" in url else detail

        def close(self) -> None:
            pass

    client = FakeClient()
    parser = WorkUaParser(client=client, max_details=3)
    result = parser.fetch_listings("керівник it")

    assert len(result.vacancies) >= 10
    # запрошены страница выдачи и три детальных
    assert len(client.urls) == 4
    assert all(len(v.description_raw) > 200 for v in result.vacancies[:3])
    # карточек больше, чем лимит детальных запросов, — часть вакансий осталась
    # со сниппетом вместо полного описания, и это обязано быть видно снаружи
    assert result.truncated is True


def test_fetch_listings_not_truncated_when_limit_is_high():
    listing = (FIXTURES / "work_ua_list.html").read_text(encoding="utf-8")
    detail = (FIXTURES / "work_ua_detail.html").read_text(encoding="utf-8")

    class FakeClient:
        def get(self, url: str) -> str:
            return listing if "search=" in url else detail

        def close(self) -> None:
            pass

    result = WorkUaParser(client=FakeClient(), max_details=50).fetch_listings("керівник it")
    assert result.truncated is False
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/unit/test_work_ua_detail.py -v`
Expected: FAIL с `ImportError: cannot import name 'WorkUaParser'`

- [ ] **Step 3: Добавить разбор детальной страницы и класс парсера**

Дописать в конец `src/jobhunt/parsers/work_ua.py`. Новых импортов не требуется — `quote_plus`,
`BaseParser` и `ParseResult` уже добавлены в блок импортов в Task 5.

```python
def parse_detail(html: str) -> str:
    """Достать полный текст описания с детальной страницы вакансии."""
    soup = BeautifulSoup(html, "lxml")
    block = soup.select_one("#job-description")
    if block is None:
        raise ParserStructureError(
            "work.ua: не найден блок #job-description — вероятно, изменилась вёрстка"
        )
    return block.get_text("\n", strip=True)


class WorkUaParser(BaseParser):
    """Источник work.ua.

    Страница выдачи содержит только сниппет описания, поэтому за полным текстом
    приходится ходить на детальную страницу каждой вакансии. Количество таких
    запросов ограничено max_details, чтобы один прогон не превращался в сотню
    обращений к сайту.

    truncated=True означает, что карточек оказалось больше лимита и часть вакансий
    осталась со сниппетом вместо полного описания. Матчинг по сниппету заметно хуже,
    поэтому это состояние не замалчивается, а доходит до журнала прогонов.
    """

    source_name = SOURCE_NAME

    def __init__(self, client, max_details: int = 25) -> None:
        self._client = client
        self._max_details = max_details

    def fetch_listings(self, query: str) -> ParseResult:
        listing_url = f"{BASE_URL}/jobs/?search={quote_plus(query)}"
        vacancies = parse_listing(self._client.get(listing_url))

        for vacancy in vacancies[: self._max_details]:
            try:
                vacancy.description_raw = parse_detail(self._client.get(vacancy.url))
            except ParserStructureError:
                # Детальная страница могла измениться или вакансию уже сняли —
                # сниппет из выдачи остаётся как запасной вариант.
                continue

        truncated = len(vacancies) > self._max_details
        return ParseResult(vacancies=vacancies, truncated=truncated)
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/unit/ -v`
Expected: PASS, все тесты зелёные

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/parsers/work_ua.py tests
git commit -m "feat: детальная страница work.ua и класс WorkUaParser"
```

---

## Task 7: Парсер dou.ua на основе RSS

**Files:**
- Create: `src/jobhunt/parsers/dou.py`, `src/jobhunt/parsers/registry.py`
- Test: `tests/unit/test_dou.py`

**Interfaces:**
- Consumes: `VacancyDTO`, `ParseResult`, `ParserStructureError`, `BaseParser`
- Produces: `jobhunt.parsers.dou.parse_feed(xml_text: str) -> ParseResult`, `parse_item_title(title: str) -> tuple[str, str | None, str | None]`, класс `DouParser(BaseParser)`; `jobhunt.parsers.registry.get_parser(source: str, client) -> BaseParser`, `jobhunt.parsers.registry.ALL_SOURCES: tuple[str, ...]`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/unit/test_dou.py`:

```python
from pathlib import Path

import pytest

from jobhunt.parsers.base import ParserStructureError
from jobhunt.parsers.dou import DouParser, parse_feed, parse_item_title

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "xml" / "dou_feed.xml"


@pytest.fixture(scope="module")
def feed_xml() -> str:
    return FIXTURE.read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("Head of IT в WayForPay, віддалено", ("Head of IT", "WayForPay", "віддалено")),
        ("Керівник IT відділу в INSPE, Львів", ("Керівник IT відділу", "INSPE", "Львів")),
        ("Просто заголовок", ("Просто заголовок", None, None)),
    ],
)
def test_parse_item_title(raw, expected):
    assert parse_item_title(raw) == expected


def test_parse_feed_extracts_vacancies(feed_xml):
    result = parse_feed(feed_xml)
    assert result.vacancies, "фид должен содержать хотя бы одну вакансию"

    first = result.vacancies[0]
    assert first.source == "dou.ua"
    assert first.external_id.isdigit()
    assert first.title
    assert first.company
    assert "utm_source" not in first.url, "трекинговый параметр должен быть отброшен"
    assert len(first.description_raw) > 200, "в фиде лежит полное описание, а не сниппет"
    assert first.posted_at is not None


def test_remote_type_detected_from_location(feed_xml):
    remote = [v for v in parse_feed(feed_xml).vacancies if v.location == "віддалено"]
    assert all(v.remote_type == "remote" for v in remote)


def test_parse_feed_raises_on_garbage():
    with pytest.raises(ParserStructureError):
        parse_feed("не xml вовсе")


def test_truncated_flag_when_feed_hits_limit():
    items = "".join(
        f"<item><title>Роль {i} в Компанія, Київ</title>"
        f"<link>https://jobs.dou.ua/companies/c/vacancies/{1000 + i}/</link>"
        f"<description>&lt;p&gt;текст&lt;/p&gt;</description>"
        f"<pubDate>Wed, 15 Jul 2026 17:50:04 +0300</pubDate></item>"
        for i in range(25)
    )
    xml = f'<?xml version="1.0"?><rss version="2.0"><channel>{items}</channel></rss>'
    assert parse_feed(xml).truncated is True


def test_fetch_listings_requests_feed_url():
    class FakeClient:
        def __init__(self):
            self.urls: list[str] = []

        def get(self, url: str) -> str:
            self.urls.append(url)
            return FIXTURE.read_text(encoding="utf-8")

        def close(self) -> None:
            pass

    client = FakeClient()
    result = DouParser(client=client).fetch_listings("IT Director")

    assert len(client.urls) == 1, "dou.ua обслуживается одним запросом — фид содержит всё"
    assert client.urls[0].startswith("https://jobs.dou.ua/vacancies/feeds/?search=")
    assert result.vacancies
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/unit/test_dou.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.parsers.dou'`

- [ ] **Step 3: Реализовать парсер dou.ua**

Создать `src/jobhunt/parsers/dou.py`:

```python
import re
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from urllib.parse import quote, urlsplit, urlunsplit

from bs4 import BeautifulSoup

from jobhunt.parsers.base import BaseParser, ParseResult, ParserStructureError, VacancyDTO

SOURCE_NAME = "dou.ua"
FEED_URL = "https://jobs.dou.ua/vacancies/feeds/"

# Фид отдаёт не больше 25 элементов на поисковый запрос и не больше 50 на общий.
# Достижение порога означает, что выдача усечена и часть вакансий не видна.
FEED_ITEM_LIMIT = 25

_ID_RE = re.compile(r"/vacancies/(\d+)/")
_TITLE_RE = re.compile(r"^(?P<title>.+?)\s+в\s+(?P<rest>.+)$")

REMOTE_MARKERS = ("віддалено", "удаленно", "remote")


def parse_item_title(title: str) -> tuple[str, str | None, str | None]:
    """Разобрать заголовок фида «Роль в Компанія, Місто» на составные части."""
    match = _TITLE_RE.match(title.strip())
    if match is None:
        return title.strip(), None, None

    role = match.group("title").strip()
    rest = match.group("rest").strip()
    if "," in rest:
        company, location = rest.rsplit(",", 1)
        return role, company.strip() or None, location.strip() or None
    return role, rest or None, None


def _clean_url(raw: str) -> str:
    """Убрать трекинговые параметры из ссылки — они мешают дедупликации."""
    parts = urlsplit(raw.strip())
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def _html_to_text(html: str) -> str:
    return BeautifulSoup(html, "lxml").get_text("\n", strip=True)


def parse_feed(xml_text: str) -> ParseResult:
    """Разобрать RSS-фид dou.ua. Описание в фиде полное, детальные страницы не нужны."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise ParserStructureError(f"dou.ua: фид не разбирается как XML: {exc}") from exc

    items = root.findall("./channel/item")
    vacancies: list[VacancyDTO] = []

    for item in items:
        link_raw = (item.findtext("link") or "").strip()
        id_match = _ID_RE.search(link_raw)
        if id_match is None:
            continue

        title_raw = (item.findtext("title") or "").strip()
        role, company, location = parse_item_title(title_raw)

        if company is None:
            slug_match = re.search(r"/companies/([^/]+)/", link_raw)
            company = slug_match.group(1) if slug_match else None

        posted_at = None
        pub_date = item.findtext("pubDate")
        if pub_date:
            try:
                posted_at = parsedate_to_datetime(pub_date)
            except (TypeError, ValueError):
                posted_at = None

        remote_type = None
        if location and any(marker in location.lower() for marker in REMOTE_MARKERS):
            remote_type = "remote"

        vacancies.append(
            VacancyDTO(
                source=SOURCE_NAME,
                external_id=id_match.group(1),
                title=role,
                url=_clean_url(link_raw),
                description_raw=_html_to_text(item.findtext("description") or ""),
                company=company,
                location=location,
                remote_type=remote_type,
                posted_at=posted_at,
            )
        )

    return ParseResult(vacancies=vacancies, truncated=len(items) >= FEED_ITEM_LIMIT)


class DouParser(BaseParser):
    """Источник dou.ua. Один запрос к RSS отдаёт и список, и полные описания."""

    source_name = SOURCE_NAME

    def __init__(self, client) -> None:
        self._client = client

    def fetch_listings(self, query: str) -> ParseResult:
        url = f"{FEED_URL}?search={quote(query)}"
        return parse_feed(self._client.get(url))
```

- [ ] **Step 4: Создать реестр парсеров**

Создать `src/jobhunt/parsers/registry.py`:

```python
from jobhunt.parsers.base import BaseParser
from jobhunt.parsers.dou import DouParser
from jobhunt.parsers.work_ua import WorkUaParser

ALL_SOURCES: tuple[str, ...] = ("work.ua", "dou.ua")

_FACTORIES = {
    "work.ua": WorkUaParser,
    "dou.ua": DouParser,
}


def get_parser(source: str, client) -> BaseParser:
    """Создать парсер по имени источника."""
    factory = _FACTORIES.get(source)
    if factory is None:
        known = ", ".join(sorted(_FACTORIES))
        raise ValueError(f"неизвестный источник {source!r}; доступны: {known}")
    return factory(client=client)
```

- [ ] **Step 5: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/unit/ -v`
Expected: PASS, все зелёные, включая `test_parsers_do_not_import_persistence_layer`

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/parsers tests
git commit -m "feat: парсер dou.ua на RSS и реестр источников"
```

---

## Task 8: Вставка и дедупликация вакансий

**Files:**
- Create: `src/jobhunt/ingest/__init__.py`, `src/jobhunt/ingest/upsert.py`
- Test: `tests/integration/test_upsert.py`

**Interfaces:**
- Consumes: `VacancyDTO`, модель `Vacancy`, `session_scope`
- Produces: `jobhunt.ingest.upsert.description_hash(text: str) -> str`, `jobhunt.ingest.upsert.upsert_vacancies(session, dtos: list[VacancyDTO]) -> UpsertStats`; `UpsertStats` с полями `new: int`, `updated: int`, `changed_description: list[str]`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_upsert.py`:

```python
from jobhunt.db.models import Vacancy
from jobhunt.ingest.upsert import description_hash, upsert_vacancies
from jobhunt.parsers.base import VacancyDTO


def _dto(external_id="1", description="Опис вакансії", title="Head of IT") -> VacancyDTO:
    return VacancyDTO(
        source="work.ua",
        external_id=external_id,
        title=title,
        url=f"https://www.work.ua/jobs/{external_id}/",
        description_raw=description,
        company="Garvis",
        location="Дніпро",
    )


def test_inserts_new_vacancy(session):
    stats = upsert_vacancies(session, [_dto()])
    session.commit()

    assert stats.new == 1
    assert stats.updated == 0
    assert session.query(Vacancy).count() == 1


def test_second_run_does_not_duplicate(session):
    upsert_vacancies(session, [_dto()])
    session.commit()
    stats = upsert_vacancies(session, [_dto()])
    session.commit()

    assert stats.new == 0
    assert stats.updated == 1
    assert session.query(Vacancy).count() == 1


def test_updates_last_seen_and_resets_missed_runs(session):
    upsert_vacancies(session, [_dto()])
    session.commit()

    vacancy = session.query(Vacancy).one()
    vacancy.missed_runs = 2
    vacancy.is_active = False
    session.commit()
    previous_seen = vacancy.last_seen_at

    upsert_vacancies(session, [_dto()])
    session.commit()
    session.refresh(vacancy)

    assert vacancy.missed_runs == 0
    assert vacancy.is_active is True, "вакансия снова появилась в выдаче — она снова активна"
    assert vacancy.last_seen_at >= previous_seen


def test_detects_changed_description(session):
    upsert_vacancies(session, [_dto(description="Старый текст")])
    session.commit()

    stats = upsert_vacancies(session, [_dto(description="Новый текст с другими требованиями")])
    session.commit()

    assert stats.changed_description == ["1"]
    vacancy = session.query(Vacancy).one()
    assert vacancy.description_raw == "Новый текст с другими требованиями"
    assert vacancy.description_hash == description_hash("Новый текст с другими требованиями")


def test_same_external_id_different_source_are_distinct(session):
    dou = _dto().model_copy(update={"source": "dou.ua"})
    upsert_vacancies(session, [_dto(), dou])
    session.commit()

    assert session.query(Vacancy).count() == 2
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/integration/test_upsert.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.ingest'`

- [ ] **Step 3: Реализовать upsert**

Создать `src/jobhunt/ingest/__init__.py` (пустой) и `src/jobhunt/ingest/upsert.py`:

```python
import hashlib
from dataclasses import dataclass, field
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import Vacancy
from jobhunt.parsers.base import VacancyDTO


@dataclass
class UpsertStats:
    """Что произошло за один прогон вставки."""

    new: int = 0
    updated: int = 0
    changed_description: list[str] = field(default_factory=list)


def description_hash(text: str) -> str:
    """Хеш описания — по нему ловим правку требований работодателем."""
    return hashlib.sha256(text.strip().encode("utf-8")).hexdigest()


def upsert_vacancies(session: Session, dtos: list[VacancyDTO]) -> UpsertStats:
    """Вставить новые вакансии и обновить уже известные.

    Уникальность определяется парой source + external_id. Повторная встреча
    вакансии сбрасывает счётчик пропусков и возвращает её в активные.
    """
    stats = UpsertStats()
    now = datetime.now(UTC)

    for dto in dtos:
        existing = session.execute(
            select(Vacancy).where(
                Vacancy.source == dto.source,
                Vacancy.external_id == dto.external_id,
            )
        ).scalar_one_or_none()

        new_hash = description_hash(dto.description_raw)

        if existing is None:
            session.add(
                Vacancy(
                    source=dto.source,
                    external_id=dto.external_id,
                    title=dto.title,
                    company=dto.company,
                    url=dto.url,
                    description_raw=dto.description_raw,
                    description_hash=new_hash,
                    location=dto.location,
                    salary_min=dto.salary_min,
                    salary_max=dto.salary_max,
                    salary_currency=dto.salary_currency,
                    remote_type=dto.remote_type,
                    posted_at=dto.posted_at,
                    first_seen_at=now,
                    last_seen_at=now,
                    missed_runs=0,
                    is_active=True,
                )
            )
            stats.new += 1
            continue

        if existing.description_hash != new_hash:
            stats.changed_description.append(dto.external_id)
            existing.description_raw = dto.description_raw
            existing.description_hash = new_hash

        existing.title = dto.title
        existing.company = dto.company
        existing.location = dto.location
        existing.salary_min = dto.salary_min
        existing.salary_max = dto.salary_max
        existing.salary_currency = dto.salary_currency
        existing.remote_type = dto.remote_type
        existing.last_seen_at = now
        existing.missed_runs = 0
        existing.is_active = True
        stats.updated += 1

    session.flush()
    return stats
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/integration/test_upsert.py -v`
Expected: PASS, 5 passed

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/ingest tests
git commit -m "feat: вставка вакансий с дедупликацией по source и external_id"
```

---

## Task 9: Отметка закрытых вакансий

**Files:**
- Create: `src/jobhunt/ingest/activity.py`
- Test: `tests/integration/test_activity.py`

**Interfaces:**
- Consumes: модель `Vacancy`
- Produces: `jobhunt.ingest.activity.mark_missing(session, source: str, seen_external_ids: set[str], threshold: int = 3) -> int` — возвращает количество вакансий, ставших неактивными; константа `MISSED_RUNS_THRESHOLD = 3`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_activity.py`:

```python
from jobhunt.db.models import Vacancy
from jobhunt.ingest.activity import mark_missing
from jobhunt.ingest.upsert import upsert_vacancies
from jobhunt.parsers.base import VacancyDTO


def _dto(external_id: str) -> VacancyDTO:
    return VacancyDTO(
        source="work.ua",
        external_id=external_id,
        title="Head of IT",
        url=f"https://www.work.ua/jobs/{external_id}/",
        description_raw="Опис",
    )


def _seed(session, ids: list[str]) -> None:
    upsert_vacancies(session, [_dto(i) for i in ids])
    session.commit()


def test_increments_missed_runs_for_absent_vacancies(session):
    _seed(session, ["1", "2"])

    mark_missing(session, "work.ua", seen_external_ids={"1"})
    session.commit()

    absent = session.query(Vacancy).filter_by(external_id="2").one()
    present = session.query(Vacancy).filter_by(external_id="1").one()
    assert absent.missed_runs == 1
    assert absent.is_active is True, "одного пропуска мало для деактивации"
    assert present.missed_runs == 0


def test_deactivates_after_three_consecutive_misses(session):
    _seed(session, ["1", "2"])

    for _ in range(3):
        mark_missing(session, "work.ua", seen_external_ids={"1"})
        session.commit()

    absent = session.query(Vacancy).filter_by(external_id="2").one()
    assert absent.missed_runs == 3
    assert absent.is_active is False


def test_returns_number_of_deactivated(session):
    _seed(session, ["1", "2", "3"])

    for _ in range(2):
        mark_missing(session, "work.ua", seen_external_ids={"1"})
        session.commit()
    deactivated = mark_missing(session, "work.ua", seen_external_ids={"1"})
    session.commit()

    assert deactivated == 2


def test_does_not_touch_other_sources(session):
    upsert_vacancies(session, [_dto("1"), _dto("1").model_copy(update={"source": "dou.ua"})])
    session.commit()

    mark_missing(session, "work.ua", seen_external_ids=set())
    session.commit()

    dou = session.query(Vacancy).filter_by(source="dou.ua").one()
    assert dou.missed_runs == 0
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/integration/test_activity.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.ingest.activity'`

- [ ] **Step 3: Реализовать отметку пропусков**

Создать `src/jobhunt/ingest/activity.py`:

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.models import Vacancy

MISSED_RUNS_THRESHOLD = 3


def mark_missing(
    session: Session,
    source: str,
    seen_external_ids: set[str],
    threshold: int = MISSED_RUNS_THRESHOLD,
) -> int:
    """Увеличить счётчик пропусков вакансиям, не встреченным в текущем прогоне.

    Вакансия считается закрытой, когда её не видно threshold прогонов подряд.
    Возвращает количество вакансий, деактивированных именно этим вызовом.
    """
    candidates = session.execute(
        select(Vacancy).where(Vacancy.source == source, Vacancy.is_active.is_(True))
    ).scalars()

    deactivated = 0
    for vacancy in candidates:
        if vacancy.external_id in seen_external_ids:
            continue
        vacancy.missed_runs += 1
        if vacancy.missed_runs >= threshold:
            vacancy.is_active = False
            deactivated += 1

    session.flush()
    return deactivated
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/integration/test_activity.py -v`
Expected: PASS, 4 passed

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/ingest/activity.py tests
git commit -m "feat: отметка закрытых вакансий по счётчику пропусков"
```

---

## Task 10: Оркестратор прогона и журнал

**Files:**
- Create: `src/jobhunt/ingest/runner.py`
- Test: `tests/integration/test_runner.py`

**Interfaces:**
- Consumes: `get_parser`, `upsert_vacancies`, `mark_missing`, модели `ParseRun`, `Profile`
- Produces: `jobhunt.ingest.runner.run_source(session, source: str, query: str, client) -> ParseRun`, `jobhunt.ingest.runner.run_profile(session, profile: Profile, client) -> list[ParseRun]`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_runner.py`:

```python
import pytest

from jobhunt.db.models import ParseRun, Profile, Vacancy
from jobhunt.ingest.runner import run_profile, run_source
from jobhunt.parsers.base import ParseResult, ParserStructureError, VacancyDTO


class FakeParser:
    source_name = "work.ua"

    def __init__(self, result: ParseResult | Exception):
        self._result = result
        self.queries: list[str] = []

    def fetch_listings(self, query: str) -> ParseResult:
        self.queries.append(query)
        if isinstance(self._result, Exception):
            raise self._result
        return self._result


def _result(ids: list[str], truncated: bool = False) -> ParseResult:
    return ParseResult(
        vacancies=[
            VacancyDTO(
                source="work.ua",
                external_id=i,
                title="Head of IT",
                url=f"https://www.work.ua/jobs/{i}/",
                description_raw="Опис",
            )
            for i in ids
        ],
        truncated=truncated,
    )


def test_successful_run_records_counts(session):
    parser = FakeParser(_result(["1", "2"]))
    run = run_source(session, "work.ua", "керівник it", client=None, parser=parser)
    session.commit()

    assert run.status == "success"
    assert run.found_count == 2
    assert run.new_count == 2
    assert run.updated_count == 0
    assert run.finished_at is not None
    assert session.query(Vacancy).count() == 2


def test_truncated_result_is_recorded(session):
    parser = FakeParser(_result(["1"], truncated=True))
    run = run_source(session, "work.ua", "manager", client=None, parser=parser)
    session.commit()

    assert run.status == "truncated", "усечённая выдача обязана быть видна в журнале"


def test_failed_run_records_error_and_reraises(session):
    parser = FakeParser(ParserStructureError("вёрстка изменилась"))

    with pytest.raises(ParserStructureError):
        run_source(session, "work.ua", "manager", client=None, parser=parser)

    run = session.query(ParseRun).one()
    assert run.status == "failed"
    assert "вёрстка изменилась" in run.error_text


def test_second_run_marks_disappeared_vacancy(session):
    run_source(session, "work.ua", "q", client=None, parser=FakeParser(_result(["1", "2"])))
    session.commit()
    run_source(session, "work.ua", "q", client=None, parser=FakeParser(_result(["1"])))
    session.commit()

    gone = session.query(Vacancy).filter_by(external_id="2").one()
    assert gone.missed_runs == 1


def test_run_profile_iterates_all_roles(session):
    profile = Profile(name="Кирилл", target_roles=["IT Director", "Head of IT"])
    session.add(profile)
    session.commit()

    parser = FakeParser(_result(["1"]))
    runs = run_profile(session, profile, client=None, parser_factory=lambda source, client: parser)
    session.commit()

    # два источника × две роли
    assert len(runs) == 4
    assert parser.queries.count("IT Director") == 2
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/integration/test_runner.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.ingest.runner'`

- [ ] **Step 3: Реализовать оркестратор**

Создать `src/jobhunt/ingest/runner.py`:

```python
from collections.abc import Callable
from datetime import UTC, datetime

from sqlalchemy.orm import Session

from jobhunt.db.models import ParseRun, Profile
from jobhunt.ingest.activity import mark_missing
from jobhunt.ingest.upsert import upsert_vacancies
from jobhunt.parsers.base import BaseParser
from jobhunt.parsers.registry import ALL_SOURCES, get_parser


def run_source(
    session: Session,
    source: str,
    query: str,
    client,
    parser: BaseParser | None = None,
) -> ParseRun:
    """Прогнать один источник по одному запросу и записать результат в журнал.

    Ошибка парсера не проглатывается: она фиксируется в журнале и пробрасывается
    дальше, иначе поломка вёрстки выглядела бы как «сегодня вакансий нет».
    """
    parser = parser or get_parser(source, client)

    run = ParseRun(
        source=source,
        query_params={"query": query},
        started_at=datetime.now(UTC),
        status="running",
    )
    session.add(run)
    session.flush()

    try:
        result = parser.fetch_listings(query)
    except Exception as exc:
        run.status = "failed"
        run.error_text = str(exc)
        run.finished_at = datetime.now(UTC)
        session.flush()
        raise

    stats = upsert_vacancies(session, result.vacancies)
    mark_missing(session, source, {v.external_id for v in result.vacancies})

    run.found_count = len(result.vacancies)
    run.new_count = stats.new
    run.updated_count = stats.updated
    run.status = "truncated" if result.truncated else "success"
    run.finished_at = datetime.now(UTC)
    session.flush()
    return run


def run_profile(
    session: Session,
    profile: Profile,
    client,
    sources: tuple[str, ...] = ALL_SOURCES,
    parser_factory: Callable[[str, object], BaseParser] = get_parser,
) -> list[ParseRun]:
    """Прогнать все источники по всем целевым ролям профиля."""
    runs: list[ParseRun] = []
    for source in sources:
        parser = parser_factory(source, client)
        for role in profile.target_roles:
            runs.append(run_source(session, source, role, client=client, parser=parser))
    return runs
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/integration/ -v`
Expected: PASS, все зелёные

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/ingest/runner.py tests
git commit -m "feat: оркестратор прогона парсеров с журналом"
```

---

## Task 11: CLI для запуска парсинга

**Files:**
- Create: `src/jobhunt/cli.py`
- Test: `tests/integration/test_cli.py`

**Interfaces:**
- Consumes: `run_profile`, `session_scope`, `HttpClient`, модель `Profile`
- Produces: `jobhunt.cli.build_parser() -> argparse.ArgumentParser`, `jobhunt.cli.create_profile(session, name: str, roles: list[str], locations: list[str]) -> Profile`, `jobhunt.cli.cmd_init_profile(name, roles, locations) -> None`, `jobhunt.cli.cmd_parse() -> None`, `jobhunt.cli.main(argv: list[str] | None = None) -> int`

- [ ] **Step 1: Написать падающий тест**

Создать `tests/integration/test_cli.py`:

```python
from jobhunt.cli import build_parser, create_profile
from jobhunt.db.models import Profile


def test_cli_parses_init_profile_arguments():
    parser = build_parser()
    args = parser.parse_args(
        ["init-profile", "--name", "Кирилл", "--role", "IT Director", "--role", "Head of IT"]
    )
    assert args.command == "init-profile"
    assert args.name == "Кирилл"
    assert args.role == ["IT Director", "Head of IT"]


def test_cli_parses_parse_command():
    parser = build_parser()
    args = parser.parse_args(["parse"])
    assert args.command == "parse"


def test_init_profile_creates_row(session):
    profile = create_profile(
        session, name="Кирилл", roles=["IT Director"], locations=["Київ"]
    )
    session.commit()

    stored = session.query(Profile).one()
    assert stored.id == profile.id
    assert stored.target_roles == ["IT Director"]
```

- [ ] **Step 2: Запустить тест и убедиться, что он падает**

Run: `uv run pytest tests/integration/test_cli.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.cli'`

- [ ] **Step 3: Реализовать CLI**

Создать `src/jobhunt/cli.py`:

```python
import argparse

from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.base import session_scope
from jobhunt.db.models import Profile
from jobhunt.http_client import HttpClient
from jobhunt.ingest.runner import run_profile


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="jobhunt", description="Job Hunt AI")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init-profile", help="создать профиль поиска")
    init.add_argument("--name", required=True)
    init.add_argument("--role", action="append", default=[], help="целевая роль, можно несколько")
    init.add_argument("--location", action="append", default=[], help="город, можно несколько")

    sub.add_parser("parse", help="собрать вакансии по профилю")
    return parser


def create_profile(
    session: Session, name: str, roles: list[str], locations: list[str]
) -> Profile:
    profile = Profile(name=name, target_roles=roles, locations=locations)
    session.add(profile)
    session.flush()
    return profile


def cmd_init_profile(name: str, roles: list[str], locations: list[str]) -> None:
    with session_scope() as session:
        profile = create_profile(session, name, roles, locations)
        print(f"профиль создан: {profile.name}, роли: {', '.join(roles) or '—'}")


def cmd_parse() -> None:
    with session_scope() as session:
        profile = session.execute(select(Profile).order_by(Profile.created_at)).scalars().first()
        if profile is None:
            print("профиль не найден — сначала выполните: jobhunt init-profile --name ... --role ...")
            return
        if not profile.target_roles:
            print("у профиля не задано ни одной целевой роли — парсить нечего")
            return

        client = HttpClient(check_robots=True)
        try:
            runs = run_profile(session, profile, client=client)
        finally:
            client.close()

        for run in runs:
            marker = " (выдача усечена, сузьте запрос)" if run.status == "truncated" else ""
            print(
                f"{run.source} «{run.query_params['query']}»: "
                f"найдено {run.found_count}, новых {run.new_count}, "
                f"обновлено {run.updated_count}{marker}"
            )


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "init-profile":
        cmd_init_profile(args.name, args.role, args.location)
    elif args.command == "parse":
        cmd_parse()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest tests/integration/test_cli.py -v`
Expected: PASS, 3 passed

- [ ] **Step 5: Живой прогон**

```bash
uv run alembic upgrade head
uv run python -m jobhunt.cli init-profile --name "Кирилл" --role "IT Director" --role "Head of IT"
uv run python -m jobhunt.cli parse
```

Expected: по каждому источнику и роли выводится строка со счётчиками; в БД появились вакансии.

Проверить: `docker compose exec db psql -U jobhunt -c "SELECT source, count(*) FROM vacancies GROUP BY source;"`

Это первый живой контакт с площадками. Если work.ua вернёт 403 — увеличить
`REQUEST_DELAY_SECONDS` в `.env` до 5.0 и повторить.

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/cli.py tests
git commit -m "feat: CLI для создания профиля и запуска парсинга"
```

---

## Task 12: Веб-таблица вакансий

**Files:**
- Modify: `src/jobhunt/web/app.py`
- Create: `src/jobhunt/web/routes/__init__.py`, `src/jobhunt/web/routes/vacancies.py`
- Create: `src/jobhunt/web/templates/base.html`, `src/jobhunt/web/templates/vacancies.html`
- Test: `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Consumes: модели `Vacancy`, `Application`, `Profile`; `session_scope`
- Produces: роут `GET /vacancies` — HTML-страница со списком; функция `jobhunt.web.routes.vacancies.list_vacancies(session, profile_id: uuid.UUID, status: str | None = None, source: str | None = None, include_inactive: bool = False) -> list[dict]`; константа `STATUSES: tuple[str, ...]`; объект `router: APIRouter`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_web_vacancies.py`:

```python
from datetime import UTC, datetime

from jobhunt.db.models import Application, Profile, Vacancy
from jobhunt.web.routes.vacancies import list_vacancies


def _seed(session) -> Profile:
    profile = Profile(name="Кирилл", target_roles=["IT Director"])
    session.add(profile)
    session.flush()

    now = datetime.now(UTC)
    active = Vacancy(
        source="work.ua",
        external_id="1",
        title="Head of IT",
        company="Garvis",
        url="https://www.work.ua/jobs/1/",
        description_raw="Опис",
        description_hash="h1",
        first_seen_at=now,
        last_seen_at=now,
    )
    closed = Vacancy(
        source="dou.ua",
        external_id="2",
        title="IT Director",
        company="WayForPay",
        url="https://jobs.dou.ua/companies/x/vacancies/2/",
        description_raw="Опис",
        description_hash="h2",
        first_seen_at=now,
        last_seen_at=now,
        is_active=False,
    )
    session.add_all([active, closed])
    session.flush()
    session.add(Application(profile_id=profile.id, vacancy_id=active.id, status="applied"))
    session.commit()
    return profile


def test_lists_only_active_by_default(session):
    profile = _seed(session)
    rows = list_vacancies(session, profile.id)
    assert [r["external_id"] for r in rows] == ["1"]


def test_includes_application_status(session):
    profile = _seed(session)
    row = list_vacancies(session, profile.id)[0]
    assert row["status"] == "applied"


def test_vacancy_without_application_has_new_status(session):
    profile = _seed(session)
    vacancy = session.query(Vacancy).filter_by(external_id="1").one()
    session.query(Application).filter_by(vacancy_id=vacancy.id).delete()
    session.commit()

    assert list_vacancies(session, profile.id)[0]["status"] == "new"


def test_filters_by_source(session):
    profile = _seed(session)
    assert list_vacancies(session, profile.id, source="dou.ua", include_inactive=True)
    assert list_vacancies(session, profile.id, source="work.ua")[0]["source"] == "work.ua"
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/integration/test_web_vacancies.py -v`
Expected: FAIL с `ModuleNotFoundError: No module named 'jobhunt.web.routes'`

- [ ] **Step 3: Реализовать выборку и роут**

Создать `src/jobhunt/web/routes/__init__.py` (пустой) и `src/jobhunt/web/routes/vacancies.py`:

```python
import uuid
from datetime import UTC, datetime
from pathlib import Path

from fastapi import APIRouter, Form, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from jobhunt.db.base import session_scope
from jobhunt.db.models import Application, Profile, Vacancy

TEMPLATES = Jinja2Templates(directory=str(Path(__file__).resolve().parents[1] / "templates"))

router = APIRouter()

STATUSES = ("new", "applied", "call", "interview", "offer", "rejected", "ignored")


def list_vacancies(
    session: Session,
    profile_id: uuid.UUID,
    status: str | None = None,
    source: str | None = None,
    include_inactive: bool = False,
) -> list[dict]:
    """Вакансии с приклеенным статусом отклика текущего профиля."""
    query = (
        select(Vacancy, Application.status)
        .outerjoin(
            Application,
            (Application.vacancy_id == Vacancy.id) & (Application.profile_id == profile_id),
        )
        .order_by(Vacancy.posted_at.desc().nulls_last(), Vacancy.first_seen_at.desc())
    )
    if not include_inactive:
        query = query.where(Vacancy.is_active.is_(True))
    if source:
        query = query.where(Vacancy.source == source)

    rows = []
    for vacancy, application_status in session.execute(query).all():
        effective_status = application_status or "new"
        if status and effective_status != status:
            continue
        rows.append(
            {
                "id": str(vacancy.id),
                "source": vacancy.source,
                "external_id": vacancy.external_id,
                "title": vacancy.title,
                "company": vacancy.company,
                "url": vacancy.url,
                "location": vacancy.location,
                "salary_min": vacancy.salary_min,
                "salary_max": vacancy.salary_max,
                "salary_currency": vacancy.salary_currency,
                "posted_at": vacancy.posted_at,
                "status": effective_status,
            }
        )
    return rows


@router.get("/vacancies", response_class=HTMLResponse)
def vacancies_page(
    request: Request,
    status: str | None = Query(default=None),
    source: str | None = Query(default=None),
) -> HTMLResponse:
    with session_scope() as session:
        profile = session.execute(select(Profile).order_by(Profile.created_at)).scalars().first()
        rows = list_vacancies(session, profile.id, status=status, source=source) if profile else []

    return TEMPLATES.TemplateResponse(
        request=request,
        name="vacancies.html",
        context={
            "rows": rows,
            "statuses": STATUSES,
            "current_status": status,
            "current_source": source,
            "has_profile": profile is not None,
        },
    )
```

- [ ] **Step 4: Создать шаблоны**

Создать `src/jobhunt/web/templates/base.html`:

```html
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Job Hunt AI{% endblock %}</title>
  <script src="https://unpkg.com/htmx.org@2.0.3"></script>
  <style>
    :root { color-scheme: light dark; }
    body { font-family: system-ui, sans-serif; margin: 0; padding: 1.5rem; line-height: 1.5; }
    h1 { font-size: 1.4rem; margin: 0 0 1rem; }
    table { border-collapse: collapse; width: 100%; }
    th, td { text-align: left; padding: .5rem .6rem; border-bottom: 1px solid #8883; vertical-align: top; }
    th { font-weight: 600; font-size: .85rem; text-transform: uppercase; letter-spacing: .03em; }
    .filters { display: flex; gap: .75rem; margin-bottom: 1rem; flex-wrap: wrap; }
    .muted { opacity: .65; font-size: .9rem; }
    .empty { padding: 2rem; text-align: center; }
    select { padding: .25rem; }
    .scroll { overflow-x: auto; }
  </style>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

Создать `src/jobhunt/web/templates/vacancies.html`:

```html
{% extends "base.html" %}
{% block title %}Вакансии — Job Hunt AI{% endblock %}
{% block content %}
<h1>Вакансии</h1>

{% if not has_profile %}
  <p class="empty">Профиль не создан. Выполните в терминале:<br>
  <code>uv run python -m jobhunt.cli init-profile --name "Имя" --role "IT Director"</code></p>
{% else %}
  <form class="filters" method="get" action="/vacancies">
    <label>Статус
      <select name="status" onchange="this.form.submit()">
        <option value="">все</option>
        {% for s in statuses %}
          <option value="{{ s }}" {% if s == current_status %}selected{% endif %}>{{ s }}</option>
        {% endfor %}
      </select>
    </label>
    <label>Источник
      <select name="source" onchange="this.form.submit()">
        <option value="">все</option>
        <option value="work.ua" {% if current_source == 'work.ua' %}selected{% endif %}>work.ua</option>
        <option value="dou.ua" {% if current_source == 'dou.ua' %}selected{% endif %}>dou.ua</option>
      </select>
    </label>
  </form>

  {% if rows %}
  <div class="scroll">
  <table>
    <thead>
      <tr>
        <th>Вакансия</th><th>Компания</th><th>Город</th>
        <th>Зарплата</th><th>Опубликована</th><th>Статус</th>
      </tr>
    </thead>
    <tbody>
      {% for row in rows %}
      <tr id="row-{{ row.id }}">
        <td>
          <a href="{{ row.url }}" target="_blank" rel="noopener">{{ row.title }}</a>
          <div class="muted">{{ row.source }}</div>
        </td>
        <td>{{ row.company or "—" }}</td>
        <td>{{ row.location or "—" }}</td>
        <td>
          {% if row.salary_min %}
            {{ row.salary_min }}{% if row.salary_max %}–{{ row.salary_max }}{% endif %}
            {{ row.salary_currency or "" }}
          {% else %}—{% endif %}
        </td>
        <td>{{ row.posted_at.strftime("%d.%m.%Y") if row.posted_at else "—" }}</td>
        <td>{% include "_status_cell.html" %}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
  </div>
  {% else %}
    <p class="empty">Вакансий пока нет. Запустите сбор:
    <code>uv run python -m jobhunt.cli parse</code></p>
  {% endif %}
{% endif %}
{% endblock %}
```

Создать `src/jobhunt/web/templates/_status_cell.html` (пока без интерактивности — она в Task 13):

```html
<span class="status">{{ row.status }}</span>
```

- [ ] **Step 5: Подключить роутер**

Заменить `src/jobhunt/web/app.py` на:

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from jobhunt.web.routes import vacancies

app = FastAPI(title="Job Hunt AI")
app.include_router(vacancies.router)


@app.get("/health")
def health() -> dict[str, str]:
    """Проверка живости — используется healthcheck-ом Docker."""
    return {"status": "ok"}


@app.get("/")
def index() -> RedirectResponse:
    return RedirectResponse(url="/vacancies")
```

- [ ] **Step 6: Запустить тесты и убедиться, что они проходят**

Run: `uv run pytest -v`
Expected: PASS, все тесты зелёные

- [ ] **Step 7: Проверить страницу глазами**

```bash
docker compose up -d --build
```

Открыть http://localhost:8000/vacancies — должна отображаться таблица собранных вакансий с работающими фильтрами.

- [ ] **Step 8: Commit**

```bash
git add src/jobhunt/web tests
git commit -m "feat: веб-таблица вакансий с фильтрами"
```

---

## Task 13: Смена статуса отклика

**Files:**
- Modify: `src/jobhunt/web/routes/vacancies.py`, `src/jobhunt/web/templates/_status_cell.html`
- Test: `tests/integration/test_status_change.py`

**Interfaces:**
- Consumes: модели `Application`, `Profile`, `Vacancy`
- Produces: `jobhunt.web.routes.vacancies.set_status(session, profile_id: uuid.UUID, vacancy_id: uuid.UUID, status: str) -> Application`; роут `POST /vacancies/{vacancy_id}/status`

- [ ] **Step 1: Написать падающие тесты**

Создать `tests/integration/test_status_change.py`:

```python
from datetime import UTC, datetime

import pytest

from jobhunt.db.models import Application, Profile, Vacancy
from jobhunt.web.routes.vacancies import set_status


def _seed(session) -> tuple[Profile, Vacancy]:
    profile = Profile(name="Кирилл", target_roles=["IT Director"])
    now = datetime.now(UTC)
    vacancy = Vacancy(
        source="work.ua",
        external_id="1",
        title="Head of IT",
        url="https://www.work.ua/jobs/1/",
        description_raw="Опис",
        description_hash="h1",
        first_seen_at=now,
        last_seen_at=now,
    )
    session.add_all([profile, vacancy])
    session.commit()
    return profile, vacancy


def test_creates_application_on_first_status_change(session):
    profile, vacancy = _seed(session)

    application = set_status(session, profile.id, vacancy.id, "applied")
    session.commit()

    assert application.status == "applied"
    assert application.applied_at is not None
    assert session.query(Application).count() == 1


def test_updates_existing_application(session):
    profile, vacancy = _seed(session)
    set_status(session, profile.id, vacancy.id, "applied")
    session.commit()

    application = set_status(session, profile.id, vacancy.id, "call")
    session.commit()

    assert application.status == "call"
    assert session.query(Application).count() == 1


def test_records_responded_at_on_positive_outcome(session):
    profile, vacancy = _seed(session)
    application = set_status(session, profile.id, vacancy.id, "call")
    session.commit()

    assert application.responded_at is not None


def test_rejects_unknown_status(session):
    profile, vacancy = _seed(session)
    with pytest.raises(ValueError):
        set_status(session, profile.id, vacancy.id, "нет-такого")
```

- [ ] **Step 2: Запустить тесты и убедиться, что они падают**

Run: `uv run pytest tests/integration/test_status_change.py -v`
Expected: FAIL с `ImportError: cannot import name 'set_status'`

- [ ] **Step 3: Реализовать смену статуса**

Дописать в конец `src/jobhunt/web/routes/vacancies.py`. Новых импортов не требуется — `datetime`,
`UTC` и `Form` уже добавлены в блок импортов в Task 12.

```python
# Статусы, означающие, что работодатель ответил
RESPONDED_STATUSES = ("call", "interview", "offer", "rejected")


def set_status(
    session: Session, profile_id: uuid.UUID, vacancy_id: uuid.UUID, status: str
) -> Application:
    """Записать статус отклика профиля на вакансию."""
    if status not in STATUSES:
        raise ValueError(f"недопустимый статус {status!r}; допустимы: {', '.join(STATUSES)}")

    application = session.execute(
        select(Application).where(
            Application.profile_id == profile_id,
            Application.vacancy_id == vacancy_id,
        )
    ).scalar_one_or_none()

    if application is None:
        application = Application(profile_id=profile_id, vacancy_id=vacancy_id)
        session.add(application)

    now = datetime.now(UTC)
    application.status = status
    if status == "applied" and application.applied_at is None:
        application.applied_at = now
    if status in RESPONDED_STATUSES and application.responded_at is None:
        application.responded_at = now

    session.flush()
    return application


@router.post("/vacancies/{vacancy_id}/status", response_class=HTMLResponse)
def change_status(
    request: Request, vacancy_id: uuid.UUID, status: str = Form(...)
) -> HTMLResponse:
    """Обработчик HTMX: возвращает обновлённую ячейку статуса, а не всю страницу."""
    with session_scope() as session:
        profile = session.execute(select(Profile).order_by(Profile.created_at)).scalars().first()
        if profile is None:
            return HTMLResponse("<span>профиль не создан</span>", status_code=400)
        set_status(session, profile.id, vacancy_id, status)

    return TEMPLATES.TemplateResponse(
        request=request,
        name="_status_cell.html",
        context={"row": {"id": str(vacancy_id), "status": status}, "statuses": STATUSES},
    )
```

- [ ] **Step 4: Сделать ячейку статуса интерактивной**

Заменить `src/jobhunt/web/templates/_status_cell.html` на:

```html
<select name="status"
        hx-post="/vacancies/{{ row.id }}/status"
        hx-target="closest td"
        hx-swap="innerHTML">
  {% for s in statuses %}
    <option value="{{ s }}" {% if s == row.status %}selected{% endif %}>{{ s }}</option>
  {% endfor %}
</select>
```

- [ ] **Step 5: Запустить все тесты**

Run: `uv run pytest -v`
Expected: PASS, все зелёные

- [ ] **Step 6: Проверить в браузере**

```bash
docker compose up -d --build
```

Открыть http://localhost:8000/vacancies, сменить статус в выпадающем списке любой строки, обновить страницу — статус должен сохраниться.

- [ ] **Step 7: Commit**

```bash
git add src/jobhunt/web tests
git commit -m "feat: смена статуса отклика из таблицы"
```

---

## Итог плана A

После Task 13 работает:

- `docker compose up` поднимает приложение и PostgreSQL с pgvector
- `jobhunt init-profile` создаёт профиль с целевыми ролями
- `jobhunt parse` обходит work.ua и dou.ua по каждой роли, соблюдая robots.txt и паузы
- Повторные прогоны не создают дублей, исчезнувшие вакансии деактивируются после трёх пропусков, правки описаний фиксируются
- Усечённая выдача видна в журнале `parse_runs` со статусом `truncated`
- http://localhost:8000/vacancies показывает таблицу с фильтрами и сменой статуса отклика

Следующий план — B: чтение резюме, банк тезисов, извлечение требований моделью, гибридный скор и экран gap-анализа.
