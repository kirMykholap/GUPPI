#!/usr/bin/env bash
# Prints the catalogue: every page in the vault, one row each, from the frontmatter.
# Run: bash scripts/vault-catalogue.sh
#
# WHY THIS EXISTS, AND WHY IT ONLY PRINTS. The owner asked for "автоматически обновляемый каталог
# всех страниц"; what was built first was index.md, a map that deliberately lists no pages,
# because a hand-kept catalogue of a hundred pages rots. Generation answered that, and this
# script wrote $VAULT/catalogue.md while rule 9 of vault-check.sh failed whenever the file
# differed from what it produces.
#
# On 2026-08-17 the file was replaced by $VAULT/pages.base, an Obsidian base. A base is a query
# rather than an answer: it is evaluated when the owner opens it, so it cannot be stale, there is
# nothing to regenerate, nothing to diff, and rule 9 is retired. It also holds no wikilinks,
# which retires the one dangerous thing the written catalogue carried - it linked to EVERY page,
# so admitting it to the register list vault-check.sh reads for links would have left the orphan
# rule running, passing and proving nothing ever again.
#
# What a base cannot do is be read by an agent: Obsidian evaluates it and no script here can.
# That is exactly what this script is for now. It answers "what is there at all" in one command,
# for the readers that have no editor - which is every reader of this repository except one.
#
# THE `authority` COLUMN, ADDED 2026-08-21, AND IT IS THE POINT OF THIS SCRIPT NOW RATHER THAN A
# SIXTH FIELD. `authority` is the question a page is the sole answer to and `title` says what the
# page claims, so the two together are the whole of the first sieve: the librarian reads them
# across the corpus in one command and opens only what they implicate. That is the wide half of
# the reading rule - the ten-page ceiling is about OPENING, never about searching - and until this
# column existed the wide half was a grep over 479 files, which is why nobody did it.
#
# It is also what makes Occam's razor executable rather than an exhortation: a page is not created
# until the family its `authority` belongs to has been read
# ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).
#
# A rules page prints an empty cell and that is correct - a rule answers with `governs:`, and
# `authority:` beside it is forbidden on any page.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

# Same discovery as vault-check.sh, deliberately identical: two rules that can disagree about
# where the vault is are worse than either of them.
VAULT="${VAULT:-}"
if [ -z "$VAULT" ]; then
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
fi
[ -n "$VAULT" ] || { echo "vault-catalogue: no vault found" >&2; exit 1; }

# ALL of a section's pages go through ONE awk. It was one awk per file first, which is fine on
# paper and cost the selftest minutes: the gate regenerates the catalogue for each of its ~45
# cases, so a hundred processes became four thousand. Every reader we own strips a trailing CR
# before doing anything else - the fifth thing in this project a checkout would otherwise have
# broken by rewriting line endings.
AWK_ROWS='
  function emit(   name, i, n, part) {
    if (cur == "") return
    name = cur; sub(/.*\//, "", name); sub(/\.md$/, "", name)
    gsub(/^[ \t]*"?|"?[ \t]*$/, "", t); gsub(/^[ \t]+|[ \t]+$/, "", s)
    gsub(/^[ \t]+|[ \t]+$/, "", p); gsub(/^[ \t]*\[|\][ \t]*$/, "", g)
    gsub(/^[ \t]*"?|"?[ \t]*$/, "", a)
    # A pipe inside a title would end the markdown cell it sits in. Replaced with no escape
    # sequence at all: awk warns on both \& and \| in a replacement, and a script that prints
    # a warning on every run teaches its reader to ignore everything it prints.
    n = split(t, part, "|"); t = part[1]
    for (i = 2; i <= n; i++) t = t "&#124;" part[i]
    printf "| [[%s]] | %s | %s | %s | %s | %s |\n", name, a, t, s, p, g
  }
  FNR == 1 { emit(); cur = FILENAME; t = ""; s = ""; p = ""; g = ""; a = ""
             infm = ($0 == "---"); done = !infm; next }
  done                { next }
  { sub(/\r$/, "") }
  /^---[[:space:]]*$/ { done = 1; next }
  /^title:/           { t = substr($0, 8) }
  /^status:/          { s = substr($0, 9) }
  /^sprint:/          { p = substr($0, 9) }
  /^tags:/            { g = substr($0, 7) }
  /^authority:/       { a = substr($0, 12) }
  END                 { emit() }
'

section() {                       # section <heading> <dir>
  local heading="$1" dir="$2" count
  count=$(find "$dir" -name '*.md' 2>/dev/null | wc -l)
  printf '\n## %s (%s)\n\n' "$heading" "$count"
  if [ "$count" -eq 0 ]; then printf '_None._\n'; return; fi
  printf '| Page | Authority | Title | Status | Sprint | Tags |\n|---|---|---|---|---|---|\n'
  # -print0 and sort -z, never word-splitting: the vault's directory name is the owner's and
  # has contained a space before, which is how an unquoted $(find) once made this whole suite
  # read nothing at all and still print "ok".
  find "$dir" -name '*.md' -print0 2>/dev/null | sort -z \
    | xargs -0 --no-run-if-empty awk "$AWK_ROWS"
}

emit_catalogue() {
  cat <<HEADER
# Catalogue — every page in the vault

<!-- PRINTED by scripts/vault-catalogue.sh, and written to no file. The owner reads this list as
     \`pages.base\` in Obsidian, which filters and groups it; this output exists for readers that
     have no editor. Nothing here is stored, so nothing here can be stale.
     The map — categories, naming, hub pages — is index.md. -->

Retrieval here is \`ripgrep\` first and the wiki links on whatever it finds; this answers the other
question, the one grep cannot: **what is there at all**. Every row is a page, and the counts are
produced by the same run that produces the rows.
HEADER
  for d in decisions concepts entities lessons proposals rules; do
    section "$d" "$VAULT/wiki/$d"
  done
}

# `archive/` IS NOT PRINTED, and it was until 2026-08-30. The section cost 70,535 bytes of the
# 201,927 this script emitted, one third of the whole, and every reader was told to throw it away:
# `.claude/agents/pre-task.md` names `## archive` among the sections to drop, and it is the only
# caller. So the rows were assembled, paid for in context by each dispatch, and discarded unread.
#
# It also brings the script into agreement with two claims that were already written: `index.md`
# and the vault's own `CLAUDE.md` both say an agent runs this script "for the same list" as
# `pages.base`, and `pages.base` filters `file.inFolder("wiki")` and holds no archive at all.
#
# WHAT THIS GIVES UP, named rather than found later: there is now no way for a reader without
# Obsidian to enumerate `archive/`. Nothing asked for one - `/pre-task` is told not to read it and
# the gate validates it by no schema - but a future reader that needs it needs a new flag, not a
# revert ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]: what an archived
# page asserts is frozen, how it is found is live, so widening this again is legitimate).

# `--write` is gone with the file it wrote. It is refused rather than ignored: a caller that
# still passes it - a skill, a hook, a habit - is a caller that believes a file is being kept up
# to date, and silently printing to stdout instead would look like success.
case "${1:-}" in
  "") ;;
  --write) echo "vault-catalogue: --write is retired; the list of every page is \$VAULT/pages.base," >&2
           echo "                 an Obsidian base, and this script only prints. Drop the flag." >&2
           exit 2 ;;
  *) echo "vault-catalogue: unknown argument '$1'; this script takes none" >&2; exit 2 ;;
esac

emit_catalogue
