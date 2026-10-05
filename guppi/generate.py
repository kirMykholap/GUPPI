"""`guppi generate [--date YYYY-MM-DD]` — the vault written from `materialize.yaml`.

The only writer to `vault/wiki/`. Applies the entries of a `materialize.yaml` in order and
writes nothing an entry does not carry: no section is derived from a ref field, no Estimate
from a flag (cases 166.2, 194.1, 201). Rule page: `vault/wiki/rules/rule-page-generation.md`.

One entry, one page (case 201.1). A `create` becomes a page: `type`, the entry's `fields`,
`status` by category (`INITIAL_STATUS`), `origin`, `sprint` (the yaml's `sprint`, which
`guppi materialize` takes from the first `## <id>` heading of `sprint.md` or, in a unit whose
ledger creates `entity-sprint-<id>`, from that `<id>` (case 628.6); else the first `## <id>`
heading of `sprint.md`), `created` (the yaml's date), `tags`; the body from `sections`, `## Purpose`
from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the
target's `estimates`, History `child <slug> added` / `estimate <slug> added`, settled at
the end of the run when the parent comes later in the yaml. An Estimate page carries
`purpose`, `method` and `checked` as fields after `target`, its `## Criterion` from
`sections`; neither `## Context` nor `## Method` is written. An `update` whose `set`
carries `method` drops no section (case 506.6), and an `update` with `sections.Criterion`
does not fail for want of a `method` field (case 506.5). A
`create` whose slug is a placeholder —
`status: draft`, no `kind` — fills it, `created` and `deferred_by` kept, History `created
over placeholder` (case 101.1); any other existing page is a collision, never a rename. An
`update` applies `set` to the frontmatter, `sections` as whole replacements — an Estimate's
Criterion is replaced whole this way (case 194.1) — `replace` inside the body (whitespace
collapsed, exactly one occurrence), History `updated: <change>`; an update with none of
those prints `nothing applied`. An `update` whose entry carries `rename: <new slug>` moves
the page first — `wiki/<category>/<old>.md` to `<new>.md`, the same category prefix, History
`renamed from <old>` — then applies the rest to the new file; every live page of `wiki/`,
Decision pages included, that names the old slug — a `[[link]]`, a ref field, the bare slug
as a word in a body — names the new one, with History `ref <old> → <new>` on every page but
a Decision page; `origin`, `## History`, `## Result`, the archive and `raw/` keep the old
name, they are records; a taken slug, live or archived, or one of another prefix fails the
entry. An `update` whose entry carries `reword` — a list of `{old, new}` pairs — replaces
each pair as a whole word (the boundary of `rename`) on every live rule, entity and
estimate, in `purpose`, `method` and every section but History and Result, with History
`reworded: old → new` on each page touched and one stdout line with the count; the page is
the owner, so a `new` its own text lacks — `purpose`, `governs`, `implementation_ref`,
Purpose, Render, compared without regard to case — or a pair with no hit fails the entry
before anything is written; Decision pages, lessons and Insights are records and stay; an
entry with `reword` alone is content (case 274.1). A rename of a slug goes through `rename`,
not `reword`; on a taken slug `rename` fails the entry and moves nothing (case 258.1). An
`update`, `estimate`, `delete` or `defer` whose slug is
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
(the union of the targets' tags); the body `## Problem` and `## Recommend` from `case_text`
when it carries them — the rest of the Case, `context` and `given` among it, stays in its
Case file `cases/case-<N>.md` in the folder of `origin` (cases 513, 544.7) — with
`## Context` before them only when `case_text` carries no `given` and the record no
`children`, the short form of a deferred decision, which has no Case file. A record with
`children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with
`children` their pages, no kind list, the tags of its sub-cases' targets and never
`## Context`; the page of a sub-case carries `parent`, its parent's page, and no `## Problem`
(case 544.7). And `## Deferred`, one `### [[slug]]` heading per target of the Case's `defer`
lines with its `purpose` verbatim (case 186.1); no `## Given`, no `## When`, no
`## Criterion` list — the contract lives on the Estimate; pages written before keep the
sections they carry and are not rewritten. A record with
`superseded_by` and no `case_text` — a Case superseded in its own session and gone from the
Spec (case 299.1) — gets a two-line body naming the superseding Decision; its status
follows the mechanism as for any superseded page (case 299.4). A `supersedes` sets
the earlier page `superseded`, appends to its `superseded_by` and removes its slug from
the `deferred_by` of each target of its `defer` list that a decision line of the
superseding Case names; a target the Case does not name keeps it, and a later Case that
supersedes the same page clears the targets it names (case 467.3). The same `supersedes`
sets each page in the `children` of the earlier page, at any depth, that stands `current`
`superseded`, a page of an earlier run too, with one History line; a child page `archived`
or already `superseded` is left as it stands, and no `deferred_by` is cleared through a
child (case 660.3). An existing page is skipped; a
`create` marked `exists` writes no page, its Decision page is still written.

One bad entry never stops the run (case 201.3): an entry that fails — a collision, a `ref`
naming no page, a `replace` absent or not unique, an unexpected shape, an unknown kind,
any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` and
skipped; the rest apply; exit 1. Every applied entry is marked `applied: <time>`, a stale
`failed` mark is dropped on apply (case 53.3), so a rerun writes nothing. An entry with
`failed` and no `kind` — a line `materialize` could not lift — is skipped with its mark
kept and one stderr line (case 142.2); an entry with `superseded_by` is not applied and
leaves no line, only its Case's Decision page is written (case 151). A `create`, `update`,
`delete` or `defer` entry whose `case`, `kind` and `slug` match an applied entry of the same
yaml — a Case ratified again in its session, its lines written again with a mark added — is
a repeat: like an `update` with no content it changes no page, appends nothing to `log.md`
and prints one stdout line, `generate: <slug>: line N repeats line M of case C; nothing
applied`; it is marked applied and loses a stale `failed` mark, so a repeat that failed on
an earlier run closes on the next (case 514). It ticks no line of any Spec — no page line,
no `read` line: a repeat does no work, and the lines of the Spec are closed by the entry
that did it; a second line of its kind and slug in its Case stays open (case 522).

The Spec (case 226.1): once a `create`, `update`, `delete` or `defer` entry is applied, the
first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case — from its
`## Case N` or `### Case N.M` heading to the next heading — of the `spec.md` beside the
yaml becomes `- [x]`. No Spec,
no section, no line: nothing is written and nothing is said. A reading (case 270.1): an
`estimate` entry, and a `create` with a folded reading, tick every unticked line
`- [ ] read `<slug>`` — in the Spec beside the yaml first, then in the `spec.md` of the
other units of `raw/`, oldest first, in any Case, since the entry carries no Case; every
line of the slug in the first Spec that holds one ticks — a reading is of the page, whose
Criterion is one, however many Cases of the session touched it (case 312); the
archive is not read. A `delete` entry, besides its page line, ticks the `read` lines of its
slug by the same walk and the same skips as an `estimate` entry: no reading of a deleted
Estimate will ever stand in the ledger, so nothing else would close its box (case 463). An
`update` entry whose `set` gives `status` the value `passed` or `failed` — an Estimate closed
by the person's decision, which no reading follows — ticks the `read` lines of its slug by
the same walk and the same skips; one that sets `pending`, or no `status`, ticks none (case
672). In the Spec beside the yaml an `estimate` or a `delete` entry, or such an `update`,
skips the section of a Case whose first decision entry carries a `line` greater than its own
— a Case ratified after the reading, the delete or the update, whose line waits for a
reading of its own (cases 280, 463, 672); a folded reading skips nothing of that, its Case
is the reading's. In every Spec all of them skip the
section of a Case whose entries the yaml beside that Spec mark `superseded_by` — the run's
entries for the Spec beside the yaml, the `materialize.yaml` of the other unit's folder
otherwise, read for the marks alone; no yaml, nothing skipped there — its work stands under
the superseding Case (case 286). An applied entry ticks its line whatever its category, an
entry with no category (`unknown`, case 320) included; only a `lesson` entry and a failed
entry tick nothing — a failed `delete` or `update` leaves the `read` lines of its slug as
they stand (cases 460.1, 463, 672); the lines on code, tests, migrations and `by hand` checks stay the
agent's.

The cascade after all entries (case 201.4): an entity or rule whose live Estimates are all
`passed` becomes `built`, a `built` one with a live Estimate not passed returns to `draft` —
an Estimate standing `archived` is not counted, as a slug with no page is not counted, since
a `delete` of the same run leaves its file in place until `cleanup` (case 328),
History `· cascade`; a `superseded` Decision page becomes `archived` (case 104.1); the
`clustered` children of an `actioned` Insight become `archived` (case 104.2); every
Insight's `severity` is recounted, a child's status read under `wiki/lessons/` or in the
archive, a child with no page counted live (case 110); an `open` Insight at 0 becomes
`archived`, an `actioned` one stays (case 104.3); the `rules` of every live Entity is
recounted — the live rules whose `applies_to` names it, in slug order — written when the
list is not empty or the field already stands, History `rules: [...] · cascade` on a change
(case 305.3). No section is derived by the cascade.

No line of the sprint page moves by the script: a milestone item leaves its milestone
only by an `update` of a Case (case 539.1).

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
from guppi.lint import CODE_SPAN
from guppi.materialize import (
    CATEGORIES,
    ITEM_KEYS,
    PREFIXES,
    dump_yaml,
    load_yaml,
    sprint_id,
    units_with,
    yaml_path,
)
from guppi.pages import HISTORY, REF_FIELDS, Page, read_page, slug_of, wiki_root

KEY_ORDER = {
    "rules": [
        "type", "kind", "purpose", "status", "enforcement", "implementation_ref", "governs",
        "render_mode", "parent", "children", "estimates", "applies_to", "deferred_by", "origin",
        "sprint", "created", "tags",
    ],
    "entities": [
        "type", "kind", "purpose", "status", "parent", "children", "estimates", "rules",
        "deferred_by", "code_ref", "origin", "sprint", "created", "tags",
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
        "type", "case", "status", "parent", "children", "create", "update", "delete", "defer",
        "source", "supersedes", "superseded_by", "origin", "sprint", "created", "tags",
    ],
}  # fmt: skip
KINDS = ("create", "update", "delete", "defer")  # a decision page's lists, in this order
SECTION_ORDER = {  # no section derived from a ref field (case 166.2)
    "rules": ["Purpose", "Render", "How it works"],
    "entities": ["Purpose", "How it works", "Milestones", "Backlog", "Closed"],  # 229.1
    "estimates": ["Context", "Criterion", "Method", "Result"],
    "lessons": ["Trigger", "Root cause"],
    "insights": ["Pattern", "Proposal"],
    # Given, When and Criterion: the shapes before 72.4 and 201.2, kept where a page carries them
    "decisions": [
        "Context", "Problem", "Recommend", "Given", "When", "Criterion", "Deferred", "Note",
    ],
}  # fmt: skip
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
RESULT = "## Result"  # a reading's record; a rename leaves it as it is (case 258.1)
REWORD_CATEGORIES = ("rules", "entities", "estimates")  # not the journal, not the records (274.1)
REWORD_FIELDS = ("purpose", "method")
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
    """A slug with a category prefix as `[[slug]]`; a slug without a category prefix, or
    anything else, as it is (case 148.1). `scalar` quotes the brackets."""
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


TICKED_KINDS = ("create", "update", "delete", "defer")
CASE_HEADING = re.compile(r"^#{2,3} Case (\S+)")
ANY_HEADING = re.compile(r"^#{1,6} ")
TASK_LINE = re.compile(r"^- \[ \] (create|update|delete|defer) `([^`]+)`")
READ_LINE = re.compile(r"^- \[ \] read `([^`]+)`")
# A line of a Frontier — the box, the id, the rest — and the separator of its segments;
# `frontier_marks` below and `prespec.check_frontier` read the lines by this one pattern
# (case 360).
FRONTIER_LINE = re.compile(r"^- \[([ x-])\] (\S+)(.*)$")
FRONTIER_SEPARATOR = " · "
DAY = re.compile(r"^\d{4}-\d\d-\d\d$")
SESSION = re.compile(r"^\d{4}$")


LEADING_BLANK = " \t"


def opens_blank(text: str) -> bool:
    """Whether `text` opens with a space or a tab — the one reading of a leading indent of a
    `replace` pair, which `replace_hits` and `indent_added_twice` share (case 543)."""
    return text[:1] in tuple(LEADING_BLANK)


def replace_hits(page: Page, old: str) -> list[tuple[str, re.Match]]:
    """Every hit of `old` in the page's sections but History, whitespace collapsed: the
    tokens of `old` joined by one `\\s+`, so a line break inside the anchor still matches.
    An `old` that opens with a space or a tab also takes every space and tab on the page just
    before its first word, so the indent of `new` replaces them and is not added after them;
    those spaces never make an anchor miss or hit twice (case 543.3). The one matching rule of
    a `replace` pair — `pre-spec` simulates the pairs of a Spec by it before the Spec is
    approved (case 351)."""
    tokens = [re.escape(t) for t in old.split()]
    if not tokens:
        return []
    lead = f"[{LEADING_BLANK}]*" if opens_blank(old) else ""
    pattern = re.compile(lead + r"\s+".join(tokens))
    return [
        (key, m)
        for key, text in page.sections.items()
        if key != HISTORY
        for m in pattern.finditer(text)
    ]


def replace_once(page: Page, old: str, new: str) -> int:
    """The number of hits of `old` in the page; when it is exactly one, `new` takes its
    place — with the spaces and tabs before it when `old` opens with one (case 543.3).
    Anything else changes nothing: an anchor that misses or is not unique fails the entry
    (case 274.1)."""
    hits = replace_hits(page, old)
    if len(hits) == 1:
        key, match = hits[0]
        text = page.sections[key]
        page.sections[key] = text[: match.start()] + new + text[match.end() :]
    return len(hits)


def indent_added_twice(old: str, new: str) -> bool:
    """Whether a `replace` pair adds an indent twice: its `new` opens with a space or a tab
    while its `old` opens with neither, so the page keeps its own indent before the match and
    the indent of `new` stands after it. `pre-spec` reports such a pair, and the Case check
    with it through `judge`; `generate` applies it as before (case 543.4)."""
    return opens_blank(new) and not opens_blank(old)


def tick_read(
    specs: list[Path],
    slug: str,
    skip: set[str] = frozenset(),
    superseded: set[str] = frozenset(),
) -> bool:
    """Case 270.1: in the first of `specs` that holds one, every unticked line
    `- [ ] read `<slug>`` — in any Case, a reading carries no Case — becomes `- [x] …`. One
    reading is of the page, whose Criterion is one, however many Cases of the session
    touched it (case 312).
    Case 280: in the first Spec, the Spec beside the yaml, a line in the section of a Case
    of `skip` — a Case ratified after the reading — is not the reading's line. Case 286: in
    any Spec, a line in the section of a superseded Case is not the reading's line either —
    `superseded` for the first Spec, the marks of the run's entries; for every other Spec
    the marks of the `materialize.yaml` beside it. True when a line was ticked; False when
    no Spec holds one — no error either way.
    Case 326: every live Spec of `raw/` is ticked, not the first that holds a line. A promise
    changed in two sessions leaves a read line in each, and one reading is of the page, so
    the older line has no Case of its own and no later reading would ever reach it. The
    archive is not read: an archived Spec keeps its open line as the record of a task nobody
    performed.
    Case 463: a `delete` of the slug ticks by this same walk, with the same two skips — `skip`
    then holds the Cases ratified after the delete — since no reading of a deleted Estimate
    will ever stand in the ledger. Case 672: so does an `update` that sets the Estimate
    `passed` or `failed` by the person's decision."""
    any_ticked = False
    for position, spec in enumerate(specs):
        if not spec.is_file():
            continue
        skipped = set(skip) | set(superseded) if position == 0 else superseded_beside(spec)
        lines = spec.read_text(encoding="utf-8").split("\n")
        case = ""
        ticked = False
        for index, line in enumerate(lines):
            heading = CASE_HEADING.match(line)
            if heading:
                case = heading.group(1)
                continue
            task = READ_LINE.match(line)
            if task and task.group(1) == slug and case not in skipped:
                lines[index] = "- [x]" + line[len("- [ ]") :]
                ticked = True
        if ticked:
            spec.write_text("\n".join(lines), encoding="utf-8", newline="\n")
            any_ticked = True
    return any_ticked


