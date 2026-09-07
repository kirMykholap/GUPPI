#!/usr/bin/env python3
"""Extract one session's dialogue from its Claude Code transcript.

The transcript is written by the harness and nothing in this repository has ever read it:
37 files and 255 MB sat unread on 2026-08-24. Dialogue is 2-4% of a transcript -- the rest
is tool output that has already done its work -- so this script lifts out the part a retro
needs and leaves the rest on disk.

WHAT IT TAKES, AND WHY EACH ONE.
  - the owner's turns and the session's replies, verbatim and in order;
  - every AskUserQuestion together with its answer. This is the half a UserPromptSubmit hook
    can never see: a menu selection is a tool result, not a submitted prompt, and 8 of 10
    rulings in one measured session arrived that way. A menu has FOUR states here, not two:
    the owner's documented preference is to interrupt a menu and answer in prose, and counting
    that as an answer lost sends a retro hunting for a ruling that is sitting in the next turn;
  - every fenced VAULT-FEEDBACK block, listed again at the end as the session's attention list.

WHAT IT CANNOT TAKE. `thinking` blocks are present in the transcript with EMPTY content -- only
an encrypted signature survives. The floor records what was said, never what was reasoned, and
a reader who forgets that will mistake silence for agreement.

OUTPUT lives one session, like `.superpowers/sdd/retro.md`. It is not knowledge until it has
been through an ingest.

Run:
  uv run python scripts/session-dialogue.py                 # this session
  uv run python scripts/session-dialogue.py <path.jsonl>    # a named transcript
  uv run python scripts/session-dialogue.py <session-id>    # a session by its id
"""

import json
import sys
from pathlib import Path

# The host console is cp1252 and this script prints Russian. Reconfiguring stdout is not
# defensive tidiness: the same class -- a tool refusing the bytes it was handed -- produced
# three separate failures in the session that wrote this file, and it has its own page.
for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover - Python < 3.7 has no reconfigure
        pass

REPO = Path(__file__).resolve().parent.parent
SDD = REPO / ".superpowers" / "sdd"
PATH_HINT = SDD / "session-transcript.path"
OUT = SDD / "session-dialogue.md"

INTERRUPT_MARK = "[Request interrupted by user"


def projects_dir() -> Path:
    """Where the harness keeps this project's transcripts.

    The directory name is the working directory with every separator, colon and space
    replaced by a dash: `c:\\PROJECTS\\job hunt ai` becomes `c--PROJECTS-job-hunt-ai`.
    """
    encoded = str(REPO).replace(":", "-").replace("\\", "-").replace("/", "-").replace(" ", "-")
    return Path.home() / ".claude" / "projects" / encoded


