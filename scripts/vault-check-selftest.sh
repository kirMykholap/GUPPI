#!/usr/bin/env bash
# Verification by removal for the three vault scripts.
#
# Every rule is broken on purpose in a throwaway copy of the vault, one at a time, and the
# check must name the defect and end with the right exit code. A rule that stays silent here
# is a rule that is not there - and this project has shipped several of those: a link check
# satisfied by its own schema examples, a wikilink satisfied by a 0-byte file, a unit rule
# that only saw bold text, a tag rule blind to the spelling Obsidian writes, and the whole
# script printing "ok" after an unquoted $(find) word-split a path containing a space and it
# read nothing at all.
#
# The vault is never touched: everything happens in a copy under a temporary directory.
#
# Run: bash scripts/vault-check-selftest.sh
#      SCRIPTS=/some/other/dir bash scripts/vault-check-selftest.sh   # test a candidate
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
REPO=$(pwd)
SCRIPTS="${SCRIPTS:-$REPO/scripts}"
SELF="${BASH_SOURCE[0]}"

# THIS SUITE HAD NO ARGUMENT CONTRACT AT ALL until 2026-08-24: `SCRIPTS=` and `JOBS=` were its only
# knobs and anything on the command line was ignored in silence. The gate refuses an unknown
# argument with a code of its own, and a sibling script that shrugs at one instead teaches the
# opposite lesson at the same prompt. So it refuses too, and with the same code.
#
# `--only` TAKES A SUBSTRING AND NOT A REGULAR EXPRESSION, and the word is in the usage line because
# it was not. `--only 'archive|units'` reads as the literal string `archive|units`, matches nothing,
# and until 2026-08-28 a run that selected no case still printed `caught 1, missed 0` and exited 0 -
# the one coming from the baseline copy, which no filter ever saw. `make smoke ONLY=<typo>` was
# therefore a clean slice that had run nothing. The matcher stays a substring deliberately: a second
# syntax is a thing to remember, and the protection against a wrong slice is a case rather than a
# richer pattern. What changed is that an empty selection is now a refusal.
LIST=0
ONLY=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --list) LIST=1; shift ;;
    --only) ONLY="${2:-}"; shift 2
            [ -n "$ONLY" ] || { echo "SELFTEST: --only needs a substring"; exit 2; } ;;
    *) echo "SELFTEST: unknown argument: $1 (the legal ones are --list and --only <substring>)"; exit 2 ;;
  esac
done

# `--list` IS A SWEEP OF THIS FILE AND RUNS NOTHING, which is the only shape that cannot drift from
# what it lists. The alternative - walking the dispatchers and printing instead of running - cannot
# see the fifteen cases written inline in the archive, catalogue and units sections, which reach
# `report` directly and go through no dispatcher at all. A `--list` blind to those would understate
# the suite by fifteen and read as complete, which is the exact defect the corpus keeps meeting.
#
# So both are swept from the source: a dispatcher invocation at column zero takes its name from the
# first quoted string on that line, and an inline case takes its name from `report "..."` written
# with a literal rather than with `$case_name`. Both are deduplicated, because an inline case
# reports its name twice - once on each branch of a `&&`/`||` pair.
#
# WHAT IT DOES NOT PROMISE: that a listed case will run, or that a running case is listed. That is
# what the count case pins - `--list` against the number a real run reports - and it is the only
# thing standing between this and a third register that drifts. That case is at the bottom of this
# file, because only a whole unfiltered run can take the second number.
#
# THE SECTIONS ARE LISTED TOO, and they are listed because they are what a slice actually IS. Until
# 2026-08-28 `--only` compared its substring against a case NAME alone, so selecting "everything
# about the archive script" worked only because those cases happen to carry the word `archive` in
# their names - a coincidence, not a mechanism, and one that silently selects nothing the day a case
# is named differently. Both lists are swept from this file's own text and neither is maintained.
#
# THE THREE SWEEPS ARE FUNCTIONS BECAUSE THEY HAVE TWO CALLERS. `--list` prints them and the count
# case at the bottom of this file compares the first two against what a run wrote; the same
# expression written twice is the shape this whole corpus exists to warn about, and one of them
# would be repaired without the other the first time a dispatcher is renamed.
#
# `sweep_inline` SKIPS COMMENT LINES, and it did not until 2026-08-28. The paragraph above explains
# an inline case by quoting the literal `report "..."`, and the sweep counted that sentence as a
# case - so `--list` said 16 inline where 15 exist, and had said so since it was built. Nothing
# compared it against a run, which is exactly what the count case now does.
sweep_dispatched() { sed -n 's/^\(run_[a-z_]*\|cov_case\)[[:space:]]\{1,\}"\([^"]*\)".*/\2/p' "$SELF"; }
sweep_inline()     { sed -n '/^[[:space:]]*#/d; s/.*[^_a-z]report[[:space:]]\{1,\}"\([^"$][^"]*\)".*/\1/p' "$SELF" | sort -u; }
sweep_sections()   { sed -n 's/^section[[:space:]]\{1,\}"\([^"]*\)".*/\1/p' "$SELF"; }

if [ "$LIST" = 1 ]; then
  dispatched=$(sweep_dispatched)
  inline=$(sweep_inline)
  sections=$(sweep_sections)
  n_d=$(printf '%s\n' "$dispatched" | grep -c . )
  n_i=$(printf '%s\n' "$inline"     | grep -c . )
  n_s=$(printf '%s\n' "$sections"   | grep -c . )
  echo "SELFTEST: --list: $((n_d + n_i)) case(s) - $n_d dispatched, $n_i written inline"
  printf '%s\n' "$dispatched" | sed 's/^/  /'
  printf '%s\n' "$inline"     | sed 's/^/  (inline) /'
  echo "SELFTEST: --list: $n_s section(s) - --only takes a substring of any line below as well"
  printf '%s\n' "$sections"   | sed 's/^/  (section) /'
  exit 0
fi

# A SUBSTRING THAT MATCHES NOTHING IS REFUSED HERE, BEFORE THE SANDBOX EXISTS. The same sweeps
# `--list` prints already answer whether it can match anything, so a run that will select no case
# need not first pay twenty seconds for a baseline gate it is about to discard. `grep -F` is the
# fixed-string search that mirrors what `wanted` does with `case` - the whole point being that this
# is a substring and not a pattern.
#
# THE COUNTER AT THE BOTTOM OF THIS FILE STAYS, and it is not redundant with this. This asks what the
# sweep can see; that asks what actually ran. `--list` explicitly does not promise the two agree -
# that is what the count case is for - so a filter that trusted only the sweep would inherit the
# sweep's blind spots and report them as a selection.
#
# IT IS TESTED NAME BY NAME WITH `case`, and not by piping the names into `grep -q`. Under
# `pipefail` a `grep -q` that matches leaves early, the `sed` upstream of it dies of SIGPIPE, and
# the PIPELINE reports that failure - so the refusal fired on every substring that DID match, which
# is the opposite of what it is for. It was written that way first and caught here.
if [ -n "$ONLY" ]; then
  only_hit=0
  only_names=$(sweep_dispatched; sweep_inline; sweep_sections)
  while IFS= read -r only_name; do
    [ -n "$only_name" ] || continue
    case "$only_name" in *"$ONLY"*) only_hit=1; break ;; esac
  done <<< "$only_names"
  if [ "$only_hit" -eq 0 ]; then
    echo "SELFTEST: --only '$ONLY' selects no case."
    echo "          It is a SUBSTRING of a case name or of a section name, never a regular"
    echo "          expression, so an alternation such as 'a|b' matches nothing at all."
    echo "          Run: bash scripts/vault-check-selftest.sh --list"
    exit 2
  fi
fi

VAULT_DIR=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
            | sed 's|/wiki$||; s|^\./||' | sort | head -1)
[ -n "$VAULT_DIR" ] || { echo "SELFTEST: no vault found"; exit 1; }

SANDBOX=$(mktemp -d)
trap 'rm -rf "$SANDBOX"' EXIT
PRISTINE="$SANDBOX/pristine"

mkdir -p "$PRISTINE/scripts"
# `vault-authority.sh` joined this list on 2026-08-21 WITH rule 13, and the pair is not optional.
# Rule 13 asks its question by RUNNING the tool - rule 12's shape - so a sandbox without the tool
# gets `missing file` from a `note`, which is `fail=1`, which turns every one of the 27 `run_clean`
# cases red and lets every `run_case` expecting exit 1 pass without its own verdict ever firing.
# That is the coupling this file's own comment above `run_case` warns about, and the question it
# says to ask - which cases does a new rule couple - has exactly this answer.
# `vault-measure.py` joined this list on 2026-08-26 WITH rule 15, for the reason the paragraph
# above records rather than for a new one - and the question that paragraph says to ask was asked
# BEFORE the rule was written rather than after the suite went red. Rule 15 also asks its question
# by running its script, so a sandbox without it gets `missing file` from a `note`, and the 27
# `run_clean` cases go red together. It is the first Python script in this list: the gate finds a
# bare interpreter rather than using `uv run`, precisely because nothing here copies a
# `pyproject.toml` and there is no environment in the sandbox to run.
cp "$SCRIPTS/vault-check.sh" "$SCRIPTS/vault-units.sh" "$SCRIPTS/vault-coverage.sh" \
   "$SCRIPTS/vault-catalogue.sh" "$SCRIPTS/vault-inject.sh" "$SCRIPTS/vault-authority.sh" \
   "$SCRIPTS/vault-archive.sh" "$SCRIPTS/vault-measure.py" \
   "$PRISTINE/scripts/"
# THE VAULT KEEPS ITS OWN NAME IN THE SANDBOX, AND THAT IS LOAD-BEARING (2026-08-19). It used to
# be copied to `vault_copy`. The corpus cites paths from the REPOSITORY ROOT, and eleven of those
# citations point inside the vault itself - `job_hunt_ai_vault/CLAUDE.md`, and two naming
# `wiki/decisions/_schema.yaml`. Under a renamed copy none of them resolved, so the placeholder
# loop below materialised `job_hunt_ai_vault/wiki/decisions/_schema.yaml` as an empty file - and a
# directory holding a `wiki/` is the whole of what vault discovery looks for. The decoy sorted
# first and won every case: missing directories, missing registers, `no required: keys parsed`,
# and the baseline copy BROKEN before a single case ran. Measured that day: caught 24, missed 96,
# while the suite still exited 0 and the number last quoted was caught 120, missed 0.
#
# Rejected: pointing the check at the copy with `VAULT=`. It removes the ambiguity and stops
# exercising discovery in 118 of 120 cases, to work around a sandbox that is not a faithful
# mirror rather than to make it one. Discovery keeps its own two cases, which rename the vault.
cp -r "$REPO/$VAULT_DIR" "$PRISTINE/$VAULT_DIR"

# Rule 8 reads the section set from `.claude/templates/handoff.md`, so the sandbox needs it or
# every case here would run against a check that reported the template missing and failed for a
# reason no case is about.
mkdir -p "$PRISTINE/.claude/templates"
cp "$REPO/.claude/templates/handoff.md" "$PRISTINE/.claude/templates/handoff.md"

# Every destination a current page GOVERNS is materialised, which the placeholder loop below does
# not do: it walks `sources:`, and a page names its file in `governs:`. Without this the first real
# rule page turns the whole suite red - the injector opens a destination the sandbox does not have,
# rule 12 reports it, and the pristine copy fails before a single case runs, taking every
# `run_clean` and every expected exit code with it.
#
# SWEPT FROM THE PAGES, never listed. This suite has already gone red for keeping its own copy of
# the vault's layout, and a list of governed files here would be a second one.
#
# THE SWEEP FOLLOWS THE INJECTOR'S GLOB AND NOT A FOLDER (2026-08-18). It used to walk
# `wiki/rules/` because that is where the injector walked; `governs:` became a property of any
# page the same day this line stopped being right. The question a path-valued field always
# raises is what the harness has to create now, and the answer has to be read off the subject
# rather than off the folder the subject used to live in - which is exactly how this loop came
# to exist in the first place.
#
# Where the repository has the file it is copied WHOLE, and that is the point: the region it
# carries comes with it, so the rendering the injector compares against is the real one. An empty
# placeholder would satisfy the path and fail the comparison, which is a green that means nothing.
#
# THIS LOOP RUNS FIRST, AND THE ORDER IS THE WHOLE FIX FOR A GREEN THAT MEANT NOTHING (2026-08-19).
# It used to run second. `CLAUDE.md` is BOTH a `governs:` destination and a `sources:` citation, so
# the placeholder loop reached it first and created it as a ZERO-BYTE file; the `[ -e ]` guard below
# then read that as already materialised and the real file was never copied. The sandbox's CLAUDE.md
# carried no region, rule 12 reported its markers, coverage read `0 of 14` against the tree's
# `1 of 14`, and 96 of 120 cases went MISSED behind that ambient red - while the suite still exited
# 0 and the last number anybody quoted was `caught 120, missed 0`.
#
# Rejected: `[ -s ]` in place of `[ -e ]` below. It repairs this instance and states the wrong rule.
# An empty file can be a legitimate destination; what is actually true is that the real file wins
# over a placeholder standing in for it, and ordering is how that is said.
while IFS= read -r dest; do
  [ -n "$dest" ] || continue
  [ -e "$PRISTINE/$dest" ] && continue
  mkdir -p "$PRISTINE/$(dirname "$dest")"
  if [ -f "$REPO/$dest" ]; then cp "$REPO/$dest" "$PRISTINE/$dest"; else : > "$PRISTINE/$dest"; fi
#
# AND IT READS THE INLINE LIST, WHICH IT DID NOT UNTIL 2026-08-22. `governs:` learned to name more
# than one file on 2026-08-21; the gate and the injector were both taught the four rules that day
# and **this loop is a THIRD parser of the same field** that nobody counted. It kept the scalar
# `sed`, so the first rule page to govern two files handed it the literal string
# `[a/one.md, b/two.md]` as one destination - it materialised a file under that name, neither real
# destination was copied, and rule 12 went red in EVERY case: `caught 112, missed 44`, against
# three real failures. The corpus records that two parsers of one field were written from the same
# four rules and deliberately not shared; the cost of that choice is that a third one is invisible
# until it meets a page that exercises the difference, and this is that bill arriving.
#
# The four rules, the same ones: trim, strip one layer of quotes, split an inline list on commas,
# and a bare value is a list of one.
done < <(find "$PRISTINE/$VAULT_DIR/wiki" -mindepth 2 -maxdepth 2 -name '*.md' 2>/dev/null \
         | xargs -r grep -l '^status: current' 2>/dev/null \
         | xargs -r sed -n 's/^governs:[[:space:]]*//p' \
         | awk '{
             line = $0
             gsub(/^[ \t]+|[ \t]+$/, "", line)
             if (line ~ /^\[.*\]$/) {
               sub(/^\[/, "", line); sub(/\]$/, "", line)
               n = split(line, parts, /,/)
               for (i = 1; i <= n; i++) {
                 t = parts[i]
                 gsub(/^[ \t]+|[ \t]+$/, "", t)
                 gsub(/^["\047]|["\047]$/, "", t)
                 if (t != "") print t
               }
             } else {
               gsub(/^["\047]|["\047]$/, "", line)
               if (line != "") print line
             }
           }' | sort -u)

# THIS LOOP RUNS SECOND, AFTER THE `governs:` SWEEP ABOVE, AND ITS `[ -e ]` GUARD IS WHAT MAKES THAT
# SAFE: a path already materialised as the real file is left alone. Reversing the two is the bug
# recorded above, and it was silent for as long as it stood.
# The corpus cites files that live outside the vault - plans, specs, source, skills. The
# sandbox is not the repository, so those paths are recreated as empty placeholders: the rule
# under test asks whether a citation resolves, not what it contains.
# Both spellings, because the check learned both: a page whose `sources:` is a block list would
# otherwise get no placeholder, and the whole "must NOT fail" half of this suite would go red as
# if the check had regressed.
{ grep -rh '^sources:' --include='*.md' "$PRISTINE/$VAULT_DIR/wiki" 2>/dev/null | grep -o '"[^"]*"' | tr -d '"'
  grep -rhA6 '^sources:' --include='*.md' "$PRISTINE/$VAULT_DIR/wiki" 2>/dev/null \
    | grep -E '^[ \t]*-[ \t]+' | sed 's/^[ \t]*-[ \t]*//; s/^"//; s/"$//'
} | grep -v '^\[\[' | grep -v '^http' | grep -v '^$' | sort -u \
  | while IFS= read -r ref; do
      [ -e "$PRISTINE/$ref" ] || [ -e "$PRISTINE/$VAULT_DIR/$ref" ] || {
        mkdir -p "$PRISTINE/$(dirname "$ref")"; : > "$PRISTINE/$ref"; }
    done

# A TOOL A RULE DELEGATES TO MUST BE THE REAL FILE, AND THE LOOP ABOVE IS WHY THIS GUARD EXISTS.
# Rules 12 and 13 ask their questions by RUNNING a script rather than re-deriving what it derives.
# The placeholder loop materialises every path a page cites in `sources:` as a ZERO-BYTE file, and
# a page citing `scripts/vault-authority.sh` is exactly the kind of page this work writes. A stub
# satisfies `[ -f ]`, runs, prints nothing, and the rule says nothing - so the rule passes having
# checked nothing, and every case written for it passes with it. MEASURED 2026-08-21: with a
# zero-byte tool, rule 13 printed not one line.
#
# The `cp` at the top wins because it runs before the loop and the loop's `[ -e ]` guard leaves a
# real file alone. That ordering is the whole protection, and it is invisible - hence this.
for tool in vault-inject.sh vault-authority.sh; do
  [ -s "$PRISTINE/scripts/$tool" ] || {
    echo "SELFTEST: $PRISTINE/scripts/$tool is empty or missing - a rule delegates to it by" >&2
    echo "          running it, so a stub would make that rule silent and every case for it green." >&2
    echo "          Add it to the cp at the top of this file." >&2
    exit 1; }
done

# CASES RUN CONCURRENTLY, AND EVERYTHING BELOW EXISTS TO STOP THAT COSTING A VERDICT (2026-08-20).
# Serial, this suite took 1093 s - 130 cases times one full 8512 ms gate, measured end to end, with
# the per-case tree copy and diff under a tenth of a second of it. The cases were already
# independent by construction: each starts from an untouched copy of `$PRISTINE`. One line made
# them serial - every helper wrote into the same `$SANDBOX/work`.
#
# THE TRAP, AND IT IS THE ONE THIS PROJECT ALREADY NAMES: a `report` that increments `pass` inside
# a backgrounded subshell increments a copy. The parent's counters stay at zero, the suite prints
# `caught 0, missed 0` and exits 0 - faster, green, and checking nothing, which is the owner's
# stated worse failure. So NO VERDICT LIVES IN A VARIABLE. Every case writes its verdict to its own
# file, and the totals are counted from those files after `wait`.
#
# ORDER IS THE FILENAME, NOT THE FINISH. Results are numbered as they are DISPATCHED, so the report
# reads in script order however the cases interleave, and two runs of a green suite are
# byte-identical. Section headings take a number too, or they would all print before the first
# result.
JOBS="${JOBS:-$(nproc 2>/dev/null || echo "${NUMBER_OF_PROCESSORS:-4}")}"
RESULTS="$SANDBOX/results"; mkdir -p "$RESULTS"
case_no=0

# Sets `$RF_NEXT` rather than echoing it: `$(next_rf)` would run in a subshell and the parent's
# counter would never move, which scrambles the order silently and passes every test.
next_rf() { case_no=$((case_no + 1)); RF_NEXT=$(printf '%s/%05d' "$RESULTS" "$case_no"); }

# `--only` SKIPS A CASE BEFORE IT COSTS ANYTHING, which is why this sits at the top of every
# dispatcher rather than at `report`. Between the two lies the expensive part - a whole-tree copy
# of 704 files and a full gate run - so a filter at the verdict would print the right report and
# save nothing, which is the wrong half of the point.
#
# THE NUMBER IS TAKEN EVEN WHEN THE CASE IS SKIPPED. Results are numbered as they are DISPATCHED so
# that two runs of a green suite are byte-identical; a filter that stopped the counter would
# renumber every case after it and quietly reorder the report.
#
# An empty `$ONLY` matches everything through `*""*`, so a bare run needs no branch here and takes
# the same path as a filtered one. A filter with a second code path is a filter that is only tested
# on one of them. It also means the section branch below is never reached on a bare run: the name
# matched first, and the answer would have been the same.
#
# THE SECTION COUNTS AS WELL AS THE NAME, added 2026-08-28. A slice of this suite is a section - the
# archive script, the marked regions, units and coverage - and matching names alone made a slice
# work by coincidence over the words those cases happen to contain. `$CURRENT_SECTION` is the last
# `section` declared above the case, set as that line prints its own record, so the grouping is
# derived from where the case is written and nothing maintains a second list of it.
#
# `$selected` IS COUNTED BECAUSE `$skipped` CANNOT ANSWER THE QUESTION. A filter that matched nothing
# skips every case and looks, from the skip count alone, exactly like one that matched most of them.
# The refusal at the bottom of this file reads this counter and nothing else.
skipped=0
selected=0
CURRENT_SECTION=""
wanted() {            # wanted <case name> - takes the number, answers whether the case runs
  next_rf
  case "$1" in
    *"$ONLY"*) selected=$((selected + 1)); return 0 ;;
  esac
  case "$CURRENT_SECTION" in
    *"$ONLY"*) selected=$((selected + 1)); return 0 ;;
  esac
  skipped=$((skipped + 1)); return 1
}

await_slot() {        # block until a worker slot frees
  while [ "$(jobs -rp | wc -l)" -ge "$JOBS" ]; do wait -n; done
}

# `$RF` is set by the helper inside its subshell. The handful of cases written inline in the parent
# set nothing and take their number here.
report() {            # report <name> <ok?> <output>
  local rf="$RF"
  # AN INLINE CASE ASKS `wanted` HERE, because it has no dispatcher to ask it in. Sixteen cases in
  # the archive, catalogue and units sections reach this function directly, on one branch of a
  # `&&`/`||` pair, so the question is asked exactly once per case just as it is above.
  #
  # WHAT THIS DOES NOT BUY, and it is a real limitation rather than an oversight: an inline case
  # skipped by `--only` has ALREADY DONE ITS WORK by the time it gets here. Its verdict is dropped,
  # not its cost. Moving the question earlier means restructuring fifteen working cases that guard
  # the archive script, which is a larger change than this flag is worth today.
  if [ -z "$rf" ]; then
    wanted "$1" || return 0
    rf="$RF_NEXT"
  fi
  if [ "$2" = "yes" ]; then
    printf 'yes\n%s\n' "$1" > "$rf"
  else
    { printf 'no\n%s\n' "$1"; printf '%s\n' "$3" | sed 's/^/           /'; } > "$rf"
  fi
}

section() { CURRENT_SECTION="$1"; next_rf; printf 'sec\n%s\n' "$1" > "$RF_NEXT"; }

RF=""

# There used to be a regen_catalogue wrapper here, called before every case. Rule 9 compared
# catalogue.md against what the generator produces, so any mutation made it stale and failed
# every unrelated case for a reason the case was not about - 14 of them did, the first time that
# rule was added without the wrapper. Rule 9 is retired and the wrapper with it: 43 seconds of
# this suite's 201 were that regeneration, measured rather than apportioned.
#
# The lesson outlives both. A rule that reads the whole store couples every case that mutates
# anything, and the question to ask when adding one is which cases are now coupled - not why the
# new rule is failing.

