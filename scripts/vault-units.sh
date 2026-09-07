#!/usr/bin/env bash
# Splits a markdown document into claim-sized units, one per line, as LINE|KIND|TEXT.
#
# A unit is one claim: a heading, a table row, a bullet, a numbered item, or the opening
# line of a paragraph. That is the granularity documents of this kind are actually written
# at.
#
# It used to be narrower - only paragraphs and bullets that open in **bold** - and that
# narrowness reproduced, one level down, the exact failure this script exists to prevent.
# The first real ingest reported it: sections 4 and 8 of the 2026-08-13 handoff are written
# in plain prose, so they contributed nothing but their headings, and their entire content
# was invisible to the denominator. A section can then be left uncompiled while coverage
# reports 100%. Bold is an emphasis choice, not a claim boundary, and nothing may depend on
# a writer having made it.
#
# The point of this script is that the *denominator* of an ingest is produced
# mechanically. If the party that accounts for the units also decided what the units
# are, a forgotten section never appears on the list and its absence is invisible -
# which is exactly how section 1 of docs/HANDOFF.md was lost on the first pass, while
# the ingest log claimed it had been read.
#
# Two shapes of document defeat a line-based reader, and both are answered here rather than
# left to be discovered by a coverage report that says 100% over almost nothing:
#
#   NO BLANK LINES AT ALL. A paragraph opening is normally "a line after a blank one", so a
#   document written without blank lines yields only its headings and bullets. `docs/
#   second-brain-info.md` is exactly that: 90 lines, 0 blank, 5 units under the old rule -
#   and it is named in the plan as the next document to be ingested. When a file has no blank
#   lines, every line that is not matched by a stronger rule is a unit of its own.
#
#   A PARAGRAPH DIRECTLY UNDER A HEADING. "A paragraph opens after a blank line" was read as
#   "after a blank line only", and a heading set the flag back to 0 - so text written flush
#   against its heading, with no blank line between, was invisible. Found on 2026-08-14 on the
#   first source that was not written from our own template: the owner's note opens three lines
#   of prose directly under `## Purpose`, and they had to be verdicted by hand to be accounted
#   for at all. A heading ENDS a block, so the line after it always opens a new claim - which is
#   why the rule sets blank = 1. Measured before it was changed: across all six sources of this
#   vault the fix adds two units, both in that note. A bullet is deliberately not treated this
#   way, because a line under a bullet is that bullet's continuation and not a claim of its own.
#
#   AN UNCLOSED FENCE swallows the whole remainder of the file, silently. That is a warning
#   on stderr and exit 3, because the alternative is a complete-looking accounting of a
#   truncated document.
#
# Run: bash scripts/vault-units.sh <file.md>
set -uo pipefail

src="${1:-}"
[ -n "$src" ] || { echo "usage: vault-units.sh <file.md>" >&2; exit 2; }
[ -f "$src" ] || { echo "no such file: $src" >&2; exit 2; }

blanks=$(grep -c '^[[:space:]]*$' "$src")

awk -v noblanks="$([ "$blanks" -eq 0 ] && echo 1 || echo 0)" '
  # A document opens as if a blank line preceded it: without this the very first paragraph
  # of a file is never a unit, which is how a two-claim probe reported one claim. YAML
  # frontmatter is skipped outright - it is metadata about the document, not a claim in it.
  FNR == 1                     { blank = 1; inblock = 0; if ($0 == "---") { infm = 1; next } }
  infm && /^---[[:space:]]*$/  { infm = 0; blank = 1; next }
  infm                         { next }
  /^```/                       { inblock = !inblock; blank = 0; next }
  inblock                      { next }
  /^[[:space:]]*$/             { blank = 1; next }
  /^\|[[:space:]]*-+/          { blank = 0; next }        # table separator
  /^#{1,6} /                   { print NR "|heading|" $0; blank = 1; next }
  /^\|/                        { print NR "|row|" $0; blank = 0; next }
  /^> \*\*/                    { print NR "|quote|" $0; blank = 0; next }
  /^>[[:space:]]*([-*+]|[0-9]+\.) / { print NR "|quoted|" $0; blank = 0; next }
  /^\*\*/                      { print NR "|para|" $0; blank = 0; next }
  /^[[:space:]]*[-*+] /        { print NR "|bullet|" $0; blank = 0; next }
  /^[[:space:]]*[0-9]+\. /     { print NR "|item|" $0; blank = 0; next }
  blank || noblanks            { print NR "|prose|" $0; blank = 0; next }   # a paragraph opens
                               { blank = 0 }              # and its later lines are not units
  END {
      if (inblock) {
          print "vault-units: unclosed code fence in " FILENAME "; everything after it was " \
                "skipped and the count below is not the document" > "/dev/stderr"
          exit 3
      }
  }
' "$src"
