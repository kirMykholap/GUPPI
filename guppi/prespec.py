"""`guppi prespec` — the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-spec` has run in this session; `guppi prespec --check <plan> [--session ID]` — the
check of that Plan Mode's artifacts against each other.

The hook reads the event logs by the session's stamp (case 136.2) — the logs from today
back to the date of this session's `session-start`, as the ledger hook reads them, so a
session across midnight keeps its `hi` and its `prespec` (case 213.2): the session is a
working one when the logs hold a `hi` of its stamp. In a working session with no `prespec` line of
the same stamp after that `hi`, the hook exits 2 with the reason on stderr, which Claude
Code shows the agent and which blocks the tool; the agent runs `/pre-spec` — `guppi gate`
writes the stamped line on the Skill call (case 136.1) — and exits Plan Mode again. A mark
of another stamp or `--------` does not count, and a `session-start` of another session
resets nothing. An ordinary session — no `hi` — is not gated: no governance applies there.
Any other tool: exit 0. Rule page: `vault/wiki/rules/rule-prespec-hook.md`.

The check prints one finding per line on stdout and exits 1 on any, 0 when there is none;
a line opening with `note:` is no finding and sets no exit code (case 378.8); without a
`hi` in the session's window it exits 0 with one line on stderr. The
session is `--session`, else `CLAUDE_SESSION_ID`; with neither it exits 2 with one line on
stderr naming the `hi:` line, and nothing is guessed from the event log (case 213.1). The
session's window is the one the ledger hook walks (`ledger.session_dir`):
the ledgers of its dates, on the `hi` date from the `hi` time on, and its folder
`raw/<hi date>/<hi HHMM>/` (case 73). Findings (cases 59.1, 59.2, 59.3, 59.6, 74,
75.2):

- a decision line written since the session's `hi` with no item of its kind under its own
  Case heading of the plan, and an item of a `then` block with no decision line of its Case;
  a `defer` line matches a `defer` item; an Estimate has its own line and its own item (case 189); a nested `estimate` of an
  older Spec is covered by its parent's create line; the lines of a Case a `{supersedes:case
  N}` of the window names need no item — the Case left the plan — and its heading still in
  the plan is a finding of its own (case 299.2); a second item of one kind and slug under one
  Case heading, in one fence tagged `then` or in another, is a finding: one decision line
  covers one item, and `materialize` lifts only the first (case 426);
- the frontier `raw/<hi date>/<hi HHMM>/frontier.md` (case 73.4): missing, an open `[ ]`
  line under `## Cases` — an open line under `## Work` waits for Work Mode and is no finding
  (case 356.1) — a `[x] … · case N` whose heading the plan lacks, a `[-] … · defer case N`
  with no `defer` item under Case N, and one whose source segment is `sprint` — a sprint
  item is never deferred (case 356.2); `sprint` is a closer of its own — an item of the sprint page
  left for a later session — legal on `[-]`, a finding on `[x]` (case 310.6); a line closed
  `· case N` whose source segment — the one standing immediately before the closer — is
  `sprint` needs an `update` of the sprint page `entity-sprint-<id>` under Case N, the
  parent or a sub-case (case 314.2); the word inside the slug of a title is not the source
  (case 335);
- a Case with a line of a kind other than `defer` and no fenced block tagged `tasks` (a
  defer-only Case has no work, case 74); an Estimate a `then` block creates or sets
  `pending` with no task line of its own — a line `- [ ] read `<slug>`` whose first
  backticked slug is that Estimate, matched by `generate.READ_LINE`, the ticker's own
  pattern; a slug named on another Estimate's read line is a finding in its own words, and a
  mention on a line that is not a read line is no task line (case 327);
- an `update` item carrying `file:` — the file route is gone (case 320); the rule that
  governs the path is named when there is one;
- the form of an Estimate item (case 203.1): a Case whose `then` block holds two or more
  Estimate items — a `create`, or an `update` with `set: {status: pending}` — without a
  written `sections: Criterion` (one promise per Case: split it); an `update` of an
  Estimate whose page does not exist; a `create` of an Estimate whose `ref` names neither
  a live rule or entity nor one a `create` of the same plan carries (case 221); a `create` of
  an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the
  four forms lint classifies — by `lint.names_a_form`, the one predicate, the existence of
  the file and of the target left to lint — and a `create` with no `method` at all (case
  331); the keys of the shape before case 189 — `contract`, `estimate_slug` — are not read;
- an item writing a `sections: Render` for a page that enforces by render whose text does
  not open with `<!-- slug -->` and close with `<!-- /slug -->`; only the text the item
  itself writes is judged, and a child's marker line in a parent is not (case 325.1);
- a `replace` anchor of any Case of the plan that misses, or hits more than once, once the
  pairs are applied in entry order to copies of the pages in memory by `generate`'s own
  matching rule, and a `reword` pair no live page holds: the anchor is judged against the
  page as the Spec leaves it, not as it stands today, and nothing is written (case 351);
- a record line of the window — `- decision[`, `- estimate[`, `- lesson[`, timed — that
  `materialize.parse_line` does not read, with its date and line number (case 75.2);
- a `[[slug]]` outside a code span in the plan — in the blockquotes and in the strings of
  the `then` blocks, never in a fence with another tag — that names neither a live or
  archived page, nor a slug a `create` of the same plan carries, nor a hub file of `wiki/`;
  one line per slug and Case (case 264.2);
- a `tasks` line that opens with the bare word `render` or `sprint`, or with the command
  outside a code span — the tickers of `render` and `sprint` match the command in the
  first code span (case 235), a line of another form stays debt (case 279.2);
- a `replace` pair of an Estimate `update` whose `old` stands inside the page's
  `## Criterion`, by `materialize.touches_criterion`, the one predicate — a Criterion
  changes only whole (case 378.4);
- the frame (case 378.7): a slug or path in a code span of a Case's `when` or `then` that
  its `given` — its own or its parent's, by `materialize.case_texts` — does not name, and a
  slug of its `then` block the `given` does not name; a slug is a span with a category
  prefix by `materialize.category_of`, a path a span holding a `/` and one more character;
  a Case without `given` is not checked;
- the ratified copy (case 387.4): beside a plan file with a copy `<plan>.ratified.md`, a Case
  whose `given`, `when`, `then`, `then` block or `tasks` differ from its section there, by
  `ratified.differences` — the one comparison the hooks of `rule-spec-reconcile` use — a Case
  of the plan with no section in the copy, and a section of the copy with no Case in the
  plan, a Case a `{supersedes:case N}` of the window names excepted, and a parent with
  sub-cases in the copy, every one of them named by such a line (case 417), the Cases under
  `## Deferred` not compared; and every name, `context` or `problem` that still holds a
  Cyrillic letter — the agent translates them before the check.

The check after a write (case 414.1): `written_findings` runs the same checks, `judge`, for
the `Stop` hook of `rule-spec-write` on the Cases it wrote, with the decision lines of the
reply added, and without the Frontier, the ratified copy and the grammar of the window.

Notes (case 378.8): a Case whose `given` or `then` holds more than seven `**＋**` lines —
a sign it is not atomic — is one line opening with `note:`, answered in the chat.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi import ratified
from guppi.event import project_root, read_payload, session_stamp
from guppi.generate import (  # the ticker, the pairs, the Frontier line (case 360)
    FRONTIER_LINE,
    FRONTIER_SEPARATOR,
    READ_LINE,
    Vault,
    replace_once,
)
from guppi.ledger import (
    hi_moment,
    hi_recorded,
    session_dir,
    session_event_log,
    session_event_logs,
)
from guppi.lint import CODE_SPAN, WIKILINK, archived_slugs, hub_files, names_a_form
from guppi.materialize import (
    DECISION_KINDS,
    FENCE,
    case_texts,
    category_of,
    find_item,
    parse_line,
    split_cases,
    tagged_blocks,
    then_blocks,
    touches_criterion,
    unquote,
)
from guppi.pages import CATEGORIES, Page, read_category, read_page, wiki_root

TOOL = "ExitPlanMode"
TIMED_RECORD = re.compile(r"^- (\d\d:\d\d:\d\d) (decision|estimate|lesson)\[")
LEAF_CATEGORIES = ("rules", "entities")
LINE_PREVIEW = 80
# `case-schema.md` writes the line as `decision[case_id]…`; `parse_line` reads `[case N]`.
# A bare id is read as the same line rather than skipped (the lines of 2026-09-12).
BARE_CASE = re.compile(r"^(- (?:\d\d:\d\d:\d\d )?decision\[)(?!case )")
WORK_LIST = "## Work"  # the list whose open lines wait for Work Mode (case 356.1)
CLOSERS = re.compile(r"^(work|sprint|kept|case (\S+)|defer case (\S+))$")
SPRINT_SOURCE = "sprint"
KEPT = "kept"  # an item of the brief's Deferred list left as it stands (case 421.3)
DEFERRED_SOURCE = "deferred"
SPRINT_PAGE = "entity-sprint-"
# Case 279.2: a task line the tickers of `render` and `sprint` would not match — the bare
# word, or the command outside a code span, right after the box.
OFF_FORM_LINE = re.compile(r"^- \[[ x]\] (?:uv run )?(?:guppi )?(?:render|sprint)\b")
AND = "**＋**"  # the operand "and" at the head of a line (case 378.6)
LONG_CHAIN = 7  # more `＋` lines than this in `given` or `then` is a note (case 378.8)


def window(event_log: str, stamp: str) -> tuple[bool, bool]:
    """`(hi, prespec)`: whether the log holds a `hi` of this session's stamp, and a `prespec`
    of the same stamp after it (case 136.2). A mark of another stamp or `--------` does not
    count, and a `session-start` of another session resets nothing: the marks bind by stamp,
    not by position."""
    seen_hi = seen_prespec = False
    for line in event_log.splitlines():
        parts = line.split(" ", 3)
        if len(parts) < 4 or parts[0] != "-" or parts[2] != stamp:
            continue
        event = parts[3].split(" ", 1)[0]
        if event == "hi":
            seen_hi = True
        elif event == "prespec" and seen_hi:
            seen_prespec = True
    return seen_hi, seen_prespec


# --- the session's window -------------------------------------------------------------


NO_SESSION = "prespec: no session id; pass --session <stamp> from the hi: line"


def resolve_session(option: str | None) -> str | None:
    """The stamp of `--session`, else of `CLAUDE_SESSION_ID`; None with neither. The last
    `session-start` of today's log was the fallback until case 213.1: a foreign start beside
    a parallel session, none after midnight — the session is never guessed."""
    if option:
        return session_stamp(option, {})
    env = os.environ.get("CLAUDE_SESSION_ID")
    if env:
        return session_stamp(env, {})
    return None


def window_lines(project_dir: Path, hi: tuple[str, str], today: str) -> list[tuple]:
    """`(unit, line number, line)` of every timed record line of the session's window: the
    session's own ledger `raw/<hi date>/<hi HHMM>/ledger.md` whole (case 103.4), then the
    date-level ledgers from the `hi` date to today, on the `hi` date from the `hi` time on,
    while any exist. A line before the `hi` in a date-level ledger, or without a time, is
    not read. `unit` is `<date>/<HHMM>` or `<date>`, so `raw/<unit>/ledger.md` names the
    file."""
    hi_date, hi_time = hi
    raw = project_dir / "vault" / "raw"
    lines: list[tuple] = []
    session = raw / hi_date / (hi_time[:2] + hi_time[3:5]) / "ledger.md"
    if session.exists():
        for number, line in enumerate(session.read_text(encoding="utf-8").splitlines(), 1):
            if TIMED_RECORD.match(line):
                lines.append((f"{hi_date}/{session.parent.name}", number, line))
    folders = sorted(d for d in raw.iterdir() if d.is_dir()) if raw.is_dir() else []
    for folder in folders:
        day = folder.name
        path = folder / "ledger.md"
        if day < hi_date or day > today or not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = TIMED_RECORD.match(line)
            if not match or (day == hi_date and match.group(1) < hi_time):
                continue
            lines.append((day, number, line))
    return lines


def session_decisions(lines: list[tuple]) -> list[dict]:
    """The decision records among the window's lines; a bare case id is read as `case N`
    and the grammar check (75.2) reports it."""
    records: list[dict] = []
    for _, _, line in lines:
        if TIMED_RECORD.match(line).group(2) != "decision":
            continue
        record = parse_line(BARE_CASE.sub(r"\1case ", line))
        if record is not None:
            records.append(record)
    return records


def check_grammar(lines: list[tuple]) -> list[str]:
    """75.2: every record line of the window goes through `materialize.parse_line`; one
    that returns None is a finding with its file and line number."""
    findings: list[str] = []
    for day, number, line in lines:
        if parse_line(line) is None:
            text = line.strip()[:LINE_PREVIEW]
            findings.append(f"raw/{day}/ledger.md:{number}: does not parse: {text}")
    return findings


# --- the plan ---------------------------------------------------------------------------


def items_of(block: dict) -> list[dict]:
    """Every decision item of a `then` block as `{kind, slug, file, nested}`; a nested
    `estimate` of a create is a create item with `nested` set, covered by its parent's
    line: a Leaf's Estimate has no line of its own (case 72.5); `new_tags` are not items."""
    items: list[dict] = []
    for kind in DECISION_KINDS:
        for item in block.get(kind) or []:
            if not isinstance(item, dict):
                continue
            items.append(
                {"kind": kind, "slug": item.get("slug"), "file": item.get("file"), "nested": False}
            )
            nested = item.get("estimate") if kind == "create" else None
            if isinstance(nested, dict) and nested.get("slug"):
                items.append(
                    {"kind": "create", "slug": nested["slug"], "file": None, "nested": True}
                )
    return items