run_case() {          # run_case <name> <expected substring> <expected exit> <mutation fn>
  local case_name="$1" expect="$2" want_code="$3" mutate="$4"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    if diff -rq "$PRISTINE" "$work" >/dev/null 2>&1; then
      report "$case_name" no "the mutation changed nothing - this case tests nothing"
      rm -rf "$work"; exit 0
    fi
    out=$(cd "$work" && bash scripts/vault-check.sh 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" && [ "$code" = "$want_code" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code (wanted $want_code)
$out"
    fi
    rm -rf "$work"
  ) &
}

run_clean() {         # run_clean <name> <mutation fn> - the check must stay green
  local case_name="$1" mutate="$2"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    if diff -rq "$PRISTINE" "$work" >/dev/null 2>&1; then
      report "$case_name" no "the mutation changed nothing - this case tests nothing"
      rm -rf "$work"; exit 0
    fi
    out=$(cd "$work" && bash scripts/vault-check.sh 2>&1); code=$?
    if [ "$code" = "0" ] && grep -q 'VAULT-CHECK: ok' <<<"$out"; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code
$out"
    fi
    rm -rf "$work"
  ) &
}

# `the vault is renamed` ASKS ONE QUESTION AND IS GRADED ON IT (2026-08-19): does discovery find a
# vault whose directory name is nothing like ours and carries spaces. It was a `run_clean` until this
# date and it was green for the wrong reason - the sandbox renamed its copy to `vault_copy`, so the
# eleven corpus citations spelling `job_hunt_ai_vault/...` resolved against empty placeholders the
# setup had just made. With the sandbox mirroring the repository those citations are real, and
# renaming the vault breaks them: eleven `sources names a path that does not exist` lines, which is
# the check WORKING. Grading discovery on a whole-run green made this case assert a second property
# nobody chose - that the corpus does not name its own directory - and that property is false.
#
# The assertion is layout rather than a path string: a discovery that lands on the wrong directory
# reports `no vault found`, or finds one and then reports `missing directory`/`missing file` for the
# folders and registers it does not have. Neither depends on whether the corpus happens to be clean,
# which a `grep` for the renamed path would.
#
# THAT THE CORPUS HARDCODES ITS OWN DIRECTORY NAME IS A FINDING, NOT A DEFECT THIS CASE HIDES. It is
# the `raw/` shape at a smaller size and it belongs with a rewriter-and-detector pair; it is recorded
# where findings go, not silenced by a mutation that would rewrite the eleven as it renames.
run_found() {         # run_found <name> <mutation fn> - discovery must land on a real vault
  local case_name="$1" mutate="$2"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    if diff -rq "$PRISTINE" "$work" >/dev/null 2>&1; then
      report "$case_name" no "the mutation changed nothing - this case tests nothing"
      rm -rf "$work"; exit 0
    fi
    out=$(cd "$work" && bash scripts/vault-check.sh 2>&1)
    if grep -q 'no vault found' <<<"$out"; then
      report "$case_name" no "discovery found nothing
$out"
    elif grep -qE 'missing (directory|file):' <<<"$out"; then
      report "$case_name" no "discovery landed on a directory that is not the vault
$out"
    else
      report "$case_name" yes ""
    fi
    rm -rf "$work"
  ) &
}

run_case_absent() {   # <name> <must appear> <must NOT appear> <exit> <mutation fn>
  local case_name="$1" expect="$2" forbid="$3" want_code="$4" mutate="$5"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    out=$(cd "$work" && bash scripts/vault-check.sh 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" \
       && ! grep -qF "$forbid" <<<"$out" && [ "$code" = "$want_code" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code (wanted $want_code), and '$forbid' must not appear
$out"
    fi
    rm -rf "$work"
  ) &
}

# run_render asserts on the BYTES THE INJECTOR WROTE, not on what the check said, and it is the
# only helper here that does. It exists for one class of defect the other three cannot see: when
# both extractors dropped fenced blocks, a slice carrying one rendered without it AND the region
# read back without it, so the two agreed, the check said `ok`, and the text was gone. A case
# written against the check's output would have passed with the bug in place - this suite
# reproducing the failure it exists to catch.
run_render() {        # run_render <name> <mutation fn> <file> <substring that must be in it>
  local case_name="$1" mutate="$2" target="$3" expect="$4"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    out=$(cd "$work" && bash scripts/vault-inject.sh 2>&1); code=$?
    if [ "$code" = "0" ] && grep -qF "$expect" "$work/$target" 2>/dev/null; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code, and '$expect' is not in $target
$out"
    fi
    rm -rf "$work"
  ) &
}

# run_inject_case READS THE INJECTOR'S OWN EXIT AND MESSAGE, which no other helper here does.
# `run_render` runs the injector and asserts on the bytes it wrote, so it can only describe a run
# that succeeded; every other injector defect in this suite is asserted THROUGH THE GATE, because
# rule 12 answers its question by running the injector. Neither reaches a refusal. The injector
# refuses a status it does not know - and a page carrying such a status is ALSO red at the gate on
# the value itself, so a gate-side case would pass for the wrong reason and keep passing if this
# refusal were deleted ([[a-case-that-passes-before-the-change-tests-nothing]]).
run_inject_case() {   # run_inject_case <name> <expected substring> <expected exit> <mutation fn>
  local case_name="$1" expect="$2" want_code="$3" mutate="$4"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    if diff -rq "$PRISTINE" "$work" >/dev/null 2>&1; then
      report "$case_name" no "the mutation changed nothing - this case tests nothing"
      rm -rf "$work"; exit 0
    fi
    out=$(cd "$work" && bash scripts/vault-inject.sh 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" && [ "$code" = "$want_code" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code (wanted $want_code), read from the injector rather than the gate
$out"
    fi
    rm -rf "$work"
  ) &
}

run_lint_case() {     # run_lint_case <name> <expected substring> <expected exit> <mutation fn>
  local case_name="$1" expect="$2" want_code="$3" mutate="$4"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    out=$(cd "$work" && bash scripts/vault-check.sh --lint 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" && [ "$code" = "$want_code" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code (wanted $want_code), under --lint
$out"
    fi
    rm -rf "$work"
  ) &
}

# The `--lint` mirror of `run_case_absent`, added 2026-08-22 with the quote advisory. An advisory
# that names pages needs the negative direction inside its own channel: `run_case_absent` proves a
# line is silent in a BARE run, which a verdict that never fires at all also passes. What has to be
# proved here is that the advisory fires AND leaves the correct page out of its list.
run_lint_absent() {   # <name> <must appear> <must NOT appear> <exit> <mutation fn>
  local case_name="$1" expect="$2" forbid="$3" want_code="$4" mutate="$5"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    out=$(cd "$work" && bash scripts/vault-check.sh --lint 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" \
       && ! grep -qF "$forbid" <<<"$out" && [ "$code" = "$want_code" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code (wanted $want_code) under --lint, and '$forbid' must not appear
$out"
    fi
    rm -rf "$work"
  ) &
}

# A CASE ABOUT THE SCRIPT RATHER THAN ABOUT THE TREE, which is what `--rules` and the argument
# contract both are. Two things follow and neither holds anywhere else in this file.
#
# The mutation edits `scripts/vault-check.sh` IN THE SANDBOX rather than a page: the register never
# reaches the vault, so a page could not break it.
#
# And `--` in place of a mutation runs the case against the untouched copy. Every other runner here
# refuses that, and the refusal is right - a mutation that changes nothing means the case tests
# nothing. An argument contract is the exception that proves the shape of the rule: there is no
# tree state that could break `unknown argument exits 2`, so demanding a mutation would force a
# meaningless one. The exception is spelled out rather than smuggled in as a default.
run_arg_case() {      # <name> <argument> <must appear> <must NOT appear or --> <exit> <mutation fn or -->
  local case_name="$1" flag="$2" expect="$3" forbid="$4" want_code="$5" mutate="$6"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    if [ "$mutate" != "--" ]; then
      "$mutate" "$work"
      if diff -rq "$PRISTINE" "$work" >/dev/null 2>&1; then
        report "$case_name" no "the mutation changed nothing - this case tests nothing"
        rm -rf "$work"; exit 0
      fi
    fi
    out=$(cd "$work" && bash scripts/vault-check.sh "$flag" 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" && [ "$code" = "$want_code" ] \
       && { [ "$forbid" = "--" ] || ! grep -qF "$forbid" <<<"$out"; }; then
      report "$case_name" yes ""
    else
      local why="exit=$code (wanted $want_code) under $flag, expecting '$expect'"
      [ "$forbid" = "--" ] || why="$why, and '$forbid' must not appear"
      report "$case_name" no "$why
$out"
    fi
    rm -rf "$work"
  ) &
}

# run_parity asserts the ONE property that separates a flag which adds a report from a flag which
# hides a check: the exit code cannot depend on it. Each code is read off its own invocation on the
# very next statement and never through a pipe, because a status read through a pipe belongs to the
# last stage of it.
run_parity() {        # run_parity <name> <mutation fn>
  local case_name="$1" mutate="$2"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    bare_out=$(cd "$work" && bash scripts/vault-check.sh 2>&1); bare=$?
    lint_out=$(cd "$work" && bash scripts/vault-check.sh --lint 2>&1); lint=$?
    if [ "$bare" = "$lint" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "bare exit=$bare, --lint exit=$lint - the flag moved the verdict
--- bare ---
$bare_out
--- lint ---
$lint_out"
    fi
    rm -rf "$work"
  ) &
}

# An unmutated copy must be clean, or every case below proves nothing.
# Serial, and first: every case below copies `$PRISTINE`, so a broken baseline makes the whole
# suite meaningless and there is nothing to overlap it with.
#
# IT IS A PRECONDITION AND NOT A CASE, and from 2026-08-28 the tally says so. It never asks `wanted`
# - it cannot, because every case below depends on it - so under `--only` it was the one verdict a
# filter could not reach, and it was being counted as a pass: a pattern matching nothing printed
# `caught 1, missed 0` and exited 0. Its own record kind keeps it visible and out of the count.
#
# THIS MOVES EVERY PUBLISHED `caught N` IN THE CORPUS DOWN BY ONE - 133, 141, 148, 156, 194 across
# at least six pages. The readings were right when they were taken; what changed is what the number
# counts, and that is recorded rather than quietly absorbed.
out=$(cd "$PRISTINE" && bash scripts/vault-check.sh 2>&1); code=$?
next_rf
if [ "$code" -eq 0 ] && grep -q 'VAULT-CHECK: ok' <<<"$out"; then
  printf 'bas\nbaseline copy\n' > "$RF_NEXT"
else
  { printf 'brk\nbaseline copy exit=%s\n' "$code"
    printf '%s\n' "$out" | sed 's/^/           /'; } > "$RF_NEXT"
fi

