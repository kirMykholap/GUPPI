"""`guppi casecheck`: `--subagent`, the `SubagentStop` hook that checks the Case of
`case-guppi` before the main agent sees it (case 419.3), and the `Stop` hook that compares a
shown Case with the checked one (case 419.4). Rule page: `vault/wiki/rules/rule-case-check.md`.

Every test feeds the payload through a stream, the shape a hook is really handed.
"""

import io
import json
from datetime import UTC, date, datetime

import pytest

from guppi import casecheck

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 15, 30, 0, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"

ANSWER = """## Case 7 — пример

> **context:**
> Контекст.

> **problem:**
> Проблема.

> **recommend:**
> Совет.

> **given:**
> `rule-x` — the rule.
> **＋** `estimate-x-works` — its Estimate.

> **when:**
> The agent runs `guppi x`.

> **then:**
> The file is written.

> **tasks:**
> - [ ] update `rule-x` — one `replace` pair
>   - old: `` the `old` text ``
>   - new: `the new text`
>   - change: `the text changed (case 7)`
> - [ ] create `estimate-x-works`
>   - type: `estimate`
>   - kind: `QA`
>   - purpose: `X works`
>   - method: `uv run pytest tests/test_x.py`
>   - tags: `[harness]`
> - [ ] read `estimate-x-works`

> **ratification:**
> ```
> - decision[case 7][update][rule-x]{ref:rule-x}
> - decision[case 7][create][estimate-x-works]{ref:rule-x}{tags:harness}
> ```
"""

RULE_X = """---
type: rule
kind: Leaf
purpose: Prevents x
status: draft
---

## Purpose

Prevents x: the `old` text stands here.
"""

SHORT_FORM = """## Case 8 — отложено

> **context:**
> Контекст.

> **problem:**
> Проблема.

```then
defer:
  - slug: rule-y
    type: rule
    purpose: Later
```
"""


@pytest.fixture
def working(tmp_path):
    """A working session: `hi` at 15:01, a plan file the agent wrote under `.claude/plans/`."""
    plan = tmp_path / ".claude" / "plans" / "plan.md"
    plan.parent.mkdir(parents=True)
    plan.write_text("# Spec — 2026-09-09, session 1501\n", encoding="utf-8")
    log = tmp_path / "vault" / "raw" / TODAY.isoformat() / "event_log.md"
    log.parent.mkdir(parents=True)
    log.write_text(
        "- 15:01:00 44c1aae1 session-start startup\n"
        "- 15:01:30 44c1aae1 hi\n"
        f"- 15:02:00 44c1aae1 tool Write: {plan}\n",
        encoding="utf-8",
    )
    rule = tmp_path / "vault" / "wiki" / "rules" / "rule-x.md"
    rule.parent.mkdir(parents=True)
    rule.write_text(RULE_X, encoding="utf-8")
    return tmp_path


def store(project):
    path = casecheck.store_of(project / ".claude" / "plans" / "plan.md")
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def answer(project, text, agent="case-guppi", **fields):
    payload = {
        "session_id": SESSION,
        "agent_type": agent,
        "last_assistant_message": text,
        "hook_event_name": "SubagentStop",
        **fields,
    }
    err = io.StringIO()
    stdin = io.StringIO(json.dumps(payload, ensure_ascii=False))
    code = casecheck.run(["--subagent"], stdin=stdin, stderr=err, project_dir=project, now=NOW)
    return code, err.getvalue()


def show(project, reply, **fields):
    payload = {"session_id": SESSION, "last_assistant_message": reply, **fields}
    err = io.StringIO()
    stdin = io.StringIO(json.dumps(payload, ensure_ascii=False))
    code = casecheck.run([], stdin=stdin, stderr=err, project_dir=project, now=NOW)
    return code, err.getvalue()


# --- the check on SubagentStop (case 419.3) ---------------------------------------------


def test_subagent_a_clean_case_is_stored(working):
    assert answer(working, ANSWER) == (0, "")
    entry = store(working)["7"]
    assert entry["findings"] == []
    assert entry["text"].startswith("## Case 7 — пример\n\n> **context:**")
    assert entry["text"].endswith("> ```")


