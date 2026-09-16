"""`guppi generate [--date YYYY-MM-DD]` — the vault written from `materialize.yaml`.

The only writer to `vault/wiki/`. Applies the entries of a `materialize.yaml` in order and
writes nothing an entry does not carry: no section is derived from a ref field, no Estimate
from a flag (cases 166.2, 194.1, 201). Rule page: `vault/wiki/rules/rule-page-generation.md`.

One entry, one page (case 201.1). A `create` becomes a page: `type`, the entry's `fields`,
`status` by category (`INITIAL_STATUS`), `origin`, `sprint` (the first `## <id>` heading of
`sprint.md`), `created` (the yaml's date), `tags`; the body from `sections`, `## Purpose`
from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the
target's `estimates`, History `child <slug> added` / `estimate <slug> added`, settled at
the end of the run when the parent comes later in the yaml. An Estimate page carries
`purpose`, `method` and `checked` as fields after `target`, its `## Criterion` from
`sections`; `## Context` and `## Method` are the shape before case 193, never written to a
new page and dropped by the `update` whose `set` carries `method` — the field replaces the
section (case 211.1); an `update` with `sections.Criterion` on a page without a `method`
field, and no `set.method`, fails alone as `a recut without method` (case 211.2). A
`create` whose slug is a placeholder —
`status: draft`, no `kind` — fills it, `created` and `deferred_by` kept, History `created
over placeholder` (case 101.1); any other existing page is a collision, never a rename. An
`update` applies `set` to the frontmatter, `sections` as whole replacements — an Estimate's
Criterion is replaced whole this way (case 194.1) — `replace` inside the body (whitespace
collapsed, exactly one occurrence), History `updated: <change>`; an update with none of
those prints `applied by hand`. An `update`, `estimate`, `delete` or `defer` whose slug is
not under `wiki/` reaches the page under `vault/archive/`, `raw/` folders excluded, and
edits it there (case 105.3). An `estimate` sets `status`, overwrites `## Result`, writes
`checked` — the date the result opens with (case 199), else the yaml's date — and appends
History `status: a → b` with the ledger pointer (case 53.2). A `delete` sets `archived`,
History `deleted`; a `delete` of a slug with no category is a thing outside the vault:
printed, applied, nothing to archive. A `defer` with a page appends the decision slug to
its `deferred_by` — a rule, an entity or an Insight (case 124.2) — History `deferred`;
without a page it writes a placeholder, `status: draft`, with the fields the Case gave. A
`lesson` writes the lesson alone, `source` when the line carries it (case 53.1). Every ref
field (`REF_FIELDS`) is written as a quoted wikilink, `"[[slug]]"`; a slug without a
category prefix stays bare; readers strip the brackets (case 172). A `create` in
`insights` applies only when marked `librarian` at synthesis; a `delete` of an Insight is
refused always (case 171). History and `log.md` lines carry the run's date and end with
`[[decision-case-N]]` when the entry belongs to a Case, else the ledger pointer (case
52.4); `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a
used and undeclared one goes to stderr. `criterion_block` on an update and the kind
`remove_criterion` — the shape before case 189 — are not applied: they fail as any shape
the script does not know.

The Decision page (case 201.2): one per Case, `decisions/decision-case-<N>.md`, written
before the first entry of its lines so their History lines can name it; `case`, `status:
current`, one list per kind present — `create`, `update`, `delete`, `defer`, the slugs in
ledger order (case 59.4) — `source`, `supersedes`, `origin`, `sprint`, `created`, `tags`
(the union of the targets' tags); the body `## Context` and `## Problem` from `case_text`
and `## Deferred`, one `### [[slug]]` heading per target of the Case's `defer` lines with
its `purpose` verbatim (case 186.1); no `## Given`, no `## When`, no `## Criterion` list —
the contract lives on the Estimate; pages written before keep theirs. A `supersedes` sets
the earlier page `superseded`, appends to its `superseded_by` and removes its slug from
the `deferred_by` of every target of its `defer` list. An existing page is skipped; a
`create` marked `exists` writes no page, its Decision page is still written.

One bad entry never stops the run (case 201.3): an entry that fails — a collision, a `ref`
naming no page, a `replace` absent or not unique, an unexpected shape, an unknown kind,
any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` and
skipped; the rest apply; exit 1. Every applied entry is marked `applied: <time>`, a stale
`failed` mark is dropped on apply (case 53.3), so a rerun writes nothing. An entry with
`failed` and no `kind` — a line `materialize` could not lift — is skipped with its mark
kept and one stderr line (case 142.2); an entry with `superseded_by` is not applied and
leaves no line, only its Case's Decision page is written (case 151); a Rule-class file
entry is printed `applied by hand` and marked applied.

The cascade after all entries (case 201.4): an entity or rule whose Estimates are all
`passed` becomes `built`, a `built` one with an Estimate not passed returns to `draft`,
History `· cascade`; a `superseded` Decision page becomes `archived` (case 104.1); the
`clustered` children of an `actioned` Insight become `archived` (case 104.2); every
Insight's `severity` is recounted, a child's status read under `wiki/lessons/` or in the
archive, a child with no page counted live (case 110); an `open` Insight at 0 becomes
`archived`, an `actioned` one stays (case 104.3). No section is derived by the cascade.

The walk (case 201.5): without `--date` every unit under `vault/raw/` with a yaml is
applied — the date-level yaml of a date first, then `raw/<date>/<HHMM>/materialize.yaml`
in folder order, dates ascending (case 103.3); `--date` walks the units of that date; a
unit with nothing unapplied changes no page; a failure on one unit is reported and the
walk goes on, with exit 1 at the end.
"""

