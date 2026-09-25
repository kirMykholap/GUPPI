"""`guppi ratified`: the `Stop` hook that writes a ratified Case from the chat into the plan
and its ratified copy (case 387.2), and `--edit`, the `PostToolUse` hook that compares an
edited plan with that copy (case 387.3).

Every test feeds the payload through a stream, the shape a hook is really handed.
"""

import io
import json
from datetime import UTC, date, datetime

import pytest

from guppi import ratified
from guppi.materialize import split_cases, then_blocks

TODAY = date(2026, 9, 9)
NOW = datetime(2026, 9, 9, 15, 30, 0, tzinfo=UTC)
SESSION = "44c1aae1-4076-4a58-a7c0-d20bc274047c"

SHOWING = """## Case 7 — пример

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
> **－** Nothing else.

> **tasks:**
> - [ ] update `rule-x` — one `replace` pair
>   - old: `` the `old` text ``
>   - new: `the new text`
>   - set: `{status: draft}`
>   - change: `the text changed (case 7)`
> - [ ] create `estimate-x-works`
>   - type: `estimate`
>   - kind: `QA`
>   - purpose: `X works`
>   - method: `uv run pytest tests/test_x.py`
>   - tags: `[harness]`
>   - sections.Criterion:
>     ```text
>     When: a
>     Then: b
>     ```
> - [ ] `guppi/x.py` — the code
> - [ ] read `estimate-x-works`

> **ratification:**
> ```
> - decision[case 7][update][rule-x]{ref:rule-x}
> - decision[case 7][create][estimate-x-works]{ref:rule-x}{tags:harness}
> ```

---

Ratify?
"""

LINES = (
    "- decision[case 7][update][rule-x]{ref:rule-x}\n"
    "- decision[case 7][create][estimate-x-works]{ref:rule-x}{tags:harness}\n"
)
ACK = f"```LEDGER\n{LINES}```\n\n## Case 7 — ratified\n\n**Changes:** the text.\n"

EXPECTED_BLOCK = {
    "update": [
        {
            "slug": "rule-x",
            "replace": [{"old": "the `old` text", "new": "the new text"}],
            "set": {"status": "draft"},
            "change": "the text changed (case 7)",
        }
    ],
    "create": [
        {
            "slug": "estimate-x-works",
            "type": "estimate",
            "kind": "QA",
            "purpose": "X works",
            "method": "uv run pytest tests/test_x.py",
            "tags": ["harness"],
            "sections": {"Criterion": "When: a\nThen: b"},
            "ref": "rule-x",
        }
    ],
}


RULE_X = """---
type: rule
kind: Leaf
purpose: Prevents x
status: draft
---

## Purpose

Prevents x: the `old` text stands here.
"""


def transcript_line(text):
    return json.dumps(
        {
            "type": "assistant",
            "isSidechain": False,
            "sessionId": SESSION,
            "message": {"role": "assistant", "content": [{"type": "text", "text": text}]},
        },
        ensure_ascii=False,
    )


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


def plan_of(project):
    return project / ".claude" / "plans" / "plan.md"


def stop(project, reply, *messages, **fields):
    transcript = project / "transcript.jsonl"
    transcript.write_text("\n".join(transcript_line(m) for m in messages) + "\n", encoding="utf-8")
    fields.setdefault("session_id", SESSION)
    stdin = io.StringIO(
        json.dumps(
            {"last_assistant_message": reply, "transcript_path": str(transcript), **fields},
            ensure_ascii=False,
        )
    )
    err = io.StringIO()
    code = ratified.run([], stdin=stdin, stderr=err, project_dir=project, now=NOW)
    return code, err.getvalue()


def edit(project, path=None):
    stdin = io.StringIO(
        json.dumps(
            {"tool_name": "Edit", "tool_input": {"file_path": str(path or plan_of(project))}}
        )
    )
    out = io.StringIO()
    code = ratified.run(["--edit"], stdin=stdin, stdout=out, project_dir=project, now=NOW)
    return code, out.getvalue()


# --- the write (case 387.2) ------------------------------------------------------------


