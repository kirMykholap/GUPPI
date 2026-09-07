#!/usr/bin/env bash
# Answers the question Occam's razor is decided by: does this claim already have a page?
#
# Run: bash scripts/vault-authority.sh [--list | --near <slug> | --group <name> | --check
#                                      | --orphans | --binding | --trace <page>]
#
# WHY THIS EXISTS. `/ingest` had no valve on its intake: a unit of knowledge became a page by
# default, and the only clamp - retire on direct replacement - had fired 27 times against 479 live
# pages. Measured 2026-08-21: 479 pages and 2.9 MB in nine days, every one `status: current`. The
# owner's ruling was to make not-multiplying-entities the ground rule rather than one more check,
# and a rule you cannot look anything up for is an exhortation
# ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).
#
# `authority:` IS THE INDEX AND `authority.md` IS ITS DICTIONARY, WHICH ARE TWO DIFFERENT THINGS.
# The slug lives in the frontmatter, which is the tree; the FAMILY a slug belongs to lives nowhere
# and cannot be derived, which is why the register is a hand-written file and not a generated one -
# exactly the standing of `tags.md`, where the definitions and the Russian aliases are the part no
# sweep could produce. The half of the register that IS derivable - which slugs exist - is the half
# that drifts, so `--check` compares it against the tree in both directions rather than trusting it
# ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).
#
# WHY THE GROUPING IS THE LIBRARIAN'S JUDGEMENT AND NOT THIS SCRIPT'S ARITHMETIC. `--near` falls
# back to counting shared words when a slug is in no group yet, and that fallback is a crutch, not
# the design: `ledger-retention` and `ledger-archive` share a word and belong together, while
# `map-admission` and `where-things-are` share none and answer the same question. Word overlap
# cannot see that; the librarian can, incrementally, about fifteen slugs per ingest rather than the
# whole register at once. Vectors were weighed and are already deferred with a reason
# ([[vectors-are-deferred-not-rejected]]), and short slugs are inside what a reader takes whole.
#
# THE REGISTER NAMES SLUGS AS PLAIN TEXT, NEVER AS `[[wikilinks]]`, AND THAT IS LOAD-BEARING. A
# register that linked every page would have to join the link sweep of rule 5, and then no page in
# this vault could ever be an orphan again - the orphan rule would run, pass, and prove nothing.
# That is the trap the generated catalogue carried and part of why it was replaced by a query.
#
# Same vault discovery as `vault-check.sh` and `vault-catalogue.sh`, deliberately identical: two
# rules that can disagree about where the vault is are worse than either of them.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

SELF="VAULT-AUTHORITY"

VAULT="${VAULT:-}"
if [ -z "$VAULT" ]; then
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
fi
[ -n "$VAULT" ] || { echo "$SELF: no vault found (no top-level directory contains a wiki/)"; exit 1; }

REGISTER="$VAULT/authority.md"

usage() {
  cat <<'USAGE'
VAULT-AUTHORITY: look a claim up before writing a page for it.

  --list             every authority slug, with the page and title that own it
  --near <slug>      the family a candidate belongs to, or the slugs sharing its words
  --group <name>     the members of one family, with their titles
  --check            the register against the tree, in both directions
  --orphans          pages carrying no authority, which nothing can look up
  --binding          what the decisions folder declares about itself
  --trace <page>     which source lines the page was compiled from

With no argument, --list.
USAGE
}