import argparse
import json
import re
import sys
from datetime import date as date_type
from datetime import datetime
from pathlib import Path

from guppi.event import project_root
from guppi.materialize import (
    CATEGORIES,
    PREFIXES,
    dump_yaml,
    load_yaml,
    sprint_id,
    units_with,
    yaml_path,
)
from guppi.pages import REF_FIELDS, Page, read_page, slug_of, wiki_root

KEY_ORDER = {
    "rules": [
        "type", "kind", "purpose", "status", "enforcement", "implementation_ref", "governs",
        "render_mode", "parent", "children", "estimates", "deferred_by", "origin", "sprint",
        "created", "tags",
    ],
    "entities": [
        "type", "kind", "purpose", "status", "parent", "children", "estimates", "deferred_by",
        "code_ref", "origin", "sprint", "created", "tags",
    ],
    "estimates": [
        "type", "kind", "status", "target", "purpose", "method", "checked", "origin", "sprint",
        "created", "tags",
    ],
    "lessons": [
        "type", "kind", "root_cause", "status", "source", "insight", "origin", "sprint",
        "created", "tags",
    ],
    "insights": [
        "type", "pattern", "status", "children", "severity", "addressed_by", "deferred_by",
        "origin", "sprint", "created", "tags",
    ],
    "decisions": [
        "type", "case", "status", "create", "update", "delete", "defer", "source", "supersedes",
        "superseded_by", "origin", "sprint", "created", "tags",
    ],
}  # fmt: skip
KINDS = ("create", "update", "delete", "defer")  # a decision page's lists, in this order
SECTION_ORDER = {  # no section derived from a ref field (case 166.2)
    "rules": ["Purpose", "Render", "How it works"],
    "entities": ["Purpose", "How it works"],
    "estimates": ["Context", "Criterion", "Method", "Result"],
    "lessons": ["Trigger", "Root cause"],
    "insights": ["Pattern", "Proposal"],
    # Given, When and Criterion: the shapes before 72.4 and 201.2, kept where a page carries them
    "decisions": ["Context", "Problem", "Given", "When", "Criterion", "Deferred", "Note"],
}
DEFERRABLE = ("rules", "entities", "insights")  # the categories a `defer` marks (124.2)
LIBRARIAN_ONLY = "an Insight is made and retired by the librarian, never created or deleted by a decision (case 171)"
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
READING_DATE = re.compile(r"^\s*(\d{4}-\d\d-\d\d)\b")  # a Result opens with its date (case 199)


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


