"""`guppi materialize [--date YYYY-MM-DD] [--show]` — the ledger and the Spec as one yaml.

Reads one unit at a time (case 103.2). A session folder `vault/raw/<date>/<HHMM>/` holding
a `ledger.md` is a unit: its ledger, its own `spec.md` and nothing else, written to
`vault/raw/<date>/<HHMM>/materialize.yaml`, the `origin` of every entry
`raw/<date>/<HHMM>/ledger.md#…`. A date-level `vault/raw/<date>/ledger.md` is a unit read
as before: the ledger and every Spec of the date — `vault/raw/<date>/spec.md` when the date
has one, then `vault/raw/<date>/<HHMM>/spec.md` in folder order — written to
`vault/raw/<date>/materialize.yaml` with the date form of `origin` (the shape before case
103; a date-level Spec on the dates before case 73). Either way the yaml
holds one entry per record line of the ledger, in ledger order, with its route computed by
the Routing Table below and its content lifted from the `then` block of its Case in the Spec. The yaml's `spec` field lists the
files read and each decision entry names the file its Case was found in; a Case heading
found in two files stops the walk with exit 1 (case 73.5). One decision entry per Case; a
sub-case's `context` and `given` are its own when present and its parent's otherwise, its
`problem`, `recommend` and `when` never, and its record carries `parent`, the `decision` of its
parent, and needs no `problem`. A Case whose sub-cases have decision lines in the unit gets one
decision record of its own: its `decision` and `origin` by its id, `case_text` with its
`context`, `problem`, `recommend` and its `given` when it has one, `children` the `decision` of
each sub-case in ledger order, `tags` the union of theirs, and no `targets` (case 544.6). What
is missing is named (`incomplete`), never invented. The `type` of a `create` that writes none
is its category's, by `SINGULAR`, the one map `generate` and pre-spec read too, and is never
`incomplete` (`fill_type`) (case 748.1); the other fields of `REQUIRED` a `create` lacks are
judged by `create_lacks`, which pre-spec reports by too (case 748.2).
The yaml's `sprint` is the first `## <id>` heading of `vault/wiki/sprint.md`, but in a unit
whose ledger holds a `create` decision line of `entity-sprint-<id>` it is that `<id>`, so the
session that opens a sprint after the close of the last one belongs to the new sprint
(`opened_sprint`) (case 628.3).
A line the grammar does not parse goes under `unparsed`. A line whose lift raises — a `then`
item of an unexpected shape, any error while the entry is built — becomes an entry `{line,
text, failed}` without `kind`, reported on stderr as `materialize: line N: <message>`; the
other lines are lifted, the yaml is written, the unit exits 1 and the walk goes on to the
next unit; on the next run such an entry is lifted again and replaced when the lift succeeds.
An existing entry the script cannot read — not a mapping, or a mapping with none of `line`,
`derived`, `librarian` — is left as it is and named on stderr (cases 142.1, 142.4, 158); the
librarian's own entries carry `librarian` and no `line`. The `then` item is found by `slug`
alone (case 320). `new_tags` declared in the `then` block of any Case, with decision lines or
without, reach the yaml once each.

The Routing Table (case 364.1). Every ratified Case produces its Decision page
`decision-case-<N>`, written by `generate` before the effects so that their History lines
can name it (case 52.4), and an effect on each target:

    decision  ref                   effect on the target
    create    none                  the vault asked first; nothing found → a new top-level page
    create    parent                a new child page, added to the parent's `children`
    create    target (an Estimate)  a new Estimate, added to the target's `estimates`; its own
                                    line and its own item, the Criterion from the Case (193)
    update    target                the target's fields; with `rename` the page moves first and
                                    every link to it in the live pages follows (case 258.1)
    update    none                  invalid: the Case should have been a `create`
    delete    target                impact analysis in the Case → archived by the librarian →
                                    `origin` kept
    delete    none, no category     outside the vault: the Decision page records it, `generate`
                                    marks it applied, nothing to archive
    defer     existing              the Decision's slug appended to the target's `deferred_by`,
                                    shown in its index line (case 52.3)
    defer     none                  a minimal placeholder page, born with `deferred_by`, for a
                                    rule or an entity only; an entry of any other kind with
                                    no page by `defer_writes_no_page` fails in `generate`
                                    (cases 783, 786)

The category of a slug comes from its prefix, which pre-spec guards; a slug with no prefix is
`unknown` (case 320). A `{supersedes:case N}` makes the earlier decision `superseded`, and
`generate` takes its slug out of a target's `deferred_by` under the condition that
`rule-case-protocol` sets (cases 52.3, 549).

No Estimate is derived (cases 189, 194.1). An Estimate has its own ledger line and its own
entry; the `ref` of the line is the Estimate itself. Its Criterion is the `when` and
`then` of its Case, verbatim with their operands, as `When:`, `Then:` — never its `given`,
the frame of the Case, which stays in the decision record (case 378.2) — lifted into the
entry's `sections.Criterion`, the shape `generate` applies as a whole replacement. A Criterion the item wrote under
`sections` stands. An Estimate `update` also carries `set: {status: pending}` unless the
item set a status itself. An `update` item that names a part of the page — `set` without
`status`, a `replace` pair, a section other than `Criterion` — and writes no Criterion
changes that part alone: nothing is lifted and no status is set; a pair whose `old` stands
in the page's `## Criterion` is `incomplete: [criterion]` — a Criterion changes only whole
(case 378.4). An `update` item that carries `change` alone names its History: it lifts
nothing and sets no status, and `generate` writes its History line; only `set.status` or a
Criterion written under `sections` replaces the Criterion (case 588.2). An Estimate `create` keeps `kind`, `purpose`, `method` and
`tags` as fields — a `ref` on the item is the entry's `ref`, never a page field (case 201.1);
`## Context` and `## Method` are not written, and a `context` key of the
old shape is dropped; a `criterion` key of the old shape goes to `sections.Criterion`. The
keys `method`, `contract`, `estimate_slug`, `estimate_kind` on a rule's or entity's item
are no keys of their own: like any key the schema does not name, they go under `unknown`
(the shape before case 189; case 440). A line with `{supersedes:case
N}` marks every entry carrying `case: N` `superseded_by`, whatever its kind (case 175), and
every entry of a sub-case of N at any depth, judged by `in_family` — the one reading of the
tag that the Spec hook, `prespec` and the clash check of `casecheck` import (case 660.2); a
tag on N.M marks N.M and its own sub-cases only; a
line may carry several such blocks side by side, one per Case, and each Case is marked
(case 429). The marks go to
whichever unit's yaml holds them — this one or any other under `raw/`, written with that
mark only (case 130.2); nothing is derived from it. A Case superseded in its own session
leaves the Spec (case 299.1): its entries, marked `superseded_by` while no heading of its
number stands in the Spec, carry no `incomplete: [then]`, and its `decisions` record no
`case_text` and no missing section — the mark alone is its completeness (case 299.3). A
nested `estimate` in an older Spec becomes its own `create` entry, for a line with its slug.

The fields of an entry, each with its writer. From the ledger line: `case`, `kind`
(`create`, `update`, `delete`, `defer`, `estimate`, `lesson`), `category` (from the slug
prefix; a slug with no category prefix is `unknown` and `incomplete: [category]`) (the file
route removed by case 320), `slug`, `ref`, `source`, `supersedes` (a list, one Case per
`{supersedes:case N}` block; one value in an older yaml) (case 429), `tags`, `addresses`
(the lesson slugs of a decision line's `{addresses:...}` marks, one per mark) (case 284.2),
`origin` (`raw/<unit>/ledger.md#case-N`; a lesson `#L<n>`), `line`, `text`, `decision`
(`decision-case-<N>`). From the `then` block: `fields`, `sections` (`Criterion` lifted from
the Case when the item wrote none), `replace`, `change`, `rename` (an update's new slug,
carried as written; `generate` checks it) (case 258.2), `reword` (a list of `{old, new}`
pairs, carried as written; a mapping or a scalar under it is `incomplete: [reword]`) (case
274.3), `impact`, `incomplete` (what the block lacks: a required field, `then`, `change`,
`criterion`, `purpose`, `source`, `reword`; `comment` on each decision entry of a Case whose
fence tagged `then` holds a YAML comment by `then_comments`, which `guppi ratified` imports
— the entry keeps what YAML read, and `generate` still applies it; `addresses` when the mark
names no lesson of this unit; `addressed_by` on a lesson whose mark names a Case with no
decision line earlier in the unit, judged by `marks_without_decision`, which the ledger hook
calls too) (cases 521.2, 284.3, 377.3, 497.1), `unknown` (a key of a `create` or `defer`
item that the category's `schema.yaml` names as no field and that is not structural — never
lifted into `fields`; the `type` and `purpose` of a `defer` are its own keys and reach
`fields` whatever the target's category, an Insight's too; and nothing is filtered at all
for a category whose `rule-<category>-schema` this unit creates or updates — the
`schema.yaml` on disk catches up only at the render after `generate`) (cases 214.1, 266,
308.2), `exists` (a create whose page is on disk with an `origin` carrying this line's
`#case-N`; a defer whose page exists) (case 105.2). Set by this script: `set`
(`status: pending` on an Estimate update), and `status`, `result`, `folded` of a reading
folded into the live create of its slug — never into one already applied or marked
`superseded_by`, and a `{supersedes}` moves the readings of the create it marks to the live
create of the slug, or makes each an `estimate` entry of its own (case 309); `superseded_by` from a later `{supersedes}` in any unit — a list of
each Case whose line retires the entry, in the order the lines are lifted, with no Case
twice; one value in an older yaml, read as a list of one by `cases_of` and appended to by
the next mark (case 776) — an `estimate` entry carries no
`case`, so no `{supersedes}` reaches it: a reading that must not apply is retired only by a
ratified Case, whose one-off migration writes `superseded_by` as a list that holds the
number of that Case and removes the entry's `failed` (case 427); `addressed_by`
(`decision-case-<N>`) on a lesson entry a decision line of the same unit marked with
`{addresses:<its slug>}`, or whose own line carries `{addressed_by:case N}` after a decision
line of Case N — one function sets it for both marks, at the entry's level, never a page
field (cases 284.3, 377.3); `failed`
from a lift that raised. Kept from an older shape on entries already written: `derived`,
`criterion_block`, `case_removed` (the shape before case 189). Set by `guppi generate`: `applied` (the time
applied) and `failed` (the error). Set by the librarian: `near`, and `librarian` with the
value `merged` or `synthesis` (`rule-documentation`). The decision record of a Case:
`case`, `decision`, `origin`, `targets` (one per line: `kind`, `category`, `slug`, and
`path`, `ref`, `source` when present), `tags`, `case_text`, `spec`, `supersedes`,
`superseded_by`, `incomplete`, `parent` on a sub-case and `children` on its parent (case
544.6). A key the code writes and this list does not name is a
finding of the reading of `estimate-materialize-assembles`.

The fence (case 444.1). A line opens a fence when, after at most three spaces of indent inside
the block it stands in — a quote, a sub-point of `tasks` — it starts with a run of three or
more backticks or three or more tildes; the fence closes only on a line of the same character
whose run is at least as long, with nothing after the run but spaces, as CommonMark reads it.
`fence_opening` and `closes_fence` are the one judgment: `then_blocks`, `tagged_blocks`,
`quoted_sections` and `criterion_text` here, `fenced_value` of `guppi/ratified.py`,
`plan_prose` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py` and
`ledger_lines` of `guppi/ledger.py` judge by them. `quoted_sections` is the one reader of the
sections of a Case; `guppi/ratified.py` and `guppi/casecheck.py` import it (case 462).
`fence_breaks`, built on the two, gives each break of a fence in the text of one section — a
line inside a fence with a full run and text after it, and a fence open at the end — for
`check_pairs` of `guppi/prespec.py` and the class `fence` of `guppi/lint.py` (case 487.1). `fence_for` gives
the fence a written block takes: backticks one longer than the longest run of backticks that
opens a line inside it, three at the least (case 444.2).

An existing yaml is extended with the lines it does not hold and never rewritten. Without
`--date` the script walks every unit under `vault/raw/` — dates ascending, the date-level
ledger of a date first, then its sessions in folder order — so a line written after the
librarian's commit of its unit is picked up by the next run; `--date` walks the units of
that date; an error on one unit stops the walk with exit 1. A unit whose folder holds
`carry.md` — the mark `/carry` leaves on a session whose Spec is ratified and whose work
is not done — is passed by with one line on stdout: no yaml is written or extended for it,
and its `applied` or `failed` state is not touched (case 190.3). With `--show` (case 76)
the same walk prints to stdout the yaml each unit would be written with, one document per
unit, `---` between two, and writes nothing under `raw/`. Rule page:
`vault/wiki/rules/rule-materialize.md`.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

from guppi.event import project_root
from guppi.ledger import SPRINT_PAGE, is_sprint_page
from guppi.ledger import body as line_body
from guppi.pages import slug_of

RECORD = re.compile(r"^- (?:\d\d:\d\d:\d\d )?(decision|estimate|lesson)(\[.*)$")
BRACKETS = re.compile(r"\[([^\]]*)\]")
BRACES = re.compile(r"\{(\w+):([^}]*)\}")
HEADING = re.compile(r"^#{1,4} (.*)$")
CASE_HEADING = re.compile(r"^#{2,4} Case (\S+)")
FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
FENCE_CLOSE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*$")
QUOTE = re.compile(r"^> ?(.*)$")
SECTION_START = re.compile(r"^\*\*(\w+):\*\*\s*(.*)$")
DECISION_KINDS = ("create", "update", "delete", "defer")
PREFIXES = {
    "rule-": "rules",
    "entity-": "entities",
    "estimate-": "estimates",
    "lesson-": "lessons",
    "insight-": "insights",
    "decision-": "decisions",
}
CATEGORIES = ("entities", "rules", "estimates", "lessons", "insights", "decisions")
SCHEMA_RULE = re.compile(r"^rule-([a-z]+)-schema$")
REQUIRED = {
    "rules": ("type", "kind", "purpose", "tags"),
    "entities": ("type", "kind", "purpose", "tags"),
    "estimates": ("kind", "purpose", "method"),  # the Criterion comes from the Case (194.1)
    "insights": ("pattern", "children", "tags"),
}
# The type of a page of each category, the one map the lift, `generate` and pre-spec read
# (case 748.1): a `create` that writes no `type` takes it from here, never `incomplete`.
SINGULAR = {
    "entities": "entity",
    "rules": "rule",
    "estimates": "estimate",
    "lessons": "lesson",
    "insights": "insight",
    "decisions": "decision",
}
CASE_SECTIONS = ("context", "problem", "recommend", "given", "when", "then", "ratification")
# A sub-case reads these from its parent, never `problem`, `recommend` or `when` (case 544.6).
INHERITED = ("context", "given")
# The story of a parent Case its own record carries (case 544.6).
PARENT_TEXT = ("context", "problem", "recommend", "given")
CRITERION_SECTIONS = ("when", "then")  # the Criterion of an Estimate, never `given` (378.2)
SESSION_FOLDER = re.compile(r"^\d{4}$")  # raw/<date>/<HHMM>/, one session's Spec (case 73)


class MaterializeError(Exception):
    pass


# --- the ledger ---------------------------------------------------------------------


def _past_brackets(text: str, count: int) -> str | None:
    """`text` past its first `count` brackets, spaces between them allowed, or None when a
    bracket is not where it should be (case 552.1)."""
    for _ in range(count):
        text = text.lstrip()
        match = BRACKETS.match(text)
        if not match:
            return None
        text = text[match.end() :]
    return text


def parse_line(text: str) -> dict | None:
    """The record of one ledger line, or None when the grammar does not match. A space
    between two brackets is read as none, for every kind of line, and a line it cannot read
    gives None, never an error (case 552.1)."""
    match = RECORD.match(text.rstrip())
    if not match:
        return None
    kind, rest = match.groups()
    heads = BRACKETS.findall(rest)
    if not heads:
        return None
    tail = rest[BRACKETS.search(rest).start() :]
    if kind == "decision":
        if len(heads) < 3 or not heads[0].startswith("case "):
            return None
        pairs = BRACES.findall(tail)
        options = {k: v.strip() for k, v in pairs}
        if heads[1] not in DECISION_KINDS:
            return None
        return {
            "record": "decision",
            "case": heads[0][5:].strip(),
            "kind": heads[1],
            "slug": heads[2].strip(),
            "ref": options.get("ref"),
            "source": options.get("source"),
            # one block per Case it supersedes, so the key may repeat (case 429)
            "supersedes": [_case_of(v) for k, v in pairs if k == "supersedes" and v.strip()],
            "tags": _tags(options.get("tags")),
            # one mark per lesson the Case closes, so the key may repeat (case 284.2)
            "addresses": [v.strip() for k, v in pairs if k == "addresses" and v.strip()],
        }
    if kind == "estimate":
        if len(heads) < 2 or heads[1] not in ("passed", "failed"):
            return None
        after = _past_brackets(tail, 2)
        if after is None:
            return None
        return {
            "record": "estimate",
            "slug": heads[0].strip(),
            "status": heads[1],
            "result": after.strip(),
        }
    if len(heads) < 2 or heads[0] not in ("error", "knowledge"):
        return None
    after = _past_brackets(tail, 2)
    if after is None:
        return None
    options = {k: v.strip() for k, v in BRACES.findall(after.split(" trigger:", 1)[0])}
    after = after[after.find("trigger:") :] if "trigger:" in after else after.strip()
    trigger, _, root_cause = after.partition("root_cause:")
    trigger = trigger.strip()
    if trigger.startswith("trigger:"):
        trigger = trigger[len("trigger:") :].strip()
    return {
        "record": "lesson",
        "kind": heads[0],
        "slug": heads[1].strip(),
        "trigger": trigger,
        "root_cause": root_cause.strip(),
        "tags": _tags(options.get("tags")),
        "source": options.get("source"),
        "addressed_by": _case_of(options.get("addressed_by")),  # written after its fix (377.3)
    }


def _case_of(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    return value[5:].strip() if value.startswith("case ") else value


def marks_without_decision(lines: list[str]) -> list[int]:
    """The index of each lesson line among `lines` whose `{addressed_by:case N}` has no
    decision line of Case N before it (case 497.1). The one judgment of the mark, read over
    the lines in their order by `parse_line`, a line it does not read skipped: `lift_line`
    names such a lesson `incomplete: [addressed_by]` over the unit's ledger, and the ledger
    hook `guppi ledger` refuses such a fresh line over the session's ledger followed by the
    lines of its `Stop`. A Case with sub-cases has no decision line of its own, so a mark
    that names the parent never has one."""
    seen: set[str] = set()
    orphans: list[int] = []
    for index, line in enumerate(lines):
        record = parse_line(line)
        if record is None:
            continue
        if record["record"] == "decision":
            seen.add(record["case"])
        elif record["record"] == "lesson":
            mark = record.get("addressed_by")
            if mark and mark not in seen:
                orphans.append(index)
    return orphans


def unlinked_lessons(lines: list[str]) -> list[int]:
    """The index of each lesson line among `lines` that no mark links to a Case (case 685.1):
    the line carries no `{addressed_by:...}`, no `lesson[<slug>]` line of the same slug
    carries one, and no decision line after it carries `{addresses:<slug>}`. The one judgment
    of the link, read over the lines in their order by `parse_line`, a line it does not read
    skipped, beside `marks_without_decision`, the judgment of the other mark: `lift_line`
    links such a lesson to no Case, and the ledger hook `guppi ledger` reminds the agent of
    it after the fresh decision lines that follow it."""
    records = [parse_line(line) for line in lines]
    marked = {r["slug"] for r in records if r and r["record"] == "lesson" and r.get("addressed_by")}
    unlinked: list[int] = []
    for index, record in enumerate(records):
        if record is None or record["record"] != "lesson" or record["slug"] in marked:
            continue
        if any(
            later and later["record"] == "decision" and record["slug"] in later["addresses"]
            for later in records[index + 1 :]
        ):
            continue
        unlinked.append(index)
    return unlinked


def cases_of(value) -> list[str]:
    """The Cases an entry's `supersedes` or `superseded_by` names: a list, or one value in an
    older yaml (cases 429, 776)."""
    if not value:
        return []
    return [str(v) for v in value] if isinstance(value, list) else [str(value)]


def _tags(value: str | None) -> list[str]:
    if not value:
        return []
    return [t.strip() for t in value.split(",") if t.strip()]


def category_of(slug: str) -> str | None:
    for prefix, category in PREFIXES.items():
        if slug.startswith(prefix):
            return category
    return None


def schema_changed(ledger: list) -> set[str]:
    """The categories whose `rule-<category>-schema` this unit creates or updates (case
    308.2). A `create` of such a category is lifted whole, no `unknown`: the `schema.yaml`
    on disk catches up only at the render after `generate`. `ledger` holds lines or records
    `parse_line` made of them (case 436.1)."""
    out: set[str] = set()
    for line in ledger:
        if isinstance(line, dict):
            record = line
        elif line.startswith("- "):
            record = parse_line(line)
        else:
            continue
        if record is None or record.get("record") != "decision":
            continue
        match = SCHEMA_RULE.match(str(record.get("slug") or ""))
        if match and match.group(1) in CATEGORIES:
            out.add(match.group(1))
    return out


# --- the Spec -----------------------------------------------------------------------


def split_cases(spec: str) -> dict[str, list[str]]:
    """Case id → the lines under its heading, up to the next heading of any level."""
    cases: dict[str, list[str]] = {}
    current: str | None = None
    for line in spec.splitlines():
        heading = HEADING.match(line)
        if heading:
            case = CASE_HEADING.match(line)
            current = case.group(1).rstrip(":") if case else None
            if current is not None:
                cases.setdefault(current, [])
            continue
        if current is not None:
            cases[current].append(line)
    return cases


def is_session(unit: str) -> bool:
    """A unit is `<date>`, a date-level ledger (the shape before case 103), or
    `<date>/<HHMM>` (a session folder with its own ledger)."""
    return "/" in unit


def spec_files(project_dir: Path, unit: str) -> list[Path]:
    """The Specs of a unit: a session's own `spec.md` alone (case 103.2); for a date-level
    unit `raw/<date>/spec.md` when it exists, then each `raw/<date>/<HHMM>/spec.md` in
    folder order (case 73.5)."""
    raw = project_dir / "vault" / "raw" / unit
    if is_session(unit):
        return [raw / "spec.md"] if (raw / "spec.md").is_file() else []
    files = [raw / "spec.md"] if (raw / "spec.md").is_file() else []
    if raw.is_dir():
        folders = sorted(p for p in raw.iterdir() if p.is_dir() and SESSION_FOLDER.match(p.name))
        files.extend(p / "spec.md" for p in folders if (p / "spec.md").is_file())
    return files


def read_specs(project_dir: Path, unit: str) -> tuple[dict[str, list[str]], dict[str, str]]:
    """The Cases of every Spec of the unit, and the file each Case was found in (relative
    to the project); a Case heading in two files is an error."""
    cases: dict[str, list[str]] = {}
    found: dict[str, str] = {}
    for path in spec_files(project_dir, unit):
        name = path.relative_to(project_dir).as_posix()
        for case, lines in split_cases(path.read_text(encoding="utf-8")).items():
            if case in found:
                raise MaterializeError(f"Case {case} is in both {found[case]} and {name}")
            cases[case] = lines
            found[case] = name
    return cases, found


def unquote(line: str) -> str:
    match = QUOTE.match(line)
    return match.group(1) if match else line


# --- the one judgment of a fence (case 444.1) ---------------------------------------


def fence_opening(line: str) -> tuple[str, int, str] | None:
    """`(character, length, tag)` of the fence `line` opens — a run of three or more
    backticks or tildes after at most three spaces of indent, the tag the first word after
    it, lowercased — or None. `line` is taken inside the block it stands in: a quote marker
    or the indent of a sub-point is removed by the caller (case 444.1)."""
    match = FENCE_OPEN.match(line)
    if not match:
        return None
    run, info = match.groups()
    words = info.split()
    return run[0], len(run), words[0].lower() if words else ""


def closes_fence(line: str, opening: tuple[str, int, str]) -> bool:
    """True when `line` closes the fence `opening` opened: a run of the same character at
    least as long, after at most three spaces of indent, with nothing after it but spaces
    (CommonMark). A shorter run, a run of the other character, or a word after the run is
    content of the fence (case 444.1)."""
    match = FENCE_CLOSE.match(line)
    if not match:
        return False
    run = match.group(1)
    return run[0] == opening[0] and len(run) >= opening[1]


def fence_breaks(text: str) -> list[tuple[str, str]]:
    """Each break of a code fence in `text`, the text of one section: `("text", line)` for a
    line inside an open fence that starts with a run of the fence's character at least as
    long as the fence and has text after the run — the fence does not close there, and the
    text after it is read as code; `("open", line)` for a fence still open at the end of the
    text, `line` its opening line. Built on `fence_opening` and `closes_fence`, the one
    judgment; `check_pairs` of `guppi/prespec.py` and the class `fence` of `guppi/lint.py`
    call it (case 487.1)."""
    breaks: list[tuple[str, str]] = []
    opening: tuple[str, int, str] | None = None
    opening_line = ""
    for line in text.splitlines():
        if opening is None:
            opening, opening_line = fence_opening(line), line
            continue
        if closes_fence(line, opening):
            opening = None
            continue
        run = fence_opening(line)
        if run and run[0] == opening[0] and run[1] >= opening[1]:
            breaks.append(("text", line))
    if opening is not None:
        breaks.append(("open", opening_line))
    return breaks


def fence_for(text: str) -> str:
    """The fence a block holding `text` is written with: backticks one longer than the
    longest run of backticks that opens a line of the text, three at the least, so that no
    line inside closes it (case 444.2)."""
    longest = 0
    for line in text.splitlines():
        body = line.lstrip()
        longest = max(longest, len(body) - len(body.lstrip("`")))
    return "`" * max(3, longest + 1)


def fenced_lines(lines: list[str]):
    """Each line of `lines`, quotes removed, as `(line, opening)`: `opening` the fence the
    line stands in, None outside any fence. The opening line of a fence is not given; its
    closing line is given as `(None, opening)`; a block not closed runs to the end. The walk
    of `tagged_blocks` and of `plan_prose` in `guppi/prespec.py` (case 444.1)."""
    opening: tuple[str, int, str] | None = None
    for raw in lines:
        line = unquote(raw)
        if opening is None:
            opening = fence_opening(line)
            if opening is None:
                yield line, None
            continue
        if closes_fence(line, opening):
            yield None, opening
            opening = None
            continue
        yield line, opening


def then_blocks(lines: list[str]) -> tuple[dict, list[str]]:
    """The merged content of every fence tagged `then` under a Case, and the parse errors."""
    merged: dict = {}
    errors: list[str] = []
    for block in tagged_blocks(lines, "then"):
        _merge_block(merged, block, errors)
    return merged, errors


BLOCK_SCALAR = re.compile(r"(?:^|\s)[|>][1-9+-]{0,2}$")


def _comment_start(line: str, quote: str | None) -> tuple[int | None, str | None]:
    """Where a YAML comment starts in `line`, and the quote still open at its end: a `#` at
    the start of the line or after a space or a tab, outside a quoted scalar. A quote opens a
    scalar only where a scalar starts — the start of the line, after `- `, `: `, `[`, `{` or
    `,` — so the apostrophe of a plain word opens none."""
    start = quote is None
    i = 0
    while i < len(line):
        char = line[i]
        if quote == "'":
            if char == "'" and line[i + 1 : i + 2] == "'":
                i += 2
                continue
            if char == "'":
                quote, start = None, False
            i += 1
            continue
        if quote == '"':
            if char == "\\":
                i += 2
                continue
            if char == '"':
                quote, start = None, False
            i += 1
            continue
        if char in " \t":
            i += 1
            continue
        if char == "#" and (i == 0 or line[i - 1] in " \t"):
            return i, None
        after = line[i + 1 : i + 2]
        if start and char in "'\"":
            quote, start = char, False
        elif char in "-:" and after in ("", " ", "\t"):
            start = start or char == ":"
        elif char in "[{,":
            start = True
        else:
            start = False
        i += 1
    return None, quote


def yaml_comments(text: str) -> list[str]:
    """The lines of `text`, the YAML of one fenced block, that hold a comment — a `#` at the
    start of a line or after a space or a tab, outside a quoted value and outside a `|` or
    `>` block. After a space YAML drops the rest of such a line, so a value without quotes
    may be cut there; after a tab PyYAML, the library the scripts use, refuses the whole
    block (case 526). The one judgment of a comment: `ratified` refuses a short Case by it, `materialize`
    marks the entries of its Case `incomplete: [comment]` (cases 521.1, 521.2)."""
    found: list[str] = []
    quote: str | None = None
    block_above: int | None = None  # the column a `|` or `>` block's lines stand right of
    for line in text.splitlines():
        indent = len(line) - len(line.lstrip(" "))
        if block_above is not None:
            if not line.strip() or indent > block_above:
                continue
            block_above = None
        at, quote = _comment_start(line, quote)
        if at is not None:
            found.append(line)
        value = (line if at is None else line[:at]).rstrip()
        match = BLOCK_SCALAR.search(value) if quote is None else None
        if match is None:
            continue
        head = value[: match.start()].strip()
        if head and not head.endswith(":") and head.strip("- \t"):
            continue
        if head.strip("- \t"):  # `key: |` — its lines stand right of the key
            block_above = len(line) - len(line.lstrip(" -\t"))
        else:  # `|` or `- |` — its lines stand right of the last dash
            block_above = line.rfind("-", 0, match.start() + 1) if "-" in head else indent - 1
    return found


def then_comments(lines: list[str]) -> list[str]:
    """The lines of the fences tagged `then` under a Case that hold a YAML comment, by
    `yaml_comments`; the one call of `ratified` and `materialize` (cases 521.1, 521.2)."""
    return [line for block in tagged_blocks(lines, "then") for line in yaml_comments(block)]


def tagged_blocks(lines: list[str], tag: str) -> list[str]:
    """The text of every fenced block tagged `tag` under a Case, quotes removed; the one
    reading of a tagged fence for `prespec` and `ratified` (case 387.3). A block not closed
    is not given."""
    blocks: list[str] = []
    buffer: list[str] = []
    for line, opening in fenced_lines(lines):
        if opening is None or opening[2] != tag:
            continue
        if line is None:
            blocks.append("\n".join(buffer))
            buffer = []
        else:
            buffer.append(line)
    return blocks


def _merge_block(merged: dict, text: str, errors: list[str]) -> None:
    try:
        data = yaml.safe_load(text) or {}
    except yaml.YAMLError as exc:
        errors.append(f"then block is not YAML: {exc}")
        return
    if not isinstance(data, dict):
        errors.append("then block is not a mapping")
        return
    for key, value in data.items():
        if isinstance(value, list):
            merged.setdefault(key, []).extend(value)
        else:
            merged[key] = value


def quoted_sections(lines: list[str], names: tuple[str, ...]) -> dict[str, str]:
    """Name → text of the `> **name:**` blockquotes among `lines`, for the names given; the
    chat form and the Spec form alike, the one reader of the sections of a Case (case 462). A
    blank line outside a fence closes a section, the fence judged by `fence_opening` and
    `closes_fence` (case 444.1)."""
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    opening: tuple[str, int, str] | None = None

    def close():
        if current is not None:
            sections[current] = "\n".join(buffer).strip("\n")

    for raw in lines:
        match = QUOTE.match(raw)
        if not match:
            if opening is None:
                opening = fence_opening(raw)
            elif closes_fence(raw, opening):
                opening = None
            if opening is None and current is not None and raw.strip() == "":
                close()
                current = None
            continue
        text = match.group(1)
        start = SECTION_START.match(text)
        if start and start.group(1) in names:
            close()
            current = start.group(1)
            buffer = [start.group(2)] if start.group(2) else []
        elif current is not None:
            buffer.append(text)
    close()
    return sections


def case_texts(cases: dict[str, list[str]], case: str) -> dict[str, str]:
    """The sections of a Case, with a missing `context` or `given` read from its parent
    (case 60), never `problem`, `recommend` or `when` (case 544.6); a Spec older than the
    seven-block form gives its text whole as `then`."""
    lines = cases.get(case, [])
    texts = quoted_sections(lines, CASE_SECTIONS)
    if not texts and lines:
        texts = {"then": "\n".join(lines).strip("\n")}
    if "." in case:
        parent = cases.get(case.rsplit(".", 1)[0], [])
        for name, text in quoted_sections(parent, CASE_SECTIONS).items():
            if name in INHERITED:
                texts.setdefault(name, text)
    return texts


def find_item(block: dict, kind: str, slug: str) -> tuple[dict | None, str | None]:
    """The `then` item for a decision, and the kind of the create it was nested in."""
    for item in block.get(kind) or []:
        if isinstance(item, dict) and item.get("slug") == slug:
            return item, None
    if kind == "create":
        for item in block.get("create") or []:
            nested = item.get("estimate") if isinstance(item, dict) else None
            if isinstance(nested, dict) and nested.get("slug") == slug:
                return dict(
                    nested, parent_create=item.get("slug"), parent_tags=item.get("tags")
                ), "estimate"
    return None, None


# --- entries ------------------------------------------------------------------------


def page_paths(project_dir: Path, category: str, slug: str) -> list[Path]:
    """The page of a slug on disk: live under `wiki/<category>/`, or under
    `vault/archive/` at any depth outside a `raw/` folder (case 102.2)."""
    wiki = project_dir / "vault" / "wiki"
    found = [wiki / category / f"{slug}.md"] if (wiki / category / f"{slug}.md").exists() else []
    archive = project_dir / "vault" / "archive"
    if archive.is_dir():
        found += [
            p
            for p in sorted(archive.rglob(f"{slug}.md"))
            if "raw" not in p.relative_to(archive).parts[:-1]
        ]
    return found


def page_exists(project_dir: Path, category: str, slug: str) -> bool:
    return bool(page_paths(project_dir, category, slug))


def has_page(project_dir: Path, category: str, slug: str) -> bool:
    """True when the page of a slug stands in its own category folder: under
    `vault/wiki/<category>/`, or in a folder `<category>` under `vault/archive/` outside a
    `raw/` folder (case 783). `defer_writes_no_page` asks it (case 786)."""
    if (project_dir / "vault" / "wiki" / category / f"{slug}.md").exists():
        return True
    archive = project_dir / "vault" / "archive"
    if not archive.is_dir():
        return False
    return any(
        p.parent.name == category and "raw" not in p.relative_to(archive).parts[:-1]
        for p in archive.rglob(f"{slug}.md")
    )


# the folders whose `defer` with no page writes a placeholder page (case 786)
PLACEHOLDER_CATEGORIES = ("rules", "entities")


def defer_writes_no_page(project_dir: Path, category: str, slug: str) -> bool:
    """True when a `defer` names a page that a placeholder cannot stand for: `category` is a
    vault folder of `CATEGORIES` outside `PLACEHOLDER_CATEGORIES`, and `has_page` finds no
    page. The one judgment whether a `defer` names a page, imported by `guppi/generate.py`,
    which fails such an entry, and `guppi/prespec.py`, which reports it (cases 783, 786)."""
    return (
        category in CATEGORIES
        and category not in PLACEHOLDER_CATEGORIES
        and not has_page(project_dir, category, slug)
    )


def page_of_case(project_dir: Path, category: str, slug: str, origin: str) -> bool:
    """True when the page on disk was born of this very line — its `origin` names the
    same `#case-N` or the same `#L<n>` of the same ledger (case 105.2). A page of another
    Case, live or archived, is not `exists`: the entry stays a create for `generate` to
    refuse as a collision, so the data of the new Case is never dropped in silence."""
    for path in page_paths(project_dir, category, slug):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^origin:\s*(.+?)\s*$", text, re.MULTILINE)
        found = match.group(1).strip("'\"") if match else ""
        if found == origin:
            return True
        this_case, that_case = origin.rsplit("#", 1)[-1], found.rsplit("#", 1)[-1]
        if this_case.startswith("case-") and this_case == that_case:
            return True
    return False


def decision_entry(
    record: dict,
    number: int,
    text: str,
    date: str,
    block: dict,
    project_dir: Path,
    schema_free: set[str] = frozenset(),
):
    kind, slug = record["kind"], record["slug"]
    entry: dict = {
        "line": number,
        "text": text,
        "case": record["case"],
        "kind": kind,
        "slug": slug,
        "origin": f"raw/{date}/ledger.md#case-{record['case']}",
        "decision": f"decision-case-{record['case']}",
    }
    for key in ("ref", "source", "supersedes", "addresses"):
        if record.get(key):
            entry[key] = record[key]
    if record.get("tags"):
        entry["tags"] = record["tags"]
    item, nested = find_item(block, kind, slug)
    incomplete: list[str] = []
    category = category_of(slug)
    if category is not None:
        entry["category"] = category
    else:  # a slug without a category prefix names no page (case 320: no file route)
        entry["category"] = "unknown"
        incomplete.append("category")
    if item is None:
        incomplete.append("then")
    else:
        _lift_item(
            entry, item, kind, nested, incomplete, schema_fields(project_dir, entry, schema_free)
        )
    if (
        kind == "create"
        and entry["category"] in CATEGORIES
        and page_of_case(project_dir, entry["category"], slug, entry["origin"])
    ):
        entry["exists"] = True
    if kind == "defer" and entry["category"] in CATEGORIES:
        entry["exists"] = page_exists(project_dir, entry["category"], slug)
    if incomplete:
        entry["incomplete"] = incomplete
    return entry


STRUCTURAL_KEYS = ("slug", "sections", "estimate", "file", "ref", "parent_create", "parent_tags")
DEFER_KEYS = ("type", "purpose")  # a defer's own keys, not fields of its target (case 266)
CREATE_SKIPPED = ("slug", "sections", "estimate", "file", "parent_create", "parent_tags")
# The closed keys of an `update` and a `delete` (case 436.1): what `_lift_item` lifts and
# `generate` applies; any other key of these kinds is dropped here and refused by the Spec
# hook and by pre-spec, which import this list.
ITEM_KEYS = {
    "update": ("slug", "set", "sections", "replace", "reword", "change", "rename"),
    "delete": ("slug", "impact", "change"),
}


def accepted_keys(kind: str, known: set[str]) -> set[str]:
    """The keys a `create` or a `defer` accepts, given the fields `known` of its category's
    schema: those fields and the item's own keys, as `_lift_item` counts them (case 436.1).
    The keys of an older shape are none of them (the shape before case 189; case 440)."""
    if kind == "defer":
        return set(known) | set(DEFER_KEYS) | set(STRUCTURAL_KEYS)
    return set(known) | set(CREATE_SKIPPED) | set(STRUCTURAL_KEYS)


def item_keys(
    kind: str, category: str | None, project_dir: Path, schema_free: set[str] = frozenset()
) -> set[str] | None:
    """The keys an item of `kind` for a page of `category` accepts — the one judgment the
    lift, `generate`, the Spec hook and pre-spec share (case 436). `ITEM_KEYS` for an
    `update` and a `delete`; for a `create` and a `defer` the fields of the category's schema
    and the item's own keys. None where no judgment is made: a category with no schema file,
    or one whose schema rule the session changes (`schema_free`) (case 308.2)."""
    if kind in ITEM_KEYS:
        return set(ITEM_KEYS[kind])
    if kind not in ("create", "defer"):
        return None
    known = schema_fields(project_dir, {"category": category}, schema_free)
    if known is None:
        return None
    return accepted_keys(kind, known)


def schema_fields(
    project_dir: Path, entry: dict, schema_free: set[str] = frozenset()
) -> set[str] | None:
    """The fields the category's `schema.yaml` names — `required` and `optional` — the
    only keys of an item that reach `fields` (case 214.1); None without a schema file, and
    then nothing is filtered — and None for a category whose schema rule this unit creates
    or updates, whose items are lifted whole (case 308.2)."""
    category = entry.get("category")
    if category in schema_free:
        return None
    path = project_dir / "vault" / "wiki" / str(category) / "schema.yaml"
    if category not in CATEGORIES or not path.exists():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    props = data.get("properties") if isinstance(data, dict) else None
    if not isinstance(props, dict):
        return None
    return {str(k) for k in (props.get("required") or [])} | {
        str(k) for k in (props.get("optional") or [])
    }


def fill_type(fields: dict, category: str | None) -> dict:
    """The `type` of a `create` that writes none, from its category by `SINGULAR`; a
    written `type` stands (case 748.1)."""
    if category in SINGULAR:
        fields.setdefault("type", SINGULAR[category])
    return fields


def create_lacks(
    category: str | None,
    fields: dict,
    sections: dict | None,
    tagged: bool,
    ref: str | None = None,
) -> list[str]:
    """The fields of `REQUIRED` that a `create` item of `category` lacks, `type` filled
    first by `fill_type`: a field is present as a key of `fields` or under `sections`, and
    the tags when the item or its decision line carries them. A rule of kind `Leaf` lacks
    `parent` when it has neither a `ref`, on its item or its decision line, nor a `parent`
    nor an `applies_to` that links it to an entity (case 795.2). The one judgment the lift
    marks `incomplete` by and pre-spec reports by (case 748.2)."""
    fields = fill_type(dict(fields), category)
    sections = sections or {}
    present = set(fields) | set(sections) | {str(k).lower() for k in sections}
    if tagged:
        present.add("tags")
    lacks = [
        name
        for name in REQUIRED.get(category, ())
        if name not in present and name.capitalize() not in sections
    ]
    if (
        category == "rules"
        and fields.get("kind") == "Leaf"
        and not (ref or fields.get("ref") or fields.get("parent") or fields.get("applies_to"))
    ):
        lacks.append("parent")
    return lacks


def create_fields(item: dict, known: set[str] | None) -> dict:
    """The fields a `create` item lifts: its keys but the structural ones, those the
    category's schema names when it has one (cases 214.1, 436)."""
    fields = {k: v for k, v in item.items() if k not in CREATE_SKIPPED}
    if known is not None:
        fields = {k: v for k, v in fields.items() if k in known}
    return fields


