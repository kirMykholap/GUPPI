"""`guppi prespec` — the `PreToolUse ExitPlanMode` hook that holds Plan Mode open until
`/pre-spec` has run in this session and the check of its plan finds nothing; `guppi
prespec --check <plan> [--session ID]` — the check of that Plan Mode's artifacts against
each other.

The hook reads the event logs by the session's stamp (case 136.2) — the logs from today
back to the date of this session's `session-start`, as the ledger hook reads them, so a
session across midnight keeps its `hi` and its `prespec` (case 213.2): the session is a
working one when the logs hold a `hi` of its stamp. In a working session with no `prespec` line of
the same stamp after that `hi`, the hook exits 2 with the reason on stderr, which Claude
Code shows the agent and which blocks the tool; the agent runs `/pre-spec` — `guppi gate`
writes the stamped line on the Skill call (case 136.1) — and exits Plan Mode again. With
the line, the hook finds the plan file of the session by `ledger.plan_path` and judges it
by `plan_findings`, the same function `--check` prints, not a copy; while it finds one,
the hook exits 2 with the findings on stderr. A `note:` line does not block, and with no
plan file of the session the exit passes on the line alone (case 561.3). A mark
of another stamp or `--------` does not count, and a `session-start` of another session
resets nothing. An ordinary session — no `hi` — is not gated: no governance applies there.
Any other tool: exit 0; an error of the hook itself prints `prespec: check skipped:
<error>` and exits 0. Rule page: `vault/wiki/rules/rule-prespec-hook.md`.

What follows is what `--check` compares — the description the skill `/pre-spec` points to,
kept here beside the code (case 561.1). The documentation language it names is the one
`guppi.toml` sets for the repository.

The check prints one finding per line on stdout and exits 1 on any, 0 when there is none;
a line opening with `note:` is no finding and sets no exit code (case 378.8); without a
`hi` in the session's window it exits 0 with one line on stderr. The
session is `--session`, else `CLAUDE_SESSION_ID`; with neither it exits 2 with one line on
stderr naming the `hi:` line, and nothing is guessed from the event log (case 213.1). The
session's window is the one the ledger hook walks (`ledger.session_dir`):
the ledgers of its dates, on the `hi` date from the `hi` time on, and its folder
`raw/<hi date>/<hi HHMM>/` (case 73). Findings (cases 59.1, 59.2, 59.3, 59.6, 74,
75.2):

- a decision line written since the session's `hi` with no item of its kind under its own
  Case heading of the plan, and an item of a `then` block with no decision line of its Case;
  a `defer` line matches a `defer` item; an Estimate has its own line and its own item (case 189); a nested `estimate` of an
  older Spec is covered by its parent's create line; the lines of a Case a `{supersedes:case
  N}` of the window names need no item and no `tasks` block — the Case left the plan — and
  its heading still in the plan is a finding of its own (case 299.2); the tag covers N and
  every sub-case of N at any depth, its lines and its headings alike, judged by
  `materialize.in_family`, the reading the Spec hook and `materialize` share; a tag on N.M
  covers N.M and its own sub-cases only (case 660.1); a second item of one kind and slug under one
  Case heading, in one fence tagged `then` or in another, is a finding: one decision line
  covers one item, and `materialize` lifts only the first (case 426);
- the frontier `raw/<hi date>/<hi HHMM>/frontier.md` (case 73.4): missing, an open `[ ]`
  line under `## Cases` — an open line under `## Work` waits for Work Mode and one under
  `## Ask` for the person, and neither is a finding (cases 356.1, 531.12); a closer — the last segment after ` · ` — none of `case N`, `work`,
  `defer`, `kept` and `defer case N`; a box that disagrees with its closer — `[x]` takes
  only `case N` or `work`, `[-]` only `defer`, `kept` or `defer case N` (case 451.2);
  `defer` after a source segment — the one standing immediately before the closer — other
  than `sprint`, `kept` after one other than `backlog`; `defer case N` after the source
  `sprint` or `backlog` (cases 356.2, 451.2), and after another source with no `defer` item
  under Case N in the plan, nor under Case N of the conserved Spec that the title line of
  the plan names — `conserved_spec_named` of `.guppi/guppi/box.py`, the judgment the hook of
  `rule-spec-capture` reads the same line by (case 620.2); `case N` whose heading the plan lacks, and after the source `sprint` with
  no `update` of the sprint page `entity-sprint-<id>` under Case N, the parent or a
  sub-case (cases 314.2, 451.3); the word inside the slug of a title is not the source
  (case 335), and a line that is not a box line is not read; a line closed `[x] … · backlog
  · case N` whose title names in a code span a page with `deferred_by`, when no decision
  line of Case N or of a sub-case, other than a `defer`, names that page, and for each Case
  M of its `deferred_by` when no Case among them both names the page and carries
  `{supersedes:case M}` — `generate` clears a defer only from the pages the superseding Case
  names; the judgment is `decided_on_its_page`, which the check of the answer of
  `case-guppi` imports (case 467);
- a Case with a line of a kind other than `defer` and no fenced block tagged `tasks` (a
  defer-only Case has no work) (case 74); an Estimate a `then` block creates or sets
  `pending` with no task line of its own — a line `- [ ] read `<slug>`` whose first
  backticked slug is that Estimate, matched by `generate.READ_LINE`, the ticker's own
  pattern; a slug named on another Estimate's read line is a finding in its own words, and a
  mention on a line that is not a read line is no task line (case 327);
- an `update` item carrying `file:` — the file route is gone (case 320); the rule that
  governs the path is named when there is one;
- the form of an Estimate item (case 203.1): a Case whose `then` block holds two or more
  Estimate items that set a new Criterion — a `create`, or an `update` that names no part of
  the page by `materialize.names_a_part`, written or lifted (one promise per Case: split
  it) (case 472.3); an `update` of an Estimate whose page does not exist; a `defer` of an
  Estimate, an Insight, a Lesson or a Decision page whose page
  `materialize.defer_writes_no_page` does not find, the judgment by which `generate` fails
  the entry, a short Case under `## Deferred` included (cases 783, 786); a `create` of an
  Estimate whose `ref` names neither a live rule or entity nor one a `create` of the same
  plan carries (case 221); a `create` of an Estimate, or an `update` carrying
  `set: {method: …}`, whose `method` names none of the forms lint classifies — a `make
  <target>`, the word `pytest`, a test path, one of the commands `guppi test`, `guppi check`
  and `guppi style`, or `by hand` — by `lint.names_a_form`, the one predicate, the existence
  of the file and of the target left to lint — and a `create` with no `method` at all
  (cases 331, 820.4); on the Estimate of a MOC as the plan leaves it — the live page, or a
  `create` or an `update` of the plan that writes `kind: MOC` — one that names neither a
  `make <target>`, nor the word `pytest` with a test path, nor `by hand`, by
  `lint.names_a_moc_form`, which `check_method` of lint calls too, in place of the line of
  no form, the Makefile, the existence of the test files and the children left to lint
  (cases 733, 820.4); and one whose `method`
  ties its reading by hand to the first moment after the render or the change — by
  `lint.tied_to_a_one_off_moment`, the one predicate of the class `moment` of lint (case
  613.1); and one whose `method` waits for another session — a part that names a later
  session, the next session, a session after another, a session of a sprint, the session
  that closes one, the librarian or `/hi`, and not the person — by
  `lint.waits_for_another_session`, the one predicate, which lint does not run over the live
  pages (case 670.4), but a part that opens with `after`, or with `by hand, after`, and
  names its event before a colon, which waits for that event, judged by
  `lint.waits_for_an_event` through `lint.waits_for_another_session` (case 781); and an
  `update` of an Estimate that replaces its Criterion whole, writes no `method`, sets no
  status of `passed` or `failed` and keeps a `method` on the live page that waits for
  another session, by the same predicate (`kept_method_waits`) (case 715). An Estimate of a
  sprint page `entity-sprint-<id>` — the `ref` of a `create`, the target of an `update` by
  `estimate_target`, the `target` of the live page — gives neither line: the Definition of
  done of a sprint may wait for a later session of it, up to the one that closes it, judged
  by `ledger.is_sprint_page` (cases 772.4, 772.5);
- a condition of a schema not met (case 714): a `create` whose page, as `generate` writes
  it, or an `update` whose `set` gives the value a condition starts on, leaves the page
  without a field or a section the condition requires, by `lint.unmet_conditions`, the one
  judgment `guppi check` reports by; the page is judged as the plan leaves it, with the
  fields and the sections of each earlier item of the plan on it; a `defer`, a `delete` and
  a category with no schema or one whose schema rule the session changes are not judged
  (`check_conditions`);
- a `create` item that lacks a field `materialize` would name under `incomplete` (case
  748.2): one finding per field, by `materialize.create_lacks`, the one judgment the lift
  marks by, `type` filled from the category first, so a missing `type` is none, and the
  tags present when the item or its decision line carries them; a missing `method` of an
  Estimate is the finding of its form alone, and a `defer`, an `update` and a `delete` are
  not judged (`check_required`);
- an item writing a `sections: Render` for a page that enforces by render whose text does
  not open with `<!-- slug -->` and close with `<!-- /slug -->`; only the text the item
  itself writes is judged, and a child's marker line in a parent is not (case 325.1);
- a `replace` anchor of any Case of the plan that misses, or hits more than once, once the
  pairs are applied in entry order to copies of the pages in memory by `generate`'s own
  matching rule, and a `reword` pair no live page holds: the anchor is judged against the
  page as the Spec leaves it, not as it stands today, and nothing is written (case 351);
- a code fence a `replace` or `reword` pair breaks — a line inside a fence with a full run
  and text after it, or a fence open at the end of the section — judged by `fence_breaks`
  of `.guppi/guppi/materialize.py` on each section the pair changes, before and after it, a break
  the section held before not counted; and each such break in the text of a `sections`
  value of a `create` or an `update`, judged on its own (case 487.1);
- a `replace` pair whose `new` opens with a space or a tab while its `old` opens with
  neither, by `generate.indent_added_twice`: the page keeps its own indent before the
  match, and the indent of `new` would stand after it (case 543.4);
- two Cases of the plan whose `update` items name one page and set one field under `set`
  to two different values, each write one section under `sections`, or each replace the
  Criterion of one Estimate whole — an `update` that names no part, by
  `materialize.names_a_part` — with both Cases, the page's slug and the field or the
  section, the line opening with the later Case; two items of one Case, and different
  fields, sections or anchors of one page, are no such finding
  (`check_same_target`) (case 561.4);
- a record line of the window — `- decision[`, `- estimate[`, `- lesson[`, timed — that
  `materialize.parse_line` does not read, with its date and line number (case 75.2);
- a `[[slug]]` outside a code span in the plan — in the blockquotes and in the strings of
  the `then` blocks, never in a fence with another tag — that names neither a live or
  archived page, nor a slug a `create` of the same plan carries, nor a hub file of `wiki/`;
  one line per slug and Case (case 264.2);
- a `tasks` line that opens with the bare word `render` or `sprint`, or with the command
  outside a code span — the tickers of `render` and `sprint` match the command in the
  first code span (case 235), a line of another form stays debt (case 279.2);
- a `replace` pair of an Estimate `update` whose `old` stands inside the page's
  `## Criterion`, by `materialize.touches_criterion`, the one predicate — a Criterion
  changes only whole (case 378.4);
- the frame (case 378.7): a slug or path in a code span of a Case's `when` or `then` that
  its `given` — its own or its parent's, by `materialize.case_texts` — does not name, and a
  slug of its `then` block the `given` does not name; a slug is a span with a category
  prefix by `materialize.category_of`, a path a span holding a `/` and one more character;
  a Case without `given` is not checked;
- the language (cases 387.4, 445.4, 476.3): every name, `context` or `problem` of a Case of
  the plan that still holds a letter outside the script of the documentation language,
  `documentation_lang`, read from
  `guppi.toml` by `config.read_settings`, a short form under `## Deferred` included, by
  `ratified.untranslated`; a Latin letter in a code span gives no finding, a letter of any
  other script there is judged as in prose (case 589.1); a `guppi.toml` that is missing or
  names an unknown code is one finding that names it; the `given`, `when`, `then` and the
  blocks are not read, and the
  plan is compared with no other file — the ratified copy is gone (case 445.2);
- a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by
  its id — that stands outside a bracket of its own in the new text an item writes for a
  page with `core: true`, on the live page or as the plan leaves it: the `new` of a
  `replace` pair, a `sections` value, a `purpose` or a `method`, never the `change` line nor
  the `context`, `problem` or `recommend` of a Case; a pointer in such a bracket, a code span
  or a fenced block is none. An Estimate whose target — the `ref` of a `create`, else the
  `target` of its live page — carries `core: true`, by `core_as_left` over the item of the plan
  that writes the target, else over its live page (`core_target`), is judged the same, its new
  `## Criterion` included: the one under its `sections`, else the `when` and `then` of its
  Case, for a `create` and an `update` that names no part, read by `new_criterion`, the one
  reading the note on a Criterion line not carried takes too (case 823.6). The judgment is
  `outside` of `.guppi/guppi/pointers.py`, imported, the one `guppi ship` refuses by, and the
  finding names the Case, the page and the pointer (`check_pointers`) (cases 807.4, 820.6).
  `plan_findings` alone runs it, not the check after a write.

The check after a write (case 414.1): `written_findings` runs the same checks, `judge`, for
the `Stop` hook of `rule-spec-write` on the Cases it wrote, with the decision lines of the
reply added, and without the Frontier, the language finding and the grammar of the window.

Notes (case 378.8): a Case whose `given` or `then` holds more than seven `**＋**` lines —
a sign it is not atomic — is one line opening with `note:`, answered in the chat. The notes
of the promise lines (cases 472.1, 472.2), `promise_notes`, which the check of the answer of
`case-guppi` imports: each line of the `## Criterion` of an Estimate that a Case replaces
whole — an `update` that names no part, by `materialize.names_a_part` — which no line of the
new Criterion equals, the operand, the labels `When:`, `Then:`, `Given:` and whitespace set
aside; the new Criterion is the one the item writes under `sections`, else the `when` and
`then` of its Case, and a Case that gives none is not compared. And each pair of `then`
lines of two sibling sub-cases whose shared words — runs of four or more letters and digits,
case set aside — make 60 percent or more of the words of the shorter line, named on the
later sibling. And, by `defer_notes`, one note per page and pair of Cases where a `create`,
`update` or `delete` item of one Case and a `defer` item of another top-level Case name the
same page, a short Case under `## Deferred` included; a change and a defer inside one
top-level Case give none (case 726.1). `plan_findings` alone prints it: the check of the
answer of `case-guppi` imports `promise_notes`, not this one. And, by `cascade_notes`, one
note per `update` item of a page that the cascade of `guppi generate` archives once the
items of the plan and the `{supersedes:case N}` marks of the window apply, and would not
archive before them — a `clustered` lesson of an Insight set `actioned`, an `open` Insight
left with no live child, the Decision page of a superseded Case — judged by
`generate.archived_by_cascade`, the function the cascade calls; the note names the Case
whose item or mark sets off the archive, which may be the Case of the `update` itself or a
sibling sub-case (case 739.1). The check of the file of a Case in `.guppi/guppi/casecheck.py`
imports it.

The sentence of a pair (cases 711.2, 711.3). `check_pairs` records the span each pair writes
into a section, with its Case. Given the Cases of an answer of `case-guppi` as `own`, it
gives a note when a pair of `own` changes a sentence — by `sentence_around`, to a full stop
that a space and a capital letter follow or to the end of the paragraph — into which a pair
of another Case wrote, and it traces, for each match of a pair of `own`, the sentence around
it cut into the parts the pairs wrote and the rest. The check of the file of a Case in
`.guppi/guppi/casecheck.py` passes `own`; `--check` does not, so it prints no such note.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi import config, ratified
from guppi.box import conserved_spec_named
from guppi.event import project_root, read_payload, session_stamp
from guppi.generate import (  # the ticker, the pairs, the Frontier line (case 360)
    DECISION_PREFIX,
    FRONTIER_LINE,
    FRONTIER_SEPARATOR,
    INITIAL_STATUS,
    READ_LINE,
    RESULT,
    Vault,
    archived_by_cascade,
    as_list,
    indent_added_twice,
    replace_hits,
    replace_once,
    reword_pattern,
)
from guppi.ledger import (
    hi_moment,
    hi_recorded,
    is_sprint_page,
    plan_path,
    session_dir,
    session_event_logs,
)
from guppi.lint import (
    CODE_SPAN,
    WIKILINK,
    archived_slugs,
    holds,
    hub_files,
    load_schema,
    method_of,
    names_a_form,
    names_a_moc_form,
    tied_to_a_one_off_moment,
    unmet_conditions,
    waits_for_another_session,
)
from guppi.materialize import (
    DECISION_KINDS,
    SINGULAR,
    case_texts,
    category_of,
    create_fields,
    create_lacks,
    criterion_text,
    defer_writes_no_page,
    fence_breaks,
    fenced_lines,
    find_item,
    in_family,
    item_keys,
    names_a_part,
    parse_line,
    quoted_sections,
    schema_changed,
    schema_fields,
    split_cases,
    tagged_blocks,
    then_blocks,
    touches_criterion,
)
from guppi.pages import (
    CATEGORIES,
    HISTORY,
    Page,
    is_core,
    read_category,
    read_page,
    wiki_root,
)
from guppi.pointers import outside  # the one judgment of a pointer, shared with ship (case 820.6)

TOOL = "ExitPlanMode"
TIMED_RECORD = re.compile(r"^- (\d\d:\d\d:\d\d) (decision|estimate|lesson)\[")
LEAF_CATEGORIES = ("rules", "entities")
LINE_PREVIEW = 80
# `ratification.md` writes the line as `decision[case_id]…`; `parse_line` reads `[case N]`.
# A bare id is read as the same line rather than skipped (the lines of 2026-09-12).
BARE_CASE = re.compile(r"^(- (?:\d\d:\d\d:\d\d )?decision\[)(?!case )")
# the lists whose open lines are no finding: Work waits for Work Mode (case 356.1), Ask for
# the person at `/hi` (case 531.12)
OPEN_LISTS = ("## Work", "## Ask")
# The closers of a Frontier line (case 451.2): `[x]` ends an item — `case N`, `work`; `[-]`
# puts it off — `defer` after the source `sprint`, `kept` after `backlog`, `defer case N`.
CLOSERS = re.compile(r"^(work|defer|kept|case (\S+)|defer case (\S+))$")
WORK, DEFER, KEPT = "work", "defer", "kept"
SPRINT_SOURCE = "sprint"
BACKLOG_SOURCE = "backlog"
# the source each closer with no Case is clean after
PUT_OFF_SOURCE = {DEFER: SPRINT_SOURCE, KEPT: BACKLOG_SOURCE}
PUT_OFF_CLOSER = {source: closer for closer, source in PUT_OFF_SOURCE.items()}
# A task line the tickers of `render` and `sprint` would not match — the bare word, or the
# command outside a code span, right after the box (case 279.2), with `--project .guppi` after
# `uv run` or without it (case 819.1).
OFF_FORM_LINE = re.compile(
    r"^- \[[ x]\] (?:uv run (?:--project \.guppi )?)?(?:guppi )?(?:render|sprint)\b"
)
AND = "**＋**"  # the operand "and" at the head of a line (case 378.6)
LONG_CHAIN = 7  # more `＋` lines than this in `given` or `then` is a note (case 378.8)
OPERAND_HEAD = re.compile(r"^\*\*[＋－]\*\*\s*")  # the operand a Criterion line opens with
LABEL_HEAD = re.compile(r"^(?:When|Then|Given):\s*")  # the labels of a Criterion (case 472.1)
WORD = re.compile(r"[^\W_]{4,}")  # a word of the sibling comparison (case 472.2)
SIBLING_SHARE = 0.6  # the share of the shorter line's words two sibling lines hold in common
NOTE_CASE = re.compile(r"^note: case (\S+?):")


def window(event_log: str, stamp: str) -> tuple[bool, bool]:
    """`(hi, prespec)`: whether the log holds a `hi` of this session's stamp, and a `prespec`
    of the same stamp after it (case 136.2). A mark of another stamp or `--------` does not
    count, and a `session-start` of another session resets nothing: the marks bind by stamp,
    not by position. The `prespec` line is found by `prespec_mark`, the one reading of it."""
    seen_hi = any(
        len(parts) == 4
        and parts[0] == "-"
        and parts[2] == stamp
        and parts[3].split(" ", 1)[0] == "hi"
        for parts in (line.split(" ", 3) for line in event_log.splitlines())
    )
    return seen_hi, prespec_mark([("", event_log)], stamp) is not None


def prespec_mark(logs: list[tuple[str, str]], stamp: str) -> tuple[str, str] | None:
    """`(date, time)` of the last `prespec` line of this session's stamp after its first
    `hi`, over the `(date, text)` event logs in date order; None when none stands (cases
    136.2, 686.1). The one reading of the line: `window` finds it through this function, and
    `guppi onward --plan` reads its time to tell the loop after the findings from its end."""
    seen_hi = False
    mark = None
    for day, text in logs:
        for line in text.splitlines():
            parts = line.split(" ", 3)
            if len(parts) < 4 or parts[0] != "-" or parts[2] != stamp:
                continue
            event = parts[3].split(" ", 1)[0]
            if event == "hi":
                seen_hi = True
            elif event == "prespec" and seen_hi:
                mark = (day, parts[1])
    return mark


# --- the session's window -------------------------------------------------------------


NO_SESSION = "prespec: no session id; pass --session <stamp> from the hi: line"


def resolve_session(option: str | None) -> str | None:
    """The stamp of `--session`, else of `CLAUDE_SESSION_ID`; None with neither. The last
    `session-start` of today's log is no fallback: a foreign start beside a parallel
    session, none after midnight — the session is never guessed (case 213.1)."""
    if option:
        return session_stamp(option, {})
    env = os.environ.get("CLAUDE_SESSION_ID")
    if env:
        return session_stamp(env, {})
    return None


def window_lines(project_dir: Path, hi: tuple[str, str], today: str) -> list[tuple]:
    """`(unit, line number, line)` of every timed record line of the session's window: the
    session's own ledger `raw/<hi date>/<hi HHMM>/ledger.md` whole (case 103.4), then the
    date-level ledgers from the `hi` date to today, on the `hi` date from the `hi` time on,
    while any exist. A line before the `hi` in a date-level ledger, or without a time, is
    not read. `unit` is `<date>/<HHMM>` or `<date>`, so `raw/<unit>/ledger.md` names the
    file."""
    hi_date, hi_time = hi
    raw = project_dir / "vault" / "raw"
    lines: list[tuple] = []
    session = raw / hi_date / (hi_time[:2] + hi_time[3:5]) / "ledger.md"
    if session.exists():
        for number, line in enumerate(session.read_text(encoding="utf-8").splitlines(), 1):
            if TIMED_RECORD.match(line):
                lines.append((f"{hi_date}/{session.parent.name}", number, line))
    folders = sorted(d for d in raw.iterdir() if d.is_dir()) if raw.is_dir() else []
    for folder in folders:
        day = folder.name
        path = folder / "ledger.md"
        if day < hi_date or day > today or not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = TIMED_RECORD.match(line)
            if not match or (day == hi_date and match.group(1) < hi_time):
                continue
            lines.append((day, number, line))
    return lines


def session_decisions(lines: list[tuple]) -> list[dict]:
    """The decision records among the window's lines; a bare case id is read as `case N`
    and the grammar check (case 75.2) reports it."""
    records: list[dict] = []
    for _, _, line in lines:
        if TIMED_RECORD.match(line).group(2) != "decision":
            continue
        record = parse_line(BARE_CASE.sub(r"\1case ", line))
        if record is not None:
            records.append(record)
    return records


def check_grammar(lines: list[tuple]) -> list[str]:
    """Every record line of the window goes through `materialize.parse_line`; one
    that returns None is a finding with its file and line number (case 75.2)."""
    findings: list[str] = []
    for day, number, line in lines:
        if parse_line(line) is None:
            text = line.strip()[:LINE_PREVIEW]
            findings.append(f"raw/{day}/ledger.md:{number}: does not parse: {text}")
    return findings


# --- the plan ---------------------------------------------------------------------------


def items_of(block: dict) -> list[dict]:
    """Every decision item of a `then` block as `{kind, slug, file, nested}`; a nested
    `estimate` of a create is a create item with `nested` set, covered by its parent's
    line: a Leaf's Estimate has no line of its own (case 72.5); `new_tags` are not items."""
    items: list[dict] = []
    for kind in DECISION_KINDS:
        for item in block.get(kind) or []:
            if not isinstance(item, dict):
                continue
            items.append(
                {"kind": kind, "slug": item.get("slug"), "file": item.get("file"), "nested": False}
            )
            nested = item.get("estimate") if kind == "create" else None
            if isinstance(nested, dict) and nested.get("slug"):
                items.append(
                    {"kind": "create", "slug": nested["slug"], "file": None, "nested": True}
                )
    return items


