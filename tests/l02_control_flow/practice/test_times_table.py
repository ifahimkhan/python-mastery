from course.l02_control_flow.practice.times_table.times_table import divider, header, row


def test_header_lists_the_columns() -> None:
    assert header(3) == "  x |   1   2   3"


def test_divider_matches_the_header_width() -> None:
    assert len(divider(5)) == len(header(5))


def test_rows_multiply_and_right_align() -> None:
    assert row(1, 3) == "  1 |   1   2   3"
    assert row(5, 5) == "  5 |   5  10  15  20  25"


def test_every_row_has_the_same_width() -> None:
    assert len(row(1, 5)) == len(row(5, 5)) == len(header(5))
