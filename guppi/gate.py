"""`guppi gate` — the hook that refuses `/handoff` on a dirty tree, and any skill while the
Spec is ahead of the ledger: on `PreToolUse` for the agent's call through the `Skill`
tool, on `UserPromptSubmit` for the person's typed `/pre-spec`, `/retro` or `/handoff`.

Reads the hook payload from stdin. Two refusals, each exit 2 with the reason on stderr,
which blocks the call once; the hook writes nothing and commits nothing.

Two entries, one gate (case 169.1). A typed slash command is expanded by the client into
the prompt and is never a `Skill` call, so no `PreToolUse` hook sees it; the
`UserPromptSubmit` payload carries it as `prompt`. When the prompt, trimmed, is one of the
three commands — arguments allowed — the same checks run and the same mark is left; a
refusal is exit 2 with a reason written for the person, whom the client shows it while
blocking the prompt: the agent must end its reply with the LEDGER block, or commit. Any
other prompt, `/hi` included, is exit 0 with no output and no mark; a `PreToolUse`
payload goes as before.

The Spec first (case 122): the text of a reply emitted before a tool call is kept in the
transcript and read at the next `Stop` of the session (case 224.1) — but a `Skill` call
in the same reply as a `LEDGER` block runs before that `Stop`, so the block is not yet in
the ledger when the skill needs it, and the last reply of a session has no `Stop` at all.
The Spec is edited by a tool call in that same reply, so it is always ahead of the
unwritten block: the hook reads the `then` items of every
Case in the session's `spec.md` and in the plan file the session's event log names last
under `.claude/plans/` (a `tool Write:` or `tool Edit:` line of this session's stamp), and
the decision lines of the session's window as `guppi prespec --check` reads them. An item
with no decision line of its Case refuses the call: `gate: /<skill> refused — N item(s) of
the Spec have no ledger line (case A, case B). The text before a tool call waits for the
next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next
reply.` No
`hi`, no Spec and no plan path: nothing to check.

Before the Spec, for `/retro` only (case 180): a session with a `hi` but no `spec.md` in
its folder, no plan file named by the event log and no record line — decision, estimate
or lesson — in its ledger window has nothing to review, and the call is refused: `gate:
/retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/.
Ratify a Case or write a reading or a lesson first`, then the advice of the path — `, then
type /retro again.` for the person; `. This refusal is a stop of
vault/wiki/where-to-stop.md: end your reply with the question to the person.` for the
agent, which asks for no call in a next reply (case 531.15). No mark. `/pre-spec` and `/handoff` in the same session go as before; without a `hi`
nothing is checked.

Then the tree: when the skill is `handoff` and `git status --porcelain` is not empty, the
reason is `commit first`. A clean tree, another skill or another tool: exit 0. The handoff
skill still checks the tree itself, a second net. Rule pages:
`vault/wiki/rules/rule-retro-commit.md`, `vault/wiki/rules/rule-ledger-write.md`.

Last the mark (case 136.1): a call of `pre-spec`, `retro` or `handoff` that passes both
checks leaves one line `- HH:MM:SS <stamp> prespec|retro|handoff` in the day's event log,
the stamp from the payload's `session_id` — the line the skills wrote through a `!`
substitution until 136.1, where `CLAUDE_SESSION_ID` is empty and every mark read
`--------`. A refused call and any other skill leave no mark. Rule page:
`vault/wiki/rules/rule-event-log.md`.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import append, format_line, log_path, project_root, read_payload, session_stamp
from guppi.ledger import hi_moment, plan_path, session_dir, session_event_logs
from guppi.materialize import split_cases, then_blocks
from guppi.prespec import item_has_line, item_name, items_of, session_decisions, window_lines

TOOL = "Skill"
SKILL = "handoff"
MARKS = {"pre-spec": "prespec", "retro": "retro", "handoff": "handoff"}


def skill_of(payload: dict) -> str:
    """The skill a payload names: `tool_input.skill` of a `Skill` call, or the typed command
    of a `UserPromptSubmit` payload when it is one of `MARKS` (case 169.1); else ""."""
    if "prompt" in payload and "tool_name" not in payload:
        head = str(payload.get("prompt") or "").strip().split(" ", 1)[0]
        name = head[1:] if head.startswith("/") else ""
        return name if name in MARKS else ""
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


def typed(payload: dict) -> bool:
    """True for a `UserPromptSubmit` payload — the person's path (case 169.1)."""
    return "prompt" in payload and "tool_name" not in payload


