"""`guppi lint` — the vault's integrity, one line per finding, exit 1 on any.

Reads every page under `vault/wiki/<category>/` (archive excluded) against that category's
`schema.yaml` and reports `<category>/<slug>: <class>: <what>`; writes nothing. The
classes, in the order they are checked: `schema` (a missing field or section, a value
outside the list, a conditional not met, a field `properties.single` names holding a list —
one value is its shape, case 362.1), `schema-description` (a field or section the
lists of `schema.yaml` name without a description under its `fields` or `sections`, or a
description of a name no list carries — the prose of the schema lives in the yaml since
case 304.8), `ref` (a slug no live or archived page carries; a
body `[[…]]` may also name a hub file under `wiki/` by its stem or its path, case 149.3;
an `applies_to` that names no live Entity, and an Entity's `rules` that differs from the
live rules whose `applies_to` names it, case 305.5;
and, case 72.6, a `[[slug]]` under a decision page's `## Criterion` that is not a live or
archived Estimate page, or a `### case N` block under an Estimate's `## Criterion` with no
live or archived `decision-case-N`), `origin` (a ledger file or `[case N]` line that does
not exist; the `#case-N` of a Case with no line of its own is found by a line `[case N.M]` of
a sub-case, case 544.9), `path` (a file named in
`implementation_ref` or `governs` that does not exist), `markers` (a page with
`enforcement: render` whose `## Render` is absent, or whose text does not open with
`<!-- slug -->` and close with `<!-- /slug -->`; and a `render_mode: full` page whose Render
holds a closing line for one of its `children` — a parent carries one opening line per
child, and the closing line is the renderer's own, case 325.2), `fence` (a section of a page
with a code fence broken — a line inside the fence with a run at least as long and text
after it, or a fence open at the end of the section — by `fence_breaks` of
`guppi/materialize.py`, the judgment `pre-spec` runs over the pairs of a plan; a harness file
is not read, `render --check` compares it with its Render, case 487.2), `layout` (a page whose `type` does
not match the folder it sits in, a page whose `slug` field is not its filename, and a `.md`
at the root of `wiki/` that no live rule page names — case 315), `orphan` (a live entity, rule or
estimate no other live page's frontmatter names; a lesson is a record and an Insight names
it or not; an Insight owns its children through `children`, archived or not, and is never
one, case 156), `status` (a `built` page with an Estimate not `passed`, a `draft` one with
every Estimate `passed`; an Estimate `passed` or `failed` without `## Result`; an Estimate
whose `target` is not an entity or a rule, or does not list it, case 53.1), `unread` (every
Estimate `pending` or `failed`, one finding each — red between a change of a promise and
its reading, by design; cases 182, 202), `method` (the `method` field alone, case 506.3:
for a MOC's Estimate a `make <target>` of the
Makefile passes whatever else it says, and one that names none may be a reading when its
children's Estimates are all readings, case 112.1, or when a sibling Estimate of the MOC
names a `make <target>` of the Makefile, case 212; on a MOC with `render_mode: full` the
Estimates of a child with `enforcement: render` are not counted, since that child's Render
is part of the parent's file and its Estimate promises the child's own behaviour, case 459;
for a Leaf's Estimate a `tests/` file that exists, the word `pytest`, a `make <target>` of the Makefile, or a reading — "by hand",
the one spelling since case 330.1; the four forms are one predicate, `names_a_form`, which
`pre-spec` calls over the plan, case 331), `moment` (an Estimate whose `method` ties a
reading by hand to the first of something after the render or after the change — a part of
the `method` between two `;` that holds `by hand` and the first of something after the
render or the change; a reading names the kind of its moment, and any such moment counts,
in this session or an earlier one; the one predicate, `tied_to_a_one_off_moment`, which
`pre-spec` calls over the plan, case 613.1), `decision` (a decision page with none of the four
kind lists `create`, `update`, `delete`, `defer` and no `children` — the page of a Case with
sub-cases carries `children` in their place, case 544.9 — or with `kind` or `target_slug` still
present, or a slug in a list with a category prefix that names neither a live nor an
archived page, case 59.4; the prefix is judged by `category_of` of `guppi/materialize.py`,
the one table, `decision-` included, case 460.3), `deferred` (a placeholder — a rule or entity page that carries
`deferred_by` and lacks the fields a `create` fills, `kind`, `estimates` and `tags` — earns
one finding, `deferred: <N> times since case <M>`, N the `deferred` lines of its History
and M the case of the first, in place of those three `schema` findings and of `orphan`; a
page with `deferred_by` whose fields are in place earns none, case 186.3). An Estimate
without a `method` field is a `schema` finding of `estimates/schema.yaml`, which requires the
field (case 506.1); the count of the shape before case 193 left with it (case 506.2). A
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
from guppi.materialize import (
    category_of,  # the one table of prefixes (case 460.3)
    fence_breaks,  # the one judgment of a fence (case 487.2)
)
from guppi.pages import CATEGORIES, HISTORY, Page, read_vault, slug_of, wiki_root

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
KINDS = ("create", "update", "delete", "defer")  # a decision page's lists (case 59.4)
PATH_FIELDS = ("implementation_ref", "governs")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
CODE_SPAN = re.compile(r"`[^`\n]*`")  # a `[[slug]]` quoted in prose is not a link
# `raw/<date>/ledger.md#…` (the shape before case 103) or `raw/<date>/<HHMM>/ledger.md#…`
ORIGIN_CASE = re.compile(r"^raw/(\d{4}-\d\d-\d\d(?:/\d{4})?)/ledger\.md#case-([\w.]+)$")
ORIGIN_LINE = re.compile(r"^raw/(\d{4}-\d\d-\d\d(?:/\d{4})?)/ledger\.md#L(\d+)$")
TEST_PATH = re.compile(r"`?(tests/[\w./-]+\.py)`?")
MAKE_TARGET = re.compile(r"`?make ([\w-]+)`?")
BY_HAND = "by hand"  # the one spelling of a reading (case 330.1)
PYTEST = "pytest"
CRITERION = "## Criterion"
RENDER = "## Render"
WHEN = "## When"
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


def holds(props: dict, when: dict) -> bool:
    """Whether the fields `props` hold every value of the `when` of a condition."""
    return all(str(props.get(key)) == str(value) for key, value in when.items())


def unmet_conditions(
    props: dict, sections, schema: dict, block: str | None = None
) -> list[tuple[dict, str]]:
    """Each condition of `schema` — a rule of the `conditional` list of its `properties` or
    of its `body`, or of the one `block` named — that the fields `props` and the section
    names `sections` do not meet, as `(when, what)`: the `when` of the rule and the words of
    the finding. The one judgment of a condition: `check_schema` reports each `what` on a
    page, and the check of a plan of `guppi/prespec.py` on the page as a Case leaves it
    (case 714)."""
    out: list[tuple[dict, str]] = []
    for name in (block,) if block else ("properties", "body"):
        for rule in (schema.get(name) or {}).get("conditional") or []:
            when = rule.get("when") or {}
            if not holds(props, when):
                continue
            for required in rule.get("required") or []:
                if name == "body" and required not in sections:
                    out.append((when, f"missing section {required} (given {rule['when']})"))
                elif name != "body" and required not in props:
                    out.append((when, f"missing field {required} (given {rule['when']})"))
            for field, banned in (rule.get("forbidden_values") or {}).items():
                if field in props and str(props[field]) in [str(b) for b in banned]:
                    out.append(
                        (when, f"{field} may not be {props[field]!r} (given {rule['when']})")
                    )
    return out


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
        for line in (page.sections.get(HISTORY) or "").splitlines()
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
    for field in props.get("single") or []:  # one value is its shape, never a list (362.1)
        if isinstance(page.props.get(field), list):
            out.append(Finding(page, "schema", f"{field} holds a list; one link is its shape"))
    for _, what in unmet_conditions(page.props, page.sections, schema, "properties"):
        out.append(Finding(page, "schema", what))
    for section in body.get("required") or []:
        if section not in page.sections:
            out.append(Finding(page, "schema", f"missing section {section}"))
    for _, what in unmet_conditions(page.props, page.sections, schema, "body"):
        out.append(Finding(page, "schema", what))
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
    archived Estimate page. One finding per slug, class `ref`. An Estimate's Criterion is
    one text, and a `### case N` line in it is no link (case 506.4)."""
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
            # a Case with no line of its own is found by a line of a sub-case (case 544.9)
            if f"[case {what}]" not in text and f"[case {what}." not in text:
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