def closes_by_decision(entry: dict) -> bool:
    """Case 672: an `update` whose `set` gives `status` the value `passed` or `failed` closes
    its Estimate by the person's decision; no reading of it follows, so it ticks the `read`
    lines of its slug as a `delete` does. An `update` that sets `pending`, or no `status`,
    leaves them for the reading."""
    sets = entry.get("set")
    return (
        entry.get("kind") == "update"
        and isinstance(sets, dict)
        and str(sets.get("status")) in ("passed", "failed")
    )


def later_cases(entries: list, line) -> set[str]:
    """Case 280: the Cases whose first decision entry carries a `line` greater than `line`
    — ratified after the reading recorded at that ledger line."""
    first: dict[str, int] = {}
    for entry in entries:
        if not isinstance(entry, dict) or "case" not in entry or "line" not in entry:
            continue
        case = str(entry["case"])
        first[case] = min(first.get(case, int(entry["line"])), int(entry["line"]))
    try:
        reading = int(line)
    except (TypeError, ValueError):
        return set()
    return {case for case, number in first.items() if number > reading}


def superseded_cases(entries: list) -> set[str]:
    """Case 286: the Cases whose entries carry `superseded_by` — their work stands under
    the superseding Case, so their lines are nobody's to tick."""
    return {
        str(entry["case"])
        for entry in entries
        if isinstance(entry, dict) and "case" in entry and entry.get("superseded_by")
    }