def same_path(a, b) -> bool:
    if not a or not b:
        return False
    norm = [str(p).replace("\\", "/").removeprefix("./") for p in (a, b)]
    return norm[0] == norm[1]


def item_name(entry: dict) -> str:
    return str(entry["slug"] or entry["file"] or "?")


def line_has_item(block: dict, record: dict) -> bool:
    return find_item(block, record["kind"], record["slug"])[0] is not None


def item_has_line(entry: dict, records: list[dict]) -> bool:
    for record in records:
        if record["kind"] != entry["kind"]:
            continue
        if entry["slug"] and record["slug"] == entry["slug"]:
            return True
    return False


def superseded_in_window(records: list[dict]) -> dict[str, str]:
    """The Cases a `{supersedes:case N}` of the window names, each with the Case that
    superseded it — a Case superseded in its own session leaves the plan (case 299.2)."""
    by: dict[str, str] = {}
    for record in records:
        for earlier in record.get("supersedes") or []:  # one block per Case (case 429)
            by.setdefault(str(earlier), str(record["case"]))
    return by


def retired_by(case: str, superseded: dict[str, str]) -> str | None:
    """The Case whose `{supersedes:case N}` covers `case` — N itself or a sub-case of N at
    any depth, judged by `materialize.in_family`, the reading the Spec hook and `materialize`
    share (case 660.1); None when no tag of the window covers it."""
    for top, by in superseded.items():
        if in_family(str(case), top):
            return by
    return None