# The subject is picked by what the cases NEED, not by sort order. Three cases assert that
# nothing happens - two `run_clean`s and the `run_case_absent` - and a mutation whose `sed`
# silently matches nothing turns those into "clean, therefore passing" while testing nothing
# at all. That is the suite reproducing, in itself, the failure it exists to catch, and it was
# demonstrated: reshape the first concept page and three cases go quiet while staying green.
SUBJECT=$(grep -l '^authority:' "$PRISTINE/$VAULT_DIR"/wiki/concepts/*.md 2>/dev/null \
          | xargs grep -l '^sources: \[' 2>/dev/null \
          | xargs grep -l '^status: current' 2>/dev/null \
          | xargs grep -l '^tags: \[' 2>/dev/null | sort | head -1 | sed "s|$PRISTINE/||")
[ -n "$SUBJECT" ] || { echo "SELFTEST: no concept page has authority + inline sources + inline tags;"
                       echo "          the cases below would pass by testing nothing. Fix the suite."
                       exit 1; }
OTHER=$(find "$PRISTINE/$VAULT_DIR/wiki/concepts" -name '*.md' | sort | sed -n 2p | sed "s|$PRISTINE/||")
DECISION=$(find "$PRISTINE/$VAULT_DIR/wiki/decisions" -name '*.md' | sort | head -1 | sed "s|$PRISTINE/||")
SUBJECT_NAME=$(basename "$SUBJECT" .md)

drop_field()      { sed -i '/^tags:/d' "$1/$SUBJECT"; }
wrong_type()      { sed -i 's/^type: concept/type: decision/' "$1/$SUBJECT"; }
drop_decided()    { sed -i '/^decided:/d' "$1/$DECISION"; }
bogus_source()    { sed -i 's|^sources: \[|sources: ["docs/no-such-file.md", |' "$1/$SUBJECT"; }
url_source()      { sed -i 's|^sources: \[|sources: ["https://example.com/an-article", |' "$1/$SUBJECT"; }
                    # line 2 is inside the frontmatter, which is the only place a claim
                    # counts; appended at the end of the file it is prose, and prose is not
                    # a claim - that is the point of the rule this case exercises
need_authority()  { local a; a=$(grep -m1 '^authority:' "$1/$SUBJECT")
                    [ -n "$a" ] || { echo "SELFTEST BUG: $SUBJECT has no authority: line"; exit 1; }
                    printf '%s' "$a"; }
dup_authority()   { local a; a=$(need_authority "$1"); sed -i "2i $a" "$1/$OTHER"; }
fenced_authority(){ local a; a=$(need_authority "$1")
                    { echo; echo '```yaml'; printf '%s\n' "$a"; echo '```'; } >> "$1/$OTHER"; }
fenced_frontmatter() { cat > "$1/$VAULT_DIR/wiki/concepts/all-in-a-fence.md" <<'PAGE'
# A page whose frontmatter is only an example

```yaml
title: "Not real frontmatter"
type: concept
status: current
created: 2026-08-13
sources: ["CLAUDE.md"]
tags: [vault, retrieval]
```

Linked from nowhere on purpose - the frontmatter rules are what is under test.
PAGE
                  }
broken_link()     { printf '\nSee [[a-page-that-was-never-written]].\n' >> "$1/$SUBJECT"; }
empty_target()    { printf '\nSee [[hollow-page]].\n' >> "$1/$SUBJECT"
                    : > "$1/$VAULT_DIR/wiki/concepts/hollow-page.md"; }
aliased_links()   { grep -rl "\[\[${SUBJECT_NAME}\]\]" "$1/$VAULT_DIR" --include='*.md' \
                      | while IFS= read -r f; do
                          sed -i "s/\[\[${SUBJECT_NAME}\]\]/[[${SUBJECT_NAME}|the page]]/g" "$f"
                        done; }
heading_links()   { grep -rl "\[\[${SUBJECT_NAME}\]\]" "$1/$VAULT_DIR" --include='*.md' \
                      | while IFS= read -r f; do
                          sed -i "s/\[\[${SUBJECT_NAME}\]\]/[[${SUBJECT_NAME}#the-rule]]/g" "$f"
                        done; }
link_in_a_fence() { grep -rl "\[\[${SUBJECT_NAME}\]\]" "$1/$VAULT_DIR" --include='*.md' \
                      | while IFS= read -r f; do
                          sed -i "s/\[\[${SUBJECT_NAME}\]\]/\`[[${SUBJECT_NAME}]]\`/g" "$f"
                        done; }
                    # Clear the link from the WHOLE copy and plant it afterwards, rather than
                    # from a list of the registers the check reads. The list is what went wrong:
                    # this mutation cleared wiki/ and index.md, the check also reads archive/,
                    # tags.md and sprint.md, and when tags.md gained a link to the subject the
                    # page stayed reachable, the orphan never fired, and two cases here reported
                    # MISSED for a reason that had nothing to do with the rule under test. A
                    # copy of a list drifts from the list; a sweep of everything cannot.
clear_links()     { grep -rl "\[\[${SUBJECT_NAME}\]\]" "$1/$VAULT_DIR" --include='*.md' 2>/dev/null \
                      | while IFS= read -r f; do
                          sed -i "s/\[\[${SUBJECT_NAME}\]\]/the page/g" "$f"
                        done; }
# THE SUITE PLANTS ITS OWN FILE AND NEVER BORROWS ONE FROM THE CORPUS (2026-08-20, owner's ruling:
# a suite is a test environment, so it works in its own sandbox and does not reach into the working
# wiki for a file). These two used to append into
# `$(find "$1/$VAULT_DIR/raw/handoffs" -name '2026-*.md' | sort | head -1)` - whichever real journal
# sorted first. That holds only while raw/ is non-empty, and the migration's whole point is that
# raw/ is an inbox that EMPTIES between sessions.
#
# MEASURED against an empty raw/handoffs rather than argued: the substitution becomes the empty
# string, the redirect prints `: No such file or directory` AND EXITS 0, so the tree is left
# unmutated. The `diff -rq` guard in the helpers then catches it and both cases report MISSED with
# *the mutation changed nothing - this case tests nothing*. So this does not fail silently - it
# fails LOUDLY WITH THE WRONG DIAGNOSIS, which is worse in one specific way: the reader is told the
# case is empty, and nothing points at raw/ having emptied.
#
# It is also the defect this suite has already been bitten by from the other side - a fixture that
# depends on the corpus stops being a fixture OF the corpus, and that run reported caught 24,
# missed 96.
#
# raw/notes/ RATHER THAN raw/handoffs/, and that is not arbitrary: a journal owes rule 8 every
# section of the template, so a planted journal would go red for its own reasons and the case would
# be testing the fixture. A note is a file inside raw/ and nothing more, which is exactly the one
# property both of these cases are about.
raw_fixture()     { local f="$1/$VAULT_DIR/raw/notes/selftest-link-fixture.md"
                    printf 'A note the selftest planted, to be a file inside raw/ and nothing more.\n' \
                      > "$f"
                    printf '%s' "$f"; }
link_only_in_raw(){ clear_links "$1"
                    printf '\nWe discussed [[%s]] at length.\n' "$SUBJECT_NAME" \
                      >> "$(raw_fixture "$1")"; }
broken_link_in_raw(){ printf '\nWe discussed [[a-page-we-decided-not-to-write]] at length.\n' \
                      >> "$(raw_fixture "$1")"; }
# A PLANTED PAGE OWES A REGISTER ENTRY, and that is the admission rule reaching into this suite
# rather than an inconvenience. Rule 13 requires every slug in the tree to sit in a family in
# `authority.md`: an ungrouped slug is a page the lookup cannot reach, so the next unit about the
# same question writes a second page and neither is wrong. A fixture that plants a page and not its
# slug is testing a corpus this project would refuse - so the fixtures plant both.
#
# Plain text, never `[[wikilinks]]`. A register that linked its pages would have to join rule 5's
# link sweep, and then nothing in the vault could be an orphan again.
plant_slug() {        # plant_slug <work> <slug>...
  local work="$1"; shift
  { printf -- '
- group: pages this selftest plants
'
    printf -- '  definition: slugs minted by a fixture, so the register agrees with the tree inside a case
'
    printf -- '  slugs: [%s]
' "$(printf '%s, ' "$@" | sed 's/, $//')"
    printf -- '  aliases: [selftest, probe]
'
  } >> "$work/$VAULT_DIR/authority.md"
}

orphan_page()     { cat > "$1/$VAULT_DIR/wiki/concepts/nobody-links-to-me.md" <<'PAGE'
---
title: "Nobody links to me"
type: concept
status: current
authority: orphan-probe
sprint: S2
basis: inference
created: 2026-08-13
sources: ["CLAUDE.md"]
tags: [vault, retrieval]
---
A page no page names.
PAGE
                    plant_slug "$1" orphan-probe; }
unknown_tag()     { sed -i 's/^tags: \[/tags: [not-a-registered-tag, /' "$1/$SUBJECT"; }
block_list_tags() { sed -i 's/^tags: .*/tags:\n  - vault\n  - retrieval\n  - not-a-registered-tag/' "$1/$SUBJECT"; }
empty_tag_list()  { sed -i 's/^tags: .*/tags: []/' "$1/$SUBJECT"; }
one_tag()         { sed -i 's/^tags: .*/tags: [vault]/' "$1/$SUBJECT"; }
six_tags()        { sed -i 's/^tags: .*/tags: [vault, retrieval, process, testing, web, data]/' "$1/$SUBJECT"; }
bad_status()      { sed -i 's/^status: current/status: draft/' "$1/$SUBJECT"; }

                    # Each of these isolates ONE exemption of rule 10.
                    #
                    # strip_quantity is a NO-OP over today's corpus and is kept on purpose.
                    # The field was withdrawn on 2026-08-18 and no page carries it, but the
                    # two cases below WRITE one in order to prove the withdrawal: without the
                    # strip they would append a second quantity: line to a subject that
                    # already had one, and a fixture malformed in a way no case is about is
                    # how a suite starts passing for the wrong reason.
                    #
                    # It also survives a revert. If the field ever came back to the corpus a
                    # catching case would silently become a case about answering - the exact
                    # failure this suite exists to prevent - and the guard costs nothing.
strip_quantity()  { sed -i '/^quantity:/d' "$1/$SUBJECT"; }
set_title()       { sed -i "s|^title: .*|title: \"$2\"|" "$1/$SUBJECT"; }
title_counts()    { strip_quantity "$1"; set_title "$1" 'Seven checks hold the layering'; }
title_declared()  { title_counts "$1"
                    sed -i '/^tags:/a quantity: the checks counted are named in the page itself' "$1/$SUBJECT"; }
title_code_span() { strip_quantity "$1"; set_title "$1" 'The page loads `htmx 2` and nothing else of ours'; }
title_iso_date()  { strip_quantity "$1"; set_title "$1" 'What predates 2026-08-05 is deferred rather than exempt'; }
title_word_one()  { strip_quantity "$1"; set_title "$1" 'An absent value never overwrites a known one'; }
title_glued()     { strip_quantity "$1"; set_title "$1" 'The host console is cp1252 and must be told otherwise'; }
                    # The ordinals joined the word list on 2026-08-19 (owner). `first` did
                    # not, and is the mirror of the measured exemption for `one`: both were
                    # counted over the corpus and neither was ever a count that could drift.
title_ordinal()   { strip_quantity "$1"; set_title "$1" 'The fifth verdict joins the layering'; }
title_word_first(){ strip_quantity "$1"; set_title "$1" 'The folder is the first narrowing and nothing precedes it'; }
                    # The filename half of rule 10, which is an ADVISORY - so run_clean cannot
                    # test a single one of its exemptions. run_clean asks for exit 0 and an `ok`
                    # line, and an advisory leaves both exactly as they were: a broken exemption
                    # would print its slug and still pass. Every non-firing case below is
                    # run_case_absent, asserting the slug does not appear in output that is
                    # otherwise green.
                    #
                    # The fixture is a NEW page and never a rename of the subject. Renaming a
                    # page the corpus cites strands its inbound wikilinks, the case goes red
                    # through rules 4 and 5, and it would prove nothing about rule 10 - which is
                    # also the reason the six standing offenders are still standing.
                    #
                    # And its title does not count. The six are exactly that shape - a title
                    # repaired in place, a slug left behind it - and a fixture whose title also
                    # counted would go red under the title half, which is the older code, and be
                    # read as this half working.
filename_page()   { cat > "$1/$VAULT_DIR/wiki/concepts/$2.md" <<'PAGE'
---
title: "The panel shows local time and the column does not"
type: concept
status: current
authority: filename-probe
sprint: S2
basis: human
created: 2026-08-18
sources: ["CLAUDE.md"]
tags: [vault, retrieval]
---
A page whose title was repaired and whose filename was not.
PAGE
                    plant_slug "$1" filename-probe
                    printf '\n- [[%s]]\n' "$2" >> "$1/$VAULT_DIR/index.md"; }
filename_counts()   { filename_page "$1" two-clocks-on-a-selftest-page; }
filename_declared() { filename_counts "$1"
                      sed -i '/^tags:/a quantity: not a count - the page is about these two clocks and a third cannot appear' \
                        "$1/$VAULT_DIR/wiki/concepts/two-clocks-on-a-selftest-page.md"; }
filename_iso_date() { filename_page "$1" what-predates-2026-08-05-is-deferred-in-the-selftest; }
filename_glued()    { filename_page "$1" the-selftest-console-is-cp1252-and-must-be-told; }
filename_word_one() { filename_page "$1" an-absent-value-never-overwrites-a-known-one-in-the-selftest; }
filename_ordinal()  { filename_page "$1" the-fifth-verdict-on-a-selftest-page; }
deprecated_here() { sed -i 's/^status: current/status: deprecated/' "$1/$SUBJECT"; }
#    THE TWO MARKS ADDED 2026-08-28, AND THEY ARE HERE TOGETHER BECAUSE THEIR DIFFERENCE IS THE
#    THING UNDER TEST. Both were minted on the same day and only one obliges a page to leave.
#    `archived` is written BY THE SWEEP as it moves a page, so finding one in `wiki/` means the move
#    did not finish - and the sweep is allowed to leave one behind, because it continues past a
#    refused move and reports the refusals at the end (owner, 2026-08-28). `processed` OPENS a
#    state: the librarian sets it, the page stays, and the sweep moves it as a separate step, so a
#    processed page in `wiki/` is legitimate and the gate must say nothing about it.
#
#    A CASE FOR THE SILENCE IS WHY THE THIRD PLANTER EXISTS. Without it, a gate that reddened every
#    new status equally would pass the two red cases and be wrong in the direction that locks the
#    librarian out of the folder it is supposed to be draining.
archived_here()   { sed -i 's/^status: current/status: archived/' "$1/$SUBJECT"; }
processed_astray() { sed -i 's/^status: current/status: processed/' "$1/$SUBJECT"; }
#    The subject is a `concepts/` page, so `processed` there is refused by the generic `badvalue`
#    route and names the schema that refused it - the same shape `implemented` has outside
#    `wiki/proposals/`. The legal home is `wiki/decisions/` and the planter below is the other half.
#
#    IT IS LINKED FROM `index.md` AND REGISTERED IN `authority.md`, for the reasons the idea-pair
#    planter gives at length: a planted page nothing names is an orphan, and a slug in the tree that
#    is not in the register is red in both directions. A case that goes red for either would be
#    green about nothing.
plant_processed_decision() {   # plant_processed_decision <work>
  cat > "$1/$VAULT_DIR/wiki/decisions/a-decision-whose-content-moved-on.md" <<'PAGE'
---
title: "A decision whose content was carried forward into the page it produced"
type: decision
status: processed
authority: selftest-processed-decision
basis: human
sprint: S3
decided: 2026-08-28
created: 2026-08-28
sources: ["scripts/vault-check.sh"]
binding: deferral
tags: [vault, harness]
---

# A decision whose content was carried forward

Planted by the selftest. It carries `status: processed` and sits in `wiki/` on purpose: the mark
opens a state and does not name a place, so the gate must judge it not at all.
PAGE
  printf '
- [[a-decision-whose-content-moved-on]]
' >> "$1/$VAULT_DIR/index.md"
  printf '
- group: the processed decision this suite plants
  definition: the fixture proving a processed page is legitimate where it stands. Answers nothing
    about the product; it exists so the planted page can be looked up like any other.
  slugs: [selftest-processed-decision]
  aliases: [selftest fixture]
' >> "$1/$VAULT_DIR/authority.md"
}

# THE DECISION LIFECYCLE, RULES 16 AND 17. Every page these plant is otherwise valid - registered
# authority, two live tags, a real `sources:` path, and a link from `index.md` so the orphan rule
# leaves it alone - because a fixture malformed in a way the case is not about is how a suite
# starts passing for the wrong reason. That failure is recorded twice in this file already.
#
# THE DATES ARE LITERALS AND NOT `date +%F`, deliberately. `lifecycle_from:` is 2026-08-30, so a
# fixture dated from the clock would silently stop testing the older cohort the moment the schema's
# date moved past it - and a case that no longer tests what it was written for looks exactly like
# one that passes.
lc_register() {       # lc_register <work> <slug> <authority>
  printf '
- [[%s]]
' "$2" >> "$1/$VAULT_DIR/index.md"
  printf '
- group: the decision-lifecycle fixture
  definition: pages this selftest plants to exercise rules 16 and 17. Answers nothing about the
    product; it exists so a planted page can be looked up like any other.
  slugs: [%s]
  aliases: [selftest, lifecycle probe]
' "$3" >> "$1/$VAULT_DIR/authority.md"
}

# A page created BEFORE the schema's date, carrying none of what rule 16 asks for. It must stay
# green: this is the 299-page cohort the owner ruled is not back-filled, and a rule that reddened
# it would lock out the librarian on the day it landed.
lc_older_bare()   { cat > "$1/$VAULT_DIR/wiki/decisions/an-older-decision-the-cut-leaves-alone.md" <<'PAGE'
---
title: "An older decision the dated cut leaves alone"
type: decision
status: current
authority: selftest-lifecycle-older
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["scripts/vault-check.sh"]
binding: deferral
tags: [vault, harness]
---

Planted by the selftest, dated the day before `lifecycle_from:`. It carries no sections and neither
lifecycle field, and rule 16 must not judge it.
PAGE
                    lc_register "$1" an-older-decision-the-cut-leaves-alone selftest-lifecycle-older; }

# Dated ON the cut and carrying both fields, but no `# ` headings at all.
lc_dated_no_sections() { cat > "$1/$VAULT_DIR/wiki/decisions/a-dated-decision-with-no-sections.md" <<'PAGE'
---
title: "A dated decision that dropped its sections"
type: decision
status: current
authority: selftest-lifecycle-nosections
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target:
sources: ["scripts/vault-check.sh"]
binding: deferral
tags: [vault, harness]
---

Planted by the selftest. Prose and no headings, so every declared section is missing at once.
PAGE
                    lc_register "$1" a-dated-decision-with-no-sections selftest-lifecycle-nosections; }

# THE CONDITIONAL SIXTH SECTION, and the pair is written as one helper taking the target kind so
# the two cases differ in exactly the field under test and in nothing else. Both carry all five
# unconditional sections, so the only thing that can fire is the conditional one. The target named
# does not exist, which rule 17 reads as an open decision rather than as a broken handshake.
plant_dated_decision_targeting() {   # plant_dated_decision_targeting <work> <kind> <slug>
  cat > "$1/$VAULT_DIR/wiki/decisions/$3.md" <<PAGE
---
title: "A dated decision that declares a target"
type: decision
status: current
authority: selftest-lifecycle-$2-target
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: $2
target: a-page-nobody-has-written-yet
sources: ["scripts/vault-check.sh"]
binding: prohibition
tags: [vault, harness]
---

# Context

Planted by the selftest. Every unconditional section is here, so the conditional one is the only
thing that can be missing.

# The question

Whether the sixth section is owed by this page.

# How it works after

The verdict fires for one value of \`target_kind:\` and stays silent for the others.

# Recommendation

None: this page is a fixture.

# Ratification

None: this page is a fixture.
PAGE
  lc_register "$1" "$3" "selftest-lifecycle-$2-target"
}
lc_rule_target_no_clause()   { plant_dated_decision_targeting "$1" rule \
                                 a-dated-decision-targeting-a-rule; }
lc_action_target_no_clause() { plant_dated_decision_targeting "$1" action \
                                 a-dated-decision-targeting-an-action; }

# Dated on the cut, all five sections present, and neither lifecycle field.
lc_dated_no_fields() { cat > "$1/$VAULT_DIR/wiki/decisions/a-dated-decision-with-no-target.md" <<'PAGE'
---
title: "A dated decision that named no target"
type: decision
status: current
authority: selftest-lifecycle-nofields
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
sources: ["scripts/vault-check.sh"]
binding: deferral
tags: [vault, harness]
---

# Context

Planted by the selftest.

# The question

Whether rule 16 asks for the fields the schema names in `required_from:`.

# How it works after

The gate reddens this page until it declares a target.

# Recommendation

None; this is a fixture.

# Ratification

None; this is a fixture.
PAGE
                    lc_register "$1" a-dated-decision-with-no-target selftest-lifecycle-nofields; }

# The half-finished landing rule 17 is for: the target EXISTS and does not name this decision back.
# It points at a rule page the repository really has, whose `decided_by:` names its own cause.
lc_handshake_half() { cat > "$1/$VAULT_DIR/wiki/decisions/a-decision-whose-target-ignores-it.md" <<'PAGE'
---
title: "A decision whose target does not name it back"
type: decision
status: current
authority: selftest-lifecycle-halfshake
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: rule
target: write-plainly-name-the-source-and-say-what-is-not-done
sources: ["scripts/vault-check.sh"]
binding: deferral
tags: [vault, harness]
---

# Context

Planted by the selftest.

# The question

Whether rule 17 sees a landing that is half done.

# How it works after

The gate reddens this page while the target does not name it in `decided_by:`.

# Recommendation

None; this is a fixture.

# Ratification

None; this is a fixture.
PAGE
                    lc_register "$1" a-decision-whose-target-ignores-it selftest-lifecycle-halfshake; }

# THE STATE THAT MUST STAY GREEN, and it is the whole shape of rule 17. The target does not exist,
# which is what "this decision is still open" means. A verdict that reddened here would fire on
# every decision the moment it was taken, and would be cleared only by doing the work - which is
# an alarm that is on by default.
lc_handshake_open() { cat > "$1/$VAULT_DIR/wiki/decisions/a-decision-whose-target-is-unwritten.md" <<'PAGE'
---
title: "A decision whose target has not been written yet"
type: decision
status: current
authority: selftest-lifecycle-openshake
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: rule
target: a-rule-page-nobody-has-written-yet
sources: ["scripts/vault-check.sh"]
binding: deferral
tags: [vault, harness]
---

# Context

Planted by the selftest.

# The question

Whether an unwritten target reads as open rather than as broken.

# How it works after

The gate stays green and the decision stays in this folder.

# Recommendation

None; this is a fixture.

# Ratification

None; this is a fixture.

# The rule text

Carried because this fixture declares `target_kind: rule`, and from 2026-08-30 such a decision owes
the section the rule page is assembled from. Without it this page goes red on that verdict and the
case stops testing the handshake it was written for.
PAGE
                    lc_register "$1" a-decision-whose-target-is-unwritten selftest-lifecycle-openshake; }

# THE TRAP RULE 16 CHECKS FOR ITSELF: a key obliged by `required_from:` and allowed by neither
# `required:` nor `optional:`. Every page in the folder would then be unwritable - carry the key and
# the `unknownkey` verdict reddens it, omit it and rule 16 does.
#
# IT INSERTS UNDER THE HEADING RATHER THAN APPENDING TO THE FILE, and that is the repair of
# 2026-08-30 rather than the original spelling. The fixture used to append one line to the end of
# the schema and rely on `required_from:` being the last block in it. A `sections_when_target_kind_rule:`
# block was added below it that day, the appended line landed in THAT list, and the case went quiet
# without anybody touching it - a fixture that depends on what happens to be last is a fixture that
# expires the next time somebody adds a block.
lc_key_not_allowed() { sed -i '/^required_from:/a\  - not-a-declared-key' \
                         "$1/$VAULT_DIR/wiki/decisions/_schema.yaml"; }

# A CANCELLED RULE THAT HAS NOT LEFT `wiki/`. `repealed` joined the `retired` verdict on 2026-08-30
# and without this case the value would have been an invitation to sit still: nothing else in the
# gate names it, so such a page could have stayed here for good with every check green - which is
# the exact shape of the window this store already has open between a repeal being decided and the
# supersession being performed.
#
# THE SUBJECT IS A `rules/` PAGE BECAUSE THE VALUE IS LEGAL THERE ALONE. Anywhere else the generic
# `badvalue` verdict fires first and the case would pass for the wrong reason.
lc_repealed_astray() { sed -i 's/^status: current/status: repealed/' \
                         "$1/$VAULT_DIR/wiki/rules/write-plainly-name-the-source-and-say-what-is-not-done.md"; }

# A `sections:` header that parses to nothing, which must be red for the reason `required:` and
# `values:` are: an empty set passes everything, silently, in the direction that hides a defect.
lc_sections_empty() { awk '
    /^sections:/ { print; skip = 1; next }
    skip && /^[ \t]*-/ { next }
    { skip = 0; print }' "$1/$VAULT_DIR/wiki/proposals/_schema.yaml" > "$1/lcs.tmp" \
                      && mv "$1/lcs.tmp" "$1/$VAULT_DIR/wiki/proposals/_schema.yaml"; }

dead_tag()        { printf '\n- tag: never-used\n  definition: minted and forgotten\n  aliases: []\n  since: 2026-08-13\n' \
                      >> "$1/$VAULT_DIR/tags.md"; }
claude_md_link()  { printf '\nWhy this rule exists: [[a-page-claude-md-invented]].\n' >> "$1/CLAUDE.md"; }
fenced_link_reg() { clear_links "$1"
                    { echo; echo '```markdown'; echo "See [[${SUBJECT_NAME}]] for the shape."
                      echo '```'; } >> "$1/$VAULT_DIR/index.md"; }
fenced_example_reg() { { echo; echo '```markdown'; echo 'See [[an-example-page-name]] for the shape.'
                         echo '```'; } >> "$1/$VAULT_DIR/index.md"; }
block_list_sources() { sed -i 's|^sources: .*|sources:\n  - "docs/no-such-file-at-all.md"|' "$1/$SUBJECT"; }
wrapped_sources() { sed -i 's|^sources: \[|sources: ["docs/HANDOFF.md",\n           "docs/no-such-file-wrapped.md"]\nx-scratch: |' "$1/$SUBJECT"; }
scalar_sources()  { sed -i 's|^sources: .*|sources: docs/no-such-file-scalar.md|' "$1/$SUBJECT"; }
bare_list_sources() { sed -i 's|^sources: .*|sources:\n  - docs/no-such-file-bare.md|' "$1/$SUBJECT"; }
unterminated_fm() { awk 'NR == 1 { print; next } /^---$/ && !done { done = 1; next } { print }' \
                      "$1/$SUBJECT" > "$1/$SUBJECT.tmp" && mv "$1/$SUBJECT.tmp" "$1/$SUBJECT"; }
quoted_tags()     { sed -i 's/^tags: .*/tags: ["vault", "retrieval"]/' "$1/$SUBJECT"; }
quoted_block()    { sed -i 's/^tags: .*/tags:\n  - "vault"\n  - "retrieval"/' "$1/$SUBJECT"; }
two_tag_lines()   { sed -i 's/^tags: .*/tags: [vault, retrieval]\ntags: [process, testing]/' "$1/$SUBJECT"; }
deprecated_dup()  { local a; a=$(need_authority "$1")
                    sed -i 's/^status: current/status: deprecated/' "$1/$OTHER"
                    sed -i "2i $a" "$1/$OTHER"; }
crlf_vault()      { find "$1/$VAULT_DIR" -name '*.md' -print0 \
                      | xargs -0 sed -i 's/$/\r/'; }
bom_page()        { printf '\357\273\277' > "$1/$SUBJECT.tmp"
                    cat "$1/$SUBJECT" >> "$1/$SUBJECT.tmp"
                    mv "$1/$SUBJECT.tmp" "$1/$SUBJECT"; }
                    # Rule 8 reads the section set from the template and judges a journal only
                    # while it is uncompiled. Four properties are held down here: a dropped
                    # section is caught, a RENAMED one is caught as a drop plus an addition
                    # (the loudest a cut by text can be), a journal already compiled is left
                    # alone whatever form it is in - which is the only reason the template could
                    # change at all while journals in the older numbered form sit in raw/ - and
                    # the check refuses to run rather than pass everything when the template is
                    # gone. The probe journal is BUILT FROM THE TEMPLATE for the same reason the
                    # rule reads it: a fixture carrying its own copy of the section list would go
                    # on passing after the template changed.
new_journal()     { local d="$1/$VAULT_DIR/raw/handoffs/2026-08-18-probe.md"
                    { printf -- '---\nsession: 2026-08-18\nsprint: S1\ncommits: none\n---\n\n'
                      awk 'FNR == 1 { b = 0 } /^```/ { b = !b; next } !b && /^## /' \
                        "$1/.claude/templates/handoff.md" \
                      | while IFS= read -r h; do printf '%s\nnone\n\n' "$h"; done
                    } > "$d"
                    printf '%s' "$d"; }
uncompiled_short()   { local d; d=$(new_journal "$1"); sed -i '/^## Lessons$/,+1d' "$d"; }
uncompiled_renamed() { local d; d=$(new_journal "$1"); sed -i 's/^## Lessons$/## Learnings/' "$d"; }
compiled_old_form()  { local b="$1/$VAULT_DIR/raw/handoffs/2026-08-18-old"
                       printf -- '---\nsession: 2026-08-18\nsprint: S1\ncommits: none\n---\n\n## 1. State\nnone\n' > "$b.md"
                       printf -- '1\tjournal\n' > "$b.coverage.tsv"; }
no_handoff_template() { rm -f "$1/.claude/templates/handoff.md"; }
missing_dir()     { rm -rf "$1/$VAULT_DIR/archive"; }
missing_file()    { rm -f "$1/$VAULT_DIR/tags.md"; }
renamed_vault()   { mv "$1/$VAULT_DIR" "$1/a vault with spaces"; }
renamed_and_one_tag() { sed -i 's/^tags: .*/tags: [vault]/' "$1/$SUBJECT"
                        mv "$1/$VAULT_DIR" "$1/a vault with spaces"; }
                    # The layout is MIRRORED off the pristine copy, never written down a second
                    # time. It used to be a list here, and that list drifted the moment
                    # `wiki/rules/` was added on 2026-08-17: this case went red naming a missing
                    # directory, which is not what "a vault with no pages yet" is about. A test
                    # that needs a set the subject also knows must derive it or sweep it.
                    # And the harness loses its regions, for the same reason and by the same move.
                    # A vault with no pages is a tree before any migration, so no governed file can
                    # be carrying a rule. Once a real rule governed `CLAUDE.md` the sandbox began
                    # materialising it WITH its region, and this case went red naming a region whose
                    # page it had just deleted - the check being right and the case being about
                    # something else. Swept out of the governed files, never listed.
empty_vault()     { rm -rf "$1/$VAULT_DIR"
                    (cd "$PRISTINE/$VAULT_DIR" && find . -type d) \
                      | while IFS= read -r d; do mkdir -p "$1/$VAULT_DIR/$d"; done
                    # AND THE SCHEMAS COME WITH THE LAYOUT, which is the third instance of
                    # the reason above. `wiki/<folder>/_schema.yaml` is what the check reads
                    # a folder's key set from, and a folder without one is red by design: a
                    # vault with no pages is still a vault whose folders declare what a page
                    # must carry. Copied off the pristine tree, never written out here - a
                    # second copy of that key list is the exact failure this file records twice.
                    (cd "$PRISTINE/$VAULT_DIR" && find . -name '_schema.yaml') \
                      | while IFS= read -r s; do cp "$PRISTINE/$VAULT_DIR/$s" "$1/$VAULT_DIR/$s"; done
                    # AND THE REGISTERS ARE SWEPT, NOT LISTED - the fourth instance of the reason
                    # above, and the first one this file did not already record. It read
                    # `for f in CLAUDE.md index.md tags.md log.md` until 2026-08-21, and the day
                    # `authority.md` joined rule 1's existence check the case went red naming a
                    # missing register, which is not what "a vault with no pages yet" is about.
                    # The same drift, in the same file, for the third time. A vault's registers are
                    # its top-level markdown; sweeping them off the pristine tree costs nothing and
                    # cannot go stale.
                    (cd "$PRISTINE/$VAULT_DIR" && find . -maxdepth 1 -name '*.md') \
                      | sed 's|^\./||' \
                      | while IFS= read -r f; do printf '# %s\n' "$f" > "$1/$VAULT_DIR/$f"; done
                    while IFS= read -r g; do
                      [ -f "$g" ] || continue
                      # ANY TYPE WORD, not the literal `rule` (2026-08-18). A marker carries its
                      # record's type since `e83ce28`, and `013a6d0` put a `<!-- concept: … -->`
                      # region into `CLAUDE.md`. Matching only `rule:` left that region standing
                      # while its page was deleted with the rest - a region with no page behind
                      # it, red, for a reason this case is not about. The sweep follows the
                      # marker form rather than a word, so the next type costs nothing here.
                      awk '
                        /^<!--[ \t]+[a-z]+:[ \t]/      { skip = 1 }
                        !skip                          { print }
                        /^<!--[ \t]+\/[a-z]+:[ \t]/    { skip = 0 }
                      ' "$g" > "$g.stripped" && mv "$g.stripped" "$g"
                    done < <(find "$1/.claude" -name '*.md' 2>/dev/null; echo "$1/CLAUDE.md"); }

section "--- the check ---"

# The fifth category, added 2026-08-15. A page in proposals/ is linked from index.md in these
# fixtures on purpose: every new page is an orphan until something names it, and an orphan report
# firing here would hide whether the case under test caught anything.
proposal_page() {
  mkdir -p "$1/$VAULT_DIR/wiki/proposals"
  cat > "$1/$VAULT_DIR/wiki/proposals/a-thing-we-might-build.md" <<'PAGE'
---
title: "A thing we might build"
type: proposal
status: current
authority: might-build-probe
sprint: S2
basis: human
created: 2026-08-15
sources: ["CLAUDE.md"]
tags: [vault, process]
---
Raised, designed, not built. What it would take is written here and nowhere else.
PAGE
  plant_slug "$1" might-build-probe
  printf '
- [[a-thing-we-might-build]]
' >> "$1/$VAULT_DIR/index.md"
}

proposal_mistyped() {
  proposal_page "$1"
  sed -i 's/^type: proposal$/type: decision/' "$1/$VAULT_DIR/wiki/proposals/a-thing-we-might-build.md"
}

proposals_gone() { rm -rf "$1/$VAULT_DIR/wiki/proposals"; }

# Eleven pages in one folder sharing one tag - one more than the ten a reader opens for a
# question, which is the number the advisory is measured against. The tag is registered first:
# an unregistered tag is a failure, and this case has to reach exit 0 to prove the density
# advisory prints without failing the run.
dense_tag() {
  printf '
- tag: dense-test
  definition: minted for the density case
  aliases: []
  since: 2026-08-16
'     >> "$1/$VAULT_DIR/tags.md"
  local i
  for i in 1 2 3 4 5 6 7 8 9 10 11; do
    cat > "$1/$VAULT_DIR/wiki/concepts/a-dense-page-$i.md" <<PAGE
---
title: "A dense page minted for the density case"
type: concept
status: current
authority: dense-probe-$i
sprint: S2
basis: human
created: 2026-08-16
sources: ["CLAUDE.md"]
tags: [dense-test, vault]
---
One of eleven pages sharing a tag inside a single folder.
PAGE
    printf '
- [[a-dense-page-%s]]
' "$i" >> "$1/$VAULT_DIR/index.md"
  done
  plant_slug "$1" dense-probe-1 dense-probe-2 dense-probe-3 dense-probe-4 dense-probe-5                   dense-probe-6 dense-probe-7 dense-probe-8 dense-probe-9 dense-probe-10                   dense-probe-11
}

