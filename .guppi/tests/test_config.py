"""`.guppi/guppi/config.py`: the settings of `guppi.toml` and the table of the languages.

Rule page: `vault/wiki/rules/rule-guppi-config.md`. The tests write a small `guppi.toml` in
a temp folder; nothing here touches the repository's own file.
"""

import pytest

from guppi import config

SETTINGS = '# guppi settings\ndocumentation_lang = "en"\nchat_lang = "ru"\n'


def test_the_table_names_each_code_and_its_script():
    assert config.name_of("en") == "English"
    assert config.name_of("ru") == "Russian"
    assert config.script_of("en") == "Latin"
    assert config.script_of("ru") == "Cyrillic"
    assert all(language.name and language.script for language in config.LANGUAGES.values())


def test_parse_gives_both_codes():
    assert config.parse(SETTINGS, "guppi.toml") == {"documentation_lang": "en", "chat_lang": "ru"}


@pytest.mark.parametrize("key", config.KEYS)
def test_a_missing_key_is_an_error_naming_the_source_and_the_key(key):
    text = "\n".join(line for line in SETTINGS.splitlines() if not line.startswith(key))
    with pytest.raises(config.ConfigError, match=f"guppi.toml: no key {key}"):
        config.parse(text, "guppi.toml")


def test_an_unknown_code_is_an_error_naming_the_source_and_the_key():
    text = SETTINGS.replace('"ru"', '"xx"')
    with pytest.raises(config.ConfigError, match="rule-guppi-config: chat_lang = 'xx'"):
        config.parse(text, "rule-guppi-config")


def test_a_text_that_is_not_toml_is_an_error():
    with pytest.raises(config.ConfigError, match="does not parse as TOML"):
        config.parse("documentation_lang = en\n", "guppi.toml")


def test_read_settings_reads_the_file_at_the_root(tmp_path):
    (tmp_path / "guppi.toml").write_text(SETTINGS, encoding="utf-8", newline="\n")
    assert config.read_settings(tmp_path)["chat_lang"] == "ru"


def test_read_settings_on_a_missing_file_is_an_error(tmp_path):
    with pytest.raises(config.ConfigError, match="guppi.toml: missing"):
        config.read_settings(tmp_path)


def test_outside_finds_a_letter_of_another_script():
    assert config.outside("a Case with один word", "en")
    assert not config.outside("A plain English line — with `code`, 42 and «quotes».", "en")
    assert not config.outside("Déjà vu, naïve", "en")
    assert config.outside("Русский текст with a Latin word", "ru")
    assert not config.outside("Русский текст — 42.", "ru")
    # inside a code span a Latin letter is accepted, any other judged as in prose (case 589.1)
    assert not config.outside("Русский текст про `rule-prespec` и `guppi/config.py`.", "ru")
    assert config.outside("An English line with `слово` in a code span.", "en")
    assert config.outside("Русский текст с `α` в коде.", "ru")


@pytest.mark.parametrize(
    ("line", "pending"),
    [
        ("setup_done = false", True),
        ("setup_done = true", False),
        ('setup_done = "false"', False),
        ("setup_done = 0", False),
        ("", False),
    ],
)
def test_setup_pending_only_on_setup_done_false(tmp_path, line, pending):
    (tmp_path / "guppi.toml").write_text(SETTINGS + line + "\n", encoding="utf-8", newline="\n")
    assert config.setup_pending(tmp_path) is pending


def test_setup_pending_on_a_missing_file_is_false(tmp_path):
    assert config.setup_pending(tmp_path) is False


def test_setup_pending_on_a_text_that_is_not_toml_is_false(tmp_path):
    text = "setup_done = false\ndocumentation_lang = en\n"
    (tmp_path / "guppi.toml").write_text(text, encoding="utf-8", newline="\n")
    assert config.setup_pending(tmp_path) is False


# --- the main branch (case 1070.1): `estimate-guppi-config-fills-the-main-branch` ---


def write_settings(folder, text):
    (folder / "guppi.toml").write_text(text, encoding="utf-8", newline="\n")


def test_main_branch_is_the_value_of_a_written_guppi_toml(tmp_path):
    write_settings(tmp_path, SETTINGS + 'main_branch = "master"\n')
    assert config.main_branch(tmp_path) == "master"


def test_main_branch_is_main_for_a_missing_file(tmp_path):
    assert config.main_branch(tmp_path) == "main"


def test_main_branch_is_main_for_a_text_that_does_not_parse(tmp_path):
    write_settings(tmp_path, "main_branch = master\n")
    assert config.main_branch(tmp_path) == "main"


def test_main_branch_is_main_for_a_missing_key(tmp_path):
    write_settings(tmp_path, SETTINGS)
    assert config.main_branch(tmp_path) == "main"


@pytest.mark.parametrize("value", ["7", '""', '"my branch"'], ids=["number", "empty", "space"])
def test_main_branch_refuses_a_value_naming_the_source_and_the_key(tmp_path, value):
    write_settings(tmp_path, SETTINGS + f"main_branch = {value}\n")
    with pytest.raises(config.ConfigError, match="guppi.toml: main_branch = "):
        config.main_branch(tmp_path)


def test_main_branch_the_render_and_the_code_share_one_judgment():
    assert config.branch_in('main_branch = "trunk"\n', "rule-guppi-config") == "trunk"
    assert config.branch_in(SETTINGS, "rule-guppi-config") is None
    with pytest.raises(config.ConfigError, match="rule-guppi-config: main_branch"):
        config.branch_in('main_branch = "a b"\n', "rule-guppi-config")