def same_path(a, b) -> bool:
    if not a or not b:
        return False
    norm = [str(p).replace("\\", "/").removeprefix("./") for p in (a, b)]
    return norm[0] == norm[1]


def item_name(entry: dict) -> str:
    return str(entry["slug"] or entry["file"] or "?")


def line_has_item(block: dict, record: dict) -> bool:
    return find_item(block, record["kind"], record["slug"])[0] is not None


def item_has_line(entry: dict, records: list[dict]) -> bool:
    for record in records:
        if record["kind"] != entry["kind"]:
            continue
        if entry["slug"] and record["slug"] == entry["slug"]:
            return True
    return False


def superseded_in_window(records: list[dict]) -> dict[str, str]:
    """299.2: the Cases a `{supersedes:case N}` of the window names, each with the Case that
    superseded it — a Case superseded in its own session leaves the plan."""
    by: dict[str, str] = {}
    for record in records:
        for earlier in record.get("supersedes") or []:  # one block per Case (case 429)
            by.setdefault(str(earlier), str(record["case"]))
    return by


def check_lines(cases: dict, blocks: dict, records: list[dict]) -> list[str]:
    """59.1: every line has its item under its own Case; every item has its line, a nested
    estimate through its parent's create line. 299.2: a Case superseded by a line of the
    window needs no item, and its heading still in the plan is a finding. 426: a second item
    of one kind and slug under one Case heading, in one fence tagged `then` or in another, is
    a finding — one decision line covers one item, and `materialize` lifts only the first."""
    findings: list[str] = []
    superseded = superseded_in_window(records)
    for case, by in superseded.items():
        if case in cases:
            findings.append(f"case {case}: superseded by case {by}, still in the plan")
    for record in records:
        case, tag = record["case"], f"[{record['kind']}][{record['slug']}]"
        if case in superseded:  # its work stands under the superseding Case
            continue
        if case not in cases:
            findings.append(f"case {case}: line {tag}: no Case {case} heading in the plan")
        elif not line_has_item(blocks[case], record):
            findings.append(f"case {case}: line {tag} has no item in the plan")
    for case, block in blocks.items():
        of_case = [r for r in records if r["case"] == case]
        seen: set[tuple[str, str]] = set()
        for entry in items_of(block):
            tag = (entry["kind"], item_name(entry))
            if not entry["nested"] and tag in seen:  # materialize lifts only the first (426)
                findings.append(
                    f"case {case}: item [{tag[0]}][{tag[1]}] stands twice — one entry per target"
                )
                continue
            seen.add(tag)
            if not entry["nested"] and not item_has_line(entry, of_case):
                findings.append(
                    f"case {case}: item [{entry['kind']}][{item_name(entry)}] has no decision line"
                )
    return findings


