"""`guppi archive` — an applied unit of `raw/` moves whole into the archive of its date.

A unit is a session folder `vault/raw/<date>/<HHMM>/` holding a `ledger.md`, or a
date-level `vault/raw/<date>/ledger.md` with its yaml (the shape before case 103). Only
units dated before the day of the run are looked at, and never the session of the run —
the latest `<HHMM>/` folder of the run day, else the nearest date back — since Retro and
the readings still write into it after the librarian's commit. A unit is done when its
`materialize.yaml` exists, every entry under `entries` carries `applied` or `superseded_by`,
and every line of its `ledger.md` that `materialize.parse_line` reads as a record has its
number in the `line` or `folded` of an entry or under `unparsed` (case 100.1).

A done session moves whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. A done
date-level unit moves with its yaml and everything else at the date root to
`vault/archive/<sprint>/<date>/raw/`, and with it every `<HHMM>/` folder of the date that
has no ledger of its own, each to `vault/archive/<sprint>/<date>/<HHMM>/raw/`; a session
folder with its own ledger is a unit of its own and stays until it is done. `event_log.md`
stays in `vault/raw/<date>/`: it is gitignored and the ledger hook walks it for the `hi`
window. No file is cut and no pointer is rewritten: `raw/<date>[/<HHMM>]/ledger.md#…` stays
the name of a ledger, which lint resolves in `raw/` or in the archive (case 103.5).

Stdout carries one line per unit: `archive: raw/<unit> → archive/<sprint>/<unit>[/raw]` or
`archive: raw/<unit> kept: <reason>` — `no yaml`, `N entries not applied`, `N ledger lines
outside the yaml`. A name already taken in the archive or a move that fails is a line on
stderr and exit 1; the other units still move. A rerun moves nothing and exits 0. The
coverage of a line is the one function `guppi tail` uses (`rule-ledger-tail`). Rule page:
`vault/wiki/rules/rule-raw-archive.md`.
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root
from guppi.materialize import (
    SESSION_FOLDER,
    load_yaml,
    parse_line,
    session_of_run,
    sprint_id,
    units_with,
    yaml_path,
)


def uncovered_lines(project_dir: Path, unit: str) -> list[tuple[int, str]]:
    """`(number, line)` of every record line of the unit's ledger that its yaml does not
    name — by `line` or `folded` of an entry, or under `unparsed`. Without a yaml every
    record line is uncovered. Shared by `archive` and `tail` (cases 100.1, 101.2)."""
    ledger = project_dir / "vault" / "raw" / unit / "ledger.md"
    data = load_yaml(yaml_path(project_dir, unit)) or {}
    covered: set[int] = set()
    for entry in data.get("entries") or []:
        if isinstance(entry, dict):
            if "line" in entry:
                covered.add(int(entry["line"]))
            covered |= {int(n) for n in entry.get("folded") or []}
    for item in data.get("unparsed") or []:
        if isinstance(item, dict) and "line" in item:
            covered.add(int(item["line"]))
        elif isinstance(item, int):
            covered.add(item)
    out: list[tuple[int, str]] = []
    for number, text in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        if number not in covered and parse_line(text) is not None:
            out.append((number, text))
    return out


def kept_reason(project_dir: Path, unit: str) -> str | None:
    """Why a unit is not done, or None when it is."""
    data = load_yaml(yaml_path(project_dir, unit))
    if data is None:
        return "no yaml"
    pending = [
        e
        for e in data.get("entries") or []
        if isinstance(e, dict) and not e.get("applied") and not e.get("superseded_by")
    ]
    if pending:
        return f"{len(pending)} entries not applied"
    outside = uncovered_lines(project_dir, unit)
    if outside:
        return f"{len(outside)} ledger lines outside the yaml"
    return None


def moves_of(project_dir: Path, unit: str, sprint: str) -> list[tuple[Path, Path]]:
    """`(source, target)` pairs of a unit: a session folder whole into `<unit>/raw/`; a
    date-level unit's root files into `<date>/raw/` and its ledger-less session folders
    into `<date>/<HHMM>/raw/`."""
    raw = project_dir / "vault" / "raw" / unit
    archive = project_dir / "vault" / "archive" / sprint
    if "/" in unit:
        return [(raw, archive / unit / "raw")]
    pairs: list[tuple[Path, Path]] = []
    for path in sorted(raw.iterdir()):
        if path.name == "event_log.md":
            continue
        if path.is_dir() and SESSION_FOLDER.match(path.name):
            if not (path / "ledger.md").is_file():
                pairs.append((path, archive / unit / path.name / "raw"))
            continue
        pairs.append((path, archive / unit / "raw" / path.name))
    return pairs


def move(source: Path, target: Path) -> None:
    if target.exists():
        raise FileExistsError(f"{target} exists")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(target))


def parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(prog="guppi archive", description=__doc__.split("\n\n")[1])


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    today = now.date().isoformat()
    session = session_of_run(project_dir, today)
    running = f"{session[0]}/{session[1]}" if session else None
    sprint = sprint_id(project_dir)
    failed = False
    for unit in units_with(project_dir, "ledger.md"):
        if unit.split("/")[0] >= today or unit == running:
            continue
        try:
            reason = kept_reason(project_dir, unit)
            if reason:
                print(f"archive: raw/{unit} kept: {reason}", file=stdout)
                continue
            pairs = moves_of(project_dir, unit, sprint)
            taken = [t for _, t in pairs if t.exists()]
            if taken:
                rel = taken[0].relative_to(project_dir).as_posix()
                print(f"archive: raw/{unit} not moved: {rel} exists", file=stderr)
                failed = True
                continue
            for source, target in pairs:
                move(source, target)
            where = f"archive/{sprint}/{unit}/raw"
            print(f"archive: raw/{unit} → {where}", file=stdout)
        except Exception as exc:  # noqa: BLE001 — one unit fails alone, the walk goes on
            print(f"archive: raw/{unit} not moved: {exc}", file=stderr)
            failed = True
    return 1 if failed else 0
