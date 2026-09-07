#!/usr/bin/env bash
# Move files into the dated archive and rewrite every `sources:` citation of them, as ONE run.
#
# Run: bash scripts/vault-archive.sh [--dry-run] <date> <session> <kind> <file>...
#      bash scripts/vault-archive.sh 2026-08-20 2026-08-20-some-slug specs probe/RUNBOOK.md
#
# WHY MOVE AND REWRITE ARE ONE COMMAND. Between them the gate is red: a `sources:` path that does
# not exist is a verdict, proved in the real tree rather than argued - `probe/RUNBOOK.md` was moved
# aside, the check returned exit 1 naming all seven pages that cite it, and the file was restored in
# the same command. A filesystem cannot make the pair atomic, so the script closes the window
# instead: it does both and then runs the gate itself, and it says so if the tree is left red.
#
# WHAT IT REWRITES, AND THE LIMIT IS THE POINT. Only lines beginning `sources:`, and only in
# `wiki/` and `archive/`. That is what makes the rewrite mechanical rather than a judgement: the
# gate is a complete detector for those citations, so a miss is caught. A path in PROSE has no
# detector and is not touched here - and often must not be, because a page recording history is
# supposed to name a path that no longer exists.
#
# `sed` CANNOT TELL AN ADDRESS FROM A QUOTATION. On 2026-08-19 a corpus-wide sweep rewrote two
# QUOTATIONS and made one sentence say the opposite of what it meant, with the gate green
# throughout. Restricting the substitution to `^sources:` is the whole defence: on that line a path
# is an address by construction and can be nothing else.
#
# `log.md` IS NEVER TOUCHED. Owner's ruling, 2026-08-20: the log is what happened and how it was
# recorded. A wrong entry stays and is caught later; correcting it in place destroys the evidence
# that the process produced a wrong entry. Its old paths are correct as written, not stale.
#
# `archive/` IS TOUCHED. Same ruling, and the vault's own predicate: what a page ASSERTS is frozen,
# how it is FOUND is live. A `sources:` line is an address, not a claim. Without this the two
# archived pages citing the probe would dangle forever and no instrument would ever say so, because
# the gate reads `wiki/` only.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

DRY=0
SWEEP=0
while :; do
  case "${1:-}" in
    --dry-run) DRY=1; shift ;;
    --sweep)   SWEEP=1; shift ;;
    *) break ;;
  esac
done

# `--sweep` FINDS ITS OWN LIST INSTEAD OF BEING GIVEN ONE, and it is a MODE OF THIS SCRIPT rather
# than a script of its own (owner, 2026-08-24). The reason is not tidiness: every refusal below is a
# rule about when a page may leave, and a second mover would acquire its own opinion about them. It
# inherits these or it does not exist.
#
# THE DATE AND THE SESSION ARE STILL ARGUMENTS AND ARE NEVER DERIVED. A derived date is a date
# nobody chose, and this store has already been bitten by a selection that failed towards green.
# `/vault-lint` supplies both.
#
# `pages` IS THE ONLY KIND IT SWEEPS. The other four are inbox kinds - what leaves `raw/` - and are
# named file by file by the ritual that produced them.
if [ "$SWEEP" = 1 ]; then
  if [ "$#" -ne 2 ]; then
    echo "usage: bash scripts/vault-archive.sh [--dry-run] --sweep <date> <session>" >&2
    exit 2
  fi
  DATE="$1"; SESSION="$2"; KIND="pages"; shift 2
else
  if [ "$#" -lt 4 ]; then
    echo "usage: bash scripts/vault-archive.sh [--dry-run] <date> <session> <kind> <file>..." >&2
    echo "       bash scripts/vault-archive.sh [--dry-run] --sweep <date> <session>" >&2
    exit 2
  fi
  DATE="$1"; SESSION="$2"; KIND="$3"; shift 3
fi

case "$DATE" in
  [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
  *) echo "VAULT-ARCHIVE: date must be YYYY-MM-DD, got: $DATE" >&2; exit 2 ;;
esac

