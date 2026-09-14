"""`guppi lint` — the vault's integrity, one line per finding, exit 1 on any.

Reads every page under `vault/wiki/<category>/` (archive excluded) against that category's
`schema.yaml` and reports `<category>/<slug>: <class>: <what>`; writes nothing. The
classes, in the order they are checked: `schema` (a missing field or section, a value
outside the list, a conditional not met), `schema-prose` (`schema.md` and `schema.yaml`
naming different fields or sections), `ref` (a slug no live or archived page carries; a
body `[[…]]` may also name a hub file under `wiki/` by its stem or its path, case 149.3),
and, case 72.6, a `[[slug]]` under a decision page's `## Criterion` that is not a live or
archived Estimate page, or a `### case N` block under an Estimate's `## Criterion` with no
live or archived `decision-case-N`), `origin` (a ledger file or `[case N]` line that does
not exist), `path` (a file named in
`implementation_ref` or `governs` that does not exist), `orphan` (a live entity, rule,
estimate or insight no other live page's frontmatter names; a lesson is a record and an
Insight names it or not), `status` (a status its Estimates do not support; an Estimate
whose `target` is not an entity or a rule, case 53.1), `method` (an Estimate whose Method
names no existing test file, or no make target for a MOC; a MOC's Estimate that names a
target passes whatever else it says, and one that names none may say by hand when its
children's Estimates are all by hand, case 112.1), `decision` (a decision page with none of the four
kind lists `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug` still
present, or a slug in a list with a category prefix that names neither a live nor an
archived page, case 59.4). A
`deferred_by` slug and a `[[decision-case-N]]` wikilink in History are refs like any other
(cases 52.3, 52.4). `## When` is never a required section of a decision page, whatever
`decisions/schema.yaml` says: a page written before case 72 has one, a later page has none
(case 72.6). Rule page: `vault/wiki/rules/rule-lint.md`.
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

from guppi.event import project_root
from guppi.pages import CATEGORIES, Page, read_vault, wiki_root

LINK_FIELDS = (
    "parent",
    "children",
    "estimates",
    "target",
    "addressed_by",
    "insight",
    "deferred_by",
)
PREFIXES = {
    "entity-": "entities",
    "rule-": "rules",
    "estimate-": "estimates",
    "lesson-": "lessons",
    "insight-": "insights",
}
KINDS = ("create", "update", "delete", "defer")  # a decision page's lists (case 59.4)
PATH_FIELDS = ("implementation_ref", "governs")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
CODE_SPAN = re.compile(r"`[^`\n]*`")  # a `[[slug]]` quoted in prose is not a link
# `raw/<date>/ledger.md#…` (the shape before case 103) or `raw/<date>/<HHMM>/ledger.md#…`
ORIGIN_CASE = re.compile(r"^raw/(\d{4}-\d\d-\d\d(?:/\d{4})?)/ledger\.md#case-([\w.]+)$")
ORIGIN_LINE = re.compile(r"^raw/(\d{4}-\d\d-\d\d(?:/\d{4})?)/ledger\.md#L(\d+)$")
TABLE_FIELD = re.compile(r"^\|\s*`([^`]+)`")
TABLE_SECTION = re.compile(r"^\|\s*`(## [^`]+)`")
TEST_PATH = re.compile(r"`?(tests/[\w./-]+\.py)`?")
MAKE_TARGET = re.compile(r"`?make ([\w-]+)`?")
BY_HAND = "by hand"
CRITERION = "## Criterion"
WHEN = "## When"
CASE_BLOCK = re.compile(r"^### case ([\w.]+)\s*$", re.MULTILINE)  # an Estimate's Criterion block


class Finding:
    def __init__(self, page: Page | str, kind: str, what: str):
        where = page if isinstance(page, str) else f"{page.category}/{page.slug}"
        self.text = f"{where}: {kind}: {what}"


def as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def load_schema(wiki: Path, category: str) -> dict | None:
    path = wiki / category / "schema.yaml"
    if not path.exists():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else None


def matches(page: Page, when: dict) -> bool:
    return all(str(page.props.get(key)) == str(value) for key, value in when.items())


def check_schema(page: Page, schema: dict) -> list[Finding]:
    out: list[Finding] = []
    if page.error:
        return [Finding(page, "schema", page.error)]
    props = schema.get("properties") or {}
    body = schema.get("body") or {}
    for field in props.get("required") or []:
        if field not in page.props:
            out.append(Finding(page, "schema", f"missing field {field}"))
    for field, allowed in (props.get("values") or {}).items():
        if field in page.props and str(page.props[field]) not in [str(a) for a in allowed]:
            out.append(
                Finding(page, "schema", f"{field} is {page.props[field]!r}, not one of {allowed}")
            )
    for rule in props.get("conditional") or []:
        if not matches(page, rule.get("when") or {}):
            continue
        for field in rule.get("required") or []:
            if field not in page.props:
                out.append(Finding(page, "schema", f"missing field {field} (given {rule['when']})"))
        for field, banned in (rule.get("forbidden_values") or {}).items():
            if field in page.props and str(page.props[field]) in [str(b) for b in banned]:
                out.append(
                    Finding(
                        page,
                        "schema",
                        f"{field} may not be {page.props[field]!r} (given {rule['when']})",
                    )
                )
    for section in body.get("required") or []:
        if section not in page.sections:
            out.append(Finding(page, "schema", f"missing section {section}"))
    for rule in body.get("conditional") or []:
        if not matches(page, rule.get("when") or {}):
            continue
        for section in rule.get("required") or []:
            if section not in page.sections:
                out.append(
                    Finding(page, "schema", f"missing section {section} (given {rule['when']})")
                )
    return out


def prose_names(text: str) -> tuple[set[str], set[str]]:
    """The fields of the Properties table and the sections of the Body table in a
    `schema.md`; `## History` counts as a section when the file has that heading."""
    fields: set[str] = set()
    sections: set[str] = set()
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line.strip()
            if current == "## History":
                sections.add("## History")
            continue
        if current == "## Properties":
            match = TABLE_FIELD.match(line)
            if match:
                fields.add(match.group(1))
        elif current == "## Body":
            match = TABLE_SECTION.match(line)
            if match:
                sections.add(match.group(1))
    return fields, sections


def check_prose(wiki: Path, category: str, schema: dict) -> list[Finding]:
    path = wiki / category / "schema.md"
    if not path.exists():
        return [Finding(f"{category}/schema", "schema-prose", "schema.md is missing")]
    fields, sections = prose_names(path.read_text(encoding="utf-8"))
    props = schema.get("properties") or {}
    body = schema.get("body") or {}
    yaml_fields = set(props.get("required") or []) | set(props.get("optional") or [])
    yaml_sections = set(body.get("required") or []) | set(body.get("optional") or [])
    out = []
    for name in sorted(fields - yaml_fields):
        out.append(
            Finding(
                f"{category}/schema",
                "schema-prose",
                f"schema.md names field {name}, schema.yaml does not",
            )
        )
    for name in sorted(yaml_fields - fields):
        out.append(
            Finding(
                f"{category}/schema",
                "schema-prose",
                f"schema.yaml names field {name}, schema.md does not",
            )
        )
    for name in sorted(sections - yaml_sections):
        out.append(
            Finding(
                f"{category}/schema",
                "schema-prose",
                f"schema.md names section {name}, schema.yaml does not",
            )
        )
    for name in sorted(yaml_sections - sections):
        out.append(
            Finding(
                f"{category}/schema",
                "schema-prose",
                f"schema.yaml names section {name}, schema.md does not",
            )
        )
    return out


def archived_slugs(wiki: Path) -> set[str]:
    """Every page under `vault/archive/`, at any depth, except what sits under a `raw/`
    folder — the archived raw of a session is no page (cases 102.2, 103.5)."""
    folder = wiki.parent / "archive"
    if not folder.is_dir():
        return set()
    return {
        p.stem
        for p in folder.rglob("*.md")
        if p.stem != "schema" and "raw" not in p.relative_to(folder).parts[:-1]
    }


def ledger_files(project_dir: Path, unit: str) -> list[Path]:
    """Where the ledger named by an `origin` may sit (case 103.5): `vault/raw/<unit>/` or,
    once archived, `vault/archive/<sprint>/<unit>/raw/`; `unit` is `<date>` or
    `<date>/<HHMM>`."""
    found = [project_dir / "vault" / "raw" / unit / "ledger.md"]
    archive = project_dir / "vault" / "archive"
    if archive.is_dir():
        found.extend(sorted(archive.glob(f"*/{unit}/raw/ledger.md")))
    return [p for p in found if p.is_file()]


def links_of(page: Page) -> list[tuple[str, str]]:
    """`(field, slug)` for every frontmatter link and every `[[slug]]` in the body; a link
    under a decision page's `## Criterion` is `criterion`, checked by `check_criterion`."""
    out = []
    for field in LINK_FIELDS:
        for slug in as_list(page.props.get(field)):
            out.append((field, slug))
    for name, text in page.sections.items():
        field = "criterion" if page.category == "decisions" and name == CRITERION else "body"
        for slug in WIKILINK.findall(CODE_SPAN.sub("", text)):
            out.append((field, slug.strip()))
    return out


