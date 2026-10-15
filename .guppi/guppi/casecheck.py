"""`guppi casecheck --subagent` — the `SubagentStop` hook that checks the Case `case-guppi`
wrote into its file, or answered with on the old path, before the main agent sees it (cases
419.3, 645.2); `guppi casecheck` — the `Stop` hook
that compares each Case the main agent shows with the one the check stored (case 419.4);
`guppi casecheck --prompt` — the `UserPromptSubmit` hook that tells the agent, at the
person's next message, of a round or a Case its last reply showed after a text of its own
(cases 699.1, 699.2).

The check. For an answer of `case-guppi` (`agent_type`), the hook takes as the answer the
newest output of the subagent in `agent_transcript_path` that holds a Case heading, that
`is_round` finds a round, or that `is_fact` finds a Fact answer — a text or the `message` of
a `SubagentHandback` call, whichever stands later; an output that is none of the three, such
as a summary after a hand-back, is passed over — or `last_assistant_message` when the
transcript is not readable or holds no such output (cases 434, 607.1); the transcript is
read by `ledger.read_records`. It reads the Cases of the answer in the chat
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
`❓ **Q<n>** - **<title>**:`, a round that `round_form` finds out of form giving no title
(case 601.5); a title that no item of a `recommend` of the answer opens with,
in bold, is a finding of the top-level Case, a title asked in more than one round looked for
once and the words of an item after its title not judged (case 544.3); a title in the
`recommend` of an entry of the store under the number alone, of the family of the answer's
Cases, that the answer does not hold, is held too, so an answer of sub-cases alone keeps its
parent's `recommend` (`stored_family`) (case 629.4). The handling of an answer of sub-cases
alone judged with its stored parent (`stored_parents`) is gone: the check reads the whole
file of a Case (cases 629.3, 645.2). The Cases of the answer are judged with the
other Cases of the session by `prespec.check_same_target`, imported: each Case of the plan
file, then each entry of the store under the number alone that the plan does not hold, its
section built by `ratified.case_section` — leaving out an entry with findings, a Case a
`{supersedes}` mark of the session's ledger names, a Case a `{supersedes}` mark on a
decision line of the answer's own `ratification` names, read by `ratification_records`, a
mark on a sub-case leaving out that sub-case alone (case 725.2), a Case the answer holds,
the family of a top-level Case the answer holds, a dropped Case, whose file holds nothing
but blank space by `dropped` (case 701.7), and an entry whose top-level Case file holds text
but no heading of its id, a part a Case built again no longer holds, by `left_by_its_file`,
its entry kept in the store (case 722.1) — and the answer's Cases last; a clash is a finding of the
Case of the answer it opens with, and a clash inside the answer, which `judge` gives, or
between two other Cases is none (`other_blocks`, `session_clashes`) (case 629.1). It runs
over the same Spec text the language finding of `/pre-spec`, `prespec.check_untranslated`,
imported: a name, `context` or `problem` that holds a letter
outside the script of the documentation language is a finding of its Case — a Latin letter in
a code span excepted, which is no finding, while a letter of any other script there is judged
as in prose (case 589.2) — and a `guppi.toml`
that is missing or names a code the table does not hold is one finding, given to the first
Case of the answer (case 537). A top-level Case N of the answer whose family — N and its
sub-cases at any depth — has a decision line other than a `defer` in the session's ledger on
a number with no section in the answer, or on a number with a sub-case in the answer, is a
Case ratified in the session and built again in another shape under its old number: a
finding of N, by `shape_findings`, names those numbers, a new number — one above the highest
top-level number among the decision lines of the ledger and the keys of the store, by
`new_number`, the one count — and the marks its decision lines carry, one
`{supersedes:case N}` and one for each number of the family with such a line (case 610.1).
A number of the answer with a section and no sub-case whose decision line other than a
`defer` in the session's ledger has no item in its `then` block, by `line_has_item` of
`.guppi/guppi/prespec.py` — a target renamed or dropped in a Case built again in its shape — is a
finding of its Case, by `target_findings`, with the same new number and marks; `case-guppi`
puts the item back or changes the number by `Edit`, never writing the whole Case again
(case 671.1). On such a number a `create` line of the ledger whose slug the number's
`ratification` holds on a `create` line with another `ref`, or with a tag added or removed,
is a finding of its Case too, by `changed_create_findings`, with the same new number and
marks, since `generate` builds the page from the first line and takes the later one for a
repeat; the order of the tags and a `{supersedes}` or `{addresses}` mark do not count, and
`case-guppi` writes the line back as the ledger holds it or changes the number by `Edit`
(case 749).
Each Case of the answer is stored with its findings, the time of the store and the `agent_id`
of the payload in `<plan>.checked.json` beside the plan file of the session, a later answer
for the same id replacing it but for the notes sent for that id, which it keeps (case 472.1).
An answer whose family the store holds under the number alone from another `agent_id` is a
finding of its first Case that names a new number by `new_number`, and each Case of that
answer is stored apart, under its number joined with its `agent_id` by `@`, the other entry
left as it was; the Spec hook, the `Stop` comparison and the file of a Case read the entry
under the number alone, and an entry with no `agent_id` is not compared (case 610.2). The
guard `guppi ratified --guard` holds a number before the agent stops: the first call of a
`case-guppi` on `case-<N>.md`, N read by `case_number`, writes under N an entry with its
`agent_id` and the time and no text, which this check replaces with the Case of the same
agent, and a call of another agent on that file is refused with a free number by `clashes`
and `new_number` (case 650.1); `held_store` reads the store for that writer and `write_store`
writes it for both. The notes
are those of `prespec.promise_notes` on the answer — a line of a Criterion replaced whole that
the new one does not carry, a `then` line shared by two siblings, named on the later (cases
472.1, 472.2): a note not yet held for its Case id is stored under `notes`, apart from the
findings, and sent back once by exit 2 beside any findings; a note is no finding, and `stop`
refuses no showing for it. Beside them stand the cascade notes of `prespec.cascade_notes`,
imported (case 739.2): an `update` of a page that the cascade of `guppi generate` archives
after an item of the answer or of another Case of the session, by `other_blocks` — the other
Cases first, the answer last, with the `{supersedes:case N}` marks of the session's ledger
and of the answer — a note only when it names a Case of the answer, as the Case of the
`update` or as the Case that sets off the archive, and stored under that Case; two other
Cases give the answer none.

The tags (case 703.1). A tag in the `tags` of a `create`, in `tags` under the `set` of an
`update`, or in a `{tags:...}` block of a decision line of the answer is a finding of its Case
when no row of `vault/wiki/tags.md` holds it, no tag line of the answer declares it, and no tag
line of a Case of the session with a decision line in the session's ledger declares it, that
Case read from the store (`unlisted_tags`). The rows and the tag lines are read by
`registered_tags`, `declared_tags` and `ratified_tags` of `.guppi/guppi/tags.py`, the reading the
ledger hook and `register_tags` of `.guppi/guppi/generate.py` share; with no `tags.md` no tag is
judged. This check is the hook's own, not one of `/pre-spec`.

The pairs of the session (cases 711.1–711.3). When the session holds other Cases, by
`other_blocks`, the hook runs `prespec.check_pairs`, imported, over their `then` blocks first
and those of the answer last, to copies of the pages in memory; it keeps the findings that
open with a Case of the answer and leaves out the pair findings `judge` gave on the answer
alone, so an old text another Case already rewrote, or that then hits twice, goes back, and
one that hits only after another Case's pair is no finding (case 711.1). The same run gives a
note, sent once beside the notes of `promise_notes`, for a pair of the answer whose sentence
another Case's pair wrote into; the Cases of the answer and of its family are its own and
give none (case 711.2). And it traces the sentence around each match of a pair of the answer,
on the page as the earlier pairs leave it: `read_outputs` reads the outputs of the `Read`
calls of the subagent in `agent_transcript_path` — the tool use and its tool result, keyed by
the file, line numbers set aside — and `unread_sentences` gives a finding of its Case when a
part no pair wrote did not come back whole from a read of the page file, or a part another
Case wrote from a read of that Case's file; a part the answer wrote is not judged, the output
of a `Grep` is no read, and a transcript the hook cannot read judges no read (case 711.3).
This check of the read is the hook's own, not one of `/pre-spec`.

The file (case 645.2). `case-guppi` writes its Case into
`raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, named by
`case_file`, and fixes it by `Edit`. The hook takes each file under the `cases/` folder of a
session folder, judged by `is_case_file`, that a `Write`, `Edit` or `MultiEdit` call of the
subagent in `agent_transcript_path` names (`written_case_files`), and reads its Cases as the
file stands: a file whose Cases the store holds under their ids with the same text — line
ends and trailing spaces aside, by `file_differences`, the one comparison of a file with the
store — and no findings is not checked or stored again, so the time of its store stands;
any other is checked whole as an answer is and stored; the hook writes no such file. Until a
reading of `estimate-case-build-writes-the-case` passes live, a transcript that names no such
file and whose newest output holds a Case heading is read the old way: that output is
checked and stored, and with no finding written by `write_case_files` — the file replaced
whole when it holds the top-level Case, the section of each sub-case replaced or placed
after its family otherwise (case 452.1); a Case of a later session removes this path. A finding exits 2 with the findings on stderr, and Claude Code sends the agent
back (measured 2026-09-25, session 0051), whatever `stop_hook_active` says: Claude Code sets it
on the second fire after a handback with no exit 2 of this hook (measured 2026-09-26, session
1337). The store guards the loop: when every Case with findings stands in the store with the
same text and findings, they are stored again and the hook exits 0. An answer that is a
round or a Fact answer is not checked or stored as a Case, and an earlier Case is not read
again (case 607.1); a round is still judged by the check of the form, which stores nothing.
With no plan file of the session no Case is stored or sent back.

The name in the summary (case 662.3). When the subagent wrote a file of `cases/` and its
newest output, by `subagent_outputs`, opens with `**Built:**` — a summary, not a round, a
`**Fact:**` answer or an answer with no file — `summary_findings` reads its `**Case:**`
lines, `**Case:** N — name`, and the top-level heading `## Case N — name` of each written
file, the heading found by `CASE_HEADING` of `.guppi/guppi/materialize.py`; it compares the id and
the name of the line with those of the heading, trailing spaces aside, not the whole line.
A file whose heading no line names, or names with another name, is a finding that names the
file and the line to write; it joins the findings of the files in one exit 2. The guard
against a loop keys on the text of the summary and the heading of the file together: a
summary sent back is held under `summary_sent` of the entry of its top-level Case, the text
and the heading, which a later store of that Case keeps; a summary whose text an earlier
output already holds gets no finding again while the heading stands as it was when it was
sent back, and gets one again once the heading changed.

The form of a round (case 601.1). Before the check of a Case, the same `--subagent` run
judges the newest output of `case-guppi` in `agent_transcript_path` by `round_form`: a text
that `is_round` — the one test of a round, which the `Stop` run imports too — finds a round
has each question, from a line that opens with `❓` to the next, judged against the
template of the skill `grill-me`: the title line by `QUESTION_LINE`, the one pattern every
check of a round reads; a `**Now:**` line; the `**Options:**` label alone on its line; an
option `🔹` with an `**After:**` line, with or without a list dash before the label (case
744.2); a `➡️` line. A question out of form is a finding
that names its first line and each part it misses and tells the agent to answer with the
round whole again; a round gets no check of a Case, so its exit 2 carries the findings of its
form alone (case 607.2). A round
whose text an earlier output already holds, trailing spaces aside, is not sent back again
(`faulty_round`). The check stores nothing and writes no file, with or without a plan file;
an unreadable transcript is not judged; a round as the main agent shows it is not judged
here.

The same comparison — `against_store` — and the same reading of a sending — `sendings`,
under `sent` — serve this module's `stop` and the Spec hook, which writes the stored answer
into the plan and refuses a showing that differs from it (case 437) or a Case whose file was
not sent after its store (case 452.3).

The comparison. On `Stop` — beside `guppi ledger`, `guppi ratified` and `guppi context`, which
run in parallel — each Case the reply shows under its heading with at least one of
its sections (`shows_sections`) is compared with the Case of the same id in the store in each
of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows — the lines up
to the horizontal rule that opens the agent's own text, line ends and trailing spaces made the
same; a section the reply does not show is not compared (case 452.2). The name of its heading,
its `context`, `problem` and `recommend`, and text under the heading outside its sections are
not compared (cases 441.3, 452.2). A parent shown with its sub-cases is compared part by part.
Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines
of its sub-cases — the list of a showing — is read as the showing of each sub-case whose id a
line names: the lines that name that id are compared with the `ratification` of that sub-case
in the store, so a stored line that is missing or a line the store lacks is a difference, and
the parent is compared on its other parts alone (`list_showing`, `showings`) (case 561.10). The
Spec hook reads a showing by the same `showings`.
A Case the store does not hold, one that differs, one stored with findings, or one with no
`SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the
id of its top-level Case, exits 2 with the reason on stderr (case 452.2); so does a shown Case
whose file holds a Case that differs from its entry of the store under its id alone, or that
the store does not hold, by `changed_file`, the one judgment the Spec hook imports (cases
645.4, 645.11). A heading with no
section — the acknowledging reply — a fence tagged `DIFF`, and a deferred decision in the
short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and
no `when` — are not compared and need no sending. Outside a working session — no `hi` —
nothing is done.

The loop guard (case 688.1). The `Stop` run judges every reply whether `stop_hook_active`
is set or not, since Claude Code keeps the flag set from a refusal of any `Stop` hook until
the person's next message, so a showing written again after a refusal is judged again. It
guards its own loop by its refusals in the stretch — the transcript after the person's last
message — read by `refusals` of `.guppi/guppi/ledger.py`, the judgment `guppi onward` calls
(`own_told`): a reason that names a Case, opening with `case <id>:`, is given while fewer than
`LIMIT`, three, of its refusals hold a reason of that Case, and any other reason — an error
of its own — while fewer than three hold the same reason (`times_given`, `give`). The
opening of a round and the layout of a showing are no reasons of it: the `--prompt` run
tells them and counts nothing (case 699.3). When no reason is left to give it exits 0 and
prints one line per Case it lets through, which the Spec hook compares at ratification. With
the flag set and a transcript it cannot read it exits 0 and prints nothing.

How a round opens (case 562). `guppi casecheck --prompt`, the run on `UserPromptSubmit`,
judges the last reply of the main agent before the person's message — the transcript's
main-agent records, the person's new message left out when the transcript holds it
(`before_message`), the reply the text blocks of its turn after the last tool call
(`last_reply`) — when its turn holds a round of `case-guppi`: a text a subagent gave back in
the turn, by `given_back`, that `is_round` finds a round — the one test of a round, a line
that opens with `❓`, no Case heading and no `**Fact:**` line before it, not a
`QUESTION_LINE` match, so a round whose title line lacks its colon is judged too (case
601.4). The `Stop` run no longer refuses a reply for it, so a round is not shown twice (case
699.1). It finds a fault
when the first line of the reply that is neither blank nor the horizontal rule opens neither
with `❓ ` nor with a bold label that ends in a colon (case 751.4) — the label of the Context paragraph, translated — and, while the
session's event log holds no `prespec` line of this session after its `hi`, judged by
`prespec.window`, the function the `ExitPlanMode` hook judges by, imported, when the main
agent wrote text in the turn after the first round came back and before its last tool call,
by `texts_after`; a text written before the round came back cannot be taken back and is not
judged, and when the turn holds a refusal of the check, by `refusals` of `.guppi/guppi/ledger.py`,
only the texts after the reply that the last such refusal follows are judged (`last_refused`),
so a round shown again with nothing before it passes (case 692.1); after `/pre-spec` that text is not
judged, since in the loop after its findings each answer of a `case-guppi` comes back in a
turn of its own and the text the main agent writes there is set by `rule-prespec` (case
581.2). On a fault it prints one line to stdout, which reaches the agent's context: it
quotes the text before the round, says the round stands as shown and is not shown again, and
tells the agent to open the next round with its Context paragraph or its first question,
with nothing before it but a horizontal rule. It exits 0 always and never blocks the message; its own error goes
to stderr, and an unreadable payload prints nothing. Text after the last question is not judged, a
turn with no round — the main agent's own questions, a `**Fact:**` answer, a re-pitch by
`wait-what` — is not judged, and the check stores nothing. The answer to an `Agent` call
stands in the `tool_result` of the call, inside the turn; the answer to a `SendMessage`
stands in a later `user` record with `origin.kind` `task-notification`, its content a string
holding the answer between `<result>` and `</result>` — a returned answer by `user_kind` of
`.guppi/guppi/ledger.py`, a record that opens the turn, so `given_back` reads it as the turn's
opener (case 592; measured on the transcript of session 2356, 2026-10-01). A notification
carries no agent type; the question line is what marks a round.

The layout of a showing (case 611). The same `--prompt` run judges the last reply when it
shows a Case — one that `showings` reads, so not the acknowledging reply, a fence tagged
`DIFF` or the short form — against the layout `orchestration.md` sets: the heading, one list
under it, one `ratification`, and the agent's own text only after the horizontal rule; the
`Stop` run no longer refuses a showing for it, while it still refuses a Case that differs
from the store or whose file was not sent (case 699.2). It finds a fault when a
line that is neither blank nor the horizontal rule stands before the first Case heading
(`CASE_HEADING` of `.guppi/guppi/materialize.py`, `## Case N —` or `### Case N.M —`); when, between a
Case heading and the next one or the horizontal rule, a line stands that is not blank, not a list item — one
that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and
not a line of the `ratification` blockquote, its `RATIFICATION_HEAD` and the `>` lines after
it, or when `quoted_sections` reads there a section other than `ratification`; and when the
main agent wrote text in the turn after the first summary of `case-guppi` came back — a text
given back whose first line that is not blank opens with `**Built:**`, by `is_summary`, the
test `summary_findings` shares — and before its last tool call, by `texts_after`, the
judgment of the check of a round, after the reply the last refusal of the check follows, with
no second copy (`outside_the_list`, `showing_layout`) (case 692.2). A text written before the
summary came back, and every text of a turn with no summary, is not judged. The note quotes
the first such text, says the Case stands as shown and is not shown again, and tells the
agent to write nothing of its own before the Case but a horizontal rule and to keep its own
text after the horizontal rule at the next showing; it is joined with the note on the
opening of a round. A horizontal rule whose next line that is not blank is a Case heading
ends one Case, and the judgment goes on under that heading, so each Case of a batch is
judged (case 751.5); text after a horizontal rule that no Case heading follows is not
judged, and the check stores nothing. The comparison above still compares the sections a reply shows; this check refuses
the showing of any but `ratification`.

A sending. The transcript is JSONL (`ledger.read_records`); a `SendUserFile` call stands in an
assistant record's `message.content` as `{"type": "tool_use", "name": "SendUserFile",
"input": {"files": [<path>, …]}}`, the record carrying its `timestamp` (measured 2026-09-27,
session 1255). The turn of the reply is the records after the last `user` record that
`user_kind` of `.guppi/guppi/ledger.py` names the person's message (`origin.kind` `human`) or a
returned answer (`task-notification`) — the one judgment of the person's message, which the
stretch of the ledger hook and the count of `.guppi/guppi/context.py` share (case 592). A tool
result, the text of a skill, the record of a local command with no `origin`, a `peer`
message of another Claude session and a `Stop` hook's refusal — a `user` record marked
`isMeta`, its text opening with `Stop hook feedback:` (transcripts of sessions 1237 and 1441,
case 584) — open no turn, so a file sent before the refusal still counts for the reply that
follows. A transcript with neither kind is read whole as the turn.

The payload is read as UTF-8; the hook never raises. An error of its own after it has read the
payload exits 2 on `Stop`, with the error and the advice to show the Case again on stderr, so
the agent sees it, under the count of the loop guard: at most three times a stretch for the
same error, flag or not (case 688.4); an error while it reads the payload, and any error of the `--subagent` run,
exits 0 with the error on stderr, since a send-back to `case-guppi` is not ended by
`stop_hook_active` and would loop; a Case its error left with no file is refused later by the
`Stop` check (case 555.1). The text of this docstring holds what the `## How it works` of
`rule-case-check` held before the section left the Leaf page (case 589.2). Rule page:
`vault/wiki/rules/rule-case-check.md`.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from guppi import caseid
from guppi.event import project_root, read_payload, session_stamp
from guppi.generate import DAY, FRONTIER_LINE, FRONTIER_SEPARATOR, SESSION
from guppi.ledger import (
    ANSWER,
    PERSON,
    PREFIXES,
    PROJECT_RUN,
    opens_turn,
    plan_path,
    read_records,
    refusals,
    refusals_in,
    reply_text,
    session_dir,
    session_event_logs,
    stretch_of,
    transcript_records,
    user_kind,
)
from guppi.materialize import (
    CASE_HEADING,
    closes_fence,
    fence_opening,
    in_family,
    parse_line,
    quoted_sections,
    schema_changed,
    split_cases,
    tagged_blocks,
    then_blocks,
)
from guppi.prespec import (
    BACKLOG_SOURCE,
    FINDING_CASE,
    NOTE_CASE,
    cascade_notes,
    check_pairs,
    check_same_target,
    check_untranslated,
    decided_on_its_page,
    deferred_pages,
    judge,
    line_has_item,
    preview,
    promise_notes,
)
from guppi.prespec import window as prespec_window
from guppi.ratified import (
    CHAT_SECTIONS,
    case_section,
    headings,
    key_judge,
    place,
)
from guppi.tags import declared_tags, ratified_tags, registered_tags, tags_file

AGENT = "case-guppi"
HANDBACK = "SubagentHandback"  # the tool a subagent gives its report through (case 434)
SEND = "SendUserFile"  # the tool that sends the person a file (case 452.2)
STORE_SUFFIX = ".checked.json"
CASES = "cases"  # the folder of the files of built Cases in a session folder (case 452.1)
RULE = "---"  # the horizontal rule after which the agent's own text stands
# The parts of a shown Case compared with its stored answer, each only when the reply shows
# it (case 452.2); the heading name and the prose — `context`, `problem`, `recommend` — are free.
MECHANICAL = ("given", "when", "then", "tasks", "ratification")
# the Case that sets off the archive, at the end of a cascade note of `prespec` (case 739.2)
CASCADE_BY = re.compile(r"archives it after case (\S+?): ")
# The title line of a question of a round, as the template of the skill `grill-me` writes it,
# and the title of an item of `recommend` (case 544.3).
QUESTION_LINE = re.compile(r"^❓ \*\*Q\d+\*\* - \*\*(.+?)\*\*:")
RECOMMEND_ITEM = re.compile(r"^- \*\*(.+?)\*\*")
# The parts of a question of a round, as the template of the skill `grill-me` writes them: the
# mark that opens a question, and the fixed labels each question holds (case 601.1).
QUESTION_MARK = "❓"
NOW_LABEL = "**Now:**"
OPTIONS_LABEL = "**Options:**"
OPTION_MARK = "🔹"
AFTER_LINE = "**After:**"
AFTER_LINES = (AFTER_LINE, "- " + AFTER_LINE)  # with or without the list dash (case 744.2)
ARROW = "➡"


def store_of(plan: Path) -> Path:
    return plan.with_name(plan.stem + STORE_SUFFIX)


# --- the file of a built Case (cases 452.1, 453) ------------------------------------------


def top_case(case: str) -> str:
    """The id of the top-level Case of `case`: `452` of `452.1`, `kir-plugin-12` of
    `kir-plugin-12.1`, by the grammar of `.guppi/guppi/caseid.py` (case 788.2)."""
    return caseid.top(case)


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


def dropped(path) -> bool:
    """Whether the file `path` stands and holds nothing but blank space: the file of a Case
    `case-guppi` dropped, which is no Case — the one judgment of the hook of
    `rule-prespec-onward`, whether a Case is out and whether one was built again after
    `/pre-spec`, and of `other_blocks` (cases 701.1, 701.2, 701.7)."""
    path = Path(str(path))
    return path.is_file() and not path.read_text(encoding="utf-8").strip()


def left_by_its_file(path, case: str) -> bool:
    """Whether the file `path` of the top-level Case of `case` stands and holds text but no
    heading of `case`: a part that the Case built again no longer holds, which is no other
    Case of the session for `other_blocks` (case 722.1). An empty file is `dropped`."""
    path = Path(str(path))
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    return bool(text.strip()) and case not in split_cases(text)


CASE_NAME = caseid.CASE_FILE  # the name `case_file` gives, in either form (case 788.2)


def case_number(path) -> str | None:
    """N of a file named `case-<N>.md` as `case_file` names it, a plain id or an id of a
    sprint (case 788.6); None for any other name, a file the guard does not hold a number for
    (case 650.1)."""
    match = CASE_NAME.match(Path(str(path)).name)
    return match.group(1) if match else None


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
    """The records of the turn the reply ends: those after the last record that `user_kind`
    of `.guppi/guppi/ledger.py` names the person's message or a returned answer (case 592); the
    whole transcript when it holds neither."""
    start = 0
    for index, record in enumerate(records):
        if opens_turn(record):
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


def held_store(plan: Path) -> dict:
    """The store of `plan` for the guard that adds an entry to it (case 650.1): empty when it
    does not stand, an error when it stands and does not read as a JSON object, so a store
    that cannot be read is never written over."""
    path = store_of(plan)
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError(f"{path} holds no JSON object")
    return data


def write_store(plan: Path, store: dict) -> None:
    """The store `<plan>.checked.json`, the one writing of the check and the guard."""
    store_of(plan).write_text(
        json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8", newline=""
    )


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
            and all(line.startswith(PREFIXES) for line in body[1:-1])
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
    """`(top-level case, finding)` for each open `backlog` line of the Frontier and each
    page of its title with `deferred_by`, against each top-level Case of the answer that,
    itself or through a sub-case, names the page on a decision line other than a `defer` — by
    `prespec.decided_on_its_page`, the judgment `/pre-spec` runs (case 467.2)."""
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


def stored_family(cases: dict, store: dict | None) -> dict[str, list[str]]:
    """Case id → its lines in the chat form, for each entry of the store under the number
    alone, of the family of a Case of the answer, that the answer does not hold (cases
    629.3, 629.4)."""
    tops = {top_case(case) for case in cases}
    found: dict[str, list[str]] = {}
    for key, entry in (store or {}).items():
        key = str(key)
        if AGENT_KEY in key or key in cases or top_case(key) not in tops:
            continue
        if isinstance(entry, dict) and isinstance(entry.get("text"), str):
            found.update(
                {case: lines for case, lines in split_cases(entry["text"]).items() if case == key}
            )
    return found


def check_rounds(
    cases: dict, rounds: list[str], store: dict | None = None
) -> list[tuple[str, str]]:
    """`(top-level case, finding)` for each title of a question of the rounds that no item
    of a `recommend` of the answer opens with, in bold (case 544.3); a title asked in more
    than one round is looked for once, and the words of an item after its title are not
    judged. A title in the `recommend` of an entry of the store under the number alone, of
    the family of the answer's Cases, that the answer does not hold, is held too: an answer of
    sub-cases alone keeps its parent's `recommend` (case 629.4)."""
    if not rounds or not cases:
        return []
    held = recommend_titles(cases) | recommend_titles(stored_family(cases, store))
    top = top_case(next(iter(cases)))
    return [
        (top, f"case {top}: recommend holds no item for the question of the rounds: {title}")
        for title in dict.fromkeys(rounds)
        if title not in held
    ]


