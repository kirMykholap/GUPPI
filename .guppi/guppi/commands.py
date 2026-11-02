"""`guppi test` and `guppi style` — the commands of the tests and of the style check that
`guppi.toml` sets.

Each reads its key of `guppi.toml` at the root of the project — `test` or `style`, a list of
commands — by `commands_of` of `.guppi/guppi/config.py`, the one reader of the file. It splits
each command into its words by `shlex`, POSIX rules, and runs it in the folder of the project
with no shell between, so no word of a command is read by a shell, and with no stdin, so no
command reads the stdin of its caller; each command prints its own lines. The commands run in
order, each one even after a red one, and the run exits 1 when any of them exits non-zero or
does not start, 0 only when every one exits 0. When `guppi.toml` or the key is missing, it
prints one line that names the file and the key, runs nothing and exits 1. With `--exit-zero`,
in each case, a missing file or key included, it prints one last line `exit code: <n>`, the
exit code of the run without the flag, and exits 0, so a skill that runs it as a `!` command
loads whatever the run finds, since Claude Code refuses a skill whose `!` command exits
non-zero; `add_exit_zero` and `exit_zero` are the one place of that flag, which `guppi check`
imports (case 1003). In the repository
of GUPPI the key `test` runs pytest over `.guppi/tests/` and the key `style` runs ruff; Work
Mode, Retro and the CI of a project run these two commands, so a project needs no tool but
`uv` (case 820). Rule page: `vault/wiki/rules/rule-guppi-config.md`.
"""

import argparse
import shlex
import subprocess
import sys
from pathlib import Path

from guppi.config import ConfigError, commands_of
from guppi.event import project_root

EXIT_ZERO = "exit code: {}"


def add_exit_zero(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """`--exit-zero` on the parser of a command whose exit code a skill reads."""
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="print the exit code of the run on a last line, and exit 0",
    )
    return parser


def exit_zero(status: int, flag: bool, stdout) -> int:
    """With the flag, the last line `exit code: <status>` and 0; without it, `status`."""
    if not flag:
        return status
    print(EXIT_ZERO.format(status), file=stdout, flush=True)
    return 0


def run(key: str, argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    """Runs the commands of `key` of `guppi.toml`; the exit code of the run."""
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    args = add_exit_zero(argparse.ArgumentParser(prog=f"guppi {key}")).parse_args(argv)
    try:
        commands = commands_of(project_dir, key)
    except ConfigError as exc:
        print(f"{key}: {exc}", file=stderr)
        return exit_zero(1, args.exit_zero, stdout)
    status = 0
    for command in commands:
        stdout.flush()
        try:
            done = subprocess.run(
                shlex.split(command), cwd=project_dir, stdin=subprocess.DEVNULL, check=False
            )
        except OSError as exc:  # a program that is not found, or does not start
            print(f"{key}: {command}: {exc}", file=stderr)
            status = 1
            continue
        if done.returncode != 0:
            status = 1
    return exit_zero(status, args.exit_zero, stdout)


def run_test(argv, **kwargs) -> int:
    """`guppi test`: the commands of the key `test`."""
    return run("test", argv, **kwargs)


def run_style(argv, **kwargs) -> int:
    """`guppi style`: the commands of the key `style`."""
    return run("style", argv, **kwargs)