def test_write_the_ratified_case_goes_into_the_plan_and_the_copy(working):
    assert stop(working, ACK, SHOWING, ACK) == (0, "")
    plan = plan_of(working).read_text(encoding="utf-8")
    copy = ratified.copy_of(plan_of(working)).read_text(encoding="utf-8")
    for text in (plan, copy):
        lines = split_cases(text)["7"]
        assert "## Case 7 — пример" in text
        sections = ratified.quoted_sections(lines, ratified.SPEC_SECTIONS)
        assert (
            sections["given"] == "`rule-x` — the rule.\n**＋** `estimate-x-works` — its Estimate."
        )
        assert sections["context"] == "Контекст." and sections["problem"] == "Проблема."
        assert "recommend" not in text and "**ratification:**" not in text
        block, errors = then_blocks(lines)
        assert errors == [] and block == EXPECTED_BLOCK
        tasks = "\n".join(ratified.tagged_blocks(lines, "tasks"))
        assert tasks.splitlines() == [
            "- [ ] update `rule-x` — one `replace` pair",
            "- [ ] create `estimate-x-works`",
            "- [ ] `guppi/x.py` — the code",
            "- [ ] read `estimate-x-works`",
        ]
    assert plan.startswith("# Spec — 2026-09-09, session 1501\n")
    assert copy.startswith("# Ratified copy of plan.md\n")


def test_write_a_second_showing_replaces_the_section_and_keeps_the_prose(working):
    stop(working, ACK, SHOWING, ACK)
    again = SHOWING.replace("> **context:**\n> Контекст.\n\n> **problem:**\n> Проблема.\n\n", "")
    again = again.replace("The file is written.", "The file is written once.")
    assert stop(working, ACK, SHOWING, ACK, again, ACK) == (0, "")
    plan = plan_of(working).read_text(encoding="utf-8")
    assert plan.count("## Case 7 —") == 1
    sections = ratified.quoted_sections(split_cases(plan)["7"], ratified.SPEC_SECTIONS)
    assert sections["then"].startswith("The file is written once.")
    assert sections["context"] == "Контекст."  # a re-showing leaves it out; the plan keeps it


def test_write_a_last_mention_in_a_diff_block_writes_nothing(working):
    diff = "```DIFF\nCase 7 · context\n- old\n+ new\n```\n"
    assert stop(working, ACK, SHOWING, diff, ACK) == (0, "")
    assert "Case 7" not in plan_of(working).read_text(encoding="utf-8")


def test_write_a_defer_only_case_is_left_to_the_agent(working):
    reply = "```LEDGER\n- decision[case 8][defer][rule-y]{ref:rule-y}\n```\n"
    assert stop(working, reply, reply) == (0, "")
    assert "Case 8" not in plan_of(working).read_text(encoding="utf-8")


def test_write_no_plan_file_in_the_event_log_is_refused(working):
    log = working / "vault" / "raw" / TODAY.isoformat() / "event_log.md"
    log.write_text(
        "- 15:01:00 44c1aae1 session-start startup\n- 15:01:30 44c1aae1 hi\n", encoding="utf-8"
    )
    code, err = stop(working, ACK, SHOWING, ACK)
    assert code == 2 and "no plan file of this session" in err


def test_write_no_showing_is_refused(working):
    code, err = stop(working, ACK, "Nothing shown.", ACK)
    assert code == 2 and "case 7: no earlier reply shows it whole" in err


def test_write_a_sub_point_off_the_form_is_refused_and_nothing_is_written(working):
    broken = SHOWING.replace("  - kind: `QA`", "  - kind: QA")
    code, err = stop(working, ACK, broken, ACK)
    assert code == 2 and "`kind`: the value is not one code span" in err
    assert "Case 7" not in plan_of(working).read_text(encoding="utf-8")


