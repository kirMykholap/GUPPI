"""`guppi agents <transcript>` — the time and the tokens of each agent of one session.

It reads the transcript of a session under `~/.claude/projects/` and the folder named after
it, whose `subagents/` holds `agent-<id>.jsonl`, the transcript of one agent, beside
`agent-<id>.meta.json`, which names its type, its description and the `toolUseId` of the
Agent call that started it. It prints one line for the main agent and one for each agent file,
so that a choice of how agents run, such as the effort a dispatch passes, rests on a count and
not on an impression (case 1029.3).

A call is one assistant message with `usage`, counted once by its `message.id`, since the
transcript writes a record per block of one message; its tokens are `call_size` of
`.guppi/guppi/context.py`, and the records are read by `read_records` and judged by `is_main`
of `.guppi/guppi/ledger.py`, so no judgment of a record stands here twice. A tool call is one
`tool_use` block, counted once by its id.

The line of the main agent gives its calls, the sum of their tokens, its tool calls and the
seconds from the first record of the transcript to the last. The line of an agent gives its
type and description, `unknown` where it has no meta file; the `effort` its Agent call passed,
read from that call in the main transcript, or `-`; the model of its calls; its calls, the sum
of their tokens and the tokens of its last call; its tool calls; and its runs and seconds, from
the `duration_ms` of each notice of a finished run in the main transcript, each notice counted
once, since the same text stands on more than one record, or `-` where none stands. It writes
no file. A transcript it cannot read gives one line on stderr and exit 1. Rule page:
`vault/wiki/rules/rule-context-size.md`.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.context import call_size
from guppi.ledger import is_main, read_records, record_text

NOTICE = re.compile(
    r"<task-id>([^<]+)</task-id>.*?<tool-use-id>([^<]*)</tool-use-id>.*?"
    r"<duration_ms>(\d+)</duration_ms>",
    re.DOTALL,
)
UNKNOWN = "unknown"
NONE = "-"


def blocks(record: dict) -> list[dict]:
    content = (record.get("message") or {}).get("content")
    return [b for b in content if isinstance(b, dict)] if isinstance(content, list) else []


def calls(records: list[dict]) -> list[int]:
    """The tokens of each call among `records`, in order, each message counted once by its
    id, its last record standing for it."""
    by_id: dict[str, int] = {}
    order: list[str] = []
    for index, record in enumerate(records):
        size = call_size(record)
        if size is None:
            continue
        key = str((record.get("message") or {}).get("id") or f"record-{index}")
        if key not in by_id:
            order.append(key)
        by_id[key] = size
    return [by_id[key] for key in order]


def tool_calls(records: list[dict]) -> int:
    seen = set()
    for record in records:
        if record.get("type") != "assistant":
            continue
        for block in blocks(record):
            if block.get("type") == "tool_use":
                seen.add(block.get("id"))
    return len(seen)


def model_of(records: list[dict]) -> str:
    models = []
    for record in records:
        model = (record.get("message") or {}).get("model")
        if record.get("type") == "assistant" and model and model not in models:
            models.append(model)
    return ",".join(models) or NONE


def seconds(records: list[dict]) -> int | None:
    stamps = []
    for record in records:
        try:
            stamps.append(datetime.fromisoformat(str(record["timestamp"])))
        except (KeyError, ValueError):
            continue
    return round((max(stamps) - min(stamps)).total_seconds()) if stamps else None


def efforts(main: list[dict]) -> dict[str, str]:
    """The `effort` each Agent call of the main transcript passed, by the id of the call."""
    found = {}
    for record in main:
        for block in blocks(record):
            if block.get("type") == "tool_use" and block.get("name") == "Agent":
                effort = (block.get("input") or {}).get("effort")
                if effort:
                    found[str(block.get("id"))] = str(effort)
    return found


def runs(main: list[dict]) -> dict[str, list[int]]:
    """The milliseconds of each finished run of each agent, by its id, from the notices of the
    main transcript, each notice counted once."""
    seen = set()
    found: dict[str, list[int]] = {}
    for record in main:
        if record.get("type") != "user":
            continue
        for task, tool, ms in NOTICE.findall(record_text(record)):
            if (task, tool, ms) in seen:
                continue
            seen.add((task, tool, ms))
            found.setdefault(task, []).append(int(ms))
    return found


def read_meta(path: Path) -> dict:
    try:
        meta = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return meta if isinstance(meta, dict) else {}


def lines_of(transcript: Path) -> list[str] | None:
    records = read_records(transcript)
    if records is None:
        return None
    main = [r for r in records if is_main(r)]
    sizes = calls(main)
    took = seconds(records)
    out = [
        (
            f"main\tcalls {len(sizes)}\ttokens {sum(sizes)}\ttools {tool_calls(main)}\t"
            f"seconds {NONE if took is None else took}"
        )
    ]
    passed, finished = efforts(main), runs(main)
    folder = transcript.with_suffix("") / "subagents"
    for path in sorted(folder.glob("agent-*.jsonl")) if folder.is_dir() else []:
        agent = path.stem[len("agent-") :]
        meta = read_meta(path.with_suffix(".meta.json"))
        own = read_records(path) or []
        sizes = calls(own)
        ms = finished.get(agent)
        out.append(
            "\t".join(
                [
                    f"agent {agent}",
                    str(meta.get("agentType") or UNKNOWN),
                    str(meta.get("description") or UNKNOWN),
                    f"effort {passed.get(str(meta.get('toolUseId')), NONE)}",
                    f"model {model_of(own)}",
                    f"calls {len(sizes)}",
                    f"tokens {sum(sizes)}",
                    f"last {sizes[-1] if sizes else NONE}",
                    f"tools {tool_calls(own)}",
                    f"runs {len(ms) if ms else NONE}",
                    f"seconds {round(sum(ms) / 1000) if ms else NONE}",
                ]
            )
        )
    return out


def run(argv, *, stdout=None, stderr=None) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    parser = argparse.ArgumentParser(prog="guppi agents")
    parser.add_argument("transcript", help="the transcript of a session under ~/.claude/projects/")
    args = parser.parse_args(argv)
    lines = lines_of(Path(args.transcript))
    if lines is None:
        print(f"agents: cannot read {args.transcript}", file=stderr)
        return 1
    for line in lines:
        print(line, file=stdout)
    return 0
