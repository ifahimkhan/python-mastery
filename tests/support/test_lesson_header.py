import pytest

from tests.support.lesson_header import HeaderError, expected_output

HEADER = '''"""
=====================================================================
 LESSON 01.2 - Variables
=====================================================================
 GOAL   : Store values.
 RUN    : uv run python -m course.l01_basics.lesson02_variables.variables
 OUTPUT :
          name = Ada
            indented line

 NEXT   : lesson03_types/types.py
=====================================================================
"""
'''


def test_reads_output_block_and_keeps_relative_indent() -> None:
    assert expected_output(HEADER) == ["name = Ada", "  indented line"]


def test_block_ends_at_ruler_when_no_label_follows() -> None:
    source = '"""\n OUTPUT :\n          one\n          two\n=====\n"""\n'
    assert expected_output(source) == ["one", "two"]


def test_parenthesised_text_opts_out() -> None:
    source = '"""\n OUTPUT : (example session: you type 7)\n NEXT : x\n"""\n'
    assert expected_output(source) is None


def test_empty_block_means_lesson_prints_nothing() -> None:
    source = '"""\n OUTPUT :\n NEXT   : x\n"""\n'
    assert expected_output(source) == []


def test_missing_docstring_fails() -> None:
    with pytest.raises(HeaderError, match="no module docstring"):
        expected_output("print('hi')\n")


def test_missing_output_label_fails() -> None:
    with pytest.raises(HeaderError, match="no 'OUTPUT :' line"):
        expected_output('"""\n GOAL : x\n"""\n')


def test_opt_out_text_without_parentheses_fails() -> None:
    with pytest.raises(HeaderError, match="must start with"):
        expected_output('"""\n OUTPUT : depends on input\n"""\n')