def retired_whole(case: str, superseded: dict[str, str], records: list[dict]) -> bool:
    """Whether the Case `case` is retired whole: `retired_by` covers it, or it covers each
    sub-case of it among the decision `records`, at least one standing there. Marks that
    retire some sub-cases, not each one with a decision line, leave it standing.
    `guppi onward --plan` imports it, so a Case replaced under a new number, whole or sub-case
    by sub-case, does not keep that hook silent (case 696.1)."""
    if retired_by(case, superseded) is not None:
        return True
    subs = {str(r["case"]) for r in records if in_family(str(r["case"]), case)} - {case}
    return bool(subs) and all(retired_by(sub, superseded) is not None for sub in subs)


def check_lines(cases: dict, blocks: dict, records: list[dict]) -> list[str]:
    """Every line has its item under its own Case; every item has its line, a nested
    estimate through its parent's create line (case 59.1). A Case superseded by a line of the
    window needs no item, and its heading still in the plan is a finding (case 299.2). A second
    item of one kind and slug under one Case heading, in one fence tagged `then` or in
    another, is a finding — one decision line covers one item, and `materialize` lifts only
    the first (case 426)."""
    findings: list[str] = []
    superseded = superseded_in_window(records)
    for case in cases:  # a sub-case of a superseded Case too (case 660.1)
        by = retired_by(case, superseded)
        if by is not None:
            findings.append(f"case {case}: superseded by case {by}, still in the plan")
    for record in records:
        case, tag = record["case"], f"[{record['kind']}][{record['slug']}]"
        if retired_by(case, superseded) is not None:  # its work stands under the superseding Case
            continue
        if case not in cases:
            findings.append(f"case {case}: line {tag}: no Case {case} heading in the plan")
        elif not line_has_item(blocks[case], record):
            findings.append(f"case {case}: line {tag} has no item in the plan")
    for case, block in blocks.items():
        of_case = [r for r in records if r["case"] == case]
        seen: set[tuple[str, str]] = set()
        for entry in items_of(block):
            tag = (entry["kind"], item_name(entry))
            if not entry["nested"] and tag in seen:  # materialize lifts only the first (case 426)
                findings.append(
                    f"case {case}: item [{tag[0]}][{tag[1]}] stands twice — one entry per target"
                )
                continue
            seen.add(tag)
            if not entry["nested"] and not item_has_line(entry, of_case):
                findings.append(
                    f"case {case}: item [{entry['kind']}][{item_name(entry)}] has no decision line"
                )
    return findings


def updates_the_sprint(blocks: dict, case: str) -> bool:
    """An `update` of the sprint page `entity-sprint-<id>` under Case N — the parent or
    any of its sub-cases (case 314.2)."""
    for key, block in blocks.items():
        if key != case and not key.startswith(f"{case}."):
            continue
        for item in (block or {}).get("update") or []:
            if isinstance(item, dict) and is_sprint_page(item.get("slug")):
                return True
    return False


DECISION_PAGE = "decision-case-"


def deferred_pages(title: str, project_dir: Path) -> dict[str, list[str]]:
    """Each live page the title of a Frontier line names in a code span that carries
    `deferred_by`, with the ids of the Cases there — `decision-case-M` read as `M` (case 467).
    A page without `deferred_by` — an open Insight, a note of the sprint page — is left out."""
    pages: dict[str, list[str]] = {}
    for span in CODE_SPAN.findall(title):
        slug = span.strip("`").strip()
        category = category_of(slug)
        path = wiki_root(project_dir) / category / f"{slug}.md" if category else None
        if path is None or not path.exists():
            continue
        deferred = read_page(path, category).props.get("deferred_by") or []
        ids = [str(d).removeprefix(DECISION_PAGE) for d in as_list(deferred)]
        if ids:
            pages[slug] = ids
    return pages


def decided_on_its_page(
    slug: str, deferred: list[str], records: list[dict], case: str
) -> tuple[bool, list[str]]:
    """The one judgment of a backlog item taken up by Case N, run by `/pre-spec` on a
    closed line (case 467.1) and by the check of the answer of `case-guppi` on an open one
    (case 467.2) (case 467). Of `records`, only the decision lines of Case N and its sub-cases are read.
    Returns whether a line of them other than a `defer` names the page, and each Case M of
    the page's `deferred_by` for which no Case among them both names the page on such a line
    and carries `{supersedes:case M}` — `generate` clears a defer only from the pages the
    superseding Case names (case 467.3)."""
    ours = [r for r in records if str(r["case"]) == case or str(r["case"]).startswith(f"{case}.")]
    naming = {str(r["case"]) for r in ours if r["slug"] == slug and r["kind"] != "defer"}
    carried: dict[str, set[str]] = {}
    for record in ours:
        marks = {str(s) for s in record.get("supersedes") or []}
        carried.setdefault(str(record["case"]), set()).update(marks)
    missing = [m for m in deferred if not any(m in carried.get(c, set()) for c in naming)]
    return bool(naming), missing


def check_backlog_line(
    item: str, title: str, case: str, records: list[dict], project_dir: Path
) -> list[str]:
    """A Frontier line of the source `backlog` closed `[x] · case N` (case 467.1)."""
    findings: list[str] = []
    for slug, deferred in deferred_pages(title, project_dir).items():
        named, missing = decided_on_its_page(slug, deferred, records, case)
        if not named:
            findings.append(
                f"frontier: {item} closes a backlog item with case {case}, and no decision "
                f"line of Case {case} other than a defer names {slug}; generate clears a "
                "defer only from a page the Case names"
            )
        for m in missing:
            findings.append(
                f"frontier: {item}: no Case among case {case} and its sub-cases names {slug} "
                f"and carries {{supersedes:case {m}}}"
            )
    return findings


def open_case_items(frontier: str) -> list[str]:
    """The items of the open box lines of a Frontier that may not stay open: a `- [ ]` line
    outside `## Work` and `## Ask` (cases 356.1, 531.12). The one judgment of an open Case
    line, which `check_frontier` reports and the hook of `rule-prespec-onward` waits on
    (case 561.5)."""
    items: list[str] = []
    may_stay_open = False
    for line in frontier.splitlines():
        if line.startswith("## "):
            may_stay_open = line.strip() in OPEN_LISTS
            continue
        match = FRONTIER_LINE.match(line)
        if match and match.group(1) == " " and not may_stay_open:
            items.append(match.group(2))
    return items


def conserved_blocks(plan: str, project_dir: Path | None) -> dict[str, dict]:
    """Case id → the merged `then` block of each Case of the conserved Spec whose `spec.md`
    the title line of the plan names, the folder found by `conserved_spec_named` of
    `.guppi/guppi/box.py` (case 620.2); empty for a plan whose title line names no folder holding
    `carry.md`."""
    if project_dir is None:
        return {}
    folder = conserved_spec_named(plan, project_dir)
    spec = folder / "spec.md" if folder is not None else None
    if spec is None or not spec.is_file():
        return {}
    cases = split_cases(spec.read_text(encoding="utf-8"))
    return {case: then_blocks(lines)[0] for case, lines in cases.items()}


def has_defer_item(blocks: dict, case: str) -> bool:
    """Whether the merged `then` block of Case `case` holds a `defer` item."""
    defers = blocks.get(case, {}).get("defer") or []
    return any(isinstance(d, dict) for d in defers)


def check_frontier(
    path: Path,
    relative: str,
    cases: dict,
    blocks: dict,
    records: list[dict] | None = None,
    project_dir: Path | None = None,
    plan: str = "",
) -> list[str]:
    """The frontier of the session's folder (cases 59.2, 73.4). An open line under `## Cases` is
    a finding (case 356.1), one under `## Work` is not — its work waits for Work Mode — nor
    one under `## Ask`, which waits for the person at `/hi` (case 531.12); a closed one is
    checked as any. Only a box line, `- [ ]`, `- [x]` or `- [-]` at the start,
    is read: `Backlog: N items` and an indented `- near` line are not (case 451.2).

    The closer, the last segment after ` · `, is one of `case N`, `work`, `defer`, `kept`
    and `defer case N`, and the box agrees with it both ways — `[x]`, an item ended, takes
    only `case N` or `work`; `[-]`, an item put off, only `defer`, `kept` or
    `defer case N` (case 451.2). The source is the segment standing immediately before the
    closer; the word inside the slug of a title is not the source (case 335). `defer` alone
    is clean only after the source `sprint`, a sprint item left for a later session, and
    `kept` only after the source `backlog`, an item of `backlog.md` left as it stands.
    `defer case N` after the source `sprint` or `backlog` is a finding — neither is deferred
    by a Case (case 356.2) — and after another source it needs a `defer` item under Case N, in the
    plan or in the conserved Spec that the title line of `plan` names, a Case of the Spec
    the session runs by `/box` (case 620.2); a title line that names no folder holding
    `carry.md` adds no Case. A line
    closed `case N` needs the heading of Case N in the plan, and after the source `sprint`
    an `update` of the sprint page `entity-sprint-<id>` under Case N, the parent or a
    sub-case (cases 314.2, 451.3). A finding of the box and one of the source are separate.
    A line of the source `backlog` closed `case N` is judged by `check_backlog_line`
    against `records` and the pages of `project_dir` (case 467.1)."""
    if not path.exists():
        return [f"frontier: {relative} is missing"]
    text = path.read_text(encoding="utf-8")
    findings = [f"frontier: {item} is open" for item in open_case_items(text)]
    conserved: dict[str, dict] | None = None  # read once, at the first `defer case N` it needs
    for line in text.splitlines():
        match = FRONTIER_LINE.match(line)
        if not match:
            continue
        box, item, rest = match.groups()
        if box == " ":
            continue
        segments = [s.strip() for s in rest.split(FRONTIER_SEPARATOR)]
        closer = CLOSERS.match(segments[-1])
        if closer is None:
            findings.append(
                f"frontier: {item} is closed without case N, work, defer, kept or defer case N"
            )
            continue
        word = closer.group(1)
        source = segments[-2] if len(segments) > 1 else ""
        ended = closer.group(2) is not None or word == WORK
        if box == "x" and not ended:
            findings.append(f"frontier: {item} closes [x] with {word}; an item put off is [-]")
        elif box == "-" and ended:
            findings.append(f"frontier: {item} closes [-] with {word}; an item ended is [x]")
        if word in PUT_OFF_SOURCE:
            if source != PUT_OFF_SOURCE[word]:
                findings.append(
                    f"frontier: {item} closes with {word}; only an item of the source "
                    f"{PUT_OFF_SOURCE[word]} closes with {word}"
                )
        elif closer.group(2) is not None:
            case = closer.group(2)
            if case not in cases:
                findings.append(
                    f"frontier: {item} closes with case {case}, no Case {case} heading in the plan"
                )
            elif source == SPRINT_SOURCE and not updates_the_sprint(blocks, case):
                findings.append(
                    f"frontier: {item} closes a sprint item with case {case}, "
                    f"no update of the sprint page under Case {case}"
                )
            elif source == BACKLOG_SOURCE and box == "x" and project_dir is not None:
                findings += check_backlog_line(item, rest, case, records or [], project_dir)
        elif closer.group(3) is not None and source in PUT_OFF_CLOSER:
            findings.append(
                f"frontier: {item} defers a {source} item by a Case; a {source} item put off "
                f"closes [-] with {PUT_OFF_CLOSER[source]}"
            )
        elif closer.group(3) is not None:
            case = closer.group(3)
            if has_defer_item(blocks, case):
                continue
            if conserved is None:
                conserved = conserved_blocks(plan, project_dir)
            if not has_defer_item(conserved, case):
                findings.append(
                    f"frontier: {item} defers to case {case}, no defer item under Case {case}"
                )
    return findings


