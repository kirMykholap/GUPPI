"""`uv run guppi <command> ...` — the one entry point for the harness's scripts.

Each command is a module with a `run(argv, ...) -> int`. Hook commands (`event`, `probe`,
later `ledger`) read their payload from stdin and are registered in `.claude/settings.json`.
"""

import sys

from guppi import event, probe

COMMANDS = {
    "event": event.run,
    "probe": probe.run,
}


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if not argv or argv[0] in ("-h", "--help"):
        names = ", ".join(sorted(COMMANDS))
        print(f"usage: guppi <command> [args]\ncommands: {names}", file=sys.stderr)
        return 0 if argv else 2
    name, rest = argv[0], argv[1:]
    command = COMMANDS.get(name)
    if command is None:
        print(f"guppi: unknown command {name!r}", file=sys.stderr)
        return 2
    return command(rest)


if __name__ == "__main__":
    sys.exit(main())
