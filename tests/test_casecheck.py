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

ANSWER = """## Case 7 — example

> **context:**
> Context.

> **problem:**
> Problem.

> **recommend:**
> Advice.

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

SHORT_FORM = """## Case 8 — deferred

> **context:**
> Context.

> **problem:**
> Problem.

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
    (tmp_path / "guppi.toml").write_text(
        'documentation_lang = "en"\nchat_lang = "ru"\n', encoding="utf-8"
    )
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


def answer(project, text, agent="case-guppi", now=NOW, **fields):
    payload = {
        "session_id": SESSION,
        "agent_type": agent,
        "last_assistant_message": text,
        "hook_event_name": "SubagentStop",
        **fields,
    }
    err = io.StringIO()
    stdin = io.StringIO(json.dumps(payload, ensure_ascii=False))
    code = casecheck.run(["--subagent"], stdin=stdin, stderr=err, project_dir=project, now=now)
    return code, err.getvalue()


FOLDER = ("vault", "raw", TODAY.isoformat(), "1501")  # the session folder of `working`


def case_path(project, case):
    return casecheck.case_file(project.joinpath(*FOLDER), case)


def prompt(value="Go on."):
    """A prompt of the person: the record that opens a turn, `origin.kind` `human` (case 592)."""
    return {
        "type": "user",
        "isSidechain": False,
        "origin": {"kind": "human"},
        "message": {"role": "user", "content": value},
    }


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
    assert entry["text"].startswith("## Case 7 — example\n\n> **context:**")
    assert entry["text"].endswith("> ```")


def test_subagent_a_missing_section_sends_it_back(working):
    faulty = ANSWER.replace(
        "> **given:**\n> `rule-x` — the rule.\n> **＋** `estimate-x-works` — its Estimate.\n\n", ""
    )
    code, err = answer(working, faulty)
    assert code == 2 and "case 7: missing section given" in err
    assert store(working)["7"]["findings"]


def test_subagent_sections_out_of_order_and_a_ratification_with_text(working):
    moved = (
        ANSWER.replace("> **recommend:**\n> Advice.\n\n", "") + "\n> **recommend:**\n> Advice.\n"
    )
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

PARENT = "## Case 9 — parent\n\n> **context:**\n> C.\n\n> **problem:**\n> P.\n\n> **recommend:**\n> A.\n\n"