def wikilink(value):
    """A slug with a category prefix as `[[slug]]`; a Rule-class slug, or anything else,
    as it is (case 148.1). `scalar` quotes the brackets."""
    if isinstance(value, str):
        slug = slug_of(value)
        if any(slug.startswith(prefix) for prefix in PREFIXES):
            return f"[[{slug}]]"
    return value


def frontmatter(props: dict, category: str) -> str:
    order = KEY_ORDER.get(category, [])
    keys = [k for k in order if k in props] + [k for k in props if k not in order]
    lines = ["---"]
    for key in keys:
        value = props[key]
        if value is None:
            continue
        if key in REF_FIELDS:  # ref fields are written as quoted wikilinks (case 148.1)
            value = [wikilink(v) for v in value] if isinstance(value, list) else wikilink(value)
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


def as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


# --- the vault ----------------------------------------------------------------------


def archived_paths(project_dir: Path, slug: str) -> list[Path]:
    """`<slug>.md` under `vault/archive/`, at any depth, in a category folder and not
    under a `raw/` folder (cases 102.2, 105.3)."""
    archive = project_dir / "vault" / "archive"
    if not archive.is_dir():
        return []
    return sorted(
        p
        for p in archive.rglob(f"{slug}.md")
        if p.parent.name in CATEGORIES and "raw" not in p.relative_to(archive).parts[:-1]
    )


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
        """The live page of a slug, or the archived one under `vault/archive/` (`raw/`
        folders excluded), so an `update` reaches a page in the archive and a `status`
        other than `archived` brings it back through `cleanup` (case 105.3)."""
        for category in CATEGORIES:
            path = self.path(category, slug)
            if path.exists():
                page = read_page(path, category)
                if page.error:
                    raise GenerateError(f"{slug}: {page.error}")
                return page
        for path in archived_paths(self.project_dir, slug):
            page = read_page(path, path.parent.name)
            if page.error:
                raise GenerateError(f"{slug}: {page.error}")
            return page
        return None

    def save(self, page: Page) -> None:
        write_page(page.path, page.props, page.sections, page.category)

    @staticmethod
    def pointer(entry: dict) -> str | None:
        """What a History line points at: the Decision page of the entry's Case as a
        wikilink, or the ledger line of a reading or a lesson (case 52.4)."""
        if entry.get("decision"):
            return f"[[{entry['decision']}]]"
        return entry.get("origin")

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

    # create

    def create(self, entry: dict) -> None:
        category, slug = entry["category"], entry["slug"]
        if category not in CATEGORIES:
            self.error(slug, f"category {category!r} is not a vault folder")
            return
        if category == "insights" and not entry.get("librarian"):  # 171: a decision's, refused
            self.error(slug, LIBRARIAN_ONLY)
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
        placeholder = None
        if path.exists():
            found = read_page(path, category)
            if (
                not found.error
                and found.props.get("kind") is None
                and str(found.props.get("status")) == "draft"
            ):
                placeholder = found  # born of a defer without a ref (case 101.1)
            else:
                self.error(
                    slug, "a page with this slug exists; a collision is an error, not a rename"
                )
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
        if category in ("rules", "entities"):
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
        if category == "estimates" and entry.get("status"):
            props["status"] = entry["status"]
            sections["## Result"] = str(entry.get("result") or "")
        page = Page(category=category, slug=slug, path=path, props=props, sections=sections)
        if placeholder is not None:
            props["created"] = placeholder.props.get("created", self.date)
            if placeholder.props.get("deferred_by") is not None:
                props["deferred_by"] = as_list(placeholder.props.get("deferred_by"))
            page.sections[HISTORY] = placeholder.sections.get(HISTORY, "")
            self.history(page, "created over placeholder", self.pointer(entry))
        else:
            self.history(page, "created", self.pointer(entry))
        if category == "estimates" and entry.get("status"):
            folded = as_list(entry.get("folded"))
            origin = str(entry["origin"])
            unit = (
                origin.split("raw/", 1)[1].split("/ledger.md", 1)[0]
                if "raw/" in origin
                else self.date
            )
            reading = f"raw/{unit}/ledger.md#L{folded[0]}" if folded else self.pointer(entry)
            self.history(page, f"status: pending → {entry['status']}", reading)
        self.save(page)
        if ref:
            self.backlink(ref, slug, category, self.pointer(entry) or entry["origin"])

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
        what = f"estimate {slug} added" if field == "estimates" else f"child {slug} added"
        self.history(parent, what, origin)
        self.save(parent)

    # update

    def update(self, entry: dict) -> None:
        slug = entry["slug"]
        page = self.find(slug)
        if page is None:
            self.error(slug, "no page to update")
            return
        if entry.get("criterion_block"):  # the shape before case 189: not applied (201.1)
            self.error(slug, "criterion_block: a shape the script no longer knows (case 201.1)")
            return
        keys = ("set", "sections", "replace", "change")
        if not any(entry.get(k) for k in keys):
            print(
                f"generate: {slug}: an update with no content in the Spec; applied by hand",
                file=self.stdout,
            )
            return
        sets = entry.get("set") or {}
        sections = entry.get("sections") or {}
        if (
            page.category == "estimates"
            and "Criterion" in sections
            and "method" not in page.props
            and "method" not in sets
        ):  # a recut that would leave the page in the old shape (case 211.2)
            self.error(slug, "a recut without method (case 211)")
            return
        for key, value in sets.items():
            page.props[key] = value
            if key == "tags":
                self.used_tags.update(as_list(value))
        if page.category == "estimates" and "method" in sets:
            # the field replaces the section; the Case is reached by origin (case 211.1)
            page.sections.pop("## Context", None)
            page.sections.pop("## Method", None)
        for name, text in sections.items():
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
        self.history(page, f"updated: {change}", self.pointer(entry))
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
        before = str(page.props.get("status"))  # a reading always lands (case 53.2)
        page.props["status"] = entry["status"]
        result = str(entry.get("result") or "")
        page.sections["## Result"] = result
        match = READING_DATE.match(result)  # the date the Result opens with (cases 199, 201.1)
        page.props["checked"] = date_type.fromisoformat(match.group(1) if match else self.date)
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
        if page is not None and page.category == "insights":
            self.error(entry["slug"], LIBRARIAN_ONLY)
            return
        if page is None:
            self.error(entry["slug"], "no page to delete")
            return
        page.props["status"] = "archived"
        self.history(page, "deleted", self.pointer(entry))
        self.save(page)

    def defer(self, entry: dict) -> None:
        """A `defer` marks its target `deferred_by` — a Rule, an Entity or an Insight (case
        124.2) — or writes a placeholder page when the target does not exist."""
        slug, category = entry["slug"], entry["category"]
        page = self.find(slug)
        decision = entry.get("decision")
        if page is not None:
            if decision and page.category in DEFERRABLE:
                current = as_list(page.props.get("deferred_by"))
                if decision not in current:
                    page.props["deferred_by"] = current + [decision]
            self.history(page, "deferred", self.pointer(entry))
            self.save(page)
            return
        if category not in CATEGORIES:
            self.error(slug, f"category {category!r} is not a vault folder")
            return
        fields = dict(entry.get("fields") or {})
        props = {"type": fields.pop("type", SINGULAR[category]), "status": "draft"}
        tags = fields.pop("tags", None) or entry.get("tags")
        props.update(fields)
        if decision and category in DEFERRABLE:
            props["deferred_by"] = [decision]
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
        self.history(page, "deferred, placeholder", self.pointer(entry))
        self.save(page)

    def clear_deferred_by(self, earlier: Page, by: str, origin: str) -> None:
        """A `supersedes` of a decision that deferred pages: every target in the earlier
        page's `defer` list drops it from `deferred_by`, an empty list is dropped (cases
        52.3, 59.4)."""
        for slug in as_list(earlier.props.get("defer")):
            page = self.find(slug)
            if page is None or earlier.slug not in as_list(page.props.get("deferred_by")):
                continue
            kept = [d for d in as_list(page.props["deferred_by"]) if d != earlier.slug]
            if kept:
                page.props["deferred_by"] = kept
            else:
                del page.props["deferred_by"]
            self.history(page, f"defer by {earlier.slug} superseded", f"[[{by}]]")
            self.save(page)

    def settle_backlinks(self) -> None:
        pending, self.pending = self.pending, []
        for ref, slug, category, origin in pending:
            self.backlink(ref, slug, category, origin, last=True)

    # decisions

    def decision(self, record: dict, deferred: list[tuple[str, str]] | None = None) -> None:
        """The Decision page of a Case; `deferred` is the `(slug, purpose)` of every `defer`
        line of the Case, in ledger order, written under `## Deferred` (case 186.1)."""
        slug = record["decision"]
        path = self.path("decisions", slug)
        if path.exists():
            return
        text = record.get("case_text") or {}
        tags = list(record.get("tags") or [])
        targets = record.get("targets") or []
        for target in targets:
            if target.get("category") in CATEGORIES:
                page = self.find(str(target.get("slug")))
                for tag in as_list(page.props.get("tags")) if page else []:
                    if tag not in tags:
                        tags.append(tag)
        props: dict = {"type": "decision", "case": str(record["case"]), "status": "current"}
        for kind in KINDS:  # one list per kind present, the slugs in ledger order (case 59.4)
            slugs = [str(t.get("slug")) for t in targets if str(t.get("kind")) == kind]
            if slugs:
                props[kind] = slugs
        sources = [str(t["source"]) for t in targets if t.get("source")]
        if sources:
            props["source"] = sources
        if record.get("supersedes"):
            props["supersedes"] = list(record["supersedes"])
        props["origin"] = record["origin"]
        props["sprint"] = self.sprint
        props["created"] = self.date
        props["tags"] = tags  # the union of the targets' tags; empty is a fact, not a gap
        sections = {}  # no Given, no When, no Criterion list: the contract lives on the Estimate (201.2)
        for name, key in (("Context", "context"), ("Problem", "problem")):
            if text.get(key):
                sections[f"## {name}"] = text[key]
        if deferred:  # the body of a deferred decision is never dropped (case 186.1)
            sections["## Deferred"] = "\n\n".join(
                f"### [[{target}]]\n\n{str(purpose).strip()}" for target, purpose in deferred
            )
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
            self.history(other, f"superseded by {slug}", f"[[{slug}]]")
            self.save(other)
            self.clear_deferred_by(other, slug, record["origin"])

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
        # 104.1: a superseded decision no longer describes the present
        for path in sorted((self.wiki / "decisions").glob("*.md")):
            if path.stem == "schema":
                continue
            page = read_page(path, "decisions")
            if page.error or str(page.props.get("status")) != "superseded":
                continue
            page.props["status"] = "archived"
            self.history(page, "archived · superseded", None)
            self.save(page)
        lessons = {}
        for path in (self.wiki / "lessons").glob("*.md"):
            if path.stem != "schema":
                lessons[path.stem] = read_page(path, "lessons")

        def child_status(slug: str) -> str:
            """`wiki/lessons/` first, then the archive (case 110); no page anywhere is
            not `archived`, so the child stays live and lint names the missing page."""
            child = lessons.get(slug)
            if child is None:
                for path in archived_paths(self.project_dir, slug):
                    child = read_page(path, path.parent.name)
                    break
            return str(child.props.get("status")) if child is not None else "none"

        for path in sorted((self.wiki / "insights").glob("*.md")):
            if path.stem == "schema":
                continue
            page = read_page(path, "insights")
            if page.error:
                continue
            status = str(page.props.get("status"))
            if status == "actioned":  # 104.2: its lessons did their work
                for slug in as_list(page.props.get("children")):
                    child = lessons.get(slug)
                    if child is None or child.error:
                        continue
                    if str(child.props.get("status")) == "clustered":
                        child.props["status"] = "archived"
                        self.history(child, "archived · insight actioned", None)
                        self.save(child)
            live = [s for s in as_list(page.props.get("children")) if child_status(s) != "archived"]
            changed = False
            if page.props.get("severity") != len(live):
                page.props["severity"] = len(live)
                changed = True
            if status == "open" and not live:  # 104.3: its evidence is withdrawn
                page.props["status"] = "archived"
                self.history(page, "archived · no live child", None)
                changed = True
            if changed:
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


