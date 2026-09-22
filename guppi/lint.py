"""`guppi lint` — the vault's integrity, one line per finding, exit 1 on any.

Reads every page under `vault/wiki/<category>/` (archive excluded) against that category's
`schema.yaml` and reports `<category>/<slug>: <class>: <what>`; writes nothing. The
classes, in the order they are checked: `schema` (a missing field or section, a value
outside the list, a conditional not met), `schema-description` (a field or section the
lists of `schema.yaml` name without a description under its `fields` or `sections`, or a
description of a name no list carries — the prose of the schema lives in the yaml since
case 304.8), `ref` (a slug no live or archived page carries; a
body `[[…]]` may also name a hub file under `wiki/` by its stem or its path, case 149.3;
an `applies_to` that names no live Entity, and an Entity's `rules` that differs from the
live rules whose `applies_to` names it, case 305.5;
and, case 72.6, a `[[slug]]` under a decision page's `## Criterion` that is not a live or
archived Estimate page, or a `### case N` block under an Estimate's `## Criterion` with no
live or archived `decision-case-N`), `origin` (a ledger file or `[case N]` line that does
not exist), `path` (a file named in
`implementation_ref` or `governs` that does not exist), `orphan` (a live entity, rule or
estimate no other live page's frontmatter names; a lesson is a record and an Insight names
it or not; an Insight owns its children through `children`, archived or not, and is never
one, case 156), `status` (a `built` page with an Estimate not `passed`, a `draft` one with
every Estimate `passed`; an Estimate `passed` or `failed` without `## Result`; an Estimate
whose `target` is not an entity or a rule, or does not list it, case 53.1), `unread` (every
Estimate `pending` or `failed`, one finding each — red between a change of a promise and
its reading, by design; cases 182, 202), `method` (the `method` field, or on a page of the
shape before case 193 the `## Method` section: for a MOC's Estimate a `make <target>` of the
Makefile passes whatever else it says, and one that names none may be a reading when its
children's Estimates are all readings, case 112.1, or when a sibling Estimate of the MOC
names a `make <target>` of the Makefile, case 212; for a Leaf's Estimate a `tests/` file
that exists, the word `pytest`, a `make <target>` of the Makefile, or a reading — "by hand",
"reading" — case 202), `decision` (a decision page with none of the four
kind lists `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug` still
present, or a slug in a list with a category prefix that names neither a live nor an
archived page, case 59.4), `deferred` (a placeholder — a rule or entity page that carries
`deferred_by` and lacks the fields a `create` fills, `kind`, `estimates` and `tags` — earns
one finding, `deferred: <N> times since case <M>`, N the `deferred` lines of its History
and M the case of the first, in place of those three `schema` findings and of `orphan`; a
page with `deferred_by` whose fields are in place earns none, case 186.3), and last
`unmigrated` (one line, `estimates: unmigrated: <N> pages in the shape before case 193` —
the live Estimates without a `method` field, or with `## Context`, `## Method` or a `###
case N` block; no line at zero; the checks of the old shape leave by an update of the rule
once it reads zero, case 202). A
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
    "applies_to",  # the edge Rule → Entity, written in the Case (case 305)
    "rules",  # its backlink on the Entity, computed by generate (case 305.3)
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
TEST_PATH = re.compile(r"`?(tests/[\w./-]+\.py)`?")
MAKE_TARGET = re.compile(r"`?make ([\w-]+)`?")
BY_HAND = "by hand"
READING = "reading"  # a live reading is a method too (case 202)
PYTEST = "pytest"
CRITERION = "## Criterion"
WHEN = "## When"
CASE_BLOCK = re.compile(r"^### case ([\w.]+)\s*$", re.MULTILINE)  # an Estimate's Criterion block
PLACEHOLDER_FIELDS = ("kind", "estimates", "tags")  # what a `create` fills (case 186.3)
DEFERRED_LINE = re.compile(r"^- \S+ deferred\b.*(?:\[\[decision-case-|#case-)([\w.]+?)\]?\]?$")


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


def is_placeholder(page: Page) -> bool:
    """A rule or entity page born of a `defer` without a `ref`: it carries `deferred_by`
    and none of the fields a `create` fills (case 186.3)."""
    return (
        page.category in ("rules", "entities")
        and not page.error
        and page.props.get("deferred_by") is not None
        and not any(field in page.props for field in PLACEHOLDER_FIELDS)
    )


def check_deferred(page: Page) -> list[Finding]:
    """One finding for a placeholder, with its count: `deferred: <N> times since case <M>`,
    N the `deferred` lines of its History, M the case of the first (case 186.3)."""
    if not is_placeholder(page):
        return []
    cases = [
        m.group(1)
        for line in (page.sections.get("## History") or "").splitlines()
        if (m := DEFERRED_LINE.match(line.strip()))
    ]
    since = f" since case {cases[0]}" if cases else ""
    times = "time" if len(cases) == 1 else "times"
    return [Finding(page, "deferred", f"{len(cases)} {times}{since}")]


def check_schema(page: Page, schema: dict) -> list[Finding]:
    out: list[Finding] = []
    if page.error:
        return [Finding(page, "schema", page.error)]
    props = schema.get("properties") or {}
    body = schema.get("body") or {}
    placeholder = is_placeholder(page)
    for field in props.get("required") or []:
        if field not in page.props and not (placeholder and field in PLACEHOLDER_FIELDS):
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


def listed_names(block: dict) -> set[str]:
    """Every name the `required`, `optional` and conditional `required` lists of a
    `properties` or `body` block carry."""
    names = {str(n) for n in block.get("required") or []}
    names |= {str(n) for n in block.get("optional") or []}
    for rule in block.get("conditional") or []:
        names |= {str(n) for n in (rule or {}).get("required") or []}
    return names


def check_descriptions(category: str, schema: dict) -> list[Finding]:
    """Case 304.8: the prose of a schema is data of its yaml — `fields` describes every
    name the lists of `properties` carry and nothing else, `sections` the same for `body`;
    one finding per name missing on either side, class `schema-description`."""
    out = []
    for block, key, word in (("properties", "fields", "field"), ("body", "sections", "section")):
        listed = listed_names(schema.get(block) or {})
        described = schema.get(key)
        described = {str(k) for k in described} if isinstance(described, dict) else set()
        for name in sorted(listed - described):
            out.append(
                Finding(
                    f"{category}/schema",
                    "schema-description",
                    f"{word} {name} has no description",
                )
            )
        for name in sorted(described - listed):
            out.append(
                Finding(
                    f"{category}/schema",
                    "schema-description",
                    f"{key} describes {name}, which no list names",
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
    `log`) or a file under `wiki/` by its path without the suffix — none since the schemas became pages (case 304)."""
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


