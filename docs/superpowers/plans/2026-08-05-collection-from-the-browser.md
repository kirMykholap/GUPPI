# Collection from the browser (slice 2b) — implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** collect vacancies from `/vacancies` with two buttons, with a live progress line, a guard against a second run, and an honest summary when it ends.

**Architecture:** a run is a row in a new `parse_batches` table; the route opens the batch synchronously and hands the work to a daemon thread that calls the existing `run_profile`. Everything the page shows — progress, the guard, the summary — is read from rows already committed per source+tag pair, so the truth is visible to the CLI process as well.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0 (imperative `select()`), Alembic, Jinja2, htmx 2, PostgreSQL 17, pytest.

**Spec:** `docs/superpowers/specs/2026-08-05-collection-from-the-browser-design.md`.

## Global Constraints

- **English for everything written into the repository** — code, identifiers, docstrings, comments, test names, commit messages, **and log messages** (`logger.*`; decided by the owner on 2026-08-05: logs are not product content). **Russian stays only in strings the owner sees**: template copy, `print()` in the CLI, `HTTPException(detail=…)` (the page renders it), and `ParseRun.error_text` (the CLI prints it). Existing Russian names and docstrings are not renamed or translated (`CLAUDE.md`).
- **The sample code in the tasks below sometimes carries Russian docstrings and comments — write them in English.** The one exception is a docstring moved verbatim from an existing file (`is_broad_tag`, Task 5): a move is not a rewrite, and mass-translation is forbidden.
- **No new dependencies**, neither Python nor npm.
- `uv run ruff check src tests` and `uv run ruff format src tests` must be clean before every commit. Line width 100.
- **A subagent runs only the tests covering its own task** — named in that task. The full suite is the controller's job, once, at the end.
- Web routes take a session only through `Depends(get_session)`, never `session_scope()`.
- Any change to code or templates needs `docker compose restart app` to be visible in the browser (uvicorn runs without `--reload`, Jinja `auto_reload` is off).
- The test database comes from `TEST_DATABASE_URL`. **Never run the suite against the production database.**

## Correction to the spec, decided while planning

The spec (§4.4) says the startup sweep is called **from the FastAPI lifespan**. It cannot be: `sweep_interrupted` needs a session, and inside the web process the only way to get one outside a request is `session_scope()`, which reads `settings.database_url` — the developer's database. Every test that does `with TestClient(app)` (four files do) would run the sweep against production data, which `CLAUDE.md` forbids outright.

The sweep therefore becomes **a CLI command, `jobhunt sweep-batches`, invoked by `docker-entrypoint.sh` right after `alembic upgrade head` and before uvicorn starts**. Same moment in time — the process that owned those batches has just died — and CLI tests already route to the test database by monkeypatching `cli.session_scope` (`tests/integration/test_cli.py`). Task 11 also updates the spec so the two documents do not disagree.

---

## File structure

| File | Responsibility |
|---|---|
| `src/jobhunt/db/models.py` | `ParseBatch` model, `ParseRun.batch_id` |
| `migrations/versions/0008_parse_batches.py` | table, partial unique index, FK column |
| `src/jobhunt/ingest/batches.py` | open / touch / finish / sweep, `CollectionAlreadyRunning` |
| `src/jobhunt/ingest/summary.py` | what counts as a problem: `is_broad_tag`, `summarize` |
| `src/jobhunt/ingest/runner.py` | stamps `batch_id`, touches progress, finalises the batch |
| `src/jobhunt/cli.py` | opens a batch for `parse`, new `sweep-batches` command |
| `src/jobhunt/web/data/collection.py` | read side: state, progress, planned count |
| `src/jobhunt/web/collection_runner.py` | the thread, its HTTP client, its error log |
| `src/jobhunt/web/routes/collection.py` | `GET /vacancies/collection`, `POST /vacancies/collect` |
| `src/jobhunt/web/templates/_collection.html` | the panel |
| `src/jobhunt/web/templates/vacancies.html` | includes the panel |
| `src/jobhunt/web/templates/_filters.html` | second trigger on the filters form |
| `tests/unit/test_batch_write_boundary.py` | only `ingest/batches.py` writes `parse_batches` |

Twelve tasks. Tasks 1–6 build the state model and the runner side (no page changes at all); 7–10 build the panel; 11–12 close the loop.

**One test from the spec's table already exists.** «Modes differ in the right to judge» is covered by `test_быстрый_режим_не_двигает_счётчик_пропусков` in `tests/integration/test_runner.py` — do not write a second one. It is named here so that nobody adds a duplicate and nobody assumes the rule is unguarded.

---

### Task 1: `parse_batches` table and model

**Files:**
- Modify: `src/jobhunt/db/models.py` (imports; new `ParseBatch`; `ParseRun.batch_id`)
- Create: `migrations/versions/0008_parse_batches.py`
- Modify: `tests/integration/test_migrations.py` (`EXPECTED_TABLES`)
- Test: `tests/integration/test_models.py`

**Interfaces:**
- Produces: `ParseBatch` with columns `id, profile_id, mode, status, started_by, planned_requests, started_at, finished_at, last_progress_at`; `ParseRun.batch_id: uuid.UUID | None`; index name `uq_parse_batches_one_running_per_profile`.

- [ ] **Step 1: Write the failing test**

Append to `tests/integration/test_models.py`:

```python
def test_one_running_batch_per_profile_is_a_database_rule(session):
    """Two presses in a row race each other. A check in code would lose that
    race; a partial unique index cannot."""
    profile = Profile(name="Кирилл", collection_cities=[])
    session.add(profile)
    session.flush()
    now = datetime.now(UTC)

    def batch(status: str) -> ParseBatch:
        return ParseBatch(
            profile_id=profile.id,
            mode="full",
            status=status,
            started_by="web",
            planned_requests=4,
            started_at=now,
            last_progress_at=now,
        )

    session.add(batch("running"))
    session.flush()

    session.add(batch("running"))
    with pytest.raises(IntegrityError):
        session.flush()
    session.rollback()


def test_finished_batches_do_not_collide(session):
    """The index is partial: history must not block the next run."""
    profile = Profile(name="Кирилл", collection_cities=[])
    session.add(profile)
    session.flush()
    now = datetime.now(UTC)
    for _ in range(3):
        session.add(
            ParseBatch(
                profile_id=profile.id,
                mode="quick",
                status="finished",
                started_by="cli",
                planned_requests=2,
                started_at=now,
                finished_at=now,
                last_progress_at=now,
            )
        )
    session.flush()

    assert session.execute(select(func.count()).select_from(ParseBatch)).scalar_one() == 3
```

Add to that file's imports what it is missing: `pytest`, `from sqlalchemy import func, select`, `from sqlalchemy.exc import IntegrityError`, and `ParseBatch` from `jobhunt.db.models`.

- [ ] **Step 2: Run it and watch it fail**

Run: `uv run pytest tests/integration/test_models.py -q -k batch`
Expected: FAIL — `ImportError: cannot import name 'ParseBatch'`.

- [ ] **Step 3: Add the model**

In `src/jobhunt/db/models.py`, add `text` to the `sqlalchemy` import list (`Index` and the rest are already there), then add the model above `class ParseRun`:

```python
class ParseBatch(Base):
    """One collection run of one profile — what ParseRun cannot express.

    ParseRun is a row per source+tag pair, so the four requests behind one
    press are not related to each other by anything: no denominator for a
    progress line, no "running now" flag, and nowhere to put the guard against
    a second press.

    The status is a lifecycle — started, ended, killed — not a verdict on the
    collection. A run whose every request failed still ends as "finished";
    what went wrong is in the ParseRun rows, which already carry failed /
    truncated / ids_incomplete per request and name the source and the tag. A
    second place holding a verdict would eventually disagree with the first.

    started_by tells which process owns the run. The sweep at container start
    may only interrupt batches it could have owned ("web"); a "cli" batch runs
    in another process, and restarting the container is none of its business.
    """

    __tablename__ = "parse_batches"
    __table_args__ = (
        # A partial unique index rather than a check in code: "read, then
        # insert" loses to two presses in a row, and this cannot.
        Index(
            "uq_parse_batches_one_running_per_profile",
            "profile_id",
            unique=True,
            postgresql_where=text("status = 'running'"),
        ),
    )

    id: Mapped[uuid.UUID] = _uuid_pk()
    profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("profiles.id", ondelete="CASCADE"))
    mode: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20), default="running", server_default="running")
    started_by: Mapped[str] = mapped_column(String(10))
    # Fixed when the batch opens: tags can be toggled mid-run, and a
    # denominator that moves under the numerator is worse than none. It also
    # matches the runner, which reads the tag set once and does not re-read it.
    planned_requests: Mapped[int] = mapped_column(Integer)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    # Touched after every finished pair. A batch that stops moving is how a
    # killed process is noticed at all — see jobhunt.ingest.batches.STALE_AFTER.
    last_progress_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
```

In `class ParseRun`, after `ids_incomplete`:

```python
    # Nullable, and it stays nullable: the rows already in the production
    # journal were written before batches existed, and inventing a batch for
    # them would be inventing a fact.
    batch_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("parse_batches.id", ondelete="CASCADE"), nullable=True, index=True
    )
```

- [ ] **Step 4: Run the test again**

Run: `uv run pytest tests/integration/test_models.py -q -k batch`
Expected: PASS (2 passed). The `session` fixture builds the schema with `create_all`, so the migration is not needed yet.

- [ ] **Step 5: Write the migration**

Create `migrations/versions/0008_parse_batches.py`:

```python
"""parse batches

Revision ID: 0008
Revises: 0007
Create Date: 2026-08-05 00:00:00.000000

"""

import logging
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

logger = logging.getLogger(__name__)

revision: str = "0008"
down_revision: str | Sequence[str] | None = "0007"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "parse_batches",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "profile_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("profiles.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("mode", sa.String(length=20), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="running"),
        sa.Column("started_by", sa.String(length=10), nullable=False),
        sa.Column("planned_requests", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_progress_at", sa.DateTime(timezone=True), nullable=False),
    )
    # The guard itself. Partial: only one RUNNING batch per profile, while the
    # history of finished ones stays unlimited.
    op.create_index(
        "uq_parse_batches_one_running_per_profile",
        "parse_batches",
        ["profile_id"],
        unique=True,
        postgresql_where=sa.text("status = 'running'"),
    )
    op.add_column(
        "parse_runs", sa.Column("batch_id", postgresql.UUID(as_uuid=True), nullable=True)
    )
    op.create_foreign_key(
        "fk_parse_runs_batch_id_parse_batches",
        "parse_runs",
        "parse_batches",
        ["batch_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_index("ix_parse_runs_batch_id", "parse_runs", ["batch_id"])


def downgrade() -> None:
    bind = op.get_bind()

    # Revision 0007 knows neither the table nor the column. Say what is lost
    # instead of losing it quietly — there is nothing to restore it from.
    batches = bind.execute(sa.text("SELECT count(*) FROM parse_batches")).scalar_one()
    if batches:
        logger.warning(
            "downgrade 0008: %d parse_batches rows are dropped — revision 0007 has no "
            "such table and nothing else holds the same data",
            batches,
        )

    op.drop_index("ix_parse_runs_batch_id", table_name="parse_runs")
    op.drop_constraint("fk_parse_runs_batch_id_parse_batches", "parse_runs", type_="foreignkey")
    op.drop_column("parse_runs", "batch_id")
    op.drop_index("uq_parse_batches_one_running_per_profile", table_name="parse_batches")
    op.drop_table("parse_batches")
```