def superseded_beside(spec: Path) -> set[str]:
    """Case 286: the superseded Cases of the `materialize.yaml` beside `spec`, read for
    the marks alone; none without a yaml, or with one that does not load."""
    try:
        data = load_yaml(spec.parent / "materialize.yaml")
    except Exception:  # noqa: BLE001 — a yaml that does not load skips nothing
        return set()
    return superseded_cases((data or {}).get("entries") or [])


def raw_specs(project_dir: Path, first: Path | None) -> list[Path]:
    """The `spec.md` beside the yaml first, then every other one under `vault/raw/` — a
    date-level `raw/<date>/spec.md` or a session's `raw/<date>/<HHMM>/spec.md` — oldest
    first by path; nothing from the archive (case 270.1)."""
    raw = project_dir / "vault" / "raw"
    others = sorted(raw.glob("*/spec.md")) + sorted(raw.glob("*/*/spec.md")) if raw.is_dir() else []
    others.sort(key=lambda p: p.relative_to(raw).parts)
    head = [first] if first is not None else []
    return head + [p for p in others if first is None or p.resolve() != first.resolve()]


def tick_spec(spec: Path, case: str, kind: str, slug: str) -> bool:
    """Case 226.1: in `spec`, under the heading `## Case <case>` or `### Case <case>` and
    before the next heading, the first line `- [ ] <kind> `<slug>`` becomes `- [x] …`.
    True when a line was ticked; False when the file, the section or the line is absent —
    no error either way, the entry is applied all the same."""
    if not spec.is_file():
        return False
    lines = spec.read_text(encoding="utf-8").split("\n")
    inside = False
    for index, line in enumerate(lines):
        heading = CASE_HEADING.match(line)
        if heading:
            inside = heading.group(1) == case
            continue
        if ANY_HEADING.match(line):
            inside = False
            continue
        if not inside:
            continue
        task = TASK_LINE.match(line)
        if task and task.group(1) == kind and task.group(2) == slug:
            lines[index] = "- [x]" + line[len("- [ ]") :]
            spec.write_text("\n".join(lines), encoding="utf-8", newline="\n")
            return True
    return False


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