def rules_of(entity_slug: str, pages: list[Page]) -> list[str]:
    """The live rules whose `applies_to` names the Entity, in slug order — what the
    cascade of `generate` writes into its `rules` (case 305.3)."""
    return sorted(
        p.slug
        for p in pages
        if p.category == "rules"
        and not p.error
        and entity_slug in as_list(p.props.get("applies_to"))
    )


def check_edges(page: Page, pages: list[Page], by_slug: dict[str, Page]) -> list[Finding]:
    """Case 305.5, class `ref`: an `applies_to` names a live Entity; an Entity's `rules`
    is the live rules whose `applies_to` names it — a difference names what is extra
    (`+`) and what is missing (`-`)."""
    out = []
    if page.category == "rules":
        for slug in as_list(page.props.get("applies_to")):
            target = by_slug.get(slug)
            if target is not None and target.category != "entities":
                out.append(Finding(page, "ref", f"applies_to names {slug}, which is not an entity"))
    elif page.category == "entities":
        listed = as_list(page.props.get("rules"))
        expected = rules_of(page.slug, pages)
        if sorted(listed) != expected:
            extra = ", ".join(f"+{s}" for s in sorted(set(listed) - set(expected)))
            missing = ", ".join(f"-{s}" for s in expected if s not in listed)
            diff = ", ".join(part for part in (extra, missing) if part)
            out.append(
                Finding(page, "ref", f"rules differs from the applies_to of the live rules: {diff}")
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
        if page.category not in ("decisions", "lessons", "insights")
        and page.slug not in referenced
        and not is_placeholder(page)  # its one finding is `deferred` (case 186.3)
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


def method_of(page: Page) -> str | None:
    """The `method` field, or on a page of the shape before case 193 the `## Method`
    section; None when the page carries neither (case 202)."""
    field = page.props.get("method")
    if field is not None and str(field).strip():
        return str(field)
    return page.sections.get("## Method")


def is_reading(method: str) -> bool:
    return BY_HAND in method or READING in method


def check_unread(page: Page) -> list[Finding]:
    """Every `pending` or `failed` Estimate is one finding, `unread: <status>` — red between
    a change of a promise and its reading, by design (cases 182, 202)."""
    if page.category != "estimates":
        return []
    status = str(page.props.get("status", ""))
    if status in ("pending", "failed"):
        return [Finding(page, "unread", status)]
    return []


def is_old_shape(page: Page) -> bool:
    """An Estimate of the shape before case 193: no `method` field, or `## Context`,
    `## Method` or a `### case N` block still on the page (case 202)."""
    return (
        page.category == "estimates"
        and not page.error
        and (
            page.props.get("method") is None
            or "## Context" in page.sections
            or "## Method" in page.sections
            or bool(CASE_BLOCK.search(page.sections.get(CRITERION) or ""))
        )
    )


def check_unmigrated(pages: list[Page]) -> list[Finding]:
    """One line for the remainder of the recut, `estimates: unmigrated: <N> pages in the
    shape before case 193`; no line at zero (case 202)."""
    count = sum(1 for p in pages if is_old_shape(p))
    if not count:
        return []
    pages_word = "page" if count == 1 else "pages"
    return [
        Finding("estimates", "unmigrated", f"{count} {pages_word} in the shape before case 193")
    ]


def sibling_names_a_target(page: Page, target: Page, by_slug: dict[str, Page], text: str) -> bool:
    """True when another Estimate of the same MOC names a `make <target>` the Makefile
    holds: the pipeline over the children is that sibling's (case 212)."""
    for slug in as_list(target.props.get("estimates")):
        other = by_slug.get(slug)
        if other is None or other is page:
            continue
        match = MAKE_TARGET.search(method_of(other) or "")
        if match and re.search(rf"^{re.escape(match.group(1))}:", text, re.MULTILINE):
            return True
    return False


def check_method(page: Page, by_slug: dict[str, Page], project_dir: Path) -> list[Finding]:
    """The `method` of an Estimate — the field, or the section of a page of the old shape:
    for a MOC's Estimate a `make <target>` of the Makefile passes whatever else it says,
    without one "by hand" passes when every child's Estimate is a reading (case 112.1) or
    when a sibling Estimate of the MOC names a `make <target>` of the Makefile (case 212);
    for a Leaf's Estimate a `tests/` file that exists, the word `pytest`, a `make
    <target>` of the Makefile, or a reading — "by hand", "reading" (case 202)."""
    if page.category != "estimates":
        return []
    method = method_of(page)
    target = by_slug.get(str(page.props.get("target", "")))
    if method is None or target is None:
        return []
    makefile = project_dir / "Makefile"
    text = makefile.read_text(encoding="utf-8") if makefile.exists() else ""
    match = MAKE_TARGET.search(method)  # the target first (case 112.1)
    if str(target.props.get("kind")) == "MOC":
        if not match and is_reading(method) and sibling_names_a_target(page, target, by_slug, text):
            return []  # the pipeline is a sibling Estimate's; nothing is hidden (case 212)
        if not match and is_reading(method):
            return [
                Finding(page, "method", f"says by hand while {child.slug} names a test file")
                for child in children_estimates(target, by_slug)
                if not is_reading(method_of(child) or "")
            ][:1]
        if not match:
            return [Finding(page, "method", "a MOC's Estimate names no `make <target>`")]
        if not re.search(rf"^{re.escape(match.group(1))}:", text, re.MULTILINE):
            return [Finding(page, "method", f"the Makefile has no target {match.group(1)}")]
        return []
    if is_reading(method):
        return []
    paths = TEST_PATH.findall(method)
    for rel in paths:
        if not (project_dir / rel).exists():
            return [Finding(page, "method", f"names {rel}, which does not exist")]
    if match:
        if not re.search(rf"^{re.escape(match.group(1))}:", text, re.MULTILINE):
            return [Finding(page, "method", f"the Makefile has no target {match.group(1)}")]
        return []
    if not paths and PYTEST not in method:
        return [
            Finding(
                page, "method", "names no tests/ file, pytest or make target and is not a reading"
            )
        ]
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
        findings.extend(check_descriptions(category, schema))
        if category == "decisions":
            schema = without_when(schema)
        for page in vault[category]:
            findings.extend(check_schema(page, schema))
    for page in pages:
        if page.error:
            continue
        findings.extend(check_refs(page, known, hubs))
        findings.extend(check_edges(page, pages, by_slug))
        findings.extend(check_criterion(page, known))
        findings.extend(check_origin(page, project_dir))
        findings.extend(check_paths(page, project_dir))
    findings.extend(check_orphans([p for p in pages if not p.error]))
    for page in pages:
        if page.error:
            continue
        findings.extend(check_deferred(page))
        findings.extend(check_status(page, by_slug))
        findings.extend(check_unread(page))
        findings.extend(check_method(page, by_slug, project_dir))
        findings.extend(check_decision(page, known))
    findings.extend(check_unmigrated(pages))
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