def hub_files(wiki: Path) -> set[str]:
    """What a body `[[…]]` may name besides a page (case 149.3): a file at the root of
    `wiki/` by its stem (`brief`, `index`, `glossary`, `case-schema`, `sprint`, `tags`,
    `log`) or a file under `wiki/` by its path without the suffix (`rules/schema`)."""
    out = {p.stem for p in wiki.glob("*.md")}
    for category in CATEGORIES:
        out |= {f"{category}/{p.stem}" for p in (wiki / category).glob("*.md")}
    return out


def check_refs(page: Page, known: set[str], hubs: set[str] = frozenset()) -> list[Finding]:
    out = []
    seen = set()
    for field, slug in links_of(page):
        if field == "criterion" or slug in known or slug in seen:
            continue
        if field == "body" and slug in hubs:  # a hub file under wiki/ (case 149.3)
            continue
        seen.add(slug)
        out.append(
            Finding(page, "ref", f"{field} names {slug}, which no live or archived page carries")
        )
    return out


def check_criterion(page: Page, known: set[str]) -> list[Finding]:
    """Case 72.6. On a decision page every `[[slug]]` under `## Criterion` is a live or
    archived Estimate page. On an Estimate page `## Criterion` may be plain text or
    `### case N` blocks; each block names a live or archived `decision-case-N`. One
    finding per slug or case, class `ref`."""
    out = []
    seen: set[str] = set()
    if page.category == "decisions":
        for field, slug in links_of(page):
            if field != "criterion" or slug in seen:
                continue
            seen.add(slug)
            if not slug.startswith("estimate-") or slug not in known:
                out.append(
                    Finding(
                        page,
                        "ref",
                        f"{CRITERION} names {slug}, which no live or archived Estimate page carries",
                    )
                )
    elif page.category == "estimates":
        for case in CASE_BLOCK.findall(page.sections.get(CRITERION) or ""):
            if case in seen:
                continue
            seen.add(case)
            if f"decision-case-{case}" not in known:
                out.append(
                    Finding(
                        page,
                        "ref",
                        f"{CRITERION} names case {case}, and no live or archived page "
                        f"decision-case-{case} exists",
                    )
                )
    return out