def estimates_to_read(block: dict) -> list[str]:
    """The Estimates a `then` block creates or sets `pending`, by slug. An `update` that
    carries `rename` gives the slug of its `rename`: after `generate` the page lives under
    it, the reading names it, and `tick_read` ticks the read line by it (case 432)."""
    slugs: list[str] = []
    for entry in items_of(block):
        if entry["kind"] == "create" and str(entry["slug"] or "").startswith("estimate-"):
            slugs.append(entry["slug"])
    for item in block.get("update") or []:
        if not isinstance(item, dict) or not str(item.get("slug") or "").startswith("estimate-"):
            continue
        set_fields = item.get("set")
        if isinstance(set_fields, dict) and set_fields.get("status") == "pending":
            slugs.append(str(item.get("rename") or item["slug"]))
    return slugs


def check_tasks(cases: dict, blocks: dict, records: list[dict]) -> list[str]:
    """A ratified Case has a `tasks` block; an Estimate to read has its task line — a
    line `- [ ] read `<slug>`` whose first backticked slug is that Estimate, matched by
    `generate.READ_LINE`, the ticker's own pattern, so the check judges as the ticker ticks
    (case 59.3). A slug named on another Estimate's read line has no line of its own and is a
    finding in its own words; a mention on an `update` line, or on any line that is not a read
    line, is no task line (case 327). A render or sprint line is in the form the tickers match
    (case 279.2)."""
    findings: list[str] = []
    superseded = superseded_in_window(records)  # a superseded Case has no work here (case 299.2)
    with_work = {
        r["case"]
        for r in records
        if r.get("kind") != "defer" and retired_by(r["case"], superseded) is None
    }
    for case, lines in cases.items():
        tasks = "\n".join(tagged_blocks(lines, "tasks"))
        if case in with_work and not tasks:  # a defer-only Case has no work (case 74)
            findings.append(f"case {case}: decision lines and no tasks block")
        read_lines = [line for line in tasks.splitlines() if READ_LINE.match(line)]
        # the Estimates with a read line of their own (case 327)
        of_their_own = {READ_LINE.match(line).group(1) for line in read_lines}
        for slug in estimates_to_read(blocks[case]):
            if slug in of_their_own:
                continue
            if any(slug in line for line in read_lines):
                findings.append(f"case {case}: {slug} is named on another read line, not its own")
            else:
                findings.append(f"case {case}: {slug} has no task line")
        for line in tasks.splitlines():
            if OFF_FORM_LINE.match(line):
                findings.append(f"case {case}: render line off form: {line}")
    return findings


def governed_paths(project_dir: Path) -> dict[str, str]:
    """`governs` path → rule slug, over the live Rule pages."""
    paths: dict[str, str] = {}
    for page in read_category(wiki_root(project_dir), "rules"):
        if page.props.get("status") == "archived":
            continue
        governs = page.props.get("governs")
        for path in governs if isinstance(governs, list) else [governs]:
            if path:
                paths[str(path).replace("\\", "/").removeprefix("./")] = page.slug
    return paths


def check_keys(blocks: dict, project_dir: Path, schema_free: set[str]) -> list[str]:
    """A key of an item that `materialize.item_keys` does not give its kind and category —
    the one judgment the lift and `generate` go by (case 436.2); a `create` or a `defer` of a
    category with no schema file, or of one in `schema_free`, is not judged (case 308.2)."""
    findings: list[str] = []
    for case, block in blocks.items():
        for kind in DECISION_KINDS:
            for item in block.get(kind) or []:
                if not isinstance(item, dict):
                    continue
                slug = str(item.get("slug"))
                accepted = item_keys(kind, category_of(slug), project_dir, schema_free)
                if accepted is None:
                    continue
                findings += [
                    f"case {case}: {kind} {slug}: key {key} is not a key of this item"
                    for key in item
                    if key not in accepted
                ]
    return findings


def check_governed(blocks: dict, governed: dict[str, str]) -> list[str]:
    """An `update` item carrying `file` — the file route is gone (case 320); every file of
    the vault is a page, the Render of a page or a record a script keeps. A path a live
    Rule page governs is named with its rule (case 59.6)."""
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            file = item.get("file") if isinstance(item, dict) else None
            if not file:
                continue
            key = str(file).replace("\\", "/").removeprefix("./")
            rule = governed.get(key)
            by = f", governed by {rule}" if rule else ""
            findings.append(f"case {case}: file {file}{by}; the file route is gone (case 320)")
    return findings


def written_criterion(item: dict) -> bool:
    """Whether the item signs its own Criterion under `sections` (cases 194.1, 204)."""
    sections = item.get("sections")
    return isinstance(sections, dict) and bool(str(sections.get("Criterion") or "").strip())


def live_page(project_dir: Path, slug: str) -> bool:
    category = category_of(slug)
    return bool(category) and (wiki_root(project_dir) / category / f"{slug}.md").exists()


NO_FORM = (
    "method names no form — a make target, pytest, a test path, guppi test, guppi check, "
    'guppi style or "by hand"'
)
MOC_NO_FORM = "method of a MOC's Estimate names no make target or test files and is not a reading"
MOMENT = (
    "method ties its reading by hand to the first moment after the render or the change — "
    "the method names the kind of its moment"
)
WAITS = "method waits for another session — a method holds only what runs in its own session"
KEPT_WAITS = (
    "the method on the page waits for another session — set a method that runs in this session"
)
# a defer of an Estimate with no page (case 783)
NO_DEFERRED_ESTIMATE = "no such Estimate page — defer the page it would check"
# a defer of another kind needs a page that stands (case 786)
NO_DEFERRED_PAGE = "no such page — a placeholder is written only for a rule or an entity"
DECIDED = ("passed", "failed")  # a status the person's decision sets, with no reading after it


SENTENCE_STOP = re.compile(r"\.[ \t\n]+(?=[A-ZА-ЯЁ])")  # a full stop, a space, a capital


def sentence_around(text: str, start: int, end: int) -> tuple[int, int]:
    """The sentence around the place `start`–`end` of a section's text: back to the last full
    stop before it that a space and a capital letter follow, or to the start of its
    paragraph, and on to the next such full stop or to the end of its paragraph; a paragraph
    ends at a blank line. The one reading of a sentence, which the note of a sentence two
    Cases change and the check of the read share (cases 711.2, 711.3)."""
    head = text.rfind("\n\n", 0, start)
    head = 0 if head < 0 else head + 2
    tail = text.find("\n\n", end)
    tail = len(text) if tail < 0 else tail
    begin, finish = head, tail
    for stop in SENTENCE_STOP.finditer(text, head, tail):
        if stop.end() <= start:
            begin = stop.end()
        elif stop.start() + 1 >= end:
            finish = stop.start() + 1
            break
    return begin, finish


def shift_spans(spans: list[list], start: int, end: int, length: int) -> None:
    """The spans written into one section before, moved for `start`–`end` replaced by a text
    of `length`; a span the replacement overlaps is widened over it."""
    delta = length - (end - start)
    for span in spans:
        if span[1] <= start:
            continue
        if span[0] >= end:
            span[0], span[1] = span[0] + delta, span[1] + delta
        else:
            span[0] = min(span[0], start)
            span[1] = max(span[0], span[1] + delta if span[1] > end else start + length)


def sentence_parts(
    text: str, begin: int, finish: int, spans: list[list]
) -> list[tuple[str, str | None]]:
    """The sentence `begin`–`finish` of `text` cut into its parts: each part a pair wrote,
    with its Case, and each part between them, with None."""
    cuts = sorted(
        (max(begin, s), min(finish, e), case) for s, e, case in spans if s < finish and e > begin
    )
    parts: list[tuple[str, str | None]] = []
    at = begin
    for s, e, case in cuts:
        if s > at:
            parts.append((text[at:s], None))
        if e > max(s, at):
            parts.append((text[max(s, at) : e], case))
        at = max(at, e)
    if at < finish:
        parts.append((text[at:finish], None))
    return [(part, case) for part, case in parts if part.strip()]


def shared_sentence_note(case: str, slug: str, other: str, sentence: str) -> str:
    """The note of a pair that changes a sentence another Case's pair wrote into (case
    711.2)."""
    return (
        f"note: case {case}: {slug}: a pair changes a sentence that case {other} changes too: "
        f"{preview(sentence)}: read both new texts side by side, and fix the pair or say in "
        "context why the two fit."
    )