def _lift_item(
    entry: dict,
    item: dict,
    kind: str,
    nested: str | None,
    incomplete: list[str],
    known: set[str] | None = None,
):
    if kind == "create":
        fields = create_fields(item, known)
        if known is not None:  # the lift by the schema (case 214.1), by `accepted_keys` (436)
            accepted = accepted_keys("create", known)
            unknown = [k for k in item if k not in accepted]
            if unknown:
                entry["unknown"] = unknown
            if item.get("ref") and not entry.get("ref"):  # the item's ref is the entry's
                entry["ref"] = str(item["ref"])
        fill_type(fields, entry.get("category"))  # from the category (case 748.1)
        if nested == "estimate" or entry.get("category") == "estimates":
            fields.pop("context", None)  # `## Context` is not written (since case 193)
            if "criterion" in fields:  # a written Criterion (the shape before case 194.1)
                entry.setdefault("sections", {})["Criterion"] = fields.pop("criterion")
            ref = fields.pop("ref", None)  # the target is the entry's `ref`, not a page field
            if ref and not entry.get("ref"):
                entry["ref"] = str(ref)
            # `purpose` and `method` stay fields: one line each on the page (case 194.1)
        if nested == "estimate":
            if "parent_create" in item and not entry.get("ref"):
                entry["ref"] = item["parent_create"]
            if item.get("parent_tags") and not entry.get("tags") and not fields.get("tags"):
                fields["tags"] = list(item["parent_tags"])
        entry["fields"] = fields
        if item.get("sections"):
            entry.setdefault("sections", {}).update(item["sections"])
        if item.get("tags") and not entry.get("tags"):
            entry["tags"] = list(item["tags"])
        category = entry.get("category")
        incomplete += create_lacks(
            category, fields, entry.get("sections"), bool(entry.get("tags")), entry.get("ref")
        )
    elif kind == "update":
        for key in ITEM_KEYS["update"]:
            if key in ("slug", "reword"):  # the target, and the pairs checked below
                continue
            if item.get(key) is not None:  # `rename`: the new slug, checked by generate (258.2)
                entry[key] = item[key]
        if item.get("reword") is not None:  # a list of pairs, carried as written (274.3)
            pairs = item["reword"]
            if isinstance(pairs, list) and all(isinstance(p, dict) for p in pairs):
                entry["reword"] = pairs
            else:
                incomplete.append("reword")
        if "change" not in item:
            incomplete.append("change")
    elif kind == "defer":
        fields = {k: v for k, v in item.items() if k not in ("slug", "file")}
        if known is not None:  # the lift by the schema (case 214.1); `type` and `purpose`
            # are the defer's own keys, kept whatever the target's category (case 266)
            kept = set(known) | set(DEFER_KEYS)
            accepted = accepted_keys("defer", known)
            unknown = [k for k in fields if k not in accepted]
            if unknown:
                entry["unknown"] = unknown
            fields = {k: v for k, v in fields.items() if k in kept}
        entry["fields"] = fields
        if "purpose" not in fields:
            incomplete.append("purpose")
    else:  # delete: the keys of `ITEM_KEYS`, the others dropped (case 436.1)
        for key in ITEM_KEYS["delete"]:
            if key != "slug" and item.get(key) is not None:
                entry[key] = item[key]