# --- the number of a Case built again (cases 610.1, 610.2) ---------------------------------

AGENT_KEY = "@"  # a key of the store joined with an agent id, `<case>@<agent_id>` (case 610.2)


def key_case(key) -> str:
    """The Case id of a key of the store: a key joined with an agent id is read by its
    number (case 610.2)."""
    return str(key).split(AGENT_KEY, 1)[0]


def new_number(
    records: list[dict],
    store: dict,
    top: str = "",
    project_dir: Path | None = None,
    folder: Path | None = None,
) -> str:
    """A free id for a Case built again (case 610.1) — `next_id` of `.guppi/guppi/caseid.py`, the one
    count, over the decision lines of the session's ledger, the keys of the store, and, given
    `project_dir` and `folder`, the Decision pages and the session's Case files, in the sprint
    of `top` (case 788.4); the count of `shape_findings`, of the clash of `subagent` (case
    610.2), of the guard `held_number` and of `guppi caseid --next`."""
    parsed = caseid.parse(top) if top else None
    sprint = parsed.sprint if parsed is not None else None
    if project_dir is None:
        ids = [str(r["case"]) for r in records if r.get("record") == "decision"]
        ids += [key_case(key) for key in store] + caseid.file_ids(folder)
    else:
        ids = caseid.known_ids(project_dir, folder, records, store)
    return caseid.next_id(sprint, ids)


