#!/usr/bin/env python3
"""Cases for `session-dialogue.py` -- the fence reader and the refusals.

Why this file exists rather than a note saying the script was tried once: every rule in
`wiki/rules/` owes a mechanical instrument, and the rule this whole mechanism serves is one
of the six that had none. The instrument is not the hook alone -- it is the pair, the hook
and the reader that proves the hook's input can be recognised.

Run: uv run python scripts/session-dialogue-selftest.py
"""

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover
        pass

HERE = Path(__file__).resolve().parent
TARGET = HERE / "session-dialogue.py"

spec = importlib.util.spec_from_file_location("session_dialogue", TARGET)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

CAUGHT = 0
MISSED = 0


def case(name: str, got, want) -> None:
    global CAUGHT, MISSED
    if got == want:
        CAUGHT += 1
        print(f"  ok    {name}")
    else:
        MISSED += 1
        print(f"  MISSED {name}\n        got  {got!r}\n        want {want!r}")


F = "```"
FF = "````"

# A NEWLINE WITH A NAME. Six times in the session that wrote this file, a tool ate what was
# written to it - and once it was a `\\n` in a patch script that reached this very file as a
# real line break inside a string literal. A named constant cannot be eaten by one more layer
# of quoting, which is the only defence that keeps working however the content is delivered.
NL = chr(10)


# --- the fence reader -------------------------------------------------------------------
# Each body is built from F rather than written literally, so this file can describe the
# marker without the reader of THIS file mistaking the description for a record.

case(
    "a plain block is read, and its kind is the first word",
    module.feedback_blocks(f"before\n{F}VAULT-FEEDBACK\nmiss: the vault said X\n{F}\nafter"),
    [("miss", "miss: the vault said X")],
)

case(
    "a block spanning several lines arrives whole",
    module.feedback_blocks(f"{F}VAULT-FEEDBACK\nmeasure: one\ntwo\nthree\n{F}"),
    [("measure", "measure: one\ntwo\nthree")],
)

case(
    "two blocks in one message are both read",
    module.feedback_blocks(f"{F}VAULT-FEEDBACK\nmiss: a\n{F}\ntext\n{F}VAULT-FEEDBACK\nharness: b\n{F}"),
    [("miss", "miss: a"), ("harness", "harness: b")],
)

case(
    "a VAULT-FEEDBACK fence nested inside another fence is an example, not a record",
    module.feedback_blocks(f"{FF}\n{F}VAULT-FEEDBACK\nmiss: this is documentation\n{F}\n{FF}"),
    [],
)

case(
    "an ordinary code block files nothing",
    module.feedback_blocks(f"{F}bash\necho hello\n{F}"),
    [],
)

case(
    "a block with no colon on its first line is kept and marked unknown",
    module.feedback_blocks(f"{F}VAULT-FEEDBACK\nsomething with no kind\n{F}"),
    [("unknown", "something with no kind")],
)

case(
    "an unknown kind is kept as written rather than discarded",
    module.feedback_blocks(f"{F}VAULT-FEEDBACK\nbanana: not one of the four\n{F}"),
    [("banana", "banana: not one of the four")],
)

case("a message with no fence at all files nothing", module.feedback_blocks("just prose"), [])


# --- who actually spoke -----------------------------------------------------------------
# The first real use of this script filed a background-task notification and the body of an
# invoked skill under the owner's name. A retro reads this file to decide what he ruled, so a
# line wrongly attributed to him here is a page tomorrow - the exact defect that once put 53
# owner-attributed blocks across 44 pages, one of them working as a rule for three days.

case(
    "a turn he typed is his",
    module.classify_user({"origin": {"kind": "human"}}, "hello"),
    "owner",
)

case(
    "a background-task notification is NOT his",
    module.classify_user({"origin": {"kind": "task-notification"}}, "<task-notification>done"),
    "system (task-notification)",
)

case(
    "the body of an invoked skill is NOT his",
    module.classify_user({"isMeta": True}, "Base directory for this skill: ..."),
    "system (skill body)",
)

# HIS, AND THE ONE THAT LOOKS LIKE THE OTHERS. An interrupt marker carries no origin at all,
# but pressing stop is something only he can do, and it is often the sharpest signal in a
# session: it marks where he refused what was about to happen.
case(
    "an interrupt marker IS his, though it carries no origin",
    module.classify_user({}, "[Request interrupted by user for tool use]"),
    "owner",
)

case(
    "an unattributed user block is not promoted to his",
    module.classify_user({}, "who wrote this?"),
    "system (unattributed)",
)

