"""`guppi ratified` — the `Stop` hook of `rule-spec-write` that writes a ratified Case into
the Spec. `guppi ratified --guard` — the `PreToolUse` hook of
`rule-spec-reconcile` that refuses the agent's edit of the plan file and of its store, and of the file of a built Case under `cases/`. `guppi ratified
--boxes` — the `PostToolUse` hook of `rule-spec-write` that rebuilds the maps of a `spec.md`
after the agent's edit of it.

The write. After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other
than `defer`, or lines that are all `defer` of a Case N that the same reply does not show in the
short form, by `casecheck.is_short_form` — a Case `case-guppi` built — the hook
reads `<plan>.checked.json` for the answer of `case-guppi` stored under
Case N, and the session's transcript for the `SendUserFile` calls on
`raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case — by
`casecheck.sent`, the one reading of a sending, and `casecheck.case_file` — and for the last
earlier reply that shows `## Case N —` (or `### Case N.M —`) with at least one of its
sections, by `casecheck.shows_sections`. It refuses a store with no Case N or one stored with
findings, a showing that differs from the answer in a section it shows — by the one comparison
of `casecheck.against_store` — and a Case whose file no `SendUserFile` call sent after the
time the store holds for Case N, a store that holds no time included, and a Case
whose file holds a Case that differs from the text the store holds under its id or that the
store does not hold, by `casecheck.changed_file`, the one judgment the `Stop` check of a
showing runs; a reply with no showing is no refusal. On a refusal nothing of
Case N is written. Otherwise it writes the stored answer into the Cases
file `<plan stem>.cases.md` beside the plan file `ledger.plan_path` names, by
`ledger.plan_cases_file`, outside the repository — never into the plan file, which holds its
title line and the map alone — and into no copy: the heading,
`context`, `problem`, `recommend`, `given`, `when` and `then` as the stored answer holds them —
a sub-case's own `recommend` under its heading; a `context`, `problem` or
`recommend` it leaves out keeps the text the file held — a block tagged `then` built from the
sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points,
each fenced by `materialize.fence_for`: backticks one longer than the longest run of backticks
that opens a line inside it, three at the least; every section
of the Case is replaced when one stands, the section inserted after its family or before
`## Deferred` otherwise. Once `spec.md` in the session's folder stands, the same answer goes
into it too: every section of the Case there replaced — an approval repeated in
one session leaves it twice — or the section placed in the last approved document; a task
line whose text stood in a replaced section keeps its box. A sub-case also writes its
parent's heading, `context`, `problem` and `recommend` from the parent's stored answer, never
from the reply. No plan file, or a sub-point the hook cannot
read, is a refusal with the reason on stderr. The chat form the hook reads: a task line
opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item; its sub-points are its
keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under
`reword`, `set` (a YAML flow mapping), `change`, `rename`, `sections.<Name>`, `drop`, a YAML
flow list of section names, the fields of a
`create` — each value one code span, with as many backticks as the value needs and padded by
one space on each side when it holds a backtick, an unpadded one refused, or a fenced
block under the sub-point; a field of a `create` whose allowed values in the schema of its
category on disk hold no text, such as `core`, loads as YAML by `materialize.typed_value`, the
reading of the lift and of pre-spec too, and a value that is none of them is refused;
a sub-point that reads into no key `materialize.item_keys` gives its
item is refused, and nothing of the Case is written — `slug` a key of every kind, and
`item_keys` the one judgment `materialize` lifts by and `generate` applies by; a `create` or a
`defer` of a category with no schema file, or of one whose schema rule the session's ledger or
the reply changes, not judged; a `create` of an Estimate takes its `ref` from its ledger line when
no sub-point gives one. A task line opening with `tag` and the tag in its first code span
declares a new tag and is no task: its sub-points `meaning` and `aliases`, each one code span,
make one entry of `new_tags` at the head of the block tagged `then`, in the order of the lines,
which `materialize` carries to `generate`, and the line stands in no block tagged `tasks`;
either sub-point missing, another sub-point or a value that is not one code span is refused,
and nothing of the Case is written. A fence tagged `DIFF` is not read. A fence is judged by
`materialize.fence_opening` and `closes_fence`, the one judgment: a fenced value under a
sub-point that holds a shorter fence of the same character is read whole.

The removal. After the writes, a decision line of the reply that carries
`{supersedes:case N}`, its own Case written in this run, removes the sections of Case N and of
its sub-cases — or of `N.M` alone — from the Cases file of the plan, from the plan file
where it holds them, and from `spec.md` when it stands, under `## Deferred`
too; a Case N none holds is no refusal. A parent of such an `N.M`
leaves with it once the marks of the session's ledger and of the reply retire each of its
sub-cases with a decision line, by `prespec.retired_whole`, imported, and the parent holds no
decision line of its own; a parent with a line of its own stays. A parent whose
own line a mark retires is named by that mark or lies under a Case it names, and so leaves by
that mark with its sub-cases.

The defer. A short put-off — a Case whose lines in the reply are all `defer`,
beside the lines of other Cases or alone, and that the same reply shows in the short form, by
`casecheck.is_short_form`, the one judgment of the `Stop` check of a showing too —
is written from that reply: the heading, `context`, `problem` and its fence tagged `then`, each `defer` line with an item of
`slug`, `type` and `purpose`. It goes under `## Deferred` of the Cases file of the plan, or of `spec.md` in the session's folder once that file stands, its section replaced when it stands and
appended otherwise; the check after the write does not run on it. A missing item,
a key of a `defer` item that `materialize.item_keys` does not give it, or a
fence tagged `then` that holds a YAML comment by `materialize.then_comments` — a `#` at the
start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>`
block; after a space YAML drops the rest of the line, so a value without quotes is cut
there, and after a tab PyYAML, the library the scripts use, refuses the whole block — is a refusal.
So is a `defer` line of the Case whose slug names a Lesson or a Decision page, by
`materialize.defers_a_record`, whether its page stands or not, judged before the fence tagged
`then` is read, with `materialize.DEFER_OF_A_RECORD`: neither page carries `deferred_by`, so no
list would show the item, and nothing of the Case is written.

The map. After each run that writes, places or removes a Case or a defer, the
hook rebuilds the map of the plan file right under its title line, cut from the Cases of the
plan — the plan file and then its Cases file, by `ledger.plan_cases_text`, the one reading of
the Cases of the plan; a plan file that holds Cases of its own, written before its Cases file
stood, keeps them — between `MAP_OPEN` and
`MAP_CLOSE`: a table of one row per top-level Case with its open `stop:` lines and open `read`
lines, a Mermaid diagram of the Cases in order, and an entry per Case and sub-case — 🧩, its id
and name and the path of its case file, then each task line without its sub-points, indented
under the entry after its box: `[x]` for a ticked line, `[ ] ⛔` for an open
`stop:` line by `prespec.STOP_LINE`, `[ ] 🔍` for an open `read` line by `generate.READ_LINE`
and `[ ]` for any other open line; an item line with the `purpose`, `change` or `impact` of its
item and a `read` line with the `purpose` of the `create` of its Estimate — and the Cases
under `## Deferred` by id and name. Once the session's `spec.md` stands, each box of the map
of the plan file is the box of the task line with the same text in the sections of the same
Case there, by `keep_boxes`, the one judgment of a kept box; a box ticked in the map alone is
written back at the next rebuild. Every word is cut from the Cases; no line of the map starts
with a box at its first character, a heading or `# `, and none is `## Deferred`, so
`split_cases`, the tickers and `place` read the plan and `spec.md` as before. The line that
opens a map of `spec.md` says that each box copies the box of its task line below and is no
task of its own; the line that opens the map of the plan file, `plan_map_head`, names its
Cases file, where those task lines stand. `guppi ratified --map <file>
--session <stamp>` prints the map of the Cases of a file and of the Cases file beside it, its
boxes taken in the same way, before any payload is read, and writes nothing.

The maps of `spec.md`. `rebuild_spec_maps` rebuilds the map at the
head of each approved document of a `spec.md` that holds one from the Cases of that document,
the folder of the file naming the case files, and adds no map to a document that has none.
The `Stop` hook runs it on the session's `spec.md` after each run that writes, places or
removes a Case or a defer there; `--boxes` runs it after the agent's `Edit`, `Write` or
`MultiEdit` of a `spec.md` of a session folder `vault/raw/<date>/<HHMM>/`, judged by
`generate.DAY` and `generate.SESSION`, and, for the `spec.md` of the session's own folder,
rebuilds the map of the plan file too; it refuses nothing, prints nothing on stdout and exits
0, an error giving one line on stderr. The tickers of the librarian's run — `tick_read` and
`tick_spec` of `generate`, `tick_command_lines` of `render` and `tick` of `sprint_close` — call
it after each write of a `spec.md`.

The check after the write. Each Case written in the run, and its sub-cases, goes
over the Cases of the plan, read by `ledger.plan_cases_text`, through the checks
of `guppi prespec --check` — `prespec.written_findings`, imported inside
the function since `.guppi/guppi/prespec.py` imports this module — with the decision lines of the
reply added to the window's, since the ledger hook runs in parallel on the same `Stop`; the
Frontier, the translation and the grammar of the window stay with `/pre-spec`. A finding is a
refusal, each finding on stderr naming its Case; the written Case stays.

The guard. On `Edit`, `Write` or `MultiEdit` of a plan file — a `.md` file under
`.claude/plans/`, by `ledger.is_plan_file`, the judgment `plan_path` uses too — or of its
store `<plan>.checked.json`, the hook refuses every `Edit` and `MultiEdit`, every `Write` of a
store, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which
Claude Code shows the agent, and the call does not run. A `Write` of a plan file that does not
exist passes when its content, trimmed, is one line that opens with `# ` — the title line the
agent writes before the first dispatch of `case-guppi` — and is refused otherwise; the hooks
find the plan by that write in the event log, so no hook can create it. Every
`Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder
`vault/raw/<date>/<HHMM>/` — by `casecheck.is_case_file`, the judgment the writer of the file
uses too — is refused the same way, whatever its name and whether it stands, the reason naming
the file and that `case-guppi` alone writes it, unless the hook input names
`case-guppi` as `agent_type`, which Claude Code gives a hook fired inside a subagent: the hook makes that call itself, by `builder_write`, since Claude
Code keeps a subagent in plan mode in Plan Mode whatever its `permissionMode` and would ask
the person — the content of a `Write`, or each `old_string` of an `Edit` or a `MultiEdit`
replaced by its `new_string` in order, once or at each match with `replace_all` — writes one
line `ratified wrote <tool> <path>` to the day's event log and exits 2 with one line that says
the file is written and the call is not to be made again; an old string missing, found more
than once without `replace_all`, or a file that does not exist is refused with that reason and
writes nothing, and an error of the number check below or of the write lets the call run with
one line on stderr, and Claude Code may ask the person that one time. A call of
`case-guppi` on any other file under `cases/`, such as its working note `note-<N>.md`, whose
name gives no number, holds no number and is written by the hook the same way.
Any `Edit`, `Write` or `MultiEdit` of
`case-guppi` outside such a folder is refused. Unless another agent holds the
number of the file: on a call of `case-guppi` on `case-<N>.md`, N by
`casecheck.case_number`, the guard reads the store of the session's plan file, and when
`casecheck.clashes` finds Case N or a sub-case of it under its number alone from another
`agent_id`, it refuses the call with a free number by `casecheck.new_number` — the judgments
the check of `rule-case-check` runs; it refuses the same way, with a free number, a call on a
file that does not stand or holds no text while a decision line of the session's ledger, a
`defer` included, names Case N or a sub-case of it, by `materialize.in_family`, since a
short-form Case has a line and no file; a call that passes while the store holds no entry under N
writes there an entry with its `agent_id` and the time and no text, so the number is held
before the agent stops. A call with no `agent_id`, a file with no number and a session with no
plan file are not judged and write nothing; an error while the guard finds the plan or reads
or writes the store lets the call run, with one line on stderr. A refusal
writes one line to the day's event log; a refused call has no `PostToolUse`, so it leaves no
`tool` line and `plan_path` still names the plan. The hooks of `rule-spec-write` and
`rule-case-check` write the plan and the store with no tool call, and so does this hook for the
entry that holds a number and for the file of `case-guppi`; the guard does not judge those
writes. A file outside `.claude/plans/` and outside
such a `cases/` folder is not judged, nor is a write through a shell; a payload the hook cannot
read exits 0 with one line on stderr. The comparison of an
edited plan with a ratified copy `<plan>.ratified.md` and its marks `<plan>.waiting.json`
 are gone.

A refusal exits 2 with the reason on stderr, which Claude Code hands back to the agent. The
hook writes, removes and checks whether `stop_hook_active` is set or not: Claude Code keeps the
flag set from the first refusal of any `Stop` hook until the person's next message, so a Case
whose lines a reply repeats after a refusal is written at that reply. It guards
its own loop by its refusals in the stretch — the transcript after the person's last message —
read by `ledger.own_refusals` under `COMMAND`: a
reason that already stands in one of them is not printed again, by `ledger.untold`, and the
hook exits 2 only while a reason not yet given is left; with the flag set and a transcript it
cannot read it prints nothing and exits 0. Outside a working session — no `hi` —
it does nothing. It never raises. An error of its own after it has read the payload exits 2 on
`Stop`, with the error and the advice to repeat the ledger lines on stderr, so the agent sees
it — once a stretch, and silent with the flag set and a transcript it cannot read. A Case not yet written then is written at the reply that repeats its lines, and one
written before the error stays and is replaced then. An error while it reads the payload, and any error of the guard, exits 0 with the error
on stderr. `untranslated` is the language
finding `guppi prespec --check` imports, a letter outside the script of the documentation
language judged by `config.outside`; a Latin letter in a code
span gives no finding. Rule pages:
`vault/wiki/rules/rule-spec-write.md`, `vault/wiki/rules/rule-spec-reconcile.md`.
"""

