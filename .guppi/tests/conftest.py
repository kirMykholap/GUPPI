"""The clock of the tests, pinned (case 145.1).

Every `run()` of `.guppi/guppi/` reads the clock only when no `now` is passed. A test that forgets
`now` passed on the day it was written and went red later, twice (2026-09-10, 09-11). The
autouse fixture below replaces `datetime` in every `guppi` module that imports it by a
subclass whose `now()` returns 2001-01-01 00:00:00 UTC, so a forgotten `now` shows the year
2001 at once. The list of modules is built by the walk, never by hand. Rule page:
`vault/wiki/rules/rule-tests-clock-pinned.md`.
"""

import importlib
import pkgutil
from datetime import UTC, datetime

import pytest

import guppi

PINNED = datetime(2001, 1, 1, 0, 0, 0, tzinfo=UTC)


class PinnedDatetime(datetime):
    """`datetime` whose `now()` is the pinned moment; everything else as the real class."""

    @classmethod
    def now(cls, tz=None):
        moment = cls(2001, 1, 1, 0, 0, 0, tzinfo=UTC)
        return moment.astimezone(tz) if tz is not None else moment

    def astimezone(self, tz=None):
        """Without a zone, UTC — not the machine's: the pinned wall clock reads the same
        everywhere (`run()` calls `datetime.now().astimezone()`)."""
        return super().astimezone(tz if tz is not None else UTC)


def clock_modules():
    """Every module under `.guppi/guppi/` that carries a `datetime` attribute."""
    out = []
    for info in pkgutil.iter_modules(guppi.__path__, prefix="guppi."):
        module = importlib.import_module(info.name)
        attr = getattr(module, "datetime", None)
        if isinstance(attr, type) and issubclass(attr, datetime):
            out.append(module)
    return out


@pytest.fixture(autouse=True)
def pinned_clock(monkeypatch):
    for module in clock_modules():
        monkeypatch.setattr(module, "datetime", PinnedDatetime)
    yield PINNED
