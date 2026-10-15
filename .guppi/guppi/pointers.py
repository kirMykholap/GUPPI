"""The judgment of a pointer — a reference to a case, an id `decision-case-N` or a mention of a
session by its id, each id of a list included — that stands outside a bracket of its own.

A pointer stands in a bracket of its own at the end of its sentence, with the words that go
with it (case 807.1). `outside` is the one judgment of a pointer outside such a bracket, which
`guppi ship` of `.guppi/guppi/ship.py` runs over each file it writes and `/pre-spec` of
`.guppi/guppi/prespec.py` runs over the new text of a page; both import it from here, and
neither holds a copy (case 820). `removed` takes each bracket that holds a pointer out whole,
and `masked` puts each sample aside first — a code span by `CODE_SPAN` of
`.guppi/guppi/lint.py`, and each line of a fenced block — so that no pointer in a sample is
judged; `unmasked` puts the samples back. In a test file under `.guppi/tests/`, `masked_strings`
puts aside in place of them each string of the Python source that is no docstring, read by
`tokenize` through `python_strings`, and the code around the strings with it, so that the
cleaning and `outside` take only the comments and the docstrings: a case id in the data of a
test is neither removed nor judged, and no bracket of the code is taken for one that holds a
pointer of a comment inside it (case 822). `python_strings` is the one judgment of a
docstring, which `bare_numbers` of `ship.py` imports too. A case id after `[case `, `#case-`
or `:case ` — the
form of a ledger line or a mark — is no pointer. The module stands apart from `ship.py`
because the clean version holds this module and not that one (case 820.5). Nothing here
reads or writes a file. Rule page: `vault/wiki/rules/rule-clean-branch.md`.
"""

import re
import tokenize
from io import StringIO

from guppi.caseid import ID
from guppi.lint import CODE_SPAN

# a reference to a case: the word `case` or `cases`, either case, and one or more ids of
# `ID`, joined by a comma, a semicolon or `and`; not the form of a line after `[`, `#` or
# `:`, and not part of a longer word
REFS = re.compile(
    rf"(?<![\[#:\w-])[Cc]ases?\s+{ID}(?:(?:\s*[,;]\s*|\s+and\s+)(?:[Cc]ases?\s+)?{ID})*\b"
)
DECISION_LINK = re.compile(rf"[ \t]?\[\[decision-case-{ID}(?:[|#][^\]]*)?\]\]")
DECISION = re.compile(rf"\bdecision-case-{ID}")
# a mention of a session by its id, each id of a list included, as `REFS` takes a list
SESSION_ID = r"(?:\d{4}-\d\d-\d\d/)?\d{4}"
SESSION = re.compile(
    rf"\b[Ss]essions?\s+{SESSION_ID}"
    rf"(?:(?:\s*[,;]\s*|\s+and\s+)(?:[Ss]essions?\s+)?{SESSION_ID})*\b"
)
POINTERS = (
    ("a reference to a case", REFS),
    ("a reference to a decision", DECISION),
    ("a mention of a session", SESSION),
)
# a bracket with no bracket inside it, on one line or across lines, and the space before it;
# a bracket that opens a line and a mark of punctuation follows takes the line break before
# it, so the mark joins the line above and does not stand alone
BRACKET = re.compile(r"(\n[ \t]*(?=\([^()]*\)[.,;:])|[ \t]?)\(([^()]*)\)")
SEPARATORS = re.compile(r"[\s,;]+|\band\b")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
MASK = "\x00{}\x00"
MASKED = re.compile(r"\x00(\d+)\x00")
# the tokens after which a statement opens: a string there, and alone in its statement, is a
# docstring
STATEMENT_START = {
    tokenize.NEWLINE,
    tokenize.NL,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.ENCODING,
}


def holds_pointer(text: str) -> bool:
    return any(pattern.search(text) for _, pattern in POINTERS)


def masked(text: str, sample: bool) -> tuple[str, list[str]]:
    """The text with each sample put aside, and the samples: with `sample`, each code span,
    each line of a fenced block. A line keeps its place, so the lines of the text keep their
    numbers."""
    spans: list[str] = []

    def keep(part: str) -> str:
        spans.append(part)
        return MASK.format(len(spans) - 1)

    if not sample:
        return text, spans
    lines, fence = text.split("\n"), None
    for number, line in enumerate(lines):
        opener = FENCE.match(line)
        if fence is None and opener:
            fence = opener.group(1)
            lines[number] = keep(line)
        elif fence is not None:
            if opener and opener.group(1)[0] == fence[0] and len(opener.group(1)) >= len(fence):
                fence = None
            lines[number] = keep(line)
        else:
            lines[number] = CODE_SPAN.sub(lambda m: keep(m.group(0)), line)
    return "\n".join(lines), spans