TYPES = {
    "entities": "entity",
    "rules": "rule",
    "estimates": "estimate",
    "lessons": "lesson",
    "insights": "insight",
    "decisions": "decision",
}


def check_layout(wiki: Path, pages: list[Page], rules: list[Page]) -> list[Finding]:
    """Case 315: a page whose `type` does not match the folder it sits in, a page whose
    `slug` field is not its filename, and a `.md` at the root of `wiki/` that no live rule
    page names — it reached the vault without a decision."""
    out: list[Finding] = []
    for page in pages:
        if page.error:
            continue
        expected = TYPES.get(page.category)
        kind = str(page.props.get("type") or "")
        if expected and kind and kind != expected:
            out.append(Finding(page, "layout", f"type is {kind!r} under {page.category}/"))
        written = page.props.get("slug")
        if written and str(written) != page.path.stem:
            out.append(
                Finding(page, "layout", f"slug is {written!r}, the file is {page.path.stem}")
            )
    named = " ".join(p.path.read_text(encoding="utf-8") for p in rules if p.path.exists())
    for file in sorted(wiki.glob("*.md")):
        if file.name not in named and f"[[{file.stem}]]" not in named:
            out.append(Finding(f"wiki/{file.stem}", "layout", "no live rule page names this file"))
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
    """At least one of the four kind lists, or `children` on the page of a Case with
    sub-cases (case 544.9), neither `kind` nor `target_slug`; every slug with a category
    prefix a live or archived page, a slug without one a thing outside the vault and not
    looked up (case 59.4). The prefix is judged by `category_of` of `guppi/materialize.py`,
    `decision-` included — one table, not a copy (case 460.3)."""
    if page.category != "decisions":
        return []
    out = []
    if not any(kind in page.props for kind in KINDS) and not page.props.get("children"):
        out.append(Finding(page, "decision", f"none of {', '.join(KINDS)} is present"))
    for field in ("kind", "target_slug"):
        if field in page.props:
            out.append(Finding(page, "decision", f"{field} is no longer a field (case 59.4)"))
    for kind in KINDS:
        for slug in as_list(page.props.get(kind)):
            if category_of(slug) is not None and slug not in known:
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
    """The Estimate pages of a MOC's direct children that count against its reading, in the
    children's order. On a MOC with `render_mode: full` the Estimates of a child with
    `enforcement: render` are skipped: that child's Render is part of the parent's file, and
    its Estimate promises the child's own behaviour, read on its own (cases 378.5, 459)."""
    full = str(moc.props.get("render_mode") or "") == "full"
    out = []
    for child_slug in as_list(moc.props.get("children")):
        child = by_slug.get(child_slug)
        if child is None:
            continue
        if full and str(child.props.get("enforcement") or "") == "render":
            continue  # its Render is spliced into the parent's file (case 459)
        for slug in as_list(child.props.get("estimates")):
            estimate = by_slug.get(slug)
            if estimate is not None:
                out.append(estimate)
    return out


