"""`guppi context`: the size of the context window after each reply, on `Stop` (case 392.1),
and the note past 400 000 tokens, on `UserPromptSubmit` (case 392.2) — a note for the
person, not an order to close the session (case 430).

Every test feeds the payload through a stream, the shape a hook is really handed, and a
transcript written by the test in the shape Claude Code writes it.
"""

import io
import json

from guppi import context


def call(size, *, sidechain=False, output=0):
    return {
        "type": "assistant",
        "isSidechain": sidechain,
        "message": {
            "role": "assistant",
            "content": [{"type": "text", "text": "x"}],
            "usage": {
                "input_tokens": 3,
                "cache_read_input_tokens": size - 3 - output,
                "cache_creation_input_tokens": 0,
                "output_tokens": output,
            },
        },
    }


def prompt(text="C1"):
    return {"type": "user", "message": {"role": "user", "content": text}}


def tool_result():
    content = [{"type": "tool_result", "tool_use_id": "t", "content": "ok"}]
    return {"type": "user", "message": {"role": "user", "content": content}}


def injected():
    return {"type": "user", "isMeta": True, "message": {"role": "user", "content": "hook"}}


def hook(tmp_path, records, *args, **fields):
    transcript = tmp_path / "transcript.jsonl"
    lines = [json.dumps(r) if isinstance(r, dict) else r for r in records]
    transcript.write_text("\n".join(lines) + "\n", encoding="utf-8")
    stdin = io.StringIO(json.dumps({"transcript_path": str(transcript), **fields}))
    out, err = io.StringIO(), io.StringIO()
    code = context.run(list(args), stdin=stdin, stdout=out, stderr=err)
    return code, out.getvalue(), err.getvalue()


def message(out):
    return json.loads(out)["systemMessage"]


# --- the line after each reply (case 392.1) -----------------------------------------------


def test_stop_the_line_names_n_and_its_change_since_the_last_reply(tmp_path):
    records = [
        prompt(),
        call(90_000),
        prompt("C2"),
        call(95_000),
        tool_result(),
        call(101_500, output=500),
    ]
    code, out, err = hook(tmp_path, records)
    assert (code, err) == (0, "")
    assert message(out) == "context: 101 500 tokens (+11 500 since the last reply)"


def test_stop_a_first_reply_counts_from_zero(tmp_path):
    _, out, _ = hook(tmp_path, [prompt(), call(67_844)])
    assert message(out) == "context: 67 844 tokens (+67 844 since the last reply)"


def test_stop_a_subagent_call_and_an_injected_text_are_not_counted(tmp_path):
    records = [
        prompt(),
        call(50_000),
        prompt("C2"),
        call(52_000),
        call(900_000, sidechain=True),
        injected(),
    ]
    _, out, _ = hook(tmp_path, records)
    assert message(out) == "context: 52 000 tokens (+2 000 since the last reply)"


def test_stop_silent_on_the_re_fire_with_no_usage_or_no_transcript(tmp_path):
    records = [prompt(), call(50_000)]
    assert hook(tmp_path, records, stop_hook_active=True) == (0, "", "")
    assert hook(tmp_path, [prompt(), "not json"]) == (0, "", "")
    stdin = io.StringIO(json.dumps({"transcript_path": str(tmp_path / "absent.jsonl")}))
    out = io.StringIO()
    assert context.run([], stdin=stdin, stdout=out, stderr=io.StringIO()) == 0
    assert out.getvalue() == ""


# --- the warning past 400 000 (case 392.2) --------------------------------------------------


def test_limit_below_it_the_prompt_hook_is_silent_and_the_line_plain(tmp_path):
    records = [prompt(), call(399_999)]
    assert hook(tmp_path, records, "--prompt") == (0, "", "")
    _, out, _ = hook(tmp_path, records)
    assert "past" not in message(out)


def test_limit_at_it_both_hooks_give_a_note_not_an_order(tmp_path):  # case 430
    records = [prompt(), call(390_000), prompt("C2"), call(400_000)]
    code, out, _ = hook(tmp_path, records, "--prompt")
    assert code == 0
    assert out.startswith("context: 400 000 tokens, past 400 000 — the session is already costly.")
    assert "not an order" in out and "taking on more work is not recommended" in out
    assert "deferring them is the better course" in out
    assert "/retro" not in out and "/handoff" not in out and "close the session" not in out
    _, out, _ = hook(tmp_path, records)
    assert message(out) == (
        "context: 400 000 tokens (+10 000 since the last reply)"
        " — past 400 000: costly, better take no more work"
    )


def test_limit_the_prompt_hook_speaks_on_a_re_fire_flag_too(tmp_path):
    # `stop_hook_active` belongs to `Stop`; the prompt hook does not read it
    code, out, _ = hook(tmp_path, [prompt(), call(450_000)], "--prompt", stop_hook_active=True)
    assert code == 0 and out.startswith("context: 450 000 tokens")
