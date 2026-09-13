"""`guppi pretask` — the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-task` has run in this session; `guppi pretask --check <plan> [--session ID]` — the
check of that Plan Mode's artifacts against each other.

The hook reads the event log the way the ledger hook does: the session is a working one
when a `hi` follows its last `session-start`. In a working session with no `pretask` line
after that `hi`, the hook exits 2 with the reason on stderr, which Claude Code shows the
agent and which blocks the tool; the agent runs `/pre-task` (whose skill records the line)
and exits Plan Mode again. An ordinary session — no `hi` — is not gated: no governance
applies there. Any other tool: exit 0. Rule page: `vault/wiki/rules/rule-pretask-hook.md`.

The check prints one finding per line on stdout and exits 1 on any, 0 and silent when
clean; without a `hi` in the session's window it exits 0 with one line on stderr. The
session is `--session`, else `CLAUDE_SESSION_ID`, else the last `session-start` of today's
event log. The session's window is the one the ledger hook walks (`ledger.session_dir`):
the ledgers of its dates, on the `hi` date from the `hi` time on, and its folder
`raw/<hi date>/<hi HHMM>/` (case 73). Findings (cases 59.1, 59.2, 59.3, 59.6, 72.5, 74,
75.2):

- a decision line written since the session's `hi` with no item of its kind under its own
  Case heading of the plan, and an item of a `then` block with no decision line of its Case;
  a `defer` line matches a `defer` item, a Rule-class `file` line an `update` with that
  `file`; a Leaf's Estimate has no line of its own (case 72.5), so a nested `estimate` of an
  older Spec is covered by its parent's create line;
- the frontier `raw/<hi date>/<hi HHMM>/frontier.md` (case 73.4): missing, an open `[ ]`
  line, a `[x] … · case N` whose heading the plan lacks, a `[-] … · defer case N` with no
  `defer` item under Case N;
- a Case with a line of a kind other than `defer` and no fenced block tagged `tasks` (a
  defer-only Case has no work, case 74); an Estimate a `then` block creates or sets
  `pending` that no line of the Case's `tasks` names;
- an `update` item with `file:` on a path a live Rule page `governs`;
- the form of a Leaf item (case 72.5): a `create` of a Leaf Rule or Entity without
  `method`; an `update` of one whose page is a Leaf without `contract`; a Case with two or
  more Leaf items that create or say `contract: changed` (split it); a create with `method`
  whose derived Estimate slug — `estimate-` + the target's slug minus its category prefix —
  names an existing page and no `estimate_slug` on the item;
- a record line of the window — `- decision[`, `- estimate[`, `- lesson[`, timed — that
  `materialize.parse_line` does not read, with its date and line number (case 75.2).
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import log_path, project_root, read_payload, session_stamp
from guppi.ledger import hi_moment, hi_recorded, session_dir, session_event_logs
from guppi.materialize import (
    DECISION_KINDS,
    FENCE,
    category_of,
    find_item,
    page_exists,
    parse_line,
    rule_class_path,
    split_cases,
    then_blocks,
    unquote,
)
from guppi.pages import read_category, read_page, wiki_root

TOOL = "ExitPlanMode"
TIMED_RECORD = re.compile(r"^- (\d\d:\d\d:\d\d) (decision|estimate|lesson)\[")
LEAF_CATEGORIES = ("rules", "entities")
LINE_PREVIEW = 80
# `case-schema.md` writes the line as `decision[case_id]…`; `parse_line` reads `[case N]`.
# A bare id is read as the same line rather than skipped (the lines of 2026-09-12).
BARE_CASE = re.compile(r"^(- (?:\d\d:\d\d:\d\d )?decision\[)(?!case )")
FRONTIER_LINE = re.compile(r"^- \[([ x-])\] (\S+)(.*)$")
FRONTIER_SEPARATOR = " · "
CLOSERS = re.compile(r"^(work|case (\S+)|defer case (\S+))$")


def window(event_log: str, stamp: str) -> tuple[bool, bool]:
    """`(hi, pretask)`: whether this session's window holds a `hi`, and a `pretask` after it."""
    ours = seen_hi = seen_pretask = False
    for line in event_log.splitlines():
        parts = line.split(" ", 3)
        if len(parts) < 4 or parts[0] != "-":
            continue
        session, event = parts[2], parts[3].split(" ", 1)[0]
        if event == "session-start" and session != stamp:
            ours = seen_hi = seen_pretask = False
        elif event == "session-start":
            ours = True
        elif event == "hi" and ours:
            seen_hi = True
        elif event == "pretask" and seen_hi:
            seen_pretask = True
    return seen_hi, seen_pretask


# --- the session's window -------------------------------------------------------------


def last_session_start(event_log: str) -> str | None:
    """The stamp of the last `session-start` line of an event log."""
    stamp = None
    for line in event_log.splitlines():
        parts = line.split(" ", 3)
        if len(parts) >= 4 and parts[0] == "-" and parts[3].split(" ", 1)[0] == "session-start":
            stamp = parts[2]
    return stamp