# ONE PASS OVER THE CORPUS, CACHED, EMITTING `slug<TAB>page<TAB>title<TAB>folder<TAB>binding<TAB>governs`.
# Every subcommand reads this and nothing re-walks the tree, because a second walk is a second
# definition of what counts as a page - and because `--group` would otherwise re-walk 479 files
# once per member of the family it is printing.
#
# Frontmatter only: the body is never read, which is what makes a sweep over the whole corpus cost
# nothing and is the same reason the ten-page ceiling is about OPENING and never about searching.
#
# The trailing CR is stripped first, as every reader in this repository does - a checkout that
# rewrites line endings has already broken five things here.
CORPUS=""
corpus() {
  if [ -z "$CORPUS" ]; then
    CORPUS=$(find "$VAULT/wiki" -name '*.md' -print0 2>/dev/null \
      | sort -z \
      | xargs -0 --no-run-if-empty awk '
          function emit(   name, folder) {
            if (cur == "") return
            name = cur; sub(/.*\//, "", name); sub(/\.md$/, "", name)
            folder = cur; sub(/\/[^\/]*$/, "", folder); sub(/.*\//, "", folder)
            gsub(/^[ \t]*"?|"?[ \t]*$/, "", t)
            gsub(/^[ \t]+|[ \t]+$/, "", a); gsub(/^[ \t]+|[ \t]+$/, "", b)
            gsub(/^[ \t]*"?|"?[ \t]*$/, "", v)
            printf "%s\t%s\t%s\t%s\t%s\t%s\n", (a == "" ? "-" : a), name, t, folder,
                   (b == "" ? "-" : b), (v == "" ? "-" : v)
          }
          FNR == 1 { emit(); cur = FILENAME; t = ""; a = ""; b = ""; v = ""; done = 0; next }
          done                { next }
          { sub(/\r$/, "") }
          /^---[[:space:]]*$/ { done = 1; next }
          /^title:/           { t = substr($0, 8) }
          /^authority:/       { a = substr($0, 12) }
          /^binding:/         { b = substr($0, 10) }
          /^governs:/         { v = substr($0, 10) }
          END                 { emit() }
        ')
  fi
  printf '%s\n' "$CORPUS"
}

# THE REGISTER PARSER, AND IT ACCEPTS A LIST THAT WRAPS. `tags.md` writes its aliases across
# several lines because they are Russian and there are many, and a parser that only understood one
# line would be silently blind to most of the dictionary it exists to read. Emits `group<TAB>slug`.
register_pairs() {
  [ -f "$REGISTER" ] || return 0
  awk '
    { sub(/\r$/, "") }
    /^-[ \t]+group:[ \t]*/ { g = $0; sub(/^-[ \t]+group:[ \t]*/, "", g)
                             gsub(/^[ \t]+|[ \t]+$/, "", g); inlist = 0; next }
    /^[ \t]+slugs:[ \t]*\[/ { line = $0; sub(/^[ \t]+slugs:[ \t]*\[/, "", line); inlist = 1 }
    inlist {
      if (line == "") line = $0
      closed = (line ~ /\]/)
      sub(/\].*$/, "", line)
      n = split(line, part, ",")
      for (i = 1; i <= n; i++) {
        s = part[i]; gsub(/^[ \t"]+|[ \t"]+$/, "", s)
        if (s != "" && g != "") print g "\t" s
      }
      line = ""
      if (closed) inlist = 0
      next
    }
  ' "$REGISTER"
}

cmd_list() {
  corpus | awk -F'\t' '$1 != "-" { printf "%s\t%s\t%s\n", $1, $2, $3 }' | sort
}

# A rules page is not an orphan of this index: it answers with `governs:`, and `authority:` beside
# it is forbidden on any page. The whole folder is out, read off the FOLDER and nothing else.
#
# It read the `governs:` field too until 2026-08-21, because a `concepts/` page could carry one and
# two of them did. The owner ended that at the retro - a page that renders its text into another
# file is a rule, so both moved into `wiki/rules/` and the field left `concepts/` with them
# ([[governs-is-a-property-of-wiki-rules-alone]]). The field test became unreachable the moment the
# schema stopped admitting `governs:` outside `wiki/rules/`, and unreachable code that guards
# nothing is the thing this session's own rule refuses to accumulate.
cmd_orphans() {
  local rows count
  rows=$(corpus | awk -F'\t' '$1 == "-" && $4 != "rules" && $6 == "-" {
                                 printf "%s\t%s\t%s\n", $4, $2, $3 }' | sort)
  if [ -z "$rows" ]; then
    echo "$SELF: every page outside wiki/rules/ carries an authority"
    return 0
  fi
  printf '%s\n' "$rows"
  count=$(printf '%s\n' "$rows" | grep -c .)
  printf '\n%s: %s pages carry no authority and nothing can look them up\n' "$SELF" "$count"
}

cmd_group() {
  local want="$1" slugs
  [ -n "$want" ] || { echo "$SELF: --group needs a name"; return 2; }
  slugs=$(register_pairs | awk -F'\t' -v g="$want" '$1 == g { print $2 }' | sort -u)
  if [ -z "$slugs" ]; then
    echo "$SELF: no group '$want' in $REGISTER"
    return 1
  fi
  corpus | awk -F'\t' -v list="$slugs" '
    BEGIN { n = split(list, arr, "\n"); for (i = 1; i <= n; i++) if (arr[i] != "") want[arr[i]] = 1 }
    $1 in want { printf "%s\t%s\t%s\n", $1, $2, $3 }' | sort
}

# `--near`: THE GROUP FIRST, THE WORD COUNT ONLY IF THERE IS NO GROUP. The order matters more than
# either half. A candidate whose family is already named gets that family whole, which is the
# answer the admission rule needs; a candidate in no family gets a ranked guess, and the guess says
# it is a guess so that nobody reads it as the register having spoken.
cmd_near() {
  local cand="$1" grp scored
  [ -n "$cand" ] || { echo "$SELF: --near needs a slug"; return 2; }

  grp=$(register_pairs | awk -F'\t' -v s="$cand" '$2 == s { print $1; exit }')
  if [ -n "$grp" ]; then
    echo "$SELF: '$cand' is already in group '$grp' - that question has a page, do not write a second"
    cmd_group "$grp"
    return 0
  fi

  # Score every GROUP by how many of its slugs share a word with the candidate. A group is the
  # better unit to rank: the question is which family to read, not which single page to compare
  # against. Words of three characters or fewer are dropped - `a`, `is`, `the` join everything.
  scored=$(register_pairs | awk -F'\t' -v cand="$cand" '
    BEGIN { n = split(cand, w, "-"); for (i = 1; i <= n; i++) if (length(w[i]) > 3) want[w[i]] = 1 }
    { m = split($2, s, "-"); hit = 0
      for (i = 1; i <= m; i++) if (s[i] in want) hit = 1
      if (hit) score[$1]++ }
    END { for (g in score) printf "%s\t%s\n", score[g], g }' | sort -rn | head -5)

  if [ -n "$scored" ]; then
    echo "$SELF: '$cand' is in no group. Families sharing its words, best first:"
    printf '%s\n' "$scored" | while IFS="$(printf '\t')" read -r n g; do
      printf '\n  group: %s  (%s slug(s) share a word)\n' "$g" "$n"
      cmd_group "$g" | sed 's/^/    /'
    done
    echo
    echo "$SELF: word overlap is a guess, not the register. Read those families before writing."
    return 0
  fi

  [ -f "$REGISTER" ] || echo "$SELF: no register at $REGISTER yet - ranking against the tree instead"
  corpus | awk -F'\t' -v cand="$cand" '
    BEGIN { n = split(cand, w, "-"); for (i = 1; i <= n; i++) if (length(w[i]) > 3) want[w[i]] = 1 }
    $1 != "-" { m = split($1, s, "-"); hit = 0
      for (i = 1; i <= m; i++) if (s[i] in want) hit++
      if (hit) printf "%s\t%s\t%s\t%s\n", hit, $1, $2, $3 }' \
  | sort -rn | head -10 | cut -f2-
}

# `--check`: BOTH DIRECTIONS, BECAUSE ONLY ONE OF THEM IS THE DANGEROUS ONE. A slug in the register
# that no page carries is a stale row - visible, harmless, repaired by deleting the row. A slug in
# the tree that no group holds is the one that costs something: it is a page the lookup cannot
# reach, so the next unit about the same question writes a second page and neither of them is
# wrong. That asymmetry is the whole reason the register is checked rather than trusted.
#
# AN ARCHIVED PAGE KEEPS ITS SLUG AND ITS ROW - owner, 2026-08-29, repealing the fourth supersession
# step of 2026-08-22 in his own words: *"снимаем это правило, оно мешает и не несет пользы. Страница
# уходит в архив со slug и authority"*. So the STALE direction asks about `wiki/` AND `archive/`,
# and a row whose page has been archived is not stale.
#
# WHAT REPEALING IT REMOVED WAS A DEADLOCK RATHER THAN A CHORE. The rule was written when pages were
# retired one at a time; the sweep archives hundreds in one run, and the register may be written only
# by the librarian, whom `lock-the-librarian.ps1` refuses to dispatch on a red tree. On 2026-08-29 a
# sweep of 239 pages left 239 stale rows, and the only party permitted to repair them was locked out
# by the redness those rows caused.
#
# THE OTHER DIRECTION STILL ASKS ABOUT `wiki/` ALONE, deliberately. Pages retired before this date
# had their rows deleted under the old rule; asking archive for a group would light up every one of
# them at once, which is a demand to write rows for pages nobody will look up rather than a defect.
cmd_check() {
  local fail=0 tree tree_all reg stale ungrouped dupes count
  if [ ! -f "$REGISTER" ]; then
    echo "$SELF: no register at $REGISTER - the lookup the admission rule is decided by does not exist"
    return 1
  fi

  tree=$(corpus | awk -F'\t' '$1 != "-" { print $1 }' | sort -u)
  reg=$(register_pairs | cut -f2 | sort -u)

  # `archive/` is read by a grep rather than by `corpus`, which caches one walk of `wiki/` and is
  # what every other subcommand reads. Only this one direction needs the wider set, and widening the
  # cache would quietly change `--near`, `--group`, `--binding` and `--orphans` along with it.
  # Whether the LOOKUP should reach archived pages is a real question and a separate one: it would
  # make *does this claim already have a page* answerable with "yes, and it is retired", which is a
  # better answer than silence. It is not built here and is not smuggled in.
  tree_all=$( { printf '%s\n' "$tree"
                grep -rh --include='*.md' '^authority:' "$VAULT/archive" 2>/dev/null \
                  | sed 's/\r$//; s/^authority:[ \t]*//; s/[ \t]*$//'
              } | grep -v '^$' | sort -u )

  stale=$(comm -13 <(printf '%s\n' "$tree_all") <(printf '%s\n' "$reg") 2>/dev/null | grep -v '^$')
  ungrouped=$(comm -23 <(printf '%s\n' "$tree") <(printf '%s\n' "$reg") 2>/dev/null | grep -v '^$')

  if [ -n "$stale" ]; then
    while IFS= read -r s; do
      [ -n "$s" ] && echo "$SELF: '$s' is grouped in the register and no page carries it"
    done <<< "$stale"
    fail=1
  fi
  if [ -n "$ungrouped" ]; then
    while IFS= read -r s; do
      [ -n "$s" ] && echo "$SELF: '$s' is carried by a page and is in no group - the lookup cannot reach it"
    done <<< "$ungrouped"
    fail=1
  fi

  # A slug in two groups makes the lookup ambiguous in the direction that hides a page: whichever
  # group is read first answers, and the other one is never opened.
  dupes=$(register_pairs | cut -f2 | sort | uniq -d)
  if [ -n "$dupes" ]; then
    while IFS= read -r s; do
      [ -n "$s" ] && echo "$SELF: '$s' is in more than one group"
    done <<< "$dupes"
    fail=1
  fi

  if [ "$fail" -eq 0 ]; then
    count=$(printf '%s\n' "$tree" | grep -c .)
    echo "$SELF: the register and the tree agree, $count slugs grouped"
  fi
  return "$fail"
}

# `--binding`: THE REPORT IS THE ACCEPTANCE TEST FOR THE BACK-FILL, NOT A STATISTIC. Two figures
# were measured before any page was marked - six `DIVERGENCE:` titles, and about thirty deferrals
# out of 189 - and a run that disagrees with them means the marking was hurried rather than done.
# `divergence` is the only value a script can verify, so it is verified here and the other two are
# left as counts a human compares against what he expects.
cmd_binding() {
  local rows titled mismatched
  rows=$(corpus | awk -F'\t' '$4 == "decisions" { print }')
  echo "$SELF: what wiki/decisions/ declares about itself"
  echo
  printf '%s\n' "$rows" | awk -F'\t' '{ c[$5]++ } END { for (v in c) printf "  %-14s %s\n", v, c[v] }' \
    | sort -k2 -rn
  echo
  titled=$(printf '%s\n' "$rows" | awk -F'\t' '$3 ~ /^DIVERGENCE:/ { print $2 }')
  echo "  pages titled DIVERGENCE:  $(printf '%s\n' "$titled" | grep -c .)"
  mismatched=$(printf '%s\n' "$rows" | awk -F'\t' '
    ($3 ~ /^DIVERGENCE:/ && $5 != "divergence") ||
    ($3 !~ /^DIVERGENCE:/ && $5 == "divergence") { print $2 "\t" $5 }')
  if [ -n "$mismatched" ]; then
    echo
    while IFS= read -r row; do
      [ -n "$row" ] && echo "$SELF: $(printf '%s' "$row" | cut -f1) declares '$(printf '%s' "$row" | cut -f2)' and its title disagrees"
    done <<< "$mismatched"
    return 1
  fi
  echo "  every DIVERGENCE: title declares divergence, and nothing else does"
  return 0
}

# `--trace`: THE AUDIT HALF, AND IT IS ALMOST FREE BECAUSE THE TRAIL ALREADY EXISTS. Every ingest
# writes a coverage sidecar beside its source, keyed by LINE NUMBER, carrying that line's verdict -
# `page:<name>` where the line was compiled into a page. That is source-to-page. This is the
# reverse, which nothing had, and it is what makes a page that ABSORBED a claim auditable rather
# than merely plausible: the admission rule sends units into existing pages, so "where did this
# paragraph come from" stops being answerable by the page's own `sources:` list alone.
cmd_trace() {
  local page="$1" found=0 sidecar src line verdict names
  [ -n "$page" ] || { echo "$SELF: --trace needs a page name"; return 2; }
  while IFS= read -r sidecar; do
    [ -n "$sidecar" ] || continue
    src="${sidecar%.coverage.tsv}.md"
    while IFS="$(printf '\t')" read -r line verdict; do
      names="${verdict%% *}"
      case "$names" in page:*) names="${names#page:}" ;; *) continue ;; esac
      # The verdict may name several pages: `page:a,b,c`. Match a whole member, never a substring,
      # or `the-pre-task-ledger` would match `the-pre-task-ledger-holds-one-session` and the trail
      # would lie in the direction of claiming provenance it does not have.
      case ",${names}," in *",${page},"*) ;; *) continue ;; esac
      found=1
      printf '%s:%s\n' "$src" "$line"
      [ -f "$src" ] && sed -n "${line}p" "$src" | sed 's/^/    /'
    done < "$sidecar"
  done < <(find "$VAULT/raw" -name '*.coverage.tsv' 2>/dev/null | sort)
  if [ "$found" -eq 0 ]; then
    echo "$SELF: no sidecar names '$page' - it predates the sidecars, or the name is wrong"
    return 1
  fi
  return 0
}

# THE ARGUMENTLESS MODES COMPOSE, AND UNTIL 2026-08-22 THE SECOND ONE WAS SILENTLY DROPPED. This
# read `case "${1:---list}"` and dispatched exactly once, so `--check --binding` ran the check,
# ignored the rest of the line, and exited 0 with a report that looked complete. It was found the
# day `--check --binding` became the command an acceptance criterion is decided by: an instrument
# that answers half a question in the voice of a whole one is the failure this project keeps
# meeting, and it fails towards "nothing to report" every time.
#
# THE MODES THAT TAKE AN OPERAND DO NOT COMPOSE, and they exit after running. `--near foo --check`
# would need a parser that knows which flags consume the next word, and this script has one caller
# shape for those - a human asking one question. So they keep the single-dispatch behaviour, and
# anything after them is refused rather than ignored, which is the same reason the loop exists.
#
# THE EXIT CODE IS THE WORST OF THE MODES RUN, not the last. `--check` returning 1 while
# `--binding` returns 0 must not read as success, and `$?` of a sequence is the last command's.
[ "$#" -eq 0 ] && set -- --list
status=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --list)    cmd_list    || status=1 ;;
    --orphans) cmd_orphans || status=1 ;;
    --binding) cmd_binding || status=1 ;;
    --check)   cmd_check   || status=1 ;;
    --near)    cmd_near  "${2:-}"; exit $? ;;
    --group)   cmd_group "${2:-}"; exit $? ;;
    --trace)   cmd_trace "${2:-}"; exit $? ;;
    -h|--help) usage; exit 0 ;;
    *)         echo "$SELF: unknown argument: $1"; echo; usage; exit 2 ;;
  esac
  shift
done
exit "$status"