def lined_numbers(top: str, records: list[dict]) -> list[str]:
    """The numbers of the family of `top` — `top` and its sub-cases at any depth — that hold
    a decision line other than a `defer` among the session's ledger `records`, in the order
    first seen."""
    return list(
        dict.fromkeys(
            str(r["case"])
            for r in records
            if r.get("record") == "decision"
            and r.get("kind") != "defer"
            and in_family(str(r["case"]), top)
        )
    )


def supersede_marks(top: str, lined: list[str]) -> str:
    """The marks the decision lines of a Case built again under a new number carry: one
    `{supersedes:case N}` for `top` and one for each number of `lined` (case 610.1)."""
    return "".join(f"{{supersedes:case {n}}}" for n in dict.fromkeys([top, *lined]))


def target_findings(
    cases: dict,
    blocks: dict,
    records: list[dict],
    store: dict,
    project_dir: Path | None = None,
    folder: Path | None = None,
) -> list[tuple[str, str]]:
    """`(top-level case, finding)` for each decision line other than a `defer` in the
    session's ledger `records` on a number of the answer that has a section in it and no
    sub-case, whose kind and slug `line_has_item` of `.guppi/guppi/prespec.py` does not find in that
    number's `then` block in `blocks`: a Case ratified in the session and built again in its
    shape under its old number with a target renamed or dropped (case 671.1). The finding names the
    number, the line, the new number by `new_number` and the marks as `shape_findings` writes
    them, and tells `case-guppi` to put the item back, or to change the number in the
    headings and the ledger lines by `Edit` and add the marks, never writing the whole Case
    again. A number with no section, or with sub-cases, is left to `shape_findings`."""
    findings: list[tuple[str, str]] = []
    for record in records:
        number = str(record.get("case", ""))
        if (
            record.get("record") != "decision"
            or record.get("kind") == "defer"
            or number not in cases
            or has_sub_cases(number, cases)
            or line_has_item(blocks.get(number) or {}, record)
        ):
            continue
        top = top_case(number)
        marks = supersede_marks(top, lined_numbers(top, records))
        finding = (
            f"case {number}: its decision line [{record['kind']}][{record['slug']}] stands in "
            "the session's ledger and the Case built again has no item for it — put the item "
            f"back, or change the number in the headings and the ledger lines to case "
            f"{new_number(records, store, top, project_dir, folder)} by Edit and add {marks}; "
            "never write the whole Case "
            "again"
        )
        findings.append((top, finding))
    return findings


