#!/usr/bin/env bash
# Answers one question about a source document: has every claim in it been accounted for?
#
# Two modes, chosen by whether the sidecar exists. The sidecar is the source's own name with
# `.md` replaced by `.coverage.tsv` - `2026-08-13-x.md` is accompanied by
# `2026-08-13-x.coverage.tsv`. A sidecar under any other name is not found, and the run
# silently falls back to evidence mode, which is why that mode now exits non-zero.
#
#   VERDICT MODE  (the sidecar is present)
#     Reports units that carry no verdict, and verdicts that are not verdicts. An ingest is
#     finished when both lists are empty. Format: one line per unit, LINE<TAB>VERDICT, where
#     VERDICT is one of
#       page:<name>[,<name>...]  compiled into those wiki pages, which must exist
#       journal                  session state, not knowledge; stays in raw/
#       elsewhere:<where>        belongs to CLAUDE.md, the code, the tracker, or log.md
#       skip:<reason>            deliberately not compiled, and why
#     Anything after the name or the reason is free prose and is kept: a verdict that
#     explains itself is worth more than a tidy one.
#
#   EVIDENCE MODE (no sidecar)
#     A first pass to help build one: for each unit it takes distinctive tokens -
#     backticked identifiers, snake_case, CamelCase - and looks for them in the vault.
#     A unit whose token appears on a page is evidence-backed; the rest need a human.
#     It exits 1, always: a first pass is not a verdict and must not read as one to
#     anything checking the exit code.
#
# WHAT THIS PROVES, AND WHAT IT DOES NOT.
#   It proves nothing was silently dropped, because the denominator is mechanical.
#   It does NOT prove a compiled unit was transcribed correctly: a page describing
#   behaviour a later slice replaced passes both modes without a murmur, identifiers and
#   all. Fidelity is checked by sampling the sidecar's line numbers against their pages,
#   and by the acceptance questions. Coverage is free; fidelity is not. The sample has
#   already caught one page the coverage half called finished and correct.
#
# Run: bash scripts/vault-coverage.sh <file.md> [--list-unmatched]
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

src="${1:-}"
[ -n "$src" ] || { echo "usage: vault-coverage.sh <file.md> [--list-unmatched]" >&2; exit 2; }
[ -f "$src" ] || { echo "no such file: $src" >&2; exit 2; }
list_unmatched=0
[ "${2:-}" = "--list-unmatched" ] && list_unmatched=1

VAULT="${VAULT:-}"
if [ -z "$VAULT" ]; then
  # The vault is whichever top-level directory holds a wiki/. Its name is the name
  # Obsidian displays, so it is the owner's to change, and nothing here may depend on it.
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
fi
[ -n "$VAULT" ] || { echo "no vault found (no top-level directory contains a wiki/)" >&2; exit 1; }

# The unit list is taken once and its exit status is respected: an unclosed fence makes
# vault-units.sh exit 3, and a denominator built from a truncated document would make every
# number below a lie in the reassuring direction.
units=$(bash scripts/vault-units.sh "$src")
units_status=$?
if [ "$units_status" -ne 0 ]; then
  echo "vault-coverage: refusing to count - vault-units.sh exited $units_status on $src" >&2
  exit "$units_status"
fi

sidecar="${src%.md}.coverage.tsv"

# The page list is built once. It used to be one `find` over the vault per verdict, which is
# 332 process spawns on the migrated handoff and 21 seconds - and /vault-lint runs coverage over
# every journal there has ever been, so that cost compounds on both axes as the vault grows.
declare -A page_exists
while IFS= read -r known; do
  [ -n "$known" ] && page_exists[$known]=1
done < <(find "$VAULT/wiki" "$VAULT/archive" -name '*.md' -size +0 2>/dev/null \
         | sed 's|.*/||; s|\.md$||' | sort -u)