# --- rule 11: marked regions, and the rules behind them --------------------------------------
#
# The subject is the handoff template, picked by what these cases NEED rather than by what
# happens to be in the sandbox: it is markdown, it is under `.claude/`, and rule 8 already
# copies it in, so it is the one harness file guaranteed to be there. A mutation aimed at a
# file that is not present would append to nothing and every case here would pass by testing
# nothing at all - which is the failure this suite exists to catch.
PROBE=".claude/templates/handoff.md"
[ -f "$PRISTINE/$PROBE" ] || { echo "SELFTEST: $PROBE is not in the sandbox; the region cases"
                               echo "          below would mutate a file nobody reads. Fix the suite."
                               exit 1; }

# What a rule ships. Two plain lines on purpose: a `## ` heading here would change the section set
# rule 8 reads out of this same template and fail every journal case for a reason none of them is
# about, which is the coupling a whole-store rule creates and the reason to look for it first.
SLICE_TEXT='The test database comes from TEST_DATABASE_URL and is created by the fixture.
Never run the suite against the production database.'

# A rule page for a region to point at. Linked from index.md, or the orphan rule fails the case
# for a reason the case is not about. It carries a `<!-- text -->` slice because a current rule
# without one is a rule that ships nothing, and rule 12 says so - so a page without a slice is a
# case of its own rather than the background every other case runs against.
plant_rule_page() {   # plant_rule_page <work> <slug> <destination>
  mkdir -p "$1/$VAULT_DIR/wiki/rules"
  cat > "$1/$VAULT_DIR/wiki/rules/$2.md" <<PAGE
---
title: "A rule minted for the region cases"
type: rule
status: current
governs: $3
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["scripts/vault-inject.sh"]
decided_by: [[a-refused-proposal-is-archived-and-takes-status-refused]]
tags: [harness, vault]
---

# A rule minted for the region cases

<!-- text -->
$SLICE_TEXT
<!-- /text -->

This paragraph is the justification. It is here to prove it does NOT travel: a rendered region
carrying this sentence means the injector shipped the page instead of the slice.
PAGE
  printf '
- [[%s]]
' "$2" >> "$1/$VAULT_DIR/index.md"
}

# The whole-mode half of the same mechanism, built 2026-08-19. `region` writes a slice into a file
# that has a life of its own; `whole` owns a file that has none, so the script writes it end to end
# and removes it by its own marker
# ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).
plant_whole_rule() {  # plant_whole_rule <work> <slug> <glob>
  mkdir -p "$1/$VAULT_DIR/wiki/rules" "$1/.claude/rules"
  cat > "$1/$VAULT_DIR/wiki/rules/$2.md" <<PAGE
---
title: "A rule minted for the whole-mode cases"
type: rule
status: current
governs: .claude/rules/$2.md
render: whole
paths:
  - "$3"
basis: human
sprint: S2
created: 2026-08-19
sources: ["scripts/vault-inject.sh"]
tags: [harness, vault]
---

# A rule minted for the whole-mode cases

<!-- text -->
$SLICE_TEXT
<!-- /text -->

This paragraph is the justification. A generated file carrying this sentence means the injector
wrote the page instead of the slice.
PAGE
  printf '
- [[%s]]
' "$2" >> "$1/$VAULT_DIR/index.md"
}

generate_in()          { (cd "$1" && bash scripts/vault-inject.sh >/dev/null 2>&1); }

whole_ungenerated()    { plant_whole_rule "$1" whole-rule 'generated-scope/*.py'; }
whole_hand_edited()    { whole_ungenerated "$1"; generate_in "$1"
                         echo 'somebody typed this line by hand' >> "$1/.claude/rules/whole-rule.md"; }
whole_no_paths()       { whole_ungenerated "$1"
                         sed -i '/^paths:$/d; /^  - "generated-scope/d' "$1/$VAULT_DIR/wiki/rules/whole-rule.md"; }
                       # `paths:` is required WHERE IT IS READ and nowhere else: Claude Code matches
                       # it on a file under `.claude/rules/` and loads the rule on a matching read.
                       # A rule delivered another way - a hook that prints its text - has no file to
                       # match, and inventing a scope so the check would pass was rejected: a field
                       # a machine reads is the last place to put something untrue. The pair below
                       # is what keeps that from decaying into `paths: is optional`.
whole_outside_rules()  { whole_no_paths "$1"
                         sed -i 's|^governs: \.claude/rules/whole-rule\.md$|governs: .claude/hooks/messages/whole-rule.md|' \
                           "$1/$VAULT_DIR/wiki/rules/whole-rule.md"
                         mkdir -p "$1/.claude/hooks/messages"; }
whole_deprecated()     { whole_ungenerated "$1"; generate_in "$1"
                         sed -i 's/^status: current$/status: deprecated/' "$1/$VAULT_DIR/wiki/rules/whole-rule.md"; }
                       # TWO pages, because the sweep knows a directory only while some current
                       # whole-mode page still generates into it. One page deleted leaves the
                       # other holding the directory open, which is the case worth testing; the
                       # last one leaving is the residual the injector's own comment names.
whole_leftover()       { plant_whole_rule "$1" whole-rule  'generated-scope/*.py'
                         plant_whole_rule "$1" whole-other 'other-scope/*.py'
                         generate_in "$1"
                         rm -f "$1/$VAULT_DIR/wiki/rules/whole-rule.md"
                         sed -i '/\[\[whole-rule\]\]/d' "$1/$VAULT_DIR/index.md"; }
whole_keeps_unmarked() { whole_ungenerated "$1"
                         printf -- '---\npaths: ["hand/*.txt"]\n---\n\nHAND-WRITTEN-AND-UNTOUCHED\n' \
                           > "$1/.claude/rules/hand-written.md"; }

# The one shape rule 12 must call agreement: the region carries exactly what the page ships.
# The destination is a parameter and defaults to the probe file, because the address cases below
# need the same agreeing region written into a file the rule does NOT govern.
# THE AGREEING SHAPE CARRIES THE SEPARATOR (2026-08-18): the rendered form is the slice plus one
# blank line, so a fixture that writes the bare slice is no longer agreement and every `run_clean`
# built on it would go red for the fixture's reason rather than the check's.
mark_region_agreeing() {   # mark_region_agreeing <work> <slug> [destination, default $PROBE]
  printf '
<!-- rule: %s -->
%s

<!-- /rule: %s -->
' "$2" "$SLICE_TEXT" "$2" >> "$1/${3:-$PROBE}"
}

rule_page()          { plant_rule_page "$1" probe-rule "$PROBE"; }
rule_mistyped()      { rule_page "$1"; sed -i 's/^type: rule$/type: decision/' "$1/$VAULT_DIR/wiki/rules/probe-rule.md"; }
rule_no_governs()    { rule_page "$1"; sed -i '/^governs:/d' "$1/$VAULT_DIR/wiki/rules/probe-rule.md"; }
rule_with_authority(){ rule_page "$1"; sed -i '/^governs:/a authority: a-claim-a-rule-may-not-make' "$1/$VAULT_DIR/wiki/rules/probe-rule.md"; }
                     # THE BLOCK FORM, REFUSED 2026-08-21 AND ONLY DIAGNOSED CORRECTLY FROM
                     # 2026-08-22. It is legal YAML, so a YAML editor and PyYAML both accept it
                     # while neither the gate nor the injector reads past the empty scalar - the
                     # text would render into a subset of its destinations and the rest would read
                     # as drift. It went red before this verdict existed, saying "a rule with no
                     # governs:" about a page that names two destinations plainly, which sends the
                     # reader to add a field that is already there.
rule_block_governs() { rule_page "$1"
                       sed -i "s|^governs: \(.*\)|governs:\n  - \1\n  - $SECOND|" \
                         "$1/$VAULT_DIR/wiki/rules/probe-rule.md"; }
                     # The per-folder schema, built 2026-08-19. `wiki/<folder>/_schema.yaml`
                     # names the keys a page there must and may carry, and vault-check.sh
                     # reads it instead of holding a second copy of the list.
unknown_key()        { sed -i '/^tags:/a banana: a key no schema declares' "$1/$SUBJECT"; }
no_required_key()    { sed -i '/^sprint:/d' "$1/$SUBJECT"; }
schema_gone()        { rm -f "$1/$VAULT_DIR/wiki/lessons/_schema.yaml"; }
schema_empty()       { sed -i '/^ *- /d' "$1/$VAULT_DIR/wiki/lessons/_schema.yaml"; }
                     # The value half of the same file, built 2026-08-19 on the owner's ruling
                     # that `basis: banana` must not pass. `values:` names a field and the
                     # values it may carry; the gate reads it from here for the same reason it
                     # reads the key set from here.
bad_basis_value()    { sed -i 's/^basis: .*/basis: banana/' "$1/$SUBJECT"; }
                     # Four spaces, not two: a value entry is indented under its field, while a
                     # required or optional key sits at two. Deleting both would report the key
                     # set missing first and this case would pass on the wrong verdict.
values_block_empty() { sed -i '/^    - /d' "$1/$VAULT_DIR/wiki/concepts/_schema.yaml"; }
                     # A legal value that is simply not the one the page had. If this ever goes
                     # red the check has stopped reading the list and started pinning the value.
other_legal_basis()  { sed -i 's/^basis: .*/basis: inference/' "$1/$SUBJECT"; }
                     # A field the schema names no values for is not judged on its value at all.
                     # Without this case, adding `values:` for one field and accidentally
                     # applying it to every field would still show a green suite.
unconstrained_field(){ sed -i 's/^sprint: .*/sprint: S9/' "$1/$SUBJECT"; }
                     # The subject is a concept that already carries authority:, so adding
                     # governs: is the whole mutation - and it is the non-rule half of the
                     # widened verdict, which is the half that was missing until today.
claim_and_governs()  { sed -i '/^tags:/a governs: CLAUDE.md' "$1/$SUBJECT"; }
# This case used to assert the opposite. The rule it tested - no two current rules on one
# destination - was removed by the owner on 2026-08-17, the first day it met a real tree: a
# file carries as many regions as it has rules, and the four rules of the repository CLAUDE.md
# all govern it. So the case flips from red to green and keeps guarding the same mechanism
# from the other side. What stays red is one SLUG marking two regions in one file, which is a
# case of its own below.
two_rules_one_file() { region_resolves "$1"
                       plant_rule_page "$1" another-rule "$PROBE"
                       mark_region_agreeing "$1" another-rule; }
rules_folder_gone()  { rm -rf "$1/$VAULT_DIR/wiki/rules"; }

region_resolves()  { rule_page "$1"; mark_region_agreeing "$1" probe-rule; }