def python_strings(text: str) -> list[tuple[int, int, bool]]:
    """`(start, end, docstring)` for each string of the Python source `text`, as offsets into
    it, read by `tokenize`, so that no code is taken for a string: an f-string whole, from its
    prefix to its closing quote. A docstring is a string that a statement is alone. The one
    judgment of a docstring, which `masked_strings` and `bare_numbers` of
    `.guppi/guppi/ship.py` read. A text that does not tokenize gives none."""
    try:
        tokens = list(tokenize.generate_tokens(StringIO(text).readline))
    except (tokenize.TokenError, SyntaxError):
        return []
    starts = [0]
    for line in text.split("\n"):
        starts.append(starts[-1] + len(line) + 1)

    def offset(row_col: tuple[int, int]) -> int:
        return starts[row_col[0] - 1] + row_col[1]

    skipped = (tokenize.COMMENT, tokenize.NL)
    found, at_start, depth, opened = [], True, 0, 0
    for index, token in enumerate(tokens):
        if token.type == tokenize.FSTRING_START:
            if depth == 0:
                opened = offset(token.start)
            depth += 1
        elif token.type == tokenize.FSTRING_END:
            depth -= 1
            if depth == 0:
                found.append((opened, offset(token.end), False))
        elif token.type == tokenize.STRING and depth == 0:
            docstring = False
            if at_start:
                after = next((t for t in tokens[index + 1 :] if t.type not in skipped), None)
                docstring = after is None or after.type in (tokenize.NEWLINE, tokenize.ENDMARKER)
            found.append((offset(token.start), offset(token.end), docstring))
        if token.type not in skipped:
            at_start = token.type in STATEMENT_START
    return found


def masked_strings(text: str) -> tuple[str, list[str]]:
    """The Python source `text` with each string that is no docstring put aside as a sample,
    and the code around the strings with it, so that only its comments and its docstrings
    stand; and the samples. In a test such a string is the data of the test (case 822). Each
    line of a sample is put aside alone, so the lines of the text keep their numbers;
    `unmasked` puts the samples back. A text that does not tokenize is put aside in no part."""
    try:
        tokens = list(tokenize.generate_tokens(StringIO(text).readline))
    except (tokenize.TokenError, SyntaxError):
        return text, []
    starts = [0]
    for line in text.split("\n"):
        starts.append(starts[-1] + len(line) + 1)
    kept = [
        (starts[t.start[0] - 1] + t.start[1], starts[t.end[0] - 1] + t.end[1])
        for t in tokens
        if t.type == tokenize.COMMENT
    ]
    kept += [(start, end) for start, end, docstring in python_strings(text) if docstring]
    spans: list[str] = []

    def keep(part: str) -> str:
        if not part:
            return part
        spans.append(part)
        return MASK.format(len(spans) - 1)

    def aside(part: str) -> str:
        return "\n".join(keep(line) for line in part.split("\n"))

    out, at = [], 0
    for start, end in sorted(kept):
        out += [aside(text[at:start]), text[start:end]]
        at = end
    out.append(aside(text[at:]))
    return "".join(out), spans


def unmasked(text: str, spans: list[str]) -> str:
    return MASKED.sub(lambda m: spans[int(m.group(1))], text)


def words_beside(inner: str) -> bool:
    """Whether a bracket holds a word beside its pointers."""
    rest = inner
    for _, pattern in POINTERS:
        rest = pattern.sub("", rest)
    return bool(SEPARATORS.sub("", rest))


def removed(body: str, keep_lines: bool = True) -> tuple[str, list[tuple[int, str]]]:
    """`body` with each bracket that holds a pointer removed whole, and `(line, bracket)`
    for each removed bracket that holds a word beside its pointers. With `keep_lines` a
    removed bracket leaves its line breaks, so the lines keep their numbers."""
    review = []

    def drop(match: re.Match) -> str:
        if not holds_pointer(match.group(2)):
            return match.group(0)
        if words_beside(match.group(2)):
            line = body.count("\n", 0, match.start(2)) + 1
            review.append((line, f"({match.group(2)})"))
        return "\n" * match.group(0).count("\n") if keep_lines else ""

    return BRACKET.sub(drop, body), review


def outside(text: str, sample: bool = True, strings: bool = False) -> list[tuple[int, str]]:
    """`(line, what)` for each pointer that stands outside a bracket of its own: the one
    judgment of a pointer, which `guppi ship` runs over the files it writes and
    `.guppi/guppi/prespec.py` over the new text of a page. With `strings`, for a test file,
    the samples are the strings of `masked_strings` in place of those of `masked`."""
    body, _ = masked_strings(text) if strings else masked(text, sample)
    body, _ = removed(DECISION_LINK.sub("", body))
    out = []
    for number, line in enumerate(body.split("\n"), start=1):
        for what, pattern in POINTERS:
            out += [(number, f"{what}: {m.group(0)}") for m in pattern.finditer(line)]
    return out