def test_write_a_value_at_a_backtick_takes_an_outer_span_padded_by_one_space():
    """Case 393: CommonMark's reading, which `code_value` shares."""
    value = "`uv run guppi x` on `Stop`"
    padded = f"- [ ] create `rule-x` — the rule\n  - sections.How it works: `` {value} ``\n"
    _, block, errors = ratified.read_tasks(padded)
    assert errors == [] and block["create"][0]["sections"]["How it works"] == value
    opening = "`uv run guppi x` on `Stop`. It prints."
    unpadded = f"- [ ] create `rule-x` — the rule\n  - sections.How it works: ``{opening}``\n"
    _, _, errors = ratified.read_tasks(unpadded)
    assert errors == ["`sections.How it works`: the value is not one code span"]


def test_write_a_value_holding_a_backtick_unpadded_is_refused_padded_read():
    """Case 402: a value that opens and closes with a code span, unpadded, would lose its edge
    backticks as CommonMark reads it; the hook refuses it with the reason."""
    value = "`a` and `b`"
    unpadded = f"- [ ] update `rule-x` — a pair\n  - old: ``{value}``\n  - new: `x`\n"
    _, _, errors = ratified.read_tasks(unpadded)
    assert errors[0] == f"`old`: {ratified.UNPADDED}"
    inside = "- [ ] update `rule-x` — a pair\n  - old: ``the `a` text``\n  - new: `x`\n"
    _, _, errors = ratified.read_tasks(inside)
    assert errors[0] == f"`old`: {ratified.UNPADDED}"
    padded = f"- [ ] update `rule-x` — a pair\n  - old: `` {value} ``\n  - new: `x`\n"
    _, block, errors = ratified.read_tasks(padded)
    assert errors == [] and block["update"][0]["replace"] == [{"old": value, "new": "x"}]


def test_write_an_unpadded_value_refuses_the_case_whole(working):
    broken = SHOWING.replace("`` the `old` text ``", "``the `old` text``")
    code, err = stop(working, ACK, broken, ACK)
    assert code == 2 and f"`old`: {ratified.UNPADDED}" in err
    assert "Case 7" not in plan_of(working).read_text(encoding="utf-8")


def test_write_nothing_outside_a_working_session_and_nothing_on_the_re_fire(working, tmp_path):
    assert stop(working, ACK, SHOWING, ACK, session_id="ffffffff-0000") == (0, "")
    assert stop(working, ACK, SHOWING, ACK, stop_hook_active=True) == (0, "")
    assert "Case 7" not in plan_of(working).read_text(encoding="utf-8")


def test_write_a_sub_case_brings_its_parents_prose(working):
    showing = (
        "## Case 9 — родитель\n\n> **context:**\n> Общий контекст.\n\n> **problem:**\n> Вопрос.\n\n"
        + SHOWING.replace("## Case 7 — пример", "### Case 9.1 — ребёнок")
        .replace("case 7", "case 9.1")
        .replace("> **context:**\n> Контекст.\n\n> **problem:**\n> Проблема.\n\n", "")
    )
    ack = ACK.replace("case 7", "case 9.1")
    assert stop(working, ack, showing, ack) == (0, "")
    plan = plan_of(working).read_text(encoding="utf-8")
    assert plan.index("## Case 9 — родитель") < plan.index("### Case 9.1 — ребёнок")
    parent = ratified.quoted_sections(split_cases(plan)["9"], ratified.SPEC_SECTIONS)
    assert parent == {"context": "Общий контекст.", "problem": "Вопрос."}


# --- the check after the write (case 414.1) --------------------------------------------

OUT_OF_FRAME = SHOWING.replace("The file is written.", "The file `guppi/y.py` is written.")


def test_checks_the_written_case_a_finding_exits_2_and_the_case_stays(working):
    code, err = stop(working, ACK, OUT_OF_FRAME, ACK)
    assert code == 2
    assert err.startswith("ratified: ") and "case 7: guppi/y.py is not named in its given" in err
    for path in (plan_of(working), ratified.copy_of(plan_of(working))):
        assert "## Case 7 — пример" in path.read_text(encoding="utf-8")


def test_checks_the_written_case_a_clean_one_exits_0_on_the_lines_of_the_reply(working):
    # no `ledger.md` yet: the ledger hook runs beside this one; the reply's lines count
    assert not (working / "vault" / "raw" / TODAY.isoformat() / "1501" / "ledger.md").exists()
    assert stop(working, ACK, SHOWING, ACK) == (0, "")