# A region that agrees with its page except for ONE TRAILING BLANK LINE. Until 2026-08-18 both
# sides of the injector's comparison arrived through `$( )`, which strips every trailing newline,
# so the shell deleted this difference before either side was read and the gate printed `every
# rule agrees with the region it governs`, exit 0, rewriting nothing. Anyone could hand-add a
# blank line inside a rendered region and the harness called it agreement.
#
# The case is written against the check's output and still fails with the fix reverted, because
# reverting makes the check SILENT rather than wrong - which is the failure shape, not an
# exception to it.
#
# TWO blank lines, not one. One is the separator the rendered form now carries, so a case written
# with one would be agreement and would report CAUGHT while testing nothing - the same class of
# green this case exists to close. The difference under test is one line BEYOND the rendered form.
region_trailing_blank() { rule_page "$1"
                          printf '
<!-- rule: probe-rule -->
%s


<!-- /rule: probe-rule -->
' "$SLICE_TEXT" >> "$1/$PROBE"; }

# --- rule 12: the rendering agrees with the page ---------------------------------------------
RULE="$VAULT_DIR/wiki/rules/probe-rule.md"
inject_disagrees()   { rule_page "$1"
                       printf '
<!-- rule: probe-rule -->
A sentence somebody typed straight into the harness file.
<!-- /rule: probe-rule -->
' >> "$1/$PROBE"; }
inject_no_slice()    { region_resolves "$1"
                       sed -i '/<!-- text -->/d; /<!-- \/text -->/d' "$1/$RULE"; }
inject_slice_open()  { region_resolves "$1"; sed -i '/<!-- \/text -->/d' "$1/$RULE"; }
inject_two_slices()  { region_resolves "$1"
                       printf '
<!-- text -->
A second thing this rule would ship.
<!-- /text -->
' >> "$1/$RULE"; }
inject_empty_slice() { region_resolves "$1"
                       sed -i '/^<!-- text -->$/,/^<!-- \/text -->$/{/^<!-- /!d}' "$1/$RULE"; }
inject_governs_air() { region_resolves "$1"
                       sed -i 's|^governs: .*|governs: docs/no-such-harness-file.md|' "$1/$RULE"; }
# `governs:` is a path from the repository root and resolves against nothing else, so the
# vault-relative spelling of a file inside the vault is simply not a file. This case proves that,
# and it used to prove it with `CLAUDE.md` - the one path that exists at both roots, and the first
# file due to be governed.
#
# IT CANNOT USE `CLAUDE.md` ANY MORE, and the reason is the migration itself: a real rule now
# governs the repository's `CLAUDE.md`, so the sandbox materialises it, and the spelling that this
# case needs to NOT resolve resolves. `index.md` carries the same property with nothing depending
# on it - it exists in the vault and not at the repository root - and the case keeps its meaning.
inject_vault_relative() { region_resolves "$1"; sed -i 's|^governs: .*|governs: index.md|' "$1/$RULE"; }
# A deprecated rule has been superseded, and rendering it would put the retired text back into
# the file its successor governs. The case is written with run_case_absent because rule 2 fails
# it anyway for sitting in wiki/ - what is under test is the message that must NOT appear.
inject_deprecated()  { rule_page "$1"; sed -i 's/^status: current$/status: deprecated/' "$1/$RULE"; }
inject_no_script()   { rm -f "$1/scripts/vault-inject.sh"; }
                     # A STATUS THE INJECTOR HAS NEVER HEARD OF, and `draft` is chosen because it
                     # is not a legal value in ANY folder - so this fixture cannot start passing
                     # because some later schema admitted the word. Before 2026-08-23 a rule page
                     # carrying it silently stopped rendering: the test was positive on `current`,
                     # so anything else read as not-current and the region was removed as though
                     # the rule had been retired.
inject_bad_status()  { rule_page "$1"; sed -i 's/^status: current$/status: draft/' "$1/$RULE"; }
                     # `decided_by:` NAMES A DECISION AND ONLY A DECISION, and the target half is
                     # the only half the tree does not already answer: a slug resolving to nothing
                     # is the link sweep's business, because a wikilink in frontmatter is swept
                     # exactly like one in the body. Measured 2026-08-23 before this case was
                     # written - a broken target printed `broken wikilink` and exited 1, and a
                     # target that existed and was an `entity` printed NOTHING and exited 0.
                     #
                     # THE CARGO IS A RULE PAGE because `decided_by:` is legal in `wiki/rules/`
                     # and `wiki/proposals/` alone; on any other folder the `unknownkey` verdict
                     # fires first and this case would pass for that reason instead.
                     #
                     # AND THE CARGO IS `region_resolves` RATHER THAN `rule_page`, which cost a
                     # suite run to learn: a rule page whose destination carries no region for it
                     # is red on THAT, so the clean case below could never be green and the red
                     # case above was red for two reasons at once.
decided_by_entity()  { region_resolves "$1"
                       sed -i '/^governs:/i decided_by: [[vault-scripts]]' "$1/$RULE"; }
                     # The same field pointed at a real decision, which must stay green. Without
                     # this direction the verdict above could be a check that reddens everything
                     # carrying the field and nothing would say so.
                     # REQUIRED IN `wiki/rules/` FROM 2026-08-23. `authority:` is forbidden
                     # there, so this field is the only way a rule names the decision behind it -
                     # and the promotion waited until all fifteen carried one, because required
                     # on an empty corpus reddens the gate and the lock reads a red gate as a
                     # refusal to dispatch the only writer permitted to clear it.
rule_no_decided_by() { region_resolves "$1"
                       sed -i '/^decided_by:/d' "$1/$RULE"; }
decided_by_decision() { region_resolves "$1"
                       sed -i '/^governs:/i decided_by: [[a-refused-proposal-is-archived-and-takes-status-refused]]' "$1/$RULE"; }
                     # ARCHIVING A JOURNAL DOES NOT MAKE IT MUTABLE, and until 2026-08-23 the link
                     # sweep did not know that. `raw/` is excluded from the sweep; `archive/` is
                     # read whole - so the moment `/ingest` moved its own journal from one to the
                     # other, a line of the owner's Russian quoting `[[wikilinks]]` AS SYNTAX
                     # became an address that resolved to nothing. `vault-archive.sh` reversed its
                     # own move and step 12 of that ingest could not finish.
                     #
                     # THE EXEMPTION FOLLOWS THE FOUR RAW KINDS, by the directory the archive
                     # script itself puts them in, and NOT the whole of `archive/`. A retired wiki
                     # page is curated text whose links were always swept and stay swept, which is
                     # the second mutation below - without it this pair would prove only that the
                     # sweep got quieter, which is the direction a defect hides in.
archived_journal()   { d="$1/$VAULT_DIR/archive/2026-08-21/2026-08-21-a-probe-session/handoffs"
                       mkdir -p "$d"
                       printf -- '---\nsession: 2026-08-21\n---\n\n# A journal the sweep must not read\n\nThe owner wrote [[a-slug-that-only-the-archive-probe-names]] meaning the syntax.\n' \
                         > "$d/2026-08-21-a-sweep-probe.md"; }
archived_page()      { d="$1/$VAULT_DIR/archive/2026-08-21/2026-08-21-a-probe-session/pages"
                       mkdir -p "$d"
                       printf -- '---\ntitle: "A retired page the sweep still reads"\ntype: decision\nstatus: deprecated\n---\n\n# A retired page\n\nIt names [[a-slug-that-only-the-archive-probe-names]] as an address.\n' \
                         > "$d/a-retired-sweep-probe.md"; }

# --- rule 13, the index the admission rule is looked up in ------------------------------------
#
# `auth_no_tool` IS THE CASE THAT PINS THE COUPLING RATHER THAN THE VERDICT. Rule 13 asks by
# running the tool, so a tree without it is red - which is fine as a verdict and lethal as an
# accident: the first run of this suite after rule 13 was written had the tool missing from the
# sandbox, and every `run_clean` case would have gone red for a reason no case was about. The tool
# is copied into PRISTINE now, and this case is what keeps that copy honest.
#
# THE OTHERS WANT EXIT 1, AND THEY WANTED 0 FOR THE LENGTH OF ONE BACK-FILL. Rule 13 printed
# advisories while 470 slugs were minted and grouped, because red before the corpus carried the
# field is read by `lock-the-librarian.ps1` as a refusal to dispatch the only writer permitted to
# clear it. It flipped to `note` in the same session, and these cases flipped with it - which is
# what a severity change is supposed to cost, and it is cheap only because the cases existed.
auth_no_tool()  { rm -f "$1/scripts/vault-authority.sh"; }
auth_stale()    { printf -- '- group: nothing real\n  definition: a family no page answers\n  slugs: [not-a-real-slug]\n' > "$1/$VAULT_DIR/authority.md"; }
auth_no_register() { rm -f "$1/$VAULT_DIR/authority.md"; }
auth_stripped()  { local f
                   f=$(grep -rl '^authority:' "$1/$VAULT_DIR/wiki/decisions" | head -1)
                   sed -i '/^authority:/d' "$f"; }
# AN ARCHIVED PAGE KEEPS ITS SLUG AND ITS ROW (owner, 2026-08-29), which repealed the fourth
# supersession step. This plants the page directly in `archive/` rather than moving one out of
# `wiki/`: a move would also change what the link sweep and the orphan rule see, and a clean case
# that stays green for a second reason is a case that tests nothing.
auth_archived_row() {
  mkdir -p "$1/$VAULT_DIR/archive/2026-08-29/a-probe/pages"
  printf -- '---\ntitle: "An archived row probe"\ntype: concept\nstatus: archived\nauthority: an-archived-row-probe\nbasis: inference\nsprint: S3\ncreated: 2026-08-29\nsources: ["scripts/vault-authority.sh"]\ntags: [vault]\n---\n\n# An archived row probe\n\nPlanted by the selftest.\n' \
    > "$1/$VAULT_DIR/archive/2026-08-29/a-probe/pages/an-archived-row-probe.md"
  printf -- '\n- group: the archived probe\n  definition: a family whose only member has been archived\n  slugs: [an-archived-row-probe]\n' \
    >> "$1/$VAULT_DIR/authority.md"
}
auth_two_homes() { local s
                   s=$(grep -rh '^authority:' "$1/$VAULT_DIR/wiki" | head -1 | sed 's/^authority:[[:space:]]*//')
                   printf -- '- group: one\n  definition: a family\n  slugs: [%s]\n\n- group: two\n  definition: the same slug again\n  slugs: [%s]\n' "$s" "$s" > "$1/$VAULT_DIR/authority.md"; }
region_dangling()  { printf '
<!-- rule: no-such-rule -->
<!-- /rule: no-such-rule -->
' >> "$1/$PROBE"; }
region_unclosed()  { rule_page "$1"; printf '
<!-- rule: probe-rule -->
And nothing closes it.
' >> "$1/$PROBE"; }
region_unopened()  { printf '
<!-- /rule: probe-rule -->
' >> "$1/$PROBE"; }
region_mismatch()  { rule_page "$1"; printf '
<!-- rule: probe-rule -->
Opened by one slug.
<!-- /rule: some-other-rule -->
' >> "$1/$PROBE"; }
region_nested()    { rule_page "$1"; printf '
<!-- rule: probe-rule -->
<!-- rule: an-inner-rule -->
Inside two at once.
<!-- /rule: an-inner-rule -->
<!-- /rule: probe-rule -->
' >> "$1/$PROBE"; }
region_twice()     { rule_page "$1"; printf '
<!-- rule: probe-rule -->
Once.
<!-- /rule: probe-rule -->
<!-- rule: probe-rule -->
And again.
<!-- /rule: probe-rule -->
' >> "$1/$PROBE"; }
# Indented, so the strict form does not match it. Detected loosely and judged strictly, this is
# a malformed marker; matched strictly and nothing else, it would be invisible - and a marker
# the steward will never find is worse than one that is wrong out loud.
region_indented()  { rule_page "$1"; printf '
  <!-- rule: probe-rule -->
Text under a marker that is not at column zero.
' >> "$1/$PROBE"; }
region_in_a_fence(){ printf '
How a region is written:

```
<!-- rule: an-example -->
<!-- /rule: an-example -->
```
' >> "$1/$PROBE"; }
# A fence opened and never closed swallows every marker below it. Without this case the rule
# would report the file clean - zero regions, nothing broken - which is the shape of green that
# this project has shipped six times.
region_blinded()   { rule_page "$1"; printf '
```
<!-- rule: probe-rule -->
Swallowed by a fence nobody closed.
' >> "$1/$PROBE"; }
region_in_a_span() { printf '
A region opens with `<!-- rule: an-example -->` and closes with `<!-- /rule: an-example -->`.
' >> "$1/$PROBE"; }

# A MEASURE REGION IS OUT OF SCOPE BY NAME, AND THE PAIR IS THE POINT. Rule 11 asks about RULE
# regions; a measure region names no rule page and renders nothing, and `vault-measure.py --check`
# is what reads it. It was already silent before the rule recognised it - by an accident of
# spelling, because the marker carries no colon and the loose filter wants one - so a case
# asserting only the silence would have passed before the change and proved nothing. What the
# second half pins is that the exemption is by NAME: a marker spelled the other way is still red.
region_measure()      { printf '
<!-- measure -->
- testimony: 34m8s -- conditions: an idle machine -- taken 2026-08-25
<!-- /measure -->
' >> "$1/$PROBE"; }
region_measure_typo() { printf '
<!-- measure: region-coverage -->
<!-- /measure: region-coverage -->
' >> "$1/$PROBE"; }

# --- rule 15: the measure regions, which live in `wiki/` where rule 11 never looks -------------
# THE SCRIPT IS ON THE COPY LIST BECAUSE OF THIS RULE, and the first case is what proves that
# coupling is real rather than assumed. Without it a later hand tidying the copy list would take
# the script out, get `missing file` from a `note`, and turn all 27 `run_clean` cases red at once
# while every `run_case` expecting exit 1 went on passing without its own verdict ever firing.
measure_no_script()  { rm -f "$1/scripts/vault-measure.py"; }
# THE VERDICTS BELOW COME FROM THE SCRIPT AND NOT FROM THE GATE. That is rules 12 and 13's shape:
# the gate carries the question, the writer carries the grammar, and a second implementation here
# would be two answers waiting to differ. These two cases prove the delegation carries a verdict
# across, and they say nothing about the grammar itself - `vault-measure-selftest.py` owns that.
measure_bad_region() { printf '
<!-- measure -->
- 34m8s on an idle machine
<!-- /measure -->
' >> "$1/$SUBJECT"; }
# A GAUGE WRITTEN BY A HAND is the prohibition this whole mechanism exists to keep intact, so it
# is the one grammar verdict worth a case on this side of the delegation too.
measure_hand_gauge() { printf '
<!-- measure -->
- gauge: region-coverage -- 9 of 15
<!-- /measure -->
' >> "$1/$SUBJECT"; }

# --- rule 15's interpreter probe: the guard that refuses a candidate unrun --------------------
#
# THE 59 CASES THAT SHIPPED WITH RULE 15 CANNOT SEE THIS GUARD, and that is the reason this one
# exists. They exercise what the rule does once it HAS an interpreter; the defect of 2026-08-26 was
# in which interpreter it picked. It hung the gate for an hour and was diagnosed twice as a starved
# machine before it was diagnosed at all. The cases could not see it because they run where the walk
# happens to land on something that works - the host's PATH is not a fixture, and a case that relies
# on it is testing the machine.
#
# THE PLANTED STUB PRINTS AND EXITS INSTEAD OF HANGING, AND THAT IS THE WHOLE CARE HERE. The real
# Microsoft Store `python3` neither answers nor exits, and an MSYS signal cannot kill it: `timeout
# 15 python3 -c` did not return in 90 seconds on this machine. That is exactly why the guard refuses
# a candidate UNRUN rather than wrapping it in a timeout. A case planting a genuinely hanging binary
# would hang this suite for ever the moment the guard regressed, and a test may not have that
# failure mode. A stub that prints something rule 15 does not understand is refused by the same
# guard for the same property of its path, and when the guard is gone it produces a NAMED note
# instead of a hang - the discriminator survives and the suite still finishes.
plant_store_stub() {   # plant_store_stub <work> - a `python3` resolving under WindowsApps
  mkdir -p "$1/probe/AppData/Local/Microsoft/WindowsApps"
  printf '#!/bin/sh\necho "PythonManager stub - this is not an interpreter"\n' \
    > "$1/probe/AppData/Local/Microsoft/WindowsApps/python3"
  chmod +x "$1/probe/AppData/Local/Microsoft/WindowsApps/python3"
}

# THE ONE RUNNER THAT MUTATES THE PROCESS AS WELL AS THE TREE. Every other case here changes files
# and asks what the gate SAYS; this changes PATH and asks what the gate RUNS. The tree is still
# mutated, because the stub is a file - so the `changed nothing` guard above still has something to
# compare, and this case cannot go green by doing nothing.
#
# THE ASSERTION IS AN ABSENCE, which is the weaker shape and is named as such. A guard that skips
# the stub leaves rule 15 to the next candidate and the run is simply green; there is no line to
# grep for. What makes the absence meaningful is that the presence is specific: run the stub and
# rule 15 says so by name.
run_probe_case() {     # run_probe_case <name> <must NOT appear> <mutation fn>
  local case_name="$1" forbid="$2" mutate="$3"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/work.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    "$mutate" "$work"
    if diff -rq "$PRISTINE" "$work" >/dev/null 2>&1; then
      report "$case_name" no "the mutation changed nothing - this case tests nothing"
      rm -rf "$work"; exit 0
    fi
    out=$(cd "$work" && PATH="$work/probe/AppData/Local/Microsoft/WindowsApps:$PATH" \
          bash scripts/vault-check.sh 2>&1); code=$?
    if [ "$code" = "0" ] && ! grep -qF "$forbid" <<<"$out"; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code - the stub was RUN instead of being skipped unrun
$out"
    fi
    rm -rf "$work"
  ) &
}

# --- the address: a region is checked against the `governs:` of the rule it names -------------
# A second governed file, MADE rather than found. The sweep picks up any markdown under
# `.claude/`, so the sandbox already contains several - but every one of them is a placeholder
# minted from some page's `sources:`, and a case that reached for whichever of those the corpus
# happens to cite today would change meaning on the day that citation changed.
SECOND=".claude/templates/a-second-governed-file.md"
plant_second_file() { mkdir -p "$1/.claude/templates"
                      printf 'A governed file that exists for the address cases and nothing else.\n' \
                        > "$1/$SECOND"; }

# THE CASE IS THE LEFTOVER, not the wrong file. A rule governing A whose region sits only in B is
# already red without this verdict - the injector opens A, finds no region, and rule 12 says so -
# and a case built that way would pass with the check reverted, which is this suite reproducing
# the failure it exists to catch. What no other verdict sees is the region present in A AND in B:
# rule 11 keys its duplicate check per file, and the injector never opens B.
region_stray()      { region_resolves "$1"; plant_second_file "$1"
                      mark_region_agreeing "$1" probe-rule "$SECOND"; }

# The green half carries a SECOND RULE on purpose. With one destination in the whole tree, a join
# that compared the wrong column - or nothing at all - would stay green here and prove nothing.
regions_two_files() { region_resolves "$1"; plant_second_file "$1"
                      plant_rule_page "$1" second-rule "$SECOND"
                      mark_region_agreeing "$1" second-rule "$SECOND"; }

# --- `governs:` NAMES A LIST, and one address is the one-element case (2026-08-21) ------------
#
# THE CORPUS EXERCISES NONE OF THIS, WHICH IS WHY THE CASES ARE HERE. Measured on 2026-08-21, on
# the real tree: making the gate's `govsplit` return nothing at all left `bash scripts/vault-check.sh`
# byte-identical and still exit 0. Every rule page in the corpus governs the file its region is
# already in, so the address comparison never reaches its interesting branch and a green gate is
# no evidence about it whatever. The suite is the only instrument that reaches it.
THIRD=".claude/templates/a-third-governed-file.md"
plant_third_file() { mkdir -p "$1/.claude/templates"
                     printf 'A governed file that exists for the list cases and nothing else.\n' \
                       > "$1/$THIRD"; }

# Rewrites the probe rule's destination. Written as one `sed` over the whole line rather than an
# append, because the field is single-valued in the fixture it starts from.
set_governs() {   # set_governs <work> <yaml value>
  sed -i "s|^governs: .*|governs: $2|" "$1/$RULE"; }

# GREEN: two destinations, a region in each. This is the case the change exists for, and it fails
# in BOTH halves if either reader is wrong - the injector has to render into the second file, and
# rule 11 has to accept a region there. Before 2026-08-21 the second region was drift by
# definition, because the field could not name it.
governs_list_both() { region_resolves "$1"; plant_second_file "$1"
                      set_governs "$1" "[$PROBE, $SECOND]"
                      mark_region_agreeing "$1" probe-rule "$SECOND"; }

# GREEN: the one-element list means exactly what the bare scalar means. Without this case the two
# spellings could drift apart unnoticed, and thirteen pages in the corpus use the bare one.
governs_list_one()  { region_resolves "$1"; set_governs "$1" "[$PROBE]"; }

# RED, and it is the LEFTOVER again rather than the wrong file - the same shape as `region_stray`
# above and for the same reason. Both governed files carry their region, so the injector is
# satisfied and rule 12 is silent; what is wrong is the THIRD region, in a file the list does not
# name. A case that simply moved the region out of the governed set would go red under rule 12
# with this change reverted, and prove nothing about the list.
governs_list_stray() { governs_list_both "$1"; plant_third_file "$1"
                       mark_region_agreeing "$1" probe-rule "$THIRD"; }

# --- the marker carries a type, and `governs:` is read as a field (2026-08-18) ----------------
#
# A CONCEPT PAGE THAT DELIVERS, planted the same way a rule page is. It is the whole point of the
# widened glob: `governs:` outside `wiki/rules/` used to be neither rendered nor refused.
# THE PAIR'S FIXTURE PLANTS BOTH PAGES, and that is the point rather than a convenience. A case
# pointing `decided_by:` at a real decision in the corpus would couple itself to that page's
# `binding:` - a field a librarian may legitimately change tomorrow - and this suite has already
# been taught what one hardcoded slug costs when forty-three cases stand on it. Here the decision
# is planted beside the proposal, so the case owns both ends of what it asserts.
#
# BOTH PAGES ARE LINKED FROM `index.md`, because a planted page nothing names is an orphan and the
# case would go red for a reason it is not about.
plant_idea_pair() {      # plant_idea_pair <work> <decision slug> <binding> <proposal slug>
  cat > "$1/$VAULT_DIR/wiki/decisions/$2.md" <<PAGE
---
title: "A decision minted for the idea pairing cases"
type: decision
status: current
authority: $2
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["scripts/vault-check.sh"]
binding: $3
tags: [vault, harness]
---

# A decision minted for the idea pairing cases

Planted by the selftest. It exists to be named by [[$4]] and for nothing else.
PAGE
  cat > "$1/$VAULT_DIR/wiki/proposals/$4.md" <<PAGE
---
title: "A proposal minted for the idea pairing cases"
type: proposal
status: idea
authority: $4
basis: human
sprint: S3
created: 2026-08-24
sources: ["scripts/vault-check.sh"]
decided_by: [[$2]]
tags: [vault, harness]
---

# A proposal minted for the idea pairing cases

Planted by the selftest, carrying [[$2]] as its cause.
PAGE
  printf '
- [[%s]]
- [[%s]]
' "$2" "$4" >> "$1/$VAULT_DIR/index.md"
  # AND THE TWO SLUGS ARE REGISTERED, which no other planter in this file has to do. Every one of
  # them plants a page that carries `governs:` instead of `authority:`, or a concept where the two
  # are forbidden together - so none of them ever met rule 13, which asks `vault-authority.sh`
  # whether every page outside `wiki/rules/` carries an authority that can be LOOKED UP. A slug in
  # the tree and not in `authority.md` is red, and the register is compared in both directions, so
  # a slug here with no page would be red too. Both are planted, so both are registered.
  #
  # PLAIN TEXT AND NEVER `[[wikilinks]]`, which is the register's own rule: a register that linked
  # every page would join the link sweep and no page in this vault could be an orphan again.
  printf '
- group: the planted pages of the idea pairing cases
  definition: the fixture this suite plants for the idea and decided_by pair. Answers nothing about
    the product; it is here so the two planted pages can be looked up like any other.
  slugs: [%s, %s]
  aliases: [selftest fixture]
' "$2" "$4" >> "$1/$VAULT_DIR/authority.md"
}
idea_binds()    { plant_idea_pair "$1" "a-planted-decision-that-binds"   prohibition "a-planted-idea-with-a-cause"; }
idea_deferred() { plant_idea_pair "$1" "a-planted-decision-that-defers"  deferral    "a-planted-idea-that-was-deferred"; }

plant_concept_page() {   # plant_concept_page <work> <slug> <destination>
  cat > "$1/$VAULT_DIR/wiki/concepts/$2.md" <<PAGE
---
title: "A concept minted for the type-in-marker cases"
type: concept
status: current
governs: $3
render: region
basis: human
sprint: S2
created: 2026-08-18
sources: ["scripts/vault-inject.sh"]
tags: [harness, vault]
---

# A concept minted for the type-in-marker cases

<!-- text -->
$SLICE_TEXT
<!-- /text -->

This paragraph is the justification, and it must not travel.
PAGE
  printf '
- [[%s]]
' "$2" >> "$1/$VAULT_DIR/index.md"
}

mark_concept_region() {   # mark_concept_region <work> <slug> [destination, default $PROBE]
  printf '
<!-- concept: %s -->
%s

<!-- /concept: %s -->
' "$2" "$SLICE_TEXT" "$2" >> "$1/${3:-$PROBE}"
}

# The green case, and it is the one that would have stayed green with the old code while proving
# the opposite: under the `wiki/rules/` glob this page rendered nowhere and its region agreed with
# nothing, and the check said `ok` about a page it never opened.
concept_renders()    { plant_concept_page "$1" probe-concept "$PROBE"
                       mark_concept_region "$1" probe-concept; }

# The same page with its `render:` stripped, which is the input the injector must refuse once the
# default is gone. Written as a strip of the planter above rather than as a second heredoc: two
# heredocs of one fixture drift apart, and this suite has already lost cases to exactly that.
# MOVED ONTO A RULES PAGE 2026-08-21, WITH `governs:` ITSELF. It stripped `render:` from a
# `concepts/` page until the owner ruled that a page which renders IS a rule; the field left that
# folder's schema with `governs:`, so the input this fixture has to build can only exist in
# `wiki/rules/` now. The subject is unchanged - a page that renders and names no mode - and only
# the folder it can live in moved.
plant_lookup_rule() {   # plant_lookup_rule <work> <slug> <authority>
  mkdir -p "$1/$VAULT_DIR/wiki/rules"
  cat > "$1/$VAULT_DIR/wiki/rules/$2.md" <<PAGE
---
title: "A rule the hook finds by its slug"
type: rule
status: current
authority: $3
render: authority
basis: human
sprint: S3
created: 2026-08-30
sources: ["scripts/vault-check.sh"]
decided_by: [[a-refused-proposal-is-archived-and-takes-status-refused]]
tags: [harness, vault]
---

# A rule the hook finds by its slug

Planted by the selftest. It names no destination and carries no marked slice, deliberately: the
hook matches its \`authority:\` against the file being touched and hands this page over then.
PAGE
}

# THE SLUG IS REGISTERED SEPARATELY from planting the page, because one of the three cases below
# removes `authority:` and a registered slug with no page carrying it is a different red - rule 13
# would fire about the register while the case is asking about the page.
lookup_rule_clean()   { plant_lookup_rule "$1" probe-lookup-rule selftest-lookup-mode
                        lc_register "$1" probe-lookup-rule selftest-lookup-mode; }
lookup_rule_governs() { plant_lookup_rule "$1" probe-lookup-rule selftest-lookup-mode
                        lc_register "$1" probe-lookup-rule selftest-lookup-mode
                        sed -i "s|^render: authority$|render: authority\ngoverns: $PROBE|" \
                          "$1/$VAULT_DIR/wiki/rules/probe-lookup-rule.md"; }
lookup_rule_no_slug() { plant_lookup_rule "$1" probe-lookup-rule selftest-lookup-mode
                        sed -i '/^authority:/d' "$1/$VAULT_DIR/wiki/rules/probe-lookup-rule.md"
                        printf '\n- [[probe-lookup-rule]]\n' >> "$1/$VAULT_DIR/index.md"; }

# ONE SLUG, TWO TYPES, AND IT MUST NOT FIRE. The entity is written with the concept subject's own
# `authority:` line, so no new slug enters the register and rule 13 has nothing to say; what is
# under test is rule 3 alone. The index line is what keeps it off the orphan rule.
authority_across_types() {
  local a; a=$(need_authority "$1")
  mkdir -p "$1/$VAULT_DIR/wiki/entities"
  cat > "$1/$VAULT_DIR/wiki/entities/the-entity-half-of-one-question.md" <<PAGE
---
title: "The entity half of a question a concept also answers"
type: entity
status: current
$a
basis: inference
sprint: S3
created: 2026-08-30
sources: ["scripts/vault-check.sh"]
tags: [vault, harness]
---

# The entity half of a question a concept also answers

Planted by the selftest. It carries the same \`authority:\` as a page in \`concepts/\`, which is
legal from 2026-08-30 and is how a reader gets from one to the other.
PAGE
  printf '\n- [[the-entity-half-of-one-question]]\n' >> "$1/$VAULT_DIR/index.md"
}

plant_rule_page_no_render() {   # plant_rule_page_no_render <work> <slug> <destination>
  plant_rule_page "$1" "$2" "$3"
  sed -i '/^render:/d' "$1/$VAULT_DIR/wiki/rules/$2.md"
}

# A PAGE THAT RENDERS AND NAMES NO MODE. Until 2026-08-20 this was silently read as `region`; the
# owner ruled it red that day, the verdict having been recorded nowhere until he was asked.
#
# THE CASE ASSERTS THE DIAGNOSIS AND NOT THE REFUSAL, and that is the whole reason it is a
# `run_case_absent`. Deleting the default line alone leaves the empty string falling through to
# the `*)` branch, which refuses correctly and says `render '' is neither region nor whole` - a
# true refusal naming a condition nobody can clear, because the field is missing rather than
# wrong. A `run_case` pinning the refusal would have gone green against exactly that defect, which
# is the failure this repository met the same day in `hook-selftest.ps1`: a case asserted the
# literal `THE CONDITION IS` while the command that refusal named was mangled and unusable.
concept_no_render()  { plant_rule_page_no_render "$1" probe-rule "$PROBE"
                       mark_region_agreeing "$1" probe-rule; }

# `render:` gained a legal-value list in `concepts/_schema.yaml` on 2026-08-20, copied from
# `rules/_schema.yaml` when the field was admitted here. Without that copy this page would pass
# rule 2 while the identical page one folder away failed, and the injector could not cover for it:
# it reads `render` only AFTER skipping every page that carries no `governs:`.
bad_render_value()   { plant_rule_page "$1" probe-rule "$PROBE"
                       mark_region_agreeing "$1" probe-rule
                       sed -i 's/^render: .*/render: banana/' "$1/$VAULT_DIR/wiki/rules/probe-rule.md"; }

# An unknown type word is MALFORMED and never "a marker for a type nobody has heard of". Narrowing
# the net to the six known words would move exactly this line into silence.
marker_unknown_type() { printf '
<!-- widget: probe-rule -->
<!-- /widget: probe-rule -->
' >> "$1/$PROBE"; }

# The slug exists - as a rule - and the marker calls it a concept. The verdict is the same red as
# a slug that exists nowhere; what is under test is that it names the folder the page is actually
# in, because that is the failure the type-in-marker design makes possible in the first place.
marker_wrong_type()  { rule_page "$1"; printf '
<!-- concept: probe-rule -->
<!-- /concept: probe-rule -->
' >> "$1/$PROBE"; }

# The inverse of a rule with no `governs:`: text marked to ship from a page that names no
# destination. The injector never opens the page, so nothing else in the harness can see it.
slice_without_governs() { plant_concept_page "$1" probe-concept "$PROBE"
                          mark_concept_region "$1" probe-concept
                          sed -i '/^governs:/d' "$1/$VAULT_DIR/wiki/concepts/probe-concept.md"; }

# A wikilink in a slice reaches the destination as dead punctuation - Obsidian syntax is inert in
# the file it is rendered into, which is why that file refuses links at all. Stated by the owner
# on 2026-08-17 with nothing holding it; this is the holding.
slice_wikilink()     { rule_page "$1"
                       sed -i 's|^The test database comes from.*|A sentence citing [[a-sprint-closes-on-its-goal]] inside the slice.|' \
                         "$1/$VAULT_DIR/wiki/rules/probe-rule.md"; }

# A wikilink inside a code span is DESCRIBING the form rather than shipping it, the same
# distinction every other content rule in this repository draws.
# A fenced block inside a slice, rendered for real and read back off the destination. The region
# is planted EMPTY so the injector has to do the writing - an agreeing region would let the case
# pass without the injector running at all.
mark_region_empty()  { printf '
<!-- rule: %s -->
<!-- /rule: %s -->
' "$2" "$2" >> "$1/${3:-$PROBE}"; }

fence_in_slice()     { cat > "$1/$VAULT_DIR/wiki/rules/probe-rule.md" <<'PAGE'
---
title: "A rule whose slice carries a fenced block"
type: rule
status: current
governs: .claude/templates/handoff.md
render: region
basis: human
sprint: S2
created: 2026-08-18
sources: ["scripts/vault-inject.sh"]
tags: [harness, vault]
---

# A rule whose slice carries a fenced block

<!-- text -->
Commands:

```
uv run pytest -q
```
<!-- /text -->

The justification stays outside the slice, fence and all.
PAGE
                       #    The heredoc is quoted because the slice contains backticks, so the
                       #    destination cannot be interpolated into it; it is written afterwards
                       #    instead of hard-coded, or this case silently governs the wrong file
                       #    the day $PROBE moves.
                       sed -i "s|^governs: .*|governs: $PROBE|" "$1/$VAULT_DIR/wiki/rules/probe-rule.md"
                       printf '
- [[probe-rule]]
' >> "$1/$VAULT_DIR/index.md"
                       mark_region_empty "$1" probe-rule; }

slice_wikilink_span() { region_resolves "$1"
                        sed -i 's|^The test database comes from.*|A slice may not carry a `[[wikilink]]`, and this line says so.|' \
                          "$1/$VAULT_DIR/wiki/rules/probe-rule.md"
                        sed -i 's|^The test database comes from.*|A slice may not carry a `[[wikilink]]`, and this line says so.|' \
                          "$1/$PROBE"; }

run_case "missing frontmatter field"   "missing frontmatter field 'tags'"         1 drop_field
run_case "frontmatter only in a fence" "missing frontmatter field 'title'"        1 fenced_frontmatter
run_case "type disagrees with folder"  "disagrees with folder 'concepts'"         1 wrong_type
run_case "decision with no date"       "a decision with no 'decided:' date"       1 drop_decided
run_case "sources names a dead path"   "sources names a path that does not exist" 1 bogus_source
run_case "duplicate authority"         "duplicate authority"                      1 dup_authority
run_case "broken wikilink"             "broken wikilink"                          1 broken_link
run_case "link to a 0-byte page"       "broken wikilink: [[hollow-page]]"         1 empty_target
run_case "only link is inside a fence" "orphan page, nothing links to it"         1 link_in_a_fence
run_case "only link is in raw/"        "orphan page, nothing links to it"         1 link_only_in_raw
run_case "orphan page"                 "orphan page, nothing links to it"         1 orphan_page
run_case "tag not in the dictionary"   "is not in"                                1 unknown_tag
run_case "unknown tag in a block list" "not-a-registered-tag"                     1 block_list_tags
run_case "tags: []"                    "carries 0 tags"                           1 empty_tag_list
run_case "one tag on a page"           "carries 1 tags"                           1 one_tag
run_case "six tags on a page"          "carries 6 tags"                           1 six_tags
#    THE EXPECTED SUBSTRING CHANGED ON 2026-08-23 AND THE CASE DID NOT. It read `status 'draft'`,
#    which was the wording of a verdict this gate no longer has: the legal status values moved out
#    of the awk pass into every `wiki/*/_schema.yaml`, so an illegal one now arrives through the
#    generic `badvalue` route and names the schema that refused it
#    ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
#    The behaviour never lapsed - `draft` was refused before and after, exit 1 both times - and
#    the suite still went from `caught 158, missed 0` to `caught 157, missed 1`, because a case
#    greps the message. That is the cost this project has written down twice: a cosmetic change is
#    load-bearing where a test reads the output ([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).
#    The substring below pins the field and the value and not the sentence around them.
#
#    The case name became MORE true, not less: until this date no schema listed a status value at
#    all, so "the schema lacks" was a figure of speech. It is now the literal mechanism under test.
run_case "a status the schema lacks"   "'status' carries 'draft'"                 1 bad_status
run_case "deprecated page left in wiki" "still in wiki/"                          1 deprecated_here
#    THE THREE CASES OF 2026-08-28, and the third is the one that matters. Two new status values
#    were minted the same day and only one obliges a page to leave; a gate that treated them alike
#    would pass both red cases below and lock the librarian out of the folder it is draining.
#
#    THE ARCHIVED MESSAGE IS PINNED ON `did not finish` AND NOT ON `still in wiki/`. The deprecated
#    case above already greps that substring, so pinning it here would leave a gate that had lost
#    the archived branch entirely still passing - both cases would match the one surviving message.
run_case "archived page left in wiki"  "did not finish"                           1 archived_here
run_case "processed outside decisions" "'status' carries 'processed'"             1 processed_astray
run_clean "processed decision stays where it is" plant_processed_decision
run_case "CLAUDE.md points at nothing" "CLAUDE.md names a page that does not exist" 1 claude_md_link
run_case "a fenced link in a register"  "orphan page, nothing links to it"         1 fenced_link_reg
run_case "sources as a block list"     "sources names a path that does not exist" 1 block_list_sources
run_case "sources wrapped over two lines" "docs/no-such-file-wrapped.md"    1 wrapped_sources
run_case "sources as a bare scalar"    "docs/no-such-file-scalar.md"             1 scalar_sources
run_case "sources as an unquoted list" "docs/no-such-file-bare.md"               1 bare_list_sources
run_case "frontmatter never closed"    "is never closed by a second ---"          1 unterminated_fm
run_case "two tags: lines on a page"   "two 'tags:' lines"                        1 two_tag_lines
run_case  "a journal lost a section"     "missing [Lessons]"                         1 uncompiled_short
run_case  "a journal renamed a section"  "missing [Lessons], unexpected [Learnings]" 1 uncompiled_renamed
run_case  "the handoff template is gone" "rule 8 reads the section set from it"      1 no_handoff_template
run_clean "an old form already compiled" compiled_old_form
run_case "a layout directory is gone"  "missing directory"                        1 missing_dir
run_case "a register file is gone"     "missing file"                             1 missing_file
run_case "a space in the vault's name" "a vault with spaces/wiki/concepts"        1 renamed_and_one_tag

section "--- and what must NOT fail ---"
run_case "unused tag stays advisory"   "advisory: tag 'never-used'"               0 dead_tag

# THE DENSITY ADVISORY MOVED BEHIND `--lint` (2026-08-20), AND IT TAKES BOTH DIRECTIONS TO SAY SO.
# One case would not: asserting it prints under the flag leaves a gate that prints it always still
# passing, and asserting it is absent from a bare run leaves a gate that never prints it at all
# still passing. The pair pins the flag to exactly one behaviour.
run_case_absent "a dense tag is silent in a bare run" \
                "VAULT-CHECK: ok" "tag dense-test selects 11 pages in concepts/" 0 dense_tag
run_lint_case "a dense tag advises under --lint" \
              "tag dense-test selects 11 pages in concepts/" 0 dense_tag

# --- a quote is Cyrillic (2026-08-22) ---------------------------------------------------------
#
# WHY THE PAGE IS MINTED RATHER THAN BORROWED. The sandbox mirrors the real corpus, which already
# carries 27 English blocks, so the advisory fires here whatever a case does. What a case can prove
# is whether ITS page is named - and that needs a path this suite owns, not whichever page
# `$SUBJECT` resolves to today.
#
# THE FIXTURE DATA IS RUSSIAN ON PURPOSE and is not a breach of the English rule: it is test data,
# the same standing exemption `test_migrations.py` keeps for its Cyrillic fixtures and stderr
# substrings. A case for a rule about Cyrillic cannot be written without any.
QUOTE_PAGE="wiki/concepts/a-page-minted-for-the-quote-cases.md"
plant_quote_page() {  # plant_quote_page <work> <the block>
  cat > "$1/$VAULT_DIR/$QUOTE_PAGE" <<PAGE
---
title: "A page minted for the quote cases"
type: concept
status: current
authority: quote-case-probe
basis: human
sprint: S2
created: 2026-08-22
sources: ["scripts/vault-check.sh"]
tags: [harness, vault]
---

# A page minted for the quote cases

$2

And a paragraph under it, so the block is not the last thing in the file.
PAGE
  printf '
- [[a-page-minted-for-the-quote-cases]]
' >> "$1/$VAULT_DIR/index.md"
  #    THE SLUG NEEDS A HOME OR THE SANDBOX IS RED FOR A REASON THIS CASE IS NOT ABOUT. Rule 13
  #    asks that every `authority:` a page carries is in a group in `authority.md`, so planting a
  #    page with a fresh slug and nothing else reddens the tree and the case fails at exit 1 with
  #    the right advisory sitting in its output. That is the diagnosis-shaped failure this suite
  #    has been bitten by twice and warns about at the archive cases; it bit these three on their
  #    first run and is fixed here rather than by relaxing what the cases want.
  printf -- '
- group: the quote cases
  definition: a family the selftest mints for the quote advisory
  slugs: [quote-case-probe]
' >> "$1/$VAULT_DIR/authority.md"
}
quote_english()  { plant_quote_page "$1" '> **owner: a ruling in words he never used.**'; }
quote_cyrillic() { plant_quote_page "$1" '> **owner: не было такого правила.**'; }

# BOTH DIRECTIONS OF THE CHANNEL, then both directions of the reader. The channel pair is the same
# shape the density advisory needed: one case alone leaves either an always-printing gate or a
# never-printing one passing.
run_case_absent "an English owner block is silent in a bare run" \
                "VAULT-CHECK: ok" "owner-attributed block(s) carry no Cyrillic" 0 quote_english
run_lint_case "an English owner block advises under --lint" \
              "$QUOTE_PAGE" 0 quote_english

# AND THE READER ITSELF, which is the half that has already been wrong here. A `grep` with a
# Cyrillic character class reported this corpus's split REVERSED and agreed with itself across two
# runs, so the wrong figure survived a correction and reached three files. A case that only proved
# an English block prints would pass on a reader that flagged every block regardless.
run_lint_absent "a Cyrillic owner block is not named" \
                "owner-attributed block(s) carry no Cyrillic" "$QUOTE_PAGE" 0 quote_cyrillic

# The advisory must not move the verdict, for the same reason the density line must not.
run_parity "the quote advisory does not move a green exit code" quote_english

# A DEPRECATED TARGET IN `archive/` AND AN ARCHIVED ONE BESIDE IT, both linked from the same live
# page. The pair is the whole point of the narrowing taken on 2026-08-29: the verdict keys on the
# literal `deprecated` and never on "the target's status", so the `archived` neighbour has to be
# absent from the list. This corpus carries about 240 archived pages, and a verdict that could not
# tell the two values apart would print hundreds of lines where forty are meant.
#
# IT APPENDS TO `$SUBJECT` RATHER THAN MINTING A LIVE PAGE. A new page under `wiki/` would need a
# registered authority slug and an inbound link of its own, and a case that went red for either of
# those would be reporting about the fixture rather than about the advisory.
DEP_PROBE_DIR="archive/2026-08-29/a-deprecated-link-probe/pages"
dep_link() {
  mkdir -p "$1/$VAULT_DIR/$DEP_PROBE_DIR"
  printf -- '---\ntitle: "A retired probe"\ntype: concept\nstatus: deprecated\nauthority: retired-link-probe\nbasis: inference\nsprint: S3\ncreated: 2026-08-29\nsuperseded_by: [[%s]]\nsources: ["scripts/vault-check.sh"]\ntags: [vault]\n---\n\n# A retired probe\n\nPlanted by the selftest; it names [[%s]] so nothing dangles.\n' \
    "$SUBJECT_NAME" "$SUBJECT_NAME" > "$1/$VAULT_DIR/$DEP_PROBE_DIR/retired-link-probe.md"
  printf -- '---\ntitle: "An archived probe"\ntype: concept\nstatus: archived\nauthority: archived-link-probe\nbasis: inference\nsprint: S3\ncreated: 2026-08-29\nsources: ["scripts/vault-check.sh"]\ntags: [vault]\n---\n\n# An archived probe\n\nPlanted by the selftest; it names [[%s]] so nothing dangles.\n' \
    "$SUBJECT_NAME" > "$1/$VAULT_DIR/$DEP_PROBE_DIR/archived-link-probe.md"
  printf '\nPlanted by the selftest: [[retired-link-probe]] and [[archived-link-probe]].\n' >> "$1/$SUBJECT"
}

run_case_absent "a live link into a retired page is silent in a bare run" \
                "VAULT-CHECK: ok" "retired-link-probe" 0 dep_link
run_lint_case "a live link into a retired page advises under --lint" \
              "retired-link-probe (1 link" 0 dep_link
run_lint_absent "the advisory names a deprecated target and not an archived one" \
                "retired-link-probe (1 link" "archived-link-probe" 0 dep_link
run_parity "the deprecated-link advisory does not move a green exit code" dep_link

# THESE TWO CATCH NOTHING TODAY AND THAT IS WHAT THEY ARE FOR. The flag currently gates a bare
# `echo`, so the exit codes cannot differ; both cases would have passed before it existed. They
# fail the day somebody puts a `note` behind `--lint` - which is the one way this flag turns from
# a report into a hidden check, and the argument for doing it will sound exactly like the argument
# that put the density line there. Green and red are both exercised, because parity on a clean
# tree is the easy half.
run_parity "the flag does not move a green exit code" dense_tag
run_parity "the flag does not move a red exit code"   two_tag_lines
run_found "the vault is renamed"       renamed_vault
run_clean "a URL in sources"           url_source
run_clean "authority inside a fence"   fenced_authority
run_clean "an aliased [[link|text]]"   aliased_links
run_clean "a [[link#heading]]"         heading_links
run_clean "a broken link in raw/"      broken_link_in_raw
run_clean "a vault with no pages yet"  empty_vault
run_clean "another value the schema allows" other_legal_basis
run_clean "a field the schema constrains no values for" unconstrained_field
run_clean "a proposal in its own folder" proposal_page
run_case "a proposal typed as a decision" "type 'decision' disagrees with folder 'proposals'" 1 proposal_mistyped
run_case "the proposals folder removed"  "missing directory"                          1 proposals_gone
run_clean "a fenced example in a register" fenced_example_reg
run_clean "quoted tag names"          quoted_tags
run_clean "quoted tags in a block list" quoted_block
run_clean "a vault written with CRLF" crlf_vault
run_clean "a page saved with a BOM"   bom_page
run_case_absent "a deprecated page's authority" "still in wiki/" "duplicate authority" 1 deprecated_dup



run_case  "a title that counts"         "the title counts (seven)"                 1 title_counts
                    # INVERTED 2026-08-19, and this is the whole test of the withdrawal.
                    # Until then a quantity: line made this fixture green; the check no
                    # longer reads the field, so the same fixture must now be caught. A case
                    # DELETED with the mechanism it tested proves the mechanism is unused; a
                    # case INVERTED proves it is gone.
run_case  "a counted title no longer answers" "the title counts (seven)"          1 title_declared
run_case  "an ordinal in a title"             "the title counts (fifth)"          1 title_ordinal
run_clean "the word first is not a count"      title_word_first
run_clean "a number inside a code span"   title_code_span
run_clean "an ISO date in a title"        title_iso_date
run_clean "the word one is not a count"   title_word_one
run_clean "a digit glued to a letter"     title_glued

run_case        "a filename that counts"          "two-clocks-on-a-selftest-page (two)"  0 filename_counts
                    # EXIT 1 SINCE 2026-08-19, and the reason is not the thing under test.
                    # The assertion is the printed slug: rule 10 stopped reading the field,
                    # so a page declaring one no longer has its name silenced. The exit code
                    # comes from somewhere else entirely - the per-folder schema rejects
                    # `quantity` as a key no schema declares, which is the same withdrawal
                    # arriving from the other side and means the field can no longer be
                    # written onto a page at all. Both are wanted; only the slug is tested.
run_case        "a counted filename no longer answers" \
                "two-clocks-on-a-selftest-page (two)"                                    1 filename_declared
run_case        "an ordinal in a filename"        \
                "the-fifth-verdict-on-a-selftest-page (fifth)"                           0 filename_ordinal
run_case_absent "an ISO date in a filename"       "VAULT-CHECK: ok" \
                "what-predates-2026-08-05-is-deferred-in-the-selftest"                   0 filename_iso_date
run_case_absent "a glued digit in a filename"     "VAULT-CHECK: ok" \
                "the-selftest-console-is-cp1252-and-must-be-told"                        0 filename_glued
run_case_absent "the word one in a filename"      "VAULT-CHECK: ok" \
                "an-absent-value-never-overwrites-a-known-one-in-the-selftest"           0 filename_word_one

section "--- the decision lifecycle ---"
#    FIVE REDS AND TWO GREENS, and the two greens are not padding. Rule 16 is scoped by a date and
#    rule 17 by whether the target exists, so the cases that must NOT fire are exactly the ones
#    that say the scoping works: a page older than the cut, and a decision whose target has not
#    been written. Without them a rule that reddened everything would pass this section.
run_case "a dated page with no sections"      "is missing the '# ' section(s)"                 1 lc_dated_no_sections
run_case "a dated page names no target"       "carries no 'target_kind:'"                      1 lc_dated_no_fields
run_case "the target ignores the decision"    "does not name this decision in decided_by:"     1 lc_handshake_half
run_case "required_from names an unknown key" "required_from: names 'not-a-declared-key'"      1 lc_key_not_allowed
run_case "an empty sections: block"           "sections: block that parses to nothing"         1 lc_sections_empty
run_case "a repealed rule still in wiki/"     "status is repealed but the page is still in"    1 lc_repealed_astray
run_clean "a page older than the cut is not judged" lc_older_bare
run_clean "an unwritten target reads as open"      lc_handshake_open
# THE CONDITIONAL SIXTH SECTION, added 2026-08-30. A decision whose target is a rule carries the
# sentence the rule page is assembled from; one whose target is an action or a repeal has no such
# sentence and is never asked for it. Both directions are here, because a verdict that ranged over
# every decision in the folder would be exactly the unclearable shape this store keeps catching.
run_case  "a rule-target decision with no clause" "owes the '# ' section"     1 lc_rule_target_no_clause
run_clean "an action-target decision owes none"   lc_action_target_no_clause

section "--- marked regions ---"
run_case "a region names no rule page"  "a region with no page behind it"                1 region_dangling
run_case "a region is never closed"     "is opened and never closed"                     1 region_unclosed
run_case "a close with no open"         "closes a region"                                1 region_unopened
run_case "a region closed by another slug" "closed with the wrong address"               1 region_mismatch
run_case "regions that nest"            "opens inside another"                           1 region_nested
run_case "one rule marks two regions"   "marks two regions in one file"                  1 region_twice
run_case "a marker not at column zero"  "not a marker alone on its line"                 1 region_indented
run_clean "a measure region is out of scope for rule 11" region_measure
run_case "a measure marker spelled with a colon is still malformed" \
                                        "not a marker alone on its line"                 1 region_measure_typo
run_case "a key no schema declares"     "is in neither the required nor the optional list" 1 unknown_key
run_case "a required key removed"       "missing frontmatter field 'sprint'"           1 no_required_key
run_case "a folder with no schema"      "no _schema.yaml"                                1 schema_gone
run_case "a schema that parses to nothing" "no required: keys parsed"                    1 schema_empty
run_case "a value no schema allows"     "does not list among its legal values"           1 bad_basis_value
run_case "a values: block emptied"      "a values: block that parses to nothing"         1 values_block_empty
run_case "authority beside governs on a concept" "beside a 'governs:'"                   1 claim_and_governs
run_case "a rule with no governs:"      "a rule with no 'governs:'"                      1 rule_no_governs
run_case "governs: as a YAML block list" "is written as a YAML block list"                1 rule_block_governs
# THE POINT IS THE DIAGNOSIS, NOT THE COLOUR. The block form was already red - `nogoverns` fired
# because the scalar is empty - so a case asserting only that it goes red would have passed before
# this verdict existed and proved nothing. What is new is that it stops being reported as a missing
# field, and that is what this case pins.
run_case_absent "the block form is not called a missing governs:" \
                "is written as a YAML block list" "a rule with no 'governs:'" 1 rule_block_governs
run_case "a rule claiming an authority" "beside a 'governs:'"                            1 rule_with_authority
run_case "a rule typed as a decision"   "type 'decision' disagrees with folder 'rules'"  1 rule_mistyped
run_case "the rules folder removed"     "missing directory"                              1 rules_folder_gone
run_case "a fence hides a marker"       "a code fence is opened and never closed"        1 region_blinded
run_case "a region at the wrong address" "which governs"                                  1 region_stray
run_case "a region outside a governs: list" "which governs"                              1 governs_list_stray

section "--- the rendering agrees with the page ---"
run_case "a hand edit to a region"      "does not carry what"                            1 inject_disagrees
run_case "a region with a trailing blank line" "does not carry what"                     1 region_trailing_blank
run_case "a rule with nowhere to render" "carries no region for it"                      1 rule_page
run_case "a rule that ships nothing"    "no <!-- text --> slice"                         1 inject_no_slice
run_case "a slice never closed"         "a text slice is opened and never closed"        1 inject_slice_open
run_case "two slices on one page"       "two text slices"                                1 inject_two_slices
run_case "an empty slice"               "an empty text slice"                            1 inject_empty_slice
run_case "governs names no file"        "which is not a file"                            1 inject_governs_air
run_case "governs written vault-relative" "the path is written from the repository root"  1 inject_vault_relative
run_case "the injector is gone"         "rule 12 asks its question by running it"        1 inject_no_script
run_case_absent "a deprecated rule does not render" "still in wiki/" "carries no region for it" 1 inject_deprecated
run_inject_case "the injector refuses a status it does not know" "is neither current nor deprecated" 1 inject_bad_status
run_case "decided_by names a page that is not a decision" "decided_by names" 1 decided_by_entity
run_case "a rule page with no decided_by" "missing frontmatter field 'decided_by'" 1 rule_no_decided_by
run_clean "decided_by names a real decision" decided_by_decision

# THE `idea` / `decided_by:` PAIR, AND IT IS NARROWED - owner, 2026-08-24. A page carrying
# `status: idea` while naming the decision that caused it is a contradiction in the ordinary case:
# an idea is a half-thought nobody ruled on. But `deferral` is a decision too, and this store has
# twenty-four of them - deferring something and writing down what you would build is the ordinary
# shape here, not the corner. So a deferral is exempt, and the half-thought that was deferred stays
# an idea. The objection this answers is written into `wiki/proposals/_schema.yaml` in the session's
# own words, where it has stood as the thing the build has to answer.
#
# TWO CASES BECAUSE ONE WOULD PROVE HALF OF IT. A verdict that never fires passes the second case,
# and a verdict that fires on everything passes the first.
run_case  "an idea naming a decision that binds" "carries 'status: idea' and names" 1 idea_binds
run_clean "an idea naming a deferral keeps its status" idea_deferred
run_clean "an archived journal's wikilinks are not swept" archived_journal
run_case "an archived page's wikilinks are still swept" "a-slug-that-only-the-archive-probe-names" 1 archived_page

section "--- the index the admission rule is looked up in ---"
run_case "the lookup tool is gone"      "rule 13 asks its question by running it"        1 auth_no_tool
run_case "a register row nothing answers" "is grouped in the register and no page carries it" 1 auth_stale
# THE PAIR. Without the second line, a `--check` that stopped looking for stale rows altogether
# would pass the first - and the repeal of 2026-08-29 is exactly a change to where it looks, so the
# two directions have to be pinned apart. A row is stale when NO page anywhere carries the slug; a
# row whose page has been archived is a live row about a retired page.
run_clean "a register row whose page has been archived is not stale" auth_archived_row
run_case "one slug in two families"     "is in more than one group"                      1 auth_two_homes
run_case "the register is gone"         "missing file"                                   1 auth_no_register
run_case "a page with no authority"     "missing frontmatter field 'authority'"          1 auth_stripped

# THE TOOL'S OWN ARGUMENT HANDLING, ADDED 2026-08-22 AND NOT ABOUT RULE 13. Every case above asks
# what the gate says when the tool reports something; this asks whether the tool ran what it was
# asked to run. It dispatched on `case "${1:-...}"`, so `--check --binding` ran the check, DROPPED
# `--binding` without a word, and exited 0 with a report that looked whole. That became urgent the
# moment `bash scripts/vault-authority.sh --check --binding` was named as the command an acceptance
# criterion is decided by: the criterion was undecidable for as long as it had existed, and nothing
# said so. Both halves are asserted, because a case naming one would pass on a tool that ran only
# that one.
# A RUNNER RATHER THAN TWO BARE SUBSHELLS, AND THE FIRST ATTEMPT HERE WAS THE DEFECT IT TESTS.
# Written as `( ... ) &` calling `report` directly, both cases ran and neither was ever counted:
# `next_rf` increments in the SUBSHELL, so the parent's case number never moved, the collector
# iterated past their report files, and the suite printed `caught 156, missed 0` while silently
# dropping two cases. The arithmetic is what caught it - eight added, six counted. Every runner
# above allocates in the parent and hands `RF` in, and this one does too.
run_tool_case() {     # <name> <exit> <must appear>... -- <arg>...
  local case_name="$1" want_code="$2"; shift 2
  local expect=() ; while [ "$1" != "--" ]; do expect+=("$1"); shift; done; shift
  wanted "$case_name" || return 0; local rf="$RF_NEXT"
  await_slot
  (
    RF="$rf"
    out=$(cd "$PRISTINE" && bash scripts/vault-authority.sh "$@" 2>&1); code=$?
    local ok=1 e
    [ "$code" = "$want_code" ] || ok=0
    for e in "${expect[@]}"; do grep -qF "$e" <<<"$out" || ok=0; done
    if [ "$ok" = 1 ]; then report "$case_name" yes ""
    else report "$case_name" no "exit=$code (wanted $want_code)
$out"; fi
  ) &
}
run_tool_case "two argumentless modes both run" 0 \
              'the register and the tree agree' 'prohibition' -- --check --binding
# AND AN UNKNOWN ARGUMENT AFTER A GOOD ONE IS STILL REFUSED. A loop that runs what it recognises
# and shrugs at the rest is the same silent-drop defect wearing a different hat.
run_tool_case "an unknown argument after a good one is refused" 2 \
              'unknown argument' -- --check --banana

# --- the marker carries a type, and `governs:` is read as a field ------------------------------
run_case "an unknown type word"        "not a marker alone on its line"             1 marker_unknown_type
run_case "a marker naming the wrong type" "so the marker names the wrong type"      1 marker_wrong_type
run_case "a slice with no governs:"    "slice on a page with no 'governs:'"         1 slice_without_governs
run_case "a wikilink in the slice"     "a wikilink in the text slice"               1 slice_wikilink

section "--- and what must NOT fail ---"
run_clean "a region with its page behind it" region_resolves
run_clean "a marker inside a fence"          region_in_a_fence
run_clean "a marker inside a code span"      region_in_a_span
run_clean "two rules, two destinations"       regions_two_files
run_clean "one rule, two destinations"        governs_list_both
run_clean "a one-element governs: list"       governs_list_one
run_clean "two rules, one file, two regions" two_rules_one_file
# WAS `run_clean` UNTIL 2026-08-21, AND THE FLIP IS THE RULING. A `concepts/` page carrying
# `governs:` was legal and rendered; the owner ruled that a page which renders is a rule, so the
# field left that folder's schema and this input is refused. The case keeps its subject and
# reverses its verdict rather than being deleted - a case removed leaves nothing asserting that
# the thing it tested is now impossible ([[governs-is-a-property-of-wiki-rules-alone]]).
run_case "a concept page carrying governs" "is in neither the required nor the optional list" 1 concept_renders
run_case_absent "a concept page that renders and names no mode" \
                "no 'render:' and this page renders" "is neither region nor whole" 1 concept_no_render
run_case "a render value no schema allows" "does not list among its legal values" 1 bad_render_value
run_clean "a wikilink inside a code span"    slice_wikilink_span
run_render "a fence inside a slice survives" fence_in_slice "$PROBE" "uv run pytest -q"
# The count left this assertion when the first rule migrated. It used to read `cover 1 of`, and
# that number is baseline-marked-files plus the one this mutation marks - so it moves every time
# a rule migrates, and a test carrying a number that drifts is how this suite has already lost
# cases. What the case is actually for is that coverage PRINTS and does not fail, and that the
# file it just marked stopped being counted as unmarked, which is the stronger claim and a
# stable one.
run_case_absent "coverage prints without failing" "advisory: a region or whole generation covers" "$PROBE" 0 region_resolves

section "--- the whole delivery mode ---"
run_case "a whole file not generated yet" "does not exist and"                            1 whole_ungenerated
run_case "a hand edit to a generated file" "does not carry what"                          1 whole_hand_edited
run_case "render: whole with no paths:"   "no 'paths:'"                                   1 whole_no_paths
# The other half of that verdict, and it is the half that decays silently. The refusal above was
# written as one pattern and matched none of the destinations it was meant to guard, because
# `governs:` is a path from the repository root and arrives with nothing in front of it - the
# refusal stopped firing and only this pairing would have shown it.
run_render "a rule generated outside .claude/rules/ needs no paths:" whole_outside_rules \
           ".claude/hooks/messages/whole-rule.md" "Never run the suite against the production database."
run_case "a generated file left by a deprecated page" "no longer current"                 1 whole_deprecated
run_case "a generated file whose page is gone" "carries the generated-marker"             1 whole_leftover
# The one shape the deleting branch must NEVER take. A file in the same directory carrying no
# marker is somebody's own rule: the store may not know about it and still has no standing to
# remove it, which is why deletion keys on the marker and not on the absence of a page.
run_render "an unmarked file is never removed" whole_keeps_unmarked \
           ".claude/rules/hand-written.md" "HAND-WRITTEN-AND-UNTOUCHED"

section "--- the gate says nothing on stderr ---"

# THE CASE THAT WOULD HAVE CAUGHT AN HOUR OF 2026-08-30. Comments added inside the embedded awk
# program pushed it past the per-argument size limit; `xargs` said so ON STDERR, the frontmatter
# pass produced NOTHING, and the gate went on exiting 0 with one misleading symptom - every
# registered tag reported as used on no page. Every red verdict in this suite would have passed by
# default in that state, which is exactly the failure this suite exists to make impossible.
#
# IT ASSERTS THE CHANNEL AND NOT A MESSAGE. Anything this script writes to stderr is a tool it
# shells out to complaining, and there is no case where that is expected: the gate reports through
# `note` on stdout and through its exit code. So the assertion is emptiness, which needs no list to
# be kept up to date and catches the next tool as well as this one.
stderrwork="$SANDBOX/stderrwork"
rm -rf "$stderrwork"; cp -r "$PRISTINE" "$stderrwork"
stderrout=$(cd "$stderrwork" && bash scripts/vault-check.sh 2>&1 >/dev/null)
[ -z "$stderrout" ] \
  && report "the gate writes nothing to stderr" yes "" \
  || report "the gate writes nothing to stderr" no "stderr was not empty:
$stderrout"

section "--- the lookup delivery mode ---"

# THE THIRD `render:` VALUE, minted 2026-08-30. `region` writes a slice into a file with a life of
# its own; `whole` owns a file end to end; `authority` writes NOWHERE. The rule is found by a hook
# that matches its `authority:` slug against the file being touched, which is how a prohibition
# reaches a reader once `wiki/decisions/` has been drained into the archive.
#
# THE MODE HAD TO COST SOMETHING OR IT WOULD BE A PER-PAGE WAIVER. It switches `nogoverns` off, and
# this store has refused a field whose only job was to silence a check. So it carries two
# obligations of its own, and the two reds below are them: the destination it does not use must be
# absent, and the slug it IS looked up by must be present. Each names an edit that turns it green.
run_clean "a rule delivered by lookup"      lookup_rule_clean
run_case  "lookup mode beside a governs:"   "beside a 'governs:'"                          1 lookup_rule_governs
run_case  "lookup mode with no slug"        "with no 'authority:'"                         1 lookup_rule_no_slug

# AND THE HALF THAT IS NOT A NEW VERDICT AT ALL. Rule 3 compared `authority:` across the whole
# corpus until 2026-08-30 and now compares within a type. The green is the point of the change: a
# concept and an entity answering one question share the slug deliberately, so a reader greps one
# string and gets the whole chain. The red is what survives it - two pages of ONE type still may
# not both claim to be the sole answer.
run_clean "one slug across two types"       authority_across_types

section "--- the catalogue generator ---"

# Two cases used to live here: a hand-edited catalogue is stale, and the catalogue does not
# rescue an orphan. Both are gone with rule 9. `catalogue.md` no longer exists - the list of
# every page is `pages.base`, which Obsidian evaluates and no script can - so there is nothing
# to be stale and nothing that could join the link register and defeat the orphan rule. The
# orphan rule keeps its own case, `orphan page`, which never depended on the catalogue.
#
# ONE CASE SURVIVES, and it is new. The generator is still how an agent answers "what is there
# at all" in a single command, and with rule 9 retired nothing else runs it: an untested
# generator that prints nothing would look exactly like a corpus with nothing in it.
catwork="$SANDBOX/catwork"
rm -rf "$catwork"; cp -r "$PRISTINE" "$catwork"
cat > "$catwork/$VAULT_DIR/wiki/concepts/a-page-the-generator-must-list.md" <<'PAGE'
---
title: "A page the generator must list"
type: concept
status: current
basis: inference
sprint: S2
created: 2026-08-17
sources: ["scripts/vault-catalogue.sh"]
tags: [vault]
---

# A page the generator must list

Planted by the selftest. It is never linked from anywhere, because what is under test is the
generator rather than the check - this copy is not run through `vault-check.sh` at all.
PAGE
out=$(cd "$catwork" && bash scripts/vault-catalogue.sh 2>&1); code=$?
{ grep -q 'a-page-the-generator-must-list' <<<"$out" && [ "$code" = "0" ]; } \
  && report "the generator lists a new page" yes "" \
  || report "the generator lists a new page" no "exit=$code
$out"

section "--- the archive script ---"

# WHY THIS EXISTS, AND IT IS DATED 2026-08-21 BECAUSE THE DEFECT SHIPPED FIRST. `vault-archive.sh`
# had no case anywhere. It was built, it was run once on `probe/RUNBOOK.md` - a file OUTSIDE the
# vault - and that single run was the whole of its evidence. On the first file INSIDE the vault, the
# ingest's own journal, it reported `cited by 0 page(s)` about a file nine pages cited, rewrote
# nothing, and left the gate red: the argument is a path from the repository root while a `sources:`
# citation inside the vault is VAULT-relative, and the script used one string for both. The two
# forms coincide outside the vault, so no amount of running it on that cargo could ever have shown
# it. This case is the fixture that would have.
#
# THE EXIT CODE IS NOT THE VERDICT HERE, deliberately. The script ends by running `vault-check.sh`
# and exiting with its code, so a sandbox that is red for an unrelated reason would fail this case
# with the wrong diagnosis - the defect this suite has already been bitten by twice. What is under
# test is the move, the sidecar and the rewrite, so the verdict is read off the output and the tree.
arcwork="$SANDBOX/arcwork"
rm -rf "$arcwork"; cp -r "$PRISTINE" "$arcwork"
mkdir -p "$arcwork/$VAULT_DIR/raw/handoffs"
printf -- '---\nsession: 2026-08-21\n---\n\n# A journal the archive must move\n' \
  > "$arcwork/$VAULT_DIR/raw/handoffs/2026-08-21-archive-probe.md"
printf '5\tpage:a-page-that-cites-the-archived-journal\n' \
  > "$arcwork/$VAULT_DIR/raw/handoffs/2026-08-21-archive-probe.coverage.tsv"
# TWO ENTRIES ON THE `sources:` LINE, AND THE SECOND ONE IS THE POINT. A rewrite that took the whole
# line, or that matched a path as a pattern, would take the neighbour with it. This corpus has
# already had a sweep make one sentence say the opposite of what it meant.
cat > "$arcwork/$VAULT_DIR/wiki/concepts/a-page-that-cites-the-archived-journal.md" <<'PAGE'
---
title: "A page that cites the archived journal"
type: concept
status: current
authority: archive-probe-citation
basis: inference
sprint: S2
created: 2026-08-21
sources: ["raw/handoffs/2026-08-21-archive-probe.md", "scripts/vault-archive.sh"]
tags: [vault]
---

# A page that cites the archived journal

Planted by the selftest. What is under test is `vault-archive.sh`, not the gate.
PAGE
out=$(cd "$arcwork" && bash scripts/vault-archive.sh 2026-08-21 a-probe-session handoffs \
        "$VAULT_DIR/raw/handoffs/2026-08-21-archive-probe.md" 2>&1)
arcdest="$arcwork/$VAULT_DIR/archive/2026-08-21/a-probe-session/handoffs"
arcsrc=$(grep '^sources:' "$arcwork/$VAULT_DIR/wiki/concepts/a-page-that-cites-the-archived-journal.md")

grep -q 'cited by 1 page(s): raw/handoffs/2026-08-21-archive-probe.md' <<<"$out" \
  && report "the citation is counted in its vault-relative form" yes "" \
  || report "the citation is counted in its vault-relative form" no "$out"

[ -f "$arcdest/2026-08-21-archive-probe.coverage.tsv" ] \
  && [ ! -e "$arcwork/$VAULT_DIR/raw/handoffs/2026-08-21-archive-probe.coverage.tsv" ] \
  && report "the sidecar rides with its source" yes "" \
  || report "the sidecar rides with its source" no "$out"

{ grep -q 'archive/2026-08-21/a-probe-session/handoffs/2026-08-21-archive-probe.md' <<<"$arcsrc" \
  && grep -q 'scripts/vault-archive.sh' <<<"$arcsrc"; } \
  && report "the citation is rewritten and its neighbour is not" yes "" \
  || report "the citation is rewritten and its neighbour is not" no "$arcsrc"

# `superseded_by:` WAS ADDED TO THIS FIXTURE ON 2026-08-29, AND IT WAS ALWAYS OWED. The vault's
# supersession rule is three steps - write the successor, mark the old page `deprecated` AND name
# the successor in `superseded_by:`, then move it - so a deprecated page without that field was
# never a legal page and this fixture was planting one. It passed because nothing read the field.
# The successor check ordered on 2026-08-29 reads it, and the fixture went red rather than the check
# being wrong: the case tests the `pages` kind, not the corpus's tolerance for a half-retired page.
#
# THE `pages` KIND, ADDED 2026-08-22, AND ITS CASE IS WRITTEN IN BOTH DIRECTIONS BECAUSE A KIND
# LIST IS EXACTLY THE SHAPE THAT FAILS TOWARDS ACCEPTANCE. A `case` arm that matched too widely
# would take any string, and the only symptom would be a file in a folder nobody looks in. So one
# case proves `pages` is accepted and lands where the archive decision says, and one proves an
# unknown kind is still refused with the message naming all five.
#
# AND IT IS THE FIRST KIND THAT DOES NOT COME FROM `raw/`. The cargo here is a retired wiki page,
# which is what made the citation rewrite worth proving again: a wiki page is cited by `[[wikilink]]`
# far more often than by `sources:`, and only the `sources:` half is this script's business.
arcpage="$SANDBOX/arcpage"
rm -rf "$arcpage"; cp -r "$PRISTINE" "$arcpage"
cat > "$arcpage/$VAULT_DIR/wiki/decisions/a-decision-that-gets-retired.md" <<'PAGE'
---
title: "A decision that gets retired"
type: decision
status: deprecated
authority: retired-probe-decision
binding: prohibition
basis: inference
sprint: S2
decided: 2026-08-21
created: 2026-08-21
superseded_by: [[a-page-that-cites-the-retired-decision]]
sources: ["raw/handoffs/2026-08-21-a-journal.md"]
tags: [vault]
---

# A decision that gets retired

Planted by the selftest. What is under test is the `pages` kind of `vault-archive.sh`.
PAGE
cat > "$arcpage/$VAULT_DIR/wiki/concepts/a-page-that-cites-the-retired-decision.md" <<'PAGE'
---
title: "A page that cites the retired decision"
type: concept
status: current
authority: retired-probe-citation
basis: inference
sprint: S2
created: 2026-08-21
sources: ["wiki/decisions/a-decision-that-gets-retired.md", "scripts/vault-archive.sh"]
tags: [vault]
---

# A page that cites the retired decision

Planted by the selftest.
PAGE
out=$(cd "$arcpage" && bash scripts/vault-archive.sh 2026-08-22 2026-08-22-a-probe-session pages \
        "$VAULT_DIR/wiki/decisions/a-decision-that-gets-retired.md" 2>&1)
pagedest="$arcpage/$VAULT_DIR/archive/2026-08-22/2026-08-22-a-probe-session/pages"
pagesrc=$(grep '^sources:' "$arcpage/$VAULT_DIR/wiki/concepts/a-page-that-cites-the-retired-decision.md")

{ [ -f "$pagedest/a-decision-that-gets-retired.md" ] \
  && [ ! -e "$arcpage/$VAULT_DIR/wiki/decisions/a-decision-that-gets-retired.md" ]; } \
  && report "a retired page moves into the dated archive under pages" yes "" \
  || report "a retired page moves into the dated archive under pages" no "$out"

{ grep -q 'archive/2026-08-22/2026-08-22-a-probe-session/pages/a-decision-that-gets-retired.md' <<<"$pagesrc" \
  && grep -q 'scripts/vault-archive.sh' <<<"$pagesrc"; } \
  && report "the retired page's citation is rewritten and its neighbour is not" yes "" \
  || report "the retired page's citation is rewritten and its neighbour is not" no "$pagesrc"

out=$(cd "$arcpage" && bash scripts/vault-archive.sh 2026-08-22 2026-08-22-a-probe-session logs \
        "$VAULT_DIR/wiki/concepts/a-page-that-cites-the-retired-decision.md" 2>&1); code=$?
{ [ "$code" -eq 2 ] && grep -q 'kind must be one of handoffs plans specs notes pages' <<<"$out"; } \
  && report "an unknown kind is still refused, and the message names all five" yes "" \
  || report "an unknown kind is still refused, and the message names all five" no "exit=$code
$out"

# THE PRECONDITION, ADDED 2026-08-23 AND CASED 2026-08-23. Under `pages` the script refuses with
# exit 2 unless a live page under `wiki/` names the slug, because nothing in `archive/` is checked,
# swept or read by `/pre-task` - so a page nothing points at has left the store rather than been
# filed in it. The positive direction is the two `pages` cases above, whose cargo IS cited; this is
# the negative one, and a precondition with only the passing direction cased is a precondition that
# can be deleted without anything going red.
#
# THE FIXTURE IS READ BACK BEFORE IT IS USED. A planted offender that did not plant makes a case
# report nothing at all and read as a pass, which this suite has already been bitten by: the guard
# below asserts both that the file exists and that NO other page names its slug, because the second
# is the property under test and it is the one an unlucky slug choice would silently destroy.
arcorphan="$SANDBOX/arcorphan"
rm -rf "$arcorphan"; cp -r "$PRISTINE" "$arcorphan"
orphan_slug=a-proposal-no-live-page-names
cat > "$arcorphan/$VAULT_DIR/wiki/proposals/$orphan_slug.md" <<'PAGE'
---
title: "A proposal no live page names"
type: proposal
status: current
authority: uncited-archive-probe
basis: inference
sprint: S3
created: 2026-08-23
sources: ["scripts/vault-archive.sh"]
tags: [vault]
---

# A proposal no live page names

Planted by the selftest. Nothing under wiki/ names this slug, and that is the whole fixture.
PAGE
orphan_holders=$(grep -rlF --include='*.md' -- "$orphan_slug" "$arcorphan/$VAULT_DIR/wiki" 2>/dev/null \
                 | grep -cv "/$orphan_slug.md$")
if [ ! -f "$arcorphan/$VAULT_DIR/wiki/proposals/$orphan_slug.md" ] || [ "$orphan_holders" -ne 0 ]; then
  report "the uncited fixture is an orphan before the script runs" no \
    "planted=$([ -f "$arcorphan/$VAULT_DIR/wiki/proposals/$orphan_slug.md" ] && echo yes || echo no), other pages naming the slug=$orphan_holders"
else
  report "the uncited fixture is an orphan before the script runs" yes ""
fi

out=$(cd "$arcorphan" && bash scripts/vault-archive.sh 2026-08-23 2026-08-23-a-probe-session pages \
        "$VAULT_DIR/wiki/proposals/$orphan_slug.md" 2>&1); code=$?
{ [ "$code" -eq 2 ] \
  && grep -q "no live page under" <<<"$out" \
  && [ -f "$arcorphan/$VAULT_DIR/wiki/proposals/$orphan_slug.md" ] \
  && [ ! -e "$arcorphan/$VAULT_DIR/archive/2026-08-23/2026-08-23-a-probe-session/pages/$orphan_slug.md" ]; } \
  && report "a page no live page names is refused the archive, and is left where it was" yes "" \
  || report "a page no live page names is refused the archive, and is left where it was" no "exit=$code (wanted 2)
$out"

# THE REFUSED PRECONDITION, ADDED 2026-08-23. A refused proposal names the decision that refused
# it, and this script is the only place that can check it: the rule applies to a page ON ITS WAY
# OUT of `wiki/`, and `vault-check.sh` reads `wiki/` alone - a verdict written there could never
# fire. It is also a CONDITIONAL requirement, which a per-folder schema cannot express.
#
# CASED IN BOTH DIRECTIONS IN ONE SANDBOX. The refusal direction is what goes red if the
# precondition is deleted; the passing direction is what goes red if it starts refusing everything.
# The fixture also carries a citing page, without which the FIRST precondition fires and this case
# would pass for that reason instead - which is the defect this suite has already shipped twice.
arcref="$SANDBOX/arcref"
rm -rf "$arcref"; cp -r "$PRISTINE" "$arcref"
refslug=a-refused-probe-proposal
cat > "$arcref/$VAULT_DIR/wiki/proposals/$refslug.md" <<'PAGE'
---
title: "A refused probe proposal"
type: proposal
status: refused
authority: refused-archive-probe
basis: inference
sprint: S3
created: 2026-08-23
sources: ["scripts/vault-archive.sh"]
tags: [vault, harness]
---

# A refused probe proposal

Planted by the selftest. What is under test is the refused precondition of `vault-archive.sh`.
PAGE
cat > "$arcref/$VAULT_DIR/wiki/concepts/a-page-that-names-the-refused-probe.md" <<'PAGE'
---
title: "A page that names the refused probe"
type: concept
status: current
authority: refused-archive-probe-citation
basis: inference
sprint: S3
created: 2026-08-23
sources: ["wiki/proposals/a-refused-probe-proposal.md", "scripts/vault-archive.sh"]
tags: [vault, harness]
---

# A page that names the refused probe

It names a-refused-probe-proposal, so the citation precondition passes and the next one is reached.
PAGE
out=$(cd "$arcref" && bash scripts/vault-archive.sh 2026-08-23 2026-08-23-a-probe-session pages \
        "$VAULT_DIR/wiki/proposals/$refslug.md" 2>&1); code=$?
{ [ "$code" -eq 2 ] \
  && grep -q "and no 'decided_by:'" <<<"$out" \
  && [ -f "$arcref/$VAULT_DIR/wiki/proposals/$refslug.md" ]; } \
  && report "a refused proposal with no decided_by is refused the archive" yes "" \
  || report "a refused proposal with no decided_by is refused the archive" no "exit=$code (wanted 2)
$out"

sed -i '/^tags:/i decided_by: [[a-refused-proposal-is-archived-and-takes-status-refused]]' \
  "$arcref/$VAULT_DIR/wiki/proposals/$refslug.md"
out=$(cd "$arcref" && bash scripts/vault-archive.sh 2026-08-23 2026-08-23-a-probe-session pages \
        "$VAULT_DIR/wiki/proposals/$refslug.md" 2>&1)
grep -q "and no 'decided_by:'" <<<"$out" \
  && report "the same page carrying decided_by is not refused for that reason" no "the precondition fired anyway
$out" \
  || report "the same page carrying decided_by is not refused for that reason" yes ""

# THE SWEEP RUNS AGAINST A TINY VAULT OF ITS OWN AND NOT AGAINST `$PRISTINE`, and that is a cost
# decision rather than a preference. A sweep over the real corpus selects about 240 pages and takes
# three minutes; seven cases of that is twenty-one minutes added to a suite that already costs
# thirty-four. The tiny vault holds one page per branch and the whole block runs in seconds.
#
# THE GATE AT THE END OF THE SCRIPT WILL BE RED HERE, and it does not matter. A six-page vault has
# no registers, no schemas and no rule pages, so `vault-check.sh` has plenty to complain about. This
# section already reads its verdicts off the OUTPUT AND THE TREE rather than off the exit code, for
# exactly the reason written at the top of it, and the sweep cases inherit that.
#
# WHAT CANNOT BE PROVED ON THE REAL CORPUS AT ALL: the refusal. Measured 2026-08-29, the sweep's
# first run over the live tree selects 239 pages and refuses NONE - every selected page already has
# a live holder, and for the `decided_by:` criterion that is true by construction. So the case below
# that plants a refusal is the only evidence the continue-past-a-refusal branch will ever have.
arcsweep="$SANDBOX/arcsweep"
rm -rf "$arcsweep"; mkdir -p "$arcsweep/scripts" "$arcsweep/tinyvault/wiki"
cp "$PRISTINE/scripts/vault-archive.sh" "$PRISTINE/scripts/vault-check.sh" "$arcsweep/scripts/"
for d in decisions lessons proposals rules entities concepts; do
  mkdir -p "$arcsweep/tinyvault/wiki/$d"
done

sweep_page() {        # sweep_page <folder> <slug> <type> <status> <extra frontmatter line>
  { printf -- '---\ntitle: "%s"\ntype: %s\nstatus: %s\nauthority: %s\n' "$2" "$3" "$4" "$2"
    printf 'basis: inference\nsprint: S3\ncreated: 2026-08-29\n'
    [ -n "${5:-}" ] && printf '%s\n' "$5"
    printf 'sources: ["scripts/vault-archive.sh"]\ntags: [vault]\n---\n\n# %s\n\nPlanted by the selftest.\n' "$2"
  } > "$arcsweep/tinyvault/wiki/$1/$2.md"
}

# Two implemented proposals. Only ONE of them is named by a live page, so the other is refused by
# the holder precondition - which is what makes this a test of continuing rather than of moving.
sweep_page proposals implemented-and-held    proposal implemented ""
sweep_page proposals implemented-and-orphan  proposal implemented ""
sweep_page proposals a-current-proposal      proposal current     ""
sweep_page lessons   a-lesson-held-outside   lesson   current     ""
sweep_page lessons   a-lesson-held-by-lessons lesson  current     ""
sweep_page lessons   the-lesson-that-holds   lesson   current     ""
sweep_page decisions a-deprecated-decision   decision deprecated  "binding: prohibition
superseded_by: [[a-successor-that-does-not-exist]]"

# The holder names two slugs and deliberately does NOT name `implemented-and-orphan`.
{ printf -- '---\ntitle: "the-holder"\ntype: concept\nstatus: current\nauthority: the-holder\n'
  printf 'basis: inference\nsprint: S3\ncreated: 2026-08-29\nsources: ["scripts/vault-archive.sh"]\ntags: [vault]\n---\n\n'
  # THE DEPRECATED DECISION IS NAMED HERE ON PURPOSE. Without a holder it is refused by the earlier
  # precondition and never reaches the successor check, so the case that exists to prove the
  # successor check would have been proving the holder check under a misleading name.
  printf '# the-holder\n\nIt names [[implemented-and-held]], [[a-lesson-held-outside]] and [[a-deprecated-decision]].\n'
} > "$arcsweep/tinyvault/wiki/concepts/the-holder.md"

# A lesson naming another lesson, and nothing outside lessons/ names it. The lessons criterion asks
# for a citation from OUTSIDE the folder, so this one must not be selected at all.
{ printf -- '---\ntitle: "the-lesson-that-holds"\ntype: lesson\nstatus: current\nauthority: the-lesson-that-holds\n'
  printf 'basis: inference\nsprint: S3\ncreated: 2026-08-29\nsources: ["scripts/vault-archive.sh"]\ntags: [vault]\n---\n\n'
  printf '# the-lesson-that-holds\n\nIt names [[a-lesson-held-by-lessons]] and nothing else does.\n'
} > "$arcsweep/tinyvault/wiki/lessons/the-lesson-that-holds.md"

sweepdry=$(cd "$arcsweep" && bash scripts/vault-archive.sh --dry-run --sweep 2026-08-29 a-sweep-session 2>&1)
[ -f "$arcsweep/tinyvault/wiki/proposals/implemented-and-held.md" ] \
  && grep -q 'nothing moved and nothing rewritten' <<<"$sweepdry" \
  && report "a dry sweep names its list and moves nothing" yes "" \
  || report "a dry sweep names its list and moves nothing" no "$sweepdry"

sweepout=$(cd "$arcsweep" && bash scripts/vault-archive.sh --sweep 2026-08-29 a-sweep-session 2>&1)
sweepcode=$?
sweepdest="$arcsweep/tinyvault/archive/2026-08-29/a-sweep-session/pages"

[ -f "$sweepdest/implemented-and-held.md" ] \
  && [ ! -e "$arcsweep/tinyvault/wiki/proposals/implemented-and-held.md" ] \
  && report "the sweep moves an implemented proposal a live page names" yes "" \
  || report "the sweep moves an implemented proposal a live page names" no "$sweepout"

grep -q '^status: archived' "$sweepdest/implemented-and-held.md" 2>/dev/null \
  && report "the sweep writes status archived on what it moves" yes "" \
  || report "the sweep writes status archived on what it moves" no \
     "$(head -8 "$sweepdest/implemented-and-held.md" 2>/dev/null)"

# THE BRANCH THE REAL CORPUS CANNOT EXERCISE. The orphan is refused, and the page after it in the
# same folder still moves. A sweep that stopped at the first refusal would leave the held one behind
# and this case is the only thing that can tell the two apart.
{ [ -f "$arcsweep/tinyvault/wiki/proposals/implemented-and-orphan.md" ] \
  && [ -f "$sweepdest/implemented-and-held.md" ] \
  && grep -q 'REFUSED' <<<"$sweepout"; } \
  && report "the sweep continues past a refusal and moves the page after it" yes "" \
  || report "the sweep continues past a refusal and moves the page after it" no "$sweepout"

[ "$sweepcode" -ne 0 ] \
  && report "a sweep with a refusal in it exits non-zero" yes "" \
  || report "a sweep with a refusal in it exits non-zero" no "exit=$sweepcode"

[ -f "$arcsweep/tinyvault/wiki/proposals/a-current-proposal.md" ] \
  && report "a page no criterion selects is left where it was" yes "" \
  || report "a page no criterion selects is left where it was" no "$sweepout"

[ -f "$arcsweep/tinyvault/wiki/lessons/a-lesson-held-by-lessons.md" ] \
  && [ ! -e "$arcsweep/tinyvault/wiki/lessons/a-lesson-held-outside.md" ] \
  && report "a lesson leaves on an outside citation and stays on an inside one" yes "" \
  || report "a lesson leaves on an outside citation and stays on an inside one" no "$sweepout"

# `deprecated` IS THE ONE STATUS THAT OBLIGES A PAGE TO LEAVE, and the successor check is what stops
# it leaving into nothing. This page names a successor that was never written.
{ [ -f "$arcsweep/tinyvault/wiki/decisions/a-deprecated-decision.md" ] \
  && grep -q 'a-successor-that-does-not-exist' <<<"$sweepout"; } \
  && report "a deprecated page whose successor is not live is refused" yes "" \
  || report "a deprecated page whose successor is not live is refused" no "$sweepout"

# THE REPEAL PRECONDITIONS, ADDED 2026-08-30. Three cases and they are three because the mechanism
# has three edges: a decision that may never leave, a cancelled page that owes its decision, and the
# same page once it has one. A refusal cased in one direction only can be deleted without anything
# going red, which is the defect this section already carries a note about.
#
# EACH FIXTURE IS CITED BEFORE IT IS USED. The FIRST precondition of `consider_page` is that a live
# page names the slug, so an uncited fixture would be refused for that reason instead and the case
# would pass while testing nothing - the failure this suite has shipped twice. The citing page is
# planted for each one and asserted before the script runs.
arcrep="$SANDBOX/arcrep"
rm -rf "$arcrep"; cp -r "$PRISTINE" "$arcrep"
repdec=a-repeal-decision-that-must-not-leave
cat > "$arcrep/$VAULT_DIR/wiki/decisions/$repdec.md" <<'PAGE'
---
title: "A repeal decision the archiver must refuse"
type: decision
status: current
authority: repeal-refusal-probe
basis: inference
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: repeal
target: a-rule-this-probe-cancelled
sources: ["scripts/vault-archive.sh"]
binding: prohibition
tags: [vault, harness]
---

# Context

Planted by the selftest.

# The question

Whether the archiver refuses to file the only live carrier of a cancellation.

# How it works after

The script exits 2 and the page stays in wiki/decisions/.

# Recommendation

None; this is a fixture.

# Ratification

None; this is a fixture.
PAGE
printf '\nCited by the selftest: [[%s]].\n' "$repdec" >> "$arcrep/$VAULT_DIR/index.md"
out=$(cd "$arcrep" && bash scripts/vault-archive.sh 2026-08-30 2026-08-30-a-probe-session pages \
        "$VAULT_DIR/wiki/decisions/$repdec.md" 2>&1); code=$?
{ [ "$code" -eq 2 ] \
  && grep -q "does not leave wiki/" <<<"$out" \
  && [ -f "$arcrep/$VAULT_DIR/wiki/decisions/$repdec.md" ]; } \
  && report "a target_kind: repeal decision is refused the archive" yes "" \
  || report "a target_kind: repeal decision is refused the archive" no "exit=$code (wanted 2)
$out"

# THE CANCELLED PAGE, IN BOTH DIRECTIONS AND IN ONE SANDBOX. `status: repealed` is legal in
# `wiki/rules/` alone, and what it owes on the way out is `decided_by:` - never `superseded_by:`,
# which a cancellation is forbidden. The refusal direction is what goes red if the precondition is
# deleted; the passing direction is what goes red if it starts refusing everything.
arcrp2="$SANDBOX/arcrp2"
rm -rf "$arcrp2"; cp -r "$PRISTINE" "$arcrp2"
repruleslug=a-rule-this-probe-cancelled
write_repealed_rule() {   # write_repealed_rule <work> <decided_by line or empty>
  { printf -- '---\n'
    printf 'title: "A rule this probe cancelled"\n'
    printf 'type: rule\nstatus: repealed\ngoverns: CLAUDE.md\nrender: region\n'
    printf 'basis: inference\nsprint: S3\ncreated: 2026-08-30\n'
    printf 'sources: ["scripts/vault-archive.sh"]\n'
    [ -n "$2" ] && printf '%s\n' "$2"
    printf 'tags: [vault, harness]\n---\n\n'
    printf '# What travels\n\n<!-- text -->\nCancelled by the selftest.\n<!-- /text -->\n'
  } > "$1/$VAULT_DIR/wiki/rules/$repruleslug.md"
  #    THE CITER LIVES UNDER `wiki/` AND NAMES THE SLUG AS BARE TEXT. The holder test greps
  #    `$VAULT/wiki` and nothing else, so a citation in `index.md` - which is where the first
  #    draft of this fixture put it - satisfies nothing and the case fails on the FIRST
  #    precondition while claiming to test the third. And the mention is bare rather than a
  #    `[[wikilink]]`, because the page is about to move to `archive/` and a wikilink to it would
  #    then be swept as broken - proving the fixture wrong instead of the mechanism right.
  cat > "$1/$VAULT_DIR/wiki/concepts/a-page-that-names-the-cancelled-rule.md" <<'CITER'
---
title: "A page that names the cancelled rule"
type: concept
status: current
authority: repealed-archive-probe-citation
basis: inference
sprint: S3
created: 2026-08-30
sources: ["scripts/vault-archive.sh"]
tags: [vault, harness]
---

# A page that names the cancelled rule

It names a-rule-this-probe-cancelled as bare text, so the citation precondition passes and the
repeal precondition is the one under test.
CITER
}
write_repealed_rule "$arcrp2" ""
out=$(cd "$arcrp2" && bash scripts/vault-archive.sh 2026-08-30 2026-08-30-a-probe-session pages \
        "$VAULT_DIR/wiki/rules/$repruleslug.md" 2>&1); code=$?
{ [ "$code" -eq 2 ] \
  && grep -q "names no 'decided_by:'" <<<"$out" \
  && [ -f "$arcrp2/$VAULT_DIR/wiki/rules/$repruleslug.md" ]; } \
  && report "a repealed page with no decided_by: is refused" yes "" \
  || report "a repealed page with no decided_by: is refused" no "exit=$code (wanted 2)
$out"

# AND THE SAME PAGE ONCE IT NAMES ITS DECISION. The verdict is read off the TREE and not off the
# exit code: this script ends by running the gate, and a sandbox red for an unrelated reason would
# fail this case with the wrong diagnosis - which is what the note at the head of this section is
# about. What is under test is that the move happened WITHOUT a `superseded_by:`, which the
# deprecated route would have refused.
arcrp3="$SANDBOX/arcrp3"
rm -rf "$arcrp3"; cp -r "$PRISTINE" "$arcrp3"
write_repealed_rule "$arcrp3" 'decided_by: [[a-decision-that-cancelled-it]]'
out=$(cd "$arcrp3" && bash scripts/vault-archive.sh 2026-08-30 2026-08-30-a-probe-session pages \
        "$VAULT_DIR/wiki/rules/$repruleslug.md" 2>&1)
{ [ ! -e "$arcrp3/$VAULT_DIR/wiki/rules/$repruleslug.md" ] \
  && [ -f "$arcrp3/$VAULT_DIR/archive/2026-08-30/2026-08-30-a-probe-session/pages/$repruleslug.md" ] \
  && ! grep -q 'superseded_by' "$arcrp3/$VAULT_DIR/archive/2026-08-30/2026-08-30-a-probe-session/pages/$repruleslug.md"; } \
  && report "a repealed page naming its decision is released without a successor" yes "" \
  || report "a repealed page naming its decision is released without a successor" no "$out"

section "--- the rule register ---"

# THE REGISTER IS SWEPT AND NEVER STORED, and that is the whole of what these cases assert.
#
# Counting what `--rules` prints against the same headings it reads would be a tautology - green
# under any implementation, including one returning a list typed in by hand, which is the failure
# this register exists to end. So the heading is REMOVED from the script inside the sandbox and the
# register must lose that row while keeping its neighbours.
drop_rule_heading() { sed -i 's/^# 11\. Marked regions/# Marked regions/' "$1/scripts/vault-check.sh"; }
run_arg_case "the register loses a rule whose heading is gone" --rules \
             "rules:   12. Every current rule" "rules:   11. Marked regions" 0 drop_rule_heading

# AND THE OTHER DIRECTION, because a sweep that returned nothing at all would pass the case above
# by losing everything rather than by losing the one row.
run_arg_case "the register names a rule on an untouched script" --rules \
             "rules:   11. Marked regions" -- 0 --

# THE USAGE ERROR NAMES WHAT IS LEGAL, and there are two now. The prohibition that gave this script
# its own exit code obliges the message to say what the legal arguments are, and nothing pinned that
# sentence until this case: it still read "the only one is --lint" while `--rules` was being added,
# and no case anywhere would have turned over. The one `unknown argument` case this suite already
# had is over `vault-authority.sh`.
run_arg_case "an unknown argument exits 2 and names both legal flags" --nonsense \
             "the legal ones are --lint and --rules" -- 2 --

section "--- the measure regions ---"
run_case "the measure script is gone"   "rule 15 asks its question by running it"        1 measure_no_script
run_case "a measure line with no role"  "a measure line opens with its role"             1 measure_bad_region
run_case "a gauge written by hand"      "never written by hand"                          1 measure_hand_gauge
run_probe_case "a store stub first on PATH is skipped unrun" \
                                        "does not understand"                              plant_store_stub

section "--- units and coverage ---"
FIX="$SANDBOX/fixtures"; mkdir -p "$FIX"

printf 'Line one of a document with no blank lines whatsoever.\nLine two says something else.\nLine three is a third claim.\n## A heading\nAnd a fourth line under it.\n' > "$FIX/no-blanks.md"
u=$(cd "$PRISTINE" && bash scripts/vault-units.sh "$FIX/no-blanks.md" 2>&1); n=$(printf '%s\n' "$u" | grep -c 'prose')
[ "$n" -eq 4 ] && report "no blank lines: every line counts" yes "" \
                || report "no blank lines: every line counts" no "$n prose units
$u"

printf 'Intro paragraph.\n\n```bash\nnever closed\n\n## A heading nobody will see\n\nA claim that vanishes.\n' > "$FIX/unclosed.md"
u=$(cd "$PRISTINE" && bash scripts/vault-units.sh "$FIX/unclosed.md" 2>&1); c=$?
{ [ "$c" -eq 3 ] && printf '%s' "$u" | grep -q 'unclosed code fence'; } \
  && report "an unclosed fence is refused" yes "" \
  || report "an unclosed fence is refused" no "exit=$c
$u"

printf '# Title\nFlush against its heading.\n\n## Second\n\nSeparated by a blank line.\n' > "$FIX/under-heading.md"
u=$(cd "$PRISTINE" && bash scripts/vault-units.sh "$FIX/under-heading.md" 2>&1); n=$(printf '%s\n' "$u" | grep -c 'prose')
[ "$n" -eq 2 ] && report "a paragraph flush under a heading" yes "" \
               || report "a paragraph flush under a heading" no "$n prose units
$u"

printf 'Before.\n\n> 1. the first quoted claim\n> 2. the second quoted claim\n> - and a third\n\nAfter.\n' > "$FIX/quoted.md"
u=$(cd "$PRISTINE" && bash scripts/vault-units.sh "$FIX/quoted.md" 2>&1); n=$(printf '%s\n' "$u" | grep -c 'quoted')
[ "$n" -eq 3 ] && report "list items inside a blockquote" yes "" \
               || report "list items inside a blockquote" no "$n quoted units
$u"

cov_case() {          # cov_case <name> <sidecar body> <expected substring> <expected exit>
  local case_name="$1" body="$2" expect="$3" want="$4"
  wanted "$case_name" || return 0; local rf="$RF_NEXT" n="$case_no"
  await_slot
  (
    RF="$rf"; work="$SANDBOX/covwork.$n"
    rm -rf "$work"; cp -r "$PRISTINE" "$work"
    src="$work/$VAULT_DIR/raw/handoffs/probe.md"
    printf 'A first claim.\n\nA second claim.\n' > "$src"
    [ -n "$body" ] && printf '%s' "$body" > "$work/$VAULT_DIR/raw/handoffs/probe.coverage.tsv"
    out=$(cd "$work" && bash scripts/vault-coverage.sh "$VAULT_DIR/raw/handoffs/probe.md" 2>&1); code=$?
    if grep -qF "$expect" <<<"$out" && [ "$code" = "$want" ]; then
      report "$case_name" yes ""
    else
      report "$case_name" no "exit=$code (wanted $want)
$out"
    fi
    rm -rf "$work"
  ) &
}

cov_case "no sidecar is not a pass"    ""                          "evidence mode"     1
cov_case "a complete sidecar passes"   "$(printf '1\tjournal\n3\tjournal\n')"  "INGEST COMPLETE" 0
cov_case "a sidecar written with CRLF" "$(printf '1\tjournal\r\n3\tjournal\r\n')" "INGEST COMPLETE" 0
cov_case "an invented verdict"         "$(printf '1\tbanana\n3\tbanana\n')"    "is not one of"   1
cov_case "a page: that does not exist" "$(printf '1\tpage:no-such-page\n3\tjournal\n')" "does not exist in the wiki" 1
cov_case "a bad name after a good one" "$(printf '1\tpage:batch-lifecycle, no-such-page-at-all\n3\tjournal\n')" "no-such-page-at-all does not exist" 1
cov_case "a missing verdict"           "$(printf '1\tjournal\n')"              "INGEST UNFINISHED" 1

# NOTHING HAS PRINTED YET. Every verdict is a file numbered as it was DISPATCHED, so the report
# below reads in script order however the workers interleaved. `wait` is what makes the count
# honest: without it this loop reads a half-written directory and reports a green suite that had
# not finished - the same shape as counting in a variable a subshell owns.
wait

# A FILTER THAT SELECTED NOTHING IS A USAGE ERROR, NOT A GREEN RUN. It is checked here rather than
# in the report loop because nothing was proved either way: no case ran, so what the loop would
# print is the section headers and the baseline, and printing those before refusing reads as a
# result. The code is 2 because the gate reserves 2 for a usage error, and a sibling script that
# answered the same mistake with 1 would teach the opposite lesson at the same prompt.
if [ -n "$ONLY" ] && [ "$selected" -eq 0 ]; then
  echo
  echo "SELFTEST: --only '$ONLY' selected no case - $skipped skipped, 0 selected."
  echo "          It is a SUBSTRING of a case name or of a section name, never a regular"
  echo "          expression, so an alternation such as 'a|b' matches nothing at all."
  echo "          Run: bash scripts/vault-check-selftest.sh --list"
  exit 2
fi

pass=0; fail=0
for rf in "$RESULTS"/*; do
  [ -f "$rf" ] || continue
  case "$(head -1 "$rf")" in
    sec) printf '%s\n' "$(sed -n 2p "$rf")" ;;
    bas) printf 'BASELINE %-36s\n' "$(sed -n 2p "$rf")" ;;
    yes) printf 'CAUGHT   %-36s\n' "$(sed -n 2p "$rf")"; pass=$((pass + 1)) ;;
    brk) printf 'BROKEN   %-36s\n' "$(sed -n 2p "$rf")"; tail -n +3 "$rf"; fail=$((fail + 1)) ;;
    *)   printf 'MISSED   %-36s\n' "$(sed -n 2p "$rf")"; tail -n +3 "$rf"; fail=$((fail + 1)) ;;
  esac
done

# THE COUNT CASE THE HEADER PROMISES, AND IT LIVES HERE BECAUSE ONLY A WHOLE RUN CAN TAKE THE SECOND
# NUMBER. `--list` sweeps this file's own text; `$pass + $fail` counts the verdicts a run actually
# wrote. The header has claimed since 2026-08-24 that the two are pinned against each other and
# nothing pinned them - the register that comment says is guarded was not guarded.
#
# IT PINS AGREEMENT WITH THE CODE AND NOT COMPLETENESS. A case reached by a route the sweep does not
# recognise is invisible to `--list` and writes a verdict all the same, which this would catch; a
# case that exists in neither is invisible to both and this says nothing about it.
#
# ON AGREEMENT IT ADDS NOTHING TO `$pass`, so `caught N` stays the number `--list` prints and a human
# can compare the two by eye. A disagreement reddens the run, which is the whole point of having it.
if [ -z "$ONLY" ]; then
  l_d=$(sweep_dispatched | grep -c .)
  l_i=$(sweep_inline     | grep -c .)
  listed=$((l_d + l_i)); ran=$((pass + fail))
  if [ "$listed" -eq "$ran" ]; then
    printf 'CHECKED  %-36s\n' "--list agrees with the run ($ran)"
  else
    printf 'MISSED   %-36s\n' "--list agrees with the run"
    echo "           --list sweeps $listed case(s) from this file; the run wrote $ran verdict(s)."
    echo "           One of them is reached by a route the other cannot see."
    fail=$((fail + 1))
  fi
fi

echo
# THE BARE LINE IS UNCHANGED, DELIBERATELY. Journals, the sprint record and the brief all quote
# `caught N, missed N` verbatim, and a filtered run says so on its own line rather than by editing
# the sentence every one of those readers greps. A filtered run is never a reading of the suite.
if [ -n "$ONLY" ]; then
  echo "SELFTEST: caught $pass, missed $fail - FILTERED by --only '$ONLY', $selected selected and $skipped skipped; this is not a reading of the suite"
else
  echo "SELFTEST: caught $pass, missed $fail"
fi
[ "$fail" -eq 0 ]