# --- the Criterion of an Estimate (cases 188, 194.1) ----------------------------------


def criterion_text(texts: dict[str, str]) -> str:
    """The Criterion of an Estimate: the Case's `when` and `then` verbatim with their
    operand lines, as `When:`, `Then:` — the `given` is the frame of the Case and stays out
    (case 378.2); a missing section is left out, never invented (case 194.1)."""
    parts = []
    for name in CRITERION_SECTIONS:
        text = texts.get(name)
        if text and fence_opening(text.splitlines()[0]) is None:  # not the whole-Case fallback
            parts.append(f"{name.capitalize()}:\n{text}")
    return "\n\n".join(parts)


def names_a_part(entry: dict) -> bool:
    """An `update` item of an Estimate that names a part of the page and writes no
    Criterion: `set` without `status`, a `replace` pair, a section other than `Criterion`,
    or `change` alone, which names its History (case 588.2). One that carries `set.status`
    or a Criterion under `sections` is the whole replacement (case 296)."""
    sets = entry.get("set") or {}
    sections = entry.get("sections") or {}
    return not ("status" in sets or sections.get("Criterion"))


def touches_criterion(project_dir: Path, slug: str, replaces) -> bool:
    """Whether the `old` of a `replace` pair stands in the `## Criterion` of the live
    Estimate page; no page, no pair, or an `old` elsewhere — False. An `old` absent from
    the page is not judged here: `generate` refuses the pair (case 296)."""
    if not isinstance(replaces, list):
        return False
    path = project_dir / "vault" / "wiki" / "estimates" / f"{slug}.md"
    if not path.is_file():
        return False
    body = path.read_text(encoding="utf-8")
    start = body.find("\n## Criterion")
    if start < 0:
        return False
    end = body.find("\n## ", start + 1)
    criterion = body[start:] if end < 0 else body[start:end]
    return any(
        isinstance(pair, dict) and str(pair.get("old", "")) in criterion for pair in replaces
    )