- [ ] **Step 6: Teach the migration test about the new table**

In `tests/integration/test_migrations.py`, add `"parse_batches"` to `EXPECTED_TABLES`.

- [ ] **Step 7: Run the migration tests**

Run: `uv run pytest tests/integration/test_migrations.py -q`
Expected: PASS. This is the run that matters: `alembic check` compares the migration against the models with `compare_server_default`, and the upgrade→downgrade→upgrade round trip covers revision 0008 too. If `alembic check` reports a diff on the partial index, the `postgresql_where` in the model and in the migration are not spelled identically — fix the migration, not the model.

- [ ] **Step 8: Commit**

```bash
git add src/jobhunt/db/models.py migrations/versions/0008_parse_batches.py tests/integration/test_migrations.py tests/integration/test_models.py
git commit -m "feat(db): parse_batches, one running batch per profile enforced by index"
```

---

### Task 2: `ingest/batches.py` — open, touch, finish, sweep

**Files:**
- Create: `src/jobhunt/ingest/batches.py`
- Test: `tests/integration/test_batches.py` (create)

**Interfaces:**
- Consumes: `ParseBatch`, `ParseRun` from Task 1.
- Produces:
  - `class CollectionAlreadyRunning(RuntimeError)`
  - `STALE_AFTER: timedelta` (15 minutes)
  - `open_batch(session, profile_id, *, mode, started_by, planned_requests, now=None) -> ParseBatch` — commits
  - `touch(session, batch_id, *, now=None) -> None`
  - `finish_batch(session, batch_id, *, status="finished", now=None) -> None`
  - `sweep_interrupted(session, *, now=None) -> int`

- [ ] **Step 1: Write the failing tests**

Create `tests/integration/test_batches.py`:

```python
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy import select

from jobhunt.db.models import ParseBatch, ParseRun, Profile
from jobhunt.ingest.batches import (
    STALE_AFTER,
    CollectionAlreadyRunning,
    finish_batch,
    open_batch,
    sweep_interrupted,
    touch,
)

NOW = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)


def _profile(session, name="Кирилл") -> Profile:
    profile = Profile(name=name, collection_cities=[])
    session.add(profile)
    session.commit()
    return profile


def test_open_batch_starts_a_running_row(session):
    profile = _profile(session)

    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW
    )

    assert batch.status == "running"
    assert batch.planned_requests == 4
    assert batch.last_progress_at == NOW


def test_second_open_is_refused(session):
    """The refusal must arrive while the caller can still report it."""
    profile = _profile(session)
    open_batch(session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW)

    with pytest.raises(CollectionAlreadyRunning):
        open_batch(
            session, profile.id, mode="quick", started_by="web", planned_requests=4, now=NOW
        )


def test_another_profile_is_not_blocked(session):
    first = _profile(session, "Кирилл")
    second = _profile(session, "Второй")
    open_batch(session, first.id, mode="full", started_by="web", planned_requests=4, now=NOW)

    other = open_batch(
        session, second.id, mode="full", started_by="web", planned_requests=2, now=NOW
    )

    assert other.status == "running"


def test_a_stale_batch_is_superseded_by_the_next_run(session):
    """A process killed hard leaves a running row behind. Without this the
    buttons would stay dark forever."""
    profile = _profile(session)
    stale = open_batch(
        session, profile.id, mode="full", started_by="cli", planned_requests=4, now=NOW
    )
    later = NOW + STALE_AFTER + timedelta(seconds=1)

    fresh = open_batch(
        session, profile.id, mode="quick", started_by="web", planned_requests=4, now=later
    )

    session.refresh(stale)
    assert stale.status == "interrupted"
    assert stale.finished_at == later
    assert fresh.status == "running"


def test_a_batch_that_still_moves_is_not_stale(session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW
    )
    touch(session, batch.id, now=NOW + STALE_AFTER)

    with pytest.raises(CollectionAlreadyRunning):
        open_batch(
            session,
            profile.id,
            mode="full",
            started_by="web",
            planned_requests=4,
            now=NOW + STALE_AFTER + timedelta(seconds=1),
        )


def test_finish_batch_closes_it(session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW
    )

    finish_batch(session, batch.id, now=NOW + timedelta(minutes=3))

    session.refresh(batch)
    assert batch.status == "finished"
    assert batch.finished_at == NOW + timedelta(minutes=3)


def test_sweep_interrupts_web_batches_and_their_running_requests(session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW
    )
    session.add(
        ParseRun(
            source="work.ua",
            profile_id=profile.id,
            batch_id=batch.id,
            query_params={"query": "Head of IT"},
            started_at=NOW,
            status="running",
        )
    )
    session.commit()

    swept = sweep_interrupted(session, now=NOW + timedelta(minutes=1))

    session.refresh(batch)
    assert swept == 1
    assert batch.status == "interrupted"
    run_status = session.execute(select(ParseRun.status)).scalar_one()
    # Otherwise the panel would keep naming a request that ended when the
    # process did.
    assert run_status == "interrupted"


def test_sweep_leaves_cli_batches_alone(session):
    """A CLI run lives in another process; restarting the container is none of
    its business."""
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="cli", planned_requests=4, now=NOW
    )

    swept = sweep_interrupted(session, now=NOW + timedelta(minutes=1))

    session.refresh(batch)
    assert swept == 0
    assert batch.status == "running"
```

- [ ] **Step 2: Run them and watch them fail**

Run: `uv run pytest tests/integration/test_batches.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.ingest.batches'`.

- [ ] **Step 3: Write the module**

Create `src/jobhunt/ingest/batches.py`:

```python
"""The lifecycle of one collection run, shared by both entry points.

The web route and `jobhunt parse` both go through here. If the web opened
batches on its own, a run started from the terminal would be invisible to the
guard and to the status line on the page — and the whole reason the state
lives in the database rather than in process memory would be lost.
"""

import logging
import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from jobhunt.db.models import ParseBatch, ParseRun

logger = logging.getLogger(__name__)

# A batch that has not moved for this long is considered dead. The ceiling for
# one source+tag pair is 25 pages against a 2 s pacing plus request time —
# under two minutes; fifteen is a wide margin that still fails fast enough to
# be usable from a page.
STALE_AFTER = timedelta(minutes=15)


class CollectionAlreadyRunning(RuntimeError):
    """This profile already has a running batch."""


def open_batch(
    session: Session,
    profile_id: uuid.UUID,
    *,
    mode: str,
    started_by: str,
    planned_requests: int,
    now: datetime | None = None,
) -> ParseBatch:
    """Open a batch, or refuse because one is already running.

    Commits, and that is part of the contract: the thread that will do the
    work runs in another session, and the CLI in another process entirely.
    An uncommitted row is invisible to both, so the worker would start against
    a batch nobody else can see.

    A stale batch is superseded in the SAME transaction that opens the new
    one — the unique index would otherwise refuse the new row and the profile
    would be locked out by a process that no longer exists.
    """
    moment = now or datetime.now(UTC)
    _supersede_stale(session, profile_id, moment)

    batch = ParseBatch(
        profile_id=profile_id,
        mode=mode,
        status="running",
        started_by=started_by,
        planned_requests=planned_requests,
        started_at=moment,
        last_progress_at=moment,
    )
    session.add(batch)
    try:
        session.flush()
    except IntegrityError as exc:
        # The refusal comes from uq_parse_batches_one_running_per_profile.
        # Rolling back is not optional: a session that hit an IntegrityError
        # cannot execute anything else until it does.
        session.rollback()
        raise CollectionAlreadyRunning(
            f"для профиля {profile_id} уже идёт сбор"
        ) from exc
    session.commit()
    return batch


def _supersede_stale(session: Session, profile_id: uuid.UUID, now: datetime) -> None:
    """Close batches of this profile that stopped moving long ago."""
    stale = session.execute(
        select(ParseBatch).where(
            ParseBatch.profile_id == profile_id,
            ParseBatch.status == "running",
            ParseBatch.last_progress_at < now - STALE_AFTER,
        )
    ).scalars()
    for batch in stale:
        logger.warning(
            "пачка %s (%s) не подавала признаков жизни с %s — считается прерванной",
            batch.id,
            batch.started_by,
            batch.last_progress_at,
        )
        batch.status = "interrupted"
        batch.finished_at = now
    session.flush()


def touch(session: Session, batch_id: uuid.UUID, *, now: datetime | None = None) -> None:
    """Mark that the run is still alive. Called after every finished pair,
    where a commit already happens anyway."""
    session.execute(
        update(ParseBatch)
        .where(ParseBatch.id == batch_id)
        .values(last_progress_at=now or datetime.now(UTC))
    )


def finish_batch(
    session: Session,
    batch_id: uuid.UUID,
    *,
    status: str = "finished",
    now: datetime | None = None,
) -> None:
    """Close the batch. Only the runner calls this — see run_profile."""
    session.execute(
        update(ParseBatch)
        .where(ParseBatch.id == batch_id)
        .values(status=status, finished_at=now or datetime.now(UTC))
    )
    session.flush()


def sweep_interrupted(session: Session, *, now: datetime | None = None) -> int:
    """Close batches whose process has just died. Returns how many.

    Only batches started by the web are touched: they lived in the process
    that is starting again right now, so they are certainly dead. A batch
    started from the CLI lives in another process and may still be running —
    interrupting it would be a lie. What protects against a CLI batch left
    behind by a killed terminal is STALE_AFTER, not this sweep.
    """
    moment = now or datetime.now(UTC)
    batches = list(
        session.execute(
            select(ParseBatch).where(
                ParseBatch.status == "running", ParseBatch.started_by == "web"
            )
        ).scalars()
    )
    for batch in batches:
        batch.status = "interrupted"
        batch.finished_at = moment
        # The journal rows of that batch are dangling too: run_source commits
        # the row as "running" before the request starts, so the panel would
        # keep naming a request that ended when the process did.
        session.execute(
            update(ParseRun)
            .where(ParseRun.batch_id == batch.id, ParseRun.status == "running")
            .values(
                status="interrupted",
                finished_at=moment,
                error_text="прогон прерван перезапуском приложения",
            )
        )
    session.flush()
    if batches:
        logger.warning("прерванных прогонов помечено: %d", len(batches))
    return len(batches)
```