# --- the Frontiers, read by the count of `guppi backlog` ---------------------------------------


def frontiers(project_dir: Path) -> list[tuple[tuple[str, str], Path]]:
    """Every `frontier.md` under `vault/raw/` and `vault/archive/`, newest session first,
    keyed `(date, HHMM)`; a date-level one has an empty HHMM and sorts after the sessions
    of its day, being older (case 354.1)."""
    found: list[tuple[tuple[str, str], Path]] = []
    for root in (project_dir / "vault" / "raw", project_dir / "vault" / "archive"):
        if not root.is_dir():
            continue
        for path in root.rglob("frontier.md"):
            parts = path.relative_to(root).parts[:-1]
            day = next((i for i, part in enumerate(parts) if DAY.match(part)), None)
            if day is None:
                continue
            after = parts[day + 1] if day + 1 < len(parts) else ""
            found.append(((parts[day], after if SESSION.match(after) else ""), path))
    return sorted(found, key=lambda item: item[0], reverse=True)


def frontier_marks(path: Path) -> list[tuple[str, set[str]]]:
    """`(box, slugs)` per line of a Frontier: its box, and the slugs its title — the text
    before the first ` · ` — holds in code spans (case 354.1)."""
    marks: list[tuple[str, set[str]]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = FRONTIER_LINE.match(line)
        if match:
            title = match.group(3).split(FRONTIER_SEPARATOR)[0]
            marks.append((match.group(1), {s.strip("`") for s in CODE_SPAN.findall(title)}))
    return marks


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
        self.spec: Path | None = None  # the Spec beside the yaml, whose page lines are ticked
        self.entries: list = []  # the yaml's entries, for the Cases later than a reading (280)

    # the Spec (case 226.1)

    def tick(self, entry: dict) -> None:
        """The first unticked `- [ ] <kind> `<slug>`` line in the section of the entry's
        Case becomes `- [x]`; a reading — an `estimate` entry, or a `create` with `folded` —
        ticks the first unticked `- [ ] read `<slug>`` line across the Specs of `raw/`
        (270.1); a `delete` entry ticks its page line and, as a reading does, the `read`
        lines of its slug — no reading of a deleted Estimate will stand in the ledger (463);
        so does an `update` that sets an Estimate `passed` or `failed` by the person's
        decision, which no reading follows (672); an `estimate` or a `delete` entry, or such
        an `update`, skips, in the Spec beside the yaml, the Cases whose first decision entry
        stands after it in the ledger (280, 463, 672); all skip, in every
        Spec, the Cases the yaml beside it marks `superseded_by` (286); nothing found — no
        Spec, no section, no line — is no error. Called for an applied entry alone, so a
        failed `delete` ticks nothing."""
        kind = entry.get("kind")
        if self.spec is not None and kind in TICKED_KINDS and "case" in entry:
            tick_spec(self.spec, str(entry["case"]), str(kind), str(entry.get("slug")))
        superseded = superseded_cases(self.entries) if self.spec else set()
        if kind in ("estimate", "delete") or closes_by_decision(entry):
            skip = later_cases(self.entries, entry.get("line")) if self.spec else set()
            tick_read(
                raw_specs(self.project_dir, self.spec), str(entry.get("slug")), skip, superseded
            )
        elif kind == "create" and entry.get("folded"):
            tick_read(
                raw_specs(self.project_dir, self.spec), str(entry.get("slug")), set(), superseded
            )

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
        keys = [k for k in ITEM_KEYS["update"] if k != "slug"]  # one list (case 436.1)
        if not any(entry.get(k) for k in keys):
            print(
                f"generate: {slug}: an update with no content in the Spec; nothing applied",
                file=self.stdout,
            )
            return
        if entry.get("rename"):  # the page moves first; the rest lands on the new file (258.1)
            page = self.rename(page, str(entry["rename"]), self.pointer(entry))
            if page is None:
                return
        if entry.get("reword") and not self.reword_pairs(  # the word changes first (274.1)
            page, entry["reword"], self.pointer(entry)
        ):
            return
        sets = entry.get("set") or {}
        sections = entry.get("sections") or {}
        for key, value in sets.items():
            page.props[key] = value
            if key == "tags":
                self.used_tags.update(as_list(value))
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

    # rename (case 258.1)

    def rename(self, page: Page, new: str, pointer: str | None) -> Page | None:
        """The page moves to `<category>/<new>.md`, History `renamed from`, and every live
        page of `wiki/` that names the old slug — a `[[link]]`, a ref field, the bare slug
        as a word in a body — names the new one; `## History`, `## Result` and `origin`
        keep the old name, they are records. A taken or foreign slug is an error."""
        old = page.slug
        prefix = next((p for p, c in PREFIXES.items() if c == page.category), None)
        if prefix is None or not new.startswith(prefix):
            self.error(old, f"rename: {new} is not a {page.category} slug")
            return None
        if self.find(new) is not None:
            self.error(old, f"rename: {new} is taken")
            return None
        if page.path.parent != self.wiki / page.category:
            self.error(old, "rename: the page is in the archive; bring it back first")
            return None
        target = self.path(page.category, new)
        page.path.unlink()
        page.slug, page.path = new, target
        self.reword(page, old, new)  # its own body names itself by the new slug too
        self.history(page, f"renamed from `{old}`", pointer)
        self.save(page)
        self.retarget(old, new, pointer, skip=new)
        return page

    @staticmethod
    def reword(page: Page, old: str, new: str) -> bool:
        """The old slug as a whole word becomes the new one in the ref fields and in every
        section but History and Result; True when anything changed."""
        word = re.compile(rf"(?<![\w-]){re.escape(old)}(?![\w-])")
        changed = False
        for key in REF_FIELDS:
            value = page.props.get(key)
            if isinstance(value, list) and old in value:
                page.props[key] = [new if v == old else v for v in value]
                changed = True
            elif value == old:
                page.props[key] = new
                changed = True
        for name, text in page.sections.items():
            if name in (HISTORY, RESULT) or not word.search(text):
                continue
            page.sections[name] = word.sub(new, text)
            changed = True
        return changed

    def retarget(self, old: str, new: str, pointer: str | None, skip: str) -> None:
        """Every live page but `skip` is reworded; a page that changed gets History
        `ref old → new`, a Decision page none — its lists are a record kept readable,
        not a change of the decision."""
        for category in CATEGORIES:
            folder = self.wiki / category
            if not folder.is_dir():
                continue
            for path in sorted(folder.glob("*.md")):
                if path.stem == skip or path.stem == "schema":
                    continue
                other = read_page(path, category)
                if other.error or not self.reword(other, old, new):
                    continue
                if category != "decisions":
                    self.history(other, f"ref `{old}` → `{new}`", pointer)
                self.written[other.slug] = category  # counted, History or not
                self.save(other)

    # reword (case 274.1)

    @staticmethod
    def owner_text(page: Page) -> str:
        """What a rule owns, lowercased: its `purpose`, `governs`, `implementation_ref`, its
        Purpose and its Render — the `new` of a pair must stand there (274.1)."""
        parts = [str(page.props.get(k, "")) for k in ("purpose", "governs", "implementation_ref")]
        parts += [page.sections.get(name, "") for name in ("## Purpose", "## Render")]
        return "\n".join(parts).lower()

    @staticmethod
    def reword_text(page: Page, old: str, new: str) -> int:
        """`old` as a whole word becomes `new` in `purpose`, `method` and every section but
        History and Result; the number of replacements."""
        word = re.compile(rf"(?<![\w-]){re.escape(old)}(?![\w-])")
        count = 0
        for key in REWORD_FIELDS:
            value = page.props.get(key)
            if isinstance(value, str):
                page.props[key], n = word.subn(new, value)
                count += n
        for name, text in page.sections.items():
            if name in (HISTORY, RESULT):
                continue
            page.sections[name], n = word.subn(new, text)
            count += n
        return count

    def reword_pairs(self, owner: Page, pairs, pointer: str | None) -> bool:
        """Every pair of `reword` replaced as a whole word on every live rule, entity and
        estimate, the owner included; one History line per page touched, one stdout line
        with the count. A pair with no hit, or with a `new` the owner's text lacks (compared
        without regard to case), fails the entry before anything is written (274.1)."""
        shape = isinstance(pairs, list) and all(
            isinstance(p, dict) and p.get("old") and p.get("new") for p in pairs
        )
        if not shape:
            self.error(owner.slug, "reword: expected a list of old/new pairs")
            return False
        owned = self.owner_text(owner)
        for pair in pairs:
            if str(pair["new"]).lower() not in owned:
                self.error(owner.slug, f"reword: `{pair['new']}` is not in the owner's text")
                return False
        pages = [owner]
        for category in REWORD_CATEGORIES:
            folder = self.wiki / category
            if not folder.is_dir():
                continue
            for path in sorted(folder.glob("*.md")):
                if path.stem == "schema" or (category, path.stem) == (owner.category, owner.slug):
                    continue
                other = read_page(path, category)
                if not other.error:
                    pages.append(other)
        for pair in pairs:  # every pair must hit before any is written
            word = re.compile(rf"(?<![\w-]){re.escape(str(pair['old']))}(?![\w-])")
            hit = any(
                word.search(str(page.props.get(k) or "")) for page in pages for k in REWORD_FIELDS
            ) or any(
                word.search(text)
                for page in pages
                for name, text in page.sections.items()
                if name not in (HISTORY, RESULT)
            )
            if not hit:
                self.error(owner.slug, f"reword: `{pair['old']}` has no hit on a live page")
                return False
        for pair in pairs:
            old, new = str(pair["old"]), str(pair["new"])
            for page in pages:
                count = self.reword_text(page, old, new)
                if not count:
                    continue
                self.history(page, f"reworded: `{old}` → `{new}`", pointer)
                print(
                    f"generate: reword `{old}` → `{new}`: {page.category}/{page.slug} ({count})",
                    file=self.stdout,
                )
                if page is not owner:  # the owner is saved with the rest of its update
                    self.save(page)
        return True

    def replace(self, page: Page, old: str, new: str) -> bool:
        return replace_once(page, old, new) == 1

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

    def clear_deferred_by(self, earlier: Page, by: str, named: set[str]) -> None:
        """A `supersedes` of a decision that deferred pages: each target in the earlier
        page's `defer` list that a decision line of the superseding Case names drops it
        from `deferred_by`, an empty list is dropped (cases 52.3, 59.4); a target the Case
        does not name keeps it and stays in the backlog (case 467.3)."""
        for slug in as_list(earlier.props.get("defer")):
            if slug not in named:
                continue
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

    def decision(
        self,
        record: dict,
        deferred: list[tuple[str, str]] | None = None,
        children: list[dict] | None = None,
    ) -> None:
        """The Decision page of a Case; `deferred` is the `(slug, purpose)` of every `defer`
        line of the Case, in ledger order, written under `## Deferred` (case 186.1).
        `children`, on the page of a Case with sub-cases, the records of its sub-cases, whose
        tags — theirs and their targets' — its page takes (case 544.7)."""
        slug = record["decision"]
        path = self.path("decisions", slug)
        if path.exists():
            return
        text = record.get("case_text") or {}
        tags = list(record.get("tags") or [])
        targets = record.get("targets") or []
        tag_targets = []
        for child in children or []:
            tags += [t for t in child.get("tags") or [] if t not in tags]
            tag_targets += child.get("targets") or []
        for target in [*targets, *tag_targets]:
            if target.get("category") in CATEGORIES:
                page = self.find(str(target.get("slug")))
                for tag in as_list(page.props.get("tags")) if page else []:
                    if tag not in tags:
                        tags.append(tag)
        props: dict = {"type": "decision", "case": str(record["case"]), "status": "current"}
        if record.get("parent"):  # the page of a sub-case names its parent's (case 544.7)
            props["parent"] = str(record["parent"])
        if record.get("children"):  # in place of the kind lists (case 544.7)
            props["children"] = [str(c) for c in record["children"]]
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
        sections = {}  # no When, no Criterion list: the contract lives on the Estimate (201.2)
        short = not text.get("given") and not record.get("children")
        if text.get("context") and short:  # the short form: no Case file (513, 544.7)
            sections["## Context"] = text["context"]
        if text.get("problem") and not record.get("parent"):  # the parent's only (544.7)
            sections["## Problem"] = text["problem"]
        if text.get("recommend"):  # the choices of the rounds (case 544.7)
            sections["## Recommend"] = text["recommend"]
        if not text and record.get("superseded_by"):  # gone from the Spec (299.4)
            by = ", ".join(f"[[{s}]]" for s in as_list(record["superseded_by"]))
            sections["## Context"] = (
                f"Superseded by {by} in its own session, before the Spec was approved; "
                "the Case left the Spec (case 299)."
            )
            sections["## Problem"] = f"Decided under {by}."
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
            self.clear_deferred_by(other, slug, {str(t.get("slug")) for t in targets})
            self.supersede_children(other, slug)

    def supersede_children(self, parent: Page, slug: str) -> None:
        """Case 660.3: the tag that supersedes a Case supersedes its sub-cases too — each page
        in the `children` of `parent`, at any depth, that stands `current` becomes
        `superseded`, takes `slug` into its `superseded_by` and one History line, whatever
        the run that wrote it; a child page `archived` or already `superseded` is left as it
        stands, the round trip of `decision-case-469` kept off it. No `deferred_by` is
        cleared through a child: only the pages the record's `supersedes` names clear theirs
        (case 467.3)."""
        for name in as_list(parent.props.get("children")):
            child = self.find(str(name).strip('[]"'))
            if child is None or child.props.get("status") != "current":
                continue
            child.props["status"] = "superseded"
            done = as_list(child.props.get("superseded_by"))
            if slug not in done:
                child.props["superseded_by"] = done + [slug]
                self.history(child, f"superseded by {slug}", f"[[{slug}]]")
            self.save(child)
            self.supersede_children(child, slug)

    # after all entries

    def recount_rules(self) -> None:
        """Case 305.3: the `rules` of every live Entity is the live rules whose
        `applies_to` names it, in slug order — the backlink of the edge Rule → Entity.
        The field is written when the list is not empty or already stands; an empty list
        on a page without the field writes nothing. An archived rule gives no edge; an
        `applies_to` on a slug with no page is left to lint."""
        guards: dict[str, list[str]] = {}
        for path in sorted((self.wiki / "rules").glob("*.md")):
            if path.stem == "schema":
                continue
            rule = read_page(path, "rules")
            if rule.error:
                continue
            for slug in as_list(rule.props.get("applies_to")):
                guards.setdefault(slug, []).append(rule.slug)
        for path in sorted((self.wiki / "entities").glob("*.md")):
            if path.stem == "schema":
                continue
            page = read_page(path, "entities")
            if page.error:
                continue
            expected = sorted(guards.get(page.slug, []))
            if "rules" not in page.props and not expected:
                continue
            current = as_list(page.props.get("rules"))
            if current == expected:
                continue
            page.props["rules"] = expected
            self.history(page, f"rules: [{', '.join(expected)}]", "cascade")
            self.save(page)

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
                # Case 328: a slug with no page is not counted, and neither is an Estimate
                # standing `archived` — a `delete` of this run retired it and its file waits
                # under `wiki/estimates/` until `cleanup`, which runs after this script.
                own = [e for e in own if e is not None and str(e.props.get("status")) != "archived"]
                if not own:
                    continue
                all_passed = all(str(e.props.get("status")) == "passed" for e in own)
                before = str(page.props["status"])
                after = "built" if all_passed else "draft"
                if before != after:
                    page.props["status"] = after
                    self.history(page, f"status: {before} → {after}", "cascade")
                    self.save(page)
        self.recount_rules()
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
    vault: Vault,
    record: dict,
    stamp: str,
    deferred: list[tuple[str, str]] | None = None,
    records: dict | None = None,
) -> None:
    """The Decision page of one record; with `records`, the Case id → record of the unit, the
    page of its parent first — a Case with sub-cases gets its page before theirs — and the
    page of a record with `children` takes the tags of their targets (case 544.7)."""
    if record.get("applied"):
        return
    records = records or {}
    parent = str(record.get("parent") or "").removeprefix("decision-case-")
    if parent in records:
        apply_decision(vault, records[parent], stamp, None, records)
    children = [
        records[str(child).removeprefix("decision-case-")]
        for child in record.get("children") or []
        if str(child).removeprefix("decision-case-") in records
    ]
    before = len(vault.errors)
    try:
        vault.decision(record, deferred, children)
    except Exception as exc:  # noqa: BLE001
        vault.error(record.get("decision", "?"), f"{type(exc).__name__}: {exc}")
    if len(vault.errors) == before:
        record["applied"] = stamp
        record.pop("failed", None)
    else:
        record["failed"] = vault.errors[-1]
    vault.write_log()