import argparse
import re
import sys
from datetime import datetime
from itertools import pairwise
from pathlib import Path

import yaml

from guppi import config
from guppi.event import append, format_line, log_path, project_root, read_payload, session_stamp
from guppi.ledger import (
    PROJECT_RUN,
    is_plan_file,
    ledger_lines,
    own_refusals,
    plan_cases_file,
    plan_cases_text,
    plan_path,
    reply_text,
    session_dir,
    session_event_logs,
    transcript_records,
    transcript_texts,
    untold,
)
from guppi.materialize import (
    CASE_HEADING,
    DECISION_KINDS,
    DEFER_OF_A_RECORD,
    HEADING,
    category_of,
    closes_fence,
    defers_a_record,
    fence_for,
    fence_opening,
    in_family,
    item_keys,
    parse_line,
    quoted_sections,
    schema_changed,
    schema_values,
    split_cases,
    tagged_blocks,
    then_comments,
    typed_value,  # the one reading of a value that is not text
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
# the parts of a Case the Spec holds
SPEC_SECTIONS = ("context", "problem", "recommend", "given", "when", "then")
PROSE = ("context", "problem")  # the parts the language finding reads
# The story of a Case the Spec holds, which a showing may leave out and a sub-case takes from
# its parent's stored answer.
STORY = ("context", "problem", "recommend")
EDIT_TOOLS = ("Edit", "Write", "MultiEdit")
COMMAND = f"{PROJECT_RUN}guppi ratified"  # the command whose refusals the hook reads
DEFERRED = "## Deferred"
APPROVED = "<!-- approved"  # the stamp `guppi spec` opens each approved document of spec.md with
SPEC_FILE = "spec.md"
TASK_LINE = re.compile(r"^- \[[ xX-]\] (.*)$")
SUB_POINT = re.compile(r"^(\s+)- ([A-Za-z_][\w .]*?):(?:\s+(.*))?$")
ITEM_LINE = re.compile(r"^(create|update|delete|defer) `([^`]+)`")
TAG_LINE = re.compile(r"^tag `([^`]+)`")  # a new tag, an entry of `new_tags`
TAG_KEYS = ("meaning", "aliases")
NEW_TAGS = "new_tags"
# --- reading a Case -----------------------------------------------------------------


def headings(text: str) -> dict[str, str]:
    """Case id → its heading line."""
    found: dict[str, str] = {}
    for line in text.splitlines():
        match = CASE_HEADING.match(line)
        if match:
            found.setdefault(match.group(1).rstrip(":"), line.rstrip())
    return found


# --- the chat form of `tasks` -------------------------------------------------------


UNPADDED = "a value holding a backtick takes its outer span padded by one space"


def code_value(text: str) -> tuple[str | None, str | None]:
    """The content of one code span, as many backticks as it needs, and the refusal. One
    space is trimmed from each side when both stand (CommonMark). A content that holds a
    backtick must stand so padded: unpadded, CommonMark eats a backtick at its edge and
    nothing shows it. `(None, None)` when the text is not one span."""
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
    is content of the value."""
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
    item: dict,
    key: str,
    value: str,
    accepted: set[str] | None = None,
    label: str = "",
    values: dict[str, list] | None = None,
) -> str | None:
    """One sub-point into its item; the error, or None. `accepted`: the keys `item_keys`
    gives the item, a sub-point outside them refused; None, nothing judged.
    `values`: the allowed values of the category of a `create`, by which `typed_value` reads
    a field whose allowed values hold no text, its refusal returned."""
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
    typed, refusal = typed_value(key, value, values or {})
    if refusal:
        return refusal
    item[key] = typed
    return None


def read_tasks(text: str, keys_for=None) -> tuple[list[str], dict, list[str]]:
    """The task lines without their sub-points, the `then` block their items make, and the
    errors of the form. `keys_for(kind, slug)`: the keys an item accepts, or None when none
    are judged. A task line `` tag `<tag>` `` is no task: its sub-points
    `meaning` and `aliases`, each one code span, make an entry of `new_tags`, in the order of
    the lines; either missing, another sub-point or a value that is not one code span is an
    error."""
    lines = text.splitlines()
    tasks: list[str] = []
    block: dict = {}
    tags: list[dict] = []
    errors: list[str] = []
    item: dict | None = None
    is_tag = False  # the item is a tag line
    accepted: set[str] | None = None
    values: dict[str, list] | None = None
    label = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        task = TASK_LINE.match(line)
        if task:
            tag = TAG_LINE.match(task.group(1))
            if tag:
                item, is_tag, label = {"tag": tag.group(1)}, True, f"tag {tag.group(1)}"
                tags.append(item)
                index += 1
                continue
            tasks.append(f"- [ ] {task.group(1)}")
            head = ITEM_LINE.match(task.group(1))
            item, is_tag = None, False
            if head:
                item = {"slug": head.group(2)}
                block.setdefault(head.group(1), []).append(item)
                accepted = keys_for(head.group(1), head.group(2)) if keys_for else None
                values_for = getattr(keys_for, "values_for", None)  # set by `key_judge`
                values = values_for(head.group(1), head.group(2)) if values_for else None
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
                if is_tag:
                    errors.append(f"`{key}`: the value of {label} is not one code span")
                    continue
            if is_tag:
                if key not in TAG_KEYS:
                    errors.append(f"`{key}`: not a key of {label}")
                else:
                    item[key] = value
                continue
            if item is None:
                errors.append(f"`{key}`: a sub-point under a line that is no item")
                continue
            error = put(item, key, value, accepted, label, values)
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
    for entry in tags:
        missing = [key for key in TAG_KEYS if key not in entry]
        if missing:
            errors.append(f"tag {entry['tag']}: no {' and no '.join(f'`{k}`' for k in missing)}")
    then = {NEW_TAGS: tags} if tags else {}
    return tasks, then | {k: block[k] for k in DECISION_KINDS if k in block}, errors


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
    `materialize.fence_for`."""
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
    """The document with every section of `case` replaced, as an approval repeated in one
    session leaves a Case twice in `spec.md`; with none, the section inserted in the
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
    given the box it had there."""
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
    too, judged by `materialize.in_family`."""
    lines = document.splitlines()
    doomed = [i for i, found in case_starts(lines) if in_family(found, case)]
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


def ratified_cases(records: list[dict], reply: str) -> tuple[list[str], dict]:
    """The Cases a reply's ledger lines ratify, in order, a short put-off of `defer_only` left
    out; and the `ref` of each `create` by `(case, slug)`."""
    kinds: dict[str, set[str]] = {}
    refs: dict = {}
    for record in records:
        kinds.setdefault(record["case"], set()).add(record["kind"])
        if record["kind"] == "create" and record.get("ref"):
            refs[(record["case"], record["slug"])] = record["ref"]
    short = set(defer_only(records, reply))
    return [case for case in kinds if case not in short], refs


def find_showing(messages: list[str], case: str):
    """`(heading, lines, text)` of the last message that shows the Case, by
    `casecheck.showings` — under its own heading with at least one of its sections, or as a sub-case named in the one `ratification` of a list showing under its
    top-level heading, its lines then that `ratification` alone and its heading
    the top-level one; None when none shows it. A fence tagged `DIFF` is not read."""
    from guppi.casecheck import showings, top_case  # it imports this module

    for text in reversed(messages):
        shown = showings(split_cases(text))
        if case in shown:
            heads = headings(text)
            return heads.get(case) or heads.get(top_case(case), ""), shown[case], text
    return None


def key_judge(project_dir: Path, schema_free: set[str]):
    """`keys_for(kind, slug)` for `read_tasks`: `materialize.item_keys` of the item's kind
    and category, the categories of `schema_free` not judged."""

    def keys_for(kind: str, slug: str) -> set[str] | None:
        return item_keys(kind, category_of(slug), project_dir, schema_free)

    def values_for(kind: str, slug: str) -> dict[str, list]:
        """Beside the keys: the allowed values of the category's schema on disk, by which `put`
        reads a field of a `create`, for every category."""
        return schema_values(project_dir, category_of(slug)) if kind == "create" else {}

    keys_for.values_for = values_for
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
    its form — the one reading of the write and of `casecheck`. A `context`,
    `problem` or `recommend` the showing leaves out is taken from `held`, the sections the Spec
    holds.
    `keys_for` judges the keys of each item."""
    chat = quoted_sections(lines, CHAT_SECTIONS)
    tasks, block, errors = read_tasks(chat.get("tasks", ""), keys_for)
    if errors:
        return [], errors
    for item in block.get("create") or []:
        ref = refs.get((case, item["slug"]))
        if ref and item["slug"].startswith("estimate-") and "ref" not in item:
            item["ref"] = ref
    sections = {n: chat[n] for n in SPEC_SECTIONS if n in chat}
    for name in STORY:
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
    """The Case into the Cases file of the plan, `ledger.plan_cases_file`, never into the plan
    file, and, when `approved` — the session's `spec.md` — stands, into it too,
    the boxes of its unchanged task lines kept; no copy. The errors,
    empty when it was written — nothing is written when any section has an error."""
    targets = [plan_cases_file(plan)]
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


# --- a deferred Case ---------------------------------------------------


def defer_only(records: list[dict], reply: str) -> list[str]:
    """The short put-offs of a reply, in order: the Cases whose lines are all `defer` and that
    the reply shows in the short form, by `casecheck.is_short_form`, the one judgment of the
    short form; lines of other Cases may stand beside them. A Case of `defer`
    lines that the reply does not show so is a Case built by `case-guppi`."""
    from guppi.casecheck import is_short_form  # it imports this module

    kinds: dict[str, set[str]] = {}
    for record in records:
        kinds.setdefault(record["case"], set()).add(record["kind"])
    shown = split_cases(reply)
    return [
        case
        for case, seen in kinds.items()
        if seen == {"defer"} and case in shown and is_short_form(shown[case])
    ]


def deferred_section(reply: str, case: str, records: list[dict], keys_for=None):
    """`(section, errors)`: the short form of Case N as the reply shows it — the heading,
    `context`, `problem` and its fence tagged `then` — checked against the reply's `defer`
    lines of Case N, and each key of a `defer` item against `keys_for`. A `defer`
    line of Case N whose slug names a Lesson or a Decision page, by `defers_a_record`, refuses
    the Case before its `then` block is read, with `DEFER_OF_A_RECORD`."""
    refused = [r["slug"] for r in records if r["case"] == case and defers_a_record(str(r["slug"]))]
    if refused:
        return [], [f"case {case}: defer {slug}: {DEFER_OF_A_RECORD}" for slug in refused]
    lines = split_cases(reply).get(case)
    if lines is None:
        return [], [f"case {case}: the reply that defers it does not show it"]
    blocks = tagged_blocks(lines, "then")
    comments = then_comments(lines)
    if comments:
        return [], [
            f"case {case}: the fence tagged then holds a YAML comment: `{line.strip()}` — "
            "put the value in quotes, since after a space YAML drops the rest of the line "
            "and after a tab PyYAML refuses the whole block"
            for line in comments
        ]
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
    """Each short put-off of the reply under `## Deferred` of `target`; the errors. Each
    Case written is added to `written`."""
    problems: list[str] = []
    for case in defer_only(records, reply):
        section, errors = deferred_section(reply, case, records, keys_for)
        if errors:
            problems += errors
            continue
        text = target.read_text(encoding="utf-8") if target.is_file() else ""
        write_text(target, place_deferred(text, case, section))
        if written is not None:
            written.add(case)
    return problems


def ancestors(case: str) -> list[str]:
    """The parents of `case` up to its top-level Case: `5.1` and `5` of `5.1.2`."""
    parts = case.split(".")
    return [".".join(parts[:i]) for i in range(len(parts) - 1, 0, -1)]


def remove_superseded(
    records: list[dict], written: set[str], targets: list[Path], session: list[dict] = ()
) -> None:
    """Each Case a `{supersedes:case N}` of a decision line names, the line's own Case
    written in this run, out of every target that stands — the plan and `spec.md`, no copy; a Case no target holds is no refusal. A parent of such a Case
    leaves too once the marks of the decision lines of the session's ledger `session` and of
    `records` retire each of its sub-cases with a decision line, by `prespec.retired_whole`,
    and it holds no decision line of its own."""
    doomed = [
        str(earlier)
        for record in records
        if record["case"] in written
        for earlier in record.get("supersedes") or []
    ]
    if doomed:
        from guppi.prespec import retired_whole, superseded_in_window  # it imports this module

        every = [r for r in [*session, *records] if r.get("record") == "decision"]
        superseded = superseded_in_window(every)
        own = {str(r["case"]) for r in every}
        parents = {parent for case in doomed for parent in ancestors(case)}
        doomed += sorted(
            parent
            for parent in parents
            if parent not in own and retired_whole(parent, superseded, every)
        )
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
    """A sub-case's parent: its heading, `context`, `problem` and `recommend` as `text` — its
    stored answer — holds them; its own `given`, `when`, `then` and blocks, if any,
    kept as they stand, each block fenced by its content; in the Cases file of the
    plan and `approved` when that stands, no copy."""
    parent = case.rsplit(".", 1)[0]
    lines = split_cases(text).get(parent)
    if lines is None:
        return
    shown = quoted_sections(lines, STORY)
    if not shown:
        return
    heading = headings(text)[parent]
    targets = [plan_cases_file(plan)]
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


# --- the map ----------------------------------------------------------

MAP_OPEN = "<!-- map: written by guppi ratified from the Cases below -->"
MAP_CLOSE = "<!-- /map -->"
TICKED = ("[x]", "[X]")
TICKED_BOX, OPEN_BOX = "[x]", "[ ]"
CASE_SIGN, STOP_SIGN, CHECK_SIGN = "🧩", "⛔", "🔍"
MAP_HEAD = (
    "**Map of the Cases** — cut from the Cases below, which follow whole; each box copies the "
    "box of its task line below and is no task of its own."
)


def plan_map_head(plan: Path) -> str:
    """The line that opens the map of the plan file: it names the Cases file beside it, where
    the Cases and their task lines stand."""
    return (
        "**Map of the Cases** — cut from the Cases of the Cases file "
        f"`{plan_cases_file(plan).name}` beside this plan, which follow whole there; each box "
        "copies the box of its task line there and is no task of its own."
    )


ITEM_WORDS = (
    ("create", "purpose"),
    ("update", "change"),
    ("delete", "impact"),
    ("defer", "purpose"),
)


def plan_cases(text: str) -> list[tuple[str, str, list[str], bool]]:
    """`(id, name, lines, deferred)` of each Case of `text` in the order of its first heading;
    `deferred` when the last heading before it that is no Case heading is `## Deferred`. The
    map of the text left out."""
    cases = split_cases(text)
    found: list[tuple[str, str, list[str], bool]] = []
    seen: set[str] = set()
    deferred = False
    for line in without_map(text).splitlines():
        if not HEADING.match(line):
            continue
        match = CASE_HEADING.match(line)
        if match is None:
            deferred = line.strip() == DEFERRED
            continue
        case = match.group(1).rstrip(":")
        if case in seen:
            continue
        seen.add(case)
        name = line.split(" — ", 1)[1].strip() if " — " in line else ""
        found.append((case, name, cases.get(case, []), deferred))
    return found


def item_words(lines: list[str]) -> dict[tuple[str, str], str]:
    """`(kind, slug)` → the words of its item in the block tagged `then` of a Case: the
    `purpose` of a `create` or a `defer`, the `change` of an `update`, the `impact` of a
    `delete`, each on one line."""
    blocks = tagged_blocks(lines, "then")
    try:
        block = yaml.safe_load(blocks[0]) if blocks else {}
    except yaml.YAMLError:
        block = {}
    words: dict[tuple[str, str], str] = {}
    if not isinstance(block, dict):
        return words
    for kind, key in ITEM_WORDS:
        for item in block.get(kind) or []:
            if isinstance(item, dict) and item.get("slug") and item.get(key):
                words[(kind, str(item["slug"]))] = " ".join(str(item[key]).split())
    return words


def map_tasks(lines: list[str]) -> list[tuple[str, str, str, str]]:
    """`(box, sign, text, words)` of each task line of a Case, its sub-points left out: `box`
    `[x]` for a line ticked by its box and `[ ]` otherwise; `sign` ⛔ for an open
    `stop:` line by `prespec.STOP_LINE`, 🔍 for an open `read` line by `generate.READ_LINE`,
    none otherwise; `words` the item's words, or for a `read` line those of the `create` of the
    same Estimate. Each pattern is imported, never copied
    (`rule-one-judgment-one-implementation`)."""
    from guppi.generate import READ_LINE  # the one judgment of a read line
    from guppi.prespec import STOP_LINE  # it imports this module at load

    words = item_words(lines)
    found: list[tuple[str, str, str, str]] = []
    for line in "\n".join(tagged_blocks(lines, "tasks")).splitlines():
        match = TASK_LINE.match(line)
        if match is None:
            continue
        text = match.group(1)
        box = TICKED_BOX if line[2:5] in TICKED else OPEN_BOX
        if box == TICKED_BOX:
            sign = ""
        elif STOP_LINE.match(line):
            sign = STOP_SIGN
        elif READ_LINE.match(line):
            sign = CHECK_SIGN
        else:
            sign = ""
        item = ITEM_LINE.match(text)
        read = READ_LINE.match("- [ ] " + text)  # the text of a read line, whatever its box
        said = ""
        if item:
            said = words.get((item.group(1), item.group(2)), "")
        elif read:
            said = words.get(("create", read.group(1)), "")
        found.append((box, sign, text, said))
    return found


def map_label(text: str) -> str:
    """A label of the Mermaid diagram: no backtick, and a quote or an angle bracket written as
    its entity."""
    text = text.replace("`", "").replace('"', "#quot;")
    return text.replace("<", "#lt;").replace(">", "#gt;")


def map_cell(text: str) -> str:
    return text.replace("|", "\\|")


def case_map(
    text: str, folder: Path | None, project_dir: Path, boxes: str = "", head: str = MAP_HEAD
) -> list[str]:
    """The lines of the map of the Cases of `text`, empty when it holds none: a table of the
    top-level Cases with their open stops and open checks, a Mermaid diagram of the Cases in
    order, an entry per Case and sub-case cut from the Case, and the Cases under `## Deferred`
    by id and name. With `boxes`, the text of the session's `spec.md`, each task line takes the
    box of the line with the same text in the sections of its Case there, by `keep_boxes`. No line starts with a box at its first character, a heading or `# `, so
    `split_cases`, the tickers and `place` read the text as before. `head` is the line that
    opens the map: `MAP_HEAD` for `spec.md`, `plan_map_head` for the plan file."""
    from guppi.casecheck import case_file  # it imports this module

    cases = plan_cases(text)
    live = [(c, n, lines) for c, n, lines, deferred in cases if not deferred]
    later = [(c, n) for c, n, _, deferred in cases if deferred]
    if not live and not later:
        return []
    tasks = {
        case: map_tasks(keep_boxes(boxes, case, lines) if boxes else lines)
        for case, _, lines in live
    }
    out = [MAP_OPEN, "", head, ""]
    tops = [(c, n) for c, n, _ in live if "." not in c]
    if tops:
        out += ["| Case | Name | ⛔ open stops | 🔍 open checks |", "|---|---|---|---|"]
        for case, name in tops:
            family_tasks = [t for c, *_ in live if in_family(c, case) for t in tasks[c]]
            stops = sum(1 for _, sign, *_ in family_tasks if sign == STOP_SIGN)
            checks = sum(1 for _, sign, *_ in family_tasks if sign == CHECK_SIGN)
            out.append(f"| {case} | {map_cell(name)} | {stops} | {checks} |")
        out.append("")
    if live:
        ids = {c for c, *_ in live}
        out += ["```mermaid", "flowchart TD"]
        for case, name, _ in live:
            stop = f"{STOP_SIGN} " if any(s == STOP_SIGN for _, s, *_ in tasks[case]) else ""
            label = map_label(f"{stop}{CASE_SIGN} {case} — {name}")
            out.append(f'    c{case.replace(".", "_")}["{label}"]')
        for before, after in pairwise(tops):
            out.append(f"    c{before[0].replace('.', '_')} --> c{after[0].replace('.', '_')}")
        for case, *_ in live:
            parent = case.rsplit(".", 1)[0] if "." in case else None
            if parent in ids:
                out.append(f"    c{parent.replace('.', '_')} --> c{case.replace('.', '_')}")
        out += ["```", ""]
    for case, name, _ in live:
        where = ""
        if folder is not None:
            path = case_file(folder, case.split(".", 1)[0])
            try:
                where = f" · `{path.relative_to(project_dir).as_posix()}`"
            except ValueError:
                where = f" · `{path.as_posix()}`"
        out.append(f"- {CASE_SIGN} **{case} — {name}**{where}")
        for box, sign, task, said in tasks[case]:
            lead = f"{sign} " if sign else ""
            tail = f" — {said}" if said else ""
            out.append(f"  - {box} {lead}{task}{tail}")
    if later:
        out += ["", "**Deferred:** " + "; ".join(f"{case} — {name}" for case, name in later)]
    out += ["", MAP_CLOSE]
    return out


def without_map(text: str) -> str:
    """`text` with no map: the lines from `MAP_OPEN` to `MAP_CLOSE` out, with the blank line
    after them."""
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if line.strip() == MAP_OPEN]
    if not starts:
        return text
    start = starts[0]
    end = next((j for j in range(start, len(lines)) if lines[j].strip() == MAP_CLOSE), None)
    if end is None:
        return text
    end += 1
    while end < len(lines) and not lines[end].strip():
        end += 1
    del lines[start:end]
    return "\n".join(lines).rstrip("\n") + "\n"