case(
    "an origin of some kind nobody has seen yet is still not his",
    module.classify_user({"origin": {"kind": "something-new"}}, "..."),
    "system (something-new)",
)


# --- the four states of a menu ----------------------------------------------------------
# The count used to be two: a menu with a result was answered, everything else was lost. That
# arithmetic files the owner's DOCUMENTED PREFERENCE as a defect - he interrupts a menu and
# answers in prose - and it merges a menu still open with one the session walked away from,
# which are the two states that want opposite responses. Widened to four on 2026-08-25 on his
# approval; the decision page carries the amendment.


def menu(result: bool = False, answer=None) -> dict:
    return {"kind": "menu", "questions": [], "answer": answer, "result": result}


def states(entries: list[dict]) -> tuple[list[str], dict]:
    """Run the resolver over a hand-built entry list. Returns the menu states and the counts."""
    counts = {"answers": 0, "prose": 0, "open": 0, "lost": 0}
    module.resolve_menus(entries, counts)
    return [e["state"] for e in entries if e["kind"] == "menu"], counts


case(
    "a menu with a result is answered by selection",
    states([menu(result=True, answer="chose this")]),
    (["selected"], {"answers": 1, "prose": 0, "open": 0, "lost": 0}),
)

# THE PRESENCE OF THE RESULT DECIDES, NOT ITS TEXT. Reading `answer` for this would file a
# selection that renders to an empty string as an answer that never came.
case(
    "a selection carrying no text is still a selection",
    states([menu(result=True, answer="")]),
    (["selected"], {"answers": 1, "prose": 0, "open": 0, "lost": 0}),
)

case(
    "a menu he interrupted and answered in prose is answered, not lost",
    states([menu(), {"kind": "owner", "text": "no, do it the other way"}]),
    (["prose"], {"answers": 0, "prose": 1, "open": 0, "lost": 0}),
)

case(
    "a menu with nothing after it is still open, not lost",
    states([menu()]),
    (["open"], {"answers": 0, "prose": 0, "open": 1, "lost": 0}),
)

case(
    "a menu the session carried on past is lost",
    states([menu(), {"kind": "session", "text": "carrying on"}]),
    (["lost"], {"answers": 0, "prose": 0, "open": 0, "lost": 1}),
)

# A NOTIFICATION IS NOT A TURN. Letting the first following entry decide without stepping over
# system blocks would file his answer as lost whenever a background job finished first - and
# this session runs dispatches in the background as a matter of course.
case(
    "a notification between the menu and his answer does not make it lost",
    states([menu(), {"kind": "system", "who": "system (task-notification)", "text": "done"},
            {"kind": "owner", "text": "the second one"}]),
    (["prose"], {"answers": 0, "prose": 1, "open": 0, "lost": 0}),
)

case(
    "a menu followed by nothing but notifications is open rather than lost",
    states([menu(), {"kind": "system", "who": "system (skill body)", "text": "..."}]),
    (["open"], {"answers": 0, "prose": 0, "open": 1, "lost": 0}),
)

# THE INTERRUPT MARKER IS HIS, and it reaches the resolver as an ordinary owner entry, so a menu
# he stopped reads as answered. Pressing stop is an answer to the menu - a refusal of it. Pinned
# here because it is the one state assignment that is a judgement rather than a reading.
case(
    "a menu he stopped and said nothing further about reads as prose",
    states([menu(), {"kind": "owner", "text": "[Request interrupted by user for tool use]"}]),
    (["prose"], {"answers": 0, "prose": 1, "open": 0, "lost": 0}),
)

case(
    "two menus in one session are resolved independently",
    states([menu(result=True, answer="a"), {"kind": "session", "text": "reply"},
            menu(), {"kind": "session", "text": "carrying on"}]),
    (["selected", "lost"], {"answers": 1, "prose": 0, "open": 0, "lost": 1}),
)


# --- the refusals -----------------------------------------------------------------------

