"""`guppi sprint-close --sprint <id> [--apply] [--carry SLUG] [--archive-unread SLUG]` — the close
of a sprint: its finished work leaves the live pages.

The close of `entity-sprint-<id>` moves (cases 612, 627):
- each Decision page whose `sprint` is `<id>`, but one that a page staying live names in
  `deferred_by` or `addressed_by` (case 627.1);
- each Insight of the sprint that stands `actioned`, and each lesson of the sprint of `kind:
  error` that stands `new`, but a lesson an `open` Insight lists in `children` (case 627.2);
- the sprint page and each Estimate its `estimates` lists; every other `passed` Estimate
  stays, and the MOC `entity-sprint` stays (case 627.3);
- each Estimate named by `--archive-unread` (case 627.4).

Each live Estimate that stands `pending` or `failed` is listed. It is settled when it is named
by `--carry` (it stays live with its status) or by `--archive-unread` (it goes), or when the
sprint page lists it and it stands `failed` — a reading read now that came out `failed` goes
with the sprint page with no choice by name. An Estimate of the sprint page is never carried:
`--carry` on it is refused. A slug named that is no listed Estimate is refused (case 627.4).

Without `--apply` the command prints the preview — each page it would move, each page of the
sprint it keeps and why, each listed Estimate and how it stands — and changes nothing. With
`--apply` it refuses, moving nothing and printing each reason on stderr, while a listed
Estimate is not settled; otherwise it sets `status: archived` on each page it moves, with a
History line that keeps the old status, through the page writer of `guppi/generate.py`, runs
`guppi cleanup`, which moves them under `vault/archive/`, and then ticks each unticked task
line of a `spec.md` under `vault/raw/` that `render.command_line("guppi sprint-close --sprint
<id> --apply")` matches — the one matcher of the tickers, imported — so the librarian, which
runs the line after `guppi generate`, finds it done; a refused run ticks nothing (case
628.1).

After that, the close empties `vault/raw/` as far as it can (cases 743.1, 743.3). It moves each
unit that `guppi/archive.py` judges done by `archive.sweep` with `close=True`, whatever its
date, and prints its lines: the session of the run, a unit not yet turned into pages and a
conserved Spec stay. Then it moves each `vault/raw/<date>/event_log.md` dated before the day
before the date of the session of the run to `vault/archive/<id>/<date>/event_log.md`, one
line `archive: raw/<date>/event_log.md → archive/<id>/<date>/event_log.md` per log, since the
hooks of the open session read only the logs back to the start of that session; a log whose
target exists stays, with one line on stderr. A date folder the moves leave empty is removed.
`.gitignore` leaves the moved logs out of git. The preview names each unit and each log the
close would move and moves none; a refused close moves none. Exit 0 on a preview or a close,
1 on a refusal or an error — a unit or a log that failed to move too, after the other moves —
2 on bad arguments.
Rule page: `vault/wiki/rules/rule-sprint-close.md`.
"""

import argparse
import io
import shutil
import sys
from datetime import date as Date
from datetime import datetime, timedelta
from pathlib import Path

from guppi import archive, cleanup
from guppi.event import project_root
from guppi.generate import HISTORY, as_list, write_page
from guppi.ledger import SPRINT_PAGE
from guppi.materialize import session_of_run, units_with
from guppi.pages import Page, read_vault, wiki_root
from guppi.render import command_line

UNREAD = ("pending", "failed")
KEEPERS = ("deferred_by", "addressed_by")


