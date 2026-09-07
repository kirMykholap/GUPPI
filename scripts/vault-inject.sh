#!/usr/bin/env bash
# Renders each rule page into the marked region it governs.
# Run: bash scripts/vault-inject.sh            # writes
#      bash scripts/vault-inject.sh --check    # writes nothing; prints every disagreement
#
# WHY THIS EXISTS. Seven harness divergences are on the record and not one was caught by
# anything mechanical. The handoff mapping had been copied into six files and was found only
# because all six happened to share the literal string `section 7`; a renamed heading would not
# have been findable that way, and neither would a reworded rule. So a rule is written once, in
# `wiki/rules/`, and this script puts it where it governs. The file keeps its skeleton and the
# page owns the text.
#
# WHAT TRAVELS IS THE MARKED SLICE, not the whole page (owner, 2026-08-17). A rule page is a page
# like any other here - it carries its justification, its measurements and its links - and none of
# that belongs in a harness file. The alternative was to render the whole body and require rule
# pages to be written short, and it was refused for a reason this project has already measured:
# prose does not stop an agent. `CLAUDE.md` went 218 lines to about 110 once, and only structure
# will keep it there. So the page marks what ships, and everything outside the mark stays home.
#
# THIS IS A SCRIPT AND NOT AN AGENT, deliberately. Four librarians once ran at once, two wrote
# `tags.md`, and both writes survived by luck; a lost update leaves no trace in `git diff`. A
# script run in sequence cannot race. It is also not a hook: every hook on record only prints,
# and a writing hook on `Write|Edit` would fire while a session is editing the same file.
#
# IT MAY SHRINK A FILE, which is what disqualified the librarian from owning harness files - the
# property that makes an unattended writer trustworthy is exactly the one that makes it unfit to
# keep a file whose value is in what it stops saying.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

# Same discovery as vault-check.sh and vault-catalogue.sh, deliberately identical: rules that can
# disagree about where the vault is are worse than any one of them.
VAULT="${VAULT:-}"
if [ -z "$VAULT" ]; then
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
fi
[ -n "$VAULT" ] || { echo "vault-inject: no vault found" >&2; exit 1; }

MODE="write"
case "${1:-}" in
  --check) MODE="check" ;;
  "")      ;;
  *)       echo "vault-inject: unknown argument '$1'; use --check or nothing" >&2; exit 2 ;;
esac

problems=0
written=0
generatedcount=0
removed=0
wholedirs=""
wholedests=""
alreadysaid=""
say() { echo "vault-inject: $*"; problems=$((problems + 1)); }

# Both extractors below refuse to INTERPRET a marker inside a fenced block, and they must, for
# the same reason rule 11 does: a page documenting the marker form would otherwise be read as
# carrying one. This is the fifth place in this repository to need that pass.
#
# THEY NO LONGER DROP THE FENCE ITSELF (2026-08-18). Both used to `next` past every fenced line
# before the accumulate rule could see it, so a fenced block INSIDE a slice was deleted on the
# way to the destination and the injector still reported `0 problem(s)` - the two sides agreed
# because both had been stripped the same way. Nothing caught it because the nine rules that
# existed shipped no code blocks. That stopped being safe the day a definition, the project
# description and the map became renderable records: those carry commands and examples.
#
# So the fence flag still suppresses MARKER RECOGNITION, and the lines are still accumulated.