def check_pairs(
    cases: dict,
    blocks: dict,
    project_dir: Path,
    own: set[str] | None = None,
    notes: list[str] | None = None,
    trace: list[dict] | None = None,
) -> list[str]:
    """The `replace` and `reword` pairs of every Case of the plan, applied in entry order to
    copies of the pages in memory by `generate`'s own matching rule — `replace_once`, the
    tokens of the anchor joined by one `\\s+` — and nothing written to disk. A `replace`
    anchor that misses, or hits more than once, is one finding with its Case, the page's slug
    and the opening of its `old`; a `reword` pair no live page holds is one too. The anchor is
    judged against the page as the Spec leaves it, not as it stands today: a pair of a later
    Case sees what an earlier one wrote, which is how the pairs of one Spec collide (314.2
    against 310.6). The meaning of the words in their place is not judged here (case 351).
    Each section a pair changes is judged by `fence_breaks` before and after the pair, and a
    break it adds is one finding; so is a break in the text of a `sections` value of a
    `create` or an `update`, judged on its own and not applied to the copies (case 487.1). A
    `replace` pair whose `new` opens with a space or a tab while its `old` opens with neither
    is one finding too, by `indent_added_twice` of `.guppi/guppi/generate.py`: the page keeps its own
    indent before the match, and the indent of `new` would stand after it (case 543.4).

    The span each pair writes is recorded with its Case, the places found by `replace_hits`
    and `reword_pattern` of `.guppi/guppi/generate.py`, imported (case 711.2). `own`, the Cases of an
    answer of `case-guppi`, with `notes`, a list: a pair of a Case of `own` whose sentence
    around its match, by `sentence_around`, holds a span a pair of a Case outside `own` wrote
    adds one note to `notes`, by `shared_sentence_note`; two pairs of `own`, or two of other
    Cases, give none, and `--check` passes no `own`. With `trace`, a list, each match of a
    pair of a Case of `own` adds `{case, slug, path, parts}`: the page file and the sentence
    around the match as the earlier pairs leave it, cut by `sentence_parts` into the parts a
    pair wrote, with its Case, and the rest, with None — what the check of the read judges
    (case 711.3)."""
    findings: list[str] = []
    pages: dict[str, Page | None] = {}
    every_page = False
    written: dict[tuple[str, str], list[list]] = {}  # (slug, section) → [start, end, case]

    def observe(case: str, page: Page, name: str, start: int, end: int) -> None:
        if own is None or case not in own:
            return
        text = page.sections[name]
        spans = written.get((page.slug, name), [])
        begin, finish = sentence_around(text, start, end)
        if notes is not None:
            others = [
                span[2]
                for span in spans
                if span[0] < finish and span[1] > begin and span[2] not in own
            ]
            for other in dict.fromkeys(others):
                note = shared_sentence_note(case, page.slug, other, text[begin:finish])
                if note not in notes:
                    notes.append(note)
        if trace is not None:
            trace.append(
                {
                    "case": case,
                    "slug": page.slug,
                    "path": page.path,
                    "parts": sentence_parts(text, begin, finish, spans),
                }
            )

    def record(case: str, page: Page, name: str, start: int, end: int, length: int) -> None:
        spans = written.setdefault((page.slug, name), [])
        shift_spans(spans, start, end, length)
        spans.append([start, start + length, case])

    def fence_findings(case: str, slug: str, before: dict[str, dict[str, str]]) -> None:
        for page_slug, sections in before.items():
            page = pages.get(page_slug)
            for name, text in (page.sections if page else {}).items():
                if text == sections.get(name, text):
                    continue
                for kind, line in added_breaks(sections.get(name, ""), text):
                    findings.append(
                        f"case {case}: {page_slug}: {name}: " + fence_break("a pair", kind, line)
                    )

    for case in cases:
        for kind in ("create", "update"):
            for item in blocks.get(case, {}).get(kind) or []:
                values = item.get("sections") if isinstance(item, dict) else None
                for name, text in values.items() if isinstance(values, dict) else []:
                    for broken, line in fence_breaks(str(text or "")):
                        findings.append(
                            f"case {case}: {item.get('slug')}: {name}: "
                            + fence_break("a sections value", broken, line)
                        )

    def load(slug: str) -> Page | None:
        if slug not in pages:
            category = category_of(slug)
            path = wiki_root(project_dir) / category / f"{slug}.md" if category else None
            pages[slug] = read_page(path, category) if path and path.exists() else None
        return pages[slug]

    def load_every() -> None:
        nonlocal every_page
        if every_page:
            return
        for category in CATEGORIES:
            folder = wiki_root(project_dir) / category
            for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
                if path.stem != "schema" and path.stem not in pages:
                    pages[path.stem] = read_page(path, category)
        every_page = True

    for case in cases:
        for item in blocks.get(case, {}).get("update") or []:
            if not isinstance(item, dict):
                continue
            slug = str(item.get("slug") or "")
            for pair in item.get("replace") or []:
                if not isinstance(pair, dict):
                    continue
                old, new = str(pair.get("old") or ""), str(pair.get("new") or "")
                if old and indent_added_twice(old, new):
                    findings.append(
                        f"case {case}: {slug}: a replace pair adds an indent twice — its new "
                        f"opens with a space or a tab and its old with neither: {preview(old)}"
                    )
                page = load(slug)
                if page is None or page.error or not old:
                    continue
                before = {slug: dict(page.sections)}
                found = replace_hits(page, old)
                if len(found) == 1:
                    name, match = found[0]
                    observe(case, page, name, match.start(), match.end())
                    replace_once(page, old, new)
                    record(case, page, name, match.start(), match.end(), len(new))
                    fence_findings(case, slug, before)
                    continue
                hits = len(found)
                what = "is not in the page" if not hits else f"hits {hits} times"
                findings.append(f"case {case}: {slug}: a replace anchor {what}: {preview(old)}")
            for pair in item.get("reword") or []:
                if not isinstance(pair, dict):
                    continue
                old, new = str(pair.get("old") or ""), str(pair.get("new") or "")
                if not old:
                    continue
                load_every()
                before = {s: dict(p.sections) for s, p in pages.items() if p}
                word = reword_pattern(old)
                places = [
                    (page, name, match.start(), match.end())
                    for page in pages.values()
                    if page
                    for name, text in page.sections.items()
                    if name not in (HISTORY, RESULT)
                    for match in word.finditer(text)
                ]
                for page, name, start, end in places:
                    observe(case, page, name, start, end)
                touched = sum(Vault.reword_text(page, old, new) for page in pages.values() if page)
                for page, name, start, end in reversed(places):  # later places first
                    record(case, page, name, start, end, len(new))
                if not touched:
                    findings.append(
                        f"case {case}: {slug}: a reword pair hits no live page: {preview(old)}"
                    )
                fence_findings(case, slug, before)
    return findings


def added_breaks(before: str, after: str) -> list[tuple[str, str]]:
    """The breaks of a fence `after` holds that `before` did not, by `fence_breaks` of
    `.guppi/guppi/materialize.py`, each counted as often as it stands (case 487.1)."""
    held = list(fence_breaks(before))
    added = []
    for found in fence_breaks(after):
        if found in held:
            held.remove(found)
        else:
            added.append(found)
    return added


def fence_break(what: str, kind: str, line: str) -> str:
    """The words of a fence finding: `what` leaves a fence with text after its run, with the
    line, or open at the end of the section (case 487.1)."""
    if kind == "open":
        return f"{what} leaves a code fence open at the end of the section: {preview(line)}"
    return f"{what} leaves a code fence with text after it: {preview(line)}"


def preview(text: str) -> str:
    """The opening of an anchor, whitespace collapsed, for a finding's one line."""
    one_line = " ".join(text.split())
    return one_line if len(one_line) <= LINE_PREVIEW else one_line[:LINE_PREVIEW] + "…"


def enforcement_of(item: dict, kind: str, project_dir: Path) -> str:
    """How the target forces its rule: in a `create` the field stands in the item itself,
    since no page exists yet; in an `update` it is read from the page (case 325.1)."""
    if kind == "create":
        return str(item.get("enforcement") or "")
    slug = str(item.get("slug") or "")
    category = category_of(slug)
    if not category:
        return ""
    path = wiki_root(project_dir) / category / f"{slug}.md"
    if not path.exists():
        return ""
    return str(read_page(path, category).props.get("enforcement") or "")


def check_markers(blocks: dict, project_dir: Path) -> list[str]:
    """An item that writes a `Render` section for a page which enforces by render carries the
    page's own markers: the text opens with `<!-- slug -->` and closes with `<!-- /slug -->`,
    or it is one finding. Only the text the item itself writes is judged — the Spec is not
    simulated in entry order, and a child's marker line inside a parent's Render is not
    checked, since its value is known only once every item is applied (case 325.1)."""
    findings: list[str] = []
    for case, block in blocks.items():
        for kind in ("create", "update"):
            for item in block.get(kind) or []:
                if not isinstance(item, dict):
                    continue
                sections = item.get("sections")
                if not isinstance(sections, dict):
                    continue
                text = str(sections.get("Render") or "").strip()
                slug = str(item.get("slug") or "")
                if not text or not slug:
                    continue
                if enforcement_of(item, kind, project_dir) != "render":
                    continue
                if text.startswith(f"<!-- {slug} -->") and text.endswith(f"<!-- /{slug} -->"):
                    continue
                findings.append(
                    f"case {case}: {kind} {slug}: Render is not wrapped in "
                    f"<!-- {slug} --> … <!-- /{slug} -->"
                )
    return findings


def check_form(blocks: dict, project_dir: Path) -> list[str]:
    """The form of an Estimate item (case 203.1): a Case whose `then` block holds two or
    more Estimate items that set a new Criterion — a `create`, or an `update` that names no
    part of the page by `materialize.names_a_part`, the judgment `materialize` lifts by,
    whether the item writes its Criterion or lifts it — is one promise too many (split it,
    case 472.3); an `update` of an
    Estimate whose page does not exist, and a `create` of an Estimate whose `ref` names
    neither a live rule or entity nor a rule or entity a `create` item of the same plan
    carries (case 221), are each a finding. A `create` of an Estimate, or an `update`
    carrying `set: {method: …}`, whose `method` names none of the forms lint classifies — a
    `make <target>`, the word `pytest`, a test path, one of the commands `guppi test`,
    `guppi check` and `guppi style`, or "by hand" — by `lint.names_a_form`, the one
    predicate, is a finding too (case 820.4); a `create`
    with no `method` at all is the same one, and the existence of the file and of the target
    is left to lint, since the test file is written in Work Mode (case 331). Such a `method`
    that ties its reading by hand to the first moment after the render or the change, by
    `lint.tied_to_a_one_off_moment`, is a finding as well (case 613.1), and so is one that
    waits for another session, by `lint.waits_for_another_session` (case 670.4), but on an
    Estimate whose target is a sprint page, by `ledger.is_sprint_page` (case 772.4); a part
    that opens with `after`, or with `by hand, after`, and names its event before a colon
    waits for that event and is no such finding, judged by `lint.waits_for_an_event` through
    `lint.waits_for_another_session` (case 781). When the
    target of the Estimate is a MOC as the plan leaves it — by `plan_kind` — a `method` that
    names neither a `make <target>`, nor the word `pytest` with a test path, nor "by hand",
    by `lint.names_a_moc_form`, the one predicate `check_method` of lint calls too, is a
    finding in place of the line of no form; whether the Makefile holds the target, whether
    each test file exists and whether the children's Estimates are readings stays with lint
    (cases 733, 820.4). A `defer` with no page by `materialize.defer_writes_no_page`
    — the one judgment, by which `generate` fails such an entry — is a finding, a short Case
    under `## Deferred` included: an Estimate with `NO_DEFERRED_ESTIMATE` (case 783), an
    Insight, a Lesson or a Decision page with `NO_DEFERRED_PAGE`; a `defer` of a rule or an
    entity with no page is not (case 786)."""
    findings: list[str] = []
    created = {  # the rules and entities the plan itself creates (case 221)
        str(item.get("slug"))
        for block in blocks.values()
        for item in block.get("create") or []
        if isinstance(item, dict) and category_of(str(item.get("slug") or "")) in LEAF_CATEGORIES
    }

    def form_finding(target: str, method: str) -> str | None:
        if plan_kind(blocks, target, project_dir) == "MOC":  # the forms of a MOC (case 733)
            return None if names_a_moc_form(method) else MOC_NO_FORM
        return None if names_a_form(method) else NO_FORM  # the forms of a Leaf (case 331)

    for case, block in blocks.items():
        promises = 0
        for item in block.get("create") or []:
            slug = item.get("slug") if isinstance(item, dict) else None
            if not slug or category_of(slug) != "estimates":
                continue
            promises += 1
            ref = str(item.get("ref") or "")
            if category_of(ref) not in LEAF_CATEGORIES or not (
                live_page(project_dir, ref) or ref in created
            ):
                findings.append(f"case {case}: create {slug}: ref {ref or '?'} names no live page")
            if no_form := form_finding(ref, str(item.get("method") or "")):
                findings.append(f"case {case}: create {slug}: {no_form}")
            # a reading tied to a one-off moment (case 613.1)
            if tied_to_a_one_off_moment(str(item.get("method") or "")):
                findings.append(f"case {case}: create {slug}: {MOMENT}")
            if waits_for_another_session(str(item.get("method") or "")) and not is_sprint_page(
                ref
            ):  # a method that waits, off a sprint page (cases 670.4, 772.4)
                findings.append(f"case {case}: create {slug}: {WAITS}")
        for item in block.get("update") or []:
            slug = item.get("slug") if isinstance(item, dict) else None
            if not slug or category_of(slug) != "estimates":
                continue
            set_fields = item.get("set")
            if not names_a_part(item):
                promises += 1
            if not live_page(project_dir, slug):
                findings.append(f"case {case}: update {slug}: no such Estimate page")
            method = set_fields.get("method") if isinstance(set_fields, dict) else None
            if method is not None and (
                no_form := form_finding(estimate_target(item, project_dir), str(method))
            ):
                findings.append(f"case {case}: update {slug}: {no_form}")
            # a reading tied to a one-off moment (case 613.1)
            if method is not None and tied_to_a_one_off_moment(str(method)):
                findings.append(f"case {case}: update {slug}: {MOMENT}")
            if (
                method is not None
                and waits_for_another_session(str(method))
                and not is_sprint_page(estimate_target(item, project_dir))
            ):  # a method that waits, off a sprint page (cases 670.4, 772.4)
                findings.append(f"case {case}: update {slug}: {WAITS}")
            if method is None and kept_method_waits(item, project_dir):  # a kept wait (case 715)
                findings.append(f"case {case}: update {slug}: {KEPT_WAITS}")
        for item in block.get("defer") or []:  # a defer that writes no page (cases 783, 786)
            slug = item.get("slug") if isinstance(item, dict) else None
            category = category_of(slug) if slug else None
            if category and defer_writes_no_page(project_dir, category, slug):
                line = NO_DEFERRED_ESTIMATE if category == "estimates" else NO_DEFERRED_PAGE
                findings.append(f"case {case}: defer {slug}: {line}")
        if promises >= 2:
            findings.append(f"case {case}: two promises in one Case — split it")
    return findings


