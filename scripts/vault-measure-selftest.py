#!/usr/bin/env python3
"""Cases for `vault-measure.py` -- every refusal, and the one thing `--check` must never do.

WHY EVERY REFUSAL GETS A CASE. A new instrument owes one in the same change: otherwise the
criterion cannot be read, and a refusal with no case is removed silently by the next refactor.
Five refusals were designed for this script and five are pinned here.

THE FIXTURE IS ITS OWN AND NEVER THE CORPUS. Every case builds a throwaway vault in a temporary
directory and points `$VAULT` at it, so a case can write, break markup, and run a gauge command
without touching a page anybody reads.

THE CASE THAT IS NOT ABOUT A REFUSAL is the most important one here: `--check` executes nothing.
It is proved by giving a gauge a command that would create a file and asserting the file does not
exist afterwards -- because the reason `--check` does not run commands is that one gauge may name
a command costing 38 minutes, and a design decision nothing tests is a comment.

Run: uv run python scripts/vault-measure-selftest.py
"""

import os
import shutil
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
TARGET = HERE / "vault-measure.py"

CAUGHT = 0
MISSED = 0

FOLDERS = ("concepts", "decisions", "entities", "lessons", "proposals", "rules")


def case(name: str, got, want) -> None:
    global CAUGHT, MISSED
    if got == want:
        CAUGHT += 1
        print(f"  ok    {name}")
    else:
        MISSED += 1
        print(f"  MISSED {name}\n        got  {got!r}\n        want {want!r}")


class Vault:
    """A throwaway vault, and the runner that points the script at it."""

    def __init__(self, root: Path) -> None:
        self.root = root
        for folder in FOLDERS:
            (root / "wiki" / folder).mkdir(parents=True, exist_ok=True)

    def page(self, folder: str, slug: str, status: str = "current", body: str = "") -> Path:
        path = self.root / "wiki" / folder / f"{slug}.md"
        path.write_text(
            f"---\ntitle: \"{slug}\"\ntype: {folder[:-1]}\nstatus: {status}\n---\n\n"
            f"# {slug}\n{body}",
            encoding="utf-8",
        )
        return path

    def run(self, *args: str) -> subprocess.CompletedProcess:
        environment = dict(os.environ)
        environment["VAULT"] = str(self.root)
        # `check=False`: a case asserts the exit code the target returned, so raising on a non-zero
        # one would turn every refusal case into an error before it could be checked.
        return subprocess.run(
            [sys.executable, str(TARGET), *args],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            env=environment, check=False,
        )

    def text(self, folder: str, slug: str) -> str:
        return (self.root / "wiki" / folder / f"{slug}.md").read_text(encoding="utf-8")


def fresh(tmp: Path, name: str) -> Vault:
    root = tmp / name
    if root.exists():
        shutil.rmtree(root)
    return Vault(root)


