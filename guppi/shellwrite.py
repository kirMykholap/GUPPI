"""`guppi shellwrite` — the `PostToolUse` hook on `Bash` and `PowerShell` that repairs or
names a file a shell call left in a wrong byte form (`rule-shell-write-check`, case 710.1).

On Windows, Windows PowerShell 5.1 reads a UTF-8 file in the ANSI code page and writes it back
with a byte-order mark, and Python's `Path.write_text` writes CRLF line endings; the guard of
`rule-bash-guard` reads only heredocs before a Bash call. After each call of `Bash` or
`PowerShell`, the hook lists the files of the repository that `git ls-files -m -o
--exclude-standard` gives — changed or new, and not ignored — at every call, so a file left
faulty is named again at the next one. A deleted file and a file with a NUL byte and no
UTF-16 mark — a binary file — are skipped. A file that opens with a UTF-16 mark, or that is
not valid UTF-8, is named and not changed, for the agent to restore with Write. In the rest
the hook turns every CRLF into LF and removes a UTF-8 mark at the start — the form
`.gitattributes` sets for every text file — and names each file it repaired; a line on a
removed mark also asks the agent to check the characters of the file, since in the first
lesson the mark came with broken characters. The lines go out as one
`hookSpecificOutput.additionalContext`, the shape in which the stdout of a `PostToolUse` hook
reaches the agent (case 255); a call that leaves no faulty file prints nothing.

A file whose characters a tool changed but which stays valid UTF-8 with no mark is not
caught. Another tool passes. A payload the hook cannot read, or a `git` call that fails,
gives exit 0 and one line on stderr; the hook never raises. A shell call of a subagent is not
checked, since a subagent does not inherit the hooks of `.claude/settings.json`. Rule page:
`vault/wiki/rules/rule-shell-write-check.md`.
"""

import json
import subprocess
import sys
from pathlib import Path

from guppi.event import project_root, read_payload

TOOLS = ("Bash", "PowerShell")
UTF8_MARK = b"\xef\xbb\xbf"
UTF16_MARKS = (b"\xff\xfe", b"\xfe\xff")
ADVICE = "change a file with Edit or Write, never through a shell command"


def changed_files(project_dir: Path) -> list[str]:
    """The paths, relative to the repository, that `git` lists as changed or new and not
    ignored; a `git` call that fails raises."""
    done = subprocess.run(
        ["git", "ls-files", "-m", "-o", "--exclude-standard", "-z"],
        cwd=project_dir,
        capture_output=True,
        check=True,
    )
    return list(dict.fromkeys(p for p in done.stdout.decode("utf-8").split("\0") if p))


def judge(data: bytes) -> tuple[bytes | None, str | None]:
    """The repaired bytes of a file, or None when nothing changes, and the line on it, or
    None when it is sound or not judged: a UTF-16 file and one not valid UTF-8 are named
    unchanged; a binary file — a NUL byte with no UTF-16 mark — is not judged."""
    if data.startswith(UTF16_MARKS):
        return None, "opens with a UTF-16 byte-order mark — restore it in UTF-8 with Write"
    if b"\0" in data:
        return None, None
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return None, "is not valid UTF-8 — restore it with Write"
    repaired = data.removeprefix(UTF8_MARK).replace(b"\r\n", b"\n")
    if repaired == data:
        return None, None
    parts = []
    if data.startswith(UTF8_MARK):
        parts.append("removed its UTF-8 byte-order mark — check its characters")
    if b"\r\n" in data:
        parts.append("turned its CRLF line endings into LF")
    return repaired, "; ".join(parts)


def lines_for(project_dir: Path) -> list[str]:
    """One line per file the hook repaired or names, in the order `git` lists them."""
    found: list[str] = []
    for name in changed_files(project_dir):
        path = project_dir / name
        if not path.is_file():
            continue
        repaired, line = judge(path.read_bytes())
        if line is None:
            continue
        if repaired is not None:
            path.write_bytes(repaired)
            found.append(f"shellwrite: {name}: the hook {line}; {ADVICE}.")
        else:
            found.append(f"shellwrite: {name} {line}; {ADVICE}.")
    return found


def run(argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        payload = read_payload(stdin)
    except Exception:  # noqa: BLE001 — a hook that raises would fail the call
        payload = {}
    if not payload:  # `read_payload` gives {} for no payload and for one that is not JSON
        print("shellwrite: payload not readable, nothing checked", file=stderr)
        return 0
    if payload.get("tool_name") not in TOOLS:
        return 0
    try:
        found = lines_for(project_dir)
    except Exception as exc:  # noqa: BLE001 — a failed git or a file it cannot read
        print(f"shellwrite: files not checked: {exc}", file=stderr)
        return 0
    if found:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "\n".join(found),
            }
        }
        print(json.dumps(output, ensure_ascii=False), file=stdout)
    return 0