def sub_case(case, then="The file is written."):
    """A sub-case of Case 9 built from ANSWER, its own ids, slugs and anchor."""
    n = case.split(".")[1]
    anchor = "`` the `old` text ``" if n == "1" else "`Prevents x:`"
    return (
        ANSWER.replace("## Case 7 — example", f"### Case {case} — part")
        .replace("case 7", f"case {case}")
        .replace(
            "> **context:**\n> Context.\n\n> **problem:**\n> Problem.\n\n> **recommend:**\n> Advice.\n\n",
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
    assert answer(
        working, PARENT + sub_case("9.1") + "\n" + sub_case("9.2", "The page is read.")
    ) == (0, "")
    path = case_path(working, "9.2")
    assert path.name == "case-9.md" and "### Case 9.2" in path.read_text(encoding="utf-8")
    assert answer(working, PARENT.replace("> C.", "> C2.") + sub_case("9.1")) == (0, "")
    text = path.read_text(encoding="utf-8")
    held = store(working)
    assert text == held["9"]["text"] + "\n\n" + held["9.1"]["text"] + "\n"
    assert "### Case 9.2" not in text and "> C2." in text


def test_subagent_a_sub_case_alone_replaces_its_section_alone(working):
    assert answer(
        working, PARENT + sub_case("9.1") + "\n" + sub_case("9.2", "The page is read.")
    ) == (0, "")
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


# --- each question of the rounds in recommend (case 544.3) --------------------------------


def round_of(*titles):
    """A round of questions in the template of the skill `grill-me`, one question per title."""
    parts = ["**Context:**\nThe item.\n"]
    for n, title in enumerate(titles, 1):
        parts.append(f"❓ **Q{n}** - **{title}**:\n\n{QUESTION_BODY}")
    return "\n".join(parts)


QUESTION_BODY = (
    "**Now:** it stands.\n\n**Options:**\n\n🔹 **(a) Keep it**\n  - **After:** it stays.\n\n"
    "🔹 **(b) Change it**\n  - **After:** it moves.\n\n➡️ (a).\n"
)


def with_items(*titles):
    """ANSWER whose `recommend` holds one item per title."""
    items = "".join(
        f"> - **{t}**\n>   - Recommended: (a).\n>   - Answer: agreed.\n" for t in titles
    )
    return ANSWER.replace("> **recommend:**\n> Advice.\n", "> **recommend:**\n" + items)


def test_subagent_rounds_every_title_in_recommend_passes(working):
    path = transcript(
        working,
        [text(round_of("Which page changes?", "Which test?"))],
        [text(with_items("Which page changes?", "Which test?"))],
    )
    assert answer(working, "", agent_transcript_path=path) == (0, "")


def test_subagent_rounds_a_title_missing_from_recommend_is_sent_back(working):
    path = transcript(
        working,
        [text(round_of("Which page changes?", "Which test?"))],
        [text(with_items("Which page changes?"))],
    )
    code, err = answer(working, "", agent_transcript_path=path)
    assert code == 2
    assert "case 7: recommend holds no item for the question of the rounds: Which test?" in err
    assert "Which page changes?" not in err


def test_subagent_rounds_a_title_asked_in_two_rounds_is_looked_for_once(working):
    path = transcript(
        working,
        [text(round_of("Which test?"))],
        [text(round_of("Which test?"))],
        [text(ANSWER)],
    )
    code, err = answer(working, "", agent_transcript_path=path)
    assert code == 2 and err.count("Which test?") == 1
    again = transcript(
        working,
        [text(round_of("Which test?"))],
        [text(round_of("Which test?"))],
        [text(with_items("Which test?"))],
    )
    assert answer(working, "", agent_transcript_path=again) == (0, "")


def test_subagent_rounds_an_answer_with_no_round_passes(working):
    path = transcript(working, [text(ANSWER)])
    assert answer(working, "", agent_transcript_path=path) == (0, "")


def test_subagent_rounds_the_words_after_the_title_are_not_judged(working):
    items = "> - **Which test?**\n>   - Anything at all.\n"
    odd = ANSWER.replace("> **recommend:**\n> Advice.\n", "> **recommend:**\n" + items)
    path = transcript(working, [text(round_of("Which test?"))], [text(odd)])
    assert answer(working, "", agent_transcript_path=path) == (0, "")


def test_subagent_rounds_a_round_sent_back_for_its_form_gives_no_title(working):
    # case 601.5: the round sent back stays in the transcript; its changed title is not required
    faulty = round_of("Which page?").replace("**Now:** it stands.\n\n", "")
    path = transcript(
        working,
        [text(faulty)],
        [text(round_of("Which page changes?"))],
        [text(with_items("Which page changes?"))],
    )
    assert answer(working, "", agent_transcript_path=path) == (0, "")


# --- the form of a round (case 601.1) -------------------------------------------------------


def round_answer(working, *outputs):
    """The `--subagent` run on a transcript whose outputs are the given texts, in order."""
    return answer(
        working, "", agent_transcript_path=transcript(working, *[[text(o)] for o in outputs])
    )


def test_subagent_round_form_a_round_in_form_passes_unstored(working):
    assert round_answer(working, round_of("Which page?", "Which test?")) == (0, "")
    assert store(working) is None
    assert not (working.joinpath(*FOLDER) / "cases").exists()


@pytest.mark.parametrize(
    ("old", "new", "missing"),
    [
        ("**Which page?**:", "**Which page?**", "the title line"),
        ("**Now:** it stands.\n\n", "", "a `**Now:**` line"),
        ("**Options:**\n", "**Options:** two\n", "the `**Options:**` label alone"),
        ("  - **After:** it stays.\n", "", None),
        ("➡️ (a).\n", "", "a `➡️` line"),
    ],
)
def test_subagent_round_form_a_question_out_of_form_is_sent_back(working, old, new, missing):
    faulty = round_of("Which page?").replace(old, new)
    if missing is None:  # no option keeps an After item
        faulty = faulty.replace("  - **After:** it moves.\n", "")
        missing = "an option `🔹` with an `- **After:**` item"
    code, err = round_answer(working, faulty)
    assert code == 2
    assert missing in err and "Which page?" in err and "answer with the round whole again" in err
    assert store(working) is None


def test_subagent_round_form_the_same_faulty_round_is_sent_back_once(working):
    faulty = round_of("Which page?").replace("**Which page?**:", "**Which page?**")
    assert round_answer(working, faulty)[0] == 2
    assert round_answer(working, faulty, faulty + "  \n") == (0, "")


def test_subagent_round_form_a_fact_and_a_case_are_not_judged_as_rounds(working):
    fact = "**Fact:** The page says so.\n\n❓ **Q1** - **Which page?**\n"
    assert round_answer(working, fact) == (0, "")
    assert round_answer(working, ANSWER) == (0, "")


def test_subagent_round_form_an_unreadable_transcript_is_not_judged(working):
    faulty = round_of("Which page?").replace("**Which page?**:", "**Which page?**")
    missing = str(working / "none.jsonl")
    assert answer(working, faulty, agent_transcript_path=missing) == (0, "")


def test_subagent_round_form_no_plan_file_still_sends_the_round_back(working):
    (working / ".claude" / "plans" / "plan.md").unlink()
    faulty = round_of("Which page?").replace("**Which page?**:", "**Which page?**")
    code, err = round_answer(working, faulty)
    assert code == 2 and "the title line" in err


def test_subagent_round_form_the_indent_of_a_hand_back_is_set_aside(working):
    indented = "  " + round_of("Which page?").replace("\n", "\n  ")
    path = transcript(working, [handback(indented)])
    assert answer(working, "", agent_transcript_path=path) == (0, "")


# --- the answer is the newest Case, round or Fact answer (cases 607.1, 607.2) ---------------

LATER = datetime(2026, 9, 9, 15, 40, 0, tzinfo=UTC)


def built_then(working, *later):
    """Case 7 built and stored at NOW, then the `--subagent` run at LATER on a transcript of
    that Case and the `later` outputs; the outcome, the store and the file as they stood."""
    assert answer(working, ANSWER) == (0, "")
    held, file = store(working), case_path(working, "7").read_text(encoding="utf-8")
    path = transcript(working, [text(ANSWER)], *[[text(output)] for output in later])
    return answer(working, "", now=LATER, agent_transcript_path=path), held, file


def test_subagent_a_case_then_a_round_its_recommend_lacks_leaves_the_case_as_it_stood(working):
    outcome, held, file = built_then(working, round_of("Which page?"))
    assert outcome == (0, "")
    assert store(working) == held
    assert case_path(working, "7").read_text(encoding="utf-8") == file


def test_subagent_a_case_then_a_fact_answer_leaves_the_case_as_it_stood(working):
    outcome, held, file = built_then(working, "**Fact:** The page says so.")
    assert outcome == (0, "")
    assert store(working) == held
    assert case_path(working, "7").read_text(encoding="utf-8") == file


def test_subagent_round_form_a_case_then_a_faulty_round_sends_back_its_form_alone(working):
    faulty = round_of("Which page?").replace("**Which page?**:", "**Which page?**")
    (code, err), held, _ = built_then(working, faulty)
    assert code == 2 and "the title line" in err and "answer with the round whole again" in err
    assert "case 7" not in err
    assert store(working) == held


def test_subagent_is_fact_and_is_round_share_one_test_of_a_fact():
    assert casecheck.is_fact("**Fact:** It says so.\n\n❓ **Q1** - **Which?**:\n")
    assert casecheck.is_fact("  **Fact:** indented by a hand-back.")
    assert not casecheck.is_fact("❓ **Q1** - **Which?**:\n\n**Fact:** after the question.")
    assert not casecheck.is_fact(ANSWER.replace("> Context.", "> **Fact:** in a Case."))
    assert not casecheck.is_round("**Fact:** It says so.\n\n❓ **Q1** - **Which?**:\n")
    assert casecheck.is_round("❓ **Q1** - **Which?**:\n\n**Fact:** after the question.")


# --- a ratified Case built again in another shape (case 610.1) -----------------------------


def ledger(project, *lines):
    """The session's ledger with these decision lines."""
    folder = project.joinpath(*FOLDER)
    folder.mkdir(parents=True, exist_ok=True)
    body = "".join(f"- 15:10:00 {line}\n" for line in lines)
    (folder / "ledger.md").write_text(body, encoding="utf-8")


CASE_9 = ANSWER.replace("## Case 7 — example", "## Case 9 — example").replace("case 7", "case 9")
FAMILY_9 = PARENT + sub_case("9.1") + "\n" + sub_case("9.2", "The page is read.")
LINES_9 = (
    "decision[case 9.1][update][rule-x]{ref:rule-x}",
    "decision[case 9.2][update][rule-x]{ref:rule-x}",
)


def test_subagent_shape_a_case_ratified_whole_back_with_sub_cases_is_sent_back(working):
    ledger(working, "decision[case 9][update][rule-x]{ref:rule-x}")
    code, err = answer(working, FAMILY_9)
    assert code == 2
    assert (
        "case 9: case 9 has decision lines in the session's ledger and comes back in another "
        "shape under its old number — build it again as case 10, its decision lines carrying "
        "{supersedes:case 9}"
    ) in err
    assert not case_path(working, "9").exists()


def test_subagent_shape_a_case_ratified_with_sub_cases_back_whole_marks_its_parent(working):
    ledger(working, *LINES_9)
    code, err = answer(working, CASE_9)
    assert code == 2
    assert "case 9: case 9.1, 9.2 has decision lines" in err
    assert "{supersedes:case 9}{supersedes:case 9.1}{supersedes:case 9.2}" in err


def test_subagent_shape_a_whole_answer_without_a_ratified_sub_case_is_sent_back(working):
    ledger(working, *LINES_9)
    code, err = answer(working, PARENT + sub_case("9.1"))
    assert code == 2 and "case 9: case 9.2 has decision lines" in err


def test_subagent_shape_the_new_number_counts_the_keys_of_the_store(working):
    case_12 = ANSWER.replace("## Case 7", "## Case 12").replace("case 7", "case 12")
    assert answer(working, case_12) == (0, "")
    ledger(working, "decision[case 9][update][rule-x]{ref:rule-x}")
    code, err = answer(working, FAMILY_9)
    assert code == 2 and "build it again as case 13" in err


@pytest.mark.parametrize(
    ("lines", "text"),
    [
        (LINES_9, sub_case("9.1")),  # a sub-case answered alone
        (("decision[case 7][update][rule-x]{ref:rule-x}",), ANSWER),  # the same shape
        (LINES_9, FAMILY_9),  # the same shape, with sub-cases
        (("decision[case 9][defer][rule-y]",), FAMILY_9),  # only a defer line
    ],
)
def test_subagent_shape_an_answer_in_its_shape_passes(working, lines, text):
    ledger(working, *lines)
    assert answer(working, text) == (0, "")


# --- a number another agent holds (case 610.2) ---------------------------------------------


def test_subagent_clash_a_number_another_agent_holds_is_sent_back_and_stored_apart(working):
    assert answer(working, ANSWER, agent_id="a1") == (0, "")
    file = case_path(working, "7").read_text(encoding="utf-8")
    other = ANSWER.replace("The file is written.", "Another file is written.")
    code, err = answer(working, other, now=LATER, agent_id="b2")
    assert code == 2
    assert (
        "case 7: the store holds case 7 from the answer of another agent — build this Case "
        "as case 8"
    ) in err
    held = store(working)
    assert held["7"]["agent_id"] == "a1" and held["7"]["stored"] == NOW.isoformat()
    assert held["7@b2"]["agent_id"] == "b2" and "Another file" in held["7@b2"]["text"]
    assert case_path(working, "7").read_text(encoding="utf-8") == file
    assert casecheck.against_store("7", "", [], held) is None  # the reading by the number
    assert answer(working, other, now=LATER, agent_id="b2") == (0, "")


def test_subagent_clash_a_sub_case_another_agent_holds_is_sent_back(working):
    assert answer(working, FAMILY_9, agent_id="a1") == (0, "")
    code, err = answer(working, sub_case("9.1", "Changed."), agent_id="b2")
    assert code == 2 and "the store holds case 9 from the answer of another agent" in err
    assert "Changed." in store(working)["9.1@b2"]["text"]


def test_subagent_clash_no_agent_id_and_the_same_agent_give_no_finding(working):
    assert answer(working, ANSWER) == (0, "")
    assert answer(working, ANSWER, agent_id="b2") == (0, "")
    assert store(working)["7"]["agent_id"] == "b2"
    assert answer(working, ANSWER, agent_id="b2") == (0, "")
    assert list(store(working)) == ["7"]


# --- no problem in a sub-case (case 544.4) --------------------------------------------------


def test_subagent_a_sub_case_with_problem_is_sent_back(working):
    own = sub_case("9.1").replace(
        "### Case 9.1 — part\n\n", "### Case 9.1 — part\n\n> **problem:**\n> Sub P.\n\n"
    )
    code, err = answer(working, PARENT + own)
    assert code == 2
    assert "case 9.1: a sub-case carries problem, which stands on its parent only" in err


def test_subagent_a_parent_without_problem_still_misses_it(working):
    bare = PARENT.replace("> **problem:**\n> P.\n\n", "")
    code, err = answer(working, bare + sub_case("9.1"))
    assert code == 2 and "case 9: missing section problem" in err
    assert "carries problem" not in err


def test_subagent_a_case_with_no_sub_cases_keeps_its_problem(working):
    assert answer(working, ANSWER) == (0, "")


# --- the language finding of /pre-spec on the answer (case 537) --------------------------


@pytest.mark.parametrize(
    "old, new, part",
    [
        ("## Case 7 — example", "## Case 7 — пример", "name"),
        ("> Context.", "> Контекст.", "context"),
        ("> Problem.", "> Проблема.", "problem"),
    ],
)
def test_subagent_script_a_letter_outside_the_script_is_a_finding_with_no_file(
    working, old, new, part
):
    russian = ANSWER.replace(old, new)
    code, err = answer(working, russian)
    assert code == 2
    assert f"case 7: its {part} holds a letter outside the Latin script of English" in err
    assert store(working)["7"]["findings"]
    assert not case_path(working, "7").exists()
    assert answer(working, russian) == (0, "")  # the same answer again: stored, not sent back
    assert store(working)["7"]["findings"]
    assert not case_path(working, "7").exists()


def test_subagent_script_an_english_answer_passes(working):
    assert answer(working, ANSWER) == (0, "")
    assert store(working)["7"]["findings"] == []
    assert case_path(working, "7").exists()


def test_subagent_script_a_russian_quotation_in_then_passes(working):
    quoted = ANSWER.replace("> The file is written.", "> The file is written: «файл записан».")
    assert answer(working, quoted) == (0, "")
    assert store(working)["7"]["findings"] == []


def test_subagent_script_a_latin_code_span_passes_under_russian(working):
    # case 589.2: a slug in a code span is Latin in any language
    (working / "guppi.toml").write_text(
        'documentation_lang = "ru"\nchat_lang = "ru"\n', encoding="utf-8"
    )
    russian = (
        ANSWER.replace("## Case 7 — example", "## Case 7 — пример")
        .replace("> Context.", "> Правило `rule-x` и файл `guppi/x.py`.")
        .replace("> Problem.", "> Проблема `rule-x`.")
    )
    assert answer(working, russian) == (0, "")
    assert store(working)["7"]["findings"] == []
    assert case_path(working, "7").exists()


def test_subagent_script_a_cyrillic_code_span_is_a_finding(working):
    # case 589.2: inside a code span a letter of another script is judged as in prose
    quoted = ANSWER.replace("> Context.", "> Context of `файл`.")
    code, err = answer(working, quoted)
    assert code == 2
    assert "case 7: its context holds a letter outside the Latin script of English" in err
    assert not case_path(working, "7").exists()


def test_subagent_script_a_missing_guppi_toml_is_one_finding(working):
    (working / "guppi.toml").unlink()
    code, err = answer(working, ANSWER)
    assert code == 2
    assert "guppi.toml: missing" in err
    assert store(working)["7"]["findings"] == [
        "guppi.toml: missing — the language of the repository is not known; no Case is read"
    ]


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
        ANSWER.replace("## Case 7 — example", "## Case 7 — an example")
        .replace("> Context.", "> The context.\n> Two lines of it.")
        .replace("> Problem.", "> The problem.")
        .replace("> Advice.", "> The advice.")
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
    "## Case 7 — example\n\nМеняет правило x: одна пара `replace` и новое Estimate.\n\n"
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


def refusal():
    """A `Stop` hook's refusal in the shape Claude Code writes it: a `user` record marked
    `isMeta`, its text opening with `Stop hook feedback:` (transcripts of sessions 1237 and
    1441, case 584)."""
    return {
        "type": "user",
        "isSidechain": False,
        "isMeta": True,
        "message": {"role": "user", "content": "Stop hook feedback:\n[uv run guppi x]: refused"},
    }


def test_stop_a_sending_before_a_refusal_counts_in_the_turn_of_the_reply(working):
    # 584: the refusal opens no turn, so the file sent before it counts for the next showing
    answer(working, ANSWER)
    records = [prompt(), sending(case_path(working, "7")), result(), refusal()]
    assert show(working, SHORT_SHOWING, records=records) == (0, "")


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
    again = ANSWER.replace("> **recommend:**\n> Advice.\n\n", "")
    code, err = show(working, again)
    assert code == 2 and "not built and checked" in err
    answer(working, again)
    assert show(working, again) == (0, "")


def test_stop_a_parent_is_compared_part_by_part(working):
    parent = "## Case 9 — parent\n\n> **context:**\n> C.\n\n> **problem:**\n> P.\n\n> **recommend:**\n> A.\n\n"
    sub = ANSWER.replace("## Case 7 — example", "### Case 9.1 — part").replace("case 7", "case 9.1")
    sub = sub.replace(
        "> **context:**\n> Context.\n\n> **problem:**\n> Problem.\n\n> **recommend:**\n> Advice.\n\n",
        "",
    )
    assert answer(working, parent + sub) == (0, "")
    assert set(store(working)) == {"9", "9.1"}
    assert show(working, parent + sub) == (0, "")
    assert show(working, parent.replace("C.", "C!") + sub) == (0, "")  # prose, not compared
    code, err = show(working, parent + sub.replace("The file is written.", "Written twice."))
    assert code == 2 and "case 9.1: its then differ" in err


def test_stop_the_re_fire_passes(working):
    assert show(working, ANSWER, stop_hook_active=True) == (0, "")


# --- a list showing under the heading of a top-level Case (case 561.10) -----------------

LINES_9_1 = (
    "- decision[case 9.1][update][rule-x]{ref:rule-x}",
    "- decision[case 9.1][create][estimate-x-works-1]{ref:rule-x}{tags:harness}",
)
LINES_9_2 = (
    "- decision[case 9.2][update][rule-x]{ref:rule-x}",
    "- decision[case 9.2][create][estimate-x-works-2]{ref:rule-x}{tags:harness}",
)


def list_showing(*lines):
    fence = "".join(f"> {line}\n" for line in lines)
    return (
        "## Case 9 — родитель\n\n- 9.1 — часть: готово, когда файл записан.\n"
        "- 9.2 — часть: готово, когда страница прочитана.\n\n"
        f"> **ratification:**\n> ```\n{fence}> ```\n\n---\n\nРатифицируешь?\n"
    )


def built_family(working):
    family = PARENT + sub_case("9.1") + "\n" + sub_case("9.2", "The page is read.")
    assert answer(working, family) == (0, "")


def test_stop_list_a_fence_with_the_stored_lines_of_two_sub_cases_passes(working):
    built_family(working)
    assert show(working, list_showing(*LINES_9_1, *LINES_9_2)) == (0, "")


def test_stop_list_a_missing_line_is_refused(working):
    built_family(working)
    code, err = show(working, list_showing(*LINES_9_1, LINES_9_2[0]))
    assert code == 2 and "case 9.2: its ratification differ" in err


def test_stop_list_an_extra_line_is_refused(working):
    built_family(working)
    extra = "- decision[case 9.1][update][rule-y]{ref:rule-y}"
    code, err = show(working, list_showing(*LINES_9_1, extra, *LINES_9_2))
    assert code == 2 and "case 9.1: its ratification differ" in err


def test_stop_list_a_showing_under_each_heading_passes_as_before(working):
    built_family(working)
    each = PARENT + sub_case("9.1") + "\n" + sub_case("9.2", "The page is read.")
    assert show(working, each) == (0, "")


# --- how a round of case-guppi opens (case 562) -----------------------------------------

ROUND = (
    "**Context:** The item is about X.\n\n❓ **Q1** - **Which way?**:\n\n**Now:** A.\n\n➡️ (a).\n"
)
SHOWN_ROUND = "**Контекст:** Пункт об X.\n\n❓ **Q1** - **Какой путь?**:\n\n➡️ (a).\n"
FACT_ANSWER = "**Fact:** The page says so.\n\n❓ **Q1** - **Which way?**:\n"
PRESPEC_MARK = "- 15:20:00 44c1aae1 prespec\n"


def assistant(*blocks):
    return {
        "type": "assistant",
        "isSidechain": False,
        "message": {"role": "assistant", "content": list(blocks)},
    }


def said(value):
    return {"type": "text", "text": value}


def agent_call(call_id="toolu_a"):
    return {
        "type": "tool_use",
        "id": call_id,
        "name": "Agent",
        "input": {"subagent_type": "case-guppi"},
    }


def agent_result(value, call_id="toolu_a"):
    block = {
        "type": "tool_result",
        "tool_use_id": call_id,
        "content": [said("  " + value.replace("\n", "\n  "))],
    }
    return {"type": "user", "isSidechain": False, "message": {"role": "user", "content": [block]}}


def notification(value):
    content = f"<task-notification>\n<task-id>a1</task-id>\n<result>{value}</result>\n</task-notification>"
    return {
        "type": "user",
        "isSidechain": False,
        "origin": {"kind": "task-notification"},
        "message": {"role": "user", "content": content},
    }


def with_prespec(working):
    log = working / "vault" / "raw" / TODAY.isoformat() / "event_log.md"
    log.write_text(log.read_text(encoding="utf-8") + PRESPEC_MARK, encoding="utf-8")


def test_round_a_reply_that_opens_with_a_line_of_its_own_is_refused(working):
    records = [prompt(), assistant(agent_call()), agent_result(ROUND)]
    code, err = show(working, "Case-guppi asks a round.\n\n" + SHOWN_ROUND, records=records)
    assert code == 2 and "Case-guppi asks a round." in err and "nothing before it" in err


def test_round_before_prespec_a_text_before_the_agent_call_is_refused(working):
    records = [
        prompt(),
        assistant(said("Dispatching case-guppi."), agent_call()),
        agent_result(ROUND),
    ]
    code, err = show(working, SHOWN_ROUND, records=records)
    assert code == 2 and "Dispatching case-guppi." in err


def test_round_after_prespec_a_text_before_the_call_with_a_question_line_passes(working):
    with_prespec(working)
    send = {"type": "tool_use", "id": "toolu_s", "name": "SendMessage", "input": {}}
    records = [notification(ROUND), assistant(said("The report."), send), result()]
    assert show(working, "❓ **561.Q1** - **Какой путь?**:\n", records=records) == (0, "")


def test_round_after_prespec_a_reply_that_opens_with_a_line_of_its_own_is_refused(working):
    with_prespec(working)
    code, err = show(working, "Both answered.\n\n" + SHOWN_ROUND, records=[notification(ROUND)])
    assert code == 2 and "Both answered." in err


def test_round_a_reply_that_opens_with_the_context_label_or_the_question_passes(working):
    records = [prompt(), assistant(agent_call()), agent_result(ROUND)]
    assert show(working, SHOWN_ROUND, records=records) == (0, "")
    question = SHOWN_ROUND[SHOWN_ROUND.index("❓") :]
    assert show(working, question, records=records) == (0, "")


@pytest.mark.parametrize(
    "records",
    [
        [prompt(), assistant(agent_call()), agent_result(FACT_ANSWER)],
        [prompt()],
        [prompt(), assistant(said("A note."), agent_call()), agent_result(ANSWER)],
    ],
)
def test_round_a_turn_with_no_round_is_not_judged(working, records):
    own_question = "Мой вопрос.\n\n❓ **Q1** - **Мой?**:\n"
    assert show(working, own_question, records=records, sent=[]) == (0, "")


def test_round_a_record_with_no_origin_opens_no_turn(working):
    # case 590.3: the record of a local command — string content, no `origin`, no `isMeta` —
    # does not cut the turn, so a round given back before it is still judged
    clear = {
        "type": "user",
        "isSidechain": False,
        "message": {"role": "user", "content": "<command-name>/clear</command-name>"},
    }
    records = [prompt(), assistant(agent_call()), agent_result(ROUND), clear]
    code, err = show(working, "A line of my own.\n\n" + SHOWN_ROUND, records=records)
    assert code == 2 and "A line of my own." in err


def test_round_a_round_whose_title_line_lacks_its_colon_is_a_round(working):
    # case 601.4: the Stop run knows a round by `is_round`, the mark alone, not QUESTION_LINE
    no_colon = ROUND.replace("**Which way?**:", "**Which way?**")
    records = [prompt(), assistant(agent_call()), agent_result(no_colon)]
    code, err = show(working, "A line of my own.\n\n" + SHOWN_ROUND, records=records)
    assert code == 2 and "A line of my own." in err


def test_round_the_re_fire_passes(working):
    records = [prompt(), assistant(agent_call()), agent_result(ROUND)]
    reply = "A line.\n\n" + SHOWN_ROUND
    assert show(working, reply, records=records, stop_hook_active=True) == (0, "")


def test_stop_list_the_file_of_the_top_level_case_must_be_sent(working):
    built_family(working)
    code, err = show(working, list_showing(*LINES_9_1, *LINES_9_2), sent=[])
    assert code == 2 and "no SendUserFile call on" in err


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
    assert answer(working, PARENT + first + "\n" + sub_case("9.2", "The page is read.")) == (0, "")


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


# --- the notes of the promise lines (cases 472.1, 472.2) -------------------------------

RECUT = """## Case 7 — recut

> **context:**
> Context.

> **problem:**
> Problem.

> **given:**
> `estimate-x-works` — its Estimate.

> **when:**
> The agent runs `guppi x`.

> **then:**
> The file is written.

> **tasks:**
> - [ ] update `estimate-x-works`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole (case 7)`
> - [ ] read `estimate-x-works`

> **ratification:**
> ```
> - decision[case 7][update][estimate-x-works]{ref:estimate-x-works}
> ```
"""

ESTIMATE_X = """---
type: estimate
kind: QA
status: passed
target: rule-x
method: by hand
---

## Criterion

When:
The agent runs `guppi x`.

Then:
The file is written.
**＋** The log is kept.
"""

DROPPED = "note: case 7: estimate-x-works: a line of its Criterion is not carried: The log is kept."


@pytest.fixture
def recut(working):
    page = working / "vault" / "wiki" / "estimates" / "estimate-x-works.md"
    page.parent.mkdir(parents=True)
    page.write_text(ESTIMATE_X, encoding="utf-8")
    return working


def test_subagent_note_a_dropped_criterion_line_is_sent_back_once_and_kept(recut):
    code, err = answer(recut, RECUT)
    assert code == 2 and DROPPED in err
    assert store(recut)["7"]["findings"] == [] and store(recut)["7"]["notes"] == [DROPPED]
    assert case_path(recut, "7").exists()  # a note is no finding: the file is written
    assert answer(recut, RECUT) == (0, "")
    assert answer(recut, RECUT.replace("> Context.", "> Context 2.")) == (0, "")
    assert store(recut)["7"]["notes"] == [DROPPED]  # a later answer keeps the notes sent


def test_stop_a_case_with_a_note_is_not_refused(recut):
    answer(recut, RECUT)
    assert show(recut, RECUT + "\n---\n\nRatify?\n") == (0, "")


SAME_PROMISE = (
    "The check sends each note back to the agent once.",
    "Each note goes back to the agent once, sent by the check.",
)


def test_subagent_note_siblings_that_share_a_promise_are_sent_back_once(working):
    text = PARENT + sub_case("9.1", SAME_PROMISE[0]) + "\n" + sub_case("9.2", SAME_PROMISE[1])
    code, err = answer(working, text)
    assert code == 2 and "note: case 9.2: a then line shares most of its words with case 9.1" in err
    assert answer(working, text) == (0, "")


def test_subagent_note_a_sub_case_answered_alone_has_no_sibling(working):
    assert answer(working, sub_case("9.2", SAME_PROMISE[1])) == (0, "")


# --- the hook's own error (case 555.1) -------------------------------------------------


def boom(*args, **kwargs):
    raise RuntimeError("boom")


def test_error_an_error_of_the_stop_run_exits_2_with_the_advice(working, monkeypatch):
    answer(working, ANSWER)
    monkeypatch.setattr(casecheck, "against_store", boom)
    code, err = show(working, ANSWER)
    assert code == 2
    assert err.startswith("casecheck: not checked: boom")
    assert "show the Case again" in err


def test_error_the_re_fire_exits_0(working, monkeypatch):
    answer(working, ANSWER)
    monkeypatch.setattr(casecheck, "against_store", boom)
    assert show(working, ANSWER, stop_hook_active=True) == (0, "")


def test_error_an_empty_payload_exits_0_with_its_line(working):
    err = io.StringIO()
    code = casecheck.run([], stdin=io.StringIO(""), stderr=err, project_dir=working, now=NOW)
    assert code == 0 and err.getvalue() == "casecheck: payload not readable, nothing checked\n"


def test_error_an_error_of_the_subagent_run_exits_0_with_its_line(working, monkeypatch):
    monkeypatch.setattr(casecheck, "check_answer", boom)
    assert answer(working, ANSWER) == (0, "casecheck: not checked: boom\n")