#  slice_of <page> - the text between the `<!-- text -->` markers.
#  Prints one status line first, then the slice, so a slice whose own first character is a
#  sentinel cannot be mistaken for one.
slice_of() {
  awk '
    { sub(/\r$/, "") }
    /^```/ { inb = !inb; if (ins) { buf = buf $0 "\n"; content = 1 } next }
    inb { if (ins) { buf = buf $0 "\n"; if ($0 ~ /[^ \t]/) content = 1 } next }
    /^<!--[ \t]+text[ \t]+-->[ \t]*$/ {
        if (seen) { bad = "two text slices; a page ships one piece of text or it is two records" }
        seen = 1; ins = 1; next
    }
    /^<!--[ \t]+\/text[ \t]+-->[ \t]*$/ {
        if (!ins) { bad = "a text slice closed but never opened" }
        ins = 0; done = 1; next
    }
    #    A SLICE MAY NOT CARRY A WIKILINK (owner, 2026-08-17; enforced 2026-08-18). The
    #    destination is a file where Obsidian syntax is inert, so a rendered `[[slug]]` reaches
    #    the reader as dead punctuation pointing nowhere. It was stated as a rule with nothing
    #    holding it and measured green on all nine pages; this is the holding.
    #
    #    Asked outside fences and outside code spans, like every other content rule here: text
    #    inside a code block is deliberately literal, and a page whose slice DOCUMENTS the
    #    wikilink form is describing it rather than shipping it.
    ins {
        buf = buf $0 "\n"; if ($0 ~ /[^ \t]/) content = 1
        clean = $0; gsub(/`[^`]*`/, " ", clean)
        if (clean ~ /\[\[[^]]*\]\]/) bad = "a wikilink in the text slice; the destination is a file where Obsidian syntax is inert, so it renders as dead punctuation - cite it outside the slice"
        next
    }
    END {
        if (bad != "")  { print "ERR " bad; exit }
        if (!seen)      { print "ERR no <!-- text --> slice; a page that marks nothing ships nothing"; exit }
        if (!done)      { print "ERR a text slice is opened and never closed"; exit }
        if (!content)   { print "ERR an empty text slice"; exit }
        print "OK"
        printf "%s", buf
    }' "$1"
}

#  marked_by <file> - prints the `type: slug` a generated file names, or nothing.
#  This is the ONLY fact the deleting branch may read. "The vault does not know about this file"
#  and "this file is mine to remove" are different statements and only the second licenses a
#  delete, so a file in the same directory carrying no marker is somebody's hand-written rule and
#  is never touched, whatever the store thinks of it
#  ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).
marked_by() {
  [ -f "$1" ] || return 0
  awk '
    { sub(/\r$/, "") }
    /^<!--[ \t]+vault-inject:[ \t]+generated[ \t]+from[ \t]+/ {
        line = $0
        sub(/^<!--[ \t]+vault-inject:[ \t]+generated[ \t]+from[ \t]+/, "", line)
        sub(/[ \t]+-[ \t]+do[ \t]+not[ \t]+edit[ \t]+-->[ \t]*$/, "", line)
        print line
        exit
    }
    NR > 40 { exit }        # the marker is the writer`s third block; a scan of the whole file is waste
  ' "$1"
}

#  paths_of <page> - the page's own `paths:` field, verbatim, header line and all.
#  Verbatim and not reformatted: the field is authored here and synced into the generated file
#  ([[paths-lives-on-the-vault-page-and-is-written-widest]]), and a script that rewrote the YAML
#  on the way would make the two spellings of one list differ for no reason a reader could see.
#  Frontmatter only - a `paths:` written in the body is prose about the field, not the field.
paths_of() {
  awk '
    { sub(/\r$/, "") }
    NR == 1 { if ($0 != "---") exit; next }
    /^---[ \t]*$/ { exit }
    /^paths:/ { inp = 1; print; next }
    inp && /^[ \t-]/ { print; next }
    inp { inp = 0 }
  ' "$1"
}