def lift_criterion(entry: dict, texts: dict[str, str], project_dir: Path | None = None) -> None:
    """An Estimate's `create` or `update` carries its Criterion under `sections` — the
    shape `generate` applies as a whole replacement. A Criterion the item wrote under
    `sections` stands; otherwise the Case's own text is lifted. An `update` is set
    `pending` unless the item set a status itself (case 194.1). An `update` that names a
    part of the page — `set` without `status`, a `replace` pair, a section other than
    `Criterion`, or `change` alone, its History (case 588.2) — and writes no Criterion
    changes that part alone: nothing is lifted and no status is set; a pair whose `old`
    stands in the page's `## Criterion` is `incomplete: [criterion]` — a Criterion changes
    only whole (case 378.4). So the Criterion is lifted only for a `create`, an `update`
    with `set.status` or one that writes it, and `pending` is set only on one that writes
    its Criterion with no status of its own."""
    if entry.get("category") != "estimates" or entry.get("kind") not in ("create", "update"):
        return
    if entry["kind"] == "update" and names_a_part(entry):
        if project_dir is not None and touches_criterion(
            project_dir, str(entry.get("slug", "")), entry.get("replace")
        ):
            entry.setdefault("incomplete", []).append("criterion")
        return
    sections = entry.setdefault("sections", {})
    if not sections.get("Criterion"):
        text = criterion_text(texts)
        if text:
            sections["Criterion"] = text
        else:
            entry.setdefault("incomplete", []).append("criterion")
    if not sections:
        entry.pop("sections")
    if entry["kind"] == "update":
        entry.setdefault("set", {}).setdefault("status", "pending")