- [ ] **Step 4: Run the tests**

Run: `uv run pytest tests/integration/test_batches.py -q`
Expected: PASS (8 passed).

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/ingest/batches.py tests/integration/test_batches.py
git commit -m "feat(ingest): batch lifecycle with a stale rule and an owner-aware sweep"
```

---

### Task 3: the `running` journal row becomes observable

**Files:**
- Modify: `src/jobhunt/ingest/runner.py` (`run_source`, right after the row is added)
- Test: `tests/integration/test_runner.py`

**Interfaces:**
- Produces: nothing new in signatures. Changes transaction boundaries: `run_source` commits the journal row before the request starts.

This is deliberately its own task. It touches the most dangerous code in the project, and it must not arrive bundled with a page element.

- [ ] **Step 1: Write the failing test**

Append to `tests/integration/test_runner.py` (it already has `session_factory`-based tests and parser stubs — follow the file's existing helpers for building a profile):

```python
def test_running_row_is_visible_to_another_session(session, session_factory):
    """"Running right now" is a fact about another process. Until the row is
    committed, no other session can see it — and the whole progress line is
    built on other sessions seeing it."""
    profile = Profile(name="Кирилл", collection_cities=[])
    session.add(profile)
    session.commit()
    seen: dict[str, str | None] = {}

    class Probe:
        def fetch_listings(self, query, filters):
            with session_factory() as other:
                seen["status"] = other.execute(select(ParseRun.status)).scalar_one_or_none()
            return ParseResult(vacancies=[], truncated=False, ids_complete=True)

    with session_factory() as worker:
        run_source(
            worker,
            "work.ua",
            "Head of IT",
            client=None,
            filters=SearchFilters(),
            profile_id=profile.id,
            tag_id=uuid.uuid4(),
            parser=Probe(),
            today=date(2026, 8, 5),
        )

    assert seen["status"] == "running"
```

Add whatever of `select`, `uuid`, `date`, `ParseResult`, `SearchFilters`, `ParseRun`, `Profile`, `run_source` the file does not already import.

The `tag_id` is a random UUID with no row behind it: this test never reaches `upsert_vacancies` (the parser returns nothing), so nothing dereferences it.

- [ ] **Step 2: Run it and watch it fail**

Run: `uv run pytest tests/integration/test_runner.py -q -k visible_to_another_session`
Expected: FAIL — `assert None == 'running'`. The row exists in the worker's transaction and nowhere else.

- [ ] **Step 3: Commit the row as soon as it exists**

In `src/jobhunt/ingest/runner.py`, inside `run_source`, replace

```python
    session.add(run)
    session.flush()
```

with

```python
    session.add(run)
    # Committed before the request starts, not with its result. A flushed row
    # lives only inside this transaction, so "running right now" was invisible
    # to every other session — the CLI could not show it and the page cannot
    # be built on it. The cost is stated plainly: an interrupted run now
    # leaves a dangling "running" row behind, which is what
    # jobhunt.ingest.batches.sweep_interrupted and STALE_AFTER exist for.
    session.commit()
```

- [ ] **Step 4: Run the runner tests**

Run: `uv run pytest tests/integration/test_runner.py tests/integration/test_activity.py -q`
Expected: PASS, all of them. `test_activity.py` is included because the deactivation cycle is what an extra commit could disturb; if anything there fails, the cause is the new transaction boundary and not the test.

- [ ] **Step 5: Correct the documented limitation**

In `docs/HANDOFF.md`, section 6, the row «Статус `running` в журнале не наблюдаем» is now wrong in both halves. Replace its two cells with:

| Что | Последствие | Насколько срочно |
|---|---|---|
| Прерванный прогон оставляет запись `running` | Запись коммитится до запроса, поэтому «идёт прямо сейчас» видно снаружи — но убитый процесс оставляет её висеть. Закрывается подметанием при старте контейнера (`jobhunt sweep-batches`) и правилом 15 минут (`ingest/batches.STALE_AFTER`) | Штатно обработано, знать про это нужно при отладке |

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/ingest/runner.py tests/integration/test_runner.py docs/HANDOFF.md
git commit -m "feat(ingest): the running journal row is committed before the request"
```

---

### Task 4: the runner fills the batch in

**Files:**
- Modify: `src/jobhunt/ingest/runner.py` (`run_source` and `run_profile` signatures, the pair loop, the `finally`)
- Test: `tests/integration/test_runner.py`

**Interfaces:**
- Consumes: `touch`, `finish_batch` from Task 2.
- Produces: `run_source(..., batch_id: uuid.UUID | None = None)` and `run_profile(..., batch_id: uuid.UUID | None = None)`; every `ParseRun` created inside a batch carries `batch_id`; the batch is finalised by `run_profile` and by nobody else.

- [ ] **Step 1: Write the failing tests**

Append to `tests/integration/test_runner.py`:

```python
def test_runs_of_a_batch_carry_its_id(session, session_factory):
    profile = _make_profile(session, ["Head of IT"])
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW_BATCH
    )
    calls: list = []

    run_profile(
        session_factory,
        profile.id,
        client=None,
        mode="full",
        sources=("work.ua",),
        parser_factory=lambda source, client: RecordingParser(source, {"Head of IT": ["1"]}, calls),
        today=TODAY,
        batch_id=batch.id,
    )

    session.expire_all()
    batch_ids = session.execute(select(ParseRun.batch_id)).scalars().all()
    assert batch_ids == [batch.id]


def test_the_batch_is_finalised_by_the_runner(session, session_factory):
    profile = _make_profile(session, ["Head of IT"])
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW_BATCH
    )
    calls: list = []

    run_profile(
        session_factory,
        profile.id,
        client=None,
        mode="full",
        sources=("work.ua",),
        parser_factory=lambda source, client: RecordingParser(source, {"Head of IT": ["1"]}, calls),
        today=TODAY,
        batch_id=batch.id,
    )

    session.expire_all()
    session.refresh(batch)
    assert batch.status == "finished"
    assert batch.finished_at is not None
    # NOW_BATCH лежит в прошлом, а touch ставит настоящее время — прогресс
    # обязан был сдвинуться хотя бы раз.
    assert batch.last_progress_at > batch.started_at


def test_the_batch_is_finalised_even_when_the_run_explodes(session, session_factory):
    """Without this the row stays "running" forever and the buttons stay dark
    until the fifteen-minute rule expires."""
    profile = _make_profile(session, ["Head of IT"])
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW_BATCH
    )

    def exploding_factory(source, client):
        raise RuntimeError("парсер не собрался")

    with pytest.raises(RuntimeError):
        run_profile(
            session_factory,
            profile.id,
            client=None,
            mode="full",
            sources=("work.ua",),
            parser_factory=exploding_factory,
            today=TODAY,
            batch_id=batch.id,
        )

    session.expire_all()
    session.refresh(batch)
    assert batch.status == "finished"
```

Add to that file: `from jobhunt.ingest.batches import open_batch` and
`NOW_BATCH = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)`. `_make_profile`,
`RecordingParser` and `TODAY` already exist in it — use them, do not add
second copies. `session.expire_all()` is not optional: `run_profile` commits in
its own sessions, and without expiring, this session answers from its identity
map (a lesson already recorded in the state handoff).

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/integration/test_runner.py -q -k batch`
Expected: FAIL — `TypeError: run_profile() got an unexpected keyword argument 'batch_id'`.

- [ ] **Step 3: Thread the batch through**

In `src/jobhunt/ingest/runner.py`:

Import at the top: `from jobhunt.ingest.batches import finish_batch, touch`.

`run_source` gains a keyword argument and passes it to the model:

```python
def run_source(
    session: Session,
    source: str,
    query: str,
    client,
    filters: SearchFilters,
    profile_id: uuid.UUID,
    tag_id: uuid.UUID,
    parser: BaseParser | None = None,
    today: date | None = None,
    batch_id: uuid.UUID | None = None,
) -> SourceRunResult:
```

```python
    run = ParseRun(
        source=source,
        profile_id=profile_id,
        batch_id=batch_id,
        query_params={"query": query},
        started_at=datetime.now(UTC),
        status="running",
        mode=filters.mode,
    )
```

`run_profile` gains the same argument, passes it to every `run_source` call, touches after each pair's commit, and finalises in its `finally`:

```python
def run_profile(
    session_factory: Callable[[], Session] | sessionmaker[Session],
    profile_id: uuid.UUID,
    client,
    mode: Literal["full", "quick"] = "full",
    sources: tuple[str, ...] = ALL_SOURCES,
    parser_factory: Callable[[str, object], BaseParser] = get_parser,
    today: date | None = None,
    batch_id: uuid.UUID | None = None,
) -> list[ParseRun]:
```

In the first pass, the `run_source(...)` call gains `batch_id=batch_id`, and the existing `session.commit()` at the end of the pair becomes:

```python
                # Коммит после каждой пары источник+тег: обрыв на следующей
                # паре не должен откатывать то, что уже собрано и уже
                # записано в журнал прогонов этой же пары.
                if batch_id is not None:
                    touch(session, batch_id)
                session.commit()
```

And the `finally` becomes:

```python
    finally:
        if batch_id is not None:
            # run_profile owns the batch id, so run_profile closes the batch —
            # here and nowhere else. Two owners would disagree about the end
            # time and the status. The rollback first is not decoration: if
            # the run died mid-transaction, the session cannot execute
            # anything until it happens.
            try:
                session.rollback()
                finish_batch(session, batch_id)
                session.commit()
            except Exception:
                logger.exception("не удалось закрыть пачку %s", batch_id)
        session.close()
```

- [ ] **Step 4: Run the tests**

Run: `uv run pytest tests/integration/test_runner.py -q`
Expected: PASS, including the three new ones.

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/ingest/runner.py tests/integration/test_runner.py
git commit -m "feat(ingest): run_profile stamps, touches and closes its batch"
```

---

### Task 5: one definition of "a problem with a run"

**Files:**
- Create: `src/jobhunt/ingest/summary.py`
- Modify: `src/jobhunt/cli.py` (drop the private `_is_broad_tag` and `BROAD_TAG_RATIO_THRESHOLD`, import them instead)
- Test: `tests/unit/test_run_summary.py` (create)

