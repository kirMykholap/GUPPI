"""`guppi generate [--date YYYY-MM-DD]` — the vault written from `materialize.yaml`.

The only writer to `vault/wiki/`. Applies the entries of `vault/raw/<date>/materialize.yaml`
in order: a `create` becomes a page with the ratified fields and the derived ones, a
`ref` lands as a backlink on the parent, an `update` edits fields and sections, an
`estimate` fills status and Result, a `lesson` brings its paired Estimate, one Decision
page per Case records the routing. What an entry lacks is not written; lint names it.
Every applied entry is marked in the yaml, so a rerun writes nothing; an entry that fails,
whatever the cause, is marked `failed` and the rest apply. `log.md` is appended after each
entry; History and log lines carry the run's date, `created` the yaml's. A `delete` of a
slug with no category is a thing outside the vault: noted, nothing to archive. A slug
collision is an error, never a rename. Without `--date` the script walks every `vault/raw/<date>/` that
holds a yaml, in date order; a failure on one date is reported and the walk goes on, with
exit 1 at the end. Rule page: `vault/wiki/rules/rule-page-generation.md`.
"""

import argparse
import json
import re
import sys
from datetime import date as date_type
from datetime import datetime
from pathlib import Path

from guppi.event import project_root
from guppi.materialize import CATEGORIES, dates_with, dump_yaml, load_yaml, sprint_id, yaml_path
from guppi.pages import Page, read_page, wiki_root

KEY_ORDER = {
    "rules": [
        "type", "kind", "purpose", "status", "enforcement", "implementation_ref", "governs",
        "render_mode", "parent", "children", "estimates", "origin", "sprint", "created", "tags",
    ],
    "entities": [
        "type", "kind", "purpose", "status", "parent", "children", "estimates", "code_ref",
        "origin", "sprint", "created", "tags",
    ],
    "estimates": ["type", "kind", "status", "target", "origin", "sprint", "created", "tags"],
    "lessons": [
        "type", "kind", "root_cause", "status", "source", "estimates", "insight", "origin",
        "sprint", "created", "tags",
    ],
    "insights": [
        "type", "pattern", "status", "children", "severity", "addressed_by", "origin", "sprint",
        "created", "tags",
    ],
    "decisions": [
        "type", "case", "status", "targets", "supersedes", "superseded_by", "origin", "sprint",
        "created", "tags",
    ],
}  # fmt: skip
SECTION_ORDER = {
    "rules": [
        "Purpose",
        "Render",
        "How it works",
        "Estimates",
        "Children",
        "Parent",
        "Implementation",
    ],
    "entities": ["Purpose", "How it works", "Estimates", "Children", "Parent", "Code"],
    "estimates": ["Context", "Criterion", "Method", "Result"],
    "lessons": ["Trigger", "Root cause", "Estimates", "Insight"],
    "insights": ["Pattern", "Proposal", "Children", "Addressed by"],
    "decisions": ["Context", "Now", "Problem", "Then", "Note"],
}
INITIAL_STATUS = {
    "entities": "draft",
    "rules": "draft",
    "estimates": "pending",
    "lessons": "new",
    "insights": "open",
    "decisions": "current",
}
SINGULAR = {
    "entities": "entity",
    "rules": "rule",
    "estimates": "estimate",
    "lessons": "lesson",
    "insights": "insight",
    "decisions": "decision",
}
HISTORY = "## History"
NEEDS_QUOTE = re.compile(r"""^[\s\[\]{}"'&*!|>%@,#`-]|: | #|:$|\s$|\n""")
LOOKS_SPECIAL = re.compile(r"^(true|false|null|yes|no|on|off|~|[-+]?\d[\d.]*)$", re.IGNORECASE)
TAG_ROW = re.compile(r"^\|\s*([\w-]+)\s*\|")
ERROR_ESTIMATE = {
    "kind": "QA",
    "status": "passed",
    "Criterion": "The failure named in Trigger was observed directly.",
    "Method": "The observation itself, by hand; recorded in the ledger line.",
    "Result": "Observed. The ledger line is the record.",
}
KNOWLEDGE_ESTIMATE = {
    "kind": "Research",
    "status": "pending",
    "Criterion": "The claim in Root cause holds when read live.",
    "Method": "One live reading by hand, recorded in the estimate line.",
}