def page_estimates(project_dir: Path, category: str, slug: str) -> list[str] | None:
    """The `estimates` field of a live page, None when the page does not exist."""
    path = project_dir / "vault" / "wiki" / category / f"{slug}.md"
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return []
    head, _, _ = text[3:].partition("\n---")
    try:
        front = yaml.safe_load(head)
    except yaml.YAMLError:
        return []
    value = front.get("estimates") if isinstance(front, dict) else None
    return [str(slug_of(v)) for v in value] if isinstance(value, list) else []  # 148.1


def estimate_entry(record: dict, number: int, text: str, date: str) -> dict:
    return {
        "line": number,
        "text": text,
        "kind": "estimate",
        "category": "estimates",
        "slug": record["slug"],
        "status": record["status"],
        "result": record["result"],
        "origin": f"raw/{date}/ledger.md#L{number}",
    }


def lesson_entry(record: dict, number: int, text: str, date: str, project_dir: Path) -> dict:
    entry = {
        "line": number,
        "text": text,
        "kind": "lesson",
        "category": "lessons",
        "slug": record["slug"],
        "origin": f"raw/{date}/ledger.md#L{number}",
        "fields": {"type": "lesson", "kind": record["kind"], "root_cause": record["root_cause"]},
        "sections": {"Trigger": record["trigger"], "Root cause": record["root_cause"]},
    }
    incomplete = []
    if record.get("tags"):
        entry["tags"] = record["tags"]
    else:
        incomplete.append("tags")
    if record.get("source"):
        entry["fields"]["source"] = record["source"]
    elif record["kind"] == "knowledge":
        incomplete.append("source")
    if page_of_case(project_dir, "lessons", record["slug"], entry["origin"]):
        entry["exists"] = True
    if incomplete:
        entry["incomplete"] = incomplete
    return entry