**Interfaces:**
- Produces:
  - `BROAD_TAG_RATIO_THRESHOLD: float`
  - `is_broad_tag(run: ParseRun) -> bool`
  - `RunSummary` frozen dataclass: `requests, found, new, updated, failed, truncated, ids_incomplete, broad_tags: int`, property `has_problems: bool`
  - `summarize(runs: Sequence[ParseRun]) -> RunSummary`

- [ ] **Step 1: Write the failing tests**

Create `tests/unit/test_run_summary.py`:

```python
from datetime import UTC, datetime

from jobhunt.db.models import ParseRun
from jobhunt.ingest.summary import is_broad_tag, summarize

NOW = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)


def _run(**kwargs) -> ParseRun:
    base = {
        "source": "work.ua",
        "query_params": {"query": "Head of IT"},
        "started_at": NOW,
        "finished_at": NOW,
        "status": "success",
        "found_count": 10,
        "new_count": 1,
        "updated_count": 9,
    }
    base.update(kwargs)
    return ParseRun(**base)


def test_summary_counts_every_kind_of_problem():
    summary = summarize(
        [
            _run(),
            _run(status="failed", found_count=0, new_count=0, updated_count=0),
            _run(status="truncated"),
            _run(ids_incomplete=True),
            _run(mode="full", found_count=10, total_available=1000),
        ]
    )

    assert summary.requests == 5
    assert summary.failed == 1
    assert summary.truncated == 1
    assert summary.ids_incomplete == 1
    assert summary.broad_tags == 1
    assert summary.has_problems is True


def test_a_clean_summary_has_no_problems():
    summary = summarize([_run(), _run()])

    assert summary == summarize([_run(), _run()])
    assert summary.found == 20
    assert summary.new == 2
    assert summary.updated == 18
    assert summary.has_problems is False


def test_quick_runs_are_never_broad():
    """Its ceiling is small by construction: the ratio would measure the crawl
    limit, not the width of the tag, and the warning would fire on every quick
    run and stop being read."""
    assert is_broad_tag(_run(mode="quick", found_count=10, total_available=1000)) is False


def test_failed_runs_are_never_broad():
    assert is_broad_tag(_run(status="failed", found_count=0, total_available=1000)) is False
```

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/unit/test_run_summary.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.ingest.summary'`.

- [ ] **Step 3: Write the module**

Create `src/jobhunt/ingest/summary.py`:

```python
"""What counts as a problem with a run — one definition, two readers.

The CLI printed this judgement and the collection panel is about to print it
again. Two copies of "the tag is too broad" would drift, and the day they do,
the page and the terminal disagree about the same journal rows.
"""

from collections.abc import Sequence
from dataclasses import dataclass

from jobhunt.db.models import ParseRun

BROAD_TAG_RATIO_THRESHOLD = 0.1


def is_broad_tag(run: ParseRun) -> bool:
    """Собранное — лишь малая доля заявленного источником объёма.

    failed-запросы не в счёт: found_count там 0 не потому, что тег широкий, а
    потому, что запрос вообще не отработал — это отдельный, уже видимый
    сигнал.

    Быстрый режим не в счёт тоже: его потолок мал по построению (work.ua — не
    больше quick_max_pages=5 страниц по 14 карточек, dou.ua — 20 + 3×40), и
    доля собранного меряет в нём потолок обхода, а не ширину тега. Живой
    ориентир: нормально работающий тег с total_available 1416 даёт 140 из
    1416 — ниже порога, то есть предупреждение срабатывало бы на каждом
    быстром прогоне и перестало бы читаться.
    """
    if run.status == "failed" or run.mode == "quick" or not run.total_available:
        return False
    return run.found_count < run.total_available * BROAD_TAG_RATIO_THRESHOLD


@dataclass(frozen=True)
class RunSummary:
    """Итог набора журнальных записей: сколько собрано и что пошло не так."""

    requests: int
    found: int
    new: int
    updated: int
    failed: int
    truncated: int
    ids_incomplete: int
    broad_tags: int

    @property
    def has_problems(self) -> bool:
        return bool(self.failed or self.truncated or self.ids_incomplete or self.broad_tags)


def summarize(runs: Sequence[ParseRun]) -> RunSummary:
    return RunSummary(
        requests=len(runs),
        found=sum(run.found_count for run in runs),
        new=sum(run.new_count for run in runs),
        updated=sum(run.updated_count for run in runs),
        failed=sum(1 for run in runs if run.status == "failed"),
        truncated=sum(1 for run in runs if run.status == "truncated"),
        ids_incomplete=sum(1 for run in runs if run.ids_incomplete),
        broad_tags=sum(1 for run in runs if is_broad_tag(run)),
    )
```

- [ ] **Step 4: Point the CLI at it**

In `src/jobhunt/cli.py`: delete `BROAD_TAG_RATIO_THRESHOLD` and the whole `_is_broad_tag` function, add `from jobhunt.ingest.summary import is_broad_tag` to the imports, and replace both uses of `_is_broad_tag(run)` with `is_broad_tag(run)`.

- [ ] **Step 5: Run both test files**

Run: `uv run pytest tests/unit/test_run_summary.py tests/integration/test_cli.py -q`
Expected: PASS. The CLI tests are the proof that the move changed no behaviour — one of them asserts the broad-tag warning verbatim.

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/ingest/summary.py src/jobhunt/cli.py tests/unit/test_run_summary.py
git commit -m "refactor(ingest): one definition of a problematic run, shared by CLI and web"
```

---

### Task 6: the CLI opens a batch, and can sweep

**Files:**
- Modify: `src/jobhunt/cli.py` (`cmd_parse`, new `cmd_sweep_batches`, `build_parser`, `main` dispatch)
- Modify: `docker-entrypoint.sh`
- Test: `tests/integration/test_cli.py`

**Interfaces:**
- Consumes: `open_batch`, `sweep_interrupted`, `CollectionAlreadyRunning` (Task 2); `run_profile(..., batch_id=...)` (Task 4).
- Produces: `jobhunt sweep-batches`; `cmd_parse` refuses to start while a batch is running.

- [ ] **Step 1: Write the failing tests**

Append to `tests/integration/test_cli.py`:

```python
def test_cmd_parse_opens_a_batch(monkeypatch, session, capsys):
    profile = _profile_with_tags(session, ["Head of IT"])
    seen: dict[str, object] = {}

    def fake_run_profile(factory, profile_id, client, mode, batch_id=None, **kwargs):
        seen["batch_id"] = batch_id
        return []

    monkeypatch.setattr(cli, "run_profile", fake_run_profile)

    assert cli.cmd_parse("Кирилл", "full") == 0

    batch = session.execute(select(ParseBatch)).scalar_one()
    assert batch.started_by == "cli"
    assert batch.mode == "full"
    assert batch.planned_requests == len(ALL_SOURCES)
    assert seen["batch_id"] == batch.id


def test_cmd_parse_refuses_while_another_run_is_going(monkeypatch, session, capsys):
    profile = _profile_with_tags(session, ["Head of IT"])
    open_batch(
        session,
        profile.id,
        mode="full",
        started_by="web",
        planned_requests=2,
        now=datetime.now(UTC),
    )

    def fake_run_profile(*args, **kwargs):
        raise AssertionError("сбор не должен был начаться")

    monkeypatch.setattr(cli, "run_profile", fake_run_profile)

    assert cli.cmd_parse("Кирилл", "full") == 1
    assert "уже идёт" in capsys.readouterr().out


def test_sweep_batches_reports_what_it_closed(session, capsys):
    profile = _profile_with_tags(session, ["Head of IT"])
    open_batch(
        session,
        profile.id,
        mode="full",
        started_by="web",
        planned_requests=2,
        now=datetime.now(UTC),
    )

    assert cli.cmd_sweep_batches() == 0

    assert "прерванных прогонов" in capsys.readouterr().out
```

Add `ParseBatch`, `ALL_SOURCES` (`from jobhunt.parsers.registry import ALL_SOURCES`) and `open_batch` to the file's imports.

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/integration/test_cli.py -q -k "batch or sweep"`
Expected: FAIL — `AttributeError: module 'jobhunt.cli' has no attribute 'cmd_sweep_batches'`, and the parse tests fail because no batch row appears.

- [ ] **Step 3: Open the batch in `cmd_parse`**

In `src/jobhunt/cli.py`, import `from jobhunt.ingest.batches import CollectionAlreadyRunning, open_batch, sweep_interrupted` and `from jobhunt.parsers.registry import ALL_SOURCES` (if it is not imported already).

Inside `cmd_parse`, within the existing `with session_scope() as session:` block, after the enabled-tag check, replace the plain `profile_id = profile.id` with:

```python
        profile_id = profile.id
        enabled_tags = session.execute(
            select(ProfileTag.id).where(
                ProfileTag.profile_id == profile.id, ProfileTag.is_enabled.is_(True)
            )
        ).all()
        try:
            batch = open_batch(
                session,
                profile_id,
                mode=mode,
                started_by="cli",
                # Одна запись журнала на пару «тег × источник» — столько же
                # запросов и уйдёт (см. run_profile).
                planned_requests=len(enabled_tags) * len(ALL_SOURCES),
            )
        except CollectionAlreadyRunning:
            print("для этого профиля уже идёт сбор — дождитесь его окончания")
            return 1
        batch_id = batch.id
```

and pass it to the runner:

```python
        runs = run_profile(
            get_session_factory(), profile_id, client=client, mode=mode, batch_id=batch_id
        )
```

- [ ] **Step 4: Add the sweep command**

In `src/jobhunt/cli.py`:

```python
def cmd_sweep_batches() -> int:
    """Закрыть прогоны, чей процесс уже мёртв.

    Вызывается точкой входа контейнера перед стартом сервера: пачки, которые
    вёл веб-процесс, умерли вместе с ним, и без этого они держали бы кнопки
    сбора выключенными до истечения правила пятнадцати минут.
    """
    with session_scope() as session:
        closed = sweep_interrupted(session)
    print(f"прерванных прогонов помечено: {closed}")
    return 0
```

In `build_parser`, next to the other subcommands:

```python
    subparsers.add_parser(
        "sweep-batches", help="закрыть прогоны, чей процесс уже мёртв (вызывается при старте)"
    )
```

In `main`, add the dispatch branch next to the others: `if args.command == "sweep-batches": return cmd_sweep_batches()`. Follow the exact dispatch style already in that function.

- [ ] **Step 5: Call it from the entrypoint**

In `docker-entrypoint.sh`, between the migrations and uvicorn:

```sh
echo "[docker-entrypoint] закрываю прогоны, прерванные прошлым запуском..."
python -m jobhunt.cli sweep-batches
```

- [ ] **Step 6: Run the CLI tests**