#  region_of <file> <type> <slug> - what currently sits between the region markers.
#  Status line first, same reason.
region_of() {
  awk -v type="$2" -v slug="$3" '
    BEGIN { openre  = "^<!--[ \t]+"  type ":[ \t]+" slug "[ \t]+-->[ \t]*$"
            closere = "^<!--[ \t]+/" type ":[ \t]+" slug "[ \t]+-->[ \t]*$" }
    { sub(/\r$/, "") }
    /^```/ { inb = !inb; if (inr) buf = buf $0 "\n"; next }
    inb { if (inr) buf = buf $0 "\n"; next }
    $0 ~ openre  { seen = 1; inr = 1; next }
    $0 ~ closere { inr = 0; done = 1; next }
    inr { buf = buf $0 "\n"; next }
    END {
        if (!seen) { print "ERR carries no region for it"; exit }
        if (!done) { print "ERR the region for it is opened and never closed"; exit }
        print "OK"
        printf "%s", buf
    }' "$1"
}

# `governs:` TAKES A LIST, AND A SCALAR IS THE ONE-ELEMENT CASE (2026-08-21). The field named one
# address and was read with `head -1`, so a rule could render into exactly one file. That became a
# limit the day a second reading agent was designed: the shared reading discipline has to reach both
# the librarian and the pre-task agent, and the quote rule governs both `/handoff` and `/ingest`.
# Copying the text into the second destination is the divergence failure this mechanism exists to
# prevent.
#
# BOTH SPELLINGS, AND THE SCALAR IS NOT DEPRECATED. Thirteen pages carry a bare path today and none
# is touched: `governs: CLAUDE.md` and `governs: [CLAUDE.md]` mean the same thing. The inline-list
# form is the one this corpus already writes `tags:` and `sources:` in, so nothing new is introduced
# for an author to remember.
#
# STILL `head -1`, AND DELIBERATELY. A block list - `governs:` followed by indented `- path` lines -
# is NOT accepted. This script WRITES the files it resolves, so a form nobody writes today, silently
# half-parsed, would render a rule into a subset of where it belongs and leave the gate reading the
# rest as drift. One spelling for the list, checked, beats two where one is guessed at.
governs_targets() {
  # THE `sed | head -1 |` IN FRONT OF THIS AWK IS GONE AND THE PARSER IS UNTOUCHED, 2026-08-24.
  # It was three processes to hand one line to a fourth, on a platform where a spawn costs about
  # 40 ms and this function runs once per governing page inside a script rule 12 of the gate runs
  # for every selftest case. The sub and the `exit` below do exactly what the two of them did:
  # strip the key and its whitespace, and take the FIRST occurrence only.
  #
  # THE FOUR RULES IN THE BODY ARE NOT RETYPED, and that is the point of doing it this way. This
  # function is already the SECOND of three readers of `governs:` in this repository, and the third
  # - the selftest's sandbox loop - was invisible until it met a page naming two destinations and
  # rendered into a file called `[a/one.md, b/two.md]`. A rewrite here would have been a fourth
  # reading of one field; only the plumbing in front of it moved.
  awk '
    /^governs:/ {
      line = $0
      sub(/^governs:[[:space:]]*/, "", line)
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
      exit
    }' "$1"
}

# THE WALK IS EVERY FOLDER, PRE-FILTERED TO THE PAGES THAT DELIVER (2026-08-18). `governs:` is a
# property of any page now, so the glob is `wiki/*/*.md` and the destination comes from the field
# rather than from the folder.
#
# The `grep -l` in front of it is not tidiness, it is the wall clock. Rule 12 of the check asks
# its question BY RUNNING THIS SCRIPT, and the selftest runs the check about ninety times: the
# injector is already 1.98 s of a 4.9 s check because the loop below spawns a grep, a sed and two
# awks per page. Walking 258 pages instead of the 9 that carry `governs:` would multiply the
# largest term of an 8m04s suite by about twenty-eight, and a suite nobody runs catches nothing.
# The filter is a sweep over the same glob, so it cannot drift from what it filters.
#
# A page with no `governs:` is therefore SKIPPED IN SILENCE, and that is the inverse of what this
# loop used to mean. Under the `wiki/rules/` glob "no governs:" and "broken" were the same thing,
# because a rule that names no destination renders nowhere; under this glob they are opposites -
# most of the corpus delivers nothing by design. The rules-only reading of it survives, in the
# check's frontmatter pass where it belongs. What is red here instead is the other half: a page
# that marks a `<!-- text -->` slice and names no destination, which the check reports.
shopt -s nullglob
#    ONE ITERATION PER (page, destination) PAIR, fed already expanded. Wrapping the body in an
#    inner loop would have re-indented two hundred lines for no behaviour, and every `continue`
#    in it already means what it would have to mean there: abandon THIS destination and take the
#    next. A page naming one destination is one iteration, exactly as before.
while IFS=$'\t' read -r page target; do
  [ -n "$page" ] || continue
  #    PARAMETER EXPANSION AND NOT `basename`/`dirname`/`sed`, measured. Each of those is a
  #    process, a process on this platform costs about 40 ms, and this loop runs inside a check
  #    the selftest runs about ninety times: the first draft of these four lines spawned four
  #    processes per page and cost 1.48 s of a 2.28 s script, which is more than the widened
  #    walk it was written to serve.
  slug=${page##*/}; slug=${slug%.md}

  # The type word the marker carries, singular, derived from the folder the page is in. The same
  # derivation as the sweep at the top of `vault-check.sh`, deliberately identical and for the
  # same reason its VAULT discovery is: two rules that can disagree about how a category is
  # spelled are worse than either of them.
  folder=${page%/*}; folder=${folder##*/}
  case "$folder" in
    *ies) type="${folder%ies}y" ;;
    *s)   type="${folder%s}" ;;
    *)    type="$folder" ;;
  esac

  # Only a current page renders. A deprecated one has been superseded, and rendering it would put
  # the retired text back into the file the successor governs. It is read into a VARIABLE rather
  # than skipped on the spot, because under `whole` a retired page still owns a file that has to
  # go - see the branch below, after the destination is known.
  #
  # AND A VALUE THIS SCRIPT DOES NOT KNOW IS REFUSED RATHER THAN READ AS not-current (2026-08-23).
  # The test above was positive - `current` or else - so every other word landed in the retired
  # branch and a rule page carrying one silently stopped rendering. Under `region` that is
  # invisible: the destination keeps the last text written into it, the page and the file drift
  # apart, and nothing says so until rule 12 of the gate compares them. The gate does now catch
  # an illegal value as `badvalue`, but the injector also runs standalone - the write ritual is
  # inject, then check - so it says it where it happens
  # ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
  #
  # It names the two words rather than reading the schema: this script is the WRITER, and a
  # writer that learns its legal set from the same file as the reader can agree with the reader
  # while both are wrong. The register is `wiki/*/_schema.yaml` and the gate reads it; here the
  # pair is the only pair a rendering page can carry, because `implemented` is legal in
  # `proposals/` alone and no proposal governs a file.
  current_status=0
  # BOTH FIELDS IN ONE PASS, 2026-08-24. `status:` was this awk and `render:` was a
  # `sed | head -1 | sed` three hundred lines further down - four processes for two fields on a
  # page, at about 40 ms a spawn, inside a script the gate runs once per selftest case. They are
  # read together here and `render` is taken out of the branch below.
  #
  # EACH KEEPS ITS OWN SEMANTICS EXACTLY. `status` strips trailing whitespace AND a carriage
  # return; `render` strips trailing whitespace and one layer of double quotes and does NOT strip
  # `\r`. Widening the second would be a silent behaviour change wearing an optimisation's
  # clothes: a page carrying `render: region` with a CR is refused today, by name, and it must
  # stay refused.
  #
  # FIRST OCCURRENCE WINS for each, which is what `exit` and `head -1` each meant, and neither
  # reader delimited the frontmatter block before - so neither does now.
  #
  # A TAB JOINS THEM AND A COMMAND SUBSTITUTION CANNOT LOSE IT. Two `print`s would have relied on
  # a trailing newline surviving `$( )`, which strips it - the failure this repository has already
  # met where a gate compared a rendered region against one. One line, one separator, and the
  # empty case still splits correctly at either end.
  fields=$(awk -F'\n' '
    /^status:/ && st == "" { s = $0; sub(/^status:[ \t]*/, "", s); sub(/[ \t\r]+$/, "", s); st = s; next }
    /^render:/ && rn == "" { r = $0; sub(/^render:[ \t]*/, "", r); sub(/[ \t]*$/, "", r)
                             sub(/^"/, "", r); sub(/"$/, "", r); rn = r; next }
    END { printf "%s\t%s\n", st, rn }
  ' "$page")
  page_status=${fields%%$'\t'*}
  render=${fields#*$'\t'}
  [ "$page_status" = "current" ] && current_status=1
  if [ "$page_status" != "current" ] && [ "$page_status" != "deprecated" ]; then
    say "$page: status '$page_status' is neither current nor deprecated, so this script cannot tell whether the page should render or be removed - it renders nothing and reports rather than guessing"
    continue
  fi

  [ -n "$target" ] || continue

  # ONE ROOT: `governs:` is a path from the repository root, and nothing else.
  #
  # It does NOT resolve the way `sources:` does, and the difference is deliberate. `sources:`
  # tries both roots because it only asks whether a citation resolves, and either answer is
  # harmless. `governs:` names a file this script is about to WRITE, so a path that could mean
  # two files means rendering a rule into the wrong one. The dual-root form made exactly one
  # path ambiguous - `CLAUDE.md` exists at the repository root and inside the vault - and it
  # was the first file due to be governed.
  #
  # A path here may therefore name the vault directory, which no script and no page was allowed
  # to do while that name was still being chosen; the owner closed that on 2026-08-17. If it is
  # ever renamed anyway, every rule governing a file inside it fails loudly on the line below
  # rather than rendering somewhere unintended.
  #    WHICH WAY THIS RULE IS DELIVERED (owner, 2026-08-19). `region` writes a slice into a file
  #    that has a life of its own and the paired markers protect the rest of it; `whole` owns a
  #    file that has no other life, where there is nothing around the text to protect and the
  #    frontmatter could not carry a marker anyway
  #    ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).
  #
  #    ABSENT IS RED, owner's ruling of 2026-08-20, and the verdict was recorded nowhere in the
  #    vault until he was asked for it. It read as `region` until that day. The default was
  #    bounded and correct everywhere it applied, and it was still a trap for the NEXT page
  #    written: the field was required where it could discriminate and absent where it could not,
  #    so a page outside `wiki/rules/` rendered under a mode nothing on it named.
  #
  #    REMOVING IT TOOK THREE MOVES IN ONE ORDER, and the order is the check's rather than a
  #    preference: `render` admitted to `concepts/_schema.yaml` WITH its value list, then the two
  #    `concepts/` pages carrying `governs:` stamped `render: region` by the librarian, and only
  #    then this. Reversed, the middle move is red - a key in neither schema block is rejected
  #    ([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]).
  #
  #    THE EMPTY CASE IS SPELLED OUT RATHER THAN LEFT TO FALL THROUGH TO `*)`. Deleting the
  #    default line alone would refuse correctly and diagnose falsely: `render '' is neither
  #    region nor whole` says the value is wrong when the field is missing, and it names no
  #    condition the reader can clear ([[a-refusal-is-conditional-or-absolute-and-nothing-else]]).
  #    The selftest case pins THE DIAGNOSIS and forbids the other sentence, because a case pinning
  #    the refusal alone would have gone green against exactly that defect - which is the failure
  #    this repository met the same day in `hook-selftest.ps1`.
  #    THE READ ITSELF MOVED UP BESIDE `status:` ON 2026-08-24 and is not repeated here. It was
  #    `sed | head -1 | sed` - three processes - and it now shares the one awk that reads the
  #    status. Everything this comment block rules on is unchanged; only where the value is
  #    fetched moved.
  case "$render" in
    region|whole) ;;
    "") say "$page: no 'render:' and this page renders - add 'render: region' or 'render: whole'"; continue ;;
    *) say "$page: render '$render' is neither region nor whole"; continue ;;
  esac

  dest="$target"

  #    A DEPRECATED WHOLE-MODE PAGE LEAVES A FILE BEHIND, and it is not enough to stop writing it.
  #    A deprecated rule does not render ([[a-deprecated-rule-does-not-render]]); under `region`
  #    that is achieved by skipping the page, because the successor rewrites the same region and
  #    the retired text is overwritten. Under `whole` the file is the rule: skipping the page
  #    leaves the retired rule on disk, and the guard keeps delivering it on every matching edit.
  #    So a retired page's own destination is a leftover, and this is the cheap half of finding
  #    one - no sweep is needed, because the page still names the file.
  if [ "$current_status" -ne 1 ]; then
    if [ "$render" = "whole" ] && [ -f "$dest" ] && [ -n "$(marked_by "$dest")" ]; then
      if [ "$MODE" = "check" ]; then
        say "$dest: generated from $page, which is no longer current - run: bash scripts/vault-inject.sh"
        #    The sweep below would reach the same file from the other direction and report it a
        #    second time. One cause printing twice reads as two causes, and a reader who fixes
        #    the first goes looking for a second that was never there.
        alreadysaid="$alreadysaid|$dest|"
      else
        rm -f "$dest"
        echo "vault-inject: removed $dest, generated from a page that is no longer current"
        removed=$((removed + 1))
      fi
    fi
    continue
  fi

  #    Collected from the CURRENT pages, so the sweep after the loop knows which directories a
  #    whole-mode file can legitimately be in and which files in them are accounted for. Both are
  #    read off the pages rather than written here, which is what keeps `.claude/rules/` an
  #    ordinary destination instead of a name this script knows.
  if [ "$render" = "whole" ]; then
    wholedirs="$wholedirs${dest%/*}"$'\n'
    wholedests="$wholedests|$dest|"
  fi

  if [ "$render" = "region" ] && [ ! -f "$dest" ]; then
    say "$page: governs '$target', which is not a file - the path is written from the repository root"
    continue
  fi

  #    THE SENTINEL IS WHAT MAKES THE COMPARISON BELOW HONEST (2026-08-18). `$( )` strips EVERY
  #    trailing newline from what it captures, so both sides used to arrive with their tails
  #    already removed and compared equal on a difference the shell had deleted before either
  #    was read. The comment below claimed byte equality and it was not true of the tail.
  #
  #    Measured before the fix, against this script: a region carrying one blank line the slice
  #    does not carry got `every rule agrees with the region it governs`, exit 0, and
  #    `0 region(s) rewritten` in write mode. A blank line hand-added inside any region passed
  #    the gate - the one thing a rendered region exists to make impossible.
  #
  #    `printf X` runs inside the same substitution, after the function, so the tail is no
  #    longer trailing and survives; `${var%X}` takes it off again. Nothing else changes: the
  #    status line is still the first line and the payload still starts after it.
  s=$(slice_of "$page"; printf 'X'); s=${s%X}; status=${s%%$'\n'*}
  case "$status" in
    OK) slice=${s#OK$'\n'} ;;
    *)  say "$page: ${status#ERR }"; continue ;;
  esac

  #    An empty region is legal and is the normal state of a freshly marked-up file: the status
  #    line arrives alone, with nothing after it to strip. With the sentinel it arrives as
  #    `OK\n` rather than as `OK`, so stripping the prefix is enough and the special case that
  #    used to compare the whole capture against the bare word is gone.
  #    A whole-mode file is CREATED, so its absence is the normal first state rather than an
  #    error - but its directory is not created. A path whose directory does not exist is a
  #    typo in `governs:` far more often than it is a directory somebody meant this script to
  #    invent, and inventing one puts a rule somewhere nobody is looking.
  if [ "$render" = "whole" ]; then
    if [ ! -d "${dest%/*}" ]; then
      say "$page: governs '$target', whose directory does not exist - a whole-mode file is created but its directory is not"
      continue
    fi

    #    `paths:` IS REQUIRED WHERE IT IS READ, AND NOWHERE ELSE (owner, 2026-08-20). Claude Code
    #    matches the `paths:` frontmatter of a file under `.claude/rules/` and loads that rule when
    #    a matching file is read. Anywhere else the block is inert text no reader consults.
    #
    #    A rule delivered by a hook message has no file to match and cannot honestly carry one. The
    #    alternative was to give it a `paths:` anyway so this check would pass; that was REJECTED,
    #    because a field a machine reads is the last place to put something untrue, and a scope
    #    written to satisfy a check is a scope nobody can later trust.
    #
    #    So the requirement keys on the DESTINATION rather than on the mode. Under `.claude/rules/`
    #    a missing `paths:` is the error it has always been - the generated file would name nothing
    #    to match and the rule would never load, which is a rule that silently is not there.
    paths=$(paths_of "$page"; printf 'X'); paths=${paths%X}
    #    BOTH SPELLINGS, and the first one is the real one. `governs:` is defined as a path from the
    #    repository root and `dest` is that string verbatim, so the destination arrives as
    #    `.claude/rules/x.md` with nothing before it - a pattern written only as `*/.claude/rules/*`
    #    matches none of them and silently stops requiring `paths:` in the one directory that needs
    #    it. Measured: written that way, the case asserting the refusal turned over on the next run.
    case "$dest" in
      .claude/rules/*|*/.claude/rules/*)
        if [ -z "$paths" ]; then
          say "$page: render: whole into .claude/rules/ and no 'paths:' - the generated file's frontmatter would name nothing to match"
          continue
        fi
        ;;
    esac

    #    THE GENERATED FORM IS DEFINED HERE, ONCE, for the reason the rendered region is: the
    #    writer and the comparison must never be able to disagree about what generated means.
    #    The marker is an HTML comment because a comment is stripped before the model reads the
    #    file - measured, so the banner costs nothing
    #    ([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]) - and it
    #    carries the page's address in the same `type: slug` form a region marker does, so one
    #    reading serves the human warning and the script's permission to delete.
    marker="<!-- vault-inject: generated from $type: $slug - do not edit -->"

    #    NO `paths:` MEANS NO FRONTMATTER BLOCK AT ALL, rather than an empty one. `---` followed by
    #    `---` is a frontmatter that says nothing, and every reader of this file would then have to
    #    decide what an empty one means. The marker still leads, so the file keeps the one property
    #    the deletion path keys on: a generated file is recognised by its marker and by nothing else
    #    ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).
    #
    #    Both forms are still defined HERE and only here, which is the property that matters: the
    #    writer and the comparison below read the same `$generated` and cannot disagree about what
    #    generated means.
    if [ -n "$paths" ]; then
      generated="---"$'\n'"$paths""---"$'\n'$'\n'"$marker"$'\n'$'\n'"$slice"
    else
      generated="$marker"$'\n'$'\n'"$slice"
    fi

    #    The sentinel again, and for the same reason it is used on the slice: `$( )` strips every
    #    trailing newline, so both sides would arrive with their tails already gone and compare
    #    equal on a difference the shell deleted before either was read.
    if [ -f "$dest" ]; then
      ondisk=$(cat "$dest"; printf 'X'); ondisk=${ondisk%X}
    else
      ondisk=""
    fi

    [ "$ondisk" = "$generated" ] && continue

    if [ "$MODE" = "check" ]; then
      if [ -e "$dest" ]; then
        say "$dest: does not carry what $page says - run: bash scripts/vault-inject.sh"
      else
        say "$dest: does not exist and $page generates it - run: bash scripts/vault-inject.sh"
      fi
      continue
    fi

    printf '%s' "$generated" > "$dest"
    echo "vault-inject: generated $type $slug into $dest"
    generatedcount=$((generatedcount + 1))
    continue
  fi

  r=$(region_of "$dest" "$type" "$slug"; printf 'X'); r=${r%X}; status=${r%%$'\n'*}
  case "$status" in
    OK) current=${r#OK$'\n'} ;;
    *)  say "$page: governs $dest, which ${status#ERR }"; continue ;;
  esac

  #    THE RENDERED FORM IS THE SLICE PLUS ONE BLANK LINE (owner, 2026-08-18), and it is defined
  #    HERE, once, because the writer and the comparison must never be able to disagree about
  #    what "rendered" means. Define it in the writer alone and the check reports a difference on
  #    every run for good; define it in the comparison alone and the separator is never written.
  #
  #    WHY A SEPARATOR AT ALL. Block-level HTML comments are stripped from `CLAUDE.md` before it
  #    reaches the model - which is why the markers cost nothing, measured at 1354 of 7213 bytes
  #    on disk and none in context - but the blank line BETWEEN two adjacent regions is stripped
  #    with them, and the rules arrived glued into one run-on block. The file looked right and
  #    what was read did not. Carrying the separator inside the region is what makes it survive,
  #    and it is idempotent: the writer drops the old region body wholesale, so one blank line is
  #    written however many times this runs.
  #
  #    A blank line and not some character that would survive on its own: an HTML comment is
  #    stripped along with the markers, a line of spaces is trailing whitespace and this project
  #    has already been bitten by an editor trimming it, and only a blank line is a paragraph
  #    break in markdown. It is affordable because the comparison above can now see a tail.
  rendered="$slice"$'\n'

  #    Byte equality, not a normalised or hashed comparison - and now true of the tail as well.
  #    `*.md` is pinned `text eol=lf`, so the working copy a script reads is the same bytes
  #    everywhere, and the regenerate-and-diff precedent of rule 9 is exactly this shape.
  #    Whitespace normalisation would let a rule and its rendering differ in the one dimension
  #    markdown reads as structure.
  if [ "$current" = "$rendered" ]; then
    continue
  fi

  if [ "$MODE" = "check" ]; then
    say "$dest: the region for '$type: $slug' does not carry what $page says - run: bash scripts/vault-inject.sh"
    continue
  fi

  tmp=$(mktemp)
  printf '%s' "$rendered" > "$tmp.slice"
  awk -v type="$type" -v slug="$slug" -v slicefile="$tmp.slice" '
    function emitslice(   l) { while ((getline l < slicefile) > 0) print l; close(slicefile) }
    BEGIN { openre  = "^<!--[ \t]+"  type ":[ \t]+" slug "[ \t]+-->[ \t]*$"
            closere = "^<!--[ \t]+/" type ":[ \t]+" slug "[ \t]+-->[ \t]*$" }
    { sub(/\r$/, "") }
    /^```/ { inb = !inb; if (!inr) print; next }
    !inb && $0 ~ openre  { print; inr = 1; emitslice(); next }
    !inb && $0 ~ closere { inr = 0; print; next }
    inr { next }
    { print }
  ' "$dest" > "$tmp"
  mv "$tmp" "$dest"
  rm -f "$tmp.slice"
  echo "vault-inject: rendered $type $slug into $dest"
  written=$((written + 1))
  #    Fed by process substitution and not a pipe, so `problems` and `written` are incremented in
  #    THIS shell. A pipe would run the loop in a subshell, every count would be discarded at the
  #    `done`, and the script would report zero problems whatever it found.
done < <(find "$VAULT/wiki" -mindepth 2 -maxdepth 2 -name '*.md' -print0 2>/dev/null \
         | xargs -0 --no-run-if-empty grep -l '^governs:' 2>/dev/null | sort \
         | while IFS= read -r gp; do
             governs_targets "$gp" | while IFS= read -r gt; do
               printf '%s\t%s\n' "$gp" "$gt"
             done
           done)


#    THE OTHER HALF: a marked file whose page is gone entirely rather than deprecated. The page
#    cannot name it, so the directories are swept - and they are swept from the destinations the
#    pages themselves name, never from a directory written into this script. `.claude/rules/` is
#    where the first customer lives and it is not special; what makes a directory sweepable is
#    that a whole-mode page generates into it.
#
#    THE RESIDUAL IS NAMED RATHER THAN HIDDEN: if the LAST whole-mode page generating into a
#    directory is deleted or archived, that directory stops being swept and a marked file in it
#    becomes invisible. Sweeping the whole repository instead would cost a recursive grep on every
#    run of a script the gate runs about ninety times per selftest. The trade is stated here so
#    that the day it bites, it is a known gap and not a discovery.
if [ -n "$wholedirs" ]; then
  while IFS= read -r sweepdir; do
    [ -n "$sweepdir" ] && [ -d "$sweepdir" ] || continue
    for candidate in "$sweepdir"/*.md; do
      [ -f "$candidate" ] || continue
      case "$wholedests" in
        *"|$candidate|"*) continue ;;      # a file a current page generates: not a leftover
      esac
      case "$alreadysaid" in
        *"|$candidate|"*) continue ;;      # its own page already named it, one line above
      esac
      owner=$(marked_by "$candidate")
      [ -n "$owner" ] || continue          # no marker: somebody's own file, never touched
      if [ "$MODE" = "check" ]; then
        say "$candidate: carries the generated-marker for '$owner' and no current page generates it - run: bash scripts/vault-inject.sh"
      else
        rm -f "$candidate"
        echo "vault-inject: removed $candidate, marked for '$owner' and generated by no current page"
        removed=$((removed + 1))
      fi
    done
  done < <(printf '%s' "$wholedirs" | sort -u)
fi

if [ "$MODE" = "check" ]; then
  [ "$problems" -eq 0 ] && echo "vault-inject: every rule agrees with the region it governs"
else
  echo "vault-inject: $written region(s) rewritten, $generatedcount file(s) generated, $removed removed, $problems problem(s)"
fi
[ "$problems" -eq 0 ] || exit 1
exit 0
