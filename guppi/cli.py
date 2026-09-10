"""`uv run guppi <command> ...` — the one entry point for the harness's scripts.

Each command is a module with a `run(argv, ...) -> int`. Hook commands (`event`, `ledger`, `spec`, `pretask`, `gate`) read their payload from stdin and are registered in `.claude/settings.json`.
"""

import sys

from guppi import (
    cleanup,
    event,
    gate,
    generate,
    index,
    ledger,
    lint,
    materialize,
    pretask,
    render,
    spec,
)

COMMANDS = {
    "cleanup": cleanup.run,
    "event": event.run,
    "gate": gate.run,
    "generate": generate.run,
    "index": index.run,
    "ledger": ledger.run,
    "lint": lint.run,
    "materialize": materialize.run,
    "pretask": pretask.run,
    "render": render.run,
    "spec": spec.run,
}


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    # Claude Code reads a hook's stderr as UTF-8; on Windows the stream would otherwise
    # carry the locale's code page (measured 2026-09-09: cp1252).
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
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