def fold_estimate(entries: list[dict], record: dict, number: int) -> bool:
    """Fold an estimate line into the live create of its page in this yaml; False when none
    is there. The create remembers the folded line. A create already applied, or marked
    `superseded_by`, is passed by: a reading never folds into a create `generate` skips
    (case 309)."""
    for entry in entries:
        if entry.get("kind") != "create" or entry.get("slug") != record["slug"]:
            continue
        if entry.get("applied") or entry.get("superseded_by"):
            continue
        entry["status"] = record["status"]
        entry["result"] = record["result"]
        entry.setdefault("folded", []).append(number)
        return True
    return False


def refold(entries: list[dict], case: str, ledger: list[str], date: str) -> None:
    """The readings folded into a `create` this mark just superseded move to the live
    `create` of the same slug in the unit; with none, each becomes an `estimate` entry of its
    own from its ledger line (case 309). The marked entry keeps no reading; the mark covers the
    sub-cases of `case` too (case 660.2)."""
    for entry in entries:
        own = entry.get("case")
        if own is None or not in_family(str(own), case):
            continue
        if entry.get("kind") != "create" or not entry.get("folded"):
            continue
        numbers = entry.pop("folded")
        entry.pop("status", None)
        entry.pop("result", None)
        live = next(
            (
                e
                for e in entries
                if e.get("kind") == "create"
                and e.get("slug") == entry.get("slug")
                and not e.get("superseded_by")
                and not e.get("applied")
            ),
            None,
        )
        for number in numbers:
            line = ledger[number - 1] if 0 < number <= len(ledger) else ""
            parsed = parse_line(line) if line.startswith("- ") else None
            if parsed is None or parsed.get("record") != "estimate":
                continue
            if live is not None:
                live["status"] = parsed["status"]
                live["result"] = parsed["result"]
                live.setdefault("folded", []).append(number)
            else:
                entries.append(estimate_entry(parsed, number, line_body(line), date))


def in_family(case: str, top: str) -> bool:
    """Whether `case` is `top` or one of its sub-cases at any depth: the one reading of a
    `{supersedes:case N}` tag, which retires N with its sub-cases (case 660)."""
    return case == top or case.startswith(top + ".")


def mark_superseded(
    entries: list[dict], decisions: list[dict], case: str, by: str, spec=None
) -> bool:
    """Mark `superseded_by` every entry of `case` or of one of its sub-cases, as `in_family`
    judges them (case 660.2) — the lines' own and the derived ones, the block removal included,
    whatever its kind (case 175) — and their decision records likewise; True when an entry
    or a record of that family was here to mark. An `estimate` or `lesson` entry carries no
    `case` and is never marked. `spec`, when given, holds the Cases whose heading stands in
    the Spec: a marked Case gone from it is complete by the mark, and `then` leaves its
    `incomplete` (case 299.3)."""
    marked = False
    for entry in entries:
        own = entry.get("case")
        if own is not None and in_family(str(own), case):
            done = cases_of(entry.get("superseded_by"))  # one value in an older yaml (case 776)
            if by not in done:
                done.append(by)
            entry["superseded_by"] = done
            marked = True
            if spec is not None and own not in spec and "then" in (entry.get("incomplete") or []):
                rest = [i for i in entry["incomplete"] if i != "then"]
                if rest:
                    entry["incomplete"] = rest
                else:
                    del entry["incomplete"]
    for decision in decisions:
        if decision.get("case") is not None and in_family(str(decision["case"]), case):
            done = decision.setdefault("superseded_by", [])
            if f"decision-case-{by}" not in done:
                done.append(f"decision-case-{by}")
            marked = True
    return marked


def mark_superseded_elsewhere(project_dir: Path, unit: str, pairs: list[tuple[str, str]]) -> None:
    """A `supersedes` of a Case whose entries lie in another unit's yaml marks them there
    (case 130.2): every other yaml under `raw/` is loaded, the entries and the `decisions`
    of that case marked, and the file written with that mark only. A case no yaml holds
    changes nothing."""
    if not pairs:
        return
    for other in units_with(project_dir, "materialize.yaml"):
        if other == unit:
            continue
        path = yaml_path(project_dir, other)
        data = load_yaml(path)
        if data is None:
            continue
        changed = False
        for case, by in pairs:
            if mark_superseded(data.get("entries") or [], data.get("decisions") or [], case, by):
                changed = True
        if changed:
            dump_yaml(path, data)