def plan_kind(blocks: dict, slug: str, project_dir: Path) -> str:
    """The `kind` of a rule or an entity as the plan leaves it — the last `create` of the
    plan that writes `kind`, or `update` whose `set` gives it, else the `kind` of the live
    page; empty when none gives one (case 733)."""
    kind = ""
    for block in blocks.values():
        for item in block.get("create") or []:
            if isinstance(item, dict) and item.get("slug") == slug and item.get("kind"):
                kind = str(item["kind"])
        for item in block.get("update") or []:
            sets = item.get("set") if isinstance(item, dict) else None
            if item.get("slug") == slug and isinstance(sets, dict) and sets.get("kind"):
                kind = str(sets["kind"])
    if kind:
        return kind
    category = category_of(slug)
    path = wiki_root(project_dir) / category / f"{slug}.md"
    if category not in LEAF_CATEGORIES or not path.is_file():
        return ""
    return str(read_page(path, category).props.get("kind") or "")


def estimate_target(item: dict, project_dir: Path) -> str:
    """The target of the Estimate an `update` item names — the `target` its `set` gives,
    else the `target` of the live page; empty when neither gives one (case 733)."""
    sets = item.get("set") if isinstance(item.get("set"), dict) else {}
    if sets.get("target"):
        return str(sets["target"])
    path = wiki_root(project_dir) / "estimates" / f"{item.get('slug')}.md"
    if not path.is_file():
        return ""
    return str(read_page(path, "estimates").props.get("target") or "")


def kept_method_waits(item: dict, project_dir: Path) -> bool:
    """Whether an `update` of an Estimate replaces its Criterion whole — it names no part
    of the page, by `materialize.names_a_part` — writes no `method`, sets no status the
    person's decision gives, `passed` or `failed`, and keeps on the live page a `method`
    that waits for another session, by `lint.waits_for_another_session`, the predicate that
    judges a `method` the plan writes (case 715). The page goes `pending`, and the Retro of
    the Case's own session cannot read it. False when the `target` of the live page is a
    sprint page, by `ledger.is_sprint_page`: its Estimate may wait for a later session of its
    sprint (case 772.5). A part of the kept `method` that opens with `after`, or with `by hand,
    after`, and names its event before a colon waits for that event, and the shared
    predicate passes it by (case 781)."""
    sets = item.get("set") if isinstance(item.get("set"), dict) else {}
    if names_a_part(item) or "method" in sets or str(sets.get("status")) in DECIDED:
        return False
    path = wiki_root(project_dir) / "estimates" / f"{item.get('slug')}.md"
    if not path.is_file():
        return False
    page = read_page(path, "estimates")
    if is_sprint_page(page.props.get("target")):
        return False
    method = method_of(page)
    return method is not None and waits_for_another_session(method)


def created_page(item: dict, category: str, project_dir: Path) -> tuple[dict, set[str]] | None:
    """The fields and the section names of the page a `create` item leaves, as `generate`
    writes it: the fields of the item the category's schema names, `type`, the first
    status, `parent` or `target` from `ref`, the lists a Leaf, a MOC or an Insight is given,
    `origin`, `sprint`, `created`, the tags, the item's sections, `## Purpose` from `purpose`
    on a rule or an entity, and `## History`. None for a category with no schema. A test runs
    `Vault.create` over the same items and asserts the two answer alike (case 714)."""
    known = schema_fields(project_dir, {"category": category})
    if known is None:
        return None
    props = {key: value for key, value in item.items() if key in known}
    props.setdefault("type", SINGULAR[category])
    props["status"] = INITIAL_STATUS.get(category)
    ref = item.get("ref")
    if ref and category in LEAF_CATEGORIES:
        props["parent"] = ref
    if ref and category == "estimates":
        props["target"] = ref
    if category in LEAF_CATEGORIES:
        props.setdefault("estimates", [])
        if props.get("kind") == "MOC":
            props.setdefault("children", [])
    if category == "insights":
        props.setdefault("children", [])
        props["severity"] = len(as_list(props.get("children")))
    props.update(origin="", sprint="", created="")
    if item.get("tags"):
        props["tags"] = list(item["tags"])
    sections = {f"## {name}" for name in item.get("sections") or {}}
    if category in LEAF_CATEGORIES and props.get("purpose"):
        sections.add("## Purpose")
    sections.add(HISTORY)
    return props, sections


def check_required(
    blocks: dict, records: list[dict], project_dir: Path, schema_free: set[str]
) -> list[str]:
    """A `create` item that lacks a field `materialize` would name under `incomplete`, by
    `materialize.create_lacks`, the one judgment the lift marks by: the fields lifted as
    the lift lifts them, `type` filled from the category, the tags counted when the item or
    its decision line carries them (case 748.2). A missing `method` of an Estimate is
    left to `check_form`, which reports it already (case 331); a `defer`, an `update` and a
    `delete` are not judged. The `ref` that saves a `Leaf` rule from lacking `parent` is the
    item's, or that of the decision line of its Case and slug (case 795.2)."""
    tagged = {
        (str(r.get("case")), str(r.get("slug")))
        for r in records
        if r.get("kind") == "create" and r.get("tags")
    }
    refs = {
        (str(r.get("case")), str(r.get("slug"))): str(r["ref"])
        for r in records
        if r.get("kind") == "create" and r.get("ref")
    }
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("create") or []:
            if not isinstance(item, dict):
                continue
            slug = str(item.get("slug") or "")
            category = category_of(slug)
            known = schema_fields(project_dir, {"category": category}, schema_free)
            sections = item.get("sections") if isinstance(item.get("sections"), dict) else {}
            lacks = create_lacks(
                category,
                create_fields(item, known),
                sections,
                bool(item.get("tags")) or (case, slug) in tagged,
                item.get("ref") or refs.get((case, slug)),
            )
            findings += [
                f"case {case}: create {slug}: no {name}, a field materialize requires"
                for name in lacks
                if not (name == "method" and category == "estimates")
            ]
    return findings


def check_conditions(blocks: dict, project_dir: Path, schema_free: set[str]) -> list[str]:
    """A Case that leaves a page short of what a condition of its category's schema
    requires — by `lint.unmet_conditions`, the judgment `guppi check` reports by (case 714). The
    page is judged as the plan leaves it: the live page, or the page a `create` writes by
    `created_page`, with the fields and the section names of each earlier item of the plan
    on the same page. A `create` is a finding for each condition its page does not meet; an
    `update` only for a condition whose `when` its `set` gives, so a Case that does not
    cause a break is not sent back for one the page already holds. A `defer` and a `delete`
    are not judged, nor is a category with no schema or one in `schema_free`, whose schema
    rule the session changes (case 308.2)."""
    wiki = wiki_root(project_dir)
    schemas: dict[str, dict | None] = {}
    pages: dict[str, tuple[dict, set[str]]] = {}  # slug → the page as the plan leaves it
    findings: list[str] = []
    for case, block in blocks.items():
        for kind in ("create", "update"):
            for item in block.get(kind) or []:
                slug = str(item.get("slug") or "") if isinstance(item, dict) else ""
                category = category_of(slug)
                if not category or category in schema_free:
                    continue
                if category not in schemas:
                    schemas[category] = load_schema(wiki, category)
                schema = schemas[category]
                if schema is None:
                    continue
                sets = item.get("set") if isinstance(item.get("set"), dict) else {}
                if kind == "create":
                    page = created_page(item, category, project_dir)
                    if page is None:
                        continue
                    pages[slug] = page
                else:
                    if slug not in pages:
                        path = wiki / category / f"{slug}.md"
                        if not path.is_file():
                            continue
                        live = read_page(path, category)
                        pages[slug] = (dict(live.props), set(live.sections))
                    props, sections = pages[slug]
                    props.update(sets)
                    sections |= {f"## {name}" for name in item.get("sections") or {}}
                props, sections = pages[slug]
                for when, what in unmet_conditions(props, sections, schema):
                    if kind == "update" and not holds(sets, when):
                        continue  # the Case did not start this condition
                    findings.append(f"case {case}: {kind} {slug}: {what}")
    return findings


def core_as_left(item: dict, kind: str, project_dir: Path) -> bool:
    """Whether the page of an item carries `core: true` as the plan leaves it: by the item
    — the field of a `create`, the `set` of an `update` — else on the live page."""
    if kind == "create" and "core" in item:
        return item.get("core") is True
    if isinstance(item.get("set"), dict) and "core" in item["set"]:
        return item["set"]["core"] is True
    slug = str(item.get("slug") or "")
    category = category_of(slug)
    path = wiki_root(project_dir) / category / f"{slug}.md" if category else None
    return bool(path and path.exists() and is_core(read_page(path, category)))


def written_texts(item: dict) -> list[str]:
    """The new text an item writes on its page: the `new` of each `replace` pair, each
    `sections` value, the `purpose` and the `method`, of the item or of its `set`; never its
    `change` line."""
    texts = [str(p.get("new") or "") for p in item.get("replace") or [] if isinstance(p, dict)]
    sections = item.get("sections")
    if isinstance(sections, dict):
        texts += [str(value or "") for value in sections.values()]
    texts += [str(item.get("purpose") or ""), str(item.get("method") or "")]
    if isinstance(item.get("set"), dict):
        texts += [str(item["set"].get(key) or "") for key in ("purpose", "method")]
    return [text for text in texts if text]


def new_criterion(item: dict, kind: str, case: str, cases: dict) -> str:
    """The new `## Criterion` of an Estimate item that writes it whole — a `create`, or an
    `update` that names no part by `materialize.names_a_part`: the Criterion it writes under
    `sections`, else the `when` and `then` of its Case; empty for an `update` that names a part.
    The one reading `criterion_notes` and `check_pointers` share (case 823.6)."""
    if kind == "update" and names_a_part(item):
        return ""
    if written_criterion(item):
        return str(item["sections"]["Criterion"])
    return criterion_text(case_texts(cases, case)) if case in cases else ""


def target_slug(item: dict, kind: str, project_dir: Path) -> str:
    """The slug of the target of an Estimate item: the `ref` of a `create`, else what
    `estimate_target` gives for an `update`; empty when neither stands."""
    raw = item.get("ref") or "" if kind == "create" else estimate_target(item, project_dir)
    return str(raw).strip().strip('"').removeprefix("[[").removesuffix("]]").strip()


def core_target(target: str, blocks: dict, project_dir: Path) -> bool:
    """Whether the target of an Estimate carries `core: true` as the plan leaves it: by
    `core_as_left` over the item of the plan that writes it, else over its live page."""
    for block in blocks.values():
        for kind in ("create", "update"):
            for item in block.get(kind) or []:
                if isinstance(item, dict) and item.get("slug") == target:
                    return core_as_left(item, kind, project_dir)
    return bool(target) and core_as_left({"slug": target}, "update", project_dir)


