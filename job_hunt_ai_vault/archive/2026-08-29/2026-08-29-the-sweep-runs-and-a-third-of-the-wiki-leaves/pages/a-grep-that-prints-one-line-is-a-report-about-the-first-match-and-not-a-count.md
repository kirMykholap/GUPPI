---
title: "A `grep -n` that prints one line is a report about the first match, not a count"
type: lesson
status: archived
authority: first-match-read-as-a-count
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "tests/integration/test_cli.py"]
tags: [process, testing, harness]
---

# It happened twice in forty minutes, and neither was noticed in the moment

| what was reported | what was measured |
|---|---|
| `tests/integration/test_cli.py` — *"line 78 carries Cyrillic prose"* | **298 Cyrillic lines, 34 Russian test function names** — the third-largest Cyrillic file in `tests/` |
| the prose half of the moved agent path — *"six `wiki/` pages"* | **five pages**, two hits having been in one file |

**Same defect, twice.** A single printed line was read as the extent of what exists, when it is the
first thing the tool found and stopped at.

**The first correction came from the librarian rather than from the session**, which is what makes
the figure a miss rather than a rounding error: `test_cli.py` is squarely inside the bucket
[[migrating-the-repository-to-english]] holds a standing refusal over, and the reported figure
placed it outside.

# Why it fails in this direction

**A first match is always smaller than a count, and never larger.** So the error is towards *there
is little to do here* — the same direction as an instrument that reports zero findings
([[an-instrument-that-fails-towards-nothing-to-do]]), and the same direction as the sibling defect
where `$'\r'` did not survive into a grep and the pattern matched every line
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]).

**Both of those produce a plausible number rather than an error**, which is why neither is caught by
looking at the output.

# The defence

**Ask the tool the question you are answering.** `-c` counts, `-l` lists files, `-o | wc -l` counts
matches rather than lines. A default `grep -n` answers *where is the first one*, and quoting it as
an extent is a claim the command was never asked to support
([[the-owners-question-was-how-would-you-check-that]]).

**And a figure that decides scope is worth a second instrument.** The scope of the English sweep was
being read off these numbers ([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]).

# The same shape in an identity question, not a count — 2026-08-21

**A `find` that resolves to *a* file was read as a reading of *the* file.** The live pre-task ledger
was reported as holding two sessions when it holds one: the command had picked a file out of the
ledger archive ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]],
[[the-ledger-archive-directory]]).

**Corrected before anything was built on it**, and the shape is worth keeping beside the counting
one above: **a wildcard that resolves to a file reads exactly like a reading of the file you meant.**
Nothing in the output says which of the matches you got.

**It fails in the same direction as the count**: the answer is plausible, arrives without an error,
and is smaller or older than the truth ([[an-instrument-that-fails-towards-nothing-to-do]]).

**And it is the identity-versus-presence defect from a third angle** — `grep -l` answering *does it
exist* when the question was *is it this one* ([[a-presence-test-cannot-answer-an-identity-question]]).

**The defence is the same and it is one word: print what you matched.** A `find` whose result is
quoted has to show its path, the way a count has to be asked with `-c`.

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# `grep -c` counts lines and not occurrences — 2026-08-22

**A `log.md` entry was reported as appearing twice. It appears once**, in a wrapped paragraph, and
`grep -c` had counted the two lines the one entry is wrapped across.

**Same family as the reading above, one flag over.** `-c` looks like *count the matches* and means
*count the matching lines*, so any target that can wrap — which is every paragraph in this
corpus, hard-wrapped at 100 — overcounts by however many lines it occupies
([[a-stated-count-drifts-from-the-list-it-heads]]).

**Caught on re-reading and corrected in the same turn**, which is the only defence available for a
number that is right-looking and cheap to produce ([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).

**The reader that answers the question asked is `grep -o ... | wc -l`**, or a reader that does not
work in lines at all.
