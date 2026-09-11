"""`guppi cleanup` — archived pages leave the live vault, restored ones come back.

Every live page under `vault/wiki/<category>/` with `status: archived` moves to
`vault/archived/<sprint>/<date>/<category>/<slug>.md`, with a History line and a `log.md`
line; its slug leaves the `children` lists of live pages and the `estimates` lists of
entities and rules (an Insight's `children` keep it, since `severity` counts the live
ones; a lesson has no Estimates, case 53.1); `[[slug]]` links in page bodies stay. A page
under `vault/archived/` whose status is no longer `archived` moves back. A live page whose
`parent` or `target` is in the archive is reported, not moved. Then the four indexes are
rewritten; an archived Estimate leaves no line, since estimates have none (case 57).
`raw/` stays where it is. Rule page: `vault/wiki/rules/rule-cleanup.md`.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root
from guppi.generate import HISTORY, as_list, write_page
from guppi.index import plan as index_plan
from guppi.materialize import CATEGORIES, sprint_id
from guppi.pages import Page, read_page, wiki_root

LISTS = ("children", "estimates")


def archive_root(project_dir: Path) -> Path:
    return project_dir / "vault" / "archived"


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
            target = (
                archive_root(self.project_dir)
                / self.sprint
                / self.date
                / page.category
                / page.path.name
            )
            if self.move(page, target, "archived"):
                gone.add(page.slug)
        return gone

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
                    page.props[field] = kept
                    section = "## Children" if field == "children" else "## Estimates"
                    numbered = field == "children" and page.category == "rules"
                    page.sections[section] = "\n".join(
                        (f"{i}. [[{s}]]" if numbered else f"- [[{s}]]")
                        for i, s in enumerate(kept, start=1)
                    )
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

    def rewrite_indexes(self) -> None:
        for path, text in index_plan(self.wiki).items():
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                path.write_text(text, encoding="utf-8", newline="\n")

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
    job = Cleanup(project_dir, now.date().isoformat(), sprint_id(project_dir), stdout, stderr)
    try:
        gone = job.archive()
        job.restore()
        job.unlink(gone)
        job.flag_dangling()
        job.rewrite_indexes()
        job.write_log()
    except Exception as exc:  # noqa: BLE001 — report, never traceback
        job.errors.append(f"cleanup: stopped: {exc}")
    for line in job.errors:
        print(line, file=stderr)
    print(f"cleanup: {job.moved} page(s) moved", file=stdout)
    return 1 if job.errors else 0
