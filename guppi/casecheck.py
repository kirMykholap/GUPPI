"""`guppi casecheck --subagent` — the `SubagentStop` hook that checks the Case `case-guppi`
answers with before the main agent sees it (case 419.3); `guppi casecheck` — the `Stop` hook
that compares each Case the main agent shows with the one the check stored (case 419.4).

The check. For an answer of `case-guppi` (`agent_type`), the hook takes as the answer the
newest output of the subagent in `agent_transcript_path` that holds a Case heading — a text
or the `message` of a `SubagentHandback` call, whichever stands later — or
`last_assistant_message` when the transcript is not readable or holds none (case 434); the
transcript is read by `ledger.read_records`. It reads the Cases of the answer in the chat
form, builds the section of each in the Spec in memory by `ratified.case_section` — the one
reading of the Spec hook, which refuses a sub-point outside `materialize.item_keys` (case
436.1) — and runs `prespec.judge` over them, the decision lines of each `ratification` fence
standing for the ledger; the categories whose schema rule those lines or the session's ledger
change are not judged by their keys (case 436.4). The Frontier and the grammar of the window
stay with `/pre-spec` (case 445.2), but for one check: for each open line of the session's
`frontier.md` whose source is `backlog` and each page of its title with `deferred_by`, a Case
of the answer that, itself or through a sub-case, names the page on a decision line other
than a `defer` gets a finding for each Case of that list when no Case among it and its
sub-cases both names the page and carries its `{supersedes}` — `prespec.decided_on_its_page`,
the judgment `/pre-spec` runs on a closed line (case 467.2). It checks besides the
chat form: the sections in the order of the schema; the ones a Case needs — a parent's
`context` and `problem`, and `when`, `then`, `tasks` and `ratification` of a Case with no
sub-cases (`given` too, unless it is a sub-case); and a `ratification` of one untagged fence of
ledger lines and nothing else, the fence judged by `materialize.fence_opening` and
`closes_fence` (case 444.1); a sub-case that carries `problem` is a finding of that sub-case,
since `problem` stands on its parent only (case 544.4). The text of the story sections —
`context`, `problem` and `recommend` — is not checked: the person judges it; the check still
requires the sections and their order (case 449), but for the titles of the items of
`recommend`: it reads the earlier outputs of the subagent in `agent_transcript_path` that hold
no Case heading — its rounds — and takes the title of each question from its line
`❓ **Q<n>** - **<title>**:`; a title that no item of a `recommend` of the answer opens with,
in bold, is a finding of the top-level Case, a title asked in more than one round looked for
once and the words of an item after its title not judged (case 544.3). It runs over the same
Spec text the language finding of `/pre-spec`,
`prespec.check_untranslated`, imported: a name, `context` or `problem` that holds a letter
outside the script of the documentation language is a finding of its Case, and a `guppi.toml`
that is missing or names a code the table does not hold is one finding, given to the first
Case of the answer (case 537). Each Case of the answer is stored with its findings and the time of
the store in `<plan>.checked.json` beside the plan file of the session, a later answer for the
same id replacing it but for the notes sent for that id, which it keeps (case 472.1). The notes
are those of `prespec.promise_notes` on the answer — a line of a Criterion replaced whole that
the new one does not carry, a `then` line shared by two siblings, named on the later (cases
472.1, 472.2): a note not yet held for its Case id is stored under `notes`, apart from the
findings, and sent back once by exit 2 beside any findings; a note is no finding — the file
of the Case is written as for an answer with none, and `stop` refuses no showing for it. When
no Case of the answer has findings, the Cases of the answer are
written, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the
id of the top-level Case, named by `case_file`: the file replaced whole when the answer holds
the top-level Case, and only the section of each sub-case replaced — or placed after its
family — when the answer holds sub-cases alone (case 452.1); an answer with a finding writes
no file. `case-guppi` itself writes no file, and the agent's edit of one is refused by
`guppi ratified --guard`, which judges the path by `is_case_file`, the predicate `case_file`
stays inside (case 453). A finding exits 2 with the findings on stderr, and Claude Code sends the agent
back (measured 2026-09-25, session 0051), whatever `stop_hook_active` says: Claude Code sets it
on the second fire after a handback with no exit 2 of this hook (measured 2026-09-26, session
1337). The store guards the loop: when every Case with findings stands in the store with the
same text and findings, they are stored again and the hook exits 0. An answer with no Case
heading, where no earlier output holds one either, is not checked or stored. With no plan
file of the session nothing is stored or sent back.

The same comparison — `against_store` — and the same reading of a sending — `sendings`,
under `sent` — serve this module's `stop` and the Spec hook, which writes the stored answer
into the plan and refuses a showing that differs from it (case 437) or a Case whose file was
not sent after its store (case 452.3).

The comparison. On `Stop`, each Case the reply shows under its heading with at least one of
its sections (`shows_sections`) is compared with the Case of the same id in the store in each
of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows — the lines up
to the horizontal rule that opens the agent's own text, line ends and trailing spaces made the
same; a section the reply does not show is not compared (case 452.2). The name of its heading,
its `context`, `problem` and `recommend`, and text under the heading outside its sections are
not compared (cases 441.3, 452.2). A parent shown with its sub-cases is compared part by part.
A Case the store does not hold, one that differs, one stored with findings, or one with no
`SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the
id of its top-level Case, exits 2 with the reason on stderr (case 452.2). A heading with no
section — the acknowledging reply — a fence tagged `DIFF`, and a deferred decision in the
short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and
no `when` — are not compared and need no sending. On the re-fire exit 0; outside a working
session — no `hi` — nothing is done.

A sending. The transcript is JSONL (`ledger.read_records`); a `SendUserFile` call stands in an
assistant record's `message.content` as `{"type": "tool_use", "name": "SendUserFile",
"input": {"files": [<path>, …]}}`, the record carrying its `timestamp` (measured 2026-09-27,
session 1255). The turn of the reply is the records after the last prompt: a `user` record,
not `isMeta`, that holds more than tool results — a tool result and the text of a skill stand
in `user` records too, and a `Stop` hook's refusal adds no `user` record (measured the same
day).

The payload is read as UTF-8; the hook never raises. Rule page:
`vault/wiki/rules/rule-case-check.md`.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi.event import project_root, read_payload, session_stamp
from guppi.generate import DAY, FRONTIER_LINE, FRONTIER_SEPARATOR, SESSION
from guppi.ledger import (
    plan_path,
    read_records,
    reply_text,
    session_dir,
    session_event_logs,
    transcript_records,
)
from guppi.materialize import (
    closes_fence,
    fence_opening,
    parse_line,
    quoted_sections,
    schema_changed,
    split_cases,
    tagged_blocks,
)
from guppi.prespec import (
    BACKLOG_SOURCE,
    FINDING_CASE,
    NOTE_CASE,
    check_untranslated,
    decided_on_its_page,
    deferred_pages,
    judge,
    promise_notes,
)
from guppi.ratified import (
    CHAT_SECTIONS,
    case_section,
    headings,
    key_judge,
    place,
)

AGENT = "case-guppi"
HANDBACK = "SubagentHandback"  # the tool a subagent gives its report through (case 434)
SEND = "SendUserFile"  # the tool that sends the person a file (case 452.2)
STORE_SUFFIX = ".checked.json"
CASES = "cases"  # the folder of the files of built Cases in a session folder (case 452.1)
RULE = "---"  # the horizontal rule after which the agent's own text stands
LEDGER_LINE = ("- decision[", "- estimate[", "- lesson[")
# The parts of a shown Case compared with its stored answer, each only when the reply shows
# it (452.2); the heading name and the prose — `context`, `problem`, `recommend` — are free.
MECHANICAL = ("given", "when", "then", "tasks", "ratification")
# The title line of a question of a round, as the template of the skill `grill-me` writes it,
# and the title of an item of `recommend` (case 544.3).
QUESTION_LINE = re.compile(r"^❓ \*\*Q\d+\*\* - \*\*(.+?)\*\*:")
RECOMMEND_ITEM = re.compile(r"^- \*\*(.+?)\*\*")


def store_of(plan: Path) -> Path:
    return plan.with_name(plan.stem + STORE_SUFFIX)


# --- the file of a built Case (cases 452.1, 453) ------------------------------------------


def top_case(case: str) -> str:
    """The id of the top-level Case of `case`: `452` of `452.1`."""
    return case.split(".", 1)[0]


def is_case_file(path) -> bool:
    """A path under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`,
    whatever its name and whether it stands — the one judgment of the guard `guppi ratified
    --guard` and of the writer, whose `case_file` stays inside it (case 453). The date and
    the `HHMM` are judged by `generate.DAY` and `generate.SESSION`."""
    parts = Path(str(path)).parts
    return any(
        parts[i] == CASES
        and SESSION.match(parts[i - 1])
        and DAY.match(parts[i - 2])
        and parts[i - 3] == "raw"
        and parts[i - 4] == "vault"
        for i in range(4, len(parts) - 1)
    )


def case_file(folder: Path, case: str) -> Path:
    """`raw/<date>/<hi HHMM>/cases/case-<N>.md` of the session folder `folder`, N the id of the
    top-level Case of `case` — the one naming of the file, of the writer, of `stop` and of the
    Spec hook (cases 452.1–452.3)."""
    return folder / CASES / f"case-{top_case(case)}.md"


def write_case_files(folder: Path, cases: list[str], store: dict) -> None:
    """Each top-level Case of an answer into its `case_file`, from the text `store` holds
    (case 452.1): replaced whole when the answer holds the top-level Case — its sections in
    the order of the answer, a blank line between — and otherwise only the section of each
    sub-case of the answer replaced, or placed after its family, by `ratified.place`."""
    groups: dict[str, list[str]] = {}
    for case in cases:
        groups.setdefault(top_case(case), []).append(case)
    for top, members in groups.items():
        path = case_file(folder, top)
        texts = {case: str(store[case]["text"]) for case in members}
        if top in members:
            text = "\n\n".join(texts[case] for case in members) + "\n"
        else:
            text = path.read_text(encoding="utf-8") if path.is_file() else ""
            for case in members:
                text = place(text, case, [*texts[case].splitlines(), ""])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")


# --- a sending (cases 452.2, 452.3) -------------------------------------------------------


def sendings(records: list[dict]) -> list[tuple[str, str]]:
    """`(timestamp, file)` for each file of each `SendUserFile` call among the assistant
    records of a transcript, in order — the one reading of a sending, of `stop` and of the
    Spec hook (case 452.2). The timestamp is the record's, empty when it has none."""
    found: list[tuple[str, str]] = []
    for record in records:
        if not isinstance(record, dict) or record.get("type") != "assistant":
            continue
        message = record.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if not (
                isinstance(block, dict)
                and block.get("type") == "tool_use"
                and block.get("name") == SEND
            ):
                continue
            data = block.get("input")
            files = data.get("files") if isinstance(data, dict) else None
            for file in files if isinstance(files, list) else []:
                if isinstance(file, str) and file:
                    found.append((str(record.get("timestamp") or ""), file))
    return found


def turn_of_reply(records: list[dict]) -> list[dict]:
    """The records of the turn the reply ends: those after the last prompt — a `user` record,
    not `isMeta`, whose content is a text or holds a block other than a tool result."""
    start = 0
    for index, record in enumerate(records):
        if record.get("type") != "user" or record.get("isMeta"):
            continue
        message = record.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        blocks = content if isinstance(content, list) else []
        if isinstance(content, str) or any(
            isinstance(block, dict) and block.get("type") != "tool_result" for block in blocks
        ):
            start = index + 1
    return records[start:]


def file_key(path, project_dir: Path) -> str:
    """A path made comparable: absolute against the project, normalised, its case folded
    where the file system folds it."""
    path = Path(str(path))
    if not path.is_absolute():
        path = project_dir / path
    return os.path.normcase(os.path.normpath(str(path)))


def moment(text) -> datetime | None:
    """An ISO time, made aware in the local zone when it has none; None when not one."""
    try:
        value = datetime.fromisoformat(str(text))
    except (TypeError, ValueError):
        return None
    return value.astimezone() if value.tzinfo is None else value


def sent(records: list[dict], path: Path, project_dir: Path, since=None) -> bool:
    """A `SendUserFile` call on `path` among `records`, by `sendings`; with `since`, a time of
    the store, only a call whose record's timestamp is later than it counts — a time that
    cannot be read on either side counts as none (case 452.3)."""
    want = file_key(path, project_dir)
    after = None if since is None else moment(since)
    for timestamp, file in sendings(records):
        if file_key(file, project_dir) != want:
            continue
        if since is None:
            return True
        when = moment(timestamp)
        if after is not None and when is not None and when > after:
            return True
    return False


def read_store(plan: Path | None) -> dict:
    if plan is None:
        return {}
    try:
        data = json.loads(store_of(plan).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def shown_text(heading: str, lines: list[str]) -> str:
    """The Case as compared: its heading and lines up to the horizontal rule, each line's
    trailing spaces and the blank lines at both ends removed."""
    kept: list[str] = []
    for line in lines:
        if line.strip() == RULE:
            break
        kept.append(line.rstrip())
    return "\n".join([heading.rstrip(), *kept]).strip("\n")


def is_short_form(lines: list[str]) -> bool:
    """A deferred decision in the short form: no `given`, no `when`, a `then` fence with
    `defer` items."""
    sections = quoted_sections(lines, CHAT_SECTIONS)
    if "given" in sections or "when" in sections:
        return False
    return any(block.lstrip().startswith("defer:") for block in tagged_blocks(lines, "then"))


def shows_sections(lines: list[str]) -> bool:
    """A showing of a Case the checks judge: at least one of its sections, not the short
    form — the one judgment of `stop` and of the showing the Spec hook reads (case 452.2)."""
    return bool(quoted_sections(lines, CHAT_SECTIONS)) and not is_short_form(lines)


def has_sub_cases(case: str, cases: dict) -> bool:
    return any(other.startswith(case + ".") for other in cases)


def form_findings(case: str, lines: list[str], cases: dict) -> list[str]:
    """The chat form of one Case: the order of its sections, the ones it needs, what
    `ratification` holds, and no `problem` in a sub-case — it stands on the parent only
    (case 544.4)."""
    sections = quoted_sections(lines, CHAT_SECTIONS)
    names = list(sections)
    findings: list[str] = []
    if names != sorted(names, key=CHAT_SECTIONS.index):
        findings.append(f"case {case}: sections out of the order of the schema: {', '.join(names)}")
    if "." in case and "problem" in sections:
        findings.append(f"case {case}: a sub-case carries problem, which stands on its parent only")
    if has_sub_cases(case, cases):
        needed = ("context", "problem")
    elif "." in case:
        needed = ("when", "then", "tasks", "ratification")
    else:
        needed = ("given", "when", "then", "tasks", "ratification")
    missing = [name for name in needed if name not in sections]
    if missing:
        findings.append(f"case {case}: missing section {', '.join(missing)}")
    if "ratification" in sections:
        body = [line.strip() for line in sections["ratification"].splitlines() if line.strip()]
        opening = fence_opening(body[0]) if body else None  # the one judgment (case 444.1)
        if not (
            len(body) >= 3
            and opening is not None
            and opening[2] == ""
            and closes_fence(body[-1], opening)
            and all(line.startswith(LEDGER_LINE) for line in body[1:-1])
        ):
            findings.append(
                f"case {case}: ratification holds one untagged fence of ledger lines and "
                "nothing else"
            )
    return findings


def ratification_records(cases: dict) -> list[dict]:
    """The decision records of every `ratification` fence of the answer."""
    records: list[dict] = []
    for lines in cases.values():
        text = quoted_sections(lines, ("ratification",)).get("ratification", "")
        for line in text.splitlines():
            record = parse_line(line.strip())
            if record and record.get("record") == "decision":
                records.append(record)
    return records


def open_backlog_lines(frontier: Path | None) -> list[tuple[str, str]]:
    """`(item, title)` of each open line of the Frontier whose source — its last segment —
    is `backlog` (case 467.2)."""
    if frontier is None or not frontier.is_file():
        return []
    found: list[tuple[str, str]] = []
    for line in frontier.read_text(encoding="utf-8").splitlines():
        match = FRONTIER_LINE.match(line)
        if not match or match.group(1) != " ":
            continue
        _, item, rest = match.groups()
        if rest.split(FRONTIER_SEPARATOR)[-1].strip() == BACKLOG_SOURCE:
            found.append((item, rest))
    return found


def check_backlog(
    records: list[dict], frontier: Path | None, project_dir: Path
) -> list[tuple[str, str]]:
    """Case 467.2: `(top-level case, finding)` for each open `backlog` line of the Frontier
    and each page of its title with `deferred_by`, against each top-level Case of the answer
    that, itself or through a sub-case, names the page on a decision line other than a
    `defer` — by `prespec.decided_on_its_page`, the judgment `/pre-spec` runs."""
    findings: list[tuple[str, str]] = []
    tops = list(dict.fromkeys(top_case(str(r["case"])) for r in records))
    for item, title in open_backlog_lines(frontier):
        for slug, deferred in deferred_pages(title, project_dir).items():
            for top in tops:
                named, missing = decided_on_its_page(slug, deferred, records, top)
                for m in missing if named else []:
                    finding = (
                        f"case {top}: names {slug}, the page of the open backlog line "
                        f"{item}, and no Case among case {top} and its sub-cases names it "
                        f"and carries {{supersedes:case {m}}}"
                    )
                    findings.append((top, finding))
    return findings


def recommend_titles(cases: dict) -> set[str]:
    """The title of each item of every `recommend` of the answer: a line `- **<title>**` at
    the top level of the list (case 544.3)."""
    titles: set[str] = set()
    for lines in cases.values():
        text = quoted_sections(lines, ("recommend",)).get("recommend", "")
        for line in text.splitlines():
            match = RECOMMEND_ITEM.match(line)
            if match:
                titles.add(match.group(1).strip())
    return titles


def check_rounds(cases: dict, rounds: list[str]) -> list[tuple[str, str]]:
    """Case 544.3: `(top-level case, finding)` for each title of a question of the rounds
    that no item of a `recommend` of the answer opens with, in bold; a title asked in more
    than one round is looked for once, and the words of an item after its title are not
    judged."""
    if not rounds or not cases:
        return []
    held = recommend_titles(cases)
    top = top_case(next(iter(cases)))
    return [
        (top, f"case {top}: recommend holds no item for the question of the rounds: {title}")
        for title in dict.fromkeys(rounds)
        if title not in held
    ]


def check_answer(
    text: str,
    project_dir: Path,
    window: list[str] = (),
    frontier: Path | None = None,
    rounds: list[str] = (),
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Case id → its findings, and case id → its notes, for every Case of an answer of
    `case-guppi`. The categories whose schema rule the lines of the `ratification` fences or
    of the session's `window` change are not judged by their keys (case 436.4). `frontier`,
    the session's `frontier.md`, adds the check of its open `backlog` lines (case 467.2).
    `rounds`, the titles of the questions of the rounds of `case-guppi` on the Case, adds
    the check that `recommend` holds an item for each (case 544.3). The
    language finding of `/pre-spec`, `check_untranslated`, runs over the same Spec text as
    `judge`, each hit a finding of its Case (case 537). The notes are those of
    `prespec.promise_notes` on the answer — a Criterion line not carried, a `then` line shared
    by siblings (cases 472.1, 472.2)."""
    cases = split_cases(text)
    heads = headings(text)
    records = ratification_records(cases)
    schema_free = schema_changed(records) | schema_changed(list(window))
    keys_for = key_judge(project_dir, schema_free)
    refs = {
        (r["case"], r["slug"]): r["ref"]
        for r in records
        if r.get("kind") == "create" and r.get("ref")
    }
    found: dict[str, list[str]] = {case: [] for case in cases}
    spec: list[str] = ["# the answer of case-guppi", ""]
    for case, lines in cases.items():
        found[case] += form_findings(case, lines, cases)
        section, errors = case_section(case, heads[case], lines, refs, keys_for=keys_for)
        found[case] += [f"case {case}: {error}" for error in errors]
        spec += section or [heads[case], ""]
    spec_text = "\n".join(spec) + "\n"
    for finding in judge(spec_text, project_dir, records, schema_free=schema_free) + (
        check_untranslated(spec_text, project_dir)  # the language finding (case 537)
    ):
        match = FINDING_CASE.match(finding)
        case = match.group(1) if match else ""
        found[case if case in found else next(iter(cases))].append(finding)
    for top, finding in check_backlog(records, frontier, project_dir) + check_rounds(
        cases, list(rounds)
    ):
        family = [c for c in found if c == top or c.startswith(f"{top}.")]
        found[family[0] if family else next(iter(cases))].append(finding)
    notes: dict[str, list[str]] = {case: [] for case in cases}
    for note in promise_notes(spec_text, project_dir):
        match = NOTE_CASE.match(note)
        case = match.group(1) if match else ""
        notes[case if case in notes else next(iter(cases))].append(note)
    return found, notes


def outputs(record: dict) -> list[str]:
    """The texts one assistant record of a subagent's transcript gives its caller: each
    text block, and the `message` of each `SubagentHandback` call."""
    message = record.get("message") if isinstance(record, dict) else None
    content = message.get("content") if isinstance(message, dict) else None
    if isinstance(content, str):
        return [content]
    found: list[str] = []
    for block in content if isinstance(content, list) else []:
        if not isinstance(block, dict):
            continue
        if block.get("type") == "text":
            found.append(str(block.get("text") or ""))
        elif block.get("type") == "tool_use" and block.get("name") == HANDBACK:
            data = block.get("input")
            found.append(str(data.get("message") or "") if isinstance(data, dict) else "")
    return found


def answer_of(payload: dict) -> str:
    """The answer of the subagent (case 434): the newest output in `agent_transcript_path`
    that holds a Case heading — a text or the `message` of a `SubagentHandback` call,
    whichever stands later; `last_assistant_message` when the transcript is not readable or
    holds none."""
    records = read_records(payload.get("agent_transcript_path"))
    for record in reversed(records or []):
        if record.get("type") != "assistant":
            continue
        for text in reversed(outputs(record)):
            if split_cases(text):
                return text
    return str(payload.get("last_assistant_message") or "")


def round_titles(payload: dict) -> list[str]:
    """The title of each question of the rounds of the subagent, in order: the outputs in
    `agent_transcript_path` that hold no Case heading, each line `❓ **Q<n>** - **<title>**:`
    of the question template of the skill `grill-me` (case 544.3). An unreadable transcript
    gives none."""
    titles: list[str] = []
    for record in read_records(payload.get("agent_transcript_path")) or []:
        if record.get("type") != "assistant":
            continue
        for text in outputs(record):
            if split_cases(text):
                continue
            for line in text.splitlines():
                match = QUESTION_LINE.match(line.strip())
                if match:
                    titles.append(match.group(1).strip())
    return titles


def subagent(payload: dict, project_dir: Path, now, stderr) -> int:
    if payload.get("agent_type") != AGENT:
        return 0
    text = answer_of(payload)
    cases = split_cases(text)
    if not cases:
        return 0
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    window = ledger_of(folder)
    frontier = folder / "frontier.md" if folder is not None else None
    found, notes = check_answer(text, project_dir, window, frontier, round_titles(payload))
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    if plan is None or not plan.is_file():
        return 0  # no plan file: nothing stored, nothing sent back (case 434)
    store = read_store(plan)
    heads = headings(text)
    repeated = True  # every Case with findings stands in the store as it is, findings and all
    fresh: list[str] = []  # the notes not yet sent for their Case id (case 472.1)
    for case, lines in cases.items():
        entry = {
            "text": shown_text(heads[case], lines),
            "findings": found[case],
            "stored": now.isoformat(),  # the time a sending must follow (case 452.1)
        }
        held = store.get(case)
        if found[case] and not (
            isinstance(held, dict) and held.get("text") == entry["text"] and held.get("findings")
        ):
            repeated = False
        kept = list(held.get("notes") or []) if isinstance(held, dict) else []
        new = [note for note in notes[case] if note not in kept]
        fresh += new
        if kept or new:  # the notes sent for the id outlive a later answer (case 472.1)
            entry["notes"] = kept + new
        store[case] = entry
    store_of(plan).write_text(
        json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8", newline=""
    )
    findings = [f for case in cases for f in found[case]]
    if not findings and folder is not None:  # the file of a Case that passed (case 452.1)
        write_case_files(folder, list(cases), store)
    if (findings and not repeated) or fresh:  # the store guards the loop (434, 472.1)
        print("casecheck: " + "; ".join(findings + fresh), file=stderr)
        return 2
    return 0


def ledger_of(folder: Path | None) -> list[str]:
    """The lines of the session's ledger, empty when there is none."""
    if folder is None or not (folder / "ledger.md").is_file():
        return []
    return (folder / "ledger.md").read_text(encoding="utf-8").splitlines()


def mechanical_parts(lines: list[str]) -> dict[str, str]:
    """The `given`, `when`, `then`, `tasks` and `ratification` of a Case, up to the horizontal
    rule, each line's trailing spaces removed (case 441.3)."""
    kept: list[str] = []
    for line in lines:
        if line.strip() == RULE:
            break
        kept.append(line)
    return {
        name: "\n".join(line.rstrip() for line in text.splitlines()).strip("\n")
        for name, text in quoted_sections(kept, MECHANICAL).items()
    }


def against_store(case: str, heading: str, lines: list[str], store: dict) -> str | None:
    """The one comparison of a shown Case with its stored answer (cases 419.4, 437, 441.3):
    the reason it fails, or None — shared by this module's `stop` and the Spec hook. Only
    the `MECHANICAL` parts `lines` shows are compared, a part it does not show left alone
    (case 452.2), so empty `lines` judge the store alone; `heading` is not compared."""
    entry = store.get(case)
    if not isinstance(entry, dict):
        return f"case {case}: not built and checked by case-guppi — dispatch it"
    if entry.get("findings"):
        return (
            f"case {case}: its check found {'; '.join(entry['findings'])} — send them to case-guppi"
        )
    stored = mechanical_parts(str(entry.get("text") or "").splitlines()[1:])
    shown = mechanical_parts(lines)
    differ = [name for name in MECHANICAL if name in shown and stored.get(name) != shown[name]]
    if differ:
        return (
            f"case {case}: its {', '.join(differ)} differ from the answer of case-guppi — show "
            "them as the answer holds them"
        )
    return None


def stop(payload: dict, project_dir: Path, now, stderr) -> int:
    if payload.get("stop_hook_active"):
        return 0
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    if folder is None:
        return 0
    reply = reply_text(payload)
    cases = split_cases(reply)
    heads = headings(reply)
    shown = {case: lines for case, lines in cases.items() if shows_sections(lines)}
    if not shown:
        return 0
    store = read_store(plan_path(session_event_logs(project_dir, now, stamp), stamp))
    problems = [
        problem
        for case, lines in shown.items()
        if (problem := against_store(case, heads[case], lines, store))
    ]
    turn = turn_of_reply(transcript_records(payload))
    unsent: dict[Path, list[str]] = {}
    for case in shown:  # the file of its top-level Case, sent in this turn (case 452.2)
        path = case_file(folder, case)
        if not sent(turn, path, project_dir):
            unsent.setdefault(path, []).append(case)
    for path, ids in unsent.items():
        problems.append(
            f"case {', '.join(ids)}: no {SEND} call on {path} in the turn of this reply — "
            "send the file"
        )
    if problems:
        print("casecheck: " + "; ".join(problems), file=stderr)
        return 2
    return 0


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        payload = read_payload(stdin)
        if not payload:
            print("casecheck: payload not readable, nothing checked", file=stderr)
            return 0
        if "--subagent" in argv:
            return subagent(payload, project_dir, now, stderr)
        return stop(payload, project_dir, now, stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"casecheck: not checked: {exc}", file=stderr)
        return 0