def updates_the_sprint(blocks: dict, case: str) -> bool:
    """Case 314.2: an `update` of the sprint page `entity-sprint-<id>` under Case N — the
    parent or any of its sub-cases."""
    for key, block in blocks.items():
        if key != case and not key.startswith(f"{case}."):
            continue
        for item in (block or {}).get("update") or []:
            if isinstance(item, dict) and str(item.get("slug") or "").startswith(SPRINT_PAGE):
                return True
    return False


def check_frontier(path: Path, relative: str, cases: dict, blocks: dict) -> list[str]:
    """59.2: the frontier of the session's folder (73.4), every line closed by a Case the
    plan holds. Case 310.6: `sprint` is a closer of its own — a line of the sprint page left
    for a later session — legal on a `[-]` box and a finding on an `[x]`. Case 314.2: a line
    closed `case N` whose source segment — the one standing immediately before the closer —
    is `sprint` needs an `update` of the sprint page under Case N; the word inside the slug
    of a title is not the source, and six live Estimates carry it there (case 335). Case
    356.1: an open line under `## Work` is no finding — its work waits for Work Mode; a closed
    one is checked as any. Case 356.2: a line whose source segment is `sprint` closed `defer
    case N` is a finding — a sprint item left for later closes `[-]` with `sprint`. Case 421.3:
    `kept` is clean on a `[-]` box after the source `deferred` — an item of the brief's
    Deferred list left as it stands, no Case — and a finding on `[x]` or after another source."""
    if not path.exists():
        return [f"frontier: {relative} is missing"]
    findings: list[str] = []
    work = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            work = line.strip() == WORK_LIST
            continue
        match = FRONTIER_LINE.match(line)
        if not match:
            continue
        box, item, rest = match.groups()
        if box == " ":
            if not work:
                findings.append(f"frontier: {item} is open")
            continue
        segments = [s.strip() for s in rest.split(FRONTIER_SEPARATOR)]
        closer = CLOSERS.match(segments[-1])
        if closer is None:
            findings.append(
                f"frontier: {item} is closed without case N, work, sprint, kept or defer case N"
            )
        elif closer.group(1) == KEPT:
            if box == "x" or segments[-2:-1] != [DEFERRED_SOURCE]:
                findings.append(
                    f"frontier: {item} closes with kept; only an item of the brief's Deferred "
                    "list, source deferred, closes [-] with kept"
                )
        elif closer.group(1) == SPRINT_SOURCE:
            if box == "x":
                findings.append(
                    f"frontier: {item} closes [x] with sprint; an item left for later is [-]"
                )
        elif closer.group(2) is not None:
            case = closer.group(2)
            if case not in cases:
                findings.append(
                    f"frontier: {item} closes with case {case}, no Case {case} heading in the plan"
                )
            elif segments[-2:-1] == [SPRINT_SOURCE] and not updates_the_sprint(blocks, case):
                findings.append(
                    f"frontier: {item} closes a sprint item with case {case}, "
                    f"no update of the sprint page under Case {case}"
                )
        elif closer.group(3) is not None and segments[-2:-1] == [SPRINT_SOURCE]:
            findings.append(
                f"frontier: {item} defers a sprint item; an item left for later closes [-] with sprint"
            )
        elif closer.group(3) is not None:
            case = closer.group(3)
            defers = blocks.get(case, {}).get("defer") or []
            if not any(isinstance(d, dict) for d in defers):
                findings.append(
                    f"frontier: {item} defers to case {case}, no defer item under Case {case}"
                )
    return findings