with tempfile.TemporaryDirectory() as raw:
    tmp = Path(raw)

    # --- the five refusals ---------------------------------------------------------------

    # THE FIRST. A destination naming no page is a number written into nothing, and it is the
    # failure the coverage script's BAD VERDICT exists against: a typo in a slug is otherwise a
    # silently dropped measurement.
    v = fresh(tmp, "r1")
    v.page("decisions", "a-real-page")
    result = v.run("--page", "no-such-page", "--role", "testimony",
                   "--value", "3 s", "--conditions", "an idle machine")
    case("a page slug nothing answers is refused", result.returncode, 2)
    case("and the refusal names the slug", "no-such-page" in result.stderr, True)

    # THE SECOND. Which page a measurement belongs on is exactly the judgement the librarian is
    # for, so an ambiguous slug is handed back rather than guessed at.
    v = fresh(tmp, "r2")
    v.page("decisions", "twice-over")
    v.page("concepts", "twice-over")
    result = v.run("--page", "twice-over", "--role", "testimony",
                   "--value", "3 s", "--conditions", "an idle machine")
    case("a slug two folders answer is refused", result.returncode, 2)
    case("and the refusal names both folders",
         "concepts" in result.stderr and "decisions" in result.stderr, True)

    # THE THIRD, IN THREE HALVES. A gauge with no command is a value waiting to be typed by a
    # hand, which is the prohibition this whole script exists to keep intact.
    v = fresh(tmp, "r3")
    v.page("entities", "the-gate")
    result = v.run("--page", "the-gate", "--role", "gauge", "--subject", "region-coverage")
    case("a gauge with no command is refused", result.returncode, 2)
    result = v.run("--page", "the-gate", "--role", "gauge", "--command", "echo 1")
    case("a gauge with no subject is refused", result.returncode, 2)
    result = v.run("--page", "the-gate", "--role", "gauge", "--subject", "region-coverage",
                   "--command", "echo 1", "--value", "9 of 15")
    case("a gauge handed a value is refused", result.returncode, 2)
    case("and the refusal says --refresh writes the reading",
         "--refresh" in result.stderr, True)

    # THE FOURTH. Two numbers taken under conditions nobody wrote down WILL be compared, and this
    # project has already reported a change that did not happen by doing exactly that.
    v = fresh(tmp, "r4")
    v.page("decisions", "a-reading")
    result = v.run("--page", "a-reading", "--role", "testimony", "--value", "34m8s")
    case("testimony with no conditions is refused", result.returncode, 2)
    result = v.run("--page", "a-reading", "--role", "testimony", "--conditions", "an idle machine")
    case("testimony with no value is refused", result.returncode, 2)

    # THE FIFTH, AND IT IS THE WRITER'S ALONE. The verdict over the whole corpus is deferred by
    # decision; this stops ONE write at the moment a subject would become ambiguous.
    v = fresh(tmp, "r5")
    v.page("entities", "page-one")
    v.page("entities", "page-two")
    v.run("--page", "page-one", "--role", "gauge", "--subject", "region-coverage",
          "--command", "echo 9 of 15")
    result = v.run("--page", "page-two", "--role", "gauge", "--subject", "region-coverage",
                   "--command", "echo 9 of 15")
    case("a gauge subject another current page carries is refused", result.returncode, 2)
    case("and the refusal names the page already carrying it",
         "page-one" in result.stderr, True)

    # ONLY A `current` PAGE RESERVES A SUBJECT. A deprecated page's gauge is a record of what was
    # once measured; treating it as a claim on the subject would make a retirement unable to
    # release the name.
    v = fresh(tmp, "r5b")
    v.page("entities", "old-page", status="deprecated")
    v.page("entities", "new-page")
    v.run("--page", "old-page", "--role", "gauge", "--subject", "region-coverage",
          "--command", "echo 9 of 15")
    result = v.run("--page", "new-page", "--role", "gauge", "--subject", "region-coverage",
                   "--command", "echo 9 of 15")
    case("a deprecated page does not reserve a gauge subject", result.returncode, 0)

    # --- what the writer writes ----------------------------------------------------------

    v = fresh(tmp, "w1")
    v.page("entities", "the-gate")
    result = v.run("--page", "the-gate", "--role", "gauge", "--subject", "region-coverage",
                   "--command", "echo 9 of 15")
    body = v.text("entities", "the-gate")
    case("a first gauge exits 0", result.returncode, 0)
    case("and the region is created for it", "<!-- measure -->" in body, True)
    case("and the region is closed", "<!-- /measure -->" in body, True)
    case("and the line names the command in backticks",
         "- gauge: region-coverage -- `echo 9 of 15` -- not yet read" in body, True)
    # A GAUGE CARRIES NO VALUE UNTIL A SCRIPT RUNS THE COMMAND. This is the prohibition itself,
    # asserted rather than described.
    case("and it carries no number a hand could have typed", "9 of 15 --" in body, False)

    # A GAUGE IS REPLACED BY SUBJECT: it is the current reading of a live thing, so a second one
    # supersedes the first rather than sitting beside it and disagreeing.
    v.run("--page", "the-gate", "--role", "gauge", "--subject", "region-coverage",
          "--command", "echo 10 of 15")
    body = v.text("entities", "the-gate")
    case("a second gauge with the same subject replaces the first",
         body.count("- gauge: region-coverage"), 1)
    case("and it is the new command that survives", "echo 10 of 15" in body, True)

    v.run("--page", "the-gate", "--role", "gauge", "--subject", "gate-seconds",
          "--command", "echo 15.3 s")
    body = v.text("entities", "the-gate")
    case("a different subject on the same page is a second gauge",
         body.count("- gauge: "), 2)

    # TESTIMONY IS APPENDED AND NEVER REPLACED. A past reading does not stop having happened when
    # a later one disagrees with it.
    v = fresh(tmp, "w2")
    v.page("decisions", "a-reading")
    v.run("--page", "a-reading", "--role", "testimony", "--value", "34m8s",
          "--conditions", "an idle machine")
    v.run("--page", "a-reading", "--role", "testimony", "--value", "37m44s",
          "--conditions", "the same machine, forty per cent slower")
    body = v.text("decisions", "a-reading")
    case("testimony is appended rather than replaced", body.count("- testimony:"), 2)
    case("and the earlier reading survives the later one", "34m8s" in body, True)
    case("and each carries its conditions", body.count("conditions:"), 2)

    result = v.run("--page", "a-reading", "--role", "testimony", "--value", "1 s",
                   "--conditions", "x", "--subject", "something")
    case("testimony handed a subject is refused", result.returncode, 2)

    # --- the refresh pass ------------------------------------------------------------------

    v = fresh(tmp, "f1")
    v.page("entities", "the-gate")
    v.run("--page", "the-gate", "--role", "gauge", "--subject", "region-coverage",
          "--command", "echo 9 of 15")
    before = v.text("entities", "the-gate")
    result = v.run("--refresh")
    after = v.text("entities", "the-gate")
    case("--refresh exits 0 when every command reads", result.returncode, 0)
    # THE ACCEPTANCE IN SUBSTANCE: a number that was not in the line before it ran. Asserted on
    # the READING's position and not on the digits, which also appear inside the command - a
    # first draft of this case passed while every gauge sat outside its own region.
    case("and it writes a number that was not there before",
         "-- 9 of 15 -- read " in after, True)
    case("and that reading was not in the line before", "-- 9 of 15 -- read " in before, False)
    case("and the line stops saying it was never read", "not yet read" in after, False)
    case("and it keeps the command it read", "`echo 9 of 15`" in after, True)

    # REFRESHED TWICE DOES NOT GROW A HISTORY INSIDE ONE LINE. The history of a gauge is git's.
    v.run("--refresh")
    twice = v.text("entities", "the-gate")
    case("refreshing twice leaves one reading on the line",
         twice.count("- gauge: region-coverage"), 1)
    case("and the line is unchanged by the second run", twice, after)

    # A COMMAND MUST PRINT EXACTLY THE LINE WANTED. Choosing among several is a judgement, and a
    # script that guesses writes a number nobody took.
    v = fresh(tmp, "f2")
    v.page("entities", "noisy")
    v.run("--page", "noisy", "--role", "gauge", "--subject", "two-lines",
          "--command", "printf 'one\\ntwo\\n'")
    result = v.run("--refresh")
    case("a command printing two lines is refused", result.returncode, 2)
    case("and the refusal says so", "printed 2 lines" in result.stdout, True)
    case("and nothing is written into the line",
         "not yet read" in v.text("entities", "noisy"), True)

    v = fresh(tmp, "f3")
    v.page("entities", "broken")
    v.run("--page", "broken", "--role", "gauge", "--subject", "fails",
          "--command", "exit 3")
    result = v.run("--refresh")
    case("a command exiting non-zero is refused", result.returncode, 2)
    case("and the refusal carries the exit code", "exited 3" in result.stdout, True)

    v = fresh(tmp, "f4")
    v.page("entities", "silent")
    v.run("--page", "silent", "--role", "gauge", "--subject", "prints-nothing",
          "--command", "true")
    result = v.run("--refresh")
    case("a command printing nothing is refused", result.returncode, 2)

    # --- the check -------------------------------------------------------------------------

    v = fresh(tmp, "c0")
    v.page("entities", "the-gate")
    v.run("--page", "the-gate", "--role", "gauge", "--subject", "region-coverage",
          "--command", "echo 9 of 15")
    result = v.run("--check")
    case("a well-formed region passes the check", result.returncode, 0)
    case("and the check says how many regions it read",
         "1 region(s)" in result.stdout, True)

    # THE CASE THIS FILE EXISTS FOR. `--check` reads shape and EXECUTES NOTHING, because running
    # every gauge would execute arbitrary commands taken from page content at unbounded cost --
    # one gauge may name a command that costs 38 minutes. A design decision nothing tests is a
    # comment, so this proves it by side effect.
    v = fresh(tmp, "c1")
    v.page("entities", "dangerous")
    witness = tmp / "the-check-executed-a-command"
    v.run("--page", "dangerous", "--role", "gauge", "--subject", "side-effect",
          "--command", f"touch '{witness.as_posix()}' && echo 1")
    result = v.run("--check")
    case("--check exits 0 over that region", result.returncode, 0)
    case("AND IT EXECUTED NOTHING", witness.exists(), False)
    # ...and the same command under --refresh does fire, so the case above is about --check and
    # not about a command that never worked.
    v.run("--refresh")
    case("while --refresh does run it", witness.exists(), True)

    v = fresh(tmp, "c2")
    v.page("decisions", "typo", body="\n<!-- measure: region-coverage -->\n<!-- /measure -->\n")
    result = v.run("--check")
    case("a marker carrying a colon is malformed rather than invisible", result.returncode, 2)
    case("and the check names the exact form", "malformed measure marker" in result.stdout, True)

    v = fresh(tmp, "c3")
    v.page("decisions", "unclosed", body="\n<!-- measure -->\n- testimony: x -- conditions: y\n")
    result = v.run("--check")
    case("a region opened and never closed is caught", result.returncode, 2)
    case("and it says which end is missing",
         "opened and never closed" in result.stdout, True)

    v = fresh(tmp, "c4")
    v.page("decisions", "unopened", body="\n<!-- /measure -->\n")
    result = v.run("--check")
    case("a close with no open is caught", result.returncode, 2)

    v = fresh(tmp, "c5")
    v.page("decisions", "twice",
           body="\n<!-- measure -->\n<!-- /measure -->\n\n<!-- measure -->\n<!-- /measure -->\n")
    result = v.run("--check")
    case("two regions in one file are caught", result.returncode, 2)

    # THE GRAMMAR'S OWN VERDICT: a gauge line carrying a number instead of a command is exactly
    # what the prohibition forbids, written straight into a page by a hand.
    v = fresh(tmp, "c6")
    v.page("decisions", "handwritten",
           body="\n<!-- measure -->\n- gauge: region-coverage -- 9 of 15\n<!-- /measure -->\n")
    result = v.run("--check")
    case("a gauge line with a value and no command is caught", result.returncode, 2)
    case("and the check quotes the prohibition",
         "never written by hand" in result.stdout, True)

    v = fresh(tmp, "c7")
    v.page("decisions", "conditionless",
           body="\n<!-- measure -->\n- testimony: 34m8s -- taken 2026-08-25\n<!-- /measure -->\n")
    result = v.run("--check")
    case("testimony with no conditions is caught by the check", result.returncode, 2)

    v = fresh(tmp, "c8")
    v.page("decisions", "roleless",
           body="\n<!-- measure -->\n- 34m8s on an idle machine\n<!-- /measure -->\n")
    result = v.run("--check")
    case("a line that does not open with its role is caught", result.returncode, 2)

    v = fresh(tmp, "c9")
    v.page("decisions", "hollow", body="\n<!-- measure -->\n<!-- /measure -->\n")
    result = v.run("--check")
    case("a region holding no line is caught", result.returncode, 2)
    case("and it is named as a marker pretending to be data",
         "pretending to be data" in result.stdout, True)

    v = fresh(tmp, "c10")
    v.page("decisions", "repeated",
           body="\n<!-- measure -->\n- gauge: same -- `echo 1` -- not yet read\n"
                "- gauge: same -- `echo 2` -- not yet read\n<!-- /measure -->\n")
    result = v.run("--check")
    case("one subject twice in one region is caught", result.returncode, 2)

    # --- the modes disagree about executing, so they may not be asked together ---------------

    v = fresh(tmp, "m1")
    v.page("decisions", "anything")
    result = v.run("--check", "--refresh")
    case("--check and --refresh together are refused", result.returncode, 2)
    result = v.run()
    case("no mode at all is refused rather than silently doing nothing", result.returncode, 2)

    # $VAULT WINS, AND A BAD ONE IS A REFUSAL. The suite renames the vault inside a sandbox to
    # prove nothing hard-codes the name; a script that silently fell back to a search would pass
    # that case while reading the wrong corpus.
    environment = dict(os.environ)
    environment["VAULT"] = str(tmp / "no-such-vault")
    result = subprocess.run([sys.executable, str(TARGET), "--check"], capture_output=True,
                            text=True, encoding="utf-8", errors="replace", env=environment,
                            check=False)  # the case asserts exit 2; raising would hide it
    case("a $VAULT holding no wiki/ is refused rather than searched past",
         result.returncode, 2)

print(f"\nVAULT-MEASURE-SELFTEST: caught {CAUGHT}, missed {MISSED}")
sys.exit(1 if MISSED else 0)