def method_of(page: Page) -> str | None:
    """The `method` field; None when the page carries none. A `## Method` section is not
    read (case 506.3)."""
    field = page.props.get("method")
    if field is not None and str(field).strip():
        return str(field)
    return None


def is_reading(method: str) -> bool:
    return BY_HAND in method


def names_a_form(method: str) -> bool:
    """Whether a `method` names one of the four forms this module classifies: a `make
    <target>`, the word `pytest`, a path under `tests/`, or the words `by hand` — the one
    spelling of a reading. The existence of the file and of the target is not judged here:
    `pre-spec` calls this predicate over the plan, where the test file is not written yet,
    and lint checks existence after it (case 331)."""
    return bool(
        is_reading(method)
        or MAKE_TARGET.search(method)
        or TEST_PATH.search(method)
        or PYTEST in method
    )


FIRST_AFTER = re.compile(r"\bfirst\b.*?\bafter the (?:render|change)\b")
CLAUSE = ";"  # a `method` joins its parts by `;`, such as a test run and a reading


def tied_to_a_one_off_moment(method: str) -> bool:
    """Whether a `method` ties a reading by hand to the first of something after the render
    or after the change — a moment that passes once and is gone when missed: a part of the
    `method` between two `;` that holds `by hand` and `FIRST_AFTER`. The one predicate of the
    class `moment`, which `pre-spec` calls over the plan (case 613.1)."""
    return any(is_reading(clause) and FIRST_AFTER.search(clause) for clause in method.split(CLAUSE))


ANOTHER_SESSION = re.compile(
    r"\b(?:later|next)\s+session\b|\bsession\s+after\b|\blibrarian\b|(?<![\w/])/hi\b",
    re.IGNORECASE,
)
PERSON = re.compile(r"\bperson\b", re.IGNORECASE)


