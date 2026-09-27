"""`guppi casecheck`: `--subagent`, the `SubagentStop` hook that checks the Case of
`case-guppi` before the main agent sees it (case 419.3) and writes the file of a Case that
passed (case 452.1), and the `Stop` hook that compares a shown Case with the checked one (case
419.4) and requires the sending of its file (case 452.2). Rule page:
`vault/wiki/rules/rule-case-check.md`.

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


FOLDER = ("vault", "raw", TODAY.isoformat(), "1501")  # the session folder of `working`


def case_path(project, case):
    return casecheck.case_file(project.joinpath(*FOLDER), case)


def prompt(value="Go on."):
    """A prompt of the person: the record that opens a turn."""
    return {"type": "user", "isSidechain": False, "message": {"role": "user", "content": value}}


def sending(*files, timestamp="2026-09-09T15:29:00.000Z"):
    """An assistant record holding a `SendUserFile` call, in the shape Claude Code writes it
    (measured 2026-09-27, session 1255)."""
    call = {
        "type": "tool_use",
        "id": "toolu_01",
        "name": "SendUserFile",
        "input": {"files": [str(f) for f in files], "display": "render"},
    }
    return {
        "type": "assistant",
        "isSidechain": False,
        "timestamp": timestamp,
        "message": {"role": "assistant", "content": [call]},
    }


def result():
    """The tool result that follows a call: a `user` record that opens no turn."""
    block = {"type": "tool_result", "tool_use_id": "toolu_01", "content": "1 file delivered."}
    return {"type": "user", "isSidechain": False, "message": {"role": "user", "content": [block]}}


def main_transcript(project, records):
    path = project / "transcript.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in records) + "\n", encoding="utf-8")
    return str(path)


def show(project, reply, sent=None, records=None, **fields):
    """The `Stop` hook on `reply`; its turn sends the file of each top-level Case the reply
    holds, or the files of `sent`, or is `records` whole."""
    if records is None:
        cases = casecheck.split_cases(reply)
        files = sent if sent is not None else sorted({case_path(project, c) for c in cases})
        records = [prompt(), sending(*files), result()] if files else [prompt()]
    fields.setdefault("transcript_path", main_transcript(project, records))
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
    assert not (working.joinpath(*FOLDER) / "cases").exists()


# --- the file of a built Case (case 452.1) ----------------------------------------------

PARENT = "## Case 9 — родитель\n\n> **context:**\n> К.\n\n> **problem:**\n> П.\n\n> **recommend:**\n> С.\n\n"


def sub_case(case, then="The file is written."):
    """A sub-case of Case 9 built from ANSWER, its own ids, slugs and anchor."""
    n = case.split(".")[1]
    anchor = "`` the `old` text ``" if n == "1" else "`Prevents x:`"
    return (
        ANSWER.replace("## Case 7 — пример", f"### Case {case} — часть")
        .replace("case 7", f"case {case}")
        .replace(
            "> **context:**\n> Контекст.\n\n> **problem:**\n> Проблема.\n\n> **recommend:**\n> Совет.\n\n",
            "",
        )
        .replace("estimate-x-works", f"estimate-x-works-{n}")
        .replace("The file is written.", then)
        .replace("`` the `old` text ``", anchor)
    )


def test_subagent_the_time_of_the_store(working):
    assert answer(working, ANSWER) == (0, "")
    assert store(working)["7"]["stored"] == NOW.isoformat()


def test_subagent_the_file_is_written_from_the_stored_text(working):
    assert answer(working, ANSWER + "\n---\n\nThe agent's own words.\n") == (0, "")
    path = case_path(working, "7")
    assert path == working.joinpath(*FOLDER, "cases", "case-7.md")
    assert path.read_text(encoding="utf-8") == store(working)["7"]["text"] + "\n"
    assert "own words" not in path.read_text(encoding="utf-8")


def test_subagent_the_file_is_replaced_whole_when_the_answer_holds_the_top_case(working):
    assert answer(working, PARENT + sub_case("9.1") + "\n" + sub_case("9.2")) == (0, "")
    path = case_path(working, "9.2")
    assert path.name == "case-9.md" and "### Case 9.2" in path.read_text(encoding="utf-8")
    assert answer(working, PARENT.replace("> К.", "> К2.") + sub_case("9.1")) == (0, "")
    text = path.read_text(encoding="utf-8")
    held = store(working)
    assert text == held["9"]["text"] + "\n\n" + held["9.1"]["text"] + "\n"
    assert "### Case 9.2" not in text and "> К2." in text


def test_subagent_a_sub_case_alone_replaces_its_section_alone(working):
    assert answer(working, PARENT + sub_case("9.1") + "\n" + sub_case("9.2")) == (0, "")
    assert answer(working, sub_case("9.1", "The file is written again.")) == (0, "")
    text = case_path(working, "9").read_text(encoding="utf-8")
    held = store(working)
    assert text == "\n\n".join(held[c]["text"] for c in ("9", "9.1", "9.2")) + "\n"
    assert "The file is written again." in text and text.count("### Case 9.1") == 1


def test_subagent_no_file_on_a_finding(working):
    no_read = ANSWER.replace("> - [ ] read `estimate-x-works`\n", "")
    assert answer(working, no_read)[0] == 2
    assert not case_path(working, "7").exists()
    assert answer(working, no_read) == (0, "")  # repeated: stored again, still no file
    assert not case_path(working, "7").exists()
    assert answer(working, ANSWER) == (0, "")
    clean = case_path(working, "7").read_text(encoding="utf-8")
    assert answer(working, no_read)[0] == 2
    assert case_path(working, "7").read_text(encoding="utf-8") == clean  # left as it stood


def test_subagent_the_path_of_the_file_is_one_the_guard_judges(working):
    # 453: the writer's path stays inside the one predicate of the guard
    for case in ("7", "9.1", "452.12"):
        assert casecheck.is_case_file(case_path(working, case))


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
    assert code == 2 and "case 7: its then differ from the answer of case-guppi" in err


def test_stop_the_translated_prose_and_heading_pass(working):
    # 441.3: the name of the heading, `context`, `problem` and `recommend` are not compared
    answer(working, ANSWER)
    translated = (
        ANSWER.replace("## Case 7 — пример", "## Case 7 — an example")
        .replace("> Контекст.", "> The context.\n> Two lines of it.")
        .replace("> Проблема.", "> The problem.")
        .replace("> Совет.", "> The advice.")
    )
    assert show(working, translated) == (0, "")


def test_stop_a_changed_mechanical_part_is_refused(working):
    # 441.3: `given`, `then`, a task sub-point, a `ratification` line
    answer(working, ANSWER)
    changes = {
        "given": ANSWER.replace("— its Estimate.", "— its promise."),
        "tasks": ANSWER.replace("`the new text`", "`the newer text`"),
        "ratification": ANSWER.replace("{ref:rule-x}", "{ref:rule-y}", 1),
    }
    for part, shown in changes.items():
        assert shown != ANSWER, part
        code, err = show(working, shown)
        assert code == 2 and f"its {part} differ" in err, (part, err)


RATIFICATION = ANSWER[ANSWER.index("> **ratification:**") :]
SHORT_SHOWING = (
    "## Case 7 — пример\n\nМеняет правило x: одна пара `replace` и новое Estimate.\n\n"
    + RATIFICATION
    + "\n---\n\nРатифицируешь?\n"
)


def test_stop_a_showing_of_the_ratification_alone_passes(working):
    # 452.2: a section the reply does not show is not compared; the short text is not either
    answer(working, ANSWER)
    assert show(working, SHORT_SHOWING) == (0, "")
    no_when = ANSWER.replace("> **when:**\n> The agent runs `guppi x`.\n\n", "")
    assert show(working, no_when) == (0, "")


def test_stop_a_showing_of_the_ratification_alone_that_differs_is_refused(working):
    answer(working, ANSWER)
    code, err = show(working, SHORT_SHOWING.replace("{ref:rule-x}", "{ref:rule-y}", 1))
    assert code == 2 and "case 7: its ratification differ" in err


def test_stop_a_shown_case_with_no_sending_is_refused(working):
    # 452.2: no `SendUserFile` call in the turn, or one only in an earlier turn
    answer(working, ANSWER)
    code, err = show(working, SHORT_SHOWING, sent=[])
    assert code == 2 and "case 7: no SendUserFile call on" in err
    assert str(case_path(working, "7")) in err
    earlier = [prompt(), sending(case_path(working, "7")), result(), prompt("Why?")]
    code, err = show(working, SHORT_SHOWING, records=earlier)
    assert code == 2 and "case 7: no SendUserFile call on" in err
    later = [prompt(), prompt("Show it."), sending(case_path(working, "7")), result()]
    assert show(working, SHORT_SHOWING, records=later) == (0, "")


def test_stop_a_sending_of_another_file_is_refused(working):
    answer(working, ANSWER)
    code, err = show(working, SHORT_SHOWING, sent=[case_path(working, "8")])
    assert code == 2 and "case 7: no SendUserFile call on" in err


def test_stop_a_sending_names_the_file_by_a_relative_or_an_absolute_path(working):
    answer(working, ANSWER)
    relative = "/".join((*FOLDER, "cases", "case-7.md"))
    assert show(working, SHORT_SHOWING, sent=[relative]) == (0, "")


def test_stop_the_acknowledging_reply_is_not_judged_and_needs_no_sending(working):
    answer(working, ANSWER)
    ack = "```LEDGER\n- decision[case 7][update][rule-x]{ref:rule-x}\n```\n\n## Case 7 — ratified\n\n**Changes:** x.\n"
    assert show(working, ack, sent=[]) == (0, "")


def test_stop_a_case_stored_with_findings_is_refused(working):
    no_read = ANSWER.replace("> - [ ] read `estimate-x-works`\n", "")
    answer(working, no_read, stop_hook_active=True)
    code, err = show(working, no_read)
    assert code == 2 and "estimate-x-works has no task line" in err


def test_stop_a_heading_a_diff_and_a_short_form_are_not_compared(working):
    ack = "```LEDGER\n- decision[case 7][update][rule-x]{ref:rule-x}\n```\n\n## Case 7 — ratified\n\n**Changes:** x.\n"
    diff = "```DIFF\nCase 7 — context\n- old\n+ new\n```\n"
    assert show(working, ack, sent=[]) == (0, "")
    assert show(working, diff, sent=[]) == (0, "")
    assert show(working, SHORT_FORM, sent=[]) == (0, "")


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
    assert show(working, parent.replace("К.", "К!") + sub) == (0, "")  # prose, not compared
    code, err = show(working, parent + sub.replace("The file is written.", "Written twice."))
    assert code == 2 and "case 9.1: its then differ" in err


def test_stop_the_re_fire_passes(working):
    assert show(working, ANSWER, stop_hook_active=True) == (0, "")


# --- Case 467.2: an open backlog line of the Frontier ------------------------------------

UPDATE_LINE = "decision[case 7][update][rule-x]{ref:rule-x}"


def taken_from_the_backlog(project, line="- [ ] C1 — `rule-x`, taken up · backlog\n"):
    """`rule-x` deferred by case 5, and the Frontier line that takes it up."""
    rule = project / "vault" / "wiki" / "rules" / "rule-x.md"
    rule.write_text(
        RULE_X.replace("status: draft\n", "status: draft\ndeferred_by: [decision-case-5]\n"),
        encoding="utf-8",
    )
    frontier = project.joinpath(*FOLDER) / "frontier.md"
    frontier.parent.mkdir(parents=True, exist_ok=True)
    frontier.write_text(f"# Frontier\n\n## Cases\n\n{line}", encoding="utf-8")


def test_subagent_backlog_a_case_naming_the_page_without_its_supersedes_is_sent_back(working):
    taken_from_the_backlog(working)
    code, err = answer(working, ANSWER)
    assert code == 2
    assert (
        "case 7: names rule-x, the page of the open backlog line C1, and no Case among case 7 "
        "and its sub-cases names it and carries {supersedes:case 5}"
    ) in err


def test_subagent_backlog_a_case_with_every_supersedes_passes(working):
    taken_from_the_backlog(working)
    marked = ANSWER.replace(UPDATE_LINE, UPDATE_LINE + "{supersedes:case 5}")
    assert answer(working, marked) == (0, "")


def test_subagent_backlog_a_sub_case_that_supersedes_covers_its_sibling(working):
    taken_from_the_backlog(working)
    first = sub_case("9.1").replace(
        "decision[case 9.1][update][rule-x]{ref:rule-x}",
        "decision[case 9.1][update][rule-x]{ref:rule-x}{supersedes:case 5}",
    )
    assert answer(working, PARENT + first + "\n" + sub_case("9.2")) == (0, "")


@pytest.mark.parametrize(
    "line",
    ["- [x] C1 — `rule-x`, taken up · backlog · case 7\n", "- [ ] C1 — `rule-x` · brief\n"],
)
def test_subagent_backlog_no_open_backlog_line_is_no_finding(working, line):
    taken_from_the_backlog(working, line)
    assert answer(working, ANSWER) == (0, "")


def test_backlog_a_case_naming_the_page_only_in_a_defer_line_is_not_judged(working):
    taken_from_the_backlog(working)
    records = [casecheck.parse_line("- decision[case 8][defer][rule-x]")]
    frontier = working.joinpath(*FOLDER) / "frontier.md"
    assert casecheck.check_backlog(records, frontier, working) == []