def resolve_session(option: str | None, project_dir: Path, now) -> str:
    if option:
        return session_stamp(option, {})
    env = os.environ.get("CLAUDE_SESSION_ID")
    if env:
        return session_stamp(env, {})
    log = log_path(project_dir, now)
    text = log.read_text(encoding="utf-8") if log.exists() else ""
    return last_session_start(text) or session_stamp(None, {})


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


def tagged_blocks(lines: list[str], tag: str) -> list[str]:
    """The text of every fenced block tagged `tag` under a Case, quotes removed."""
    blocks: list[str] = []
    fence_open = recording = False
    buffer: list[str] = []
    for raw in lines:
        line = unquote(raw)
        match = FENCE.match(line)
        if match:
            if not fence_open:
                fence_open, recording, buffer = True, match.group(1).lower() == tag, []
            else:
                fence_open = False
                if recording:
                    blocks.append("\n".join(buffer))
                recording = False
            continue
        if recording:
            buffer.append(line)
    return blocks


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
    path = rule_class_path(record["slug"])
    if path:
        return any(
            isinstance(i, dict) and same_path(i.get("file"), path)
            for i in block.get(record["kind"]) or []
        )
    return find_item(block, record["kind"], record["slug"])[0] is not None


def item_has_line(entry: dict, records: list[dict]) -> bool:
    for record in records:
        if record["kind"] != entry["kind"]:
            continue
        if entry["slug"] and record["slug"] == entry["slug"]:
            return True
        if entry["file"] and same_path(entry["file"], rule_class_path(record["slug"])):
            return True
    return False


def check_lines(cases: dict, blocks: dict, records: list[dict]) -> list[str]:
    """59.1: every line has its item under its own Case; every item has its line, a nested
    estimate through its parent's create line."""
    findings: list[str] = []
    for record in records:
        case, tag = record["case"], f"[{record['kind']}][{record['slug']}]"
        if case not in cases:
            findings.append(f"case {case}: line {tag}: no Case {case} heading in the plan")
        elif not line_has_item(blocks[case], record):
            findings.append(f"case {case}: line {tag} has no item in the plan")
    for case, block in blocks.items():
        of_case = [r for r in records if r["case"] == case]
        for entry in items_of(block):
            if not entry["nested"] and not item_has_line(entry, of_case):
                findings.append(
                    f"case {case}: item [{entry['kind']}][{item_name(entry)}] has no decision line"
                )
    return findings