def without_maps(text: str) -> str:
    """`text` with every map out, by `without_map` one at a time: the text of a `spec.md` of
    several approved documents, or of a Spec, judged apart from its maps, which are rebuilt
    once the document stands."""
    while True:
        bare = without_map(text)
        if bare == text:
            return text
        text = bare


def with_map(
    text: str,
    folder: Path | None,
    project_dir: Path,
    boxes: str = "",
    source: str | None = None,
    head: str = MAP_HEAD,
) -> str:
    """`text` with its map rebuilt right under its title line, the first line that opens with
    `# `, or at its head when it has none; with no map when it holds no Case. `boxes` and
    `head` as `case_map` takes them. The map is cut from `source` when given — for the plan
    file, the Cases of the plan by `ledger.plan_cases_text` — and from `text`
    otherwise."""
    bare = without_map(text)
    lines = bare.splitlines()
    cut = bare if source is None else without_map(source)
    found = case_map(cut, folder, project_dir, boxes, head)
    if not found:
        return bare
    at = next((i + 1 for i, line in enumerate(lines) if line.startswith("# ")), 0)
    head = lines[:at]
    rest = lines[at:]
    while rest and not rest[0].strip():
        rest = rest[1:]
    return "\n".join([*head, *([""] if head else []), *found, "", *rest]).rstrip("\n") + "\n"