def estimates_to_read(block: dict) -> list[str]:
    """The Estimates a `then` block creates or sets `pending`, by slug. An `update` that
    carries `rename` gives the slug of its `rename`: after `generate` the page lives under
    it, the reading names it, and `tick_read` ticks the read line by it (case 432)."""
    slugs: list[str] = []
    for entry in items_of(block):
        if entry["kind"] == "create" and str(entry["slug"] or "").startswith("estimate-"):
            slugs.append(entry["slug"])
    for item in block.get("update") or []:
        if not isinstance(item, dict) or not str(item.get("slug") or "").startswith("estimate-"):
            continue
        set_fields = item.get("set")
        if isinstance(set_fields, dict) and set_fields.get("status") == "pending":
            slugs.append(str(item.get("rename") or item["slug"]))
    return slugs


def check_tasks(cases: dict, blocks: dict, records: list[dict]) -> list[str]:
    """59.3: a ratified Case has a `tasks` block; an Estimate to read has its task line — a
    line `- [ ] read `<slug>`` whose first backticked slug is that Estimate, matched by
    `generate.READ_LINE`, the ticker's own pattern, so the check judges as the ticker ticks.
    A slug named on another Estimate's read line has no line of its own and is a finding in
    its own words; a mention on an `update` line, or on any line that is not a read line, is
    no task line (case 327). 279.2: a render or sprint line is in the form the tickers
    match."""
    findings: list[str] = []
    superseded = superseded_in_window(records)  # a superseded Case has no work here (299.2)
    with_work = {
        r["case"] for r in records if r.get("kind") != "defer" and r["case"] not in superseded
    }
    for case, lines in cases.items():
        tasks = "\n".join(tagged_blocks(lines, "tasks"))
        if case in with_work and not tasks:  # a defer-only Case has no work, case 74
            findings.append(f"case {case}: decision lines and no tasks block")
        read_lines = [line for line in tasks.splitlines() if READ_LINE.match(line)]
        of_their_own = {READ_LINE.match(line).group(1) for line in read_lines}  # case 327
        for slug in estimates_to_read(blocks[case]):
            if slug in of_their_own:
                continue
            if any(slug in line for line in read_lines):
                findings.append(f"case {case}: {slug} is named on another read line, not its own")
            else:
                findings.append(f"case {case}: {slug} has no task line")
        for line in tasks.splitlines():
            if OFF_FORM_LINE.match(line):
                findings.append(f"case {case}: render line off form: {line}")
    return findings