def check_frontier(path: Path, relative: str, cases: dict, blocks: dict) -> list[str]:
    """59.2: the frontier of the session's folder (73.4), every line closed by a Case the
    plan holds."""
    if not path.exists():
        return [f"frontier: {relative} is missing"]
    findings: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = FRONTIER_LINE.match(line)
        if not match:
            continue
        box, item, rest = match.groups()
        if box == " ":
            findings.append(f"frontier: {item} is open")
            continue
        closer = CLOSERS.match(rest.split(FRONTIER_SEPARATOR)[-1].strip())
        if closer is None:
            findings.append(f"frontier: {item} is closed without case N, work or defer case N")
        elif closer.group(2) is not None:
            case = closer.group(2)
            if case not in cases:
                findings.append(
                    f"frontier: {item} closes with case {case}, no Case {case} heading in the plan"
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
    """The Estimates a `then` block creates or sets `pending`, by slug."""
    slugs: list[str] = []
    for entry in items_of(block):
        if entry["kind"] == "create" and str(entry["slug"] or "").startswith("estimate-"):
            slugs.append(entry["slug"])
    for item in block.get("update") or []:
        if not isinstance(item, dict) or not str(item.get("slug") or "").startswith("estimate-"):
            continue
        set_fields = item.get("set")
        if isinstance(set_fields, dict) and set_fields.get("status") == "pending":
            slugs.append(item["slug"])
    return slugs


def check_tasks(cases: dict, blocks: dict, records: list[dict]) -> list[str]:
    """59.3: a ratified Case has a `tasks` block; an Estimate to read has its task line."""
    findings: list[str] = []
    with_work = {r["case"] for r in records if r.get("kind") != "defer"}
    for case, lines in cases.items():
        tasks = "\n".join(tagged_blocks(lines, "tasks"))
        if case in with_work and not tasks:  # a defer-only Case has no work, case 74
            findings.append(f"case {case}: decision lines and no tasks block")
        for slug in estimates_to_read(blocks[case]):
            if not any(slug in line for line in tasks.splitlines()):
                findings.append(f"case {case}: {slug} has no task line")
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
    """59.6: a `file` item on a path a Rule page governs has no file route."""
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            file = item.get("file") if isinstance(item, dict) else None
            if not file:
                continue
            key = str(file).replace("\\", "/").removeprefix("./")
            if key in governed:
                findings.append(f"case {case}: file {file} is governed by {governed[key]}")
    return findings


def leaf_page(project_dir: Path, slug: str) -> bool | None:
    """Whether the page of `slug` is a Leaf, by the `kind` of its frontmatter; None when no
    page exists under its category."""
    category = category_of(slug)
    if category not in LEAF_CATEGORIES:
        return None
    path = wiki_root(project_dir) / category / f"{slug}.md"
    if not path.exists():
        return None
    return read_page(path, category).props.get("kind") == "Leaf"


def derived_estimate_slug(slug: str) -> str:
    """`estimate-` + the target's slug minus its category prefix (case 72.1)."""
    return "estimate-" + slug.split("-", 1)[1] if "-" in slug else f"estimate-{slug}"


def page_estimates(project_dir: Path, slug: str) -> list[str]:
    """The `estimates` of a live page, by slug; empty when the page or the field is not
    there (case 90.2)."""
    category = category_of(slug)
    if not category:
        return []
    path = wiki_root(project_dir) / category / f"{slug}.md"
    if not path.exists():
        return []
    value = read_page(path, category).props.get("estimates")
    return [str(v) for v in value] if isinstance(value, list) else []


def check_form(blocks: dict, project_dir: Path) -> list[str]:
    """72.5: a Leaf `create` carries `method`, a Leaf `update` `contract`; one contract per
    Case; a derived Estimate slug that names an existing page needs `estimate_slug`. 90.2: a
    contract change whose page carries no Estimate or more than one names the one it moves.
    `file` and `defer` items are outside these checks."""
    findings: list[str] = []
    for case, block in blocks.items():
        contracts = 0
        for item in block.get("create") or []:
            slug = item.get("slug") if isinstance(item, dict) else None
            if not slug or category_of(slug) not in LEAF_CATEGORIES:
                continue
            if item.get("kind") == "Leaf":
                contracts += 1
                if not item.get("method"):
                    findings.append(f"case {case}: create {slug} has no method")
            if item.get("method") and not item.get("estimate_slug"):
                derived = derived_estimate_slug(slug)
                if page_exists(project_dir, "estimates", derived):
                    findings.append(f"case {case}: estimate {derived} exists; name estimate_slug")
        for item in block.get("update") or []:
            slug = item.get("slug") if isinstance(item, dict) else None
            if not slug or category_of(slug) not in LEAF_CATEGORIES:
                continue
            if item.get("contract") == "changed":
                contracts += 1
                if not item.get("estimate_slug"):
                    estimates = page_estimates(project_dir, slug) or []
                    if len(estimates) != 1:  # none to take, or a choice to make (case 90.2)
                        named = ", ".join(estimates) or "none"
                        findings.append(
                            f"case {case}: {slug} has {len(estimates)} estimates ({named}); "
                            "name estimate_slug"
                        )
            if leaf_page(project_dir, slug) and not item.get("contract"):
                findings.append(f"case {case}: update {slug} has no contract")
        if contracts >= 2:
            findings.append(f"case {case}: two contracts in one Case — split it")
    return findings


def check(plan: str, project_dir: Path, stamp: str, now, stdout, stderr) -> int:
    logs = session_event_logs(project_dir, now, stamp)
    hi = hi_moment(logs, stamp)
    folder = session_dir(project_dir, now, stamp)
    if hi is None or folder is None or not hi_recorded("".join(t for _, t in logs), stamp):
        print(f"pretask: no hi recorded for session {stamp}; nothing checked", file=stderr)
        return 0
    cases = split_cases(plan)
    blocks: dict[str, dict] = {}
    findings: list[str] = []
    for case, lines in cases.items():
        blocks[case], errors = then_blocks(lines)
        findings += [f"case {case}: {e}" for e in errors]
    lines = window_lines(project_dir, hi, now.date().isoformat())
    records = session_decisions(lines)
    findings += check_grammar(lines)
    findings += check_lines(cases, blocks, records)
    relative = folder.relative_to(project_dir).as_posix() + "/frontier.md"
    findings += check_frontier(folder / "frontier.md", relative, cases, blocks)
    findings += check_tasks(cases, blocks, records)
    findings += check_governed(blocks, governed_paths(project_dir))
    findings += check_form(blocks, project_dir)
    for finding in findings:
        print(finding, file=stdout)
    return 1 if findings else 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi pretask", description=__doc__.split("\n\n")[1])
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
            print(f"pretask: no plan file at {plan_file}", file=stderr)
            return 2
        plan = plan_file.read_text(encoding="utf-8")
        stamp = resolve_session(args.session, project_dir, now)
        return check(plan, project_dir, stamp, now, stdout, stderr)
    try:
        payload = read_payload(stdin)
        if payload.get("tool_name") != TOOL:
            return 0
        stamp = session_stamp(None, payload)
        log = log_path(project_dir, now)
        event_log = log.read_text(encoding="utf-8") if log.exists() else ""
        hi, done = window(event_log, stamp)
        if hi and not done:
            print(
                f"pretask: Plan Mode is closing without /pre-task in session {stamp}. "
                "Run /pre-task, then exit Plan Mode again.",
                file=stderr,
            )
            return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"pretask: check skipped: {exc}", file=stderr)
    return 0
