#!/usr/bin/env python3
"""The writer of the vault's `measure` regions -- and the only thing that writes a gauge's number.

WHY A SCRIPT AND NOT A LIBRARIAN. The owner ruled on 2026-08-25 that the agent decides and the
script does the mechanical work, so that the number in a page is not stochastic. The session that
proposed the opposite had, that same day, written about forty `measure:` destinations in a grammar
decided the day before and never read. The party writing a line by hand is the party that does not
know the slug.

THE TWO ROLES A MEASUREMENT CAN HAVE, and the role decides what the line may carry:

  gauge      a number that can be PRINTED. The line names the subject and the command, and
             carries no value written by a hand. `--refresh` runs the command and writes the
             reading beside it. This is what keeps the live prohibition intact -- a gauge that
             can be printed is never written by hand -- rather than overturning it.
  testimony  a reading that cannot be re-taken: what it was, under what conditions, on what day.
             It is appended and never replaced, because a past reading does not stop having
             happened when a later one disagrees.

THE REGION, decided 2026-08-24: a marked section legal in any folder, required nowhere, with no
frontmatter flag beside it. A flag would restate what a sweep of the bodies can already see, and
two records of one fact drift.

    <!-- measure -->
    - gauge: <subject-slug> -- `<command>` -- not yet read
    - gauge: <subject-slug> -- `<command>` -- <reading> -- read <date>
    - testimony: <text> -- conditions: <text> -- taken <date>
    <!-- /measure -->

THE LINE SPELLING IS THIS FILE'S, and it is written here rather than in a page because nothing in
the vault decided it: what was decided is one line per number, the role first, and no value on a
gauge line. THE COMMAND IS FENCED IN BACKTICKS AND THE READING FOLLOWS THE LAST ONE, which is the
whole of the parse. A separator character would have to be one that cannot appear inside a shell
command, and there is none: the first gauge this project will write names a command containing a
pipe.

THE EXIT CODE FORK, NAMED RATHER THAN DISCOVERED. This script uses 2 for a refusal AND for a usage
error, following `vault-archive.sh`; the gate, the catalogue, the coverage and the authority
scripts use 2 for a usage error alone. So the gate rule that calls `--check` READS THE LINES AND
NEVER THE CODE -- the shape rules 12 and 13 already use.

WHAT `--check` REFUSES TO DO, and it is a design decision rather than an omission:

  - it EXECUTES NOTHING. Comparing every gauge against a fresh run would execute arbitrary
    commands taken from page content at unbounded cost, and one gauge may name a command that
    costs 38 minutes. What protects a gauge from a lie is that it names the command anyone can
    re-run: that is re-checkability, not a guarantee.
  - it does NOT judge gauge uniqueness over the corpus. That verdict is deferred by decision. The
    fifth refusal below is a WRITER'S refusal -- it stops one write -- which is a different thing
    from a sweep issuing a verdict over pages nobody is writing.

Run:
  uv run python scripts/vault-measure.py --check
  uv run python scripts/vault-measure.py --refresh
  uv run python scripts/vault-measure.py --page <slug> --role gauge --subject <slug> --command <command>
  uv run python scripts/vault-measure.py --page <slug> --role testimony --value <text> --conditions <text>
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover
        pass

REPO = Path(__file__).resolve().parent.parent

OPEN = "<!-- measure -->"
CLOSE = "<!-- /measure -->"

# Detected LOOSELY and judged STRICTLY, which is rule 11's shape and is here for its reason: a
# pattern matching only the exact form makes a typo invisible rather than wrong, and six checks in
# this project have reported green while examining nothing.
LOOSE_OPEN = re.compile(r"^<!--\s*measure\s*-->\s*$")
LOOSE_CLOSE = re.compile(r"^<!--\s*/\s*measure\s*-->\s*$")
LOOSE_ANY = re.compile(r"^<!--\s*/?\s*measure\b.*-->\s*$")

GAUGE = re.compile(r"^-\s+gauge:\s*(?P<subject>[^`]*?)\s*--\s*`(?P<command>.+)`\s*(?P<tail>.*)$")
TESTIMONY = re.compile(r"^-\s+testimony:\s*(?P<body>.+)$")

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def say(message: str) -> None:
    print(f"VAULT-MEASURE: {message}")


def die(message: str) -> None:
    """Refuse loudly, and on stderr. A writer that fails towards doing nothing is
    indistinguishable from one that was never run."""
    print(f"VAULT-MEASURE: {message}", file=sys.stderr)
    sys.exit(2)


def vault() -> Path:
    """The vault is the top-level directory holding a `wiki/`.

    `$VAULT` WINS WHEN IT IS SET, because the gate exports it and the suite renames the vault
    inside a sandbox to prove nothing hard-codes the name. Falling back to a search keeps the
    script runnable by hand, which is how the librarian will use it.
    """
    named = os.environ.get("VAULT")
    if named:
        candidate = Path(named)
        if not candidate.is_absolute():
            candidate = REPO / candidate
        if (candidate / "wiki").is_dir():
            return candidate
        die(f"$VAULT names {candidate}, which holds no wiki/")
    for candidate in sorted(REPO.iterdir()):
        if candidate.is_dir() and (candidate / "wiki").is_dir():
            return candidate
    die("no directory holding a wiki/ under the repository, and $VAULT names none")


def pages(root: Path) -> list[Path]:
    return sorted(root.glob("*/*.md"))


def frontmatter_status(text: str) -> str:
    """The `status:` field, or the empty string. Read with a regex rather than a YAML parser
    because this repository adds no dependencies, and because the field is one flat scalar."""
    match = re.search(r"^status:\s*(\S+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else ""


def find_page(root: Path, slug: str) -> Path:
    """Resolve a slug to exactly one page, and refuse rather than guess.

    TWO OF THE FIVE REFUSALS LIVE HERE. A slug nothing answers is a typo that would otherwise be a
    silently dropped number -- the failure the coverage script's `BAD VERDICT` exists against --
    and a slug two folders answer is a question this script may not decide, because which page a
    measurement belongs on is exactly the judgement the librarian is for.
    """
    hits = [p for p in pages(root) if p.stem == slug]
    if not hits:
        die(f"no page with the slug '{slug}' under {root} - a destination naming no page "
            "would be a number written into nothing")
    if len(hits) > 1:
        where = ", ".join(sorted(p.parent.name for p in hits))
        die(f"the slug '{slug}' is in {len(hits)} folders ({where}) - which page the measurement "
            "belongs on is the librarian's judgement, not this script's")
    return hits[0]


def region_bounds(lines: list[str], path: Path) -> tuple[int, int] | None:
    """The half-open bounds of the one measure region in a file, or None.

    Refuses on broken markup rather than repairing it: an unclosed region, a close with no open,
    and a second region in one file are all things a writer must not paper over.
    """
    opens = [i for i, line in enumerate(lines) if LOOSE_OPEN.match(line)]
    closes = [i for i, line in enumerate(lines) if LOOSE_CLOSE.match(line)]
    if not opens and not closes:
        return None
    if len(opens) > 1:
        die(f"{path}: two measure regions in one file - one page carries one region")
    if not opens:
        die(f"{path}:{closes[0] + 1}: closes a measure region that was never opened")
    if not closes:
        die(f"{path}:{opens[0] + 1}: the measure region is opened and never closed")
    if closes[0] < opens[0]:
        die(f"{path}:{closes[0] + 1}: a measure region is closed before it is opened")
    return opens[0] + 1, closes[0]


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n")


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines), encoding="utf-8")


def gauge_subjects(root: Path, exclude: Path | None = None) -> dict[str, Path]:
    """Every gauge subject carried by a `current` page, and the page carrying it.

    ONLY `current` PAGES ANSWER. A deprecated page's gauge is a record of what was once measured
    and does not reserve the subject -- the same join rule 11 uses when it decides which rule page
    a region may name.
    """
    found: dict[str, Path] = {}
    for page in pages(root):
        if exclude is not None and page == exclude:
            continue
        text = page.read_text(encoding="utf-8", errors="replace")
        if OPEN not in text:
            continue
        if frontmatter_status(text) != "current":
            continue
        lines = text.split("\n")
        bounds = region_bounds(lines, page)
        if bounds is None:
            continue
        for line in lines[bounds[0]:bounds[1]]:
            match = GAUGE.match(line)
            if match:
                found.setdefault(match.group("subject").strip(), page)
    return found


# --- the write mode ---------------------------------------------------------------------------


def ensure_region(lines: list[str], path: Path) -> tuple[int, int]:
    """The region's bounds, creating an empty region at the end of the body if there is none.

    CREATED RATHER THAN REFUSED, and said out loud because it is the one place this script writes
    something nobody asked for. A page's first measurement would otherwise need a hand-written
    region before the script that exists to stop hand-writing could run -- which is the failure
    this whole mechanism was built against.
    """
    bounds = region_bounds(lines, path)
    if bounds is not None:
        return bounds
    while lines and lines[-1].strip() == "":
        lines.pop()
    lines += ["", "# Measure", "", OPEN, CLOSE, ""]
    say(f"{path}: no measure region - created one at the end of the page")
    #    THE BOUNDS ARE THE CONTENT'S, NOT THE MARKERS'. `OPEN` sits at len-3 and `CLOSE` at
    #    len-2, so the empty span between them is (len-2, len-2). Off by one here puts every
    #    first measurement ABOVE the opening marker, where the region reads as empty and the
    #    refresh pass walks past a gauge it cannot see - caught by the selftest, which went red
    #    in fourteen cases at once for this one line.
    return len(lines) - 2, len(lines) - 2


def write_measurement(root: Path, args: argparse.Namespace) -> int:
    page = find_page(root, args.page)
    lines = read_lines(page)
    start, end = ensure_region(lines, page)
    body = lines[start:end]
    # THE LOCAL DATE, DELIBERATELY, and the linter is silenced rather than obeyed. Every date in
    # this store is a calendar day of the owner's, not an instant: a correction note is dated the
    # day the text became false, and a measurement is dated the day it was taken. UTC would stamp
    # yesterday on anything measured late in his evening, which is a wrong answer to the question
    # the date is asked.
    today = date.today().isoformat()  # noqa: DTZ011

    if args.role == "gauge":
        # THE THIRD REFUSAL. A gauge with no command is a value waiting to be typed by a hand,
        # which is the thing the prohibition forbids; a gauge with no subject cannot be replaced
        # by a later reading, and one page may legitimately carry several gauges.
        if not args.command:
            die("a gauge names the command that prints it: --command is required. A gauge "
                "carrying a value instead of a command is a number written by a hand")
        if not args.subject:
            die("a gauge needs --subject: one page can carry more than one gauge, so the "
                "subject cannot default to the page, and it is what a later reading replaces")
        if not SLUG.match(args.subject):
            die(f"'{args.subject}' is not a subject slug - lower case, digits and single hyphens")
        if args.value:
            die("a gauge takes no --value. The line names the command and --refresh writes the "
                "reading beside it")

        # THE FIFTH REFUSAL, AND IT IS THE WRITER'S ALONE. A sweep issuing this verdict over the
        # whole corpus is deferred by decision and is NOT built here: this stops one write, at the
        # moment a subject would become ambiguous, and says which page already holds it.
        taken = gauge_subjects(root, exclude=page).get(args.subject)
        if taken is not None:
            die(f"the gauge subject '{args.subject}' is already carried by {taken} - two current "
                "pages claiming one subject is two numbers that will disagree")

        line = f"- gauge: {args.subject} -- `{args.command}` -- not yet read"
        # A GAUGE IS REPLACED BY SUBJECT and testimony is appended: a gauge is the current
        # reading of a live thing, so a second one supersedes the first rather than sitting
        # beside it.
        for index, existing in enumerate(body):
            match = GAUGE.match(existing)
            if match and match.group("subject").strip() == args.subject:
                body[index] = line
                lines[start:end] = body
                write_lines(page, lines)
                say(f"{page}: gauge '{args.subject}' replaced - run --refresh to read it")
                return 0
        body.append(line)
    else:
        if not args.value:
            die("testimony needs --value: the reading itself")
        # THE FOURTH REFUSAL. A reading with no conditions cannot be compared with a later one,
        # and comparing two numbers taken under different conditions is how this project has
        # already reported a change that did not happen.
        if not args.conditions:
            die("testimony needs --conditions: a reading whose conditions are not written down "
                "cannot be compared with the next one, and will be")
        if args.command or args.subject:
            die("testimony takes no --command and no --subject: it is a reading that cannot be "
                "re-taken, which is what makes it testimony rather than a gauge")
        body.append(f"- testimony: {args.value} -- conditions: {args.conditions} -- taken {today}")

    lines[start:end] = body
    write_lines(page, lines)
    say(f"{page}: {args.role} written")
    return 0


# --- the refresh pass -------------------------------------------------------------------------


def run_command(command: str) -> tuple[bool, str]:
    """Run one gauge's command and return its single line.

    THROUGH `bash -c`, because every command this project writes down is a bash command, and
    running them through the host shell would make a gauge's meaning depend on which shell read
    it. NO TIMEOUT, deliberately: one gauge names a command that costs 38 minutes, and cutting it
    off would write a number that is not the answer.
    """
    try:
        # `check=False` IS THE BEHAVIOUR AND NOT AN OVERSIGHT: this runs a gauge's own command and
        # a non-zero exit is one of the answers it may give, read below rather than raised here.
        done = subprocess.run(["bash", "-c", command], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", check=False)
    except FileNotFoundError:
        return False, "bash is not on the PATH, and every gauge command is a bash command"
    if done.returncode != 0:
        first = (done.stderr or done.stdout).strip().split("\n")[0]
        return False, f"the command exited {done.returncode}: {first}"
    printed = [line for line in done.stdout.split("\n") if line.strip()]
    if not printed:
        return False, "the command printed nothing - a gauge command prints the line wanted"
    if len(printed) > 1:
        return False, (f"the command printed {len(printed)} lines - a gauge command prints "
                       "exactly the line wanted, and choosing among several is not this "
                       "script's judgement")
    return True, printed[0].strip()


def refresh(root: Path) -> int:
    """Walk every measure region, run each gauge's command, write each number beside it."""
    read = written = refused = 0
    # THE LOCAL DATE, DELIBERATELY, and the linter is silenced rather than obeyed. Every date in
    # this store is a calendar day of the owner's, not an instant: a correction note is dated the
    # day the text became false, and a measurement is dated the day it was taken. UTC would stamp
    # yesterday on anything measured late in his evening, which is a wrong answer to the question
    # the date is asked.
    today = date.today().isoformat()  # noqa: DTZ011
    for page in pages(root):
        text = page.read_text(encoding="utf-8", errors="replace")
        if OPEN not in text:
            continue
        lines = text.split("\n")
        bounds = region_bounds(lines, page)
        if bounds is None:
            continue
        start, end = bounds
        changed = False
        for index in range(start, end):
            match = GAUGE.match(lines[index])
            if not match:
                continue
            read += 1
            ok, result = run_command(match.group("command"))
            if not ok:
                say(f"{page}: gauge '{match.group('subject').strip()}' not read - {result}")
                refused += 1
                continue
            # THE TAIL IS REPLACED WHOLE, never appended to, so a region refreshed twice does not
            # grow a history of readings inside one line. The history of a gauge is git's.
            fresh = (f"- gauge: {match.group('subject').strip()} -- `{match.group('command')}` "
                     f"-- {result} -- read {today}")
            if fresh != lines[index]:
                lines[index] = fresh
                changed = True
                written += 1
        if changed:
            write_lines(page, lines)
    say(f"refresh: {read} gauge(s) read, {written} written, {refused} refused")
    return 2 if refused else 0


