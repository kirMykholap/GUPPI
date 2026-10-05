"""The examples of `vault/wiki/orchestration.md`: a reply that shows a Case passes the `Stop`
check of `rule-case-check` (case 651.2, `estimate-orchestration-showing-example-passes-the-
check`), and a short-form defer passes the `Stop` hook of `rule-spec-write` that writes it
under `## Deferred` (case 651.3, `estimate-orchestration-defer-example-passes-the-hook`). The
tests hold no copy of the examples or of the checks: they read the blocks tagged `showing`
and `defer` from the rendered page and run the functions of `guppi/casecheck.py` and
`guppi/ratified.py` over them. A page that holds no block tagged `showing` or `defer` fails
the tests that read it, with a message that names the file and the tag; no test of the file
is skipped (case 661).
"""

import shutil
from pathlib import Path

import pytest

from guppi import casecheck, ratified
from guppi.materialize import closes_fence, fence_opening, parse_line, split_cases, tagged_blocks

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "vault" / "wiki" / "orchestration.md"


def example(tag: str, path: Path = PAGE) -> str:
    """The first block tagged `tag` of the page, its lines as they stand — the quote markers
    kept — the fence judged by `fence_opening` and `closes_fence`, the one judgment of a
    fence (case 444.1)."""
    opening, kept = None, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if opening is None:
            found = fence_opening(line)
            opening = found if found and found[2] == tag else None
            continue
        if closes_fence(line, opening):
            return "\n".join(kept) + "\n"
        kept.append(line)
    pytest.fail(f"{path} holds no block tagged {tag} — the example of case 651 is gone (case 661)")


@pytest.mark.parametrize("tag", ["showing", "defer"])
def test_a_page_without_the_example_fails_and_names_the_file(tmp_path, tag):
    bare = tmp_path / "orchestration.md"
    bare.write_text("# Orchestration\n\nNo example.\n", encoding="utf-8")
    with pytest.raises(pytest.fail.Exception) as failed:
        example(tag, bare)
    assert str(bare) in str(failed.value) and tag in str(failed.value)


# --- a showing (case 651.2) --------------------------------------------------------------


def store_of_showing(text: str) -> dict:
    """An entry for each sub-case id a ledger line of the showing names: its heading and a
    `ratification` of its own lines, read by `fence_ledger_lines` — what `case-guppi` stores
    for a Case with sub-cases."""
    lines = casecheck.fence_ledger_lines(text.splitlines())
    ids = list(dict.fromkeys(str(parse_line(line)["case"]) for line in lines))
    store = {}
    for case in ids:
        own = [f"> {line}" for line in lines if str(parse_line(line)["case"]) == case]
        body = ["", "> **ratification:**", "> ```", *own, "> ```"]
        store[case] = {
            "text": casecheck.shown_text(f"### Case {case} — sub-case", body),
            "findings": [],
        }
    return store


def test_showing_example_passes_the_check():
    text = example("showing")
    assert casecheck.outside_the_list(text) is None
    store = store_of_showing(text)
    assert len(store) >= 2, "the example shows a Case with two sub-cases"
    shown = casecheck.showings(split_cases(text))
    for case in store:
        assert case in shown, f"case {case}: no showing read"
        assert casecheck.against_store(case, "", shown[case], store) is None


def test_showing_example_a_fence_not_quoted_is_outside_the_list():
    text = example("showing")
    broken = "\n".join(
        line[2:] if line.startswith("> ") and not line.startswith("> **") else line
        for line in text.splitlines()
    )
    assert casecheck.outside_the_list(broken) is not None


# --- a short-form defer (case 651.3) -----------------------------------------------------


def defer_records(text: str) -> list[dict]:
    """One `defer` record of the Case of the example for each slug of its `then` items."""
    (case,) = split_cases(text)
    blocks = tagged_blocks(split_cases(text)[case], "then")
    slugs = [
        line.split("slug:", 1)[1].strip() for line in blocks[0].splitlines() if "slug:" in line
    ]
    return [parse_line(f"- decision[case {case}][defer][{slug}]{{ref:{slug}}}") for slug in slugs]


def seeded(project: Path) -> Path:
    """The schema files of the vault and an empty plan file."""
    for schema in (ROOT / "vault" / "wiki").glob("*/schema.yaml"):
        target = project / "vault" / "wiki" / schema.parent.name / "schema.yaml"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(schema, target)
    plan = project / ".claude" / "plans" / "plan.md"
    plan.parent.mkdir(parents=True)
    plan.write_text("# Spec\n", encoding="utf-8")
    return plan


def test_defer_example_passes_the_hook(tmp_path):
    text = example("defer")
    records = defer_records(text)
    assert records, "the example defers at least one target"
    plan = seeded(tmp_path)
    keys_for = ratified.key_judge(tmp_path, set())
    assert ratified.write_defers(text, records, plan, keys_for) == []
    written = plan.read_text(encoding="utf-8")
    (case,) = split_cases(text)
    assert written.index(ratified.DEFERRED) < written.index(f"## Case {case} —")


def test_defer_example_items_as_one_mapping_get_the_error(tmp_path):
    text = example("defer")
    records = defer_records(text)
    lines = text.splitlines()
    first = next(i for i, line in enumerate(lines) if line.strip().startswith("- slug:"))
    lines[first] = lines[first].replace("- slug:", "  slug:", 1)
    broken = "\n".join(lines) + "\n"
    plan = seeded(tmp_path)
    errors = ratified.write_defers(broken, records, plan, ratified.key_judge(tmp_path, set()))
    assert any("no fence tagged then with its defer items" in e for e in errors), errors