def create_line(record: dict) -> str:
    """A `create` decision record as its line: the brackets, `ref` and the tags."""
    line = f"decision[case {record['case']}][create][{record['slug']}]"
    if record.get("ref"):
        line += f"{{ref:{record['ref']}}}"
    if record.get("tags"):
        line += f"{{tags:{','.join(record['tags'])}}}"
    return line


def changed_create_findings(
    cases: dict,
    ratified: list[dict],
    records: list[dict],
    store: dict,
    project_dir: Path | None = None,
    folder: Path | None = None,
) -> list[tuple[str, str]]:
    """`(top-level case, finding)` for each `create` line in the session's ledger `records`
    on a number of the answer that has a section in it and no sub-case, when the
    `ratification` of that number in the answer, `ratified`, holds a `create` line of the
    same slug whose `ref` differs, or whose tags differ by a tag added or removed: a Case
    ratified in the session and built again with another parent or tags for a page it
    creates, which `generate` would build from the first line, taking the later one for a
    repeat (cases 514, 749). The order of the tags and a `{supersedes}` or `{addresses}` mark do
    not count; a slug with no `create` line under that number in the answer is left to
    `target_findings`. The finding names the number, the slug, both lines, the new number
    by `new_number` and the marks by `supersede_marks`, and tells `case-guppi` to write the
    line back as the ledger holds it, or to change the number in the headings and the ledger
    lines by `Edit` and add the marks, never writing the whole Case again."""
    answered = {
        (str(r["case"]), r["slug"]): r
        for r in ratified
        if r.get("record") == "decision" and r.get("kind") == "create"
    }
    findings: list[tuple[str, str]] = []
    for record in records:
        number = str(record.get("case", ""))
        if (
            record.get("record") != "decision"
            or record.get("kind") != "create"
            or number not in cases
            or has_sub_cases(number, cases)
        ):
            continue
        again = answered.get((number, record["slug"]))
        if again is None or (
            (again.get("ref") or None) == (record.get("ref") or None)
            and set(again.get("tags") or []) == set(record.get("tags") or [])
        ):
            continue
        top = top_case(number)
        marks = supersede_marks(top, lined_numbers(top, records))
        finding = (
            f"case {number}: create {record['slug']}: the session's ledger holds "
            f"{create_line(record)} and the Case built again holds {create_line(again)} — "
            "the librarian builds the page from the first line; write the line back as the "
            "ledger holds it, or change the number in the headings and the ledger lines to "
            f"case {new_number(records, store, top, project_dir, folder)} by Edit and add "
            f"{marks}; never write the "
            "whole Case again"
        )
        findings.append((top, finding))
    return findings


def shape_findings(
    cases: dict,
    records: list[dict],
    store: dict,
    project_dir: Path | None = None,
    folder: Path | None = None,
) -> list[tuple[str, str]]:
    """`(top-level case, finding)` for each top-level Case N of the answer whose family — N
    and its sub-cases at any depth — has a decision line other than a `defer` in the
    session's ledger `records` on a number with no section in the answer, or on a number with
    a sub-case in the answer: a Case ratified in the session and built again in another shape
    under its old number (case 610.1). The finding names those numbers, the new number by
    `new_number`, and the marks its decision lines carry: one `{supersedes:case N}` and one
    for each number of the family that has such a line. An answer of sub-cases alone, a
    family with only `defer` lines, and a Case built again in the same shape give none."""
    findings: list[tuple[str, str]] = []
    for top in (case for case in cases if "." not in case):
        lined = lined_numbers(top, records)
        changed = [n for n in lined if n not in cases or has_sub_cases(n, cases)]
        if not changed:
            continue
        marks = supersede_marks(top, lined)
        finding = (
            f"case {top}: case {', '.join(changed)} has decision lines in the session's "
            "ledger and comes back in another shape under its old number — build it "
            f"again as case {new_number(records, store, top, project_dir, folder)}, its "
            f"decision lines carrying {marks}"
        )
        findings.append((top, finding))
    return findings


def superseded_cases(window: list[str]) -> list[str]:
    """Each Case a `{supersedes:case N}` mark of the session's ledger names."""
    return [n for record in ledger_records(list(window)) for n in record.get("supersedes") or []]


def other_blocks(
    cases: dict, plan: str, store: dict | None, window: list[str], folder: Path | None = None
) -> dict[str, dict]:
    """Case id → its `then` block, for the other Cases of the session in the order they are
    judged (case 629.1): each Case of the plan, then each entry of the store under the
    number alone that the plan does not hold — its section built by `ratified.case_section` —
    leaving out an entry with findings, a Case a `{supersedes}` mark of the ledger names, a
    Case a `{supersedes}` mark on a decision line of the answer's own `ratification` names,
    read by `ratification_records` — a mark on a sub-case leaves out that sub-case alone
    (case 725.2) —, a Case the answer holds, the family of a top-level Case the answer holds,
    an entry whose top-level Case file in the session folder `folder` stands and holds
    nothing but blank space, a dropped Case, by `dropped` (case 701.7), and an entry whose
    top-level Case file stands and holds text but no heading of its id, a part a Case built
    again no longer holds, by `left_by_its_file` (case 722.1); the store keeps that entry."""
    tops = [case for case in cases if "." not in case]
    retired = superseded_cases(window) + [
        n for record in ratification_records(cases) for n in record.get("supersedes") or []
    ]

    def left_out(case: str) -> bool:
        return (
            case in cases
            or any(in_family(case, top) for top in tops)
            or any(in_family(case, n) for n in retired)
        )

    blocks: dict[str, dict] = {}
    planned = split_cases(plan or "")
    for case, lines in planned.items():
        if not left_out(case):
            blocks[case] = then_blocks(lines)[0]
    for key, entry in (store or {}).items():
        key = str(key)
        if AGENT_KEY in key or key in planned or left_out(key) or not isinstance(entry, dict):
            continue
        if entry.get("findings") or not isinstance(entry.get("text"), str):
            continue
        if folder is not None and dropped(case_file(folder, key)):
            continue  # a dropped Case is no other Case of the session (case 701.7)
        if folder is not None and left_by_its_file(case_file(folder, key), key):
            continue  # a part its Case built again no longer holds (case 722.1)
        chat = split_cases(entry["text"]).get(key)
        if chat is None:
            continue
        section, errors = case_section(key, headings(entry["text"]).get(key, ""), chat, {})
        if section and not errors:
            blocks[key] = then_blocks(section)[0]
    return blocks


def as_tags(value) -> list[str]:
    """The tags of a `tags` value: a list, or one string of tags split by commas."""
    if isinstance(value, str):
        value = value.split(",")
    return (
        [str(tag).strip() for tag in value or [] if str(tag).strip()]
        if isinstance(value, (list, tuple))
        else []
    )


def unlisted_tags(
    answer: dict[str, dict], records: list[dict], listed: set[str] | None
) -> list[tuple[str, str]]:
    """`(case, finding)` for each tag of a `create`, of `tags` under the `set` of an
    `update` and of a `{tags:...}` block of a decision line of the answer that `listed` does
    not hold — the rows of `tags.md` by `registered_tags` of `.guppi/guppi/tags.py`, the tag lines
    of the answer and of the Cases of the session with a decision line in its ledger (case
    703.1).
    None, no `tags.md`: no tag is judged."""
    if listed is None:
        return []
    used: list[tuple[str, str]] = []
    for case, block in answer.items():
        for item in block.get("create") or []:
            if isinstance(item, dict):
                used += [(case, tag) for tag in as_tags(item.get("tags"))]
        for item in block.get("update") or []:
            values = item.get("set") if isinstance(item, dict) else None
            if isinstance(values, dict):
                used += [(case, tag) for tag in as_tags(values.get("tags"))]
    used += [(str(r.get("case")), tag) for r in records for tag in as_tags(r.get("tags"))]
    advice = "use a tag of tags.md, or declare it by a tag line in this Case."
    return [
        (case, f"case {case}: tag {tag} is not in tags.md: {advice}")
        for case, tag in dict.fromkeys(used)
        if tag not in listed
    ]


READ = "Read"  # the one tool whose output counts as a read of a sentence (case 711.3)
NUMBERED = re.compile(r"^\s*\d+[\t→]", re.MULTILINE)  # the line number a Read output opens with


def path_key(path) -> str:
    """A path as the read check compares it: resolved, the case of a Windows path ignored."""
    try:
        return os.path.normcase(os.path.abspath(str(path)))
    except (OSError, ValueError):
        return str(path)


def flat(text: str) -> str:
    """`text` with its whitespace collapsed, so a part is found across the lines of a file."""
    return " ".join(text.split())


def result_text(content) -> str:
    """The text of the content of a tool result: a string, or a list of text blocks."""
    if isinstance(content, str):
        return content
    blocks = content if isinstance(content, list) else []
    return "\n".join(
        str(block.get("text") or "")
        for block in blocks
        if isinstance(block, dict) and block.get("type") == "text"
    )