# --- the check --------------------------------------------------------------------------------


def check(root: Path) -> int:
    """Shape only. EXECUTES NOTHING -- see the module docstring for why that is a decision."""
    problems = 0
    regions = 0
    for page in pages(root):
        text = page.read_text(encoding="utf-8", errors="replace")
        lines = text.split("\n")

        # MALFORMED MARKERS ARE CAUGHT BEFORE THE STRICT PASS, so a mistyped marker is wrong
        # rather than invisible. `<!-- measure: subject -->` is the likeliest mistake: it is the
        # form every OTHER region in this repository takes.
        for number, line in enumerate(lines, start=1):
            if LOOSE_ANY.match(line) and not (LOOSE_OPEN.match(line) or LOOSE_CLOSE.match(line)):
                say(f"{page}:{number}: malformed measure marker - the form is exactly "
                    f"'{OPEN}' and '{CLOSE}', alone on the line")
                problems += 1

        opens = [i for i, line in enumerate(lines) if LOOSE_OPEN.match(line)]
        closes = [i for i, line in enumerate(lines) if LOOSE_CLOSE.match(line)]
        if not opens and not closes:
            continue
        if len(opens) > 1:
            say(f"{page}: two measure regions in one file - one page carries one region")
            problems += 1
            continue
        if not opens:
            say(f"{page}:{closes[0] + 1}: closes a measure region that was never opened")
            problems += 1
            continue
        if not closes:
            say(f"{page}:{opens[0] + 1}: the measure region is opened and never closed")
            problems += 1
            continue
        if closes[0] < opens[0]:
            say(f"{page}:{closes[0] + 1}: a measure region is closed before it is opened")
            problems += 1
            continue

        regions += 1
        body = [line for line in lines[opens[0] + 1:closes[0]] if line.strip()]
        if not body:
            say(f"{page}:{opens[0] + 1}: the measure region holds no line - a region carrying no "
                "number is a marker pretending to be data")
            problems += 1
        seen: set[str] = set()
        for offset, line in enumerate(body):
            number = opens[0] + 2 + offset
            if GAUGE.match(line):
                subject = GAUGE.match(line).group("subject").strip()
                if not SLUG.match(subject):
                    say(f"{page}:{number}: the gauge subject '{subject}' is not a slug")
                    problems += 1
                # WITHIN THE PAGE ONLY. Two current pages claiming one subject is a verdict over
                # the corpus and is deferred; two lines on ONE page is this region contradicting
                # itself, which no deferral covers.
                elif subject in seen:
                    say(f"{page}:{number}: the gauge subject '{subject}' appears twice in one "
                        "region - a gauge is replaced by subject, never repeated")
                    problems += 1
                seen.add(subject)
            elif TESTIMONY.match(line):
                if "conditions:" not in line:
                    say(f"{page}:{number}: testimony with no 'conditions:' - a reading whose "
                        "conditions are not written down cannot be compared with the next one")
                    problems += 1
            elif line.strip().startswith("- gauge:"):
                say(f"{page}:{number}: a gauge line names its command in backticks and carries "
                    "no value - a gauge that can be printed is never written by hand")
                problems += 1
            else:
                say(f"{page}:{number}: a measure line opens with its role - '- gauge:' or "
                    f"'- testimony:' - and this one opens with {line.strip()[:40]!r}")
                problems += 1

    if problems:
        say(f"{problems} problem(s) in {regions} measure region(s)")
        return 2
    say(f"every measure region is well formed ({regions} region(s))")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(add_help=True, description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--page")
    parser.add_argument("--role", choices=("gauge", "testimony"))
    parser.add_argument("--subject")
    parser.add_argument("--command")
    parser.add_argument("--value")
    parser.add_argument("--conditions")
    args = parser.parse_args()

    root = vault() / "wiki"

    if args.check and args.refresh:
        die("--check and --refresh are different questions: --check executes nothing and "
            "--refresh executes every gauge's command")
    if args.check:
        sys.exit(check(root))
    if args.refresh:
        sys.exit(refresh(root))
    if not args.page or not args.role:
        die("nothing to do: pass --check, --refresh, or --page with --role")
    sys.exit(write_measurement(root, args))


if __name__ == "__main__":
    main()