# The kinds are decided, and a new one is a change to a decided list rather than a typo to
# tolerate. `logs` is deliberately absent: it is raised for a later session and is not built.
#
# `pages` WAS ADDED 2026-08-22, ON THE OWNER'S RULING, AND IT IS THE FIRST KIND THAT IS NOT AN
# INBOX KIND. The other four are what leaves `raw/`. A retired wiki page leaves `wiki/`, and
# `archive/<date>/<session>/` was ruled to hold it - "the wiki pages retired that day, dated by the
# day they were retired" - by the decision that dated the archive at all. That clause had never been
# executable: this script could not express the destination, so every retired page in the corpus
# went flat into `archive/` instead, about thirty of them, the practice quietly outvoting the rule
# for six days. The occasion was retiring `advisory-is-the-default-for-a-hook`, and the owner chose
# the dated form over the practice.
case "$KIND" in
  handoffs|plans|specs|notes|pages) ;;
  *) echo "VAULT-ARCHIVE: kind must be one of handoffs plans specs notes pages, got: $KIND" >&2; exit 2 ;;
esac

VAULT="${VAULT:-}"
if [ -z "$VAULT" ]; then
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
fi
[ -n "$VAULT" ] || { echo "VAULT-ARCHIVE: no vault found" >&2; exit 2; }

DEST_REL="archive/$DATE/$SESSION/$KIND"
DEST="$VAULT/$DEST_REL"

# NO REGULAR EXPRESSION EVER SEES A PATH HERE, and that is a measurement rather than a preference.
# The first version escaped the path for `sed`, and the escape did not survive being written into
# this file: three forms were tried against the real corpus and two of them turned
# `probe/RUNBOOK.md` into `probe&RUNBOOK&md`, so the script reported *cited by 0 page(s)* about the
# nine pages that cite it - an instrument failing towards "nothing to do here". Same class as the
# literal backslash that does not survive a heredoc in this shell, which this store already carries.
#
# So finding is `grep -F` and rewriting is `awk` with `index()` and `substr()`: both literal by
# construction. A path has dots and slashes in it and is never a pattern.
#
# `index($0, "sources:") == 1` IS THE WHOLE OF THE NARROWING. The substitution happens on a line
# that BEGINS with `sources:` and nowhere else, which is what makes it mechanical rather than a
# judgement: on that line a path is an address and can be nothing else. Anywhere else it may be a
# quotation, and rewriting a quotation is how a sweep once made a sentence say the opposite of what
# it meant while the gate stayed green.
cites() {             # cites <file> <path> - true if a sources: line in <file> names <path>
  awk -v p="$2" 'index($0, "sources:") == 1 && index($0, p) > 0 { found = 1 }
                 END { exit !found }' "$1"
}

rewrite_in() {        # rewrite_in <file> <old> <new>
  awk -v old="$2" -v new="$3" '
    index($0, "sources:") == 1 {
      out = ""; rest = $0
      while ((p = index(rest, old)) > 0) {
        out = out substr(rest, 1, p - 1) new
        rest = substr(rest, p + length(old))
      }
      $0 = out rest
    }
    { print }' "$1" > "$1.varch" && mv "$1.varch" "$1"
}

# `status: archived` IS WRITTEN BEFORE THE PAGE MOVES, and that order is the whole reason the value
# had to enter the schemas first. The sweep continues past a refusal, so a run can end with a page
# still in `wiki/` wearing the mark - and `scripts/vault-check.sh` carries a verdict for exactly
# that state, reading it as a move that did not finish. Written after the move instead, that verdict
# is unreachable and the mark tells nobody anything.
#
# IT TOUCHES THE FRONTMATTER AND NOTHING ELSE. The block is delimited by `---` on the first line and
# the next `---`; a body line beginning `status:` - inside a fence, or quoting a schema - is prose
# and is not this field. `index($0, "status:") == 1` is the same anchoring `cites` and `rewrite_in`
# use, for the same reason: on that line the word is a field and can be nothing else.
#
# A PAGE WITH NO `status:` LINE IS LEFT ALONE rather than given one. That is a schema fault and the
# gate is the instrument that decides it; an archiver quietly repairing frontmatter would be a
# second writer of a page's fields, and there is one.
set_status_archived() {   # set_status_archived <file>
  awk 'NR == 1 && $0 == "---" { fm = 1; print; next }
       fm && $0 == "---" { fm = 0; print; next }
       fm && index($0, "status:") == 1 && !seen { print "status: archived"; seen = 1; next }
       { print }' "$1" > "$1.varch" && mv "$1.varch" "$1"
}