class GenerateError(Exception):
    pass


# --- writing pages ------------------------------------------------------------------


def scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float):
        return str(value)
    if isinstance(value, date_type):
        return value.isoformat()
    text = str(value)
    if text and not NEEDS_QUOTE.search(text) and not LOOKS_SPECIAL.match(text):
        return text
    return json.dumps(text, ensure_ascii=False)


def flow(value) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(flow(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ", ".join(f"{k}: {flow(v)}" for k, v in value.items()) + "}"
    return scalar(value)


def frontmatter(props: dict, category: str) -> str:
    order = KEY_ORDER.get(category, [])
    keys = [k for k in order if k in props] + [k for k in props if k not in order]
    lines = ["---"]
    for key in keys:
        value = props[key]
        if value is None:
            continue
        if isinstance(value, list) and value and all(isinstance(v, dict) for v in value):
            lines.append(f"{key}:")
            lines.extend(f"  - {flow(v)}" for v in value)
        else:
            lines.append(f"{key}: {flow(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def body(sections: dict[str, str], category: str) -> str:
    order = [f"## {name}" for name in SECTION_ORDER.get(category, [])]
    keys = [k for k in order if k in sections]
    keys += [k for k in sections if k not in order and k != HISTORY]
    if HISTORY in sections:
        keys.append(HISTORY)
    out = []
    for key in keys:
        text = sections[key].strip("\n")
        out.append(f"\n{key}\n\n{text}\n" if text else f"\n{key}\n")
    return "".join(out)


def write_page(path: Path, props: dict, sections: dict[str, str], category: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = frontmatter(props, category) + body(sections, category)
    path.write_text(text, encoding="utf-8", newline="\n")


def links(slugs: list[str], numbered: bool = False) -> str:
    if numbered:
        return "\n".join(f"{i}. [[{s}]]" for i, s in enumerate(slugs, start=1))
    return "\n".join(f"- [[{s}]]" for s in slugs)


def paths_list(paths: list[str]) -> str:
    return "\n".join(f"- `{p}`" for p in paths)


def as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


# --- the vault ----------------------------------------------------------------------


class Vault:
    def __init__(self, project_dir: Path, date: str, sprint: str, now, stdout, stderr):
        self.project_dir = project_dir
        self.wiki = wiki_root(project_dir)
        self.date = date  # the yaml's date: `created`
        self.run_date = now.strftime("%Y-%m-%d")  # History and log lines
        self.sprint = sprint
        self.now = now
        self.stdout = stdout
        self.stderr = stderr
        self.errors: list[str] = []
        self.log_lines: list[str] = []
        self.written: dict[str, str] = {}  # slug → category, pages touched this run
        self.used_tags: set[str] = set()
        self.pending: list[
            tuple[str, str, str, str]
        ] = []  # backlinks whose parent is not there yet

    # pages

    def path(self, category: str, slug: str) -> Path:
        return self.wiki / category / f"{slug}.md"

    def find(self, slug: str) -> Page | None:
        for category in CATEGORIES:
            path = self.path(category, slug)
            if path.exists():
                page = read_page(path, category)
                if page.error:
                    raise GenerateError(f"{slug}: {page.error}")
                return page
        return None

    def save(self, page: Page) -> None:
        write_page(page.path, page.props, page.sections, page.category)

    def history(self, page: Page, what: str, origin: str | None) -> None:
        line = f"- {self.run_date} {what}" + (f" · {origin}" if origin else "")
        current = page.sections.get(HISTORY, "").strip("\n")
        page.sections[HISTORY] = (current + "\n" + line).strip("\n")
        self.log_lines.append(
            f"- {self.run_date} {page.category}/{page.slug} {what}"
            + (f" · {origin}" if origin else "")
            + " · generate"
        )
        self.written[page.slug] = page.category

    def error(self, slug: str, what: str) -> None:
        self.errors.append(f"generate: {slug}: {what}")

    def rebuild_list(self, page: Page, field: str) -> None:
        slugs = as_list(page.props.get(field))
        section = {"children": "## Children", "estimates": "## Estimates"}[field]
        numbered = field == "children" and page.category == "rules"
        page.sections[section] = links(slugs, numbered)

    # create

    def create(self, entry: dict) -> None:
        category, slug = entry["category"], entry["slug"]
        if category not in CATEGORIES:
            self.error(slug, f"category {category!r} is not a vault folder")
            return
        path = self.path(category, slug)
        if entry.get("exists"):
            if entry.get("status"):
                self.estimate(
                    {
                        "slug": slug,
                        "status": entry["status"],
                        "result": entry.get("result", ""),
                        "origin": entry["origin"],
                    }
                )
            return
        if path.exists():
            self.error(slug, "a page with this slug exists; a collision is an error, not a rename")
            return
        fields = dict(entry.get("fields") or {})
        sections_in = dict(entry.get("sections") or {})
        props: dict = {"type": fields.pop("type", SINGULAR[category])}
        for key, value in fields.items():
            if key == "tags":
                continue
            props[key] = value
        props["status"] = INITIAL_STATUS[category]
        ref = entry.get("ref")
        if ref and category in ("rules", "entities"):
            props["parent"] = ref
        if ref and category == "estimates":
            props["target"] = ref
        if category in ("rules", "entities", "lessons"):
            props.setdefault("estimates", [])
        if category in ("rules", "entities") and props.get("kind") == "MOC":
            props.setdefault("children", [])
        if category == "insights":
            props.setdefault("children", [])
            props["severity"] = len(as_list(props.get("children")))
        props["origin"] = entry["origin"]
        props["sprint"] = self.sprint
        props["created"] = self.date
        tags = entry.get("tags") or fields.get("tags")
        if tags:
            props["tags"] = list(tags)
            self.used_tags.update(props["tags"])
        sections: dict[str, str] = {}
        for name, text in sections_in.items():
            sections[f"## {name}"] = str(text).strip("\n")
        if (
            category in ("rules", "entities")
            and "## Purpose" not in sections
            and props.get("purpose")
        ):
            sections["## Purpose"] = str(props["purpose"])
        if category in ("rules", "entities", "lessons"):
            sections["## Estimates"] = links(as_list(props.get("estimates")))
        if "children" in props and category in ("rules", "entities", "insights"):
            sections["## Children"] = links(as_list(props["children"]), category == "rules")
        if props.get("parent"):
            sections["## Parent"] = links([props["parent"]])
        if props.get("implementation_ref"):
            sections["## Implementation"] = paths_list(as_list(props["implementation_ref"]))
        if props.get("code_ref"):
            sections["## Code"] = paths_list(as_list(props["code_ref"]))
        if category == "estimates" and entry.get("status"):
            props["status"] = entry["status"]
            sections["## Result"] = str(entry.get("result") or "")
        page = Page(category=category, slug=slug, path=path, props=props, sections=sections)
        self.history(page, "created", entry["origin"])
        if category == "estimates" and entry.get("status"):
            self.history(page, f"status: pending → {entry['status']}", entry["origin"])
        self.save(page)
        if ref:
            self.backlink(ref, slug, category, entry["origin"])
        if category == "lessons":
            self.lesson_estimate(page, entry)

    def backlink(self, ref: str, slug: str, category: str, origin: str, last: bool = False) -> None:
        parent = self.find(ref)
        if parent is None:
            if last:
                self.error(slug, f"ref {ref} names no page; the backlink is missing")
            else:  # the parent may be created later in this yaml
                self.pending.append((ref, slug, category, origin))
            return
        field = "estimates" if category == "estimates" else "children"
        current = as_list(parent.props.get(field))
        if slug in current:
            return
        parent.props[field] = current + [slug]
        self.rebuild_list(parent, field)
        what = f"estimate {slug} added" if field == "estimates" else f"child {slug} added"
        self.history(parent, what, origin)
        self.save(parent)

    def lesson_estimate(self, lesson: Page, entry: dict) -> None:
        slug = "estimate-" + lesson.slug.removeprefix("lesson-")
        template = ERROR_ESTIMATE if lesson.props.get("kind") == "error" else KNOWLEDGE_ESTIMATE
        path = self.path("estimates", slug)
        if path.exists():
            self.error(slug, "the lesson's paired estimate exists already")
            return
        props = {
            "type": "estimate",
            "kind": template["kind"],
            "status": template["status"],
            "target": lesson.slug,
            "origin": entry["origin"],
            "sprint": self.sprint,
            "created": self.date,
        }
        if lesson.props.get("tags"):
            props["tags"] = list(lesson.props["tags"])
        sections = {
            "## Context": f"The paired Estimate of [[{lesson.slug}]], a `{lesson.props.get('kind')}` lesson.",
            "## Criterion": template["Criterion"],
            "## Method": template["Method"],
        }
        if "Result" in template:
            sections["## Result"] = template["Result"]
        page = Page(category="estimates", slug=slug, path=path, props=props, sections=sections)
        self.history(page, "created", entry["origin"])
        if template["status"] == "passed":
            self.history(page, "status: pending → passed", entry["origin"])
        self.save(page)
        lesson.props["estimates"] = as_list(lesson.props.get("estimates")) + [slug]
        self.rebuild_list(lesson, "estimates")
        self.save(lesson)

    # update

    def update(self, entry: dict) -> None:
        slug = entry["slug"]
        page = self.find(slug)
        if page is None:
            self.error(slug, "no page to update")
            return
        if not any(entry.get(k) for k in ("set", "sections", "replace", "change")):
            print(
                f"generate: {slug}: an update with no content in the Spec; applied by hand",
                file=self.stdout,
            )
            return
        for key, value in (entry.get("set") or {}).items():
            page.props[key] = value
            if key in ("children", "estimates"):
                self.rebuild_list(page, key)
            if key == "tags":
                self.used_tags.update(as_list(value))
        for name, text in (entry.get("sections") or {}).items():
            page.sections[f"## {name}"] = str(text).strip("\n")
        replaces = entry.get("replace") or []
        if not isinstance(replaces, list) or not all(isinstance(i, dict) for i in replaces):
            self.error(slug, "replace: expected a list of old/new pairs")
            return
        for item in replaces:
            if not self.replace(page, str(item.get("old", "")), str(item.get("new", ""))):
                self.error(slug, f"replace: {item.get('old', '')[:60]!r} is absent or not unique")
                return
        change = entry.get("change") or "updated"
        self.history(page, f"updated: {change}", entry.get("origin"))
        self.save(page)

    def replace(self, page: Page, old: str, new: str) -> bool:
        tokens = [re.escape(t) for t in old.split()]
        if not tokens:
            return False
        pattern = re.compile(r"\s+".join(tokens))
        hits = [
            (key, m)
            for key, text in page.sections.items()
            if key != HISTORY
            for m in pattern.finditer(text)
        ]
        if len(hits) != 1:
            return False
        key, match = hits[0]
        text = page.sections[key]
        page.sections[key] = text[: match.start()] + new + text[match.end() :]
        return True

    # estimate

    def estimate(self, entry: dict) -> None:
        slug = entry["slug"]
        page = self.find(slug)
        if page is None or page.category != "estimates":
            self.error(slug, "no estimate page to fill")
            return
        before = str(page.props.get("status"))
        if before == entry["status"] and "## Result" in page.sections:
            print(f"generate: {slug}: already {before} with a Result; skipped", file=self.stdout)
            return
        page.props["status"] = entry["status"]
        page.sections["## Result"] = str(entry.get("result") or "")
        self.history(page, f"status: {before} → {entry['status']}", entry.get("origin"))
        self.save(page)

    # delete, defer

    def delete(self, entry: dict) -> None:
        if entry.get("category") not in CATEGORIES:
            print(
                f"generate: {entry['slug']}: outside the vault, nothing to archive",
                file=self.stdout,
            )
            return
        page = self.find(entry["slug"])
        if page is None:
            self.error(entry["slug"], "no page to delete")
            return
        page.props["status"] = "archived"
        self.history(page, "deleted", entry.get("origin"))
        self.save(page)

    def defer(self, entry: dict) -> None:
        slug, category = entry["slug"], entry["category"]
        page = self.find(slug)
        if page is not None:
            self.history(page, "deferred", entry.get("origin"))
            self.save(page)
            return
        if category not in CATEGORIES:
            self.error(slug, f"category {category!r} is not a vault folder")
            return
        fields = dict(entry.get("fields") or {})
        props = {"type": fields.pop("type", SINGULAR[category]), "status": "draft"}
        tags = fields.pop("tags", None) or entry.get("tags")
        props.update(fields)
        props["origin"] = entry["origin"]
        props["sprint"] = self.sprint
        props["created"] = self.date
        if tags:
            props["tags"] = list(tags)
        sections = {}
        if props.get("purpose"):
            sections["## Purpose"] = str(props["purpose"])
        page = Page(
            category=category,
            slug=slug,
            path=self.path(category, slug),
            props=props,
            sections=sections,
        )
        self.history(page, "deferred, placeholder", entry["origin"])
        self.save(page)

    def settle_backlinks(self) -> None:
        pending, self.pending = self.pending, []
        for ref, slug, category, origin in pending:
            self.backlink(ref, slug, category, origin, last=True)

    # decisions

    def decision(self, record: dict) -> None:
        slug = record["decision"]
        path = self.path("decisions", slug)
        if path.exists():
            return
        text = record.get("case_text") or {}
        tags = list(record.get("tags") or [])
        for target in record.get("targets") or []:
            if target.get("category") in CATEGORIES:
                page = self.find(str(target.get("slug")))
                for tag in as_list(page.props.get("tags")) if page else []:
                    if tag not in tags:
                        tags.append(tag)
        props: dict = {
            "type": "decision",
            "case": str(record["case"]),
            "status": "current",
            "targets": record.get("targets") or [],
        }
        if record.get("supersedes"):
            props["supersedes"] = list(record["supersedes"])
        props["origin"] = record["origin"]
        props["sprint"] = self.sprint
        props["created"] = self.date
        props["tags"] = tags  # the union of the targets' tags; empty is a fact, not a gap
        sections = {}
        for name, key in (("Context", "context"), ("Now", "given"), ("Problem", "problem")):
            if text.get(key):
                sections[f"## {name}"] = text[key]
        then = "\n\n".join(t for t in (text.get("when"), text.get("then")) if t)
        if then:
            sections["## Then"] = then
        page = Page(category="decisions", slug=slug, path=path, props=props, sections=sections)
        self.history(page, "created", record["origin"])
        self.save(page)
        for earlier in record.get("supersedes") or []:
            other = self.find(earlier)
            if other is None:
                continue
            other.props["status"] = "superseded"
            done = as_list(other.props.get("superseded_by"))
            if slug not in done:
                other.props["superseded_by"] = done + [slug]
            self.history(other, f"superseded by {slug}", record["origin"])
            self.save(other)

    # after all entries

    def cascade(self) -> None:
        estimates: dict[str, Page] = {}
        for path in (self.wiki / "estimates").glob("*.md"):
            if path.stem != "schema":
                estimates[path.stem] = read_page(path, "estimates")
        for category in ("entities", "rules"):
            for path in sorted((self.wiki / category).glob("*.md")):
                if path.stem == "schema":
                    continue
                page = read_page(path, category)
                if page.error or str(page.props.get("status")) not in ("draft", "built"):
                    continue
                own = [estimates.get(s) for s in as_list(page.props.get("estimates"))]
                own = [e for e in own if e is not None]
                if not own:
                    continue
                all_passed = all(str(e.props.get("status")) == "passed" for e in own)
                before = str(page.props["status"])
                after = "built" if all_passed else "draft"
                if before != after:
                    page.props["status"] = after
                    self.history(page, f"status: {before} → {after}", "cascade")
                    self.save(page)
        lessons = {}
        for path in (self.wiki / "lessons").glob("*.md"):
            if path.stem != "schema":
                lessons[path.stem] = read_page(path, "lessons")
        for path in sorted((self.wiki / "insights").glob("*.md")):
            if path.stem == "schema":
                continue
            page = read_page(path, "insights")
            if page.error:
                continue
            live = [
                s
                for s in as_list(page.props.get("children"))
                if str(lessons.get(s, Page("lessons", s, path)).props.get("status")) != "archived"
            ]
            if page.props.get("severity") != len(live):
                page.props["severity"] = len(live)
                self.save(page)

    def register_tags(self, new_tags: list[dict]) -> None:
        path = self.wiki / "tags.md"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        known = {m.group(1) for m in map(TAG_ROW.match, text.splitlines()) if m}
        known.discard("tag")
        rows = []
        for item in new_tags or []:
            tag = str(item.get("tag", "")).strip()
            if tag and tag not in known:
                rows.append(f"| {tag} | {item.get('meaning', '')} | {item.get('aliases', '')} |")
                known.add(tag)
        if rows:
            text = text.rstrip("\n") + "\n" + "\n".join(rows) + "\n"
            path.write_text(text, encoding="utf-8", newline="\n")
            self.log_lines.append(
                f"- {self.run_date} tags.md registers {', '.join(r.split('|')[1].strip() for r in rows)} · generate"
            )
        for tag in sorted(self.used_tags - known):
            print(f"generate: tag {tag} is used but not registered in tags.md", file=self.stderr)

    def write_log(self) -> None:
        """Append the lines gathered so far and clear them: called after every entry, so a
        run that stops leaves the feed level with the pages."""
        if not self.log_lines:
            return
        path = self.wiki / "log.md"
        text = path.read_text(encoding="utf-8") if path.exists() else "# Log\n"
        text = text.rstrip("\n") + "\n" + "\n".join(self.log_lines) + "\n"
        path.write_text(text, encoding="utf-8", newline="\n")
        self.log_lines = []


# --- the run ------------------------------------------------------------------------


def apply(vault: Vault, data: dict) -> None:
    stamp = vault.now.strftime("%H:%M:%S")
    for entry in data.get("entries") or []:
        if entry.get("applied"):
            continue
        kind = entry.get("kind")
        if entry.get("category") == "file":
            print(
                f"generate: {entry['slug']}: a Rule-class file, applied by hand", file=vault.stdout
            )
            entry["applied"] = stamp
            continue
        before = len(vault.errors)
        try:
            if kind == "create" or kind == "lesson":
                vault.create(entry)
            elif kind == "update":
                vault.update(entry)
            elif kind == "estimate":
                vault.estimate(entry)
            elif kind == "delete":
                vault.delete(entry)
            elif kind == "defer":
                vault.defer(entry)
            else:
                vault.error(entry.get("slug", "?"), f"unknown kind {kind!r}")
        except Exception as exc:  # noqa: BLE001 — one entry fails alone, the run goes on
            vault.error(entry.get("slug", "?"), f"{type(exc).__name__}: {exc}")
        if len(vault.errors) == before:
            entry["applied"] = stamp
        else:
            entry["failed"] = vault.errors[-1]
        vault.write_log()
    vault.settle_backlinks()
    vault.write_log()
    for record in data.get("decisions") or []:
        if record.get("applied"):
            continue
        before = len(vault.errors)
        try:
            vault.decision(record)
        except Exception as exc:  # noqa: BLE001
            vault.error(record.get("decision", "?"), f"{type(exc).__name__}: {exc}")
        if len(vault.errors) == before:
            record["applied"] = stamp
        vault.write_log()
    vault.cascade()
    vault.register_tags(data.get("new_tags") or [])
    vault.write_log()


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi generate", description=__doc__.split("\n\n")[1])
    p.add_argument("--date", default=None, help="one raw/<date> folder; without it, every date")
    return p


def generate_date(project_dir: Path, date: str, now, stdout, stderr) -> int:
    """One date: apply the unapplied entries of its yaml; exit 1 when an entry failed."""
    path = yaml_path(project_dir, date)
    data = load_yaml(path)
    if data is None:
        print(
            f"generate: {path.relative_to(project_dir).as_posix()} does not exist; run materialize first",
            file=stderr,
        )
        return 1
    vault = Vault(
        project_dir, date, str(data.get("sprint") or sprint_id(project_dir)), now, stdout, stderr
    )
    try:
        apply(vault, data)
    except GenerateError as exc:
        vault.errors.append(f"generate: {exc}")
    except Exception as exc:  # noqa: BLE001 — report, never traceback; the yaml marks are still written
        vault.errors.append(f"generate: stopped: {exc}")
    finally:
        dump_yaml(path, data)
    for line in vault.errors:
        print(line, file=stderr)
    touched = len(vault.written)
    print(f"generate: {date}: {touched} page(s) written or changed", file=stdout)
    return 1 if vault.errors else 0


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    dates = [args.date] if args.date else dates_with(project_dir, "materialize.yaml")
    if not dates:
        print(
            "generate: no vault/raw/<date>/materialize.yaml to apply; run materialize first",
            file=stderr,
        )
        return 1
    failed = False
    for date in dates:
        failed = generate_date(project_dir, date, now, stdout, stderr) != 0 or failed
    return 1 if failed else 0