def resolve_transcript(argument: str | None) -> Path:
    """Find the transcript, and say out loud which route found it."""
    if argument:
        candidate = Path(argument)
        if candidate.is_file():
            print(f"transcript: named on the command line -- {candidate}")
            return candidate
        by_id = projects_dir() / f"{argument}.jsonl"
        if by_id.is_file():
            print(f"transcript: resolved from a session id -- {by_id}")
            return by_id
        die(f"no transcript at {candidate} and no session {argument} under {projects_dir()}")

    if PATH_HINT.is_file():
        hinted = Path(PATH_HINT.read_text(encoding="utf-8-sig").strip())
        if hinted.is_file():
            print(f"transcript: from {PATH_HINT.name} -- {hinted}")
            return hinted
        print(f"WARNING: {PATH_HINT} names {hinted}, which does not exist. Falling back.")

    directory = projects_dir()
    if not directory.is_dir():
        die(f"no transcript directory at {directory}")
    files = sorted(directory.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        die(f"no .jsonl transcripts under {directory}")
    print(f"transcript: newest under {directory} -- {files[0].name}")
    print("           (a fallback: SessionStart did not leave a path hint)")
    return files[0]


def die(message: str) -> None:
    """Refuse loudly. An extractor that fails towards an empty file is indistinguishable
    from one that was never run, and the corpus has a page saying exactly that."""
    print(f"SESSION-DIALOGUE: {message}", file=sys.stderr)
    sys.exit(2)


def text_of(block: dict) -> str:
    return block.get("text", "") if block.get("type") == "text" else ""


def answer_text(block: dict) -> str:
    content = block.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(text_of(b) for b in content if isinstance(b, dict)).strip()
    return json.dumps(content, ensure_ascii=False) if content is not None else ""


def feedback_blocks(text: str) -> list[tuple[str, str]]:
    """Fenced VAULT-FEEDBACK blocks at the top level of a message.

    Depth is counted rather than judged: a VAULT-FEEDBACK fence opens a record only when no
    other fence is open, which is how this rule can be written about without filing a line.
    """
    found: list[tuple[str, str]] = []
    depth = 0
    collecting: list[str] | None = None
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            info = stripped.lstrip("`").strip()
            if collecting is not None and not info:
                body = "\n".join(collecting).strip()
                kind = body.split(":", 1)[0].strip() if ":" in body.split("\n")[0] else "unknown"
                found.append((kind, body))
                collecting = None
                depth = 0
                continue
            if depth == 0 and info == "VAULT-FEEDBACK":
                collecting = []
                depth = 1
                continue
            depth = 0 if depth else 1
            continue
        if collecting is not None:
            collecting.append(line)
    return found


def classify_user(record: dict, body: str) -> str:
    """Who actually spoke a user-role text block.

    NOT EVERY USER-ROLE BLOCK IS THE OWNER, and the first real use of this script found that out
    the hard way: a background-task notification and the body of an invoked skill both arrived as
    user-role text and were both rendered under his name. A retro reads this file to decide what
    he ruled; a line filed under his name that he never said is the exact defect the whole
    ratification apparatus exists against - 53 such blocks were once found across 44 pages, and
    one of them worked as a rule for three days.

    The discriminator is `origin.kind`, measured on a live transcript rather than assumed:

      {"kind": "human"}             a turn he typed
      {"kind": "task-notification"} the harness telling the session a background job finished
      absent, with isMeta true      the body of a skill the session invoked
      absent, with isMeta false     an interrupt marker - which IS his, he pressed stop
    """
    if body.startswith(INTERRUPT_MARK):
        return "owner"
    origin = record.get("origin")
    if isinstance(origin, dict):
        kind = origin.get("kind")
        if kind == "human":
            return "owner"
        if kind:
            return f"system ({kind})"
    if record.get("isMeta"):
        return "system (skill body)"
    return "system (unattributed)"


MENU_STATE_NOTE = {
    "prose": "**Answered in prose.** No selection came back - he interrupted the menu and said "
             "it in his own words, in the turn below.",
    "open": "**Still open.** No selection, and nothing follows it: the menu is the last thing in "
            "the transcript, and an answer may yet be coming.",
    "lost": "**Lost.** No selection, and the session carried on without him.",
}


def resolve_menus(entries: list[dict], counts: dict) -> None:
    """Give every menu one of FOUR states, and count them apart.

    This used to count two. A menu with a `tool_result` was answered; everything else was an
    answer lost. That arithmetic files the owner's documented preference as a defect - he
    interrupts a menu and answers in prose, and the prose IS the ruling. It also merges two
    states that want opposite responses: a menu still open when the transcript was read needs
    nothing done, and a menu the session walked away from needs chasing.

    The three discriminators are whether a `tool_result` exists, whether a later turn exists,
    and whose it is:

      selected  a result came back - he chose from the menu;
      prose     no result, and the next turn is HIS - he interrupted and answered in words;
      open      no result and no later turn at all - the menu is the last thing in the
                transcript;
      lost      no result, and the session moved on without him.

    `system` entries are stepped over rather than read as turns: a background-task notification
    arriving between the menu and his answer is neither party speaking, and letting it decide
    would file the answer that follows it as lost.

    AN INTERRUPT MARKER COUNTS AS HIS TURN, so a menu he stopped and then said nothing further
    about reads as `prose`. That is deliberate rather than an oversight: pressing stop is
    something only he can do and it is an answer to the menu - a refusal of it - which is nearer
    to answered than to lost. The four states are his; a fifth for `interrupted and silent` is
    not one of them, and inventing one here would widen a ratified scope by hand.
    """
    for position, entry in enumerate(entries):
        if entry.get("kind") != "menu":
            continue
        # PRESENCE OF A RESULT, NEVER ITS TEXT. A selection that renders to an empty string is
        # still a selection, and reading `answer` for this would file it as unanswered.
        if entry.get("result"):
            entry["state"] = "selected"
            counts["answers"] += 1
            continue
        entry["state"] = "open"
        for later in entries[position + 1:]:
            if later.get("kind") == "system":
                continue
            entry["state"] = "prose" if later.get("kind") == "owner" else "lost"
            break
        counts[entry["state"]] += 1


def extract(path: Path) -> tuple[list[dict], dict]:
    """Walk the transcript once. Returns the entries in order, and the counts."""
    entries: list[dict] = []
    questions: dict[str, dict] = {}
    counts = {"owner": 0, "session": 0, "menus": 0, "answers": 0, "prose": 0, "open": 0,
              "lost": 0, "marks": 0, "system": 0, "unparsed": 0}

    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                counts["unparsed"] += 1
                continue
            if record.get("type") not in ("user", "assistant"):
                continue
            # A subagent's turns are not this session's dialogue. None of them appeared in the
            # transcript measured on 2026-08-24, but the guard costs a line and the absence
            # was measured on one session rather than guaranteed.
            if record.get("isSidechain"):
                continue

            message = record.get("message") or {}
            role = message.get("role")
            content = message.get("content")
            if isinstance(content, str):
                content = [{"type": "text", "text": content}]
            if not isinstance(content, list):
                continue

            for block in content:
                if not isinstance(block, dict):
                    continue
                kind = block.get("type")

                if kind == "text":
                    body = block.get("text", "").strip()
                    if not body:
                        continue
                    if role == "user":
                        speaker = classify_user(record, body)
                        if speaker == "owner":
                            counts["owner"] += 1
                            entries.append({"kind": "owner", "text": body})
                        else:
                            # KEPT AND LABELLED, NEVER DROPPED. A recorder that loses data is worse
                            # than a noisy one - but a line filed under the owner's name that he
                            # never said is worse than both, and this file is read at a retro
                            # whose whole purpose is deciding what he ruled.
                            counts["system"] += 1
                            entries.append({"kind": "system", "who": speaker, "text": body})
                    elif role == "assistant":
                        counts["session"] += 1
                        marks = feedback_blocks(body)
                        counts["marks"] += len(marks)
                        entries.append({"kind": "session", "text": body, "marks": marks})

                elif kind == "tool_use" and block.get("name") == "AskUserQuestion":
                    asked = (block.get("input") or {}).get("questions") or []
                    questions[block.get("id")] = {
                        "kind": "menu",
                        "questions": [
                            {
                                "question": q.get("question", ""),
                                "options": [o.get("label", "") for o in (q.get("options") or [])],
                            }
                            for q in asked
                        ],
                        "answer": None,
                        "result": False,
                    }
                    counts["menus"] += 1
                    entries.append(questions[block.get("id")])

                elif kind == "tool_result" and block.get("tool_use_id") in questions:
                    questions[block["tool_use_id"]]["answer"] = answer_text(block)
                    questions[block["tool_use_id"]]["result"] = True

    # THE FOUR STATES ARE DECIDED HERE AND NOWHERE ELSE, because three of them cannot be known
    # at the moment the menu is read: they depend on what comes after it. Counting `answers` in
    # the branch above would also count a repeated `tool_result` twice.
    resolve_menus(entries, counts)
    return entries, counts


def render(entries: list[dict], counts: dict, path: Path) -> str:
    lines = [
        "# Session dialogue",
        "",
        f"Extracted from `{path}`.",
        "",
        "**This file lives one session**, like `.superpowers/sdd/retro.md`, and it is not knowledge",
        "until it has been through an ingest. It carries what was **said**: the transcript stores",
        "`thinking` blocks with empty content, so nothing here is what the session reasoned in",
        "private.",
        "",
        (
            f"Owner turns {counts['owner']}, session replies {counts['session']}, "
            f"menus {counts['menus']} (selected {counts['answers']}, "
            f"answered in prose {counts['prose']}, still open {counts['open']}, "
            f"lost {counts['lost']}), "
            f"feedback marks {counts['marks']}, "
            f"system blocks {counts['system']}."
        ),
        "",
        "---",
        "",
    ]

    all_marks: list[tuple[str, str]] = []
    for turn, entry in enumerate(entries, start=1):
        if entry["kind"] == "owner":
            body = entry["text"]
            label = "owner (interrupted)" if body.startswith(INTERRUPT_MARK) else "owner"
            lines += [f"## {turn}. {label}", "", body, ""]
        elif entry["kind"] == "system":
            # Shown so nothing is lost, short so it cannot drown the dialogue: a skill body runs
            # to a hundred and fifty lines that already live in the repository.
            body = entry["text"]
            head = body if len(body) <= 400 else body[:400] + " ... (truncated)"
            lines += [f"## {turn}. {entry['who']} - NOT the owner", "", head, ""]
        elif entry["kind"] == "session":
            lines += [f"## {turn}. session", "", entry["text"], ""]
            all_marks += entry.get("marks", [])
        else:
            lines += [f"## {turn}. menu", ""]
            for question in entry["questions"]:
                lines.append(f"**Asked:** {question['question']}")
                for option in question["options"]:
                    lines.append(f"- {option}")
                lines.append("")
            state = entry.get("state", "open")
            if state == "selected":
                answer = entry["answer"]
                lines += [
                    f"**Answered:** {answer}" if answer
                    else "**Answered:** (a selection carrying no text)",
                    "",
                ]
            else:
                lines += [MENU_STATE_NOTE[state], ""]

    lines += ["---", "", "# Attention list -- the marks this session filed", ""]
    if all_marks:
        for kind, body in all_marks:
            lines += [f"## {kind}", "", "```", body, "```", ""]
    else:
        lines += ["**None.** The session filed no `VAULT-FEEDBACK` block.", ""]

    return "\n".join(lines) + "\n"


def main() -> None:
    argument = sys.argv[1] if len(sys.argv) > 1 else None
    path = resolve_transcript(argument)

    # A named transcript writes beside the live extract rather than over it. Reading a past
    # session to check something is the ordinary reason to pass an argument, and silently
    # destroying this session's extract to do it would be a trap.
    out = OUT if argument is None else SDD / f"session-dialogue-{path.stem[:8]}.md"

    entries, counts = extract(path)
    SDD.mkdir(parents=True, exist_ok=True)
    out.write_text(render(entries, counts, path), encoding="utf-8")

    print(f"owner turns      : {counts['owner']}")
    print(f"session replies  : {counts['session']}")
    print(f"menus asked      : {counts['menus']}")
    print(f"menus answered   : {counts['answers']}  (by selection)")
    print(f"answered in prose: {counts['prose']}  (interrupted, then answered in his own words)")
    print(f"menus still open : {counts['open']}  (the last thing in the transcript)")
    print(f"menus lost       : {counts['lost']}  (no result, and the session moved on)")
    print(f"feedback marks   : {counts['marks']}")
    print(f"system blocks    : {counts['system']}  (labelled, never filed as his)")
    if counts["unparsed"]:
        print(f"unparsed lines   : {counts['unparsed']}")
    print(f"written          : {out} ({out.stat().st_size} bytes)")

    # The refusal conditions, and each one is a real failure rather than a tidy check.
    if counts["owner"] == 0:
        die("no owner turns found -- wrong transcript, or a format change")
    if counts["session"] == 0:
        die("no session replies found -- wrong transcript, or a format change")
    # ONE OF THE FOUR STATES IS A DEFECT AND THE OTHER THREE ARE NOT. The warning used to fire
    # on all three non-selected states at once, so the reading it produced most often was about
    # a menu the owner had already answered in his own words.
    if counts["lost"]:
        print(
            f"WARNING: {counts['lost']} menu(s) lost -- asked, no result, and the session "
            "carried on without him. This is the state worth chasing. A menu answered in prose "
            "is not one, and answering in prose is his documented preference."
        )


if __name__ == "__main__":
    main()
