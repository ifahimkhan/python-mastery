"""
=====================================================================
 PRACTICE 04.B - Gradebook
=====================================================================
 GOAL   : Keep scores per student in a dict of lists, then compute
          averages, rankings and a grade distribution.
 RUN    : uv run python -m course.l04_collections.practice.gradebook.gradebook
 OUTPUT :
          1. Grace   94.3  A
          2. Ada     91.7  A
          3. Linus   78.3  C
          4. Alan    61.0  D
          distribution: {'A': 2, 'B': 0, 'C': 1, 'D': 1, 'F': 0}
          class average: 83.2
 DESIGN : Every function takes the gradebook and RETURNS something new.
          add_score() returns an updated copy instead of changing the
          dict it was given (lesson 04.6).
 EXTEND : Drop each student's lowest score before averaging.
=====================================================================
"""

from collections import Counter

Gradebook = dict[str, list[int]]  # a name for a type (level 08)

GRADE_LIMITS = (("A", 90), ("B", 80), ("C", 70), ("D", 60))
FAIL_GRADE = "F"
DECIMALS = 1


def add_score(book: Gradebook, student: str, score: int) -> Gradebook:
    """A NEW gradebook with the score added. ``book`` is left unchanged."""
    updated = {name: scores.copy() for name, scores in book.items()}  # copy the lists too
    updated.setdefault(student, []).append(score)
    return updated


def average(scores: list[int]) -> float:
    return sum(scores) / len(scores) if scores else 0.0


def averages(book: Gradebook) -> dict[str, float]:
    return {name: round(average(scores), DECIMALS) for name, scores in book.items()}


def letter(score: float) -> str:
    for grade, limit in GRADE_LIMITS:
        if score >= limit:
            return grade
    return FAIL_GRADE


def average_of(pair: tuple[str, float]) -> float:
    return pair[1]


def ranking(book: Gradebook) -> list[tuple[str, float]]:
    """(name, average) pairs, best first; equal averages in name order."""
    pairs = sorted(averages(book).items())  # by name first...
    return sorted(pairs, key=average_of, reverse=True)  # ...then by average (stable sort)


def distribution(book: Gradebook) -> dict[str, int]:
    """How many students got each letter grade, from A to F."""
    counts = Counter(letter(avg) for avg in averages(book).values())
    all_grades = [grade for grade, _ in GRADE_LIMITS] + [FAIL_GRADE]
    return {grade: counts[grade] for grade in all_grades}


def main() -> None:
    book: Gradebook = {
        "Ada": [95, 88, 92],
        "Linus": [72, 85, 78],
        "Grace": [90, 94, 99],
    }
    book = add_score(book, "Alan", 58)
    book = add_score(book, "Alan", 64)

    for position, (name, avg) in enumerate(ranking(book), start=1):
        print(f"{position}. {name:<6} {avg:5.1f}  {letter(avg)}")
    print("distribution:", distribution(book))
    all_scores = [score for scores in book.values() for score in scores]
    print("class average:", round(average(all_scores), DECIMALS))


if __name__ == "__main__":
    main()
