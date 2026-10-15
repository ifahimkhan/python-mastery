"""
=====================================================================
 PRACTICE 04.A - Word statistics
=====================================================================
 GOAL   : Analyse a text with lists, sets, dicts and Counter: word
          counts, unique words, the longest words and a bar chart.
 RUN    : uv run python -m course.l04_collections.practice.word_stats.word_stats
 OUTPUT :
          words: 36  unique: 26  sentences: 3
          longest: ['programming', 'beautiful', 'community']
          average word length: 4.58
          top 5:
            is     ##### 5
            the    ### 3
            python ## 2
            and    ## 2
            better ## 2
 DESIGN : words() turns text into a clean list once; every other
          function takes that list and returns a value. Only main() prints.
 EXTEND : Ignore common "stop words" (the, a, and, is, ...) in the top list.
=====================================================================
"""

from collections import Counter

TEXT = """\
Python is a programming language that lets you work quickly. The code is
readable, and the community is friendly. Beautiful is better than ugly, and
simple is better than complex: the Zen of Python says so.
"""

TOP_N = 5
LONGEST_N = 3
BAR_CHAR = "#"
PUNCTUATION = ".,:;!?"


def words(text: str) -> list[str]:
    """Lower-case words with punctuation stripped from both ends."""
    cleaned = [word.strip(PUNCTUATION).lower() for word in text.split()]
    return [word for word in cleaned if word]


def unique_words(word_list: list[str]) -> set[str]:
    return set(word_list)


def longest_words(word_list: list[str], n: int) -> list[str]:
    """The n longest distinct words, longest first; ties in alphabetical order."""
    distinct = sorted(set(word_list))  # alphabetical first...
    return sorted(distinct, key=len, reverse=True)[:n]  # ...sorted() keeps that order for ties


def average_length(word_list: list[str]) -> float:
    if not word_list:
        return 0.0
    return sum(len(word) for word in word_list) / len(word_list)


def top_words(word_list: list[str], n: int) -> list[tuple[str, int]]:
    return Counter(word_list).most_common(n)


def bar_chart(counts: list[tuple[str, int]]) -> list[str]:
    """One aligned line per (word, count): the word, a bar, and the number."""
    if not counts:
        return []
    width = max(len(word) for word, _ in counts)
    return [f"{word:<{width}} {BAR_CHAR * count} {count}" for word, count in counts]


def count_sentences(text: str) -> int:
    return sum(text.count(mark) for mark in ".!?")


def main() -> None:
    word_list = words(TEXT)
    print(
        f"words: {len(word_list)}  unique: {len(unique_words(word_list))}"
        f"  sentences: {count_sentences(TEXT)}"
    )
    print("longest:", longest_words(word_list, LONGEST_N))
    print(f"average word length: {average_length(word_list):.2f}")
    print(f"top {TOP_N}:")
    for line in bar_chart(top_words(word_list, TOP_N)):
        print("  " + line)


if __name__ == "__main__":
    main()