def session_boxes(folder: Path | None) -> str:
    """The text of the session's `spec.md`, whose task lines give the boxes of the map of the
    plan file once it stands; empty before."""
    return document(folder / SPEC_FILE) if folder is not None else ""


def rebuild_map(plan: Path, folder: Path | None, project_dir: Path) -> None:
    """The map of the plan file rebuilt from the Cases of the plan — the plan file and then
    its Cases file, by `ledger.plan_cases_text` — under the line that names the
    Cases file, its boxes taken from the session's `spec.md` once it stands; the file written
    only when it changed."""
    text = document(plan)
    new = with_map(
        text,
        folder,
        project_dir,
        session_boxes(folder),
        source=plan_cases_text(plan),
        head=plan_map_head(plan),
    )
    if new != text:
        write_text(plan, new)


def print_map(path: Path, session: str, project_dir: Path, now, out, stderr) -> int:
    """`--map <file> --session <stamp>`: the map of the Cases of `path` and of the Cases file
    beside it, by `ledger.plan_cases_text`, on `out`, its boxes and its head line
    taken as `rebuild_map` takes them; no payload read and no file written. A file that does
    not stand, or a session with no `hi`, prints the reason on stderr and exits 1."""
    stamp = session_stamp(session, {})
    folder = session_dir(project_dir, now, stamp)
    if folder is None:
        print(f"ratified: no hi of session {stamp} — no map printed", file=stderr)
        return 1
    if not path.is_file():
        print(f"ratified: {path} does not stand — no map printed", file=stderr)
        return 1
    found = case_map(
        without_map(plan_cases_text(path)),
        folder,
        project_dir,
        session_boxes(folder),
        plan_map_head(path),
    )
    out.write("\n".join(found) + ("\n" if found else ""))
    return 0