def governed_paths(project_dir: Path) -> dict[str, str]:
    """`governs` path → rule slug, over the live Rule pages."""
    paths: dict[str, str] = {}
    for page in read_category(wiki_root(project_dir), "rules"):
        if page.props.get("status") == "archived":
            continue
        governs = page.props.get("governs")
        for path in governs if isinstance(governs, list) else [governs]:
            if path:
                paths[str(path).replace("\\", "/").removeprefix("./")] = page.slug
    return paths


def check_governed(blocks: dict, governed: dict[str, str]) -> list[str]:
    """Case 320: an `update` item carrying `file` — the file route is gone; every file of
    the vault is a page, the Render of a page or a record a script keeps. A path a live
    Rule page governs is named with its rule (59.6)."""
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            file = item.get("file") if isinstance(item, dict) else None
            if not file:
                continue
            key = str(file).replace("\\", "/").removeprefix("./")
            rule = governed.get(key)
            by = f", governed by {rule}" if rule else ""
            findings.append(f"case {case}: file {file}{by}; the file route is gone (case 320)")
    return findings


def written_criterion(item: dict) -> bool:
    """Whether the item signs its own Criterion under `sections` (cases 194.1, 204)."""
    sections = item.get("sections")
    return isinstance(sections, dict) and bool(str(sections.get("Criterion") or "").strip())


def live_page(project_dir: Path, slug: str) -> bool:
    category = category_of(slug)
    return bool(category) and (wiki_root(project_dir) / category / f"{slug}.md").exists()


NO_FORM = 'method names no form — a make target, pytest, a tests/ file or "by hand"'


def check_pairs(cases: dict, blocks: dict, project_dir: Path) -> list[str]:
    """The `replace` and `reword` pairs of every Case of the plan, applied in entry order to
    copies of the pages in memory by `generate`'s own matching rule — `replace_once`, the
    tokens of the anchor joined by one `\\s+` — and nothing written to disk. A `replace`
    anchor that misses, or hits more than once, is one finding with its Case, the page's slug
    and the opening of its `old`; a `reword` pair no live page holds is one too. The anchor is
    judged against the page as the Spec leaves it, not as it stands today: a pair of a later
    Case sees what an earlier one wrote, which is how the pairs of one Spec collide (314.2
    against 310.6). The meaning of the words in their place is not judged here (case 351)."""
    findings: list[str] = []
    pages: dict[str, Page | None] = {}
    every_page = False

    def load(slug: str) -> Page | None:
        if slug not in pages:
            category = category_of(slug)
            path = wiki_root(project_dir) / category / f"{slug}.md" if category else None
            pages[slug] = read_page(path, category) if path and path.exists() else None
        return pages[slug]

    def load_every() -> None:
        nonlocal every_page
        if every_page:
            return
        for category in CATEGORIES:
            folder = wiki_root(project_dir) / category
            for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
                if path.stem != "schema" and path.stem not in pages:
                    pages[path.stem] = read_page(path, category)
        every_page = True

    for case in cases:
        for item in blocks.get(case, {}).get("update") or []:
            if not isinstance(item, dict):
                continue
            slug = str(item.get("slug") or "")
            for pair in item.get("replace") or []:
                if not isinstance(pair, dict):
                    continue
                old = str(pair.get("old") or "")
                page = load(slug)
                if page is None or page.error or not old:
                    continue
                hits = replace_once(page, old, str(pair.get("new") or ""))
                if hits == 1:
                    continue
                what = "is not in the page" if not hits else f"hits {hits} times"
                findings.append(f"case {case}: {slug}: a replace anchor {what}: {preview(old)}")
            for pair in item.get("reword") or []:
                if not isinstance(pair, dict):
                    continue
                old, new = str(pair.get("old") or ""), str(pair.get("new") or "")
                if not old:
                    continue
                load_every()
                touched = sum(Vault.reword_text(page, old, new) for page in pages.values() if page)
                if not touched:
                    findings.append(
                        f"case {case}: {slug}: a reword pair hits no live page: {preview(old)}"
                    )
    return findings