def check_pointers(blocks: dict, project_dir: Path, cases: dict | None = None) -> list[str]:
    """A pointer to a case, a decision or a session outside a bracket of its own in the new
    text of a page with `core: true`, or of an Estimate whose target carries `core: true` —
    its `method` and its new Criterion, by `new_criterion`, included — by `outside` of
    `.guppi/guppi/pointers.py`, the judgment `guppi ship` removes and refuses by (cases
    807.4, 820.6, 823.6)."""
    cases = cases or {}
    findings: list[str] = []
    for case, block in blocks.items():
        for kind in ("create", "update"):
            for item in block.get(kind) or []:
                if not isinstance(item, dict):
                    continue
                slug = str(item.get("slug") or "")
                texts = written_texts(item)
                if not core_as_left(item, kind, project_dir):
                    if category_of(slug) != "estimates" or not core_target(
                        target_slug(item, kind, project_dir), blocks, project_dir
                    ):
                        continue
                    if not written_criterion(item):
                        texts.append(new_criterion(item, kind, case, cases))
                for text in texts:
                    for _, what in outside(text):
                        findings.append(
                            f"case {case}: {kind} {slug}: a pointer outside a bracket of its "
                            f"own: {what}"
                        )
    return findings


def check_criterion_pairs(blocks: dict, project_dir: Path) -> list[str]:
    """A `replace` pair of an Estimate `update` whose `old` stands inside the page's
    `## Criterion` — judged by `materialize.touches_criterion`, the predicate `materialize`
    marks `incomplete: [criterion]` by; a Criterion changes only whole (case 378.4)."""
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            slug = str(item.get("slug") or "") if isinstance(item, dict) else ""
            if category_of(slug) != "estimates":
                continue
            for pair in item.get("replace") or []:
                if touches_criterion(project_dir, slug, [pair]):
                    findings.append(
                        f"case {case}: update {slug}: a replace pair inside the Criterion — "
                        f"a Criterion changes only whole: {preview(str(pair.get('old') or ''))}"
                    )
    return findings


def check_same_target(blocks: dict) -> list[str]:
    """Two Cases of the plan whose `update` items name one page and set one field
    under `set` to two different values, each write one section under `sections`, or each
    replace the Criterion of one Estimate whole — an `update` that names no part, by
    `materialize.names_a_part` (case 561.4). One finding per pair, opening with the later Case in the
    plan's order, so the check after a write gives it to the Case just written. Two items of
    one Case are not compared here — a second item of one kind and slug keeps the finding of
    `check_lines` (case 426) — and different fields, sections or anchors of one page are no
    finding: their `replace` pairs are judged by `check_pairs`. Its second caller is the check
    of the answer of `case-guppi` at `SubagentStop`, `casecheck.session_clashes`, which runs it
    over the other Cases of the session and the answer's Cases last (case 629.1)."""
    seen: dict[str, list[tuple[str, dict]]] = {}  # slug → (case, item) in plan order
    findings: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            slug = str(item.get("slug") or "") if isinstance(item, dict) else ""
            if not slug:
                continue
            for earlier, other in seen.get(slug, []):
                if earlier == case:
                    continue
                findings += same_target_findings(case, earlier, slug, item, other)
            seen.setdefault(slug, []).append((case, item))
    return findings


def same_target_findings(later: str, earlier: str, slug: str, item: dict, other: dict) -> list[str]:
    """The clashes of two `update` items of one page under two Cases (case 561.4)."""
    findings: list[str] = []
    mine, theirs = item.get("set"), other.get("set")
    if isinstance(mine, dict) and isinstance(theirs, dict):
        for field in mine:
            if field in theirs and json.dumps(mine[field], sort_keys=True, default=str) != (
                json.dumps(theirs[field], sort_keys=True, default=str)
            ):
                findings.append(
                    f"case {later}: {slug}: sets {field} to another value than case {earlier}"
                )
    mine, theirs = item.get("sections"), other.get("sections")
    if isinstance(mine, dict) and isinstance(theirs, dict):
        for name in mine:
            if name in theirs:
                findings.append(
                    f"case {later}: {slug}: writes the section {name} that case {earlier} "
                    "writes too"
                )
    if category_of(slug) == "estimates" and not names_a_part(item) and not names_a_part(other):
        findings.append(
            f"case {later}: {slug}: replaces the Criterion that case {earlier} replaces too — "
            "one promise is signed in one wording"
        )
    return findings


# --- the frame of a Case (cases 378.7, 378.8) ------------------------------------------


def frame_name(span: str) -> bool:
    """Whether a code span names a thing the frame must hold: a slug with a category prefix,
    or a path — a `/` and one more character, a slash command included (case 378.7)."""
    return bool(category_of(span)) or ("/" in span and len(span) > 1)


def item_slugs(block: dict) -> list[str]:
    return [
        str(item["slug"])
        for kind in DECISION_KINDS
        for item in block.get(kind) or []
        if isinstance(item, dict) and item.get("slug")
    ]


def check_frame(cases: dict, blocks: dict) -> list[str]:
    """The `when` and `then` name only what `given` names, and every slug of the `then`
    block stands in `given`; a sub-case reads its parent's `given` by `case_texts`; a Case
    without `given` — a defer, an older Spec — is not checked (case 378.7). One finding per
    name."""
    findings: list[str] = []
    for case in cases:
        texts = case_texts(cases, case)
        given = texts.get("given") or ""
        if not given:
            continue
        named: list[str] = []
        for section in ("when", "then"):
            for span in CODE_SPAN.findall(texts.get(section) or ""):
                name = span.strip("`").strip()
                if frame_name(name) and name not in named:
                    named.append(name)
        for slug in item_slugs(blocks.get(case, {})):
            if slug not in named:
                named.append(slug)
        for name in named:
            if name not in given:
                findings.append(f"case {case}: {name} is not named in its given")
    return findings


def chain_notes(cases: dict) -> list[str]:
    """A Case whose own `given` or `then` holds more than seven `＋` lines — a sign
    it is not atomic; a note, not a finding (case 378.8)."""
    notes: list[str] = []
    for case in cases:
        texts = case_texts(cases, case)
        for section in ("given", "then"):
            count = sum(
                1 for line in (texts.get(section) or "").splitlines() if line.startswith(AND)
            )
            if count > LONG_CHAIN:
                notes.append(
                    f"note: case {case}: {section} holds {count} ＋ lines — is the Case atomic?"
                )
    return notes


# --- the promise lines of a Case (cases 472.1, 472.2) -----------------------------------


def criterion_line(line: str) -> str:
    """A line of a Criterion as compared: its operand, its label and extra whitespace set
    aside (case 472.1)."""
    line = OPERAND_HEAD.sub("", line.strip())
    return " ".join(LABEL_HEAD.sub("", line).split())


def criterion_notes(cases: dict, blocks: dict, project_dir: Path) -> list[str]:
    """Each line of the `## Criterion` of an Estimate that a Case replaces whole — an
    `update` that names no part, by `materialize.names_a_part` — which no line of the new
    Criterion equals; the new one is the Criterion the item writes, else the `when` and `then`
    of its Case, and a Case that gives none is not compared (case 472.1). A `create` has no
    old Criterion."""
    notes: list[str] = []
    for case, block in blocks.items():
        for item in block.get("update") or []:
            slug = str(item.get("slug") or "") if isinstance(item, dict) else ""
            if category_of(slug) != "estimates" or names_a_part(item):
                continue
            path = wiki_root(project_dir) / "estimates" / f"{slug}.md"
            if not path.is_file():
                continue
            new = new_criterion(item, "update", case, cases)
            if not new.strip():
                continue
            carried = {criterion_line(line) for line in new.splitlines()}
            old = read_page(path, "estimates").section("## Criterion") or ""
            for line in old.splitlines():
                key = criterion_line(line)
                if key and key not in carried:
                    notes.append(
                        f"note: case {case}: {slug}: a line of its Criterion is not carried: "
                        f"{preview(key)}"
                    )
    return notes


def words(line: str) -> set[str]:
    return {word.lower() for word in WORD.findall(line)}


def sibling_notes(cases: dict) -> list[str]:
    """Each pair of `then` lines of two sibling sub-cases — of one parent — whose
    shared words make `SIBLING_SHARE` or more of the words of the shorter line, named on the
    later sibling; a line with no word is compared with none, and a Case with no quoted
    `then` — an older Spec — gives no line (case 472.2)."""
    families: dict[str, list[str]] = {}
    for case in cases:
        if "." in case:
            families.setdefault(case.rsplit(".", 1)[0], []).append(case)
    notes: list[str] = []
    for members in families.values():
        lines = {
            case: [
                (line, words(line))
                for line in quoted_sections(cases[case], ("then",)).get("then", "").splitlines()
                if words(line)
            ]
            for case in members
        }
        for index, later in enumerate(members):
            for earlier in members[:index]:
                for line, mine in lines[later]:
                    for other, theirs in lines[earlier]:
                        if len(mine & theirs) >= SIBLING_SHARE * min(len(mine), len(theirs)):
                            notes.append(
                                f"note: case {later}: a then line shares most of its words "
                                f"with case {earlier}: {preview(line)} | {preview(other)}"
                            )
    return notes


def defer_notes(cases: dict) -> list[str]:
    """One note per page and pair of Cases, where a `create`, `update` or `delete`
    item of one Case and a `defer` item of another top-level Case name the same page, a short
    Case under `## Deferred` included; a Case and its sub-cases are one Case here, and a page
    only `defer` items name gives none (case 726.1). A note, not a finding."""
    changes: list[tuple[str, str]] = []
    defers: list[tuple[str, str]] = []
    for case, lines in cases.items():
        block = then_blocks(lines)[0]
        for kind in DECISION_KINDS:
            for item in block.get(kind) or []:
                if isinstance(item, dict) and item.get("slug"):
                    (defers if kind == "defer" else changes).append((case, str(item["slug"])))
    notes: list[str] = []
    for case, slug in changes:
        for other, deferred in defers:
            if deferred != slug or other.split(".")[0] == case.split(".")[0]:
                continue
            note = f"note: case {case}: {slug}: changed while case {other} puts it off"
            if note not in notes:
                notes.append(note)
    return notes


def cascade_notes(
    blocks: dict[str, dict],
    records: list[dict],
    project_dir: Path,
    judged: set[str] | None = None,
) -> list[str]:
    """One note per `update` item of a page that the cascade of `generate` archives
    once the items of `blocks`, in their order, and the `{supersedes:case N}` marks of
    `records` apply, and would not archive before them — judged by
    `generate.archived_by_cascade`, the one function the cascade calls: a lesson standing
    `clustered` among the children of an Insight an item sets `actioned`, an `open` Insight
    whose last live child an item or the cascade archives, and the Decision page of a Case a
    mark names, or of one of its sub-cases (case 739.1). An item reads `set: {status: …}` and `set:
    {children: …}` of an `update`, and a `delete` sets `archived`. The note names the Case of
    the `update`, the page and the Case whose item or mark sets off the archive; an `update`
    and that item in one Case, or in two sub-cases of one, give it too. A `create`, a
    `delete`, a `defer` and a move between `built` and `draft` give none. `judged`: the Cases
    a note must name, as the Case of the `update` or as the Case that sets off the archive,
    every Case of `blocks` when None — the check of the file of a Case passes the Cases of
    the file, so two other Cases give it none. A note, not a finding."""
    wiki = wiki_root(project_dir)
    statuses: dict[str, str] = {}
    children: dict[str, list[str]] = {}
    for page in read_category(wiki, "lessons"):
        statuses[page.slug] = str(page.props.get("status"))
    for page in read_category(wiki, "insights"):
        if not page.error:
            statuses[page.slug] = str(page.props.get("status"))
            children[page.slug] = as_list(page.props.get("children"))
    updates = [
        (case, str(item["slug"]))
        for case, block in blocks.items()
        for item in block.get("update") or []
        if isinstance(item, dict) and item.get("slug")
    ]
    marks = superseded_in_window(records)
    decisions = {slug for _, slug in updates if slug.startswith(DECISION_PREFIX)}
    decisions |= {f"{DECISION_PREFIX}case-{n}" for n in marks}
    for slug in decisions:
        path = wiki / "decisions" / f"{slug}.md"
        if path.exists():
            statuses[slug] = str(read_page(path, "decisions").props.get("status"))
    before = archived_by_cascade(statuses, children)
    cause: dict[str, str] = {}
    for case, block in blocks.items():
        for kind in ("update", "delete"):
            for item in block.get(kind) or []:
                if not isinstance(item, dict) or not item.get("slug"):
                    continue
                slug = str(item["slug"])
                given = item.get("set") if kind == "update" else {"status": "archived"}
                if not isinstance(given, dict):
                    continue
                if "status" in given:
                    statuses[slug] = str(given["status"])
                    cause[slug] = case
                if "children" in given and slug in children:
                    children[slug] = as_list(given["children"])
                    cause[slug] = case
    for slug in decisions:
        number = slug.removeprefix(f"{DECISION_PREFIX}case-")
        by = retired_by(number, marks)
        if by is not None:
            statuses[slug] = "superseded"
            cause[slug] = by
    after = archived_by_cascade(statuses, children) - before

    def trigger(slug: str) -> str | None:
        """The Case whose item or mark sets off the archive of `slug`."""
        if slug.startswith(DECISION_PREFIX):  # the Case of the mark
            return cause.get(slug)
        for insight, kids in children.items():  # a lesson: the Case that actions its Insight
            if slug in kids and statuses.get(insight) == "actioned" and insight in cause:
                return cause[insight]
        for kid in children.get(slug, []):  # an Insight: the Case that archives a child
            if kid in cause and statuses.get(kid) == "archived":
                return cause[kid]
            if kid in after and kid != slug:
                found = trigger(kid)
                if found is not None:
                    return found
        return cause.get(slug)  # an Insight whose `children` an item rewrites

    notes: list[str] = []
    for case, slug in updates:
        by = trigger(slug) if slug in after else None
        if by is None or (judged is not None and not {case, by} & judged):
            continue
        note = (
            f"note: case {case}: {slug}: updated while the cascade archives it after case {by}: "
            "drop the update, or say in its context why it stands"
        )
        if note not in notes:
            notes.append(note)
    return notes