def project_of(spec: Path) -> Path:
    """The project folder of a `spec.md` under `vault/raw/`: the folder that holds `vault`;
    the folder of the file when none does."""
    for parent in spec.resolve().parents:
        if parent.name == "vault":
            return parent.parent
    return spec.parent


def rebuild_spec_maps(spec: Path, project_dir: Path | None = None) -> bool:
    """The map at the head of each approved document of `spec` that holds one, rebuilt from
    the Cases of that document, the folder of the file naming the case files; a document with
    no map gets none. The file written only when it changed; True then.
    The one rebuild of the maps of `spec.md`, which the hooks and the tickers call."""
    if not spec.is_file():
        return False
    project_dir = project_of(spec) if project_dir is None else project_dir
    text = spec.read_text(encoding="utf-8")
    lines = text.split("\n")
    starts = [i for i, line in enumerate(lines) if line.startswith(APPROVED)]
    if not starts:
        return False
    bounds = [0, *starts, len(lines)]
    out: list[str] = []
    for start, end in pairwise(bounds):
        part = lines[start:end]
        before_any = start == 0 and 0 not in starts  # the text before the first stamp
        if before_any or not any(line.strip() == MAP_OPEN for line in part):
            out += part
            continue
        body = list(part)
        tail = 0
        while body and not body[-1]:
            body.pop()
            tail += 1
        rebuilt = with_map("\n".join(body) + "\n", spec.parent, project_dir)
        out += rebuilt.rstrip("\n").split("\n") + [""] * tail
    new = "\n".join(out)
    if new == text:
        return False
    spec.write_text(new, encoding="utf-8", newline="\n")
    return True


