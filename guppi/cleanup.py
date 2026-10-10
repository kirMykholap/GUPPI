"""`guppi cleanup` — archived pages leave the live vault, restored ones come back.

Every live page under `vault/wiki/<category>/` with `status: archived` moves to
`vault/archive/<sprint>/<date>/<HHMM>/<category>/<slug>.md` — `date` the day of the run,
`HHMM` the session of the run: the latest `<HHMM>/` folder under `raw/<date>/`, and without
one the latest of the nearest date back; `<date>/<category>/` when no session folder
exists (case 102.2) — with a History line and a `log.md` line; its slug leaves the `children` lists of live pages and the `estimates` lists of
entities and rules (an Insight's `children` keep it, since `severity` counts the live
ones; a lesson has no Estimates, case 53.1); `[[slug]]` links in page bodies stay. A page
under `vault/archive/`, at any depth, whose status is no longer `archived` moves back. A live page whose
`parent` or `target` is in the archive is reported, not moved. No index is rewritten: the
index files are gone, the reader computes the line (case 147.6).
`raw/` is `guppi archive`'s, not this script's. Rule page: `vault/wiki/rules/rule-cleanup.md`.

`sprint` is the `sprint` field of the `materialize.yaml` of the session of the run, by
`unit_sprint` of `guppi/materialize.py`, the one judgment `guppi archive` and `guppi generate`
import too; the first `## <id>` heading of `sprint.md` only when that yaml or its field is
missing, or no session folder exists — so the session that opens a sprint files its pages
under the new sprint, though `guppi sprint` rewrites `sprint.md` later in the run (case 770).
A moved page gets the History line
`archived · cleanup`, a page moved back `restored · cleanup`, and a live page whose list lost
a slug `child <slug> archived · cleanup` or `estimate <slug> archived · cleanup`; `log.md` gets
each line with the page's path. `[[slug]]` links in page bodies stay because Obsidian resolves
a name in any folder and lint counts archived slugs as known. A rerun moves nothing and exits
0. A file that cannot be moved, or a name already taken in the archive, is reported on stderr
with exit 1, and the other pages still move (case 632.1).
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root
from guppi.generate import HISTORY, as_list, write_page
from guppi.materialize import CATEGORIES, session_of_run, sprint_id, unit_sprint
from guppi.pages import Page, read_page, wiki_root

LISTS = ("children", "estimates")


def archive_root(project_dir: Path) -> Path:
    return project_dir / "vault" / "archive"


def live_pages(wiki: Path) -> list[Page]:
    pages = []
    for category in CATEGORIES:
        folder = wiki / category
        if folder.is_dir():
            pages += [
                read_page(p, category) for p in sorted(folder.glob("*.md")) if p.stem != "schema"
            ]
    return [p for p in pages if not p.error]


def archived_pages(root: Path) -> list[Page]:
    if not root.is_dir():
        return []
    pages = []
    for path in sorted(root.rglob("*.md")):
        category = path.parent.name
        if category in CATEGORIES:
            pages.append(read_page(path, category))
    return [p for p in pages if not p.error]


class Cleanup:
    def __init__(self, project_dir: Path, date: str, sprint: str, stdout, stderr):
        self.project_dir = project_dir
        self.wiki = wiki_root(project_dir)
        self.date = date
        self.sprint = sprint
        self.stdout = stdout
        self.stderr = stderr
        self.errors: list[str] = []
        self.log_lines: list[str] = []
        self.moved = 0

    def history(self, page: Page, what: str) -> None:
        line = f"- {self.date} {what} · cleanup"
        current = page.sections.get(HISTORY, "").strip("\n")
        page.sections[HISTORY] = (current + "\n" + line).strip("\n")
        self.log_lines.append(f"- {self.date} {page.category}/{page.slug} {what} · cleanup")

    def move(self, page: Page, target: Path, what: str) -> bool:
        if target.exists():
            self.errors.append(
                f"cleanup: {page.slug}: {target.relative_to(self.project_dir).as_posix()} exists already"
            )
            return False
        self.history(page, what)
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            write_page(target, page.props, page.sections, page.category)
            page.path.unlink()
        except OSError as exc:
            self.errors.append(f"cleanup: {page.slug}: cannot move: {exc}")
            return False
        self.moved += 1
        return True

    def archive(self) -> set[str]:
        gone: set[str] = set()
        for page in live_pages(self.wiki):
            if str(page.props.get("status")) != "archived":
                continue
            target = self.session_root() / page.category / page.path.name
            if self.move(page, target, "archived"):
                gone.add(page.slug)
        return gone

    def session_root(self) -> Path:
        """`vault/archive/<sprint>/<date>/<HHMM>/` of the run's session, or
        `vault/archive/<sprint>/<date>/` when no session folder exists (case 102.2)."""
        root = archive_root(self.project_dir) / self.sprint / self.date
        session = session_of_run(self.project_dir, self.date)
        return root if session is None else root / session[1]

    def restore(self) -> None:
        for page in archived_pages(archive_root(self.project_dir)):
            if str(page.props.get("status")) == "archived":
                continue
            self.move(page, self.wiki / page.category / page.path.name, "restored")

    def unlink(self, gone: set[str]) -> None:
        if not gone:
            return
        for page in live_pages(self.wiki):
            changed = False
            for field in LISTS:
                if page.category == "insights" and field == "children":
                    continue
                if field == "estimates" and page.category not in ("entities", "rules"):
                    continue
                current = as_list(page.props.get(field))
                kept = [s for s in current if s not in gone]
                if kept != current:
                    page.props[field] = kept  # the field only; no section rebuilt (166.4)
                    for slug in current:
                        if slug in gone:
                            self.history(
                                page,
                                f"{ {'children': 'child', 'estimates': 'estimate'}[field] } {slug} archived",
                            )
                    changed = True
            if changed:
                write_page(page.path, page.props, page.sections, page.category)

    def flag_dangling(self) -> None:
        archived = {p.slug for p in archived_pages(archive_root(self.project_dir))}
        for page in live_pages(self.wiki):
            for field in ("parent", "target"):
                slug = page.props.get(field)
                if slug and str(slug) in archived:
                    print(
                        f"cleanup: {page.category}/{page.slug}: {field} {slug} is archived; the page stays, decide it",
                        file=self.stderr,
                    )

    def write_log(self) -> None:
        if not self.log_lines:
            return
        path = self.wiki / "log.md"
        text = path.read_text(encoding="utf-8") if path.exists() else "# Log\n"
        path.write_text(
            text.rstrip("\n") + "\n" + "\n".join(self.log_lines) + "\n",
            encoding="utf-8",
            newline="\n",
        )


def parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(prog="guppi cleanup", description=__doc__.split("\n\n")[1])


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
    sprint = (
        sprint_id(project_dir) if session is None else unit_sprint(project_dir, "/".join(session))
    )
    job = Cleanup(project_dir, today, sprint, stdout, stderr)
    try:
        gone = job.archive()
        job.restore()
        job.unlink(gone)
        job.flag_dangling()
        job.write_log()
    except Exception as exc:  # noqa: BLE001 — report, never traceback
        job.errors.append(f"cleanup: stopped: {exc}")
    for line in job.errors:
        print(line, file=stderr)
    print(f"cleanup: {job.moved} page(s) moved", file=stdout)
    return 1 if job.errors else 0