def deferred_of(data: dict) -> dict[str, list[tuple[str, str]]]:
    """Per Case, the `(slug, purpose)` of its `defer` entries in ledger order — for the
    `## Deferred` section of the Decision page (case 186.1); a `purpose` the entry lacks
    is left out, never invented."""
    out: dict[str, list[tuple[str, str]]] = {}
    for entry in data.get("entries") or []:
        if not isinstance(entry, dict) or entry.get("kind") != "defer":
            continue
        purpose = (entry.get("fields") or {}).get("purpose")
        if purpose is None or "case" not in entry:
            continue
        out.setdefault(str(entry["case"]), []).append((str(entry.get("slug")), str(purpose)))
    return out


def apply_decision(
    vault: Vault, record: dict, stamp: str, deferred: list[tuple[str, str]] | None = None
) -> None:
    if record.get("applied"):
        return
    before = len(vault.errors)
    try:
        vault.decision(record, deferred)
    except Exception as exc:  # noqa: BLE001
        vault.error(record.get("decision", "?"), f"{type(exc).__name__}: {exc}")
    if len(vault.errors) == before:
        record["applied"] = stamp
        record.pop("failed", None)
    else:
        record["failed"] = vault.errors[-1]
    vault.write_log()


def apply(vault: Vault, data: dict) -> None:
    stamp = vault.now.strftime("%H:%M:%S")
    records = {str(r.get("case")): r for r in data.get("decisions") or []}
    deferred = deferred_of(data)
    for entry in data.get("entries") or []:
        if not isinstance(entry, dict) or entry.get("applied"):
            continue
        if entry.get("superseded_by"):  # a later Case did its work; only the Decision page
            if "case" in entry and str(entry["case"]) in records:  # of its Case is written,
                case = str(entry["case"])
                apply_decision(vault, records[case], stamp, deferred.get(case))  # before the
            continue  # superseding one marks it (case 151)
        if "kind" not in entry and entry.get("failed"):  # a line materialize could not lift
            vault.error(
                f"line {entry.get('line', '?')}", f"not lifted by materialize; {entry['failed']}"
            )
            continue  # the mark stays as materialize wrote it (case 142.2)
        if "case" in entry and str(entry["case"]) in records:  # the Decision page first (52.4)
            case = str(entry["case"])
            apply_decision(vault, records[case], stamp, deferred.get(case))
        kind = entry.get("kind")
        if entry.get("category") == "file":
            print(
                f"generate: {entry['slug']}: a Rule-class file, applied by hand", file=vault.stdout
            )
            entry["applied"] = stamp
            entry.pop("failed", None)
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
            else:  # `remove_criterion` among them: the shape before case 189 (201.1)
                vault.error(entry.get("slug", "?"), f"unknown kind {kind!r}")
        except Exception as exc:  # noqa: BLE001 — one entry fails alone, the run goes on
            vault.error(entry.get("slug", "?"), f"{type(exc).__name__}: {exc}")
        if len(vault.errors) == before:
            entry["applied"] = stamp
            entry.pop("failed", None)  # a failure that is over is not shown (53.3)
        else:
            entry["failed"] = vault.errors[-1]
        vault.write_log()
    vault.settle_backlinks()
    vault.write_log()
    for record in data.get("decisions") or []:
        apply_decision(vault, record, stamp, deferred.get(str(record.get("case"))))
    vault.cascade()
    vault.register_tags(data.get("new_tags") or [])
    vault.write_log()


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi generate", description=__doc__.split("\n\n")[1])
    p.add_argument(
        "--date", default=None, help="the units of one raw/<date>; without it, every unit"
    )
    return p


def generate_date(project_dir: Path, unit: str, now, stdout, stderr) -> int:
    """One unit, `<date>` or `<date>/<HHMM>` (case 103.3): apply the unapplied entries of
    its yaml; exit 1 when an entry failed."""
    date = unit.split("/")[0]
    path = yaml_path(project_dir, unit)
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
    print(f"generate: {unit}: {touched} page(s) written or changed", file=stdout)
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
    dates = units_with(project_dir, "materialize.yaml", args.date)
    if args.date and not dates:
        dates = [args.date]  # so the missing yaml is named
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