def run(*args) -> subprocess.CompletedProcess:
    # `check=False`: a case asserts the exit code the target returned, so raising on a non-zero one
    # would turn every refusal case into an error before it could be checked.
    return subprocess.run(
        [sys.executable, str(TARGET), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


case("an unknown session id exits 2", run("no-such-session-id-at-all").returncode, 2)
case("a path that is not a file exits 2", run("./no/such/file.jsonl").returncode, 2)

with tempfile.TemporaryDirectory() as tmp:
    empty = Path(tmp) / "empty.jsonl"
    empty.write_text("", encoding="utf-8")
    result = run(str(empty))
    case("a transcript with no owner turn exits 2", result.returncode, 2)
    case(
        "and it says WHY rather than writing an empty file quietly",
        "no owner turns found" in result.stderr,
        True,
    )

    # `origin` IS NOT DECORATION IN THESE FIXTURES. Without it the block is classified as
    # unattributed rather than his, so this case and the two below it would exit 2 for the wrong
    # reason - reporting "no owner turns" while claiming to test "no session reply". They did
    # exactly that for one run, which is why the field is written here rather than left out.
    only_owner = Path(tmp) / "only-owner.jsonl"
    only_owner.write_text(
        json.dumps(
            {
                "type": "user",
                "isSidechain": False,
                "origin": {"kind": "human"},
                "message": {"role": "user", "content": [{"type": "text", "text": "hello"}]},
            }
        )
        + NL,
        encoding="utf-8",
    )
    result = run(str(only_owner))
    case("a transcript with no session reply exits 2", result.returncode, 2)
    case("and it says WHICH half was missing", "no session replies" in result.stderr, True)

    sidechain = Path(tmp) / "sidechain.jsonl"
    sidechain.write_text(
        "\n".join(
            json.dumps(record)
            for record in (
                {
                    "type": "user",
                    "isSidechain": True,
                    "message": {"role": "user", "content": [{"type": "text", "text": "subagent"}]},
                },
                {
                    "type": "assistant",
                    "isSidechain": True,
                    "message": {"role": "assistant", "content": [{"type": "text", "text": "sub"}]},
                },
            )
        )
        + "\n",
        encoding="utf-8",
    )
    case("a transcript of nothing but subagent turns exits 2", run(str(sidechain)).returncode, 2)

    good = Path(tmp) / "good.jsonl"
    good.write_text(
        "\n".join(
            json.dumps(record)
            for record in (
                {
                    "type": "user",
                    "isSidechain": False,
                    "origin": {"kind": "human"},
                    "message": {"role": "user", "content": [{"type": "text", "text": "a question"}]},
                },
                {
                    "type": "assistant",
                    "isSidechain": False,
                    "message": {
                        "role": "assistant",
                        "content": [
                            {"type": "text", "text": f"{F}VAULT-FEEDBACK\nmiss: something\n{F}"},
                            {
                                "type": "tool_use",
                                "id": "t1",
                                "name": "AskUserQuestion",
                                "input": {
                                    "questions": [
                                        {"question": "which?", "options": [{"label": "this"}]}
                                    ]
                                },
                            },
                        ],
                    },
                },
                {
                    "type": "user",
                    "isSidechain": False,
                    "message": {
                        "role": "user",
                        "content": [
                            {"type": "tool_result", "tool_use_id": "t1", "content": "chose this"}
                        ],
                    },
                },
            )
        )
        + "\n",
        encoding="utf-8",
    )
    # END TO END, because the classifier being right in isolation is not the claim. The claim is
    # that a transcript carrying a notification reports ONE owner turn and not two.
    mixed = Path(tmp) / "mixed.jsonl"
    mixed.write_text(
        NL.join(
            json.dumps(record)
            for record in (
                {
                    "type": "user",
                    "isSidechain": False,
                    "origin": {"kind": "human"},
                    "message": {"role": "user", "content": [{"type": "text", "text": "his turn"}]},
                },
                {
                    "type": "user",
                    "isSidechain": False,
                    "origin": {"kind": "task-notification"},
                    "message": {"role": "user", "content": "a background job finished"},
                },
                {
                    "type": "user",
                    "isSidechain": False,
                    "isMeta": True,
                    "message": {"role": "user", "content": [{"type": "text", "text": "skill body"}]},
                },
                {
                    "type": "assistant",
                    "isSidechain": False,
                    "message": {"role": "assistant", "content": [{"type": "text", "text": "reply"}]},
                },
            )
        )
        + NL,
        encoding="utf-8",
    )
    result = run(str(mixed))
    case("a notification and a skill body are not counted as owner turns",
         "owner turns      : 1" in result.stdout, True)
    case("and they are counted as system blocks instead",
         "system blocks    : 2" in result.stdout, True)
    mixedout = module.SDD / f"session-dialogue-{mixed.stem[:8]}.md"
    mixedbody = mixedout.read_text(encoding="utf-8")
    case("the notification is labelled NOT the owner in the file",
         "system (task-notification) - NOT the owner" in mixedbody, True)
    # THE HEADING, NOT THE WORD. A first draft of this case asserted that
    # `owner\\n\\na background job finished` was absent - and it is present, inside the heading
    # `system (task-notification) - NOT the owner`. A case can pass or fail for a reason that has
    # nothing to do with its name; this one nearly failed for one.
    case("and nothing of it is filed under his heading",
         (". owner" + NL + NL + "a background job finished") not in mixedbody, True)
    mixedout.unlink()

    result = run(str(good))
    case("a well-formed transcript exits 0", result.returncode, 0)
    case("its owner turn is counted", "owner turns      : 1" in result.stdout, True)
    case("its menu is counted with its answer", "menus answered   : 1" in result.stdout, True)
    case("its feedback mark is counted", "feedback marks   : 1" in result.stdout, True)

    written = module.SDD / f"session-dialogue-{good.stem[:8]}.md"
    body = written.read_text(encoding="utf-8")
    case("the menu answer reaches the file", "chose this" in body, True)
    case("the option label reaches the file", "- this" in body, True)
    case("the mark reaches the attention list", "miss: something" in body, True)
    written.unlink()

    # END TO END FOR THE TWO STATES THE OLD ARITHMETIC MERGED, because the resolver being right
    # in isolation is not the claim. The claim is that a real transcript of the shape he
    # actually produces stops reporting a lost menu.
    def transcript(name: str, *records) -> Path:
        target = Path(tmp) / name
        target.write_text(NL.join(json.dumps(r) for r in records) + NL, encoding="utf-8")
        return target

    def asked(tool_id: str) -> dict:
        return {
            "type": "assistant",
            "isSidechain": False,
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "type": "tool_use",
                        "id": tool_id,
                        "name": "AskUserQuestion",
                        "input": {"questions": [{"question": "which?",
                                                 "options": [{"label": "this"}]}]},
                    }
                ],
            },
        }

    def said(text: str, origin: str | None = "human") -> dict:
        record = {"type": "user", "isSidechain": False,
                  "message": {"role": "user", "content": [{"type": "text", "text": text}]}}
        if origin:
            record["origin"] = {"kind": origin}
        return record

    def replied(text: str) -> dict:
        return {"type": "assistant", "isSidechain": False,
                "message": {"role": "assistant", "content": [{"type": "text", "text": text}]}}

    interrupted = transcript(
        "interrupted.jsonl",
        said("a question"),
        asked("t1"),
        # HIS, THOUGH IT CARRIES NO ORIGIN - he pressed stop. Written without one on purpose:
        # that is how the marker arrives in a real transcript.
        said("[Request interrupted by user for tool use]", origin=None),
        said("no, do it the other way"),
        replied("understood"),
    )
    result = run(str(interrupted))
    case("an interrupted menu answered in prose exits 0", result.returncode, 0)
    case("and it is counted as answered in prose",
         "answered in prose: 1" in result.stdout, True)
    case("and it is NOT counted as a selection",
         "menus answered   : 0" in result.stdout, True)
    case("and it is NOT counted as lost", "menus lost       : 0" in result.stdout, True)
    case("so no warning fires about it", "WARNING" in result.stdout, False)
    prosebody = (module.SDD / f"session-dialogue-{interrupted.stem[:8]}.md").read_text(
        encoding="utf-8")
    case("and the file says he answered in prose rather than nothing",
         "**Answered in prose.**" in prosebody, True)
    (module.SDD / f"session-dialogue-{interrupted.stem[:8]}.md").unlink()

    walked = transcript(
        "walkedaway.jsonl",
        said("a question"),
        asked("t1"),
        replied("carrying on without an answer"),
    )
    result = run(str(walked))
    case("a menu the session walked away from is counted as lost",
         "menus lost       : 1" in result.stdout, True)
    # THE ONE STATE THAT IS A DEFECT IS THE ONE THAT WARNS. The warning used to fire on all
    # three non-selected states, so its most frequent reading was about a menu he had already
    # answered in his own words.
    case("and THAT is what the warning fires on",
         "menu(s) lost" in result.stdout, True)
    (module.SDD / f"session-dialogue-{walked.stem[:8]}.md").unlink()

    trailing = transcript(
        "stillopen.jsonl",
        said("a question"),
        replied("thinking"),
        asked("t1"),
    )
    result = run(str(trailing))
    case("a menu that is the last thing in the transcript is still open",
         "menus still open : 1" in result.stdout, True)
    case("and a menu still open is not a lost one",
         "menus lost       : 0" in result.stdout, True)
    openbody = (module.SDD / f"session-dialogue-{trailing.stem[:8]}.md").read_text(
        encoding="utf-8")
    case("and the file says so rather than reporting no result",
         "**Still open.**" in openbody, True)
    (module.SDD / f"session-dialogue-{trailing.stem[:8]}.md").unlink()

print(f"\nSESSION-DIALOGUE-SELFTEST: caught {CAUGHT}, missed {MISSED}")
sys.exit(1 if MISSED else 0)
