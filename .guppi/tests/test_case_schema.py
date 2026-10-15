"""The example Case of `vault/wiki/case-example.md`, in the chat form `case-guppi` writes
into its file, passes the check the `SubagentStop` hook runs over that file (case 717.1,
`estimate-case-example-passes-the-check`; before it case 646). The test holds no copy of
the example or of the checks: it reads the block tagged `case` from the rendered page and
runs `casecheck.check_answer` over it. While `case-example.md` does not stand — until the
librarian's render writes it — the example is read from `vault/wiki/case-schema.md`, where
it stood before. A page that holds no block tagged `case` fails both tests with a message
that names the file it read, so an example a render lost does not pass unseen (case 652).
"""

import shutil
from pathlib import Path

import pytest

from guppi import casecheck
from guppi.materialize import closes_fence, fence_opening, quoted_sections, split_cases

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "vault" / "wiki" / "case-schema.md"
EXAMPLE = ROOT / "vault" / "wiki" / "case-example.md"  # the examples' own file (case 717.1)
ANCHOR = "the buyer pays at `/checkout/pay`"  # the `old` of the example's pair
PADDED = f"`` {ANCHOR} ``"


def example(path: Path | None = None) -> str:
    """The first block tagged `case` of the page — `case-example.md`, or `case-schema.md`
    while the first does not stand (case 717.1) — its lines as they stand, the quote
    markers of the Case kept, which `tagged_blocks` would remove; the fence judged by
    `fence_opening` and `closes_fence`, the one judgment of a fence (case 444.1)."""
    if path is None:
        path = EXAMPLE if EXAMPLE.is_file() else SCHEMA
    opening, kept = None, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if opening is None:
            found = fence_opening(line)
            opening = found if found and found[2] == "case" else None
            continue
        if closes_fence(line, opening):
            return "\n".join(kept) + "\n"
        kept.append(line)
    pytest.fail(f"{path} holds no block tagged case — the example of case 717.1 is gone (case 652)")


def seed(project: Path, text: str) -> None:
    """The schema files of the vault, the page whose anchor the example's pair names, and
    the Estimate the example replaces, its Criterion only the lines the example's `when` and
    `then` carry — so the check finds what the example breaks and nothing of the seed."""
    for schema in (ROOT / "vault" / "wiki").glob("*/schema.yaml"):
        target = project / "vault" / "wiki" / schema.parent.name / "schema.yaml"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(schema, target)
    (project / "guppi.toml").write_text(
        'documentation_lang = "en"\nchat_lang = "ru"\n', encoding="utf-8"
    )
    entities = project / "vault" / "wiki" / "entities"
    (entities / "entity-checkout.md").write_text(
        "---\ntype: entity\nkind: Leaf\npurpose: Takes payment\nstatus: draft\n"
        f"tags: [checkout]\n---\n\n## Purpose\n\nToday {ANCHOR}.\n",
        encoding="utf-8",
    )
    cases = split_cases(text)
    item = "update `estimate-checkout-orders-the-steps`"
    owner = next(case for case, lines in cases.items() if item in "\n".join(lines))
    sections = quoted_sections(cases[owner], ("when", "then"))
    criterion = f"When:\n{sections['when']}\n\nThen:\n{sections['then']}"
    estimates = project / "vault" / "wiki" / "estimates"
    (estimates / "estimate-checkout-orders-the-steps.md").write_text(
        '---\ntype: estimate\nkind: QA\nstatus: passed\ntarget: "[[entity-checkout]]"\n'
        "purpose: The steps of checkout come in order\nmethod: uv run --project .guppi pytest tests/test_x.py\n"
        f"tags: [checkout]\n---\n\n## Criterion\n\n{criterion}\n",
        encoding="utf-8",
    )


def check(project: Path, text: str):
    seed(project, text)
    return casecheck.check_answer(text, project)


def test_case_schema_the_example_passes_the_check(tmp_path):
    text = example()
    found, notes = check(tmp_path, text)
    standing = [f for each in found.values() for f in each]
    noted = [n for each in notes.values() for n in each]
    assert standing == [] and noted == [], "\n".join(standing + noted)


def test_case_schema_an_unpadded_span_of_the_example_is_a_finding(tmp_path):
    text = example()
    assert PADDED in text
    broken = text.replace(PADDED, f"``{ANCHOR}``", 1)
    found, _ = check(tmp_path, broken)
    standing = [f for each in found.values() for f in each]
    assert any("padded by one space" in f for f in standing), "\n".join(standing)