def preview(text: str) -> str:
    """The opening of an anchor, whitespace collapsed, for a finding's one line."""
    one_line = " ".join(text.split())
    return one_line if len(one_line) <= LINE_PREVIEW else one_line[:LINE_PREVIEW] + "…"


def enforcement_of(item: dict, kind: str, project_dir: Path) -> str:
    """How the target forces its rule: in a `create` the field stands in the item itself,
    since no page exists yet; in an `update` it is read from the page (case 325.1)."""
    if kind == "create":
        return str(item.get("enforcement") or "")
    slug = str(item.get("slug") or "")
    category = category_of(slug)
    if not category:
        return ""
    path = wiki_root(project_dir) / category / f"{slug}.md"
    if not path.exists():
        return ""
    return str(read_page(path, category).props.get("enforcement") or "")


def check_markers(blocks: dict, project_dir: Path) -> list[str]:
    """An item that writes a `Render` section for a page which enforces by render carries the
    page's own markers: the text opens with `<!-- slug -->` and closes with `<!-- /slug -->`,
    or it is one finding. Only the text the item itself writes is judged — the Spec is not
    simulated in entry order, and a child's marker line inside a parent's Render is not
    checked, since its value is known only once every item is applied (case 325.1)."""
    findings: list[str] = []
    for case, block in blocks.items():
        for kind in ("create", "update"):
            for item in block.get(kind) or []:
                if not isinstance(item, dict):
                    continue
                sections = item.get("sections")
                if not isinstance(sections, dict):
                    continue
                text = str(sections.get("Render") or "").strip()
                slug = str(item.get("slug") or "")
                if not text or not slug:
                    continue
                if enforcement_of(item, kind, project_dir) != "render":
                    continue
                if text.startswith(f"<!-- {slug} -->") and text.endswith(f"<!-- /{slug} -->"):
                    continue
                findings.append(
                    f"case {case}: {kind} {slug}: Render is not wrapped in "
                    f"<!-- {slug} --> … <!-- /{slug} -->"
                )
    return findings


def check_form(blocks: dict, project_dir: Path) -> list[str]:
    """The form of an Estimate item (case 203.1): a Case whose `then` block holds two or
    more Estimate items — a `create`, or an `update` with `set: {status: pending}` — without
    a written `sections: Criterion` is one promise too many (split it); an `update` of an
    Estimate whose page does not exist, and a `create` of an Estimate whose `ref` names
    neither a live rule or entity nor a rule or entity a `create` item of the same plan
    carries (case 221), are each a finding. A `create` of an Estimate, or an `update`
    carrying `set: {method: …}`, whose `method` names none of the four forms lint
    classifies — by `lint.names_a_form`, the one predicate — is a finding too; a `create`
    with no `method` at all is the same one, and the existence of the file and of the target
    is left to lint, since the test file is written in Work Mode (case 331). The branch of a
    MOC stays with lint. The keys of the shape before case 189 — `contract`,
    `estimate_slug` — are not read."""
    findings: list[str] = []
    created = {  # the rules and entities the plan itself creates (case 221)
        str(item.get("slug"))
        for block in blocks.values()
        for item in block.get("create") or []
        if isinstance(item, dict) and category_of(str(item.get("slug") or "")) in LEAF_CATEGORIES
    }
    for case, block in blocks.items():
        promises = 0
        for item in block.get("create") or []:
            slug = item.get("slug") if isinstance(item, dict) else None
            if not slug or category_of(slug) != "estimates":
                continue
            if not written_criterion(item):
                promises += 1
            ref = str(item.get("ref") or "")
            if category_of(ref) not in LEAF_CATEGORIES or not (
                live_page(project_dir, ref) or ref in created
            ):
                findings.append(f"case {case}: create {slug}: ref {ref or '?'} names no live page")
            if not names_a_form(str(item.get("method") or "")):  # case 331
                findings.append(f"case {case}: create {slug}: {NO_FORM}")
        for item in block.get("update") or []:
            slug = item.get("slug") if isinstance(item, dict) else None
            if not slug or category_of(slug) != "estimates":
                continue
            set_fields = item.get("set")
            pending = isinstance(set_fields, dict) and set_fields.get("status") == "pending"
            if pending and not written_criterion(item):
                promises += 1
            if not live_page(project_dir, slug):
                findings.append(f"case {case}: update {slug}: no such Estimate page")
            method = set_fields.get("method") if isinstance(set_fields, dict) else None
            if method is not None and not names_a_form(str(method)):  # case 331
                findings.append(f"case {case}: update {slug}: {NO_FORM}")
        if promises >= 2:
            findings.append(f"case {case}: two promises in one Case — split it")
    return findings


def check_criterion_pairs(blocks: dict, project_dir: Path) -> list[str]:
    """378.4: a `replace` pair of an Estimate `update` whose `old` stands inside the page's
    `## Criterion` — judged by `materialize.touches_criterion`, the predicate `materialize`
    marks `incomplete: [criterion]` by; a Criterion changes only whole."""
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            slug = str(item.get("slug") or "") if isinstance(item, dict) else ""
            if category_of(slug) != "estimates":
                continue
            for pair in item.get("replace") or []:
                if touches_criterion(project_dir, slug, [pair]):
                    findings.append(
                        f"case {case}: update {slug}: a replace pair inside the Criterion — "
                        f"a Criterion changes only whole: {preview(str(pair.get('old') or ''))}"
                    )
    return findings


# --- the frame of a Case (cases 378.7, 378.8) ------------------------------------------


