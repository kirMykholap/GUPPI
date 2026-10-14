"""`guppi context` — the size of the context window, counted from the transcript.

On `Stop`, `uv run guppi context` reads the transcript at `transcript_path` and skips the
records of a subagent (`isSidechain`). N is the sum of the input, cache read, cache creation
and output tokens of the last main-agent call the transcript holds — at `Stop` the last call
may not be there yet, so N may lag one call — and D is N less the same sum at the last call
before the start of the turn: the last `user` record that `opens_turn` of `guppi/ledger.py`
names the person's message or a returned answer, the one judgment the turn of
`guppi/casecheck.py` and the stretch of the ledger hook share. A record with no
`origin.kind`, a record marked `isMeta` and a tool result do not move it. It prints JSON with a `systemMessage`: `context: <N> tokens (<+D> since the last
reply)`; at N of 400 000 or more the line ends with `— past 400 000: costly, better take no
more work`.
On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call
carrying `usage`, it prints nothing.

With `--prompt`, on `UserPromptSubmit`: at N of 400 000 or more it prints to the agent's
context the size and a note for the agent to pass to the person, not an order: the session
is already costly, taking on more work is not recommended, and while the Frontier holds open
items, deferring them is the better course; nothing orders the session closed and nothing
names /retro or /handoff. Below the limit it prints nothing. An error of
its own on `Stop` prints a `systemMessage` `context: not counted: <error>` in place of the size
line, so the person sees it; with `--prompt` the error goes to stderr, since a block there would
block the person's message. It exits 0 always. Rule page:
`vault/wiki/rules/rule-context-size.md`.
"""

import argparse
import json
import sys

from guppi.event import read_payload
from guppi.ledger import opens_turn, transcript_records

LIMIT = 400_000
USAGE_KEYS = (
    "input_tokens",
    "cache_read_input_tokens",
    "cache_creation_input_tokens",
    "output_tokens",
)


def call_size(record: dict) -> int | None:
    """The tokens of one assistant call, or None when the record is no call with `usage`."""
    if record.get("type") != "assistant":
        return None
    usage = (record.get("message") or {}).get("usage")
    if not isinstance(usage, dict):
        return None
    return sum(int(usage.get(key) or 0) for key in USAGE_KEYS)


def sizes(records: list[dict]) -> tuple[int, int] | None:
    """`(N, D)`, or None when no call carries `usage`. D counts from the last call before
    the start of the turn — the last record that `opens_turn` of `guppi/ledger.py` names the
    person's message or a returned answer; D is N itself when no call stands
    before it."""
    last = None
    at_prompt = 0
    for record in records:
        if opens_turn(record):
            at_prompt = last or 0
            continue
        size = call_size(record)
        if size is not None:
            last = size
    if last is None:
        return None
    return last, last - at_prompt


def number(value: int) -> str:
    return f"{value:,}".replace(",", " ")


def stop_line(n: int, d: int) -> str:
    sign = "+" if d >= 0 else "-"
    line = f"context: {number(n)} tokens ({sign}{number(abs(d))} since the last reply)"
    if n >= LIMIT:
        line += f" — past {number(LIMIT)}: costly, better take no more work"
    return line


def prompt_text(n: int) -> str | None:
    if n < LIMIT:
        return None
    return (
        f"context: {number(n)} tokens, past {number(LIMIT)} — the session is already costly. "
        "A note for the agent to pass to the person, not an order: taking on more work is not "
        "recommended; while the Frontier holds open items, deferring them is the better course "
        "(rule-context-size)."
    )


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi context", description=__doc__.split("\n\n")[0])
    p.add_argument("--prompt", action="store_true", help="the UserPromptSubmit hook")
    return p


def run(argv, *, stdin=None, stdout=None, stderr=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    args = None
    try:
        args = parser().parse_args(argv)
        payload = read_payload(stdin)
        if not payload:
            return 0
        if not args.prompt and payload.get("stop_hook_active"):
            return 0
        found = sizes(transcript_records(payload))
        if found is None:
            return 0
        n, d = found
        if args.prompt:
            text = prompt_text(n)
            if text:
                print(text, file=stdout)  # stdout of UserPromptSubmit reaches the context
            return 0
        print(json.dumps({"systemMessage": stop_line(n, d)}, ensure_ascii=False), file=stdout)
    except SystemExit:  # argparse: a bad invocation must not fail the session
        return 0
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        line = f"context: not counted: {exc}"
        if args is None or args.prompt:  # a block of the prompt would block the person's message
            print(line, file=stderr)
        else:  # shown to the person in place of the size line
            print(json.dumps({"systemMessage": line}, ensure_ascii=False), file=stdout)
    return 0