Run: `uv run pytest tests/integration/test_cli.py -q`
Expected: PASS, all of them.

- [ ] **Step 7: Commit**

```bash
git add src/jobhunt/cli.py docker-entrypoint.sh tests/integration/test_cli.py
git commit -m "feat(cli): parse opens a batch, sweep-batches closes the dead ones at start"
```

---

### Task 7: the read side for the panel

**Files:**
- Create: `src/jobhunt/web/data/collection.py`
- Test: `tests/integration/test_web_collection_data.py` (create)

**Interfaces:**
- Consumes: `RunSummary`, `summarize` (Task 5); `STALE_AFTER` (Task 2).
- Produces:
  - `CollectionState` frozen dataclass: `status: str` (`"never" | "running" | "stale" | "finished" | "interrupted"`), `mode: str | None`, `started_by: str | None`, `done: int`, `planned: int`, `current: str | None`, `found: int`, `started_at: datetime | None`, `finished_at: datetime | None`, `last_progress_at: datetime | None`, `summary: RunSummary | None`, property `busy: bool` — **`status == "running"` only**. A stale batch must leave the buttons enabled: the next run is what supersedes a batch left behind by a dead process, so treating `stale` as busy would lock the profile out for good.
  - `load_state(session, profile_id, *, now=None) -> CollectionState`
  - `planned_requests(session, profile_id) -> int`

- [ ] **Step 1: Write the failing tests**

Create `tests/integration/test_web_collection_data.py`. There is no shared conftest for web tests — helpers are copied per file, which is the established pattern in this repo. The header and the two helpers, in full:

```python
from datetime import UTC, datetime, timedelta

from jobhunt.db.models import ParseRun, Profile, ProfileTag
from jobhunt.ingest.batches import STALE_AFTER, finish_batch, open_batch
from jobhunt.parsers.registry import ALL_SOURCES
from jobhunt.web.data.collection import load_state, planned_requests

NOW = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)


def _profile(session, name="Кирилл") -> Profile:
    profile = Profile(name=name, collection_cities=[])
    session.add(profile)
    session.commit()
    return profile


def _run(session, batch, source: str, query: str, *, status: str, found: int = 0, new: int = 0):
    """Журнальная запись этой пачки. running — это запись без finished_at:
    ровно то, что оставляет run_source, пока запрос ещё идёт."""
    session.add(
        ParseRun(
            source=source,
            profile_id=batch.profile_id,
            batch_id=batch.id,
            query_params={"query": query},
            started_at=NOW,
            finished_at=None if status == "running" else NOW,
            status=status,
            found_count=found,
            new_count=new,
        )
    )
    session.flush()
```

And the cases:

```python
def test_state_of_a_profile_that_never_collected(session):
    profile = _profile(session)

    state = load_state(session, profile.id, now=NOW)

    assert state.status == "never"
    assert state.busy is False


def test_progress_counts_finished_requests_and_names_the_current_one(session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW
    )
    _run(session, batch, "work.ua", "Head of IT", status="success", found=70)
    _run(session, batch, "dou.ua", "Head of IT", status="success", found=58)
    _run(session, batch, "work.ua", "IT Director", status="running")
    session.commit()

    state = load_state(session, profile.id, now=NOW)

    assert state.status == "running"
    assert (state.done, state.planned) == (2, 4)
    assert state.current == "work.ua «IT Director»"
    assert state.found == 128
    assert state.busy is True


def test_a_batch_that_stopped_moving_reads_as_stale(session):
    profile = _profile(session)
    open_batch(session, profile.id, mode="full", started_by="cli", planned_requests=4, now=NOW)

    state = load_state(session, profile.id, now=NOW + STALE_AFTER + timedelta(seconds=1))

    assert state.status == "stale"
    assert state.started_by == "cli"


def test_the_idle_line_describes_the_last_batch(session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="quick", started_by="web", planned_requests=2, now=NOW
    )
    _run(session, batch, "work.ua", "Head of IT", status="failed", found=0)
    _run(session, batch, "dou.ua", "Head of IT", status="success", found=12, new=3)
    finish_batch(session, batch.id, now=NOW + timedelta(minutes=2))
    session.commit()

    state = load_state(session, profile.id, now=NOW + timedelta(hours=1))

    assert state.status == "finished"
    assert state.mode == "quick"
    assert state.summary.requests == 2
    assert state.summary.failed == 1
    assert state.summary.found == 12
    assert state.summary.new == 3


def test_only_this_profile_is_looked_at(session):
    mine = _profile(session, "Кирилл")
    other = _profile(session, "Второй")
    open_batch(session, other.id, mode="full", started_by="web", planned_requests=4, now=NOW)

    assert load_state(session, mine.id, now=NOW).status == "never"


def test_planned_requests_counts_enabled_tags_times_sources(session):
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    session.add(ProfileTag(profile_id=profile.id, text="IT Director", is_enabled=True))
    session.add(ProfileTag(profile_id=profile.id, text="CTO", is_enabled=False))
    session.commit()

    assert planned_requests(session, profile.id) == 2 * len(ALL_SOURCES)
```

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/integration/test_web_collection_data.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'jobhunt.web.data.collection'`.

- [ ] **Step 3: Write the module**

Create `src/jobhunt/web/data/collection.py`:

```python
"""Состояние сбора для панели: что показывать и можно ли жать кнопки.

Только чтение. Пачки открывает и закрывает `jobhunt.ingest.batches` — веб в
эту таблицу не пишет вовсе, и это держится тестом
`tests/unit/test_batch_write_boundary.py`.
"""

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from jobhunt.db.models import ParseBatch, ParseRun, ProfileTag
from jobhunt.ingest.batches import STALE_AFTER
from jobhunt.ingest.summary import RunSummary, summarize
from jobhunt.parsers.registry import ALL_SOURCES


@dataclass(frozen=True)
class CollectionState:
    """Одна пачка глазами страницы.

    status:
      never       — этот профиль ещё ни разу не собирал;
      running     — идёт прямо сейчас;
      stale       — числится идущим, но не двигается дольше STALE_AFTER:
                    процесс, который его вёл, почти наверняка убит;
      finished    — закончился сам;
      interrupted — закрыт подметанием или вытеснен следующим запуском.
    """

    status: str
    mode: str | None = None
    started_by: str | None = None
    done: int = 0
    planned: int = 0
    current: str | None = None
    found: int = 0
    started_at: datetime | None = None
    finished_at: datetime | None = None
    last_progress_at: datetime | None = None
    summary: RunSummary | None = None

    @property
    def busy(self) -> bool:
        """Кнопки выключены. `stale` сюда НЕ входит: зависшую пачку следующий
        запуск обязан вытеснить, иначе профиль заперт мёртвым процессом."""
        return self.status == "running"


def planned_requests(session: Session, profile_id: uuid.UUID) -> int:
    """Сколько запросов уйдёт: включённые теги × источники (см. run_profile)."""
    tags = session.execute(
        select(func.count())
        .select_from(ProfileTag)
        .where(ProfileTag.profile_id == profile_id, ProfileTag.is_enabled.is_(True))
    ).scalar_one()
    return tags * len(ALL_SOURCES)


def load_state(
    session: Session, profile_id: uuid.UUID, *, now: datetime | None = None
) -> CollectionState:
    """Последняя пачка профиля — идущая, если она есть, иначе самая свежая."""
    moment = now or datetime.now(UTC)
    batch = session.execute(
        select(ParseBatch)
        .where(ParseBatch.profile_id == profile_id)
        # Тай-брейкер по id обязателен: now() в PostgreSQL — константа внутри
        # транзакции, и две пачки, заведённые одной транзакцией, получают
        # одинаковый started_at.
        .order_by(ParseBatch.started_at.desc(), ParseBatch.id.desc())
        .limit(1)
    ).scalar_one_or_none()
    if batch is None:
        return CollectionState(status="never")

    runs = list(
        session.execute(select(ParseRun).where(ParseRun.batch_id == batch.id)).scalars()
    )
    finished = [run for run in runs if run.status != "running"]
    current_run = next((run for run in runs if run.status == "running"), None)

    status = batch.status
    if status == "running" and batch.last_progress_at < moment - STALE_AFTER:
        status = "stale"

    return CollectionState(
        status=status,
        mode=batch.mode,
        started_by=batch.started_by,
        done=len(finished),
        planned=batch.planned_requests,
        current=(
            f"{current_run.source} «{current_run.query_params.get('query', '?')}»"
            if current_run is not None
            else None
        ),
        found=sum(run.found_count for run in finished),
        started_at=batch.started_at,
        finished_at=batch.finished_at,
        last_progress_at=batch.last_progress_at,
        summary=summarize(finished) if finished else None,
    )
```

- [ ] **Step 4: Run the tests**

Run: `uv run pytest tests/integration/test_web_collection_data.py -q`
Expected: PASS (6 passed).

- [ ] **Step 5: Commit**

```bash
git add src/jobhunt/web/data/collection.py tests/integration/test_web_collection_data.py
git commit -m "feat(web): read side of the collection panel"
```

---

### Task 8: the panel on the page

**Files:**
- Create: `src/jobhunt/web/templates/_collection.html`
- Create: `src/jobhunt/web/routes/collection.py` (the GET only; POST arrives in Task 9)
- Modify: `src/jobhunt/web/app.py` (include the router)
- Modify: `src/jobhunt/web/templates/vacancies.html` (include the panel)
- Modify: `src/jobhunt/web/routes/vacancies.py` (`collection` in the page context)
- Modify: `src/jobhunt/web/templates/base.html` (styles for the panel)
- Test: `tests/integration/test_web_collection.py` (create)

**Interfaces:**
- Consumes: `load_state`, `CollectionState` (Task 7).
- Produces: `GET /vacancies/collection` returning the `_collection.html` fragment with `id="collection"`; the page context key `collection`.

- [ ] **Step 1: Write the failing tests**

Create `tests/integration/test_web_collection.py`. Header first — the `client` fixture is the one from `tests/integration/test_web_tags.py`, and `_profile` / `_run` are the two helpers written in Task 1 of this file's sibling (`test_web_collection_data.py`); copy them here rather than importing across test modules, which is what the other web test files do:

```python
from datetime import UTC, datetime, timedelta

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select

from jobhunt.db.models import ParseBatch, ParseRun, Profile, ProfileTag
from jobhunt.ingest.batches import finish_batch, open_batch
from jobhunt.web.app import app
from jobhunt.web.deps import get_session
from jobhunt.web.routes import collection as collection_routes

NOW = datetime(2026, 8, 5, 12, 0, tzinfo=UTC)