def promise_notes(plan: str, project_dir: Path) -> list[str]:
    """The notes of the promise lines of the plan's Cases (cases 472.1, 472.2) — printed by
    `--check`, and sent back once by the check of the answer of `case-guppi`, which imports
    this function."""
    cases = split_cases(plan)
    blocks = {case: then_blocks(lines)[0] for case, lines in cases.items()}
    return criterion_notes(cases, blocks, project_dir) + sibling_notes(cases)


# --- a bare wikilink in the plan (case 264.2) -------------------------------------------


def plan_prose(lines: list[str]) -> list[str]:
    """The lines of a Case a `[[slug]]` is read from: the ones outside any fence and the
    ones inside a fence tagged `then`; a fence with another tag or none is skipped. The fence
    is judged by `materialize.fenced_lines`, the walk of `tagged_blocks` (case 444.1)."""
    return [
        line
        for line, opening in fenced_lines(lines)
        if line is not None and (opening is None or opening[2] == "then")
    ]


def known_slugs(project_dir: Path) -> set[str]:
    """What a `[[…]]` may name: a live page, an archived page, a hub file (case 149.3)."""
    wiki = wiki_root(project_dir)
    live = {p.stem for category in CATEGORIES for p in (wiki / category).glob("*.md")}
    return live | archived_slugs(wiki) | hub_files(wiki)


def check_bare_links(cases: dict, blocks: dict, project_dir: Path) -> list[str]:
    """A `[[slug]]` outside a code span in the plan — in the blockquotes and in the
    strings of the `then` blocks — that names neither a live or archived page, nor a slug a
    `create` of the same plan carries, nor a hub file of `wiki/`; one line per slug and
    Case (case 264.2). The text would reach a page as it stands, and lint would read it as a broken
    link (cases 130.1, 140, 160, 262)."""
    known = known_slugs(project_dir)
    created = {
        str(item.get("slug"))
        for block in blocks.values()
        for item in block.get("create") or []
        if isinstance(item, dict) and item.get("slug")
    }
    findings: list[str] = []
    for case, lines in cases.items():
        seen: set[str] = set()
        prose = CODE_SPAN.sub("", "\n".join(plan_prose(lines)))
        for slug in WIKILINK.findall(prose):
            slug = slug.strip()
            if slug in known or slug in created or slug in seen:
                continue
            seen.add(slug)
            findings.append(f"case {case}: [[{slug}]] outside a code span names no page")
    return findings


def check_untranslated(plan: str, project_dir: Path) -> list[str]:
    """Every name, `context` or `problem` of a Case of the plan that still holds a letter
    outside the script of the documentation language `guppi.toml` sets, a short form under
    `## Deferred` included, by `ratified.untranslated` (cases 387.4, 445.4, 476.3); a Latin
    letter in a code span gives no finding (case 589.1); a `guppi.toml` that is missing or names a code
    the table does not hold is one finding, and no Case is read. The plan is compared with no
    other file."""
    try:
        language = config.read_settings(project_dir)["documentation_lang"]
    except config.ConfigError as exc:
        return [f"{exc} — the language of the repository is not known; no Case is read"]
    name, script = config.name_of(language), config.script_of(language)
    return [
        f"case {case}: its {part} holds a letter outside the {script} script of {name} — "
        "translate it"
        for case, part in ratified.untranslated(plan, language)
    ]


def judge(
    plan: str,
    project_dir: Path,
    records: list[dict],
    lines: list[tuple] | None = None,
    frontier: tuple[Path, str] | None = None,
    schema_free: set[str] | None = None,
) -> list[str]:
    """The checks of `--check` on the plan's Cases, in the order they print. `lines`, the
    window's record lines, adds their grammar (case 75.2); `frontier`, its path and the name a
    finding gives it, adds the Frontier (case 59.2). The check after a write passes neither, and
    the language finding stays with `check` (cases 414.1, 445.4). `schema_free`: the
    categories whose keys are not judged, by default those `records` change (case 436.2)."""
    if schema_free is None:
        schema_free = schema_changed(records)
    cases = split_cases(plan)
    blocks: dict[str, dict] = {}
    findings: list[str] = []
    for case, case_lines in cases.items():
        blocks[case], errors = then_blocks(case_lines)
        findings += [f"case {case}: {e}" for e in errors]
    if lines is not None:
        findings += check_grammar(lines)
    findings += check_lines(cases, blocks, records)
    if frontier is not None:
        findings += check_frontier(
            frontier[0], frontier[1], cases, blocks, records, project_dir, plan
        )
    findings += check_tasks(cases, blocks, records)
    findings += check_governed(blocks, governed_paths(project_dir))
    findings += check_keys(blocks, project_dir, schema_free)
    findings += check_conditions(blocks, project_dir, schema_free)
    findings += check_required(blocks, records, project_dir, schema_free)
    findings += check_form(blocks, project_dir)
    findings += check_markers(blocks, project_dir)
    findings += check_pairs(cases, blocks, project_dir)
    findings += check_bare_links(cases, blocks, project_dir)
    findings += check_criterion_pairs(blocks, project_dir)
    findings += check_same_target(blocks)
    findings += check_frame(cases, blocks)
    return findings


def plan_findings(
    plan: str, project_dir: Path, stamp: str, now
) -> tuple[list[str], list[str]] | None:
    """The findings and the notes of `--check` on a plan, for a session and a moment — the
    one judgment `check` prints and the `ExitPlanMode` hook refuses by (case 561.3). None
    when the session's window holds no `hi`: nothing is checked."""
    logs = session_event_logs(project_dir, now, stamp)
    hi = hi_moment(logs, stamp)
    folder = session_dir(project_dir, now, stamp)
    if hi is None or folder is None or not hi_recorded("".join(t for _, t in logs), stamp):
        return None
    lines = window_lines(project_dir, hi, now.date().isoformat())
    records = session_decisions(lines)
    relative = folder.relative_to(project_dir).as_posix() + "/frontier.md"
    findings = judge(plan, project_dir, records, lines, (folder / "frontier.md", relative))
    findings += check_untranslated(plan, project_dir)
    cases = split_cases(plan)
    blocks = {case: then_blocks(case_lines)[0] for case, case_lines in cases.items()}
    findings += check_pointers(blocks, project_dir, cases)
    notes = (
        chain_notes(cases)
        + promise_notes(plan, project_dir)
        + defer_notes(cases)
        + cascade_notes(blocks, records, project_dir)
    )
    return findings, notes


def check(plan: str, project_dir: Path, stamp: str, now, stdout, stderr) -> int:
    judged = plan_findings(plan, project_dir, stamp, now)
    if judged is None:
        print(f"prespec: no hi recorded for session {stamp}; nothing checked", file=stderr)
        return 0
    findings, notes = judged
    for line in findings + notes:
        print(line, file=stdout)
    return 1 if findings else 0


def gate(project_dir: Path, now, stamp: str, stderr) -> int:
    """The `ExitPlanMode` hook (cases 136, 213.2, 561.3): in a working session — a `hi` of
    the stamp in its logs — with no `prespec` line after it, exit 2 with the reason; with the
    line, the plan file of the session by `ledger.plan_path` is judged by `plan_findings`, and
    while it finds one, exit 2 with the findings on stderr. Notes alone, or no plan file of
    the session, pass."""
    logs = session_event_logs(project_dir, now, stamp)
    hi, done = window("".join(text for _, text in logs), stamp)
    if not hi:
        return 0
    if not done:
        print(
            f"prespec: Plan Mode is closing without /pre-spec in session {stamp}. "
            "Run /pre-spec, then exit Plan Mode again.",
            file=stderr,
        )
        return 2
    plan_file = plan_path(logs, stamp)
    if plan_file is None or not plan_file.is_file():
        return 0
    judged = plan_findings(plan_file.read_text(encoding="utf-8"), project_dir, stamp, now)
    if judged is None or not judged[0]:
        return 0
    print(
        f"prespec: the check of the plan {plan_file} finds {len(judged[0])} finding(s); fix "
        "them, run the check again, then exit Plan Mode:",
        file=stderr,
    )
    for line in judged[0]:
        print(line, file=stderr)
    return 2


FINDING_CASE = re.compile(r"^case (\S+?):")


def written_findings(
    plan: str, written: set[str], project_dir: Path, stamp: str, now, extra: list[dict]
) -> list[str]:
    """The findings of `judge` on the Cases the `Stop` hook of `rule-spec-write` wrote in
    one run and on their sub-cases, a finding of another Case left out (case 414.1). The records
    are the window's decision lines and `extra`, the lines of the reply itself, each once: the
    ledger hook runs in parallel on the same `Stop`, so `ledger.md` may not hold them yet. No
    Frontier, no language finding, no grammar of the window: they stay with `/pre-spec`."""
    hi = hi_moment(session_event_logs(project_dir, now, stamp), stamp)
    lines = window_lines(project_dir, hi, now.date().isoformat()) if hi else []
    records: list[dict] = []
    seen: set[str] = set()
    for record in session_decisions(lines) + list(extra):
        key = json.dumps(record, sort_keys=True)
        if key not in seen:
            seen.add(key)
            records.append(record)

    def ours(finding: str) -> bool:
        match = FINDING_CASE.match(finding)
        case = match.group(1) if match else ""
        return any(case == w or case.startswith(w + ".") for w in written)

    return [f for f in judge(plan, project_dir, records) if ours(f)]


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="guppi prespec", description=__doc__.split("\n\n")[1])
    p.add_argument("--check", metavar="PLAN", help="the plan file to check against the session")
    p.add_argument("--session", default=None, help="session id; else CLAUDE_SESSION_ID or the log")
    return p


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    if argv:
        args = parser().parse_args(argv)
        if not args.check:
            parser().print_usage(stderr)
            return 2
        plan_file = Path(args.check)
        if not plan_file.is_file():
            print(f"prespec: no plan file at {plan_file}", file=stderr)
            return 2
        plan = plan_file.read_text(encoding="utf-8")
        stamp = resolve_session(args.session)
        if stamp is None:
            print(NO_SESSION, file=stderr)
            return 2
        return check(plan, project_dir, stamp, now, stdout, stderr)
    try:
        payload = read_payload(stdin)
        if payload.get("tool_name") != TOOL:
            return 0
        stamp = session_stamp(None, payload)
        # the logs from today back to this session's start, as the ledger hook reads them,
        # so yesterday's `hi` and `prespec` are found after midnight (case 213.2)
        return gate(project_dir, now, stamp, stderr)
    except Exception as exc:  # noqa: BLE001 — a hook that raises would fail the session
        print(f"prespec: check skipped: {exc}", file=stderr)
    return 0