def frame_name(span: str) -> bool:
    """Whether a code span names a thing the frame must hold: a slug with a category prefix,
    or a path — a `/` and one more character, a slash command included (case 378.7)."""
    return bool(category_of(span)) or ("/" in span and len(span) > 1)


def item_slugs(block: dict) -> list[str]:
    return [
        str(item["slug"])
        for kind in DECISION_KINDS
        for item in block.get(kind) or []
        if isinstance(item, dict) and item.get("slug")
    ]


def check_frame(cases: dict, blocks: dict) -> list[str]:
    """378.7: `when` and `then` name only what `given` names, and every slug of the `then`
    block stands in `given`; a sub-case reads its parent's `given` by `case_texts`; a Case
    without `given` — a defer, an older Spec — is not checked. One finding per name."""
    findings: list[str] = []
    for case in cases:
        texts = case_texts(cases, case)
        given = texts.get("given") or ""
        if not given:
            continue
        named: list[str] = []
        for section in ("when", "then"):
            for span in CODE_SPAN.findall(texts.get(section) or ""):
                name = span.strip("`").strip()
                if frame_name(name) and name not in named:
                    named.append(name)
        for slug in item_slugs(blocks.get(case, {})):
            if slug not in named:
                named.append(slug)
        for name in named:
            if name not in given:
                findings.append(f"case {case}: {name} is not named in its given")
    return findings


def chain_notes(cases: dict) -> list[str]:
    """378.8: a Case whose own `given` or `then` holds more than seven `＋` lines — a sign
    it is not atomic; a note, not a finding."""
    notes: list[str] = []
    for case in cases:
        texts = case_texts(cases, case)
        for section in ("given", "then"):
            count = sum(
                1 for line in (texts.get(section) or "").splitlines() if line.startswith(AND)
            )
            if count > LONG_CHAIN:
                notes.append(
                    f"note: case {case}: {section} holds {count} ＋ lines — is the Case atomic?"
                )
    return notes


# --- a bare wikilink in the plan (case 264.2) -------------------------------------------


def plan_prose(lines: list[str]) -> list[str]:
    """The lines of a Case a `[[slug]]` is read from: the ones outside any fence and the
    ones inside a fence tagged `then`; a fence with another tag or none is skipped."""
    out: list[str] = []
    fence_open = reading = False
    for raw in lines:
        line = unquote(raw)
        match = FENCE.match(line)
        if match:
            if not fence_open:
                fence_open, reading = True, match.group(1).lower() == "then"
            else:
                fence_open = False
            continue
        if not fence_open or reading:
            out.append(line)
    return out


def known_slugs(project_dir: Path) -> set[str]:
    """What a `[[…]]` may name: a live page, an archived page, a hub file (case 149.3)."""
    wiki = wiki_root(project_dir)
    live = {p.stem for category in CATEGORIES for p in (wiki / category).glob("*.md")}
    return live | archived_slugs(wiki) | hub_files(wiki)


def check_bare_links(cases: dict, blocks: dict, project_dir: Path) -> list[str]:
    """264.2: a `[[slug]]` outside a code span in the plan — in the blockquotes and in the
    strings of the `then` blocks — that names neither a live or archived page, nor a slug a
    `create` of the same plan carries, nor a hub file of `wiki/`; one line per slug and
    Case. The text would reach a page as it stands, and lint would read it as a broken
    link (cases 130.1, 140, 160, 262)."""
    known = known_slugs(project_dir)
    created = {
        str(item.get("slug"))
        for block in blocks.values()
        for item in block.get("create") or []
        if isinstance(item, dict) and item.get("slug")
    }
    findings: list[str] = []
    for case, lines in cases.items():
        seen: set[str] = set()
        prose = CODE_SPAN.sub("", "\n".join(plan_prose(lines)))
        for slug in WIKILINK.findall(prose):
            slug = slug.strip()
            if slug in known or slug in created or slug in seen:
                continue
            seen.add(slug)
            findings.append(f"case {case}: [[{slug}]] outside a code span names no page")
    return findings


def check_ratified(plan: str, plan_file: Path | None, records: list[dict]) -> list[str]:
    """387.4: the plan against its ratified copy `<plan>.ratified.md` by `ratified.differences`,
    the one comparison — a Case that differs in what the scripts apply, a Case with no section
    in the copy, a section of the copy with no Case in the plan, a Case a `{supersedes:case N}`
    of the window names excepted, and a parent with sub-cases in the copy, every one of them
    named by such a line, which left the plan with them (case 417); then every name, `context`
    or `problem` of the plan that still holds a Cyrillic letter. No copy — a plan written
    before case 387 — no comparison."""
    findings: list[str] = []
    copy = ratified.copy_of(plan_file) if plan_file is not None else None
    if copy is not None and copy.is_file():
        text = copy.read_text(encoding="utf-8")
        superseded = superseded_in_window(records)
        for case, parts in ratified.differences(plan, text).items():
            findings.append(f"case {case}: differs from its ratified copy in {', '.join(parts)}")
        ours, theirs = ratified.outside_deferred(plan), ratified.outside_deferred(text)
        findings += [
            f"case {case}: no section in the ratified copy" for case in ours if case not in theirs
        ]

        def left(case: str) -> bool:
            subs = [other for other in theirs if other.startswith(case + ".")]
            return case in superseded or (bool(subs) and all(s in superseded for s in subs))

        findings += [
            f"case {case}: in the ratified copy, not in the plan"
            for case in theirs
            if case not in ours and not left(case)
        ]
    findings += [
        f"case {case}: its {part} still holds Cyrillic — translate it"
        for case, part in ratified.untranslated(plan)
    ]
    return findings