# ---------------------------------------------------------------- verdict mode
if [ -f "$sidecar" ]; then
  missing=0; total=0; malformed=0
  declare -A verdict
  # `|| [ -n "$l" ]` because a file whose last line carries no newline ends the loop before
  # that line is handled: a sidecar written without a trailing newline silently lost its
  # final verdict, and the unit it belonged to was then reported as unaccounted for.
  while IFS=$'\t' read -r l v || [ -n "${l:-}" ]; do
    # A trailing CR is stripped from BOTH fields. git rewrote every sidecar to CRLF on
    # the checkout that merged this branch, and `journal` became `journal\r`: 317 of 411
    # verdicts across three sources turned into BAD VERDICT lines the moment the branch
    # touched main. The gate that retired a 129 KB file went red on a line ending.
    l=${l%$'\r'}; v=${v%$'\r'}
    [ -n "${l:-}" ] && verdict[$l]="$v"
  done < "$sidecar"

  # A verdict that is not one of the four is not an accounting. `/ingest` says there is no
  # fifth option; before this, "banana" on every line reported INGEST COMPLETE. The realistic
  # case is not a joke word but a mistyped page name, which turns "compiled" into "lost".
  while IFS=$'\t' read -r l v || [ -n "${l:-}" ]; do
    l=${l%$'\r'}; v=${v%$'\r'}
    [ -n "${l:-}" ] || continue
    case "$v" in
      journal) ;;
      elsewhere:?*) ;;
      skip:?*) ;;
      page:?*)
        # The names run up to the prose, and the prose is introduced by an em dash -
        # ` — `, the way every verdict in this vault already writes it. Two other rules
        # were tried and both were wrong: truncating at the first space validated only the
        # first name of a list and lost the rest silently, and splitting on space as well
        # as comma rejected the free prose this file's own header promises, turning one
        # real annotation into eleven BAD VERDICT lines and leaving the ingest gate red
        # with no legal fix. Names first, prose after the dash, and both are kept.
        names=${v#page:}; names=${names%%" — "*}
        old_ifs=$IFS; IFS=', '
        for n in $names; do
          n=${n#"${n%%[![:space:]]*}"}          # leading space
          n=${n%% *}                            # and everything from the first space on
          [ -n "$n" ] || continue
          if [ -z "${page_exists[$n]:-}" ]; then
            echo "BAD VERDICT $src:$l  page:$n does not exist in the wiki"
            malformed=$((malformed + 1))
          fi
        done
        IFS=$old_ifs ;;
      *)
        echo "BAD VERDICT $src:$l  '$v' is not one of journal / page: / elsewhere: / skip:"
        malformed=$((malformed + 1)) ;;
    esac
  done < "$sidecar"

  while IFS='|' read -r line kind text; do
    [ "$kind" = "heading" ] && continue
    total=$((total + 1))
    if [ -z "${verdict[$line]:-}" ]; then
      missing=$((missing + 1))
      printf 'NO VERDICT %s:%s  [%s]  %s\n' "$src" "$line" "$kind" \
        "$(printf '%s' "$text" | cut -c1-100)"
    fi
  done <<< "$units"

  echo
  echo "$src: $((total - missing)) of $total units carry a verdict"
  [ "$malformed" -gt 0 ] && echo "$malformed verdicts are not verdicts"
  [ "$missing" -eq 0 ] && [ "$malformed" -eq 0 ] && { echo "INGEST COMPLETE"; exit 0; }
  [ "$missing" -gt 0 ] && echo "INGEST UNFINISHED: $missing units still need one"
  exit 1
fi

# --------------------------------------------------------------- evidence mode
echo "no sidecar at $sidecar - evidence mode (this is a first pass, not a verdict)"
echo

section=""; total=0; matched=0
declare -A sec_total sec_matched
order=()

while IFS='|' read -r line kind text; do
  if [ "$kind" = "heading" ]; then
    section=$(printf '%s' "$text" | sed 's/^#\{1,6\} //')
    [ -n "${sec_total[$section]+x}" ] || { order+=("$section"); sec_total[$section]=0; sec_matched[$section]=0; }
    continue
  fi
  [ -n "$section" ] || section="(preamble)"
  [ -n "${sec_total[$section]+x}" ] || { order+=("$section"); sec_total[$section]=0; sec_matched[$section]=0; }

  tokens=$(printf '%s' "$text" \
    | grep -o '`[^`]*`' | tr -d '`' \
    | grep -oE '[A-Za-z_][A-Za-z0-9_.]{4,}' | sort -u | head -4)
  [ -z "$tokens" ] && tokens=$(printf '%s' "$text" \
    | grep -oE '\b[a-z]+_[a-z_]+\b|\b[A-Z][a-z]+[A-Z][A-Za-z]+\b' | sort -u | head -4)

  total=$((total + 1))
  sec_total[$section]=$(( ${sec_total[$section]} + 1 ))

  hit=""
  if [ -n "$tokens" ]; then
    while IFS= read -r t; do
      [ -z "$t" ] && continue
      if grep -rqlF "$t" "$VAULT/wiki" --include='*.md' 2>/dev/null; then hit="$t"; break; fi
    done <<< "$tokens"
  fi

  if [ -n "$hit" ]; then
    matched=$((matched + 1)); sec_matched[$section]=$(( ${sec_matched[$section]} + 1 ))
  elif [ "$list_unmatched" -eq 1 ]; then
    printf '%s:%s  [%s]  %s\n' "$section" "$line" "$kind" "$(printf '%s' "$text" | cut -c1-110)"
  fi
done <<< "$units"

if [ "$list_unmatched" -eq 0 ]; then
  printf '%-56s %s\n' "SECTION" "EVIDENCED / UNITS"
  for s in "${order[@]}"; do
    [ "${sec_total[$s]}" -eq 0 ] && continue
    printf '%-56s %3d / %-3d %s\n' "$(printf '%s' "$s" | cut -c1-54)" \
      "${sec_matched[$s]}" "${sec_total[$s]}" \
      "$( [ "${sec_matched[$s]}" -eq 0 ] && echo '  <-- nothing evidenced' )"
  done
  echo
  echo "TOTAL: $matched of $total units evidenced in $VAULT/wiki"
  echo "Write $sidecar to turn this into verdicts."
fi
exit 1