def decision_record(
    case: str,
    entries_of_case: list[dict],
    date: str,
    texts: dict,
    block_errors,
    spec: str | None = None,
    gone_from_spec: bool = False,
):
    """The `decisions` record of one Case. `gone_from_spec`: every entry of the Case is
    marked `superseded_by` and no heading of its number stands in the Spec — the Case left
    it (299.1); the record carries no `case_text` and no `incomplete` (case 299.3)."""
    targets = []
    tags: list[str] = []
    supersedes: list[str] = []
    for entry in entries_of_case:
        if entry.get("derived"):  # an entry of an older shape, kept as it is (case 189)
            continue
        target = {"kind": entry["kind"], "category": entry["category"], "slug": entry["slug"]}
        for key in ("ref", "source"):
            if entry.get(key):
                target[key] = entry[key]
        targets.append(target)
        for tag in entry.get("tags") or []:
            if tag not in tags:
                tags.append(tag)
        for earlier in cases_of(entry.get("supersedes")):
            if f"decision-case-{earlier}" not in supersedes:
                supersedes.append(f"decision-case-{earlier}")
    record = {
        "case": case,
        "decision": f"decision-case-{case}",
        "origin": f"raw/{date}/ledger.md#case-{case}",
        "targets": targets,
        "tags": tags,
        "case_text": texts,
    }
    if "." in case:  # a sub-case names the record of its parent (case 544.6)
        record["parent"] = f"decision-case-{case.rsplit('.', 1)[0]}"
    if spec is not None:
        record["spec"] = spec
    if supersedes:
        record["supersedes"] = supersedes
    if gone_from_spec:  # superseded in its own session: complete by the mark (299.3)
        del record["case_text"]
        return record
    # `problem` stands on the parent only: a sub-case needs none (case 544.6)
    needed = ("context",) if "." in case else ("context", "problem")
    if any(
        e.get("kind") != "defer" for e in entries_of_case
    ):  # the short form of a defer (56, 542)
        needed += ("given", "when")
    missing = [name for name in needed if name not in texts]
    if missing or block_errors:
        record["incomplete"] = missing + list(block_errors)
    return record


def parents_of(cases: list[str]) -> dict[str, list[str]]:
    """Parent id → the ids of its sub-cases among `cases` and among the parents found, in
    the order they come; a parent of a parent is found too (case 544.6)."""
    parents: dict[str, list[str]] = {}
    queue = list(cases)
    while queue:
        case = queue.pop(0)
        if "." not in case:
            continue
        parent = case.rsplit(".", 1)[0]
        if parent not in parents:
            parents[parent] = []
            queue.append(parent)
        if case not in parents[parent]:
            parents[parent].append(case)
    return parents


def parent_record(
    case: str,
    children: list[str],
    date: str,
    cases: dict[str, list[str]],
    tags: list[str],
    spec: str | None = None,
) -> dict:
    """The `decisions` record of a Case whose sub-cases have decision lines in the unit and
    which has none of its own: its `decision` and `origin` by its id, `case_text` with its
    `context`, `problem`, `recommend` and its `given` when it has one, `children` the records
    of its sub-cases in ledger order, `tags` the union of theirs, and no `targets`; a missing
    `context` or `problem` is `incomplete` (case 544.6)."""
    texts = quoted_sections(cases.get(case, []), PARENT_TEXT)
    record = {
        "case": case,
        "decision": f"decision-case-{case}",
        "origin": f"raw/{date}/ledger.md#case-{case}",
        "children": [f"decision-case-{c}" for c in children],
        "tags": tags,
        "case_text": texts,
    }
    if "." in case:
        record["parent"] = f"decision-case-{case.rsplit('.', 1)[0]}"
    if spec is not None:
        record["spec"] = spec
    needed = ("context",) if "." in case else ("context", "problem")  # problem: the top only
    missing = [name for name in needed if name not in texts]
    if missing:
        record["incomplete"] = missing
    return record


# --- assembly -----------------------------------------------------------------------


def opened_sprint(ledger: list[str]) -> str | None:
    """The `<id>` of the first `create` decision line of an `entity-sprint-<id>` slug in a
    unit's ledger, else None: the yaml's `sprint` of the unit that opens a sprint (case 628.3)."""
    for line in ledger:
        record = parse_line(line)
        if (
            record
            and record["record"] == "decision"
            and record["kind"] == "create"
            and is_sprint_page(record["slug"])
        ):
            return record["slug"][len(SPRINT_PAGE) :]
    return None


def sprint_id(project_dir: Path) -> str:
    path = project_dir / "vault" / "wiki" / "sprint.md"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                return line[3:].split(" ", 1)[0].strip()
    return "unknown"


def lift_line(
    record: dict,
    number: int,
    text: str,
    date: str,
    project_dir: Path,
    cases: dict[str, list[str]],
    blocks: dict,
    texts_of: dict,
    entries: list[dict],
    decisions: list[dict],
    elsewhere: list[tuple[str, str]],
    schema_free: set[str] = frozenset(),
    ledger: list[str] | None = None,
) -> int:
    """One record line into its entries; the count added. Any exception is the line's
    alone: `assemble` catches it and writes a `failed` entry instead (case 142.1)."""
    if record["record"] == "estimate":
        if fold_estimate(entries, record, number):
            return 1
        entries.append(estimate_entry(record, number, text, date))
        return 1
    if record["record"] == "lesson":
        lesson = lesson_entry(record, number, text, date, project_dir)
        mark = record.get("addressed_by")
        # the one judgment the ledger hook calls too (case 497.1)
        if mark and number - 1 in marks_without_decision(ledger or []):
            lesson.setdefault("incomplete", []).append("addressed_by")  # no decision line before it
        elif mark:
            address(lesson, mark)
        entries.append(lesson)
        return 1
    case = record["case"]
    if case not in blocks:
        blocks[case] = then_blocks(cases.get(case, []))
    block, errors = blocks[case]
    entry = decision_entry(record, number, text, date, block, project_dir, schema_free)
    if errors and "then" in (entry.get("incomplete") or []):
        entry["incomplete"] = [e for e in entry["incomplete"] if e != "then"] + errors
    # a value cut at a space, a block refused at a tab (cases 521.2, 526)
    if then_comments(cases.get(case, [])):
        entry.setdefault("incomplete", []).append("comment")
    if case not in texts_of:
        texts_of[case] = case_texts(cases, case)
    lift_criterion(entry, texts_of[case], project_dir)  # an Estimate's own entry (189, 194.1, 296)
    entries.append(entry)
    added = 1
    for earlier in record.get("supersedes") or []:  # one block per Case (case 429)
        if mark_superseded(entries, decisions, earlier, case, cases):
            refold(entries, earlier, ledger or [], date)  # its readings move (case 309)
        else:
            elsewhere.append((earlier, case))  # another unit's yaml (130.2)
    if record.get("addresses") and not mark_addressed(entries, record["addresses"], case):
        entry.setdefault("incomplete", []).append("addresses")  # a mark without its lesson
    return added


def address(lesson: dict, case: str) -> None:
    """The one writer of `addressed_by` on a lesson entry, for both marks: a decision line's
    `{addresses:<lesson slug>}` and a lesson line's `{addressed_by:case N}` (cases 284.3,
    377.3). At the entry's level — never a page field, the lesson page carries none."""
    lesson["addressed_by"] = f"decision-case-{case}"


def mark_addressed(entries: list[dict], slugs: list[str], case: str) -> bool:
    """A decision line's `{addresses:<lesson slug>}` reaches the lesson entry of this unit
    as `addressed_by: decision-case-N`, at the entry's level — never a page field, the
    lesson page carries none (case 284.3). True when every named lesson was here."""
    found = True
    for slug in slugs:
        lessons = [e for e in entries if e.get("kind") == "lesson" and e.get("slug") == slug]
        if not lessons:
            found = False
        for lesson in lessons:
            address(lesson, case)
    return found