def test_subagent_a_missing_section_sends_it_back(working):
    faulty = ANSWER.replace(
        "> **given:**\n> `rule-x` — the rule.\n> **＋** `estimate-x-works` — its Estimate.\n\n", ""
    )
    code, err = answer(working, faulty)
    assert code == 2 and "case 7: missing section given" in err
    assert store(working)["7"]["findings"]


def test_subagent_sections_out_of_order_and_a_ratification_with_text(working):
    moved = ANSWER.replace("> **recommend:**\n> Совет.\n\n", "") + "\n> **recommend:**\n> Совет.\n"
    code, err = answer(working, moved)
    assert code == 2 and "out of the order of the schema" in err
    chatty = ANSWER.replace("> ```\n> - decision", "> Ratify?\n> ```\n> - decision", 1)
    code, err = answer(working, chatty)
    assert code == 2 and "ratification holds one untagged fence" in err


def test_subagent_a_finding_of_the_prespec_checks_sends_it_back(working):
    no_read = ANSWER.replace("> - [ ] read `estimate-x-works`\n", "")
    code, err = answer(working, no_read)
    assert code == 2 and "case 7: estimate-x-works has no task line" in err


def test_subagent_two_update_lines_of_one_slug_send_it_back(working):  # case 426
    second = "> - [ ] update `rule-x` — the page renamed\n>   - rename: `rule-y`\n"
    twice = ANSWER.replace(
        "> - [ ] create `estimate-x-works`", second + "> - [ ] create `estimate-x-works`"
    )
    code, err = answer(working, twice)
    assert code == 2 and "case 7: item [update][rule-x] stands twice" in err


def test_subagent_a_finding_is_sent_back_whatever_stop_hook_active_says(working):
    # 434: Claude Code sets `stop_hook_active` on the second fire after a handback with no
    # exit 2 of the hook; the store guards the loop — the same faulty text a second time passes
    no_read = ANSWER.replace("> - [ ] read `estimate-x-works`\n", "")
    code, err = answer(working, no_read, stop_hook_active=True)
    assert code == 2 and "estimate-x-works has no task line" in err
    assert answer(working, no_read, stop_hook_active=True) == (0, "")
    assert store(working)["7"]["findings"] == ["case 7: estimate-x-works has no task line"]


