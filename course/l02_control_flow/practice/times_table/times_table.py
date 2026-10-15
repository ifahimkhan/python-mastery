"""
=====================================================================
 PRACTICE 02.B - Times table
=====================================================================
 GOAL   : Print a neat multiplication table with nested loops and
          f-string widths.
 RUN    : uv run python -m course.l02_control_flow.practice.times_table.times_table
 OUTPUT :
            x |   1   2   3   4   5
          ----+--------------------
            1 |   1   2   3   4   5
            2 |   2   4   6   8  10
            3 |   3   6   9  12  15
            4 |   4   8  12  16  20
            5 |   5  10  15  20  25
 DESIGN : header() and row() return strings instead of printing, so
          tests can check every line.
 EXTEND : Make the column width grow with the size, so a 12 x 12
          table (largest value 144) still lines up.
=====================================================================
"""

CELL_WIDTH = 4
LABEL_WIDTH = 3
TABLE_SIZE = 5


def header(size: int) -> str:
    line = f"{'x':>{LABEL_WIDTH}} |"
    for column in range(1, size + 1):
        line += f"{column:>{CELL_WIDTH}}"
    return line


def divider(size: int) -> str:
    return "-" * (LABEL_WIDTH + 1) + "+" + "-" * (CELL_WIDTH * size)


def row(n: int, size: int) -> str:
    line = f"{n:>{LABEL_WIDTH}} |"
    for column in range(1, size + 1):
        line += f"{n * column:>{CELL_WIDTH}}"
    return line


def main() -> None:
    print(header(TABLE_SIZE))
    print(divider(TABLE_SIZE))
    for n in range(1, TABLE_SIZE + 1):
        print(row(n, TABLE_SIZE))


if __name__ == "__main__":
    main()