def without_when(schema: dict) -> dict:
    """The decision schema with `## When` dropped from every required list of `body`
    (case 72.6): lint does not depend on whether `schema.yaml` still requires it."""
    body = dict(schema.get("body") or {})
    body["required"] = [s for s in body.get("required") or [] if s != WHEN]
    body["conditional"] = [
        {**rule, "required": [s for s in rule.get("required") or [] if s != WHEN]}
        for rule in body.get("conditional") or []
    ]
    return {**schema, "body": body}


def check_origin(page: Page, project_dir: Path) -> list[Finding]:
    origin = page.props.get("origin")
    if origin is None:
        return []  # a missing required field is the schema check's finding
    origin = str(origin)
    match = ORIGIN_CASE.match(origin) or ORIGIN_LINE.match(origin)
    if match:
        unit, what = match.groups()
        ledgers = ledger_files(project_dir, unit)
        if not ledgers:
            return [Finding(page, "origin", f"{origin}: no such ledger")]
        if len(ledgers) > 1:
            return [Finding(page, "origin", f"{origin}: two ledgers for raw/{unit}")]
        text = ledgers[0].read_text(encoding="utf-8")
        if ORIGIN_CASE.match(origin):
            if f"[case {what}]" not in text:
                return [Finding(page, "origin", f"{origin}: no line carrying [case {what}]")]
        elif len(text.splitlines()) < int(what):
            return [Finding(page, "origin", f"{origin}: the ledger has no line {what}")]
        return []
    if page.category == "insights":
        return []
    return [Finding(page, "origin", f"{origin}: not raw/<date>[/<HHMM>]/ledger.md#case-N")]