class Close:
    """The pages of one close, judged once; the preview and the run read the same lists."""

    def __init__(self, pages: dict[str, list[Page]], sprint: str, carry, unread):
        self.sprint = sprint
        self.carry = list(carry)
        self.unread = list(unread)
        live = [p for category in pages.values() for p in category if not p.error]
        self.by_slug = {p.slug: p for p in live}
        self.page = self.by_slug.get(SPRINT_PAGE + sprint)
        self.move: dict[str, Page] = {}  # slug → page, in the order of the judgment
        self.why: dict[str, str] = {}
        self.keep: list[tuple[Page, str]] = []
        self.errors: list[str] = []
        if self.page is None or self.page.category != "entities":
            self.errors.append(f"sprint-close: no live {SPRINT_PAGE}{sprint} page")
            return
        own = as_list(self.page.props.get("estimates"))
        self.listed = [
            p for p in pages["estimates"] if not p.error and str(p.props.get("status")) in UNREAD
        ]
        self.judge_estimates(own)
        self.add(self.page, "the sprint page")
        for slug in own:
            estimate = self.by_slug.get(slug)
            if estimate is not None:
                self.add(estimate, "an Estimate of the sprint page")
        for slug in self.unread:
            if slug in self.by_slug and slug not in self.move:
                self.add(self.by_slug[slug], "archived unread")
        self.judge_insights_and_lessons(pages)
        self.judge_decisions(pages)

    def of_sprint(self, page: Page) -> bool:
        return str(page.props.get("sprint") or "") == self.sprint

    def add(self, page: Page, why: str) -> None:
        if str(page.props.get("status")) == "archived" or page.slug in self.move:
            return
        self.move[page.slug] = page
        self.why[page.slug] = why

    def judge_estimates(self, own: list[str]) -> None:
        listed = {p.slug for p in self.listed}
        for slug in self.carry + self.unread:
            if slug not in listed:
                self.errors.append(
                    f"sprint-close: {slug}: no live Estimate that stands pending or failed"
                )
        for slug in self.carry:
            if slug in own:
                self.errors.append(
                    f"sprint-close: {slug}: an Estimate of the sprint page is never carried; "
                    "read it now or archive it unread"
                )
        for estimate in self.listed:
            if not self.settled(estimate, own):
                self.errors.append(
                    f"sprint-close: {estimate.slug}: {estimate.props.get('status')} and not named: "
                    "read it now, or name it by --carry or --archive-unread"
                    if estimate.slug not in own
                    else f"sprint-close: {estimate.slug}: {estimate.props.get('status')}, an "
                    "Estimate of the sprint page: read it now or name it by --archive-unread"
                )

    def settled(self, estimate: Page, own: list[str]) -> bool:
        if estimate.slug in self.unread:
            return True
        if estimate.slug in own:
            return str(estimate.props.get("status")) == "failed"
        return estimate.slug in self.carry

    def judge_insights_and_lessons(self, pages: dict[str, list[Page]]) -> None:
        held: set[str] = set()
        for insight in pages["insights"]:
            if insight.error or not self.of_sprint(insight):
                continue
            status = str(insight.props.get("status"))
            if status == "actioned":
                self.add(insight, "an actioned Insight of the sprint")
            elif status == "open":
                held.update(as_list(insight.props.get("children")))
                self.keep.append((insight, "an open Insight"))
        for lesson in pages["lessons"]:
            if lesson.error or not self.of_sprint(lesson):
                continue
            if lesson.slug in held:
                self.keep.append((lesson, "a child of an open Insight"))
            elif (
                str(lesson.props.get("kind")) == "error"
                and str(lesson.props.get("status")) == "new"
            ):
                self.add(lesson, "an error lesson of the sprint that joined no Insight")
            elif str(lesson.props.get("kind")) == "knowledge":
                self.keep.append((lesson, "a knowledge lesson"))

    def judge_decisions(self, pages: dict[str, list[Page]]) -> None:
        named: dict[str, str] = {}
        for page in self.by_slug.values():
            if page.slug in self.move or page.category == "decisions":
                continue
            for field in KEEPERS:
                for slug in as_list(page.props.get(field)):
                    named.setdefault(slug, f"named in {field} of {page.slug}")
        for decision in pages["decisions"]:
            if decision.error or not self.of_sprint(decision):
                continue
            if str(decision.props.get("status")) == "archived":
                continue
            if decision.slug in named:
                self.keep.append((decision, named[decision.slug]))
            else:
                self.add(decision, "a Decision page of the sprint")

    def estimate_lines(self) -> list[str]:
        own = as_list(self.page.props.get("estimates")) if self.page else []
        lines = []
        for estimate in self.listed:
            status = estimate.props.get("status")
            target = estimate.props.get("target") or ""
            if estimate.slug in self.unread:
                way = "archived unread"
            elif estimate.slug in self.carry and estimate.slug not in own:
                way = "carried into the next sprint"
            elif estimate.slug in own and status == "failed":
                way = "goes with the sprint page, its status kept"
            else:
                way = "not settled"
            lines.append(f"unread: estimates/{estimate.slug} {status} · {target} · {way}")
        return lines

    def preview(self) -> list[str]:
        lines = [f"sprint-close: {self.sprint} — preview, nothing moved"]
        lines += [f"move: {p.category}/{slug} · {self.why[slug]}" for slug, p in self.move.items()]
        lines += [f"keep: {p.category}/{p.slug} · {why}" for p, why in self.keep]
        lines += self.estimate_lines()
        return lines


def mark(page: Page, date: str, sprint: str) -> None:
    """`status: archived` with a History line that keeps the old status."""
    old = str(page.props.get("status") or "")
    page.props["status"] = "archived"
    line = f"- {date} status: {old} → archived · the close of sprint {sprint} (sprint-close)"
    current = page.sections.get(HISTORY, "").strip("\n")
    page.sections[HISTORY] = (current + "\n" + line).strip("\n")
    write_page(page.path, page.props, page.sections, page.category)