def test_checks_the_written_case_a_line_both_in_the_ledger_and_the_reply_counts_once(working):
    ledger = working / "vault" / "raw" / TODAY.isoformat() / "1501" / "ledger.md"
    ledger.parent.mkdir(parents=True)
    ledger.write_text("".join(f"- 15:20:00 {line[2:]}\n" for line in LINES.splitlines()))
    assert stop(working, ACK, SHOWING, ACK) == (0, "")


def test_checks_the_written_case_a_finding_of_another_case_is_not_reported(working):
    other = (
        OUT_OF_FRAME.replace("## Case 7 — пример", "## Case 8 — другой")
        .replace("case 7", "case 8")
        .replace("old: `` the `old` text ``", "old: `Prevents x:`")  # its own anchor
    )
    stop(working, ACK.replace("case 7", "case 8"), other, ACK.replace("case 7", "case 8"))
    assert stop(working, ACK, SHOWING, ACK) == (0, "")


def test_checks_the_written_case_the_re_fire_checks_nothing(working):
    assert stop(working, ACK, OUT_OF_FRAME, ACK, stop_hook_active=True) == (0, "")


# --- the reconciliation (case 387.3) -------------------------------------------------


def test_reconcile_an_edit_of_what_the_scripts_apply_is_named_and_marked(working):
    stop(working, ACK, SHOWING, ACK)
    plan = plan_of(working)
    plan.write_text(
        plan.read_text(encoding="utf-8").replace("The file is written.", "Two files."),
        encoding="utf-8",
    )
    code, out = edit(working)
    assert code == 0
    context = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    assert "case 7: then changed since the ratification" in context
    assert ratified.read_marks(plan) == ["7"]


def test_reconcile_an_edit_of_prose_alone_is_silent(working):
    stop(working, ACK, SHOWING, ACK)
    plan = plan_of(working)
    plan.write_text(
        plan.read_text(encoding="utf-8")
        .replace("Контекст.", "Context.")
        .replace("пример", "example"),
        encoding="utf-8",
    )
    assert edit(working) == (0, "")
    assert ratified.read_marks(plan) == []


def test_reconcile_a_marked_case_not_shown_whole_is_refused_once(working):
    stop(working, ACK, SHOWING, ACK)
    plan = plan_of(working)
    plan.write_text(
        plan.read_text(encoding="utf-8")
        .replace("`the new text`", "`other`")
        .replace("new: the new text", "new: other"),
        encoding="utf-8",
    )
    edit(working)
    code, err = stop(working, "Changed it.", "Changed it.")
    assert code == 2 and "case 7 changed in then block since its ratification" in err
    assert ratified.read_marks(plan) == []
    assert stop(working, "An answer to a question.", "An answer to a question.") == (0, "")


def test_reconcile_a_marked_case_shown_whole_passes(working):
    stop(working, ACK, SHOWING, ACK)
    plan = plan_of(working)
    plan.write_text(
        plan.read_text(encoding="utf-8").replace("The file is written.", "Two files."),
        encoding="utf-8",
    )
    edit(working)
    reshown = SHOWING.replace("The file is written.", "Two files.")
    assert stop(working, reshown, reshown) == (0, "")


def test_reconcile_another_file_or_no_copy_is_not_compared(working):
    other = working / "notes.md"
    other.write_text("## Case 7 — x\n", encoding="utf-8")
    assert edit(working, other) == (0, "")
    assert edit(working) == (0, "")  # no copy yet


def test_differences_skip_the_deferred_and_untranslated_finds_cyrillic():
    copy = (
        "## Case 1 — a\n\n> **then:**\n> A.\n\n## Deferred\n\n## Case 2 — b\n\n> **then:**\n> B.\n"
    )
    plan = copy.replace("> A.", "> C.").replace("> B.", "> D.")
    assert ratified.differences(plan, copy) == {"1": ["then"]}
    text = "## Case 1 — имя\n\n> **context:**\n> Text.\n\n> **problem:**\n> Вопрос.\n"
    assert ratified.untranslated(text) == [("1", "name"), ("1", "problem")]