def repeated(entries: list, entry: dict) -> dict | None:
    """The applied entry of the same yaml that `entry` repeats: the same `case`, `kind` and
    `slug`, for a `create`, `update`, `delete` or `defer` (case 514). An `estimate` or a
    `lesson` entry carries no `case` and is never a repeat."""
    if entry.get("kind") not in KINDS or "case" not in entry:
        return None
    key = (str(entry["case"]), entry["kind"], str(entry.get("slug")))
    for other in entries:
        if other is entry or not isinstance(other, dict) or not other.get("applied"):
            continue
        if (
            "case" in other
            and (str(other["case"]), other.get("kind"), str(other.get("slug"))) == key
        ):
            return other
    return None


def apply(vault: Vault, data: dict) -> None:
    stamp = vault.now.strftime("%H:%M:%S")
    records = {str(r.get("case")): r for r in data.get("decisions") or []}
    deferred = deferred_of(data)
    vault.entries = data.get("entries") or []
    for entry in vault.entries:
        if not isinstance(entry, dict) or entry.get("applied"):
            continue
        if entry.get("superseded_by"):  # a later Case did its work; only the Decision page
            if "case" in entry and str(entry["case"]) in records:  # of its Case is written,
                case = str(entry["case"])
                apply_decision(vault, records[case], stamp, deferred.get(case), records)  # before
            continue  # the superseding one marks it (case 151)
        if "kind" not in entry and entry.get("failed"):  # a line materialize could not lift
            vault.error(
                f"line {entry.get('line', '?')}", f"not lifted by materialize; {entry['failed']}"
            )
            continue  # the mark stays as materialize wrote it (case 142.2)
        if "case" in entry and str(entry["case"]) in records:  # the Decision page first (52.4)
            case = str(entry["case"])
            apply_decision(vault, records[case], stamp, deferred.get(case), records)
        kind = entry.get("kind")
        first = repeated(vault.entries, entry)
        if first is not None:  # a Case ratified again, its line written again (case 514)
            print(
                f"generate: {entry.get('slug')}: line {entry.get('line', '?')} repeats line "
                f"{first.get('line', '?')} of case {entry['case']}; nothing applied",
                file=vault.stdout,
            )
            entry["applied"] = stamp
            entry.pop("failed", None)
            continue  # no tick: the Spec's lines are closed by the entry that did the work (522)
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
            vault.tick(entry)  # the Spec's page line, once the entry applied (226.1)
        else:
            entry["failed"] = vault.errors[-1]
        vault.write_log()
    vault.settle_backlinks()
    vault.write_log()
    for record in data.get("decisions") or []:
        apply_decision(vault, record, stamp, deferred.get(str(record.get("case"))), records)
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
    vault.spec = path.parent / "spec.md"  # the Spec beside the yaml (226.1)
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