def transcript(project, *records):
    """A subagent transcript of assistant records, each a list of content blocks."""
    path = project / "agent.jsonl"
    lines = [
        json.dumps({"type": "assistant", "isSidechain": True, "message": {"content": blocks}})
        for blocks in records
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def text(value):
    return {"type": "text", "text": value}


def handback(value):
    return {"type": "tool_use", "name": "SubagentHandback", "input": {"message": value}}


def test_subagent_a_handback_then_a_summary_stores_the_handback_case(working):
    path = transcript(working, [handback(ANSWER)], [text("I sent Case 7.")])
    assert answer(working, "I sent Case 7.", agent_transcript_path=path) == (0, "")
    assert store(working)["7"]["text"].startswith("## Case 7")


def test_subagent_the_newest_output_with_a_case_is_the_answer(working):
    # a Case by handback, a newer Case as text, then a question by handback: the text's Case
    older = ANSWER.replace("The file is written.", "The old file is written.")
    path = transcript(working, [handback(older)], [text(ANSWER)], [handback("Which page?")])
    assert answer(working, "", agent_transcript_path=path) == (0, "")
    assert "The old file" not in store(working)["7"]["text"]


def test_subagent_a_case_as_text_then_by_handback_then_a_summary_is_stored_once(working):
    path = transcript(working, [text(ANSWER)], [handback(ANSWER)], [text("Sent.")])
    assert answer(working, "Sent.", agent_transcript_path=path) == (0, "")
    assert list(store(working)) == ["7"]


def test_subagent_no_output_with_a_case_and_no_transcript_fall_back(working):
    path = transcript(working, [text("Which page?")], [handback("Which page?")])
    assert answer(working, "Which page?", agent_transcript_path=path) == (0, "")
    assert store(working) is None
    missing = str(working / "none.jsonl")
    assert answer(working, ANSWER, agent_transcript_path=missing) == (0, "")
    assert "7" in store(working)


def test_subagent_a_foreign_key_of_an_update_is_sent_back(working):
    # 436.1: `replace old` under an `update` is not a key of the item
    wrong = ANSWER.replace("  - old: ``", "  - replace old: ``").replace(
        "  - new: `the new text`", "  - replace new: `the new text`"
    )
    code, err = answer(working, wrong)
    assert code == 2 and "`replace old`: not a key of update rule-x" in err


def test_subagent_a_schema_the_session_changes_is_not_judged(working):
    # 436.4: the categories come from the fences and the session's ledger; a window line with
    # no item in the answer is no finding
    schema = working / "vault" / "wiki" / "estimates" / "schema.yaml"
    schema.parent.mkdir(parents=True)
    schema.write_text("properties:\n  required: [type, purpose, method]\n", encoding="utf-8")
    odd = ANSWER.replace("  - kind: `QA`", "  - flavour: `QA`")
    code, err = answer(working, odd)
    assert code == 2 and "`flavour`: not a key of create estimate-x-works" in err
    folder = working / "vault" / "raw" / TODAY.isoformat() / "1501"
    folder.mkdir(parents=True)
    (folder / "ledger.md").write_text(
        "- 15:10:00 decision[case 5][update][rule-estimates-schema]{ref:rule-estimates-schema}\n",
        encoding="utf-8",
    )
    assert answer(working, odd) == (0, "")


def test_subagent_no_plan_file_sends_nothing_back(working):
    (working / ".claude" / "plans" / "plan.md").unlink()
    no_read = ANSWER.replace("> - [ ] read `estimate-x-works`\n", "")
    assert answer(working, no_read) == (0, "")


def test_subagent_a_question_and_another_agent_pass_unstored(working):
    assert answer(working, "Which of the two pages should the Case change?") == (0, "")
    assert answer(working, ANSWER, agent="ask-guppi") == (0, "")
    assert store(working) is None


# --- the comparison on Stop (case 419.4) ------------------------------------------------


def test_stop_the_checked_case_shown_unchanged_passes(working):
    answer(working, ANSWER)
    assert show(working, ANSWER + "\n---\n\nRatify?\n") == (0, "")


def test_stop_a_case_not_in_the_store_is_refused(working):
    code, err = show(working, ANSWER)
    assert code == 2 and "case 7: not built and checked by case-guppi" in err


def test_stop_a_changed_case_is_refused(working):
    answer(working, ANSWER)
    code, err = show(working, ANSWER.replace("The file is written.", "The file is written twice."))
    assert code == 2 and "case 7: differs from the answer of case-guppi" in err


def test_stop_a_case_stored_with_findings_is_refused(working):
    no_read = ANSWER.replace("> - [ ] read `estimate-x-works`\n", "")
    answer(working, no_read, stop_hook_active=True)
    code, err = show(working, no_read)
    assert code == 2 and "estimate-x-works has no task line" in err


def test_stop_a_heading_a_diff_and_a_short_form_are_not_compared(working):
    ack = "```LEDGER\n- decision[case 7][update][rule-x]{ref:rule-x}\n```\n\n## Case 7 — ratified\n\n**Changes:** x.\n"
    diff = "```DIFF\nCase 7 — context\n- old\n+ new\n```\n"
    assert show(working, ack) == (0, "")
    assert show(working, diff) == (0, "")
    assert show(working, SHORT_FORM) == (0, "")


def test_stop_a_case_shown_again_without_recommend_is_compared(working):
    again = ANSWER.replace("> **recommend:**\n> Совет.\n\n", "")
    code, err = show(working, again)
    assert code == 2 and "not built and checked" in err
    answer(working, again)
    assert show(working, again) == (0, "")


def test_stop_a_parent_is_compared_part_by_part(working):
    parent = "## Case 9 — родитель\n\n> **context:**\n> К.\n\n> **problem:**\n> П.\n\n> **recommend:**\n> С.\n\n"
    sub = ANSWER.replace("## Case 7 — пример", "### Case 9.1 — часть").replace("case 7", "case 9.1")
    sub = sub.replace(
        "> **context:**\n> Контекст.\n\n> **problem:**\n> Проблема.\n\n> **recommend:**\n> Совет.\n\n",
        "",
    )
    assert answer(working, parent + sub) == (0, "")
    assert set(store(working)) == {"9", "9.1"}
    assert show(working, parent + sub) == (0, "")
    code, err = show(working, parent.replace("К.", "К!") + sub)
    assert code == 2 and "case 9: differs" in err


def test_stop_the_re_fire_passes(working):
    assert show(working, ANSWER, stop_hook_active=True) == (0, "")