# Candidate files by fixed string, then confirmed by `cites` so a path mentioned only in prose is
# never counted and never rewritten.
pages_citing() {      # pages_citing <path>
  grep -rlF "$1" "$VAULT/wiki" "$VAULT/archive" --include='*.md' 2>/dev/null \
    | while IFS= read -r f; do cites "$f" "$1" && printf '%s\n' "$f"; done
}

# EVERY PRECONDITION BELOW IS A JUDGEMENT ABOUT ONE PAGE, so it returns a refusal instead of ending
# the process. Until 2026-08-28 each called `exit 2` from inside the loop, which is right for a named
# list - the caller asked for these files and one of them may not go - and impossible for a sweep,
# which the owner ruled continues past a refusal and collects them.
#
# `REFUSAL` CARRIES THE WHOLE MESSAGE, several lines of it. The reason a page may not leave is the
# only thing telling the reader what to do next, and a sweep printing one line per refusal would be
# a list of names with the instructions thrown away.
#
# WHAT IS A PAGE REFUSAL AND WHAT ENDS THE RUN. Everything decided ABOUT A PAGE is collected: a
# missing file, an occupied destination, no live holder, a refusal without its decision. Everything
# decided BEFORE THE WALK - a malformed date, an unknown kind, no vault - still exits 2 above, where
# it always did. The line between them is whether the answer could differ from one page to the next.
REFUSAL=""
consider_page() {     # consider_page <file> - appends to `pairs` and returns 0, or sets REFUSAL and returns 1
  local f="$1" base slug holders successor successor_file d cite_old
  REFUSAL=""

  if [ ! -e "$f" ]; then REFUSAL="no such file: $f"; return 1; fi
  base=$(basename "$f")
  if [ -e "$DEST/$base" ]; then
    REFUSAL="destination already exists, refusing to clobber: $DEST/$base"
    return 1
  fi

  # A PAGE DOES NOT LEAVE `wiki/` UNLESS SOMETHING LIVE STILL POINTS AT IT (2026-08-23).
  #
  # `archive/` is history and `wiki/` is the source of truth, so an archived page is reached
  # through the live page that carries its claim - *ссылка на него остается в новом документе*.
  # A page archived with nothing pointing at it is not filed, it is lost: `archive/` is outside
  # rules 2, 3, 6, 7 and 14, outside the injector sweep, outside `vault-authority.sh`, and
  # `/pre-task` discards it as retired text
  # ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).
  #
  # WHICH DEFINITION OF *CITED*, because this script already had another one and they disagree.
  # `pages_citing` below matches a `sources:` PATH, and on 2026-08-23 it reported `cited by 0
  # page(s)` about a page five live pages named. This test matches the SLUG - the filename
  # without `.md` - anywhere in a live page, which catches `[[slug]]` and a bare mention alike
  # ([[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]). A hyphenated
  # slug does not occur in ordinary prose, so the loose match costs no false positive, and a
  # bare mention is a real pointer that a wikilink counter would have thrown away.
  #
  # `wiki/` ONLY, and that is the whole point: a holder in `archive/` is history pointing at
  # history. The page being archived is excluded by basename, so a page naming itself does not
  # vouch for itself. `pages` only - a handoff or a spec is not addressed by slug.
  if [ "$KIND" = "pages" ]; then
    slug=${base%.md}

    # A `target_kind: repeal` DECISION NEVER LEAVES `wiki/decisions/`, and this refusal is
    # absolute rather than a condition that can be cleared (owner, 2026-08-30).
    #
    # WHY IT IS THE ONE PAGE THAT MAY NOT BE FILED. Every other criterion here rests on something
    # live carrying the claim after the page goes. A repeal has nothing of the kind: it records
    # that a thing NO LONGER EXISTS, the page it cancelled is itself in `archive/`, and a
    # cancellation has no successor and can have none - the owner overturned the ruling that a
    # repeal is recorded by supersession on the ground that replacing a thing with nothing is not
    # a relation between two pages. So the decision is the only live carrier, and `/pre-task`
    # reads no page in `archive/`: filing it would mean the next plan cannot see that we already
    # built this thing and removed it.
    #
    # THE COST IS NAMED RATHER THAN HIDDEN: this folder now has a class of page that grows and
    # never shrinks. The owner ordered a step at the sprint close to look at them as a set, which
    # is where that cost is meant to be paid.
    if grep -qE '^target_kind:[ \t]*repeal[ \t]*$' "$f" 2>/dev/null; then
      REFUSAL="it carries 'target_kind: repeal', and such a decision does not leave wiki/.
  A repeal records that something no longer exists. The page it cancelled is
  already in archive/, a cancellation has no successor, and /pre-task reads
  nothing in archive/ - so this page is the only live carrier of the fact.
  Reviewing these as a set is a step of the sprint close, not a sweep."
      return 1
    fi
    # `--include` GOES BEFORE `--`, and it did not until 2026-08-23. After `--` it is an
    # OPERAND, not an option: grep reported `No such file or directory` on it into the
    # `2>/dev/null` beside this line and searched with no filter at all. That is not cosmetic -
    # `wiki/*/_schema.yaml` carries thirteen real page slugs in its comment blocks, so a mention
    # inside a schema comment counted as a live page naming the slug and would have released a
    # page nothing points at. Proved both ways in a scratch tree before the token was moved.
    holders=$(grep -rlF --include='*.md' -- "$slug" "$VAULT/wiki" 2>/dev/null \
              | while IFS= read -r h; do [ "$(basename "$h")" = "$base" ] || printf '%s\n' "$h"; done)
    if [ -z "$holders" ]; then
      REFUSAL="no live page under $VAULT/wiki names '$slug'.
  Write the successor that carries the claim first, then archive this.
  Nothing in archive/ is checked, swept or read by /pre-task, so a page
  nothing points at has left the store rather than been filed in it."
      return 1
    fi

    # A DEPRECATED PAGE ALSO NEEDS ITS OWN SUCCESSOR ALIVE, and the holder test above does not ask
    # that (owner, 2026-08-28). `deprecated` means the page went FALSE and another page now carries
    # the claim rightly; the relation is written in `superseded_by:`. The holder test accepts ANY
    # live page naming the slug, so without this a page whose successor is itself deprecated - or
    # absent - leaves on the strength of an unrelated mention, and the claim it was replaced by is
    # reachable from nothing.
    #
    # IT ASKS ONLY OF `deprecated`. A refused proposal has no successor and is forbidden one; an
    # implemented one is not replaced but recorded elsewhere. Neither is checked here and neither
    # should be ([[a-refused-proposal-is-archived-and-takes-status-refused]]).
    if grep -q '^status:[ \t]*deprecated' "$f" 2>/dev/null; then
      successor=$(sed -n 's/^superseded_by:[ \t]*\[\[\([^]]*\)\]\].*/\1/p' "$f" | head -1)
      if [ -z "$successor" ]; then
        REFUSAL="it carries 'status: deprecated' and names no 'superseded_by:'.
  A page is deprecated because it went false and another page now carries the
  claim. Write that relation down before the page leaves: once it is in archive/
  nothing reads it again and the successor is reachable from nothing."
        return 1
      fi
      # THE SUCCESSOR IS LOOKED UP BY CONCATENATION AND NEVER BY `find -name`, which takes a GLOB.
      # A slug is kebab-case today and this file's standing rule is that no pattern ever sees a
      # path: the day a slug carries a bracket, a glob lookup answers about the wrong page or about
      # none, and both directions fail silently.
      successor_file=""
      for d in "$VAULT"/wiki/*/; do
        if [ -e "$d$successor.md" ]; then successor_file="$d$successor.md"; break; fi
      done
      if [ -z "$successor_file" ]; then
        REFUSAL="its successor '$successor' is not a live page under $VAULT/wiki.
  superseded_by: names the page that carries the claim now. If that page is itself
  retired or was never written, this one is not superseded - it is being dropped."
        return 1
      fi
    fi

    # A REPEALED PAGE NEEDS THE DECISION THAT CANCELLED IT, AND IS FORBIDDEN A SUCCESSOR
    # (owner, 2026-08-30). `status: repealed` is legal in `wiki/rules/` alone.
    #
    # THIS IS A SECOND ROUTE AND NOT A HOLE IN THE FIRST. The refusal above - `deprecated` may not
    # leave without a live `superseded_by:` - stays absolute and unconditional, and that was the
    # choice: making it conditional on a field a page could simply omit would turn the strongest
    # test in this script into one an omission clears. A cancellation is a different cause with a
    # precondition of its own, so it gets its own value and its own check.
    #
    # WHY THE PRECONDITION IS `decided_by:` AND NOT A SUCCESSOR. A page is deprecated because it
    # went false and another page carries the claim rightly; a page is repealed because the thing
    # is gone and NOTHING carries it. What must exist instead is the decision that cancelled it -
    # which stays live in `wiki/decisions/` for good, by the refusal at the top of this function,
    # precisely so this pointer never goes dead.
    if grep -q '^status:[ \t]*repealed' "$f" 2>/dev/null; then
      if ! grep -qE '^decided_by:[ \t]*\[\[[^]]+\]\]' "$f" 2>/dev/null; then
        REFUSAL="it carries 'status: repealed' and names no 'decided_by:'.
  A repealed page is cancelled and replaced by nothing, so it has no successor
  and is forbidden one. What it owes instead is the decision that cancelled it,
  which stays live in wiki/decisions/ and is the only carrier of the fact once
  this page reaches archive/."
        return 1
      fi
    fi

    # A REFUSED PROPOSAL NAMES THE DECISION THAT REFUSED IT, and this is the only place that can
    # be checked. The rule applies to a page ON ITS WAY OUT of `wiki/`, and by the time it has
    # landed the frontmatter pass cannot see it: `vault-check.sh` reads `wiki/` alone. A verdict
    # written there would be one that can never fire.
    #
    # AND IT IS A CONDITIONAL REQUIREMENT, which is the other reason it is not in the schema:
    # `decided_by:` is required WHEN the status is `refused` and optional otherwise, and a
    # per-folder schema states one list of required keys for the whole folder. That is the same
    # shape as `paths` under `render: whole` in `wiki/rules/`, which the injector reports for the
    # same reason ([[a-refused-proposal-is-archived-and-takes-status-refused]]).
    #
    # NO `superseded_by:` IS ASKED FOR, deliberately, and its absence is not checked either. A
    # refusal is a CAUSE; `superseded_by:` is a relation between two pages asserting one claim
    # differently, which a refusal and the proposal it refused do not.
    if grep -q '^status:[ \t]*refused' "$f" 2>/dev/null && ! grep -q '^decided_by:' "$f" 2>/dev/null; then
      REFUSAL="it carries 'status: refused' and no 'decided_by:'.
  A refused proposal names the decision that refused it, in decided_by:,
  because that is the only record of who refused it and when. Once the
  page is in archive/ nothing checks it again, so this is the last gate."
      return 1
    fi
  fi
  # The new citation is written VAULT-relative, which is how `raw/handoffs/...` is already written
  # in this corpus. The gate accepts either form; one form in the corpus is worth more than two.
  #
  # AND THE OLD PATH HAS TWO FORMS THAT ARE NOT THE SAME STRING (2026-08-21). The argument is a path
  # from the repository root, because this script cd's there. A `sources:` citation of a file INSIDE
  # the vault is VAULT-relative, so searching the corpus for the ARGUMENT finds nothing and the
  # script reports `cited by 0 page(s)` about a file that nine pages cite - an instrument failing
  # towards "nothing to do here", which is the same direction this file already has a comment about.
  #
  # MEASURED ON THE FIRST JOURNAL IT WAS EVER GIVEN, not argued. The only earlier cargo was
  # `probe/RUNBOOK.md`, OUTSIDE the vault, where the two forms ARE the same string - so the defect
  # could not appear until something inside the vault was archived, and the first such thing was the
  # ingest's own journal. A `case` rather than a `sed`: no regular expression ever sees a path here.
  cite_old="$f"
  case "$f" in "$VAULT"/*) cite_old="${f#"$VAULT"/}" ;; esac
  pairs="$pairs$f	$cite_old	$DEST_REL/$base
"
  return 0
}

# --- the archival criteria, one selector per folder ---
#
# EACH SELECTOR IS ONE PASS OVER THE CORPUS AND NEVER ONE PASS PER PAGE. The naive shape - for each
# of 182 lessons, grep the whole of `wiki/` for its slug - is 182 full-tree greps, and one pass of
# the gate over this corpus already costs 23 seconds. The slugs go into a pattern file and
# `grep -oF -f` extracts every one that occurs, in a single walk.
#
# NO SELECTOR DECIDES WHETHER A PAGE MAY LEAVE. It decides whether a page is a CANDIDATE; the
# preconditions above decide the rest, and they are the same ones a named file goes through.
sweep_tmp=""
cleanup_sweep() { [ -n "$sweep_tmp" ] && rm -rf "$sweep_tmp"; }
trap cleanup_sweep EXIT

# Every slug that appears in a live wiki page OUTSIDE the given folder. One walk, literal matching.
slugs_cited_outside() {   # slugs_cited_outside <folder>
  local folder="$1" pat="$sweep_tmp/pat" list="$sweep_tmp/files" f
  : > "$pat"; : > "$list"
  for f in "$VAULT/wiki/$folder"/*.md; do
    [ -e "$f" ] || continue
    basename "$f" .md >> "$pat"
  done
  [ -s "$pat" ] || return 0
  while IFS= read -r f; do
    case "$f" in "$VAULT/wiki/$folder/"*) continue ;; esac
    printf '%s\n' "$f" >> "$list"
  done < <(find "$VAULT/wiki" -name '*.md' -type f)
  [ -s "$list" ] || return 0
  xargs -a "$list" -d '\n' grep -ohF -f "$pat" 2>/dev/null | sort -u
}

# Every slug a live wiki page names in a `decided_by:` line. The field takes exactly one wikilink.
slugs_named_in_decided_by() {
  grep -rh --include='*.md' '^decided_by:' "$VAULT/wiki" 2>/dev/null \
    | sed -n 's/^decided_by:[ \t]*\[\[\([^]]*\)\]\].*/\1/p' | sort -u
}

