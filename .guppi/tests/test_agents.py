"""`guppi agents <transcript>`: one line for the main agent and one for each agent of a
session, its effort, model, calls, tokens, runs and seconds, over a transcript, a `subagents/`
folder and a meta file under a temporary folder, with timestamps fixed in the data,
`estimate-context-size-agents-counts-each-agent` (case 1029.3). Rule page:
`vault/wiki/rules/rule-context-size.md`."""

import io
import json

from guppi import agents, cli


def call(message_id, size, model="claude-opus-5-5", tools=(), at="2026-11-05T10:00:00Z"):
    """One record of an assistant message, its `usage` summing to `size`."""
    content = [{"type": "text", "text": "x"}] + [
        {"type": "tool_use", "id": tool, "name": "Read", "input": {}} for tool in tools
    ]
    usage = {"input_tokens": size - 10, "output_tokens": 10}
    message = {"id": message_id, "model": model, "content": content, "usage": usage}
    return {"type": "assistant", "timestamp": at, "message": message}


def dispatch(tool_id, effort=None, at="2026-11-05T10:00:05Z"):
    given = {"description": "Build Case 7", "subagent_type": "case-guppi", "prompt": "p"}
    if effort:
        given["effort"] = effort
    block = {"type": "tool_use", "id": tool_id, "name": "Agent", "input": given}
    message = {"id": f"msg-{tool_id}", "content": [block]}
    return {"type": "assistant", "timestamp": at, "message": message}


def notice(task, tool, ms, at="2026-11-05T10:05:00Z"):
    text = (
        f"<task-notification>\n<task-id>{task}</task-id>\n<tool-use-id>{tool}</tool-use-id>\n"
        f"<status>completed</status>\n<usage><subagent_tokens>9</subagent_tokens>"
        f"<tool_uses>2</tool_uses><duration_ms>{ms}</duration_ms></usage>\n</task-notification>"
    )
    return {
        "type": "user",
        "timestamp": at,
        "origin": {"kind": "task-notification"},
        "message": {"content": text},
    }


def write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")


def session(tmp_path):
    """A main transcript with two calls, one of them in two records, an Agent call at `high`
    and one with no effort, the notices of three finished runs, one of them written twice;
    and the transcripts of two agents, one with no meta file."""
    transcript = tmp_path / "s1.jsonl"
    main = [
        {"type": "user", "timestamp": "2026-11-05T10:00:00Z", "origin": {"kind": "human"}},
        call("m1", 1000, tools=("t1",)),
        call("m1", 1000, tools=("t1",)),  # the same message, a second block
        dispatch("call-a", "high"),
        dispatch("call-b"),
        notice("a1", "call-a", 90_000),
        notice("a1", "call-a", 90_000),  # the same notice on a second record
        notice("a1", "send-1", 30_000),  # the run after a message
        call("m2", 3000, at="2026-11-05T10:10:00Z"),
    ]
    write_jsonl(transcript, main)
    folder = tmp_path / "s1" / "subagents"
    write_jsonl(
        folder / "agent-a1.jsonl",
        [call("x1", 500, tools=("u1", "u2")), call("x2", 700, tools=("u3",))],
    )
    meta = {"agentType": "case-guppi", "description": "Build Case 7", "toolUseId": "call-a"}
    (folder / "agent-a1.meta.json").write_text(json.dumps(meta), encoding="utf-8")
    write_jsonl(folder / "agent-b2.jsonl", [call("y1", 200, model="claude-sonnet-5-5")])
    return transcript


def lines(argv):
    out, err = io.StringIO(), io.StringIO()
    code = agents.run(argv, stdout=out, stderr=err)
    return code, out.getvalue().splitlines(), err.getvalue()


def test_one_line_for_the_main_agent_and_one_for_each_agent(tmp_path):
    code, out, err = lines([str(session(tmp_path))])
    assert (code, err) == (0, "")
    assert out == [
        "main\tcalls 2\ttokens 4000\ttools 3\tseconds 600",
        (
            "agent a1\tcase-guppi\tBuild Case 7\teffort high\tmodel claude-opus-5-5\tcalls 2"
            "\ttokens 1200\tlast 700\ttools 3\truns 2\tseconds 120"
        ),
        (
            "agent b2\tunknown\tunknown\teffort -\tmodel claude-sonnet-5-5\tcalls 1\ttokens 200"
            "\tlast 200\ttools 0\truns -\tseconds -"
        ),
    ]


def test_a_message_in_several_records_is_one_call(tmp_path):
    records = [call("m1", 1000), call("m1", 1000), call("m2", 5)]
    assert agents.calls(records) == [1000, 5]


def test_a_transcript_it_cannot_read_gives_one_line_and_exit_1(tmp_path):
    missing = tmp_path / "none.jsonl"
    code, out, err = lines([str(missing)])
    assert (code, out) == (1, [])
    assert err == f"agents: cannot read {missing}\n"


def test_it_writes_no_file(tmp_path):
    transcript = session(tmp_path)
    before = sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*"))
    lines([str(transcript)])
    assert sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*")) == before


def test_the_command_stands_in_the_map_of_the_commands():
    assert cli.COMMANDS["agents"] is agents.run