def judge(
    plan: str,
    project_dir: Path,
    records: list[dict],
    lines: list[tuple] | None = None,
    frontier: tuple[Path, str] | None = None,
) -> list[str]:
    """The checks of `--check` on the plan's Cases, in the order they print. `lines`, the
    window's record lines, adds their grammar (75.2); `frontier`, its path and the name a
    finding gives it, adds the Frontier (59.2). The check after a write passes neither, and
    the comparison with the ratified copy stays with `check` (case 414.1)."""
    cases = split_cases(plan)
    blocks: dict[str, dict] = {}
    findings: list[str] = []
    for case, case_lines in cases.items():
        blocks[case], errors = then_blocks(case_lines)
        findings += [f"case {case}: {e}" for e in errors]
    if lines is not None:
        findings += check_grammar(lines)
    findings += check_lines(cases, blocks, records)
    if frontier is not None:
        findings += check_frontier(frontier[0], frontier[1], cases, blocks)
    findings += check_tasks(cases, blocks, records)
    findings += check_governed(blocks, governed_paths(project_dir))
    findings += check_form(blocks, project_dir)
    findings += check_markers(blocks, project_dir)
    findings += check_pairs(cases, blocks, project_dir)
    findings += check_bare_links(cases, blocks, project_dir)
    findings += check_criterion_pairs(blocks, project_dir)
    findings += check_frame(cases, blocks)
    return findings


def check(
    plan: str, project_dir: Path, stamp: str, now, stdout, stderr, plan_file: Path | None = None
) -> int:
    logs = session_event_logs(project_dir, now, stamp)
    hi = hi_moment(logs, stamp)
    folder = session_dir(project_dir, now, stamp)
    if hi is None or folder is None or not hi_recorded("".join(t for _, t in logs), stamp):
        print(f"prespec: no hi recorded for session {stamp}; nothing checked", file=stderr)
        return 0
    lines = window_lines(project_dir, hi, now.date().isoformat())
    records = session_decisions(lines)
    relative = folder.relative_to(project_dir).as_posix() + "/frontier.md"
    findings = judge(plan, project_dir, records, lines, (folder / "frontier.md", relative))
    findings += check_ratified(plan, plan_file, records)
    for line in findings + chain_notes(split_cases(plan)):
        print(line, file=stdout)
    return 1 if findings else 0


FINDING_CASE = re.compile(r"^case (\S+?):")


def written_findings(
    plan: str, written: set[str], project_dir: Path, stamp: str, now, extra: list[dict]
) -> list[str]:
    """Case 414.1: the findings of `judge` on the Cases the `Stop` hook of `rule-spec-write`
    wrote in one run and on their sub-cases, a finding of another Case left out. The records
    are the window's decision lines and `extra`, the lines of the reply itself, each once: the
    ledger hook runs in parallel on the same `Stop`, so `ledger.md` may not hold them yet. No
    Frontier, no ratified copy, no grammar of the window: they stay with `/pre-spec`."""
    hi = hi_moment(session_event_logs(project_dir, now, stamp), stamp)
    lines = window_lines(project_dir, hi, now.date().isoformat()) if hi else []
    records: list[dict] = []
    seen: set[str] = set()
    for record in session_decisions(lines) + list(extra):
        key = json.dumps(record, sort_keys=True)
        if key not in seen:
            seen.add(key)
            records.append(record)

    def ours(finding: str) -> bool:
        match = FINDING_CASE.match(finding)
        case = match.group(1) if match else ""
        return any(case == w or case.startswith(w + ".") for w in written)

    return [f for f in judge(plan, project_dir, records) if ours(f)]


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi prespec", description=__doc__.split("\n\n")[1])
    p.add_argument("--check", metavar="PLAN", help="the plan file to check against the session")
    p.add_argument("--session", default=None, help="session id; else CLAUDE_SESSION_ID or the log")
    return p


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    if argv:
        args = parser().parse_args(argv)
        if not args.check:
            parser().print_usage(stderr)
            return 2
        plan_file = Path(args.check)
        if not plan_file.is_file():
            print(f"prespec: no plan file at {plan_file}", file=stderr)
            return 2
        plan = plan_file.read_text(encoding="utf-8")
        stamp = resolve_session(args.session)
        if stamp is None:
            print(NO_SESSION, file=stderr)
            return 2
        return check(plan, project_dir, stamp, now, stdout, stderr, plan_file)
    try:
        payload = read_payload(stdin)
        if payload.get("tool_name") != TOOL:
            return 0
        stamp = session_stamp(None, payload)
        # the logs from today back to this session's start, as the ledger hook reads them,
        # so yesterday's `hi` and `prespec` are found after midnight (case 213.2)
        hi, done = window(session_event_log(project_dir, now, stamp), stamp)
        if hi and not done:
            print(
                f"prespec: Plan Mode is closing without /pre-spec in session {stamp}. "
                "Run /pre-spec, then exit Plan Mode again.",
                file=stderr,
            )
            return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"prespec: check skipped: {exc}", file=stderr)
    return 0
