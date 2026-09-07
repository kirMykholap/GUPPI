#!/usr/bin/env python3
"""The undrained part of `wiki/lessons/` -- the lessons nothing anywhere cites.

`lessons/` is a store that nothing empties. The folder grows monotonically and is read only when
somebody greps into it, so most of what it holds has never been proposed against or ruled on.

NO FIGURE LIVES IN THIS DOCSTRING, AND THAT IS THE REPAIR RATHER THAN AN OMISSION. The counts that
stood here were taken against a population this script no longer measures, and a number in prose
goes false without saying so. Run the script; it prints today's.

TWO NUMBERS, NOT ONE, AND THEY ANSWER DIFFERENT QUESTIONS -- owner, 2026-08-26. A citation is not
an action. Writing a proposal that cites a lesson used to mark that lesson handled, so the queue
fell in an ingest where **no lesson was acted on**; the fall was an artefact of the drafts being
filed. So:

- **cited** -- a rule, a proposal or a decision names the slug. This is what keeps a lesson OUT of
  the queue, and it has to stay wide or the collector re-proposes the same family for ever. It
  measures the loop's end state and nothing else.
- **landed** -- a `rules/` page names it, or a proposal that names it carries `status: implemented`.
  A proposal is a design that is NOT built by the folder's own definition, so citing one cannot
  mean a lesson was acted on. This is the number that measures progress.

`landed` is a subset of `cited` by construction. Where they are equal, either everything cited has
landed or the corpus is not marking `implemented`.

KNOWN BLIND SPOT, AND IT IS PRINTED RATHER THAN ABSORBED. This scans `wiki/` and never `archive/`.
An implemented proposal is obliged to leave `wiki/proposals/` once a live page names it, so on the
day one moves, `landed` drops and the queue rises -- with nothing having gone backwards. Read a
move in those two numbers as an address change, never as regress.

This prints the queue and nothing else. It does NOT group, because grouping is a judgement and the
one mechanism that looks like it can do this arithmetic cannot: `--near` matches on WORDS, and the
seven pages of the shell-quoting family -- apostrophe, heredoc, sed, grep, backslash, TMPDIR, CR --
share none. That is why every lesson carries an `authority:` value of its own and **not one family
has ever held two of them**.

The queue is the input to the collector dispatch in `/vault-lint`. A lesson leaves it the moment a
rule, a proposal **or a decision** cites it, so the loop has an end state rather than re-proposing
for ever. The narrower reading -- a rule or a proposal alone -- stood in this sentence while the
bullets above already said otherwise, and it is the membership the owner widened on 2026-08-26.

Run: uv run python scripts/lessons-queue.py [--slugs]
"""

import re
import sys
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover
        pass

REPO = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[\[([^\]]+)\]\]")
# Anchored and multiline: `status:` is a frontmatter key, and the word appears in prose all over
# this corpus. Matching it loosely would count a page that merely discusses the mark.
IMPLEMENTED = re.compile(r"^status:[ \t]*implemented[ \t]*$", re.MULTILINE)


def vault() -> Path:
    """The vault is the top-level directory holding a `wiki/`. Its name is the one Obsidian
    displays and the owner changes it, so it is never hard-coded."""
    for candidate in sorted(REPO.iterdir()):
        if candidate.is_dir() and (candidate / "wiki").is_dir():
            return candidate
    print("LESSONS-QUEUE: no directory holding a wiki/ under the repository", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    root = vault() / "wiki"
    lessons = {p.stem: p for p in sorted((root / "lessons").glob("*.md"))}
    if not lessons:
        print("LESSONS-QUEUE: wiki/lessons/ is empty or missing", file=sys.stderr)
        sys.exit(2)

    cited_by_rule: set[str] = set()
    cited_by_proposal: set[str] = set()
    cited_by_decision: set[str] = set()
    landed_by_proposal: set[str] = set()
    for folder, sink in (
        ("rules", cited_by_rule),
        ("proposals", cited_by_proposal),
        ("decisions", cited_by_decision),
    ):
        for page in (root / folder).glob("*.md"):
            body = page.read_text(encoding="utf-8", errors="replace")
            hits = {slug for slug in LINK.findall(body) if slug in lessons}
            sink |= hits
            if folder == "proposals" and IMPLEMENTED.search(body):
                landed_by_proposal |= hits

    cited = cited_by_rule | cited_by_proposal | cited_by_decision
    landed = cited_by_rule | landed_by_proposal
    queue = sorted(set(lessons) - cited)

    if "--slugs" in sys.argv:
        for slug in queue:
            print(slug)
        return

    print(f"lessons                              : {len(lessons)}")
    print(f"  cited by a rule                    : {len(cited_by_rule)}")
    print(f"  cited by a proposal                : {len(cited_by_proposal)}")
    print(f"  cited by a decision                : {len(cited_by_decision)}")
    print(f"CITED - any of the three             : {len(cited)}")
    print(f"LANDED - a rule or an implemented one: {len(landed)}")
    print(f"THE QUEUE - cited by none            : {len(queue)}")
    print()
    print("CITED keeps a lesson out of the queue and measures the loop's end state. LANDED is the")
    print("progress number: a proposal is a design that is not built, so citing one is not acting")
    print("on a lesson. Neither counts archive/, so an implemented proposal moving out drops")
    print("LANDED and raises the queue with nothing having gone backwards.")
    print()
    print("Run with --slugs for the list. Grouping is the librarian's judgement, not this")
    print("script's arithmetic: see scripts/vault-authority.sh line 22.")


if __name__ == "__main__":
    main()