def is_session_spec(path: Path) -> bool:
    """The `spec.md` of a session folder `vault/raw/<date>/<HHMM>/`, the date and the `HHMM`
    judged by `generate.DAY` and `generate.SESSION`, imported, never copied."""
    from guppi.generate import DAY, SESSION  # the one judgment of a session folder

    parts = Path(str(path)).parts
    return (
        len(parts) >= 5
        and parts[-1] == SPEC_FILE
        and bool(SESSION.match(parts[-2]))
        and bool(DAY.match(parts[-3]))
        and parts[-4] == "raw"
        and parts[-5] == "vault"
    )


def boxes(payload: dict, project_dir: Path, now) -> None:
    """`--boxes`, the `PostToolUse` hook on the agent's edit: after an edit of a
    `spec.md` of a session folder, its maps rebuilt, and, when it is the `spec.md` of the
    session's own folder, the map of the plan file too; any other file left as it stands."""
    tool_input = payload.get("tool_input") or {}
    raw = tool_input.get("file_path") if isinstance(tool_input, dict) else None
    if not raw:
        return
    path = Path(str(raw))
    if not path.is_absolute():
        path = project_dir / path
    if not is_session_spec(path) or not path.is_file():
        return
    rebuild_spec_maps(path, project_dir)
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    if folder is None or folder.resolve() != path.parent.resolve():
        return
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    if plan is not None and plan.is_file():
        rebuild_map(plan, folder, project_dir)


# --- the Cyrillic finding ----------------------------------------