def check_paths(page: Page, project_dir: Path) -> list[Finding]:
    out = []
    for field in PATH_FIELDS:
        for rel in as_list(page.props.get(field)):
            if not (project_dir / rel).exists():
                out.append(Finding(page, "path", f"{field} names {rel}, which does not exist"))
    return out


def check_orphans(pages: list[Page]) -> list[Finding]:
    referenced: set[str] = set()
    for page in pages:
        for field, slug in links_of(page):
            if field not in ("body", "criterion"):
                referenced.add(slug)
    return [
        Finding(page, "orphan", "no other live page names it in its frontmatter")
        for page in pages
        if page.category not in ("decisions", "lessons") and page.slug not in referenced
    ]


def check_decision(page: Page, known: set[str]) -> list[Finding]:
    """At least one of the four kind lists, neither `kind` nor `target_slug`; every slug
    with a category prefix a live or archived page, a slug without one a thing outside the
    vault and not looked up (case 59.4)."""
    if page.category != "decisions":
        return []
    out = []
    if not any(kind in page.props for kind in KINDS):
        out.append(Finding(page, "decision", f"none of {', '.join(KINDS)} is present"))
    for field in ("kind", "target_slug"):
        if field in page.props:
            out.append(Finding(page, "decision", f"{field} is no longer a field (case 59.4)"))
    for kind in KINDS:
        for slug in as_list(page.props.get(kind)):
            if any(slug.startswith(p) for p in PREFIXES) and slug not in known:
                out.append(
                    Finding(
                        page,
                        "decision",
                        f"{kind} names {slug}, which no live or archived page carries",
                    )
                )
    return out


def check_status(page: Page, by_slug: dict[str, Page]) -> list[Finding]:
    out = []
    status = str(page.props.get("status", ""))
    if page.category == "estimates":
        if status in ("passed", "failed") and "## Result" not in page.sections:
            out.append(Finding(page, "status", f"{status} without a ## Result section"))
        target = by_slug.get(str(page.props.get("target", "")))
        if target is not None and target.category not in ("entities", "rules"):
            out.append(
                Finding(
                    page,
                    "status",
                    f"target {target.slug} is a {target.category[:-1]}, not an entity or rule",
                )
            )
        elif target is not None and page.slug not in as_list(target.props.get("estimates")):
            out.append(
                Finding(page, "status", f"target {target.slug} does not list it in estimates")
            )
        return out
    if page.category not in ("entities", "rules"):
        return out
    estimates = [by_slug.get(slug) for slug in as_list(page.props.get("estimates"))]
    estimates = [e for e in estimates if e is not None]
    if not estimates:
        return out
    all_passed = all(str(e.props.get("status")) == "passed" for e in estimates)
    if status == "built" and not all_passed:
        pending = [e.slug for e in estimates if str(e.props.get("status")) != "passed"]
        out.append(Finding(page, "status", f"built while {pending[0]} is not passed"))
    if status == "draft" and all_passed:
        out.append(Finding(page, "status", "draft while every Estimate is passed"))
    return out