def read_outputs(payload: dict) -> dict[str, str] | None:
    """The outputs of the `Read` calls of the subagent in `agent_transcript_path`, by the
    tool use and the tool result that answers it, keyed by the file by `path_key`; the line
    numbers set aside and the whitespace collapsed, all the reads of one file joined (case
    711.3).
    None when the transcript cannot be read: no read is judged then."""
    records = read_records(payload.get("agent_transcript_path"))
    if records is None:
        return None
    calls: dict[str, str] = {}
    outputs_of: dict[str, list[str]] = {}
    for record in records:
        message = record.get("message") if isinstance(record, dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") == READ:
                data = block.get("input")
                if isinstance(data, dict) and data.get("file_path"):
                    calls[str(block.get("id"))] = path_key(data["file_path"])
            elif block.get("type") == "tool_result" and str(block.get("tool_use_id")) in calls:
                text = NUMBERED.sub("", result_text(block.get("content")))
                outputs_of.setdefault(calls[str(block["tool_use_id"])], []).append(flat(text))
    return {key: "\n".join(texts) for key, texts in outputs_of.items()}


def unread_sentences(
    trace: list[dict], reads: dict[str, str], folder: Path | None, own: set[str]
) -> list[tuple[str, str]]:
    """`(case, finding)` for each sentence around a match of a pair of the answer whose
    parts did not come back whole from a `Read`: a part no pair wrote from a read of the page
    file, a part another Case's pair wrote from a read of that Case's file
    `raw/<date>/<hi HHMM>/cases/case-<N>.md`, whitespace and line numbers set aside (case
    711.3). A part a
    pair of the answer wrote is not judged; the output of a search or any other tool is no
    read. One finding per Case, page and sentence."""
    found: list[tuple[str, str]] = []
    for item in trace:
        missing = False
        for part, writer in item["parts"]:
            if writer in own:
                continue
            if writer is None:
                source = path_key(item["path"])
            elif folder is not None:
                source = path_key(case_file(folder, writer))
            else:
                continue
            if flat(part) not in reads.get(source, ""):
                missing = True
                break
        if missing:
            sentence = "".join(part for part, _ in item["parts"])
            finding = (
                f"case {item['case']}: {item['slug']}: the sentence around a pair was not read "
                f"whole: {preview(sentence)}: Read the page around it, and the file of each "
                "other Case that wrote into it, and check the pair."
            )
            found.append((item["case"], finding))
    return list(dict.fromkeys(found))


def session_clashes(answer: dict[str, dict], others: dict[str, dict]) -> list[str]:
    """The clashes of the answer's Cases with the other Cases of the session, by
    `prespec.check_same_target`, imported — the one judgment `/pre-spec` and the check after
    ratification run (case 629.1). The answer's Cases come last, so a finding opens with a
    Case of the answer; a clash inside the answer, which `judge` already gives, and one
    between two other Cases are left out."""
    if not others:
        return []
    inside = set(check_same_target(answer))
    combined = {**others, **answer}
    return [
        finding
        for finding in check_same_target(combined)
        if finding not in inside
        and (match := FINDING_CASE.match(finding))
        and match.group(1) in answer
    ]


def check_answer(
    text: str,
    project_dir: Path,
    window: list[str] = (),
    frontier: Path | None = None,
    rounds: list[str] = (),
    store: dict | None = None,
    plan: str = "",
    folder: Path | None = None,
    reads: dict[str, str] | None = None,
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Case id → its findings, and case id → its notes, for every Case of an answer of
    `case-guppi`. The categories whose schema rule the lines of the `ratification` fences or
    of the session's `window` change are not judged by their keys (case 436.4). `frontier`,
    the session's `frontier.md`, adds the check of its open `backlog` lines (case 467.2).
    `rounds`, the titles of the questions of the rounds of `case-guppi` on the Case, adds
    the check that `recommend` holds an item for each (case 544.3). `store`, the store of
    checked answers, adds the check of a Case built again in another shape against the
    decision lines of `window`, `shape_findings` (case 610.1), and of one built again in its
    shape without the item of one of its lines, `target_findings` (case 671.1), or with a
    `create` line whose `ref` or tags changed, `changed_create_findings` (case 749). The
    language finding of `/pre-spec`, `check_untranslated`, runs over the same Spec text as
    `judge`, each hit a finding of its Case (case 537). The notes are those of
    `prespec.promise_notes` on the answer — a Criterion line not carried, a `then` line shared
    by siblings (cases 472.1, 472.2). `plan`, the text of the plan file, with `store`, adds the
    check of the answer's Cases against the other Cases of the session, `session_clashes`
    (case 629.1); `folder`, the session folder, leaves a dropped Case out of them (case
    701.7)."""
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
        if case in found or not match:
            found[case if case in found else next(iter(cases))].append(finding)
    answer = {
        case: then_blocks(lines)[0]
        for case, lines in split_cases(spec_text).items()
        if case in cases
    }
    listed = registered_tags(tags_file(project_dir))  # None, no tag judged (case 703.1)
    if listed is not None:
        listed |= ratified_tags(store, ledger_records(list(window)))
        for block in answer.values():
            listed |= declared_tags(block)
    for case, finding in unlisted_tags(answer, records, listed):
        found[case if case in found else next(iter(cases))].append(finding)
    others: dict[str, dict] = {}
    if store is not None:  # the other Cases of the session (case 629.1)
        others = other_blocks(cases, plan, store, window, folder)
        for finding in session_clashes(answer, others):
            found[FINDING_CASE.match(finding).group(1)].append(finding)
    tops = {top_case(case) for case in answer}  # the family of the file is its own
    own = set(answer) | {case for case in others if top_case(case) in tops}
    pair_notes: list[str] = []  # the notes of the pairs (case 711.2)
    trace: list[dict] = []  # the sentences around each match of a pair (case 711.3)
    if others:  # the pairs of the session first, those of the answer last (case 711.1)
        alone = set(check_pairs(answer, answer, project_dir))  # what `judge` gave
        for case, held in found.items():
            found[case] = [f for f in held if f not in alone]
        combined = {**others, **answer}
        for finding in check_pairs(combined, combined, project_dir, own, pair_notes, trace):
            match = FINDING_CASE.match(finding)
            if match and match.group(1) in found:
                found[match.group(1)].append(finding)
    elif reads is not None:
        check_pairs(answer, answer, project_dir, own, pair_notes, trace)
    if reads is not None:
        for case, finding in unread_sentences(trace, reads, folder, own):
            found[case if case in found else next(iter(cases))].append(finding)
    shapes = []
    if store is not None:  # a Case built again under its old number (cases 610.1, 671.1, 749)
        ledger = ledger_records(window)
        shapes = (
            shape_findings(cases, ledger, store, project_dir, folder)
            + target_findings(cases, answer, ledger, store, project_dir, folder)
            + changed_create_findings(cases, records, ledger, store, project_dir, folder)
        )
    for top, finding in (
        check_backlog(records, frontier, project_dir)
        + check_rounds(cases, list(rounds), store)
        + shapes
    ):
        family = [c for c in found if c == top or c.startswith(f"{top}.")]
        found[family[0] if family else next(iter(cases))].append(finding)
    # an update of a page the cascade archives, the other Cases first (case 739.2)
    cascade = cascade_notes(
        {**others, **answer}, ledger_records(list(window)) + records, project_dir, set(answer)
    )
    notes: dict[str, list[str]] = {case: [] for case in cases}
    for note in promise_notes(spec_text, project_dir) + pair_notes + cascade:
        match = NOTE_CASE.match(note)
        case = match.group(1) if match else ""
        if case not in notes and (by := CASCADE_BY.search(note)) and by.group(1) in notes:
            case = by.group(1)  # the Case of the file whose item sets off the archive
        if case in notes or not match:
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
    """The answer of the subagent (cases 434, 607.1): the newest output in
    `agent_transcript_path` that holds a Case heading, that `is_round` finds a round, or that
    `is_fact` finds a Fact answer — a text or the `message` of a `SubagentHandback` call,
    whichever stands later; an output that is none of the three, such as a summary after a
    hand-back, is passed over. `last_assistant_message` when the transcript is not readable
    or holds no such output."""
    records = read_records(payload.get("agent_transcript_path"))
    for record in reversed(records or []):
        if record.get("type") != "assistant":
            continue
        for text in reversed(outputs(record)):
            if split_cases(text) or is_round(text) or is_fact(text):
                return text
    return str(payload.get("last_assistant_message") or "")


def round_titles(payload: dict) -> list[str]:
    """The title of each question of the rounds of the subagent, in order: the outputs in
    `agent_transcript_path` that hold no Case heading, each line `❓ **Q<n>** - **<title>**:`
    of the question template of the skill `grill-me` (case 544.3). An output that
    `round_form` finds out of form gives none, so a round the hook sent back adds no title
    the person never saw (case 601.5). An unreadable transcript gives none."""
    titles: list[str] = []
    for text in subagent_outputs(payload) or []:
        if split_cases(text) or round_form(text):
            continue
        for line in text.splitlines():
            match = QUESTION_LINE.match(line.strip())
            if match:
                titles.append(match.group(1).strip())
    return titles


def subagent_outputs(payload: dict) -> list[str] | None:
    """Every output of the subagent in `agent_transcript_path`, in order, by `outputs`; None
    when the transcript is not readable."""
    records = read_records(payload.get("agent_transcript_path"))
    if records is None:
        return None
    return [
        text
        for record in records
        if isinstance(record, dict) and record.get("type") == "assistant"
        for text in outputs(record)
    ]


def round_form(text: str) -> list[str]:
    """The findings of each question out of the form of the template of the skill `grill-me`,
    for a text that `is_round` finds a round; none for any other text (case 601.1). A question
    opens at a line that opens with `❓` and runs to the next such line or to the end; the
    text before the first one, the Context paragraph, is not judged. A question is out of
    form when its first line does not match `QUESTION_LINE`; when it holds no line that opens
    with `**Now:**`, no line that is `**Options:**` alone, or no line that opens with `➡️`;
    or when no line that opens with `🔹` has a line that opens with `**After:**` or with
    `- **After:**` after it, before the next `🔹` or `➡️` line (case 744.2). The lines are
    read with their indent set aside."""
    if not is_round(text):
        return []
    questions: list[list[str]] = []
    for line in (line.strip() for line in text.splitlines()):
        if line.startswith(QUESTION_MARK):
            questions.append([line])
        elif questions:
            questions[-1].append(line)
    findings: list[str] = []
    for first, *body in questions:
        missing = []
        if not QUESTION_LINE.match(first):
            missing.append("the title line `❓ **Q<n>** - **<title>**:`")
        if not any(line.startswith(NOW_LABEL) for line in body):
            missing.append(f"a `{NOW_LABEL}` line")
        if OPTIONS_LABEL not in body:
            missing.append(f"the `{OPTIONS_LABEL}` label alone on its line")
        if not option_with_after(body):
            missing.append(f"an option `{OPTION_MARK}` with an `{AFTER_LINE}` line")
        if not any(line.startswith(ARROW) for line in body):
            missing.append("a `➡️` line")
        if missing:
            findings.append(f"the question {first[:100]!r} misses {', '.join(missing)}")
    return findings


def option_with_after(lines: list[str]) -> bool:
    """Whether a line that opens with `🔹` has a line that opens with `**After:**` or with
    `- **After:**` after it, before the next `🔹` or `➡️` line (cases 601.1, 744.2)."""
    in_option = False
    for line in lines:
        if line.startswith(OPTION_MARK):
            in_option = True
        elif line.startswith(ARROW):
            in_option = False
        elif in_option and line.startswith(AFTER_LINES):
            return True
    return False


def faulty_round(payload: dict) -> list[str]:
    """The findings of `round_form` on the newest output of the subagent, or none when an
    earlier output holds the same text, trailing spaces aside — a round sent back once and
    given again unchanged is not sent back again, and nothing is stored (case 601.1). An unreadable
    transcript gives none."""
    texts = subagent_outputs(payload)
    if not texts:
        return []
    found = round_form(texts[-1])
    if not found:
        return []
    if any(spaces_aside(text) == spaces_aside(texts[-1]) for text in texts[:-1]):
        return []
    return found + ["answer with the round whole again"]


def spaces_aside(text: str) -> list[str]:
    """The lines of a text with the spaces at their ends and the blank lines at its ends set
    aside."""
    return [line.rstrip() for line in text.strip().splitlines()]


BUILT_LABEL = "**Built:**"  # the first line of a summary of `case-guppi` (case 645.1)
CASE_LABEL = "**Case:**"  # the line that names the top-level Case it built (case 662.1)
NAME_DASH = " — "  # between the id and the name, in a heading and in the line alike


def is_summary(text: str) -> bool:
    """A summary of `case-guppi`, the one test of it that `summary_findings` and the check of
    a showing share (case 692.2): its first line that is not blank opens with `**Built:**`.
    The lines are read with their indent set aside: the harness indents a hand-back."""
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    return first.startswith(BUILT_LABEL)


def top_heading(text: str) -> tuple[str, str] | None:
    """The id and the name of the first Case heading of a file of a Case, found by
    `CASE_HEADING` of `.guppi/guppi/materialize.py` — the top-level Case of the file (case 662.3);
    None when the file holds none."""
    for line in text.splitlines():
        match = CASE_HEADING.match(line)
        if match:
            rest = line.rstrip().split(NAME_DASH, 1)
            return match.group(1), rest[1].strip() if len(rest) == 2 else ""
    return None


def summary_names(text: str) -> dict[str, str]:
    """The id and the name of each `**Case:** N — name` line of a summary, trailing spaces
    aside (case 662.3)."""
    names: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith(CASE_LABEL):
            continue
        rest = line[len(CASE_LABEL) :].strip().split(NAME_DASH, 1)
        if rest and rest[0]:
            names.setdefault(rest[0].strip(), rest[1].strip() if len(rest) == 2 else "")
    return names


def summary_findings(payload: dict, files: list[Path], store: dict) -> list[str]:
    """The findings on the `**Case:**` lines of the newest output of the subagent when it
    is a summary — its first line that is not blank opens with `**Built:**` — for the files
    of `cases/` it wrote: a file whose top-level heading no line names with the same id and
    name is a finding that names the file and the line to write (case 662.3). A summary
    whose text an earlier output already holds gets no finding again while the heading of the
    file stands as it was when it was sent back, held under `summary_sent` of the entry of
    that Case in `store`, which this function writes; a round, a Fact answer and an answer
    with no file are not judged."""
    texts = subagent_outputs(payload)
    if not texts or not files:
        return []
    newest = texts[-1]
    if not is_summary(newest):
        return []
    names = summary_names(newest)
    repeated = any(spaces_aside(text) == spaces_aside(newest) for text in texts[:-1])
    sent_text = "\n".join(spaces_aside(newest))
    findings: list[str] = []
    for path in files:
        heading = top_heading(path.read_text(encoding="utf-8"))
        if heading is None:
            continue
        case, name = heading
        if names.get(case) == name:
            continue
        held = store.get(case)
        sent = {"text": sent_text, "heading": f"{case}{NAME_DASH}{name}"}
        if repeated and isinstance(held, dict) and held.get("summary_sent") == sent:
            continue  # sent back once for this text and this heading (the loop guard)
        if isinstance(held, dict):
            held["summary_sent"] = sent
        line = f"{CASE_LABEL} {case}{NAME_DASH}{name}"
        given = f"{CASE_LABEL} {case}{NAME_DASH}{names[case]}" if case in names else None
        findings.append(
            f"case {case}: the summary names {path} as `{given}`, not as its heading — write `{line}`"
            if given
            else f"case {case}: the summary has no line for {path} — write `{line}` "
            f"right after the line `{BUILT_LABEL}`"
        )
    return findings


EDIT_CALLS = ("Write", "Edit", "MultiEdit")  # the calls that write a file of a Case (case 645.2)


def written_case_files(payload: dict, project_dir: Path) -> list[Path]:
    """Each file under the `cases/` folder of a session folder, by `is_case_file`, that a
    `Write`, `Edit` or `MultiEdit` call of the subagent in `agent_transcript_path` names, in
    the order of its first call, a relative path read from `project_dir`; none when the
    transcript is not readable (case 645.2)."""
    found: dict[str, Path] = {}
    for record in read_records(payload.get("agent_transcript_path")) or []:
        if not isinstance(record, dict) or record.get("type") != "assistant":
            continue
        message = record.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            data = block.get("input")
            if block.get("name") not in EDIT_CALLS or not isinstance(data, dict):
                continue
            if not data.get("file_path"):
                continue
            path = Path(str(data["file_path"]))
            path = path if path.is_absolute() else project_dir / path
            if is_case_file(path):
                found.setdefault(str(path), path)
    return list(found.values())


def file_differences(text: str, store: dict) -> list[str]:
    """Each Case of the text of a file of a Case whose text, as `shown_text` keeps it,
    differs from the entry of the store under its id alone — line ends and trailing spaces
    aside — or that the store does not hold (case 645.4). The one comparison of a file with the
    store, which the `Stop` check of a showing and the Spec hook import."""
    heads = headings(text)
    differ: list[str] = []
    for case, lines in split_cases(text).items():
        entry = store.get(case)
        held = entry.get("text") if isinstance(entry, dict) else None
        shown = shown_text(heads[case], lines)
        if not isinstance(held, str) or spaces_aside(held) != spaces_aside(shown):
            differ.append(case)
    return differ


def changed_file(folder: Path, case: str, store: dict) -> str | None:
    """The reason the file of the top-level Case of `case` fails against the store, by
    `file_differences` — the Cases that differ or that the store does not hold, and the file
    — or None; a file that does not stand gives none, its sending is judged apart (case
    645.4). The one judgment of a changed file, which the `Stop` check of a showing and the
    Spec hook run."""
    path = case_file(folder, case)
    if not path.is_file():
        return None
    differ = file_differences(path.read_text(encoding="utf-8"), store)
    if not differ:
        return None
    return (
        f"case {', '.join(differ)}: {path} differs from the text the check stored — let "
        "case-guppi fix the file so that the check stores it again"
    )


def subagent(payload: dict, project_dir: Path, now, stderr) -> int:
    """The files of `cases/` the subagent wrote or edited, each checked whole and stored,
    one the store holds unchanged with no findings skipped; the hook writes none of them
    (case 645.2). With no such file and a newest output that holds a Case heading, the old path —
    that output checked, stored and, with no finding, written by `write_case_files` — until a
    reading of `estimate-case-build-writes-the-case` passes live."""
    if payload.get("agent_type") != AGENT:
        return 0
    form = faulty_round(payload)  # a round out of form, sent back with no store (case 601.1)
    files = [path for path in written_case_files(payload, project_dir) if path.is_file()]
    text = "" if files else answer_of(payload)
    if not files and not split_cases(text):
        return send_back(form, stderr)
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    plan = plan_path(session_event_logs(project_dir, now, stamp), stamp)
    if plan is None or not plan.is_file():
        return send_back(form, stderr)  # no plan file: no Case stored or sent back (case 434)
    store = read_store(plan)
    window = ledger_of(folder)
    frontier = folder / "frontier.md" if folder is not None else None
    plan_text = plan.read_text(encoding="utf-8")  # the session's other Cases (case 629.1)
    findings: list[str] = []
    fresh: list[str] = []
    repeated = True
    texts = [path.read_text(encoding="utf-8") for path in files] or [text]
    for each in texts:
        if files and not stored_with_findings(each, store) and not file_differences(each, store):
            continue  # unchanged and passed: its time of store stands (case 645.2)
        found, new, same = judge_and_store(
            each, payload, project_dir, now, store, window, frontier, plan_text, folder
        )
        findings += found
        fresh += new
        repeated = repeated and same
    named = summary_findings(payload, files, store)  # the `**Case:**` line (case 662.3)
    write_store(plan, store)
    if not files and not findings and folder is not None:  # the old path (cases 452.1, 645.2)
        write_case_files(folder, list(split_cases(text)), store)
    if (findings and not repeated) or fresh:  # the store guards the loop (cases 434, 472.1)
        return send_back(findings + fresh + named + form, stderr)
    return send_back(named + form, stderr)


def stored_with_findings(text: str, store: dict) -> bool:
    """Whether a Case of the text stands in the store under its id alone with findings."""
    return any(
        isinstance(store.get(case), dict) and store[case].get("findings")
        for case in split_cases(text)
    )


def judge_and_store(
    text: str,
    payload: dict,
    project_dir: Path,
    now,
    store: dict,
    window: list[str],
    frontier: Path | None,
    plan_text: str,
    folder: Path | None = None,
) -> tuple[list[str], list[str], bool]:
    """The findings of the Cases of `text` by `check_answer`, each Case stored in `store`;
    the notes not yet sent for their Case id; and whether every Case with findings stands in
    the store as it is, findings and all (cases 434, 472.1, 610.2)."""
    cases = split_cases(text)
    found, notes = check_answer(
        text,
        project_dir,
        window,
        frontier,
        round_titles(payload),
        store,
        plan_text,
        folder,
        read_outputs(payload),  # None, no transcript, no read judged (case 711.3)
    )
    agent_id = str(payload.get("agent_id") or "")
    apart = clashes(cases, store, agent_id)  # a number another agent holds (case 610.2)
    if apart:
        for top in apart:
            number = new_number(ledger_records(window), store, top, project_dir, folder)
            first = next(case for case in cases if in_family(case, top))
            found[first].append(
                f"case {top}: the store holds case {top} from the answer of another agent — "
                f"build this Case as case {number}"
            )
    heads = headings(text)
    repeated = True  # every Case with findings stands in the store as it is, findings and all
    fresh: list[str] = []  # the notes not yet sent for their Case id (case 472.1)
    for case, lines in cases.items():
        entry = {
            "text": shown_text(heads[case], lines),
            "findings": found[case],
            "stored": now.isoformat(),  # the time a sending must follow (case 452.1)
        }
        if agent_id:
            entry["agent_id"] = agent_id  # whose answer it is (case 610.2)
        key = f"{case}{AGENT_KEY}{agent_id}" if top_case(case) in apart else case
        held = store.get(key)
        if found[case] and not (
            isinstance(held, dict) and held.get("text") == entry["text"] and held.get("findings")
        ):
            repeated = False
        kept = list(held.get("notes") or []) if isinstance(held, dict) else []
        new = [note for note in notes[case] if note not in kept]
        fresh += new
        if kept or new:  # the notes sent for the id outlive a later answer (case 472.1)
            entry["notes"] = kept + new
        if isinstance(held, dict) and held.get("summary_sent"):  # the loop guard (case 662.3)
            entry["summary_sent"] = held["summary_sent"]
        store[key] = entry
    return [f for case in cases for f in found[case]], fresh, repeated


def clashes(cases: dict, store: dict, agent_id: str) -> list[str]:
    """The top-level Case of each family of the answer whose entry under the number alone —
    of the top-level Case or of one of its sub-cases — holds the answer of an agent other
    than `agent_id` (case 610.2). An entry with no `agent_id`, stored before the change, and
    an answer with none are not compared."""
    if not agent_id:
        return []
    found: list[str] = []
    for top in dict.fromkeys(top_case(case) for case in cases):
        held = {
            str(entry.get("agent_id"))
            for key, entry in store.items()
            if AGENT_KEY not in str(key)
            and in_family(str(key), top)
            and isinstance(entry, dict)
            and entry.get("agent_id")
        }
        if held - {agent_id}:
            found.append(top)
    return found


def send_back(findings: list[str], stderr) -> int:
    """Exit 2 with the findings on stderr, so Claude Code sends `case-guppi` back; 0 when
    there are none."""
    if not findings:
        return 0
    print("casecheck: " + "; ".join(findings), file=stderr)
    return 2


def ledger_records(lines: list[str]) -> list[dict]:
    """The records of the lines of a ledger that `parse_line` reads."""
    return [record for line in lines if (record := parse_line(str(line).strip()))]


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


RATIFICATION_HEAD = "> **ratification:**"


def fence_ledger_lines(lines: list[str]) -> list[str]:
    """The ledger lines of the `ratification` of a Case's lines, up to the horizontal rule."""
    kept: list[str] = []
    for line in lines:
        if line.strip() == RULE:
            break
        kept.append(line)
    text = quoted_sections(kept, ("ratification",)).get("ratification", "")
    return [line.strip() for line in text.splitlines() if line.strip().startswith(PREFIXES)]


def list_showing(case: str, lines: list[str]) -> dict[str, list[str]]:
    """Under the heading of a top-level Case, one `ratification` whose fence holds the
    ledger lines of its sub-cases — the list of a showing (case 561.10). Each id a line names →
    the lines of a `ratification` that holds that id's lines alone, in their order, in the
    chat form `quoted_sections` reads. Empty when `case` is a sub-case or no line names an id
    other than its own: then the Case is shown under its own heading, as before. The one
    reading of `stop` and of the Spec hook's `find_showing`."""
    if "." in case:
        return {}
    named: dict[str, list[str]] = {}
    for line in fence_ledger_lines(lines):
        record = parse_line(line)
        if record and record.get("record") == "decision":
            named.setdefault(str(record["case"]), []).append(line)
    if not named or set(named) == {case}:
        return {}
    return {
        sub: [RATIFICATION_HEAD, "> ```", *(f"> {line}" for line in own), "> ```"]
        for sub, own in named.items()
    }


def without_ratification(lines: list[str]) -> list[str]:
    """The lines of a Case with its `ratification` blockquote left out — the parent's own
    parts of a list showing, compared as before (case 561.10)."""
    kept: list[str] = []
    skipping = False
    for line in lines:
        if line.strip() == RATIFICATION_HEAD:
            skipping = True
            continue
        if skipping and line.startswith(">"):
            continue
        skipping = False
        kept.append(line)
    return kept


def showings(cases: dict[str, list[str]]) -> dict[str, list[str]]:
    """Case id → the lines that show it in a reply: each Case under its own heading with at
    least one of its sections, by `shows_sections`, and each sub-case named in the one
    `ratification` of a list showing under its top-level heading, by `list_showing` (case
    561.10). A Case shown under its own heading keeps that showing; a parent of a list is
    compared on its other parts alone."""
    shown: dict[str, list[str]] = {}
    listed: dict[str, list[str]] = {}
    for case, lines in cases.items():
        if not shows_sections(lines):
            continue
        subs = list_showing(case, lines)
        if subs:
            listed.update(subs)
            rest = without_ratification(lines)
            if shows_sections(rest):
                shown[case] = rest
        else:
            shown[case] = lines
    for case, lines in listed.items():
        shown.setdefault(case, lines)
    return shown


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


# --- the layout of a showing (case 611) ---------------------------------------------------

LIST_ITEM = re.compile(r"^(?:[-*] |\d+\. )")


def outside_the_list(reply: str) -> str | None:
    """The first text of a reply that shows a Case standing outside the layout
    `orchestration.md` sets, or None (case 611). Up to the horizontal rule, a line that is not blank
    before the first Case heading (`CASE_HEADING`), and under a Case heading any line but a
    blank one, a list item (`LIST_ITEM`), a line indented under a list item and the
    `ratification` blockquote — its `RATIFICATION_HEAD` and the `>` lines after it; a section
    other than `ratification` that `quoted_sections` reads under a heading is refused too.
    A horizontal rule before the first Case heading is passed over, and one whose next line
    that is not blank is a Case heading ends one Case of a batch, so the next is judged too
    (case 751.5). Text after a horizontal rule that no Case heading follows is not judged."""
    seen_heading = in_list = in_ratification = False
    block: list[str] = []

    def other_section() -> str | None:
        sections = quoted_sections(block, CHAT_SECTIONS)
        other = next((name for name in sections if name != "ratification"), None)
        return f"> **{other}:**" if other else None

    lines = reply.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if CASE_HEADING.match(line):
            if seen_heading and (section := other_section()):
                return section
            seen_heading, in_list, in_ratification, block = True, False, False, []
            continue
        if not stripped:
            block.append(line)
            continue
        if stripped == RULE:
            following = next((later for later in lines[index + 1 :] if later.strip()), "")
            if not seen_heading or CASE_HEADING.match(following):
                continue
            break
        if not seen_heading:
            return stripped
        block.append(line)
        if stripped == RATIFICATION_HEAD:
            in_ratification, in_list = True, False
            continue
        if in_ratification and stripped.startswith(">"):
            continue
        in_ratification = False
        if LIST_ITEM.match(line):
            in_list = True
            continue
        if in_list and line[:1] in (" ", "\t"):
            continue
        return stripped
    return other_section() if seen_heading else None


def showing_layout(records: list[dict], reply: str, since: int = -1) -> str | None:
    """The note on a reply that showed a Case with a text of the main agent's own outside
    its list and `ratification`, or None — a text written in the turn after the first summary
    of `case-guppi` came back, by `is_summary`, and before the last tool call, by
    `texts_after`, the judgment the check of a round uses, after the reply that the last
    refusal of the check follows, `since` (case 692.2); or a line of the reply by
    `outside_the_list` (case 611). A text written before the summary came back, and every
    text of a turn with no summary, is not judged. The `--prompt` run gives it at the
    person's next message, and the Case is not shown again (case 699.2)."""
    before = texts_after(records, is_summary, since)
    quoted = before[0] if before else outside_the_list(reply)
    if quoted is None:
        return None
    return (
        f"casecheck: your last reply showed a Case with a text of your own outside its list "
        f"and ratification: {quoted[:120]!r} — the Case stands as shown and is not shown "
        "again; at the next showing write nothing of your own before the Case but a "
        "horizontal rule and keep your own text after the horizontal rule"
    )


# --- how a round opens (case 562) ----------------------------------------------------------

RESULT = re.compile(r"<result>(.*?)</result>", re.DOTALL)
FACT = "**Fact:**"
# the bold label of the Context paragraph, translated: `**Контекст:**` or `**Context**:`
LABEL_LINE = re.compile(r"^\*\*[^*\n]+(?::\*\*|\*\*:)")


def opening_record(records: list[dict]) -> dict | None:
    """The record that opens the turn of the reply — the last person's message or returned
    answer, by `user_kind` of `.guppi/guppi/ledger.py`, as `turn_of_reply` judges it; None when the
    transcript holds none."""
    turn = turn_of_reply(records)
    index = len(records) - len(turn) - 1
    return records[index] if index >= 0 else None


def block_text(content) -> str:
    """The text of a `tool_result`'s content: a string, or the text blocks of a list."""
    if isinstance(content, str):
        return content
    blocks = content if isinstance(content, list) else []
    return "\n".join(
        str(block.get("text") or "")
        for block in blocks
        if isinstance(block, dict) and block.get("type") == "text"
    )


def turn_blocks(records: list[dict]):
    """`(index, position, record, block)` for each block of each record of the turn of the
    reply, in order: `index` the record's place in `records`, `position` the block's place in
    the turn, counted from 1 — the one numbering of `given_back_at` and `texts_after`."""
    turn = turn_of_reply(records)
    offset = len(records) - len(turn)
    position = 0
    for index, record in enumerate(turn, start=offset):
        message = record.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            position += 1
            if isinstance(block, dict):
                yield index, position, record, block


def given_back_at(records: list[dict]) -> list[tuple[int, str]]:
    """`(position, text)` for each text subagents gave back in the turn of the reply, by
    `turn_blocks` (measured 2026-10-01, session 2356): the answer to an `Agent` call stands in
    the `tool_result` of that call, inside the turn, at the position of that block; the answer
    to a `SendMessage` comes back after the turn has ended, as a `user` record with
    `origin.kind` `task-notification` whose content is a string holding the answer between
    `<result>` and `</result>` — a returned answer by `user_kind` of `.guppi/guppi/ledger.py`, which
    opens the turn, so it is read here as the turn's opener, at position 0, before every text
    of the turn (case 592)."""
    texts: list[tuple[int, str]] = []
    opener = opening_record(records)
    if isinstance(opener, dict) and user_kind(opener) == ANSWER:
        message = opener.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        texts += [(0, text) for text in RESULT.findall(content)] if isinstance(content, str) else []
    agent_calls = set()
    for _, position, _, block in turn_blocks(records):
        if block.get("type") == "tool_use" and block.get("name") == "Agent":
            agent_calls.add(block.get("id"))
        elif block.get("type") == "tool_result" and block.get("tool_use_id") in agent_calls:
            texts.append((position, block_text(block.get("content"))))
    return texts


def given_back(records: list[dict]) -> list[str]:
    """The texts subagents gave back in the turn of the reply, by `given_back_at`."""
    return [text for _, text in given_back_at(records)]


def is_round(text: str) -> bool:
    """A round of `case-guppi`, the one test of a round that every check of a round imports
    (case 601.1): no Case heading, no `**Fact:**` line before the first question, and a line
    that opens with `❓` — the mark alone, so a question whose title line is out of form still
    makes the text a round. The lines are read with their indent set aside: the harness
    indents a hand-back."""
    lines = [line.strip() for line in text.splitlines()]
    if split_cases("\n".join(lines)) or is_fact(text):
        return False
    return any(line.startswith(QUESTION_MARK) for line in lines)


def is_fact(text: str) -> bool:
    """A Fact answer of `case-guppi`, the one test of it that `is_round` and `answer_of`
    share (case 607.1): no Case heading, and a line that opens with `**Fact:**` before any
    line that opens with `❓`. The lines are read with their indent set aside."""
    lines = [line.strip() for line in text.splitlines()]
    if split_cases("\n".join(lines)):
        return False
    for line in lines:
        if line.startswith(FACT):
            return True
        if line.startswith(QUESTION_MARK):
            return False
    return False


def texts_after(records: list[dict], finds, since: int = -1) -> list[str]:
    """The texts the main agent wrote in the turn of the reply before its last tool call,
    after the first text given back in the turn that `finds` finds — a round by `is_round`, a
    summary by `is_summary` — and in a record after `since`, the index in `records` of the
    reply that the last refusal of the check follows (`last_refused`), -1 for none (case
    692). A text written before that text came back cannot be taken back, so it is not judged;
    a text given back in the returned answer that opens the turn stands before every text of
    the turn. Empty when no text given back is one that `finds` finds."""
    start = next((at for at, text in given_back_at(records) if finds(text)), None)
    if start is None:
        return []
    texts: list[tuple[int, str]] = []
    last_call = -1
    for index, position, record, block in turn_blocks(records):
        if record.get("type") != "assistant":
            continue
        if block.get("type") == "text" and str(block.get("text") or "").strip():
            if position > start and index > since:
                texts.append((position, str(block["text"]).strip()))
        elif block.get("type") == "tool_use":
            last_call = position
    return [text for at, text in texts if at < last_call]


def round_opening(
    records: list[dict], reply: str, after_prespec: bool, since: int = -1
) -> str | None:
    """The note on a reply that showed a round of `case-guppi` after a text of the main
    agent's own, or None (case 562). The turn holds a round when a text given back in it, by
    `given_back`, is one by `is_round`. Before `/pre-spec` — no `prespec` line of the session
    after its `hi` — a text of the main agent written after the first round of the turn came
    back and before the last tool call, by `texts_after`, is a fault, and only after the reply
    that the last refusal of the check follows, `since` (case 692.1); always, a reply whose
    first line that is neither blank nor the horizontal rule opens neither with `❓ ` nor with
    a bold label that ends in a colon (case 751.4). After `/pre-spec` only the first line is judged: in the loop over its findings each
    answer of a `case-guppi` comes back in a turn of its own, and the text the main agent
    writes there is set by `rule-prespec` (case 581.2). Text after the last question is not
    judged. The `--prompt` run gives the note at the person's next message, and the round is
    not shown again (case 699.1)."""
    if not any(is_round(text) for text in given_back(records)):
        return None
    before = [] if after_prespec else texts_after(records, is_round, since)
    first = next(
        (line.strip() for line in reply.splitlines() if line.strip() not in ("", RULE)), ""
    )
    if not before and (first.startswith("❓ ") or LABEL_LINE.match(first)):
        return None
    quoted = before[0] if before else first
    return (
        f"casecheck: your last reply showed a round of case-guppi after a text of your own: "
        f"{quoted[:120]!r} — the round stands as shown and is not shown again; open the next "
        "round with its Context paragraph or its first question, with nothing before it but a "
        "horizontal rule"
    )


COMMAND = f"{PROJECT_RUN}guppi casecheck"  # the command of the `Stop` run, as its refusal names it
LIMIT = 3  # the refusals of one Case, or of one other reason, a stretch (case 688.1)
REASON_CASE = re.compile(r"^(case [^:]+):")


def own_told(payload: dict) -> list[str] | None:
    """The text of each refusal of the `Stop` run in the stretch, by `refusals` of
    `.guppi/guppi/ledger.py` — the one judgment of the refusals, which `guppi onward` calls; None
    when the transcript cannot be read (case 688.1)."""
    found = refusals(payload, COMMAND)
    return None if found is None else [text for _, text in found[COMMAND]]


def last_refused(records: list[dict]) -> int:
    """The index in `records`, the main-agent records of the transcript, of the reply that
    the last refusal of the `Stop` run in their stretch follows, by `stretch_of` and
    `refusals_in` of `.guppi/guppi/ledger.py` — the one judgment of the refusals and of the stretch;
    -1 when none stands (case 692)."""
    span = stretch_of(records)
    found = refusals_in(span, COMMAND)[COMMAND]
    return len(records) - len(span) + found[-1][0] if found else -1


def times_given(reason: str, told: list[str]) -> int:
    """How many refusals of the stretch hold a reason of the Case `reason` names — any reason
    that opens with the same `case <id>:` — or, for a reason that names no Case, the same
    reason (case 688.1)."""
    match = REASON_CASE.match(reason)
    key = match.group(0) if match else reason
    return sum(1 for text in told if f"casecheck: {key}" in text or f"; {key}" in text)


def give(problems: list[str], told: list[str], stderr) -> int:
    """The reasons of the `Stop` run under the count (case 688.1): each reason still given
    fewer than `LIMIT` times in the stretch exits 2 on stderr; when none is left, the run
    exits 0 with one line per Case it lets through, which the Spec hook compares at
    ratification."""
    if not problems:
        return 0
    left = [problem for problem in problems if times_given(problem, told) < LIMIT]
    if left:
        print("casecheck: " + "; ".join(left), file=stderr)
        return 2
    for case in dict.fromkeys(m.group(1) for p in problems if (m := REASON_CASE.match(p))):
        print(
            f"casecheck: {case} shown unchecked after three refusals; the Spec hook compares it "
            "at ratification",
            file=stderr,
        )
    return 0


def stop(payload: dict, project_dir: Path, now, stderr) -> int:
    told = own_told(payload)
    if told is None and payload.get("stop_hook_active"):
        return 0  # the flag set and no transcript to count by: it cannot tell its own loop
    told = told or []
    stamp = session_stamp(None, payload)
    folder = session_dir(project_dir, now, stamp)
    if folder is None:
        return 0
    reply = reply_text(payload)
    cases = split_cases(reply)
    heads = headings(reply)
    shown = showings(cases)
    logs = session_event_logs(project_dir, now, stamp)
    turn_records = transcript_records(payload)
    if not shown:  # a layout fault is told at the next message (cases 699.1, 699.2)
        return 0
    store = read_store(plan_path(logs, stamp))
    problems = [
        problem
        for case, lines in shown.items()
        if (problem := against_store(case, heads.get(case, ""), lines, store))
    ]
    for top in dict.fromkeys(top_case(case) for case in shown):  # its file (case 645.4)
        if folder is not None and (changed := changed_file(folder, top, store)):
            problems.append(changed)
    turn = turn_of_reply(turn_records)
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
    return give(problems, told, stderr)


PROMPT_FLAG = "--prompt"


def before_message(records: list[dict]) -> list[dict]:
    """The main-agent records before the person's message the `UserPromptSubmit` payload
    carries: the records from the last person's message on, by `user_kind` of
    `.guppi/guppi/ledger.py`, are left out when no reply of the agent follows it — the transcript
    may hold that message already."""
    for index in range(len(records) - 1, -1, -1):
        if records[index].get("type") == "assistant":
            return records
        if user_kind(records[index]) == PERSON:
            return records[:index]
    return records


def last_reply(records: list[dict]) -> str:
    """The text of the last reply of the main agent: the text blocks of the turn, by
    `turn_blocks`, after its last tool call."""
    texts: list[str] = []
    for _, _, record, block in turn_blocks(records):
        if record.get("type") != "assistant":
            continue
        if block.get("type") == "tool_use":
            texts = []
        elif block.get("type") == "text" and str(block.get("text") or "").strip():
            texts.append(str(block["text"]))
    return "\n\n".join(texts)


def prompt_note(payload: dict, project_dir: Path, now) -> str | None:
    """The note on the layout of the last reply of the main agent before the person's
    message, or None — `round_opening` when its turn holds a round, and `showing_layout` when
    the reply shows a Case by `showings`; each judges only what follows the reply the last
    refusal of the `Stop` run follows, `last_refused` (cases 699.1, 699.2)."""
    records = before_message(transcript_records(payload))
    reply = last_reply(records)
    if not reply:
        return None
    stamp = session_stamp(None, payload)
    logs = session_event_logs(project_dir, now, stamp)
    _, after_prespec = prespec_window("".join(text for _, text in logs), stamp)
    since = last_refused(records)
    notes = [round_opening(records, reply, after_prespec, since)]
    if showings(split_cases(reply)):
        notes.append(showing_layout(records, reply, since))
    found = [note for note in notes if note]
    return "; ".join(found) if found else None


def run(
    argv, *, stdin=None, stdout=None, stderr=None, project_dir: Path | None = None, now=None
) -> int:
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    project_dir = project_root() if project_dir is None else Path(project_dir)
    now = datetime.now().astimezone() if now is None else now
    argv = argv or []
    try:
        payload = read_payload(stdin)
    except Exception as exc:  # noqa: BLE001 — no payload, no way to tell a re-fire (case 555.1)
        if PROMPT_FLAG not in argv:
            print(f"casecheck: not checked: {exc}", file=stderr)
        return 0
    if not payload:
        if PROMPT_FLAG not in argv:
            print("casecheck: payload not readable, nothing checked", file=stderr)
        return 0
    if PROMPT_FLAG in argv:  # never blocks the person's message (case 699.1)
        try:
            note = prompt_note(payload, project_dir, now)
        except Exception as exc:  # noqa: BLE001 — its own error goes to stderr
            print(f"casecheck: not checked: {exc}", file=stderr)
            return 0
        if note:
            print(note, file=stdout)
        return 0
    if "--subagent" in argv:
        try:
            return subagent(payload, project_dir, now, stderr)
        except Exception as exc:  # noqa: BLE001 — a send-back would loop (case 555.1)
            print(f"casecheck: not checked: {exc}", file=stderr)
            return 0
    try:
        return stop(payload, project_dir, now, stderr)
    except Exception as exc:  # noqa: BLE001 — shown to the agent, not swallowed (case 555.1)
        reason = f"not checked: {exc}. Fix the cause, then show the Case again."
        try:
            told = own_told(payload)
        except Exception:  # noqa: BLE001 — judged as a transcript it cannot read
            told = None
        if told is None and payload.get("stop_hook_active"):
            return 0
        return give([reason], told or [], stderr)  # at most three times a stretch (case 688.4)
