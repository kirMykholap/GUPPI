"""`guppi gitstate` — the branch and the status of git, or one line outside a repository.

`/hi` splices the output after its label `Branch:` (`rule-git-context`). In a git repository
it prints the output of `git branch --show-current`, then the line `Status:` and the lines of
`git status --short`. In a folder that is no git repository — a failed or missing git
included — it prints the one line `none: this folder is no git repository`. It exits 0 in each case, since Claude Code
stops the whole skill on a `!` command that fails (case 851.3). It writes nothing. This module
holds the one judgment of whether a folder is a git repository: `git` of `.guppi/guppi/box.py`
and `dirty` of `.guppi/guppi/gate.py` give an empty text when git fails and do not tell the
two apart. Rule page: `vault/wiki/rules/rule-git-context.md`.
"""

import argparse
import subprocess
import sys
from pathlib import Path

from guppi.event import project_root

NO_REPOSITORY = "none: this folder is no git repository"


def git(folder: Path, *args: str) -> str | None:
    """The stdout of `git <args>` in `folder`, or None when git fails or is missing."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=folder,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError:
        return None
    return result.stdout if result.returncode == 0 else None


def is_repository(folder: Path) -> bool:
    return (git(folder, "rev-parse", "--is-inside-work-tree") or "").strip() == "true"


def state(folder: Path) -> str:
    """The text `guppi gitstate` prints for `folder`."""
    if not is_repository(folder):
        return NO_REPOSITORY
    branch = (git(folder, "branch", "--show-current") or "").strip()
    status = (git(folder, "status", "--short") or "").rstrip("\n")
    return f"{branch}\nStatus:\n{status}" if status else f"{branch}\nStatus:"


def parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(prog="guppi gitstate", description=__doc__.split("\n\n")[1])


def run(argv, *, stdout=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    print(state(project_dir), file=stdout)
    return 0
