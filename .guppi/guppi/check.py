"""`guppi check` — the vault checks, every step in a row, red if any is.

Runs `STEPS` in order: `guppi render --check`, `guppi sprint --check`, `guppi backlog
--check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`. Each step runs as
a process of its own, by the Python that runs this command, in the folder of the project and
with no stdin, so no step reads the stdin of its caller; it prints its own lines as it does
when it runs alone. Every step runs even after a red one, so a red step hides no finding of
a later step, and the run exits 1 when any step exits non-zero, 0 only when every step exits
0 (case 587). Where the module `guppi.ship` is missing, by `ship_stands` of
`.guppi/guppi/pages.py` — a project that installed GUPPI holds no command `ship` — it runs
the other five and prints one line that it skips `guppi ship --check`, which sets no exit
code (case 820.5). Every step only reports, so nothing here writes to the tree (cases 147.7,
227). It needs no tool but `uv`, which runs it, so a project runs it on any machine; the
target `lint` of the `Makefile` this repository keeps for now runs it (case 820).
Rule page: `vault/wiki/rules/rule-lint.md`.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from guppi.event import project_root
from guppi.pages import ship_stands

# how a step runs: the entry point of `guppi`, by the Python that runs this command; `-P`
# keeps the folder of the project off the search path, so no file there stands for a module
GUPPI = (sys.executable, "-P", "-m", "guppi.cli")
STEPS = (
    ("render", "--check"),
    ("sprint", "--check"),
    ("backlog", "--check"),
    ("glossary", "--check"),
    ("lint",),
    ("ship", "--check"),
)
SHIP = ("ship", "--check")
SKIPPED = "check: guppi ship --check skipped: no command ship in this project"


def parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(prog="guppi check", description="run the vault checks")


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    project_dir = project_root() if project_dir is None else Path(project_dir)
    parser().parse_args(argv)
    env = dict(os.environ, CLAUDE_PROJECT_DIR=str(project_dir))
    status = 0
    for step in STEPS:
        if step == SHIP and not ship_stands():
            print(SKIPPED, file=stdout)
            continue
        stdout.flush()  # a line of this command stands before the lines of the next step
        done = subprocess.run(
            [*GUPPI, *step], cwd=project_dir, env=env, stdin=subprocess.DEVNULL, check=False
        )
        if done.returncode != 0:
            status = 1
    return status