def waits_for_another_session(method: str) -> bool:
    """Whether a `method` waits for another session: a part between two `;` that names a
    later session, the next session, a session after another, the librarian or `/hi`, and
    does not name the person — whose answer at a `/hi` is the one reading a method may leave
    to another session. A method holds only what runs in its own session (case 670.4). The
    one predicate of this judgment, which `pre-spec` calls over the plan; the lint run does
    not call it, so the live pages give no finding by it."""
    return any(
        ANOTHER_SESSION.search(part) and not PERSON.search(part) for part in method.split(CLAUSE)
    )


def check_moment(page: Page) -> list[Finding]:
    """An Estimate whose `method` ties its reading by hand to the first moment after the
    render or the change, by `tied_to_a_one_off_moment`, is one finding of the class `moment`;
    a reading names the kind of its moment (case 613.1)."""
    if page.category != "estimates":
        return []
    if tied_to_a_one_off_moment(method_of(page) or ""):
        return [
            Finding(
                page,
                "moment",
                "ties its reading by hand to the first moment after the render or the change — "
                "name the kind of its moment",
            )
        ]
    return []


def check_unread(page: Page) -> list[Finding]:
    """Every `pending` or `failed` Estimate is one finding, `unread: <status>` — red between
    a change of a promise and its reading, by design (cases 182, 202)."""
    if page.category != "estimates":
        return []
    status = str(page.props.get("status", ""))
    if status in ("pending", "failed"):
        return [Finding(page, "unread", status)]
    return []


def check_markers(page: Page) -> list[Finding]:
    """A page that forces its rule by render carries its own marker pair around the text of
    its `## Render`: the section opens with `<!-- slug -->` and closes with `<!-- /slug -->`,
    or the renderer cannot tell the page's own text from a child's. A `full` page whose Render
    holds a closing line for one of its `children` is the second finding of the class: a
    parent carries one opening line per child, and the closing line is the renderer's own
    (case 325.2)."""
    if str(page.props.get("enforcement") or "") != "render":
        return []
    section = page.sections.get(RENDER)
    if section is None:
        return [Finding(page, "markers", f"no {RENDER} section")]
    opening, closing = f"<!-- {page.slug} -->", f"<!-- /{page.slug} -->"
    lines = section.splitlines()
    if lines[:1] != [opening] or lines[-1:] != [closing]:
        return [Finding(page, "markers", f"{RENDER} is not wrapped in {opening} … {closing}")]
    if str(page.props.get("render_mode") or "") != "full":
        return []
    for child in as_list(page.props.get("children")):
        slug = slug_of(child)
        if f"<!-- /{slug} -->" in lines[1:-1]:
            return [
                Finding(
                    page,
                    "markers",
                    f"a closing line <!-- /{slug} --> for the child {slug}; "
                    "a parent carries one opening line per child",
                )
            ]
    return []


def check_fences(page: Page) -> list[Finding]:
    """One `fence` finding per break of a code fence in a section of the page, History
    included: a line inside a fence with a full run and text after it, or a fence open at
    the end of the section — by `fence_breaks` of `guppi/materialize.py`, the judgment
    `pre-spec` runs over the pairs of a plan; no copy of the pattern here (case 487.2)."""
    findings = []
    for name, text in page.sections.items():
        for kind, line in fence_breaks(text):
            what = "open at the end of the section" if kind == "open" else "with text after its run"
            findings.append(Finding(page, "fence", f"{name}: a code fence {what}: {line}"))
    return findings


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
    """The `method` field of an Estimate (case 506.3):
    for a MOC's Estimate a `make <target>` of the Makefile passes whatever else it says,
    without one "by hand" passes when every counted Estimate of the children is a reading
    (case 112.1) or when a sibling Estimate of the MOC names a `make <target>` of the Makefile
    (case 212); on a MOC with `render_mode: full` the Estimates of a child with `enforcement:
    render` are not counted (`children_estimates`, case 459);
    for a Leaf's Estimate a `tests/` file that exists, the word `pytest`, a `make
    <target>` of the Makefile, or a reading — "by hand", the one spelling since case 330.1."""
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
    if not names_a_form(method):  # the one predicate, shared with pre-spec (case 331)
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
        findings.extend(check_markers(page))
        findings.extend(check_fences(page))
    findings.extend(check_layout(wiki, pages, vault["rules"]))
    findings.extend(check_orphans([p for p in pages if not p.error]))
    for page in pages:
        if page.error:
            continue
        findings.extend(check_deferred(page))
        findings.extend(check_status(page, by_slug))
        findings.extend(check_unread(page))
        findings.extend(check_method(page, by_slug, project_dir))
        findings.extend(check_moment(page))
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
