"""`guppi gate` — the `PreToolUse` hook on the `Skill` tool that refuses `/handoff` on a
dirty tree, and any skill while the Spec is ahead of the ledger.

Reads the hook payload from stdin. Two refusals, each exit 2 with the reason on stderr,
which blocks the call once; the hook writes nothing and commits nothing.

The Spec first (case 122): the text of a reply emitted before a tool call is never kept —
not in the transcript, not in `last_assistant_message` — so a `LEDGER` block followed by a
`Skill` call in the same reply is lost. The Spec is edited by a tool call in that same
reply, so it is always ahead of a lost block: the hook reads the `then` items of every
Case in the session's `spec.md` and in the plan file the session's event log names last
under `.claude/plans/` (a `tool Write:` or `tool Edit:` line of this session's stamp), and
the decision lines of the session's window as `guppi pretask --check` reads them. An item
with no decision line of its Case refuses the call: `gate: /<skill> refused — N item(s) of
the Spec have no ledger line (case A, case B). The text before a tool call is never kept:
end this reply in text with the LEDGER block, then call /<skill> in the next reply.` No
`hi`, no Spec and no plan path: nothing to check.

Then the tree: when the skill is `handoff` and `git status --porcelain` is not empty, the
reason is `commit first`. A clean tree, another skill or another tool: exit 0. The hook
sees only calls made through the `Skill` tool, which is how the Retro skill calls
`/handoff`; the handoff skill checks the tree itself for the case where the person types
it. Rule pages: `vault/wiki/rules/rule-retro-commit.md`, `vault/wiki/rules/rule-ledger-write.md`.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.ledger import hi_moment, session_dir, session_event_logs
from guppi.materialize import split_cases, then_blocks
from guppi.pretask import item_has_line, item_name, items_of, session_decisions, window_lines

TOOL = "Skill"
SKILL = "handoff"
PLAN_TOOLS = ("Write", "Edit", "MultiEdit")


def skill_of(payload: dict) -> str:
    if payload.get("tool_name") != TOOL:
        return ""
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return ""
    for key in ("skill", "name", "skill_name"):
        value = tool_input.get(key)
        if value:
            return str(value).strip().lstrip("/").split(" ", 1)[0]
    return ""


def dirty(project_dir: Path) -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=project_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


def plan_path(logs: list[tuple[str, str]], stamp: str) -> Path | None:
    """The plan file of the session: the path of the last `tool Write:` / `tool Edit:` /
    `tool MultiEdit:` line of this session's stamp that lies under `.claude/plans/` (case
    122). None when no such line exists; a path the log truncated does not exist and is
    skipped by the caller."""
    last = None
    for _, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 4)
            if len(parts) < 5 or parts[0] != "-" or parts[2] != stamp or parts[3] != "tool":
                continue
            tool, sep, path = parts[4].partition(": ")
            if not sep or tool not in PLAN_TOOLS:
                continue
            candidate = Path(path.strip())
            if candidate.parent.name == "plans" and candidate.parent.parent.name == ".claude":
                last = candidate
    return last


def unwritten_items(specs: list[str], records: list[dict]) -> list[str]:
    """`case N: [kind][slug]` for every `then` item of every Case of the Specs given that
    has no decision line of its Case among the records — the second half of
    `pretask.check_lines` — each once, in Spec order."""
    findings: list[str] = []
    for spec in specs:
        cases = split_cases(spec)
        for case, lines in cases.items():
            block, _ = then_blocks(lines)
            of_case = [r for r in records if r["case"] == case]
            for entry in items_of(block):
                if entry["nested"] or item_has_line(entry, of_case):
                    continue
                finding = f"case {case}: [{entry['kind']}][{item_name(entry)}]"
                if finding not in findings:
                    findings.append(finding)
    return findings


def spec_check(project_dir: Path, stamp: str, now) -> list[str]:
    """The unwritten items of the session's `spec.md` and plan file; empty without a `hi`,
    or when neither file exists."""
    logs = session_event_logs(project_dir, now, stamp)
    hi = hi_moment(logs, stamp)
    folder = session_dir(project_dir, now, stamp)
    if hi is None or folder is None:
        return []
    sources = [folder / "spec.md"]
    plan = plan_path(logs, stamp)
    if plan is not None:
        sources.append(plan)
    specs = []
    for path in sources:
        try:
            if path.is_file():
                specs.append(path.read_text(encoding="utf-8"))
        except OSError:
            continue
    if not specs:
        return []
    records = session_decisions(window_lines(project_dir, hi, now.date().isoformat()))
    return unwritten_items(specs, records)


def run(
    argv, *, stdin=None, stderr=None, project_dir: Path | None = None, status=None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        skill = skill_of(payload)
        if not skill:
            return 0
        stamp = session_stamp(None, payload)
        unwritten = spec_check(project_dir, stamp, now)
        if unwritten:
            cases = sorted({f.split(":", 1)[0] for f in unwritten}, key=case_key)
            print(
                f"gate: /{skill} refused — {len(unwritten)} item(s) of the Spec have no ledger "
                f"line ({', '.join(cases)}). The text before a tool call is never kept: end "
                f"this reply in text with the LEDGER block, then call /{skill} in the next reply.",
                file=stderr,
            )
            return 2
        if skill != SKILL:
            return 0
        tree = dirty(project_dir) if status is None else status
        if not tree:
            return 0
        count = len(tree.splitlines())
        print(
            f"gate: /handoff refused — commit first. {count} path(s) uncommitted; the librarian's "
            "commit must be separate from the session's.",
            file=stderr,
        )
        return 2
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"gate: not checked: {exc}", file=stderr)
        return 0


def case_key(text: str) -> tuple:
    """`case 12.3` sorts after `case 9` and before `case 12.10`."""
    number = text.removeprefix("case ").strip()
    return tuple(int(p) if p.isdigit() else 0 for p in number.split("."))
