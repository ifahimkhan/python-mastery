"""Reference answers for Level 04. Try the exercises first!

Each answer explains WHY it is written this way.
"""

from collections import Counter, defaultdict

MIN_DISTINCT_FOR_SECOND = 2


class CollectionsSolutions:
    # set() drops duplicates, sorted() returns a NEW list (numbers.sort()
    # would reorder the caller's list: never change what you were given).
    def second_largest(self, numbers: list[int]) -> int | None:
        distinct = sorted(set(numbers), reverse=True)
        if len(distinct) < MIN_DISTINCT_FOR_SECOND:
            return None
        return distinct[1]

    # dict keys are unique AND keep insertion order, so dict.fromkeys() is
    # an "ordered set". list(set(items)) would lose the order.
    def remove_duplicates(self, items: list[str]) -> list[str]:
        return list(dict.fromkeys(items))

    # Counter does the get(word, 0) + 1 loop for us. dict() turns it back
    # into a plain dict so the return type is exactly dict[str, int].
    def word_frequencies(self, text: str) -> dict[str, int]:
        return dict(Counter(text.lower().split()))

    # A dict comprehension reads like the task: "value: key for each pair".
    def invert(self, mapping: dict[str, int]) -> dict[int, str]:
        return {value: key for key, value in mapping.items()}

    # Set intersection is exactly "in both". It also ignores duplicates.
    def common_elements(self, a: list[int], b: list[int]) -> set[int]:
        return set(a) & set(b)

    # Filter with `if`, transform in the expression.
    def squares_of_evens(self, numbers: list[int]) -> list[int]:
        return [n * n for n in numbers if n % 2 == 0]

    # Two for clauses, read left to right like two nested loops.
    def flatten(self, nested: list[list[int]]) -> list[int]:
        return [item for row in nested for item in row]

    # defaultdict(list) creates each group the first time we see a length.
    def group_by_length(self, words: list[str]) -> dict[int, list[str]]:
        groups: defaultdict[int, list[str]] = defaultdict(list)
        for word in words:
            groups[len(word)].append(word)
        return dict(groups)

    # Slicing builds new lists, so the input is never changed.
    # `% len(items)` wraps big and negative steps into 0..len-1
    # (Python's % is never negative for a positive right side, lesson 01.6).
    def rotate(self, items: list[int], steps: int) -> list[int]:
        if not items:
            return []
        cut = len(items) - steps % len(items)
        return items[cut:] + items[:cut]

    # most_common() sorts by count and keeps first-seen order for ties,
    # which is exactly what the task asks for.
    def top_words(self, text: str, n: int) -> list[tuple[str, int]]:
        return Counter(text.lower().split()).most_common(n)