def tick(project_dir: Path, sprint: str) -> int:
    """Case 628.1: each unticked close line of a `spec.md` under `vault/raw/`, by the one
    matcher of the tickers; the count ticked."""
    pattern = command_line(f"guppi sprint-close --sprint {sprint} --apply")
    ticked = 0
    for unit in units_with(project_dir, "spec.md"):
        spec = project_dir / "vault" / "raw" / unit / "spec.md"
        lines = spec.read_text(encoding="utf-8").split("\n")
        changed = False
        for index, line in enumerate(lines):
            if pattern.match(line):
                lines[index] = "- [x]" + line[len("- [ ]") :]
                changed = True
                ticked += 1
        if changed:
            spec.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return ticked


def old_logs(project_dir: Path, now) -> list[Path]:
    """Case 743.3: each `vault/raw/<date>/event_log.md` dated before the day before the date
    of the session of the run — the logs no hook of the open session reads."""
    raw = project_dir / "vault" / "raw"
    if not raw.is_dir():
        return []
    today = now.date().isoformat()
    session = session_of_run(project_dir, today)
    start = Date.fromisoformat(session[0] if session else today)
    limit = (start - timedelta(days=1)).isoformat()
    return sorted(
        folder / "event_log.md"
        for folder in raw.iterdir()
        if folder.is_dir() and folder.name < limit and (folder / "event_log.md").is_file()
    )


def move_logs(project_dir: Path, sprint: str, now, stdout, stderr, apply: bool = True) -> bool:
    """Move the old logs under `vault/archive/<sprint>/<date>/`; True when one failed."""
    failed = False
    for log in old_logs(project_dir, now):
        date = log.parent.name
        target = project_dir / "vault" / "archive" / sprint / date / "event_log.md"
        where = f"archive/{sprint}/{date}/event_log.md"
        if not apply:
            print(f"archive: raw/{date}/event_log.md would move → {where}", file=stdout)
            continue
        if target.exists():
            print(f"archive: raw/{date}/event_log.md not moved: vault/{where} exists", file=stderr)
            failed = True
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(log), str(target))
        print(f"archive: raw/{date}/event_log.md → {where}", file=stdout)
    return failed


def remove_empty_dates(project_dir: Path) -> None:
    """A date folder of `vault/raw/` that the moves left empty goes."""
    raw = project_dir / "vault" / "raw"
    for folder in sorted(raw.iterdir()) if raw.is_dir() else []:
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()


def empty_raw(project_dir: Path, sprint: str, now, stdout, stderr, apply: bool = True) -> bool:
    """Cases 743.1, 743.3: the sweep of the done units, then the old logs; True when a move
    failed."""
    failed = archive.sweep(project_dir, now, stdout, stderr, close=True, apply=apply)
    failed = move_logs(project_dir, sprint, now, stdout, stderr, apply=apply) or failed
    if apply:
        remove_empty_dates(project_dir)
    return failed


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi sprint-close", description=__doc__.split("\n\n")[0])
    p.add_argument("--sprint", required=True, help="the id of entity-sprint-<id>")
    p.add_argument("--apply", action="store_true", help="close; without it, the preview")
    p.add_argument("--carry", action="append", default=[], metavar="SLUG")
    p.add_argument("--archive-unread", action="append", default=[], metavar="SLUG")
    return p


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    close = Close(read_vault(wiki_root(project_dir)), args.sprint, args.carry, args.archive_unread)
    if close.page is None:
        for line in close.errors:
            print(line, file=stderr)
        return 1
    if not args.apply:
        for line in close.preview():
            print(line, file=stdout)
        for line in close.errors:
            print(line, file=stdout)
        empty_raw(project_dir, args.sprint, now, stdout, stderr, apply=False)
        return 0
    if close.errors:
        for line in close.errors:
            print(line, file=stderr)
        print(f"sprint-close: {args.sprint}: refused, nothing moved", file=stderr)
        return 1
    date = now.date().isoformat()
    record = close.estimate_lines()  # before the marks: the record keeps each status
    for page in close.move.values():
        mark(page, date, args.sprint)
    out = io.StringIO()
    code = cleanup.run([], stdout=out, stderr=stderr, project_dir=project_dir, now=now)
    for line in record:
        print(line, file=stdout)
    print(
        f"sprint-close: {args.sprint}: {len(close.move)} page(s) marked archived; {out.getvalue().strip()}",
        file=stdout,
    )
    if code != 0:
        return 1
    tick(project_dir, args.sprint)
    return 1 if empty_raw(project_dir, args.sprint, now, stdout, stderr) else 0