@pytest.fixture
def client(session):
    """TestClient с переопределённой зависимостью сессии — использует тестовую БД."""

    def _override_get_session():
        yield session

    app.dependency_overrides[get_session] = _override_get_session
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
```

Plus `_profile` and `_run` copied verbatim from `test_web_collection_data.py`. And the cases:

```python
def test_the_panel_is_on_the_page_even_with_no_tags(client, session):
    """Цель htmx-подмены обязана существовать всегда: на отсутствующую цель
    htmx не шлёт запрос вовсе и молчит об этом."""
    _profile(session)
    session.commit()

    html = client.get("/vacancies").text

    assert 'id="collection"' in html
    assert "Полная сверка" in html


def test_an_idle_panel_does_not_poll(client, session):
    _profile(session)
    session.commit()

    html = client.get("/vacancies/collection").text

    assert "every 3s" not in html


def test_a_running_panel_polls_and_shows_progress(client, session):
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=4, now=NOW
    )
    _run(session, batch, "work.ua", "Head of IT", status="success", found=70)
    _run(session, batch, "dou.ua", "IT Director", status="running")
    session.commit()

    html = client.get("/vacancies/collection").text

    assert "every 3s" in html
    assert "1 из 4" in html
    assert "dou.ua «IT Director»" in html


def test_the_panel_of_a_run_started_from_the_terminal_says_so(client, session):
    profile = _profile(session)
    open_batch(session, profile.id, mode="full", started_by="cli", planned_requests=4, now=NOW)
    session.commit()

    html = client.get("/vacancies/collection").text

    assert "из терминала" in html


def test_the_panel_follows_the_profile_in_the_address(client, session):
    mine = _profile(session, "Кирилл")
    other = _profile(session, "Второй")
    open_batch(session, other.id, mode="full", started_by="web", planned_requests=4, now=NOW)
    session.commit()

    html = client.get(f"/vacancies/collection?profile={other.id}").text

    assert "Собираю" in html
    assert f"profile={other.id}" in html
```

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/integration/test_web_collection.py -q`
Expected: FAIL — 404 on `/vacancies/collection`, and `id="collection"` is not in the page.

- [ ] **Step 3: Write the template**

Create `src/jobhunt/web/templates/_collection.html`:

```html
{# Панель сбора. Целится сама в себя и приезжает вместе со своей целью,
   поэтому id обязан быть на внешнем элементе: htmx на отсутствующую цель
   бросает htmx:targetError и не шлёт запрос вовсе — молча.

   Опрос живёт ровно столько, сколько идёт прогон: пока пачка running, ответ
   несёт hx-trigger="every 3s", а первый же ответ после её окончания его не
   несёт, и htmx прекращает опрашивать сам. Своего таймера у нас нет. #}
<div class="collection" id="collection"
     {% if collection.status == "running" %}
     hx-get="/vacancies/collection{{ profile_query }}"
     hx-target="#collection" hx-swap="outerHTML"
     hx-trigger="every 3s"
     {% endif %}>
  <div class="collection-buttons">
    <button type="button" class="collect"
            hx-post="/vacancies/collect{{ profile_query }}"
            hx-vals='{"mode": "quick"}'
            hx-target="#collection" hx-swap="outerHTML"
            {% if collection.busy or not can_collect %}disabled{% endif %}>
      Проверить новое
      <span class="muted">верхушка выдачи за сутки; пропавших не трогает</span>
    </button>
    <button type="button" class="collect"
            hx-post="/vacancies/collect{{ profile_query }}"
            hx-vals='{"mode": "full"}'
            hx-target="#collection" hx-swap="outerHTML"
            {% if collection.busy or not can_collect %}disabled{% endif %}>
      Полная сверка
      <span class="muted">вся выдача; отмечает исчезнувшие вакансии</span>
    </button>
  </div>

  <p class="collection-status">
    {% if not can_collect %}
      Собирать нечем: у профиля нет ни одного включённого тега.
    {% elif collection.status == "running" %}
      Собираю: {{ collection.done }} из {{ collection.planned }} запросов{% if collection.current %},
      сейчас {{ collection.current }}{% endif %}, найдено {{ collection.found }}.
      {% if collection.started_by == "cli" %}Прогон запущен из терминала.{% endif %}
    {% elif collection.status == "stale" %}
      Прогон не подаёт признаков жизни с {{ collection.last_progress_at.strftime("%H:%M") }} —
      похоже, он оборвался. Можно запустить заново.
    {% elif collection.status == "interrupted" %}
      Прошлый сбор прерван перезапуском. Собранное до обрыва сохранено.
    {% elif collection.status == "finished" and collection.summary %}
      {{ collection.finished_at.strftime("%d.%m %H:%M") }},
      {{ "полная сверка" if collection.mode == "full" else "проверка нового" }}:
      {{ collection.summary.requests }} запросов, найдено {{ collection.summary.found }},
      новых {{ collection.summary.new }}{% if collection.summary.has_problems %},
      с ошибкой {{ collection.summary.failed }}, усечено {{ collection.summary.truncated }}{% endif %}.
    {% elif collection.status == "finished" %}
      {# Пачка закрылась, не сделав ни одного запроса: теги выключили уже
         после её открытия. Сказать «сбор ещё не запускался» здесь значило бы
         соврать — он запускался и ничего не сделал. #}
      Сбор завершился, не отправив ни одного запроса: похоже, теги выключили
      уже после запуска.
    {% else %}
      Сбор ещё не запускался.
    {% endif %}
  </p>
</div>
```

- [ ] **Step 4: Write the route**

Create `src/jobhunt/web/routes/collection.py`:

```python
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from jobhunt.web.data.collection import CollectionState, load_state, planned_requests
from jobhunt.web.data.profiles import resolve_profile
from jobhunt.web.deps import get_session
from jobhunt.web.routes._common import remembered_profile_id
from jobhunt.web.templating import TEMPLATES

router = APIRouter()


def panel_context(
    session: Session, profile_id: uuid.UUID | None, requested: uuid.UUID | None
) -> dict:
    """Контекст панели — один на страницу и на фрагмент.

    Разойтись они не имеют права: страница рисует панель при загрузке, а
    фрагмент подменяет её же каждые три секунды.

    Профиля нет — панель всё равно рисуется, с выключенными кнопками: цель
    htmx-подмены обязана существовать в разметке всегда (инвариант слайса 2a).

    profile_query повторяет правило `_page_url` из роутов вакансий: профиль
    попадает в адреса панели, только если пришёл ИЗ АДРЕСА. Профиль из cookie
    — память браузера, а не выбор пользователя, и в адресе опроса ему незачем.
    """
    if profile_id is None:
        return {
            "collection": CollectionState(status="never"),
            "can_collect": False,
            "profile_query": "",
        }
    return {
        "collection": load_state(session, profile_id),
        "can_collect": planned_requests(session, profile_id) > 0,
        "profile_query": f"?profile={requested}" if requested is not None else "",
    }


@router.get("/vacancies/collection", response_class=HTMLResponse)
def collection_panel(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    profile: Annotated[uuid.UUID | None, Query()] = None,
) -> HTMLResponse:
    """Панель сбора отдельным фрагментом — её опрашивает htmx, пока идёт прогон."""
    resolved = resolve_profile(
        session, requested_id=profile, remembered_id=remembered_profile_id(request)
    )
    if profile is not None and resolved is None:
        raise HTTPException(status_code=404, detail="профиль не найден")
    return TEMPLATES.TemplateResponse(
        request=request,
        name="_collection.html",
        context=panel_context(session, resolved.id if resolved else None, profile),
    )
```

- [ ] **Step 5: Wire it into the page**

`src/jobhunt/web/app.py`: `from jobhunt.web.routes import collection, tags, vacancies` and `app.include_router(collection.router)`.

`src/jobhunt/web/routes/vacancies.py`, inside `vacancies_page`'s context dict, add `**panel_context(session, resolved.id if resolved else None, profile)` (import it from `jobhunt.web.routes.collection`).

`src/jobhunt/web/templates/vacancies.html`: add `{% include "_collection.html" %}` immediately **before** `{% include "_filters.html" %}`, inside the `{% else %}` branch that already renders the tool.

- [ ] **Step 6: Style it**

In `src/jobhunt/web/templates/base.html`, next to the `.tags-panel` rules, using the existing palette variables only (both themes then work by themselves):

```css
    .collection { margin-bottom: 1rem; }
    .collection-buttons { display: flex; gap: .5rem; flex-wrap: wrap; }
    .collect {
      display: inline-flex;
      flex-direction: column;
      align-items: flex-start;
      gap: .1rem;
      padding: .4rem .8rem;
      border: 1px solid var(--border);
      border-radius: .4rem;
      background: var(--surface);
      color: var(--fg);
      font: inherit;
      text-align: left;
      cursor: pointer;
    }
    .collect:hover:not(:disabled) { border-color: var(--muted); }
    .collect:focus-visible { outline: 2px solid var(--link); outline-offset: 2px; }
    .collect:disabled { opacity: .55; cursor: default; }
    .collection-status { margin: .5rem 0 0; font-size: .9rem; color: var(--muted); }
```

- [ ] **Step 7: Run the tests**

Run: `uv run pytest tests/integration/test_web_collection.py tests/integration/test_web_vacancies.py -q`
Expected: PASS. `test_web_vacancies.py` is in the list for one reason: it holds the htmx swap-target invariant, and the panel is a new target on the page.

- [ ] **Step 8: Commit**

```bash
git add src/jobhunt/web/templates/_collection.html src/jobhunt/web/routes/collection.py src/jobhunt/web/app.py src/jobhunt/web/routes/vacancies.py src/jobhunt/web/templates/vacancies.html src/jobhunt/web/templates/base.html tests/integration/test_web_collection.py
git commit -m "feat(web): collection panel with progress read from the journal"
```

---

### Task 9: the buttons actually start a run

**Files:**
- Create: `src/jobhunt/web/collection_runner.py`
- Modify: `src/jobhunt/web/routes/collection.py` (the POST)
- Create: `tests/unit/test_batch_write_boundary.py`
- Test: `tests/integration/test_web_collection.py`

**Interfaces:**
- Consumes: `open_batch`, `CollectionAlreadyRunning` (Task 2); `planned_requests` (Task 7).
- Produces: `POST /vacancies/collect` with form field `mode`; `jobhunt.web.collection_runner.start(profile_id, mode, batch_id) -> None`; the module attribute `start_collection` on the routes module, which tests replace.

- [ ] **Step 1: Write the failing tests**

Append to `tests/integration/test_web_collection.py`:

```python
@pytest.fixture
def started(monkeypatch):
    """Настоящий поток в тестах не поднимается — он ушёл бы в сеть.

    Подменяется атрибут модуля роутов, а не функция внутри collection_runner:
    роут зовёт именно его, и подмена ровно в точке вызова — тот же приём,
    которым тесты CLI подменяют run_profile."""
    calls = []
    monkeypatch.setattr(
        collection_routes, "start_collection", lambda **kwargs: calls.append(kwargs)
    )
    return calls


def test_pressing_a_button_opens_a_batch_and_starts_the_work(client, session, started):
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    session.commit()

    response = client.post("/vacancies/collect", data={"mode": "full"})

    assert response.status_code == 200
    batch = session.execute(select(ParseBatch)).scalar_one()
    assert batch.started_by == "web"
    assert batch.mode == "full"
    assert started == [{"profile_id": profile.id, "mode": "full", "batch_id": batch.id}]
    assert "Собираю" in response.text


def test_a_second_press_is_refused_with_the_panel(client, session, started):
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    open_batch(session, profile.id, mode="full", started_by="web", planned_requests=2, now=NOW)
    session.commit()

    response = client.post("/vacancies/collect", data={"mode": "quick"})

    # 409 и фрагментом: подставит его тот же обработчик htmx:responseError,
    # что уже работает на ячейке статуса.
    assert response.status_code == 409
    assert 'id="collection"' in response.text
    assert started == []


def test_an_unknown_mode_is_refused(client, session, started):
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=True))
    session.commit()

    assert client.post("/vacancies/collect", data={"mode": "everything"}).status_code == 400
    assert started == []


def test_a_profile_without_enabled_tags_cannot_start(client, session, started):
    profile = _profile(session)
    session.add(ProfileTag(profile_id=profile.id, text="Head of IT", is_enabled=False))
    session.commit()

    response = client.post("/vacancies/collect", data={"mode": "full"})

    assert response.status_code == 409
    assert session.execute(select(ParseBatch)).first() is None
    assert started == []
```

Create `tests/unit/test_batch_write_boundary.py`:

```python
"""Граница «пачки сбора пишет только ingest/batches.py».

Правило объявлено в спеке слайса 2b (§4.2) и в докстринге
web/data/collection.py. Без теста оно проживёт до первого роута, которому
покажется быстрее поправить статус на месте, — и тогда защита от второго
запуска, подметание и правило пятнадцати минут разойдутся по трём файлам.
"""

import ast
import pathlib

SRC_DIR = pathlib.Path(__file__).resolve().parents[2] / "src" / "jobhunt"
WRITER_PATH = "ingest/batches.py"
MODEL_PATH = "db/models.py"
BATCH_FIELDS = {"planned_requests", "started_by", "last_progress_at"}
WRITING_SQL_CONSTRUCTS = {"update", "insert", "delete"}


def violations(source: str, name: str) -> list[str]:
    """Записи в parse_batches в одном файле: конструктор, присваивание полю,
    запись через SQL-выражение."""
    offenders: list[str] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id == "ParseBatch":
                offenders.append(f"{name}:{node.lineno}: строит ParseBatch(...)")
            if isinstance(func, ast.Attribute) and func.attr == "ParseBatch":
                offenders.append(f"{name}:{node.lineno}: строит models.ParseBatch(...)")
            if (
                isinstance(func, ast.Name)
                and func.id in WRITING_SQL_CONSTRUCTS
                and node.args
                and isinstance(node.args[0], ast.Name)
                and node.args[0].id == "ParseBatch"
            ):
                offenders.append(f"{name}:{node.lineno}: пишет через {func.id}(ParseBatch)")
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Attribute) and target.attr in BATCH_FIELDS:
                    offenders.append(f"{name}:{node.lineno}: присваивает .{target.attr}")
    return offenders


def _scan() -> list[str]:
    offenders: list[str] = []
    for path in sorted(SRC_DIR.rglob("*.py")):
        relative = path.relative_to(SRC_DIR).as_posix()
        if relative in (WRITER_PATH, MODEL_PATH):
            continue
        offenders.extend(violations(path.read_text(encoding="utf-8"), relative))
    return offenders


def test_только_ingest_batches_пишет_пачки():
    assert _scan() == [], "запись пачек вне ingest/batches.py: " + "; ".join(_scan())


def test_граница_не_вырождена():
    """Прогон по настоящим файлам был бы зелёным и при пустой реализации."""
    assert violations("batch = ParseBatch(profile_id=x)", "web/routes/collection.py") == [
        "web/routes/collection.py:1: строит ParseBatch(...)"
    ]
    assert violations("batch.started_by = 'web'", "web/x.py") == [
        "web/x.py:1: присваивает .started_by"
    ]
    assert violations("session.execute(update(ParseBatch).values(status='x'))", "web/x.py") == [
        "web/x.py:1: пишет через update(ParseBatch)"
    ]
    assert violations("state = load_state(session, profile_id)", "web/x.py") == []
```

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/integration/test_web_collection.py tests/unit/test_batch_write_boundary.py -q`
Expected: FAIL — 405 on the POST (no such route), and the boundary test cannot import its own module-level names until the file exists (it will pass once written; run it now to see it green **after** step 4, and confirm at step 5 that it fails when the rule is broken).

- [ ] **Step 3: Write the runner**

Create `src/jobhunt/web/collection_runner.py`:

```python
"""Фоновый прогон сбора: единственное место, где веб-процесс уходит в сеть.

Поток, а не очередь задач: владелец выбрал, что перезапуск контейнера прогон
прерывает (спека, §2), — а раз долговечность через рестарт не нужна, платить
за неё отдельным сервисом незачем. Защита от второго запуска и наблюдаемость
живут в БД (`ingest/batches.py`), а не в памяти этого процесса: иначе прогон,
запущенный из терминала, был бы им не виден.
"""

import logging
import threading
import uuid

from jobhunt.db.base import get_session_factory
from jobhunt.http_client import HttpClient
from jobhunt.ingest.runner import run_profile

logger = logging.getLogger(__name__)


def start(*, profile_id: uuid.UUID, mode: str, batch_id: uuid.UUID) -> None:
    """Отправить прогон в фоновый поток и сразу вернуть управление.

    daemon=True: остановка контейнера не должна ждать минуты живого прогона.
    Недобитая пачка станет interrupted при следующем старте — это и есть
    выбранная модель долговечности, а не недосмотр.
    """
    threading.Thread(
        target=_run,
        kwargs={"profile_id": profile_id, "mode": mode, "batch_id": batch_id},
        daemon=True,
        name=f"collect-{batch_id}",
    ).start()


def _run(*, profile_id: uuid.UUID, mode: str, batch_id: uuid.UUID) -> None:
    """Тело потока. Пачку закрывает run_profile — здесь только клиент и лог.

    Второй финализации тут нет намеренно: два владельца разошлись бы во
    времени окончания и в статусе (спека, §7).
    """
    client = HttpClient(check_robots=True)
    try:
        run_profile(
            get_session_factory(), profile_id, client=client, mode=mode, batch_id=batch_id
        )
    except Exception:
        # Исключение в потоке иначе не видно нигде: у него нет вызывающего,
        # который мог бы его показать.
        logger.exception("сбор для профиля %s оборвался", profile_id)
    finally:
        client.close()
```

- [ ] **Step 4: Write the POST route**

In `src/jobhunt/web/routes/collection.py`:

```python
from fastapi import Form
from fastapi.responses import HTMLResponse

from jobhunt.ingest.batches import CollectionAlreadyRunning, open_batch
from jobhunt.web.collection_runner import start as start_collection

MODES = ("full", "quick")


@router.post("/vacancies/collect", response_class=HTMLResponse)
def start_collection_run(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    mode: Annotated[str, Form()],
    profile: Annotated[uuid.UUID | None, Query()] = None,
) -> HTMLResponse:
    """Открыть пачку и отдать работу фоновому потоку.

    Пачка открывается СИНХРОННО, до старта потока: отказ уникального индекса
    случился бы иначе уже после того, как браузер получил «сбор пошёл», и
    второе нажатие соврало бы.

    Отказ отдаётся кодом 409 и той же панелью: подставит её глобальный
    обработчик htmx:responseError из base.html — htmx 2 сам тело ответа при
    4xx не подставляет.
    """
    resolved = resolve_profile(
        session, requested_id=profile, remembered_id=remembered_profile_id(request)
    )
    if resolved is None:
        raise HTTPException(
            status_code=404 if profile is not None else 400, detail="профиль не найден"
        )
    if mode not in MODES:
        raise HTTPException(status_code=400, detail=f"неизвестный режим сбора {mode!r}")

    planned = planned_requests(session, resolved.id)
    if planned == 0:
        return TEMPLATES.TemplateResponse(
            request=request,
            name="_collection.html",
            context=panel_context(session, resolved.id, profile),
            status_code=409,
        )

    try:
        batch = open_batch(
            session,
            resolved.id,
            mode=mode,
            started_by="web",
            planned_requests=planned,
        )
    except CollectionAlreadyRunning:
        return TEMPLATES.TemplateResponse(
            request=request,
            name="_collection.html",
            context=panel_context(session, resolved.id, profile),
            status_code=409,
        )

    start_collection(profile_id=resolved.id, mode=mode, batch_id=batch.id)
    return TEMPLATES.TemplateResponse(
        request=request,
        name="_collection.html",
        context=panel_context(session, resolved.id, profile),
    )
```

- [ ] **Step 5: Run the tests, then verify the boundary is not vacuous**

Run: `uv run pytest tests/integration/test_web_collection.py tests/unit/test_batch_write_boundary.py tests/unit/test_web_boundary.py -q`
Expected: PASS.

Then prove the new boundary can fail: temporarily add `ParseBatch(profile_id=None)` to `src/jobhunt/web/routes/collection.py`, run `uv run pytest tests/unit/test_batch_write_boundary.py -q`, confirm it FAILS naming that line, and remove it. A boundary that has never failed is a boundary nobody has tested.

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/web/collection_runner.py src/jobhunt/web/routes/collection.py tests/integration/test_web_collection.py tests/unit/test_batch_write_boundary.py
git commit -m "feat(web): the buttons open a batch and hand the work to a thread"
```

---

### Task 10: the table refreshes itself when the run ends

**Files:**
- Modify: `src/jobhunt/web/routes/collection.py` (the `HX-Trigger` header)
- Modify: `src/jobhunt/web/templates/_filters.html` (second trigger on the form)
- Test: `tests/integration/test_web_collection.py`, `tests/integration/test_web_vacancies.py`

**Interfaces:**
- Produces: response header `HX-Trigger: jobhunt-collected` on the panel fragment when the run has ended and the request came from htmx.

- [ ] **Step 1: Write the failing tests**

Append to `tests/integration/test_web_collection.py`:

```python
def test_the_end_of_a_run_tells_the_page_to_reload_the_table(client, session):
    """Первый же ответ после окончания прогона и опрос прекращает, и таблицу
    просит перезапросить — именно он, потому что следующего опроса не будет."""
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW
    )
    _run(session, batch, "work.ua", "Head of IT", status="success", found=7)
    finish_batch(session, batch.id, now=NOW)
    session.commit()

    response = client.get("/vacancies/collection", headers={"HX-Request": "true"})

    assert response.headers["HX-Trigger"] == "jobhunt-collected"
    assert "every 3s" not in response.text


def test_a_running_panel_does_not_ask_for_a_reload(client, session):
    profile = _profile(session)
    open_batch(session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW)
    session.commit()

    response = client.get("/vacancies/collection", headers={"HX-Request": "true"})

    assert "HX-Trigger" not in response.headers


def test_a_plain_page_load_does_not_ask_for_a_reload(client, session):
    """Без HX-Request просить перезагрузку некого: заголовок услышал бы только
    htmx, а его тут нет."""
    profile = _profile(session)
    batch = open_batch(
        session, profile.id, mode="full", started_by="web", planned_requests=1, now=NOW
    )
    finish_batch(session, batch.id, now=NOW)
    session.commit()

    assert "HX-Trigger" not in client.get("/vacancies/collection").headers
```

Append to `tests/integration/test_web_vacancies.py`, next to the bubbled-change tests from slice 2a:

```python
def test_the_filters_form_listens_for_the_end_of_a_collection():
    """Таблицу после сбора перезапрашивает форма, а не панель: фильтры знает
    форма, и запрос обязан уйти с ними, иначе сбор молча сбросит показ."""
    markup = (TEMPLATES_DIR / "_filters.html").read_text(encoding="utf-8")
    form = FILTERS_FORM.search(JINJA_COMMENT.sub("", markup))
    trigger = HX_TRIGGER.search(form.group(0)).group(1)

    assert "jobhunt-collected from:body" in trigger
    # И прежний триггер на месте: новое событие — отдельная запись в списке,
    # а не расширение того, что уже есть (иначе вернётся всплывший change).
    assert "change from:(" in trigger
```

- [ ] **Step 2: Run and watch them fail**

Run: `uv run pytest tests/integration/test_web_collection.py tests/integration/test_web_vacancies.py -q -k "collected or reload"`
Expected: FAIL — `KeyError: 'HX-Trigger'` and the assertion on the form trigger.

- [ ] **Step 3: Set the header**

In `src/jobhunt/web/routes/collection.py`, inside `collection_panel`, after building the response:

```python
    response = TEMPLATES.TemplateResponse(
        request=request,
        name="_collection.html",
        context=context,
    )
    # Ответ, в котором прогон впервые оказался законченным, — единственный:
    # он же перестаёт нести hx-trigger="every 3s", и следующего опроса не
    # будет. Событие слушает форма фильтров и перезапрашивает строки С
    # ТЕКУЩИМИ ФИЛЬТРАМИ — панель про фильтры не знает и знать не должна.
    #
    # Имя через дефис, а не через двоеточие: `:` в грамматике триггеров htmx
    # вводит модификаторы (delay:, from:), и имя события — не место выяснять,
    # как токенизатор разрешает неоднозначность.
    if request.headers.get("HX-Request") and context["collection"].status in (
        "finished",
        "interrupted",
        # stale тоже: прогон мёртв, но собранное им уже в базе, и показать
        # это некому — опрос на этом ответе всё равно прекращается.
        "stale",
    ):
        response.headers["HX-Trigger"] = "jobhunt-collected"
    return response
```

- [ ] **Step 4: Add the second trigger**

In `src/jobhunt/web/templates/_filters.html`:

```html
      hx-trigger="change from:(#filters select, #filters input[type=checkbox]), jobhunt-collected from:body"
```

and extend the comment above the form with one sentence: the second spec re-requests the rows when a collection ends, and it is a separate entry in the list rather than a widening of the first.

- [ ] **Step 5: Run the tests**

Run: `uv run pytest tests/integration/test_web_collection.py tests/integration/test_web_vacancies.py -q`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/jobhunt/web/routes/collection.py src/jobhunt/web/templates/_filters.html tests/integration/test_web_collection.py tests/integration/test_web_vacancies.py
git commit -m "feat(web): the table reloads itself when a collection ends"
```

---

### Task 11: documentation catches up with the code

**Files:**
- Modify: `docs/superpowers/specs/2026-08-05-collection-from-the-browser-design.md` (§4.4)
- Modify: `CLAUDE.md` (boundaries table, invariants)
- Modify: `docs/HANDOFF.md` (sections 3 and 6)

No new behaviour. This is the task that keeps the next session from re-deriving what this one decided.

- [ ] **Step 1: Correct the spec**

In §4.4, replace "A sweep at application startup (`sweep_interrupted`, called from the FastAPI lifespan)" with the CLI form and the reason:

```markdown
- **A sweep at container start** — `jobhunt sweep-batches`, called by
  `docker-entrypoint.sh` right after `alembic upgrade head`. Not the FastAPI
  lifespan, although that is the obvious place: inside the web process the only
  way to get a session outside a request is `session_scope()`, which reads
  `settings.database_url` — the developer's database. Every test that does
  `with TestClient(app)` would then sweep production data, which `CLAUDE.md`
  forbids outright.
```

- [ ] **Step 2: Record the new boundary in `CLAUDE.md`**

Add a row to the boundaries table:

```markdown
| `tests/unit/test_batch_write_boundary.py` | collection batches are written only by `ingest/batches.py` |
```

And to "Invariants worth knowing before editing":

```markdown
- One running batch per profile is a **partial unique index**, not a check in code.
  `open_batch` commits on purpose: the worker thread and the CLI live in other
  sessions, and an uncommitted batch is invisible to them.
- `run_source` commits the journal row as `running` **before** the request. That is
  what makes progress observable — and what makes a killed process leave a dangling
  row, which `sweep_interrupted` and `STALE_AFTER` clean up.
- The batch is closed by `run_profile` and by nobody else. Two owners would disagree
  about the end time and the status.
```

- [ ] **Step 3: Update the state handoff**

In `docs/HANDOFF.md` section 3, add `ingest/batches.py`, `ingest/summary.py`, `web/data/collection.py`, `web/collection_runner.py` and `web/routes/collection.py` to the file map with one line each. Section 6's row about `running` was already corrected in Task 3 — check it reads correctly next to the new text and fix it if not.

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/specs/2026-08-05-collection-from-the-browser-design.md CLAUDE.md docs/HANDOFF.md
git commit -m "docs: the sweep is a CLI command, and the new boundaries are written down"
```

---

### Task 12: live check on the production database, then in the browser

The last task, and it is a task rather than a step inside another one — for the same reason it was in slice 2a: this is the only place where htmx at runtime, the address bar and the network panel are checked, and folded into another task it gets skipped.

**Files:**
- Modify: `docs/HANDOFF.md` (a new section with the results)

- [x] **Step 1: Restart the app and measure the panel**

```bash
docker compose restart app
```

Then measure the fragment the poll hits — ten requests against the production database, once with no run in progress and once during a run. Write the script to the session scratchpad, not into the repository:

```python
# measure_panel.py
import statistics
import time
import urllib.request

URL = "http://localhost:8000/vacancies/collection"
samples = []
for _ in range(10):
    started = time.perf_counter()
    urllib.request.urlopen(URL).read()
    samples.append((time.perf_counter() - started) * 1000)

print("median ms:", round(statistics.median(samples), 1))
print("max ms:", round(max(samples), 1))
```

Run: `uv run python measure_panel.py`

Write the median into this plan under this step, both idle and during a run. **The decision it feeds:** if the median is above ~150 ms, three seconds of polling is not free and the interval has to be reconsidered before the browser check, not after. Slice 2a's reference numbers on the same database: data access ~4 ms, page render 6.4 ms.

**Measured 2026-08-05:** median **3.7 ms** idle (908 bytes) and **4.3 ms** during a run (1112 bytes); max 22 ms once the first cold request is past. Two orders of magnitude under the threshold — **the interval stays at three seconds.**

- [x] **Step 2: Walk the browser checklist**

Use a direct Playwright script against the cached chromium, or the Playwright MCP server if it now starts (it was pointed at Edge on 2026-08-05 and takes effect in a fresh process). Read the two harness traps in `docs/HANDOFF.md` §5в first — Cyrillic typed through `insertText` fires no `keyup`, and first batches are not full lists.

Scenarios, each recorded with its result:

1. «Проверить новое» starts a run: the status line switches to «Собираю: 0 из N» without a page reload.
2. While it runs, both buttons are disabled, and the counter moves at least once during the run.
3. The network panel shows one `GET /vacancies/collection` roughly every three seconds — and **no** requests to `/vacancies/rows` while the run is going.
4. When the run ends, polling stops (no further requests to the panel) and the table is re-requested exactly once.
5. The table comes back **with the filters still applied**: set a chip and a status filter before pressing the button, and confirm both survive the refresh.
6. A second press during a run is impossible (the button is disabled); pressing via the address bar — `curl -X POST` with `mode=full` — returns 409 and the panel.
7. A run started from the terminal (`uv run python -m jobhunt.cli parse --profile "Кирилл" --mode quick`) is reflected the moment the panel is next read: reload the page during the run and the buttons are disabled and the line says «запущен из терминала». **Do not expect an already-open idle page to notice by itself** — spec §6 gives the fragment `hx-trigger="every 3s"` only while a batch is running, so an idle page has no poll at all. Check the recovery path too: pressing a button on such a stale page must come back 409 and heal the panel in the same swap.
8. `docker compose restart app` mid-run: after the restart the panel says the previous run was interrupted, and the vacancies collected before the break are in the table.
9. A profile with every tag disabled: the buttons are disabled and the panel says what is missing, and pressing is impossible.
10. Dark theme: the panel, both buttons and the status line are legible, and keyboard focus is visible on both buttons.

- [x] **Step 3: Record the results**

Add a section to `docs/HANDOFF.md` in the shape of §5в — a table of scenario and result, the measured numbers, and anything the check found that the plan did not predict. If production data was changed (a real collection run does change it), say what was changed and what was compared afterwards.

- [x] **Step 4: Commit**

```bash
git add docs/HANDOFF.md docs/superpowers/plans/2026-08-05-collection-from-the-browser.md
git commit -m "docs: live check of collection from the browser"
```

---

## Controller's checklist after the last task

- [x] `uv run pytest -q` — the whole suite, once, in the main session
- [x] `uv run ruff check src tests` and `uv run ruff format --check src tests`
- [x] `docker compose restart app` and one manual look at `/vacancies`
- [ ] `superpowers:finishing-a-development-branch`
