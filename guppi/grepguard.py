"""`guppi grepguard` — the `PreToolUse` hook on `Grep` that leaves the Decision pages out of
every search over the wiki (`rule-search-leaves-out-decisions`, case 664.1).

For a `Grep` whose searched folder — its `path`, or the working directory of the payload
(`cwd`, else the project root) when the call has none — holds `vault/wiki/decisions/` and
does not lie in it, judged by `pageread.inside`, the hook prints
`hookSpecificOutput.updatedInput`: the input with `!**/decisions/**` at the end of its `glob`,
after a space when the `glob` holds another filter, and with no permission decision, so the
search runs as changed and prints no line and no path of a Decision page. The exclusion
stands last since the Grep tool reads its glob in order: with it first, `!**/decisions/** *.md`
still matched every Decision page (case 664). A `glob` that already ends with the exclusion
is not changed; one that holds it elsewhere gets it again at the end. A call of the librarian
is changed as any other agent's: the hook does not read the agent.

A `Grep` whose `path` is `vault/wiki/decisions/` or lies in it — a search an agent makes only
for a reason of its frame — a `path` that is one file, a folder that does not hold the
Decision pages, any other tool, and a payload the hook cannot read pass unchanged: exit 0,
nothing printed. The hook never refuses a call; the payload is read as UTF-8, and an error
lets the call pass with one line on stderr. Rule page:
`vault/wiki/rules/rule-search-leaves-out-decisions.md`.
"""

import json
import sys
from pathlib import Path

from guppi.event import project_root, read_payload
from guppi.pageread import inside
from guppi.pages import wiki_root

TOOL = "Grep"
EXCLUSION = "!**/decisions/**"


def searched_folder(payload: dict, tool_input: dict, project_dir: Path) -> Path:
    """The folder the call searches: its `path`, read from the working directory when it is
    relative, or that directory itself when the call names none."""
    base = Path(str(payload.get("cwd") or project_dir))
    path = tool_input.get("path")
    if not path:
        return base
    found = Path(str(path))
    return found if found.is_absolute() else base / found


def guarded_glob(glob: str) -> str | None:
    """The glob with the exclusion at its end, after a space when it holds another filter;
    None when it already ends with it."""
    glob = glob.strip()
    if glob.split()[-1:] == [EXCLUSION]:
        return None
    return f"{glob} {EXCLUSION}" if glob else EXCLUSION


def before(payload: dict, project_dir: Path, stdout) -> int:
    if payload.get("tool_name") != TOOL:
        return 0
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return 0
    folder = searched_folder(payload, tool_input, project_dir)
    decisions = wiki_root(project_dir) / "decisions"
    if folder.is_file() or not inside(decisions, folder) or inside(folder, decisions):
        return 0
    glob = guarded_glob(str(tool_input.get("glob") or ""))
    if glob is None:
        return 0
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "updatedInput": {**tool_input, "glob": glob},
        }
    }
    print(json.dumps(output, ensure_ascii=False), file=stdout)
    return 0


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        payload = read_payload(stdin)
        if not payload:
            return 0
        return before(payload, project_dir, stdout)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the call
        print(f"grepguard: passed unchanged: {exc}", file=stderr)
        return 0