def dirty(project_dir: Path) -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=project_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


def unwritten_items(specs: list[str], records: list[dict]) -> list[str]:
    """`case N: [kind][slug]` for every `then` item of every Case of the Specs given that
    has no decision line of its Case among the records — the second half of
    `prespec.check_lines` — each once, in Spec order."""
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


def nothing_to_review(project_dir: Path, stamp: str, now) -> str | None:
    """The session's folder, as `raw/<date>/<HHMM>/`, when a `/retro` has nothing to review
    (case 180): a `hi`, but no `spec.md` in the folder, no plan file named by the event
    log, and no record line — decision, estimate or lesson — in the session's ledger
    window. None without a `hi`, or when any of the three exists."""
    logs = session_event_logs(project_dir, now, stamp)
    hi = hi_moment(logs, stamp)
    folder = session_dir(project_dir, now, stamp)
    if hi is None or folder is None:
        return None
    if (folder / "spec.md").is_file():
        return None
    plan = plan_path(logs, stamp)
    if plan is not None and plan.is_file():
        return None
    if window_lines(project_dir, hi, now.date().isoformat()):
        return None
    return f"raw/{folder.parent.name}/{folder.name}/"


def mark(project_dir: Path, payload: dict, skill: str, now) -> None:
    """The stamped mark of a skill call the gate let through (case 136.1); nothing for a
    skill outside `MARKS`."""
    name = MARKS.get(skill)
    if name:
        append(log_path(project_dir, now), format_line(name, payload, [], None, now))


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
        if skill == "retro":
            empty = nothing_to_review(project_dir, stamp, now)
            if empty:
                if typed(payload):
                    advice = ", then type /retro again."
                else:  # case 531.15: a stop, not a call in the next reply
                    advice = (
                        ". This refusal is a stop of vault/wiki/where-to-stop.md: end your "
                        "reply with the question to the person."
                    )
                print(
                    f"gate: /retro refused — nothing to review: no Spec and no ledger line in "
                    f"{empty}. Ratify a Case or write a reading or a lesson first{advice}",
                    file=stderr,
                )
                return 2
        unwritten = spec_check(project_dir, stamp, now)
        if unwritten:
            cases = sorted({f.split(":", 1)[0] for f in unwritten}, key=case_key)
            if typed(payload):  # 169.1: the reason is for the person
                advice = f"Ask the agent to end its reply with the LEDGER block, then type /{skill} again."
            else:
                advice = (
                    "The text before a tool call waits for the next Stop: end this reply in text with "
                    f"the LEDGER block, then call /{skill} in the next reply."
                )
            print(
                f"gate: /{skill} refused — {len(unwritten)} item(s) of the Spec have no ledger "
                f"line ({', '.join(cases)}). {advice}",
                file=stderr,
            )
            return 2
        if skill == SKILL:
            tree = dirty(project_dir) if status is None else status
            if tree:
                count = len(tree.splitlines())
                print(
                    f"gate: /handoff refused — commit first. {count} path(s) uncommitted; the "
                    "librarian's commit must be separate from the session's.",
                    file=stderr,
                )
                return 2
        mark(project_dir, payload, skill, now)
        return 0
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"gate: not checked: {exc}", file=stderr)
        return 0


def case_key(text: str) -> tuple:
    """`case 12.3` sorts after `case 9` and before `case 12.10`."""
    number = text.removeprefix("case ").strip()
    return tuple(int(p) if p.isdigit() else 0 for p in number.split("."))