def children_estimates(moc: Page, by_slug: dict[str, Page]) -> list[Page]:
    """The Estimate pages of a MOC's direct children, in the children's order."""
    out = []
    for child_slug in as_list(moc.props.get("children")):
        child = by_slug.get(child_slug)
        if child is None:
            continue
        for slug in as_list(child.props.get("estimates")):
            estimate = by_slug.get(slug)
            if estimate is not None:
                out.append(estimate)
    return out


def check_method(page: Page, by_slug: dict[str, Page], project_dir: Path) -> list[Finding]:
    if page.category != "estimates":
        return []
    method = page.sections.get("## Method")
    target = by_slug.get(str(page.props.get("target", "")))
    if method is None or target is None:
        return []
    if str(target.props.get("kind")) == "MOC":
        match = MAKE_TARGET.search(method)  # the target first (case 112.1)
        if not match and BY_HAND in method:
            return [
                Finding(page, "method", f"says by hand while {child.slug} names a test file")
                for child in children_estimates(target, by_slug)
                if BY_HAND not in (child.sections.get("## Method") or "")
            ][:1]
        if not match:
            return [Finding(page, "method", "a MOC's Estimate names no `make <target>`")]
        makefile = project_dir / "Makefile"
        text = makefile.read_text(encoding="utf-8") if makefile.exists() else ""
        if not re.search(rf"^{re.escape(match.group(1))}:", text, re.MULTILINE):
            return [Finding(page, "method", f"the Makefile has no target {match.group(1)}")]
        return []
    if BY_HAND in method:
        return []
    paths = TEST_PATH.findall(method)
    if not paths:
        return [Finding(page, "method", "names no tests/ file and does not say by hand")]
    for rel in paths:
        if not (project_dir / rel).exists():
            return [Finding(page, "method", f"names {rel}, which does not exist")]
    return []


def lint(project_dir: Path) -> list[str]:
    wiki = wiki_root(project_dir)
    vault = read_vault(wiki)
    pages = [p for category in CATEGORIES for p in vault[category]]
    by_slug = {p.slug: p for p in pages}
    known = set(by_slug) | archived_slugs(wiki)
    hubs = hub_files(wiki)
    findings: list[Finding] = []
    for category in CATEGORIES:
        schema = load_schema(wiki, category)
        if schema is None:
            if vault[category]:
                findings.append(Finding(f"{category}/schema", "schema", "schema.yaml is missing"))
            continue
        findings.extend(check_prose(wiki, category, schema))
        if category == "decisions":
            schema = without_when(schema)
        for page in vault[category]:
            findings.extend(check_schema(page, schema))
    for page in pages:
        if page.error:
            continue
        findings.extend(check_refs(page, known, hubs))
        findings.extend(check_criterion(page, known))
        findings.extend(check_origin(page, project_dir))
        findings.extend(check_paths(page, project_dir))
    findings.extend(check_orphans([p for p in pages if not p.error]))
    for page in pages:
        if page.error:
            continue
        findings.extend(check_status(page, by_slug))
        findings.extend(check_method(page, by_slug, project_dir))
        findings.extend(check_decision(page, known))
    return [f.text for f in findings]


def parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(prog="guppi lint", description=__doc__.split("\n\n")[1])


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    try:
        findings = lint(project_dir)
    except Exception as exc:  # noqa: BLE001 — a lint that raises is still a red lint
        print(f"lint: cannot read the vault: {exc}", file=stderr)
        return 1
    for line in findings:
        print(line, file=stdout)
    return 1 if findings else 0
