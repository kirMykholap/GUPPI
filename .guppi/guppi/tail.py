"""`guppi tail` — every ledger line that no vault page holds yet.

Walks every `ledger.md` under `vault/raw/` — the date-level ledger of a date first (the
shape before case 103), then the session ledgers `raw/<date>/<HHMM>/ledger.md` in folder
order, dates ascending — and prints every line that `materialize.parse_line` reads as a
record and whose number is neither in the `line` or `folded` of an entry nor under
`unparsed` of the `materialize.yaml` beside it, as `<date> L<n>: <the line>` or
`<date>/<HHMM> L<n>: <the line>`. A ledger without a yaml prints every record line it has;
a ledger fully covered prints nothing; with an empty tail the output is empty. Exit 0
always; a ledger that cannot be read is a line on stderr and the walk goes on. The
coverage of a line is the one function `guppi archive` uses (case 101.2). `/hi` splices
the output into its context as `Tail:`. Rule page: `vault/wiki/rules/rule-ledger-tail.md`.
"""

import argparse
import sys
from pathlib import Path

from guppi.archive import uncovered_lines
from guppi.event import project_root
from guppi.materialize import units_with


def parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(prog="guppi tail", description=__doc__.split("\n\n")[1])


def run(argv, *, stdout=None, stderr=None, project_dir: Path | None = None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    try:
        parser().parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (None, 0) else 0
    for unit in units_with(project_dir, "ledger.md"):
        try:
            for number, text in uncovered_lines(project_dir, unit):
                print(f"{unit} L{number}: {text}", file=stdout)
        except Exception as exc:  # noqa: BLE001 — one ledger fails alone
            print(f"tail: raw/{unit}: {exc}", file=stderr)
    return 0