# Pages in a folder whose frontmatter carries a given `status:` value.
pages_with_status() {     # pages_with_status <folder> <value>
  grep -rl --include='*.md' -E "^status:[ \t]*$2[ \t]*$" "$VAULT/wiki/$1" 2>/dev/null | sort
}

# Pages in a folder whose frontmatter carries `binding: divergence`.
pages_with_divergence() { # pages_with_divergence <folder>
  grep -rl --include='*.md' -E '^binding:[ \t]*divergence[ \t]*$' "$VAULT/wiki/$1" 2>/dev/null | sort
}

# THE CRITERIA, AS DECIDED. `deprecated` is first and applies in every walked folder: it is the one
# status that obliges a page to leave `wiki/` on sight, because the page went false and there is
# nothing to wait for. The rest are per folder and each names the ruling behind it.
#
# `entities/` AND `concepts/` ARE NOT WALKED - 169 pages with no exit criterion, deferred by the
# owner on 2026-08-28 against "not ever". `rules/` is walked on `deprecated` alone, which is what
# `wiki/rules/_schema.yaml` describes: deprecated plus a decision behind the overturn, the librarian
# setting that mark and this script writing `archived` as it moves the page.
sweep_candidates() {
  local folder slug cited f
  for folder in decisions lessons proposals rules; do
    pages_with_status "$folder" deprecated
  done

  # rules/: `repealed` as well, admitted 2026-08-30. A cancelled rule leaves on the same footing a
  # deprecated one does - it is false where it stands - but by a different precondition, checked in
  # `consider_page`: the decision that cancelled it, never a successor. The value is legal in this
  # folder alone, so no other folder is walked for it.
  pages_with_status rules repealed

  # lessons/: a live page OUTSIDE lessons/ names the slug (owner, 2026-08-26).
  cited=$(slugs_cited_outside lessons)
  for f in "$VAULT/wiki/lessons"/*.md; do
    [ -e "$f" ] || continue
    slug=$(basename "$f" .md)
    case "$cited" in
      *"$slug"*) printf '%s\n' "$f" ;;
    esac
  done

  # decisions/: binding: divergence, or a live page names it in decided_by:, or it carries the
  # `processed` mark the librarian sets on the same predicate. The mark is selected as well as the
  # predicate, deliberately and on the owner's instruction: they should agree, and where an agent
  # set the mark wrongly the predicate is what the page is actually judged by.
  pages_with_divergence decisions
  pages_with_status decisions processed
  cited=$(slugs_named_in_decided_by)
  for f in "$VAULT/wiki/decisions"/*.md; do
    [ -e "$f" ] || continue
    slug=$(basename "$f" .md)
    case "$cited" in
      *"$slug"*) printf '%s\n' "$f" ;;
    esac
  done

  # proposals/: implemented or refused.
  pages_with_status proposals implemented
  pages_with_status proposals refused
}

if [ "$SWEEP" = 1 ]; then
  sweep_tmp=$(mktemp -d)
  mapfile -t sweep_files < <(sweep_candidates | sort -u)
  if [ "${#sweep_files[@]}" -eq 0 ]; then
    echo "VAULT-ARCHIVE: the sweep selected no page - nothing in wiki/ meets a criterion today."
    exit 0
  fi
  echo "VAULT-ARCHIVE: the sweep selected ${#sweep_files[@]} page(s)"
  set -- "${sweep_files[@]}"
fi

# THE LONGEST DESTINATION IS COMPUTED BEFORE ANYTHING MOVES, and it is computed rather than
# attempted. `git mv` has already failed here with *Filename too long* at 240 characters, and this
# clone carries `core.longpaths true` - a per-repository setting that travels with nothing - so a
# successful run HERE is not evidence about a fresh clone anywhere else. Refusing the whole run is
# right: a sweep that stopped halfway would leave the corpus between two states.
longest=""
for f in "$@"; do
  candidate="$DEST/$(basename "$f")"
  if [ "${#candidate}" -gt "${#longest}" ]; then longest="$candidate"; fi
done
if [ "${#longest}" -gt 240 ]; then
  echo "VAULT-ARCHIVE: the longest destination path is ${#longest} characters, over the 240 that" >&2
  echo "VAULT-ARCHIVE:   git has already refused in this repository:" >&2
  echo "VAULT-ARCHIVE:   $longest" >&2
  echo "VAULT-ARCHIVE:   Shorten the session slug. Nothing was moved." >&2
  exit 2
fi

pairs=""
refusals=""
refused=0
for f in "$@"; do
  if consider_page "$f"; then continue; fi
  if [ "$SWEEP" = 1 ]; then
    refused=$((refused + 1))
    refusals="$refusals  $f
    $REFUSAL
"
    continue
  fi
  echo "VAULT-ARCHIVE: refusing to archive $f: $REFUSAL" >&2
  exit 2
done

if [ -z "$pairs" ]; then
  echo "VAULT-ARCHIVE: every selected page was refused; nothing to move."
  printf '%s' "$refusals" >&2
  exit 1
fi

echo "VAULT-ARCHIVE: destination $DEST"
printf '%s' "$pairs" | while IFS=$'\t' read -r old cite new; do
  [ -n "$old" ] && printf 'VAULT-ARCHIVE: map  %s  ->  %s\n' "$cite" "$new"
done

# Every page whose `sources:` names one of these, counted before anything moves, so the report can
# be read against the tree it ran on.
cited=0
while IFS=$'\t' read -r old cite new; do
  [ -n "$old" ] || continue
  n=$(pages_citing "$cite" | wc -l)
  cited=$((cited + n))
  printf 'VAULT-ARCHIVE: cited by %s page(s): %s\n' "$n" "$cite"
done <<< "$pairs"

if [ "$DRY" = 1 ]; then
  # A DRY RUN SHOWS THE REFUSALS TOO, and it is the only place they can be read before the corpus
  # moves. A sweep's dry run whose list omitted what it would refuse would be a list of what it
  # would do, missing the half that says what it would not.
  if [ "$refused" -gt 0 ]; then
    printf 'VAULT-ARCHIVE: %s page(s) would be REFUSED and left where they are:\n' "$refused" >&2
    printf '%s' "$refusals" >&2
  fi
  echo "VAULT-ARCHIVE: --dry-run, nothing moved and nothing rewritten"
  if [ "$refused" -gt 0 ]; then exit 1; fi
  exit 0
fi

mkdir -p "$DEST"

moved=0
sidecars=0

move_one() {          # move_one <path> <dest-dir> - git mv where git knows the file, mv otherwise
  b=$(basename "$1")
  if git ls-files --error-unmatch "$1" >/dev/null 2>&1; then
    git mv "$1" "$2/$b"
  else
    mv "$1" "$2/$b"
  fi
}

marked=0
while IFS=$'\t' read -r old cite new; do
  [ -n "$old" ] || continue
  base=$(basename "$old")
  if [ "$KIND" = "pages" ]; then
    set_status_archived "$old"
    marked=$((marked + 1))
  fi
  if git ls-files --error-unmatch "$old" >/dev/null 2>&1; then
    git mv "$old" "$DEST/$base"
  else
    mv "$old" "$DEST/$base"
  fi
  rc=$?
  if [ "$rc" -ne 0 ]; then echo "VAULT-ARCHIVE: move failed for $old" >&2; exit 1; fi
  moved=$((moved + 1))

  sidecar="${old%.md}.coverage.tsv"
  if [ "$old" != "$sidecar" ] && [ -e "$sidecar" ]; then
    move_one "$sidecar" "$DEST"
    if [ $? -ne 0 ]; then echo "VAULT-ARCHIVE: sidecar move failed for $sidecar" >&2; exit 1; fi
    sidecars=$((sidecars + 1))
    printf 'VAULT-ARCHIVE: sidecar moved with its source: %s\n' "$(basename "$sidecar")"
  fi
done <<< "$pairs"

rewritten=0
while IFS=$'\t' read -r old cite new; do
  [ -n "$old" ] || continue
  while IFS= read -r page; do
    [ -n "$page" ] || continue
    rewrite_in "$page" "$cite" "$new"
    rewritten=$((rewritten + 1))
  done < <(pages_citing "$cite")
done <<< "$pairs"

printf 'VAULT-ARCHIVE: moved %s file(s) and %s sidecar(s), rewrote sources: on %s page(s)\n' \
  "$moved" "$sidecars" "$rewritten"
if [ "$KIND" = "pages" ]; then
  printf 'VAULT-ARCHIVE: marked %s page(s) status: archived before moving them\n' "$marked"
fi

# THE REFUSALS PRINT BEFORE THE GATE RUNS, AND THAT IS NOT A MATTER OF TASTE. The gate writes to
# stderr when it is red and its output is what a reader looks at first; a refusal list underneath it
# is a list nobody reads. It is also the mitigation for this script's exit code meaning two things
# at once - see the exit below.
if [ "$refused" -gt 0 ]; then
  printf 'VAULT-ARCHIVE: %s page(s) were REFUSED and left where they are:\n' "$refused" >&2
  printf '%s' "$refusals" >&2
fi

# THE SWEEP RECORDS WHAT IT DID IN `log.md`, and the explicit mode still does not (owner,
# 2026-08-28). The log is filled by whoever performed the action, and a sweep that moved 240 pages
# without leaving a line is a change nothing in the store accounts for. The file is APPENDED to and
# never rewritten - that is the standing ruling about this register, and it is why a wrong entry
# stays and is corrected beside itself rather than in place.
#
# The named-file mode is left alone because `/ingest` calls it and the librarian writes its own
# `- ingest:` line for the same act; two lines about one move is the drift this store repairs.
log_the_sweep() {
  local log="$VAULT/log.md" last
  [ -e "$log" ] || return 0
  last=$(grep '^## ' "$log" 2>/dev/null | tail -1)
  {
    case "$last" in
      "## $DATE"*) ;;
      *) printf '\n## %s\n' "$DATE" ;;
    esac
    printf '%s\n' "- archive: the sweep moved $moved page(s) into $DEST_REL, marked $marked status: archived, rewrote $rewritten citation(s) and refused $refused"
  } >> "$log"
}
if [ "$SWEEP" = 1 ]; then log_the_sweep; fi

# The script closes its own window rather than trusting the caller to. The exit code is captured on
# the very next statement and never read through a pipe.
bash scripts/vault-check.sh > /dev/null 2>&1
gate=$?
if [ "$gate" -eq 0 ]; then
  echo "VAULT-ARCHIVE: gate exits 0 - the move and the rewrite left the tree green"
else
  echo "VAULT-ARCHIVE: THE GATE IS RED AFTER THE MOVE (exit $gate). Run it and read what it says." >&2
fi

if [ "$SWEEP" = 1 ]; then
  echo "VAULT-ARCHIVE: prose references were NOT touched. log.md carries one appended line."
else
  echo "VAULT-ARCHIVE: prose references were NOT touched and log.md was NOT touched."
fi
echo "VAULT-ARCHIVE: read 'git diff' for meaning before committing - a grep returning zero is not"
echo "VAULT-ARCHIVE: the same thing as a diff a human has read."
# ONE EXIT CODE FOR TWO EVENTS, AND THE AMBIGUITY IS NAMED RATHER THAN HIDDEN. 1 means the gate is
# red OR a page was refused, and this store already carries a page about a non-zero exit from the
# gate no longer naming one event. The mitigation is that both are PRINTED and the refusals come
# first, so a reader who sees 1 has the list and the gate's own words in front of them. 2 stays what
# it is everywhere in this repository: the run was wrong before it started.
if [ "$refused" -gt 0 ] || [ "$gate" -ne 0 ]; then exit 1; fi
exit 0