def untranslated(plan_text: str, language: str) -> list[tuple[str, str]]:
    """`(case, part)` for every name, `context` or `problem` of a Case of the plan that still
    holds a letter outside the script of `language`, the code of the documentation language,
    a short form under `## Deferred` included; a Latin letter in a code
    span gives no finding; the `given`, `when`, `then` and the blocks are not
    read."""
    names = headings(plan_text)
    found: list[tuple[str, str]] = []
    for case, lines in split_cases(plan_text).items():
        name = names.get(case, "").split(" — ", 1)[-1]  # the heading's words are not the name
        if config.outside(name, language):
            found.append((case, "name"))
        for name, text in quoted_sections(lines, PROSE).items():
            if config.outside(text, language):
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
    with `# `."""
    lines = str(content or "").strip().splitlines()
    return len(lines) == 1 and lines[0].startswith("# ")


def guard_refusal(payload: dict) -> tuple[str, str] | None:
    """`(path, reason)` when the guard refuses the call, None when it lets it through: every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store,
    every `Write` of a plan file that exists, and a `Write` that creates a plan file with any
    content but one title line; every `Edit`, `Write` and `MultiEdit` of a file under the
    `cases/` folder of a session folder, by `casecheck.is_case_file`, whatever its name and
    whether it stands, unless the hook input names `case-guppi` as `agent_type`; and every such call of `case-guppi` on a file outside such a folder. A file outside
    `.claude/plans/` and outside such a folder is not judged for any other agent. A call of
    `case-guppi` this lets through on `case-<N>.md` is judged next by `held_number`, which
    reads the store: refused when another agent holds the number."""
    from guppi.casecheck import AGENT, is_case_file  # it imports this module

    tool = payload.get("tool_name")
    if tool not in EDIT_TOOLS:
        return None
    tool_input = payload.get("tool_input")
    raw = tool_input.get("file_path") if isinstance(tool_input, dict) else None
    if not raw:
        return None
    path = Path(str(raw))
    builder = payload.get("agent_type") == AGENT  # the field Claude Code gives
    if builder and not is_case_file(path):
        return str(path), (
            f"{path} is outside cases/ of the session folder; case-guppi writes only under "
            f"cases/ of a session folder (rule-spec-reconcile)"
        )
    if is_store(path):
        return str(path), (
            f"{path} is the store of the answers of case-guppi; the hooks alone write it, and "
            f"{CHANGE_THROUGH} (rule-spec-reconcile)"
        )
    if is_case_file(path):
        if builder:
            return None
        return str(path), (
            f"{path} is the file of a built Case under cases/ of the session folder; "
            f"case-guppi alone writes it, and {CHANGE_THROUGH} (rule-spec-reconcile)"
        )
    if not is_plan_file(path):
        return None
    if tool == "Write" and not path.exists():
        if is_title_line(tool_input.get("content")):
            return None
        return str(path), (
            f"{path} is created with its title line alone — one line that opens with `# `; "
            f"the hooks write the map of the Cases into it, and {CHANGE_THROUGH} (rule-spec-reconcile)"
        )
    return str(path), (
        f"{path} is the plan of the session; the hooks alone write it, and {CHANGE_THROUGH} "
        "(rule-spec-reconcile)"
    )


def held_number(
    payload: dict, project_dir: Path, now, stderr
) -> tuple[tuple[str, str] | None, bool]:
    """`((path, reason), True)` when a call of `case-guppi` on `case-<N>.md` under `cases/`
    meets Case N, or a sub-case of it, held in the store under its number alone by another
    `agent_id` — by `casecheck.clashes`, the reason naming a free number by
    `casecheck.new_number`; and the same, with a free number, when the file does
    not stand or holds no text, by `has_text`, while a decision line of the session's ledger of
    any kind, a `defer` included, names Case N or a sub-case of it, by `materialize.in_family`, since a short-form Case has a line and no file; a refused call holds no
    number. A call that passes while the store holds no entry under N writes
    there an entry with its `agent_id` and the time and no text. A call with no `agent_id`, a
    file with no number and a session with no plan file are not judged and write nothing; an
    error while finding the plan or reading or writing the store prints one line on stderr and
    gives `(None, False)`, so the guard lets the call run and writes no file."""
    from guppi.casecheck import (  # it imports this module
        AGENT,
        case_number,
        clashes,
        held_store,
        is_case_file,
        ledger_of,
        ledger_records,
        new_number,
        write_store,
    )

    if payload.get("tool_name") not in EDIT_TOOLS or payload.get("agent_type") != AGENT:
        return None, True
    tool_input = payload.get("tool_input")
    raw = tool_input.get("file_path") if isinstance(tool_input, dict) else None
    agent_id = str(payload.get("agent_id") or "")
    if not raw or not agent_id or not is_case_file(Path(str(raw))):
        return None, True
    number = case_number(raw)
    if number is None:
        return None, True
    try:
        stamp = session_stamp(None, payload)
        plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
        if plan is None or not plan.is_file():
            return None, True
        store = held_store(plan)
        folder = session_dir(project_dir, now, stamp)
        if clashes({number: []}, store, agent_id):
            free = new_number(ledger_records(ledger_of(folder)), store, number, project_dir, folder)
            reason = (
                f"{raw}: another case-guppi holds case {number} in the store — build this "
                f"Case as case {free}, in cases/case-{free}.md (rule-spec-reconcile)"
            )
            return (str(raw), reason), True
        if not has_text(Path(str(raw))):
            records = ledger_records(ledger_of(folder))
            if any(
                record.get("record") == "decision" and in_family(str(record["case"]), number)
                for record in records
            ):
                free = new_number(records, store, number, project_dir, folder)
                reason = (
                    f"{raw}: a decision line of the session's ledger names case {number}, and "
                    f"its file holds no text — build this Case as case {free}, in "
                    f"cases/case-{free}.md (rule-spec-reconcile)"
                )
                return (str(raw), reason), True
        if number not in store:
            store[number] = {"agent_id": agent_id, "stored": now.isoformat()}
            write_store(plan, store)
    except Exception as exc:  # noqa: BLE001 — the call runs, as on any error of the guard
        print(f"ratified: number not held: {exc}", file=stderr)
        return None, False
    return None, True


def has_text(path: Path) -> bool:
    """Whether the file stands and holds more than white space: a Case file with text is a
    Case built before, which a call may write again under its own number."""
    return path.is_file() and bool(path.read_bytes().decode("utf-8").strip())


def builder_file(payload: dict) -> Path | None:
    """The file under `cases/` that a call of `case-guppi` names, which the guard writes
    itself; None for any other call."""
    from guppi.casecheck import AGENT, is_case_file  # it imports this module

    if payload.get("tool_name") not in EDIT_TOOLS or payload.get("agent_type") != AGENT:
        return None
    tool_input = payload.get("tool_input")
    raw = tool_input.get("file_path") if isinstance(tool_input, dict) else None
    if not raw or not is_case_file(Path(str(raw))):
        return None
    return Path(str(raw))


def text_after(payload: dict, path: Path) -> tuple[str | None, str | None]:
    """The text a `Write`, an `Edit` or a `MultiEdit` of `path` would leave, and None; or None
    and the reason it cannot be made: the content of a `Write`, or each
    `old_string` of an `Edit` or of the `edits` of a `MultiEdit` replaced by its `new_string`
    in order, once or at each match with `replace_all`, the text read as UTF-8 with its line
    ends as they stand. The reason when an old string is missing, is found more than once
    without `replace_all`, or the file to edit does not exist. The one computation that
    `builder_write` and the hook `guppi frontierguard` share."""
    tool = payload.get("tool_name")
    tool_input = payload["tool_input"]
    if tool == "Write":
        return str(tool_input.get("content") or ""), None
    if not path.is_file():
        return None, f"{path} does not exist; write it whole by Write (rule-spec-reconcile)"
    text = path.read_bytes().decode("utf-8")
    edits = tool_input.get("edits") if tool == "MultiEdit" else [tool_input]
    for edit in edits or []:
        old, new = str(edit.get("old_string") or ""), str(edit.get("new_string") or "")
        found = text.count(old) if old else 0
        if not found:
            return None, (
                f"{path}: the old string is not in the file; nothing written (rule-spec-reconcile)"
            )
        if found > 1 and not edit.get("replace_all"):
            return None, (
                f"{path}: the old string is found {found} times and replace_all is not "
                "set; nothing written (rule-spec-reconcile)"
            )
        text = text.replace(old, new) if edit.get("replace_all") else text.replace(old, new, 1)
    return text, None


def builder_write(payload: dict, path: Path) -> str | None:
    """Make the write of `case-guppi` on `path` as the tool would, the text by `text_after`,
    written as UTF-8. None once written; the reason of `text_after`, with the
    file left as it stands, when the text cannot be made. An error of the write raises."""
    text, reason = text_after(payload, path)
    if text is None:
        return reason
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))
    return None


def guard(payload: dict, project_dir: Path, now, stderr) -> int:
    """`PreToolUse`: refuse the agent's edit of the plan file, of its store and
    of a file of a built Case under `cases/`, by `guard_refusal`, and a call of
    `case-guppi` on the file of a Case another agent holds, or on a file with no
    text of a Case the session's ledger names, by `held_number`.
    A call of `case-guppi` on its file that both let through the guard writes itself, by
    `builder_write`, and stops with exit 2 and one line that says so, since Claude Code keeps a
    subagent in plan mode in Plan Mode and would ask the person; an error of
    `held_number` or of the write lets the call run. A refusal and a write each write one line
    to the day's event log first: a stopped call has no `PostToolUse`, so it leaves no `tool`
    line, and a refusal not written is nowhere."""
    tool = str(payload.get("tool_name"))
    refused = guard_refusal(payload)
    if refused is None:
        refused, held = held_number(payload, project_dir, now, stderr)
        target = builder_file(payload)
        if refused is None and held and target is not None:
            try:
                reason = builder_write(payload, target)
            except Exception as exc:  # noqa: BLE001 — the call runs, as on any error of the guard
                print(f"ratified: not written: {exc}", file=stderr)
                return 0
            if reason is None:
                event(project_dir, now, payload, ["wrote", tool, str(target)], stderr)
                print(
                    f"ratified: {target} is written by this hook as the {tool} sets it; do not "
                    f"make the call again, and Read the file before its next Edit "
                    f"(rule-spec-reconcile)",
                    file=stderr,
                )
                return 2
            refused = str(target), reason
    if refused is None:
        return 0
    path, reason = refused
    event(project_dir, now, payload, ["refused", tool, path], stderr)
    print(f"ratified: {reason}", file=stderr)
    return 2


def event(project_dir: Path, now, payload: dict, words: list[str], stderr) -> None:
    """One line `ratified <words>` in the day's event log; the call is stopped whatever the
    log does."""
    try:
        append(log_path(project_dir, now), format_line("ratified", payload, words, None, now))
    except Exception as exc:  # noqa: BLE001 — the stop stands whatever the log does
        print(f"ratified: {words[0]} not logged: {exc}", file=stderr)


def stop(payload: dict, project_dir: Path, now, stderr, told: list[str] | None = None) -> int:
    """The write, the removal and the check, whether `stop_hook_active` is set or not: Claude
    Code keeps the flag set from a refusal of any `Stop` hook until the person's next message,
    so a Case repeated after a refusal would wait for the person otherwise. Each
    reason is printed once a stretch: one that stands in `told`, the hook's own refusals in
    the stretch, stays silent, by `ledger.untold`."""
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
    cases, refs = ratified_cases(records, reply)
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    keys_for = key_judge(project_dir, window_schema_free(folder, reply))
    approved = folder / SPEC_FILE  # the approved Spec, once `guppi spec` wrote it
    problems: list[str] = []
    written: set[str] = set()
    if cases:
        if plan is None or not plan.is_file():
            problems.append(
                "no plan file of this session in the event log — create it with its title "
                "line, then repeat the ledger lines"
            )
        else:
            # it imports this module
            from guppi.casecheck import (
                SEND,
                against_store,
                case_file,
                changed_file,
                read_store,
                sent,
            )

            store = read_store(plan)
            records_of_session = transcript_records(payload)
            messages = transcript_texts(payload)
            if messages and messages[-1].strip() == reply.strip():
                messages = messages[:-1]
            for case in cases:
                found = find_showing(messages, case)  # none is no refusal
                heading, lines = (found[0], found[1]) if found else ("", [])
                # the Case against its store
                problem = against_store(case, heading, lines, store)
                if problem:
                    problems.append(problem)
                    continue
                path = case_file(folder, case)
                stored = store[case].get("stored")
                if not sent(records_of_session, path, project_dir, since=stored or ""):
                    problems.append(
                        f"case {case}: no {SEND} call on {path} after its answer was stored "
                        f"({stored or 'no time held'}) — send the file, then repeat the ledger "
                        "lines"
                    )
                    continue
                changed = changed_file(folder, case, store)  # a file changed after
                if changed:
                    problems.append(changed)
                    continue
                answer = store[case]["text"]  # the Case as case-guppi wrote it
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
                if isinstance(parent, dict):  # its prose from its stored answer only
                    write_parent(plan, case, str(parent.get("text") or ""), approved)
    checked = set(written)  # the check after the write reads the Cases of `write_case` only
    deferring = bool(defer_only(records, reply))
    if deferring:
        # into the Cases file of the plan; once spec.md stands, there
        target = approved if approved.is_file() else plan
        if target is None or not target.is_file():
            problems.append(
                "no plan file of this session in the event log — create it with its title "
                "line, then repeat the ledger lines"
            )
        else:
            if target is plan:
                target = plan_cases_file(plan)
            problems += write_defers(reply, records, target, keys_for, written)
    # spec.md, the plan file and its Cases file
    targets = [approved] + ([plan, plan_cases_file(plan)] if plan is not None else [])
    from guppi.casecheck import ledger_of, ledger_records  # it imports this module

    session = ledger_records(ledger_of(folder))
    # the superseded sections out
    remove_superseded(records, written, targets, session)
    removing = any(record.get("supersedes") for record in records)
    if approved.is_file() and (written or removing or deferring):
        rebuild_spec_maps(approved, project_dir)  # the maps of spec.md
    if plan is not None and plan.is_file() and (written or removing or deferring):
        rebuild_map(plan, folder, project_dir)  # the map under the title line
    if checked:
        from guppi import prespec  # it imports this module at load

        text = plan_cases_text(plan)  # the plan file and its Cases file
        problems += prespec.written_findings(text, checked, project_dir, stamp, now, records)
    loud = untold(problems, told, payload)  # each reason once a stretch
    if loud:
        print("ratified: " + "; ".join(loud), file=stderr)
        return 2
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi ratified", description=__doc__.split("\n\n")[0])
    p.add_argument(
        "--guard", action="store_true", help="the PreToolUse hook on an edit of the plan"
    )
    p.add_argument(
        "--boxes",
        action="store_true",
        help="the PostToolUse hook on an edit: rebuild the maps of a spec.md",
    )
    p.add_argument("--map", type=Path, help="print the map of the Cases of this file")
    p.add_argument("--session", help="the stamp of the hi: line, with --map")
    return p


def run(
    argv, *, stdin=None, stderr=None, project_dir: Path | None = None, now=None, stdout=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stderr = sys.stderr if stderr is None else stderr
    stdout = sys.stdout if stdout is None else stdout
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    try:
        args = parser().parse_args(argv)
    except Exception as exc:  # noqa: BLE001 — no payload, no way to read its refusals
        print(f"ratified: not done: {exc}", file=stderr)
        return 0
    if args.map is not None:  # before any payload is read
        if not args.session:
            print("ratified: --map takes --session <stamp>", file=stderr)
            return 1
        return print_map(args.map, args.session, project_dir, now, stdout, stderr)
    try:
        payload = read_payload(stdin)
    except Exception as exc:  # noqa: BLE001 — no payload, no way to read its refusals
        print(f"ratified: not done: {exc}", file=stderr)
        return 0
    if not payload:
        print("ratified: payload not readable, nothing done", file=stderr)
        return 0
    if args.boxes:  # refuses nothing and prints nothing on stdout
        try:
            boxes(payload, project_dir, now)
        except Exception as exc:  # noqa: BLE001 — an edit is never refused for a map
            print(f"ratified: not done: {exc}", file=stderr)
        return 0
    if args.guard:
        try:
            return guard(payload, project_dir, now, stderr)
        except Exception as exc:  # noqa: BLE001 — a guard that raises would block every edit
            print(f"ratified: not done: {exc}", file=stderr)
            return 0
    told: list[str] | None = None
    try:
        told = own_refusals(payload, COMMAND)  # its refusals in the stretch
        return stop(payload, project_dir, now, stderr, told)
    except Exception as exc:  # noqa: BLE001 — shown to the agent, not swallowed
        message = (
            f"ratified: not done: {exc}. Fix the cause, then repeat the ledger lines of the "
            "Case so that the Spec takes it."
        )
        # once a stretch; silent with the flag set and no transcript to tell by
        if not untold([message], told, payload):
            return 0
        print(message, file=stderr)
        return 2