def assemble(
    project_dir: Path, unit: str, existing: dict | None, stderr
) -> tuple[dict, int, list[tuple[str, str]], int]:
    """The yaml of one unit, `<date>` or `<date>/<HHMM>` (case 103.2); the `origin` of
    every entry names the unit's ledger, so `date` below is the unit path. Returns the
    data, the entries added, the supersedes for other units and the lines that failed."""
    raw = project_dir / "vault" / "raw" / unit
    ledger_path = raw / "ledger.md"
    if not ledger_path.exists():
        raise MaterializeError(f"{ledger_path.relative_to(project_dir).as_posix()} does not exist")
    ledger = ledger_path.read_text(encoding="utf-8").splitlines()
    schema_free = schema_changed(ledger)  # the categories lifted whole (case 308.2)
    cases, spec_of = read_specs(project_dir, unit)
    date = unit
    elsewhere: list[tuple[str, str]] = []
    data = existing or {
        "date": unit.split("/")[0],
        "sprint": sprint_id(project_dir),
        "ledger": f"vault/raw/{unit}/ledger.md",
        "spec": [],
        "entries": [],
        "decisions": [],
        "unparsed": [],
    }
    opening = opened_sprint(ledger)  # the unit that opens a sprint belongs to it (case 628.3)
    if opening:
        data["sprint"] = opening
    if is_session(unit):
        data["session"] = unit.split("/")[1]
    data["spec"] = [p.relative_to(project_dir).as_posix() for p in spec_files(project_dir, unit)]
    texts_of: dict[str, dict] = {}
    entries: list[dict] = data.setdefault("entries", [])
    decisions: list[dict] = data.setdefault("decisions", [])
    unparsed: list[dict] = data.setdefault("unparsed", [])
    # An entry another hand wrote in a shape this script cannot read — not a mapping, or a
    # mapping with none of `line`, `derived`, `librarian` — is left as it is, named once
    # (case 142.1). The librarian's own entries carry `librarian` and no line.
    for entry in entries:
        if not isinstance(entry, dict) or not (
            "line" in entry or entry.get("derived") or entry.get("librarian")
        ):
            print(
                f"materialize: an entry the script cannot read is left alone: {entry!r:.80}",
                file=stderr,
            )
    entries[:] = [e for e in entries if isinstance(e, dict)]
    # A line whose lift failed last run is lifted again and replaced on success (142.1).
    retry = {e["line"]: e for e in entries if "line" in e and e.get("failed") and "kind" not in e}
    known = {e["line"]: e for e in entries if "line" in e and e["line"] not in retry}
    folded = {n for e in entries for n in e.get("folded") or []}
    known_unparsed = {u["line"] for u in unparsed if isinstance(u, dict)} | folded
    blocks: dict[str, tuple[dict, list[str]]] = {}
    added = 0
    failed = 0
    for number, line in enumerate(ledger, start=1):
        if not line.startswith("- "):
            continue
        text = line_body(line)
        if number in known:
            if known[number].get("text") != text:
                print(
                    f"materialize: line {number} changed since the yaml was written; entry left alone",
                    file=stderr,
                )
            continue
        if number in known_unparsed:
            continue
        record = parse_line(line)
        if record is None:
            unparsed.append({"line": number, "text": text})
            continue
        before = len(entries)
        try:
            added += lift_line(
                record,
                number,
                text,
                date,
                project_dir,
                cases,
                blocks,
                texts_of,
                entries,
                decisions,
                elsewhere,
                schema_free,
                ledger,
            )
        except Exception as exc:  # noqa: BLE001 — one line fails alone, the rest are lifted (142.1)
            del entries[before:]
            message = f"{type(exc).__name__}: {exc}"
            print(f"materialize: line {number}: {message}", file=stderr)
            entries.append({"line": number, "text": text, "failed": message})
            failed += 1
            continue
        if number in retry:
            entries.remove(retry[number])
    # new_tags: from the then block of every Case of the Spec, lines or none (case 61)
    for case, lines in cases.items():
        if case not in blocks:
            blocks[case] = then_blocks(lines)
        for tag in blocks[case][0].get("new_tags") or []:
            if isinstance(tag, dict) and tag not in data.setdefault("new_tags", []):
                data["new_tags"].append(tag)
    # decisions: one per case, from the entries of that case
    by_case: dict[str, list[dict]] = {}
    for entry in entries:
        if entry.get("kind") in DECISION_KINDS and "case" in entry:  # not the librarian's
            by_case.setdefault(entry["case"], []).append(entry)
    present = {d["case"]: d for d in decisions if isinstance(d, dict) and "case" in d}
    for case, group in by_case.items():
        _block, errors = blocks.get(case) or then_blocks(cases.get(case, []))
        if case not in texts_of:
            texts_of[case] = case_texts(cases, case)
        gone = case not in cases and all(e.get("superseded_by") for e in group)
        record = decision_record(
            case, group, date, texts_of[case], errors, spec_of.get(case), gone_from_spec=gone
        )
        if case in present:
            present[case]["targets"] = record["targets"]
            present[case]["tags"] = record["tags"]
            for key in ("supersedes", "criterion", "spec"):
                if key in record:
                    present[case][key] = record[key]
        else:
            decisions.append(record)
            present[case] = record
    # a Case whose sub-cases have decision lines gets a record of its own (case 544.6)
    for parent, children in parents_of(list(by_case)).items():
        tags = []
        for child in children:
            for tag in (present.get(child) or {}).get("tags") or []:
                if tag not in tags:
                    tags.append(tag)
        if parent in present:
            present[parent]["children"] = [f"decision-case-{c}" for c in children]
            if parent not in by_case:
                present[parent]["tags"] = tags
            continue
        record = parent_record(parent, children, date, cases, tags, spec_of.get(parent))
        decisions.append(record)
        present[parent] = record
    for decision in decisions:
        for earlier in decision.get("supersedes") or []:
            top = earlier[len("decision-case-") :]
            for key, target in present.items():
                if not in_family(str(key), top):
                    continue  # the tag retires the Case with its sub-cases (case 660.2)
                done = target.setdefault("superseded_by", [])
                if decision["decision"] not in done:
                    done.append(decision["decision"])
    return data, added, elsewhere, failed


def yaml_path(project_dir: Path, unit: str) -> Path:
    return project_dir / "vault" / "raw" / unit / "materialize.yaml"


def load_yaml(path: Path) -> dict | None:
    if not path.exists():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else None


def unit_sprint(project_dir: Path, unit: str, fallback: str | None = None) -> str:
    """The sprint of a unit (cases 743.2, 770): the `sprint` field of its own yaml, stripped,
    else `fallback`, else the first heading of `sprint.md` by `sprint_id`. The one judgment
    that `guppi archive`, `guppi cleanup` and `guppi generate` import."""
    data = load_yaml(yaml_path(project_dir, unit)) or {}
    found = str(data.get("sprint") or "").strip()
    if found:
        return found
    return sprint_id(project_dir) if fallback is None else fallback


def yaml_text(data: dict) -> str:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100)


def dump_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml_text(data), encoding="utf-8", newline="\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi materialize", description=__doc__.split("\n\n")[1])
    p.add_argument(
        "--date", default=None, help="the units of one raw/<date> folder; without it, every unit"
    )
    p.add_argument(
        "--show",
        action="store_true",
        help="print the yaml each date would be written with; write nothing (case 76)",
    )
    return p


def dates_with(project_dir: Path, name: str) -> list[str]:
    """Every `vault/raw/<date>/` that holds `name` at the date level, in date order."""
    raw = project_dir / "vault" / "raw"
    if not raw.is_dir():
        return []
    return sorted(p.name for p in raw.iterdir() if p.is_dir() and (p / name).is_file())


def session_of_run(project_dir: Path, date: str) -> tuple[str, str] | None:
    """`(date, HHMM)` of the session of a run on `date` (case 102.2): the latest `<HHMM>/`
    folder under `raw/<date>/`, and without one the latest of the nearest date back — a
    session across midnight. None when no session folder exists at all."""
    raw = project_dir / "vault" / "raw"
    if not raw.is_dir():
        return None
    for folder in sorted((p for p in raw.iterdir() if p.is_dir() and p.name <= date), reverse=True):
        sessions = sorted(
            p.name for p in folder.iterdir() if p.is_dir() and SESSION_FOLDER.match(p.name)
        )
        if sessions:
            return folder.name, sessions[-1]
    return None


def units_with(project_dir: Path, name: str, date: str | None = None) -> list[str]:
    """Every unit under `vault/raw/` that holds `name` (case 103.2): dates ascending, the
    date-level `<date>` first when the file sits at the date root, then `<date>/<HHMM>` for
    each session folder holding it, in folder order. With `date`, the units of that date."""
    raw = project_dir / "vault" / "raw"
    if not raw.is_dir():
        return []
    dates = [raw / date] if date else sorted(p for p in raw.iterdir() if p.is_dir())
    units: list[str] = []
    for folder in dates:
        if not folder.is_dir():
            continue
        if (folder / name).is_file():
            units.append(folder.name)
        sessions = sorted(
            p for p in folder.iterdir() if p.is_dir() and SESSION_FOLDER.match(p.name)
        )
        units.extend(f"{folder.name}/{p.name}" for p in sessions if (p / name).is_file())
    return units


def is_carried_over(project_dir: Path, unit: str) -> bool:
    """A unit whose folder holds `carry.md` — the mark `/carry` leaves on a session whose
    Spec is ratified and whose work is not done (case 190.3). The walk passes it by:
    its yaml is neither written nor extended; the mark's content is not read."""
    return (project_dir / "vault" / "raw" / unit / "carry.md").is_file()


def materialize_date(project_dir: Path, unit: str, now, stdout, stderr, show=False) -> int:
    """One unit: extend or write its yaml; one line on stdout. Exit 2 on an error of the
    unit itself (nothing written), 1 when a line failed alone and the yaml was written
    without it (case 142.1), else 0. With `show` the yaml goes to stdout instead and no
    file changes (case 76)."""
    try:
        path = yaml_path(project_dir, unit)
        existing = load_yaml(path)
        data, added, elsewhere, failed = assemble(project_dir, unit, existing, stderr)
        if show:
            stdout.write(yaml_text(data))
            return 1 if failed else 0
        dump_yaml(path, data)
        mark_superseded_elsewhere(project_dir, unit, elsewhere)
    except MaterializeError as exc:
        print(f"materialize: {exc}", file=stderr)
        return 2
    except Exception as exc:  # noqa: BLE001 — report, never traceback
        print(f"materialize: materialize.yaml not written: {exc}", file=stderr)
        return 2
    verb = "extended with" if existing else "written with"
    print(
        f"materialize: {path.relative_to(project_dir).as_posix()} {verb} {added} entries",
        file=stdout,
    )
    return 1 if failed else 0


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    units = units_with(project_dir, "ledger.md", args.date)
    if not units:
        what = (
            f"vault/raw/{args.date}/ledger.md does not exist"
            if args.date
            else "no ledger.md under vault/raw/ to read"
        )
        print(f"materialize: {what}", file=stderr)
        return 1
    failed = False
    shown = 0
    for unit in units:
        if is_carried_over(project_dir, unit):  # a conserved session (case 190.3)
            print(
                f"materialize: vault/raw/{unit}/ passed by — carry.md marks its Spec as "
                "ratified and not done",
                file=stdout,
            )
            continue
        if args.show and shown:
            print("---", file=stdout)  # one yaml document per unit (case 76)
        shown += 1
        code = materialize_date(project_dir, unit, now, stdout, stderr, show=args.show)
        if code == 2:  # an error of the unit itself stops the walk (case 142.4)
            return 1
        failed = failed or code == 1  # a failed line: the walk goes on, exit 1 at the end
    return 1 if failed else 0
