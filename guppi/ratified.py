"""`guppi ratified` — the `Stop` hook that writes a ratified Case into the Spec
(`rule-spec-write`, case 387.2); `guppi ratified --guard` — the `PreToolUse` hook that refuses
the agent's edit of the plan file and of its store (`rule-spec-reconcile`, case 445.1).

The write. After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other
than `defer`, the hook reads the session's transcript, finds the last earlier reply that shows
`## Case N —` (or `### Case N.M —`) whole — `when`, `then` and `tasks` present — compares it
with the answer of `case-guppi` stored under Case N in `<plan>.checked.json` by the one
comparison of `casecheck.against_store`, refuses a showing that differs, a store with no Case
N or one stored with findings, and writes the stored answer (case 437) into the plan file
`ledger.plan_path` names, outside the repository, and into no copy (case 445.2): the heading,
`context`, `problem`, `given`, `when` and `then` as the stored answer holds them — a `context`
or `problem` it leaves out keeps the text the file held — a block tagged `then` built from the
sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points,
each fenced by `materialize.fence_for`: backticks one longer than the longest run of backticks
that opens a line inside it, three at the least (case 444.2); every section
of the Case is replaced when one stands, the section inserted after its family or before
`## Deferred` otherwise. Once `spec.md` in the session's folder stands, the same answer goes
into it too (case 441.6): every section of the Case there replaced — an approval repeated in
one session leaves it twice — or the section placed in the last approved document; a task
line whose text stood in a replaced section keeps its box. A sub-case also writes its
parent's heading, `context` and `problem` from the parent's stored answer, never from the
reply. The chat form the hook reads: a task line opening with `create`, `update`,
`delete` or `defer` and the slug in its first code span is an item; its sub-points are its
keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under
`reword`, `set` (a YAML flow mapping), `change`, `rename`, `sections.<Name>`, the fields of a
`create` — each value one code span, with as many backticks as the value needs and padded by
one space on each side when it holds a backtick, an unpadded one refused (case 402), or a fenced
block under the sub-point; a sub-point that reads into no key `materialize.item_keys` gives its
item is refused, and nothing of the Case is written — a `create` or a `defer` of a category with
no schema file, or of one whose schema rule the session's ledger or the reply changes, not
judged (cases 308.2, 436.1); a `create` of an Estimate takes its `ref` from its ledger line when
no sub-point gives one. A fence tagged `DIFF` is not read (case 441.8). A fence is judged by
`materialize.fence_opening` and `closes_fence`, the one judgment: a fenced value under a
sub-point that holds a shorter fence of the same character is read whole (case 444.1).

The removal (case 441.7). After the writes, a decision line of the reply that carries
`{supersedes:case N}`, its own Case written in this run, removes the sections of Case N and of
its sub-cases — or of `N.M` alone — from the plan and `spec.md` when it stands, under
`## Deferred` too; a Case N neither holds is no refusal (case 445.3).

The defer (case 421.1). A Case whose lines in the reply are all `defer` — beside the lines of
other Cases or alone — is written from the same reply, which shows it in the short form: the
heading, `context`, `problem` and its fence tagged `then`, each `defer` line with an item of
`slug`, `type` and `purpose`. It goes under `## Deferred` of the plan file, or of `spec.md` in
the session's folder once that file stands (Retro), its section replaced when it stands and
appended otherwise; the check after the write does not run on it. No showing, a missing item,
or a key of a `defer` item that `materialize.item_keys` does not give it (case 436.3) is a
refusal.

The check after the write (case 414.1). Each Case written in the run, and its sub-cases, goes
through the checks of `guppi prespec --check` — `prespec.written_findings`, imported inside
the function since `guppi/prespec.py` imports this module — with the decision lines of the
reply added to the window's, since the ledger hook runs in parallel on the same `Stop`; the
Frontier and the grammar of the window stay with `/pre-spec`. A finding is a refusal; the
written Case stays.

The guard (case 445.1). On `Edit`, `Write` or `MultiEdit` of a plan file — a `.md` file under
`.claude/plans/`, by `ledger.is_plan_file`, the judgment `plan_path` uses too — or of its
store `<plan>.checked.json`, the hook refuses every `Edit` and `MultiEdit`, every `Write` of a
store, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which
Claude Code shows the agent, and the call does not run. A `Write` of a plan file that does not
exist passes when its content, trimmed, is one line that opens with `# ` — the title line the
agent writes before the first dispatch of `case-guppi` — and is refused otherwise. A refusal
writes one line to the day's event log; a refused call has no `PostToolUse`, so it leaves no
`tool` line and `plan_path` still names the plan. A file outside `.claude/plans/` is not
judged; a payload the hook cannot read exits 0 with one line on stderr. The comparison of an
edited plan with a ratified copy `<plan>.ratified.md` and its marks `<plan>.waiting.json`
(case 387.3) are gone.

A refusal exits 2 with the reason on stderr, which Claude Code hands back to the agent; on the
re-fire (`stop_hook_active`) the hook exits 0 and does nothing, so it cannot loop. Outside a
working session — no `hi` — it does nothing. It never raises. `untranslated` is the Cyrillic
finding `guppi prespec --check` imports (cases 387.4, 445.4). Rule pages:
`vault/wiki/rules/rule-spec-write.md`, `vault/wiki/rules/rule-spec-reconcile.md`.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

from guppi.event import append, format_line, log_path, project_root, read_payload, session_stamp
from guppi.ledger import (
    is_plan_file,
    ledger_lines,
    plan_path,
    reply_text,
    session_dir,
    session_event_logs,
    transcript_texts,
)
from guppi.materialize import (
    CASE_HEADING,
    DECISION_KINDS,
    HEADING,
    QUOTE,
    SECTION_START,
    category_of,
    closes_fence,
    fence_for,
    fence_opening,
    item_keys,
    parse_line,
    schema_changed,
    split_cases,
    tagged_blocks,
)

CHAT_SECTIONS = (
    "context",
    "problem",
    "recommend",
    "given",
    "when",
    "then",
    "tasks",
    "ratification",
)
SPEC_SECTIONS = ("context", "problem", "given", "when", "then")
PROSE = ("context", "problem")
WHOLE = ("when", "then", "tasks")
EDIT_TOOLS = ("Edit", "Write", "MultiEdit")
DEFERRED = "## Deferred"
APPROVED = "<!-- approved"  # the stamp `guppi spec` opens each approved document of spec.md with
SPEC_FILE = "spec.md"
TASK_LINE = re.compile(r"^- \[[ xX-]\] (.*)$")
SUB_POINT = re.compile(r"^(\s+)- ([A-Za-z_][\w .]*?):(?:\s+(.*))?$")
ITEM_LINE = re.compile(r"^(create|update|delete|defer) `([^`]+)`")
CYRILLIC = re.compile(r"[А-Яа-яЁё]")


# --- reading a Case -----------------------------------------------------------------


def quoted_sections(lines: list[str], names: tuple[str, ...]) -> dict[str, str]:
    """Name → text of the `> **name:**` blockquotes among `lines`, for the names given; the
    chat form and the Spec form alike. A blank line outside a fence closes a section, the
    fence judged by `materialize.fence_opening` and `closes_fence` (case 444.1)."""
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    opening: tuple[str, int, str] | None = None

    def close():
        if current is not None:
            sections[current] = "\n".join(buffer).strip("\n")

    for raw in lines:
        match = QUOTE.match(raw)
        if not match:
            if opening is None:
                opening = fence_opening(raw)
            elif closes_fence(raw, opening):
                opening = None
            if opening is None and current is not None and raw.strip() == "":
                close()
                current = None
            continue
        text = match.group(1)
        start = SECTION_START.match(text)
        if start and start.group(1) in names:
            close()
            current = start.group(1)
            buffer = [start.group(2)] if start.group(2) else []
        elif current is not None:
            buffer.append(text)
    close()
    return sections


def headings(text: str) -> dict[str, str]:
    """Case id → its heading line."""
    found: dict[str, str] = {}
    for line in text.splitlines():
        match = CASE_HEADING.match(line)
        if match:
            found.setdefault(match.group(1).rstrip(":"), line.rstrip())
    return found


def shown_whole(lines: list[str]) -> bool:
    """A Case shown whole in the chat: its `when`, `then` and `tasks` stand."""
    sections = quoted_sections(lines, CHAT_SECTIONS)
    return all(name in sections for name in WHOLE)


# --- the chat form of `tasks` -------------------------------------------------------


UNPADDED = "a value holding a backtick takes its outer span padded by one space"


def code_value(text: str) -> tuple[str | None, str | None]:
    """The content of one code span, as many backticks as it needs, and the refusal. One
    space is trimmed from each side when both stand (CommonMark). A content that holds a
    backtick must stand so padded: unpadded, CommonMark eats a backtick at its edge and
    nothing shows it (case 402). `(None, None)` when the text is not one span."""
    text = text.strip()
    ticks = len(text) - len(text.lstrip("`"))
    if not ticks or len(text) <= 2 * ticks or not text.endswith("`" * ticks):
        return None, None
    inner = text[ticks:-ticks]
    padded = len(inner) > 1 and inner.startswith(" ") and inner.endswith(" ") and inner.strip()
    if "`" in inner and not padded:
        return None, UNPADDED
    return (inner[1:-1] if padded else inner), None


def fenced_value(lines: list[str], start: int) -> tuple[str | None, int]:
    """The text of the fenced block that opens at `start`, dedented by its fence; and the
    index after its closing fence. None when no fence opens there or none closes it. The
    indent of the opening line is the sub-point's; inside it the fence is judged by
    `materialize.fence_opening` and `closes_fence`, so a shorter fence of the same character
    is content of the value (case 444.1)."""
    if start >= len(lines):
        return None, start
    first = lines[start]
    indent = len(first) - len(first.lstrip())
    opening = fence_opening(first[indent:])
    if opening is None:
        return None, start
    body: list[str] = []
    for index in range(start + 1, len(lines)):
        line = lines[index]
        inner = line[indent:] if line[:indent].strip() == "" else line.lstrip()
        if closes_fence(inner, opening):
            return "\n".join(body), index + 1
        body.append(inner)
    return None, len(lines)


def sub_point_key(key: str) -> str:
    """The key of the item a sub-point reads into: `old` and `new` into `replace`, `reword
    old` and `reword new` into `reword`, `sections.<Name>` into `sections`."""
    if key in ("old", "new"):
        return "replace"
    if key in ("reword old", "reword new"):
        return "reword"
    if key.startswith("sections."):
        return "sections"
    return key


def put(
    item: dict, key: str, value: str, accepted: set[str] | None = None, label: str = ""
) -> str | None:
    """One sub-point into its item; the error, or None. `accepted`: the keys `item_keys`
    gives the item, a sub-point outside them refused; None, nothing judged (case 436.1)."""
    if accepted is not None and sub_point_key(key) not in accepted:
        return f"`{key}`: not a key of {label}"
    if key in ("old", "reword old"):
        item.setdefault("replace" if key == "old" else "reword", []).append({"old": value})
        return None
    if key in ("new", "reword new"):
        pairs = item.get("replace" if key == "new" else "reword") or []
        if not pairs or "new" in pairs[-1]:
            return f"`{key}` with no `old` before it"
        pairs[-1]["new"] = value
        return None
    if key == "set":
        try:
            data = yaml.safe_load(value)
        except yaml.YAMLError:
            data = None
        if not isinstance(data, dict):
            return "`set` is not a YAML mapping"
        item.setdefault("set", {}).update(data)
        return None
    if key.startswith("sections."):
        item.setdefault("sections", {})[key[len("sections.") :]] = value
        return None
    if value.lstrip().startswith(("[", "{")):
        try:
            item[key] = yaml.safe_load(value)
        except yaml.YAMLError:
            return f"`{key}` is not YAML"
        return None
    item[key] = value
    return None


def read_tasks(text: str, keys_for=None) -> tuple[list[str], dict, list[str]]:
    """The task lines without their sub-points, the `then` block their items make, and the
    errors of the form. `keys_for(kind, slug)`: the keys an item accepts, or None when none
    are judged (case 436.1)."""
    lines = text.splitlines()
    tasks: list[str] = []
    block: dict = {}
    errors: list[str] = []
    item: dict | None = None
    accepted: set[str] | None = None
    label = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        task = TASK_LINE.match(line)
        if task:
            tasks.append(f"- [ ] {task.group(1)}")
            head = ITEM_LINE.match(task.group(1))
            item = None
            if head:
                item = {"slug": head.group(2)}
                block.setdefault(head.group(1), []).append(item)
                accepted = keys_for(head.group(1), head.group(2)) if keys_for else None
                label = f"{head.group(1)} {head.group(2)}"
            index += 1
            continue
        point = SUB_POINT.match(line)
        if point:
            key, rest = point.group(2).strip(), point.group(3)
            if rest and rest.strip():
                value, refusal = code_value(rest)
                index += 1
                if refusal:
                    errors.append(f"`{key}`: {refusal}")
                    continue
                if value is None:
                    errors.append(f"`{key}`: the value is not one code span")
                    continue
            else:
                value, index = fenced_value(lines, index + 1)
                if value is None:
                    errors.append(f"`{key}`: no value — neither a code span nor a fenced block")
                    index += 1
                    continue
            if item is None:
                errors.append(f"`{key}`: a sub-point under a line that is no item")
                continue
            error = put(item, key, value, accepted, label)
            if error:
                errors.append(error)
            continue
        if line.strip():
            errors.append(f"a line off the form: {line.strip()[:60]}")
        index += 1
    for entries in block.values():
        for entry in entries:
            for pairs in (entry.get("replace") or [], entry.get("reword") or []):
                if pairs and "new" not in pairs[-1]:
                    errors.append(f"{entry['slug']}: an `old` with no `new`")
    return tasks, {k: block[k] for k in DECISION_KINDS if k in block}, errors


# --- writing the Spec ---------------------------------------------------------------


class _Dumper(yaml.SafeDumper):
    pass


def _string(dumper, data):
    return dumper.represent_scalar(
        "tag:yaml.org,2002:str", data, style="|" if "\n" in data else None
    )


_Dumper.add_representer(str, _string)


def dump(block: dict) -> str:
    return yaml.dump(
        block, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1_000_000
    ).rstrip("\n")


def fenced(tag: str, text: str) -> list[str]:
    """A block tagged `tag` holding `text`, a blank line after it; its fence one longer than
    the longest run of backticks that opens a line of the text, three at the least, by
    `materialize.fence_for` (case 444.2)."""
    fence = fence_for(text)
    return [f"{fence}{tag}", *text.splitlines(), fence, ""]


def spec_section(heading: str, sections: dict[str, str], block: dict, tasks: list[str]):
    """The Spec form of one Case, a list of lines ending in a blank line."""
    out = [heading, ""]
    for name in SPEC_SECTIONS:
        if name in sections:
            out.append(f"> **{name}:**")
            out += [f"> {line}" if line else ">" for line in sections[name].splitlines()]
            out.append("")
    if block:
        out += fenced("then", dump(block))
    if tasks:
        out += fenced("tasks", "\n".join(tasks))
    return out


def family(case: str, other: str) -> bool:
    root = case.split(".", 1)[0]
    return other == root or other.startswith(root + ".")


def case_starts(lines: list[str]) -> list[tuple[int, str]]:
    """`(index, case id)` of every Case heading among `lines`."""
    return [
        (i, match.group(1).rstrip(":"))
        for i, match in ((i, CASE_HEADING.match(line)) for i, line in enumerate(lines))
        if match
    ]


def section_end(lines: list[str], start: int) -> int:
    """The index of the next heading after `start`, or the end."""
    return next((j for j in range(start + 1, len(lines)) if HEADING.match(lines[j])), len(lines))


def place(document: str, case: str, section: list[str]) -> str:
    """The document with every section of `case` replaced (case 441.6: an approval repeated
    in one session leaves a Case twice in `spec.md`); with none, the section inserted in the
    last approved document — the whole document when it holds no stamp — after the last
    section of its family, or before its `## Deferred`, or at the end."""
    lines = document.splitlines()
    own = [i for i, found in case_starts(lines) if found == case]
    if own:
        for i in reversed(own):
            lines[i : section_end(lines, i)] = section
        return "\n".join(lines).rstrip("\n") + "\n"
    base = max((i for i, line in enumerate(lines) if line.startswith(APPROVED)), default=0)
    starts = [(i, found) for i, found in case_starts(lines) if i >= base]
    kin = [i for i, found in starts if family(case, found)]
    if kin and "." not in case:  # a parent stands before its sub-cases
        at = kin[0]
    elif kin:
        at = section_end(lines, kin[-1])
    else:
        at = next((j for j in range(base, len(lines)) if lines[j].strip() == DEFERRED), len(lines))
    before = lines[:at]
    if before and before[-1].strip():
        before.append("")
    return "\n".join(before + section + lines[at:]).rstrip("\n") + "\n"


def keep_boxes(document: str, case: str, section: list[str]) -> list[str]:
    """`section` with each task line whose text stood in a section of `case` in `document`
    given the box it had there (case 441.6)."""
    lines = document.splitlines()
    boxes: dict[str, str] = {}
    for i, found in case_starts(lines):
        if found != case:
            continue
        for line in lines[i : section_end(lines, i)]:
            match = TASK_LINE.match(line)
            if match:
                boxes[match.group(1)] = line[: line.index("]") + 1]
    kept: list[str] = []
    for line in section:
        match = TASK_LINE.match(line)
        if match and match.group(1) in boxes:
            line = boxes[match.group(1)] + line[line.index("]") + 1 :]
        kept.append(line)
    return kept


def remove_case(document: str, case: str) -> str:
    """The document without the sections of `case` and of its sub-cases, under `## Deferred`
    too (case 441.7)."""
    lines = document.splitlines()
    doomed = [i for i, found in case_starts(lines) if found == case or found.startswith(case + ".")]
    if not doomed:
        return document
    for i in reversed(doomed):
        del lines[i : section_end(lines, i)]
        while 0 < i < len(lines) and not lines[i - 1].strip() and not lines[i].strip():
            del lines[i]  # one blank line where the section stood
    return "\n".join(lines).rstrip("\n") + "\n"


def document(path: Path) -> str:
    """The text of the plan or of `spec.md`; empty when the file does not stand."""
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="")


def ratified_cases(records: list[dict]) -> tuple[list[str], dict]:
    """The Cases a reply's ledger lines ratify, in order, a defer-only Case left out; and the
    `ref` of each `create` by `(case, slug)`."""
    kinds: dict[str, set[str]] = {}
    refs: dict = {}
    for record in records:
        kinds.setdefault(record["case"], set()).add(record["kind"])
        if record["kind"] == "create" and record.get("ref"):
            refs[(record["case"], record["slug"])] = record["ref"]
    return [case for case, seen in kinds.items() if seen != {"defer"}], refs


def find_showing(messages: list[str], case: str):
    """`(heading, lines, text)` of the last message that shows the Case whole; None when none
    shows it. A fence tagged `DIFF` is not read (case 441.8)."""
    for text in reversed(messages):
        cases = split_cases(text)
        if case in cases and shown_whole(cases[case]):
            return headings(text)[case], cases[case], text
    return None


def key_judge(project_dir: Path, schema_free: set[str]):
    """`keys_for(kind, slug)` for `read_tasks`: `materialize.item_keys` of the item's kind
    and category, the categories of `schema_free` not judged (cases 308.2, 436.1)."""

    def keys_for(kind: str, slug: str) -> set[str] | None:
        return item_keys(kind, category_of(slug), project_dir, schema_free)

    return keys_for


def window_schema_free(folder: Path | None, reply: str) -> set[str]:
    """The categories whose schema rule a decision line of the session's ledger or of the
    reply creates or updates — their `create` and `defer` items not judged by their keys."""
    lines = list(ledger_lines(reply))
    if folder is not None:
        path = folder / "ledger.md"
        if path.is_file():
            lines += path.read_text(encoding="utf-8").splitlines()
    return schema_changed(lines)


def case_section(
    case: str,
    heading: str,
    lines: list[str],
    refs: dict,
    held: dict | None = None,
    keys_for=None,
) -> tuple[list[str], list[str]]:
    """The Spec section of a Case shown in the chat form, built in memory, and the errors of
    its form — the one reading of the write and of `casecheck` (case 419.3). A `context` or
    `problem` the showing leaves out is taken from `held`, the sections the Spec holds.
    `keys_for` judges the keys of each item (case 436.1)."""
    chat = quoted_sections(lines, CHAT_SECTIONS)
    tasks, block, errors = read_tasks(chat.get("tasks", ""), keys_for)
    if errors:
        return [], errors
    for item in block.get("create") or []:
        ref = refs.get((case, item["slug"]))
        if ref and item["slug"].startswith("estimate-") and "ref" not in item:
            item["ref"] = ref
    sections = {n: chat[n] for n in SPEC_SECTIONS if n in chat}
    for name in PROSE:
        if name not in sections and held and name in held:
            sections[name] = held[name]
    return spec_section(heading, sections, block, tasks), []


def write_case(
    plan: Path,
    case: str,
    heading: str,
    lines: list[str],
    refs: dict,
    keys_for=None,
    approved: Path | None = None,
) -> list[str]:
    """The Case into the plan and, when `approved` — the session's `spec.md` — stands, into it
    too, the boxes of its unchanged task lines kept (case 441.6); no copy (case 445.2). The
    errors, empty when it was written — nothing is written when any section has an error."""
    targets = [plan]
    if approved is not None and approved.is_file():
        targets.append(approved)
    sections: list[tuple[Path, str, list[str]]] = []
    for path in targets:
        text = document(path)
        held = quoted_sections(split_cases(text).get(case, []), SPEC_SECTIONS)
        section, errors = case_section(case, heading, lines, refs, held, keys_for)
        if errors:
            return errors
        if path == approved:
            section = keep_boxes(text, case, section)
        sections.append((path, text, section))
    for path, text, section in sections:
        write_text(path, place(text, case, section))
    return []


# --- a deferred Case (case 421.1) ---------------------------------------------------


def defer_only(records: list[dict]) -> list[str]:
    """The Cases whose lines in a reply are all `defer`, in order; lines of other Cases may
    stand beside them."""
    kinds: dict[str, set[str]] = {}
    for record in records:
        kinds.setdefault(record["case"], set()).add(record["kind"])
    return [case for case, seen in kinds.items() if seen == {"defer"}]


def deferred_section(reply: str, case: str, records: list[dict], keys_for=None):
    """`(section, errors)`: the short form of Case N as the reply shows it — the heading,
    `context`, `problem` and its fence tagged `then` — checked against the reply's `defer`
    lines of Case N, and each key of a `defer` item against `keys_for` (case 436.3)."""
    lines = split_cases(reply).get(case)
    if lines is None:
        return [], [f"case {case}: the reply that defers it does not show it"]
    blocks = tagged_blocks(lines, "then")
    try:
        data = yaml.safe_load(blocks[0]) if blocks else None
    except yaml.YAMLError:
        data = None
    items = data.get("defer") if isinstance(data, dict) else None
    if not isinstance(items, list):
        return [], [f"case {case}: no fence tagged then with its defer items"]
    complete = {
        str(item.get("slug"))
        for item in items
        if isinstance(item, dict) and all(item.get(k) for k in ("slug", "type", "purpose"))
    }
    missing = [r["slug"] for r in records if r["case"] == case and r["slug"] not in complete]
    if missing:
        return [], [
            f"case {case}: no defer item with slug, type and purpose for {', '.join(missing)}"
        ]
    if keys_for is not None:
        foreign = []
        for item in items:
            if not isinstance(item, dict):
                continue
            accepted = keys_for("defer", str(item.get("slug")))
            if accepted is None:
                continue
            foreign += [
                f"case {case}: `{key}`: not a key of defer {item.get('slug')}"
                for key in item
                if key not in accepted
            ]
        if foreign:
            return [], foreign
    section = spec_section(headings(reply)[case], quoted_sections(lines, PROSE), {}, [])
    return section + fenced("then", blocks[0]), []


def place_deferred(document: str, case: str, section: list[str]) -> str:
    """The document with the section of `case` replaced where it stands, or appended at the
    end of `## Deferred`, the heading added when the document has none."""
    if case in split_cases(document):
        return place(document, case, section)
    lines = document.rstrip("\n").splitlines()
    if not any(line.strip() == DEFERRED for line in lines):
        lines += ["", DEFERRED]
    return "\n".join(lines + [""] + section).rstrip("\n") + "\n"


def write_defers(
    reply: str, records: list[dict], target: Path, keys_for=None, written: set | None = None
) -> list[str]:
    """Each defer-only Case of the reply under `## Deferred` of `target`; the errors. Each
    Case written is added to `written`."""
    problems: list[str] = []
    for case in defer_only(records):
        section, errors = deferred_section(reply, case, records, keys_for)
        if errors:
            problems += errors
            continue
        text = target.read_text(encoding="utf-8") if target.is_file() else ""
        write_text(target, place_deferred(text, case, section))
        if written is not None:
            written.add(case)
    return problems


def remove_superseded(records: list[dict], written: set[str], targets: list[Path]) -> None:
    """Each Case a `{supersedes:case N}` of a decision line names, the line's own Case
    written in this run, out of every target that stands — the plan and `spec.md`, no copy
    (cases 441.7, 445.3); a Case no target holds is no refusal."""
    doomed = [
        earlier
        for record in records
        if record["case"] in written
        for earlier in record.get("supersedes") or []
    ]
    for path in targets:
        if not doomed or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        new = text
        for case in doomed:
            new = remove_case(new, case)
        if new != text:
            write_text(path, new)


def write_parent(plan: Path, case: str, text: str, approved: Path | None = None) -> None:
    """A sub-case's parent: its heading, `context` and `problem` as `text` — its stored
    answer (case 441.6) — holds them; its own `given`, `when`, `then` and blocks, if any,
    kept as they stand, each block fenced by its content (case 444.2); in the plan and
    `approved` when that stands, no copy (case 445.2)."""
    parent = case.rsplit(".", 1)[0]
    lines = split_cases(text).get(parent)
    if lines is None:
        return
    shown = quoted_sections(lines, PROSE)
    if not shown:
        return
    heading = headings(text)[parent]
    targets = [plan]
    if approved is not None and approved.is_file():
        targets.append(approved)
    for path in targets:
        current = document(path)
        held_lines = split_cases(current).get(parent, [])
        held = quoted_sections(held_lines, SPEC_SECTIONS)
        sections = {**held, **shown}
        block_text = tagged_blocks(held_lines, "then")
        task_text = tagged_blocks(held_lines, "tasks")
        section = spec_section(heading, sections, {}, [])
        if block_text:
            section += fenced("then", "\n".join(block_text))
        if task_text:
            section += fenced("tasks", "\n".join(task_text))
        write_text(path, place(current, parent, section))


# --- the Cyrillic finding (cases 387.4, 445.4) ----------------------------------------


def untranslated(plan_text: str) -> list[tuple[str, str]]:
    """`(case, part)` for every name, `context` or `problem` of a Case of the plan that still
    holds a Cyrillic letter, a short form under `## Deferred` included (case 445.4); the
    `given`, `when`, `then` and the blocks are not read."""
    names = headings(plan_text)
    found: list[tuple[str, str]] = []
    for case, lines in split_cases(plan_text).items():
        if CYRILLIC.search(names.get(case, "")):
            found.append((case, "name"))
        for name, text in quoted_sections(lines, PROSE).items():
            if CYRILLIC.search(text):
                found.append((case, name))
    return found


# --- the hooks ----------------------------------------------------------------------


CHANGE_THROUGH = "a Case changes only through its case-guppi and a new ratification"


def is_store(path: Path) -> bool:
    """The store `<plan>.checked.json` of a plan file, beside it (`rule-case-check`)."""
    from guppi.casecheck import STORE_SUFFIX  # it imports this module

    name = path.name
    if not name.endswith(STORE_SUFFIX):
        return False
    return is_plan_file(path.with_name(name[: -len(STORE_SUFFIX)] + ".md"))


def is_title_line(content) -> bool:
    """The content of the `Write` that creates a plan file: trimmed, one line that opens
    with `# ` (case 445.1)."""
    lines = str(content or "").strip().splitlines()
    return len(lines) == 1 and lines[0].startswith("# ")


def guard_refusal(payload: dict) -> tuple[str, str] | None:
    """`(path, reason)` when the guard refuses the call, None when it lets it through (case
    445.1): every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store,
    every `Write` of a plan file that exists, and a `Write` that creates a plan file with any
    content but one title line. A file outside `.claude/plans/` is not judged."""
    tool = payload.get("tool_name")
    if tool not in EDIT_TOOLS:
        return None
    tool_input = payload.get("tool_input")
    raw = tool_input.get("file_path") if isinstance(tool_input, dict) else None
    if not raw:
        return None
    path = Path(str(raw))
    if is_store(path):
        return str(path), (
            f"{path} is the store of the answers of case-guppi; the hooks alone write it, and "
            f"{CHANGE_THROUGH} (rule-spec-reconcile)"
        )
    if not is_plan_file(path):
        return None
    if tool == "Write" and not path.exists():
        if is_title_line(tool_input.get("content")):
            return None
        return str(path), (
            f"{path} is created with its title line alone — one line that opens with `# `; "
            f"the hooks write the Cases into it, and {CHANGE_THROUGH} (rule-spec-reconcile)"
        )
    return str(path), (
        f"{path} is the plan of the session; the hooks alone write it, and {CHANGE_THROUGH} "
        "(rule-spec-reconcile)"
    )


def guard(payload: dict, project_dir: Path, now, stderr) -> int:
    """`PreToolUse`: refuse the agent's edit of the plan file and of its store (case 445.1).
    A refusal writes one line to the day's event log first: a refused call has no
    `PostToolUse`, so it leaves no `tool` line, and a refusal not written is nowhere."""
    refused = guard_refusal(payload)
    if refused is None:
        return 0
    path, reason = refused
    tool = str(payload.get("tool_name"))
    try:
        line = format_line("ratified", payload, ["refused", tool, path], None, now)
        append(log_path(project_dir, now), line)
    except Exception as exc:  # noqa: BLE001 — the refusal stands whatever the log does
        print(f"ratified: refusal not logged: {exc}", file=stderr)
    print(f"ratified: {reason}", file=stderr)
    return 2


def stop(payload: dict, project_dir: Path, now, stderr) -> int:
    if payload.get("stop_hook_active"):
        return 0
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    if folder is None:
        return 0
    reply = reply_text(payload)
    records = [
        record
        for record in (parse_line(line) for line in ledger_lines(reply))
        if record and record.get("record") == "decision"
    ]
    cases, refs = ratified_cases(records)
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    keys_for = key_judge(project_dir, window_schema_free(folder, reply))
    approved = folder / SPEC_FILE  # the approved Spec, once `guppi spec` wrote it (441.6)
    problems: list[str] = []
    written: set[str] = set()
    if cases:
        if plan is None or not plan.is_file():
            problems.append(
                "no plan file of this session in the event log — create it with its title "
                "line, then repeat the ledger lines"
            )
        else:
            from guppi.casecheck import against_store, read_store  # it imports this module

            store = read_store(plan)
            messages = transcript_texts(payload)
            if messages and messages[-1].strip() == reply.strip():
                messages = messages[:-1]
            for case in cases:
                found = find_showing(messages, case)
                if found is None:
                    problems.append(f"case {case}: no earlier reply shows it whole")
                    continue
                heading, lines, _ = found
                problem = against_store(case, heading, lines, store)  # case 437
                if problem:
                    problems.append(problem)
                    continue
                answer = store[case]["text"]  # the Case as case-guppi answered it
                errors = write_case(
                    plan,
                    case,
                    headings(answer)[case],
                    split_cases(answer)[case],
                    refs,
                    keys_for,
                    approved,
                )
                if errors:
                    problems += [f"case {case}: {error}" for error in errors]
                    continue
                written.add(case)
                parent = store.get(case.rsplit(".", 1)[0]) if "." in case else None
                if isinstance(parent, dict):  # its prose from its stored answer only (441.6)
                    write_parent(plan, case, str(parent.get("text") or ""), approved)
    checked = set(written)  # the check after the write reads the Cases of `write_case` only
    if defer_only(records):
        target = approved if approved.is_file() else plan  # a defer at Retro goes to spec.md
        if target is None or not target.is_file():
            problems.append(
                "no plan file of this session in the event log — create it with its title "
                "line, then repeat the ledger lines"
            )
        else:
            problems += write_defers(reply, records, target, keys_for, written)
    targets = [approved] + ([plan] if plan is not None else [])
    remove_superseded(records, written, targets)  # cases 441.7, 445.3
    if checked:
        from guppi import prespec  # it imports this module at load (case 414.1)

        text = plan.read_text(encoding="utf-8")
        problems += prespec.written_findings(text, checked, project_dir, stamp, now, records)
    if problems:
        print("ratified: " + "; ".join(problems), file=stderr)
        return 2
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi ratified", description=__doc__.split("\n\n")[0])
    p.add_argument(
        "--guard", action="store_true", help="the PreToolUse hook on an edit of the plan"
    )
    return p


def run(argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
        payload = read_payload(stdin)
        if not payload:
            print("ratified: payload not readable, nothing done", file=stderr)
            return 0
        if args.guard:
            return guard(payload, project_dir, now, stderr)
        return stop(payload, project_dir, now, stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"ratified: not done: {exc}", file=stderr)
        return 0
