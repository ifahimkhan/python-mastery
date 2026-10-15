"""
=====================================================================
 PRACTICE 03.A - A tiny text-tools library
=====================================================================
 GOAL   : Write a handful of small, well-named, typed functions that
          each do one thing, then combine them.
 RUN    : uv run python -m course.l03_functions.practice.text_tools.text_tools
 OUTPUT :
          word_count: 9
          title_case: The Quick Brown Fox Jumps Over The Lazy Dog
          truncate: The quick brown...
          truncate(width=12, suffix=' >>'): The quick >>
          is_palindrome('Never odd or even'): True
          is_palindrome('Python'): False
          initials: T.Q.B.F.J.O.T.L.D.
          slugify: the-quick-brown-fox
 DESIGN : Every function takes text and returns text (or a number/bool).
          Nothing prints except main(), so each function is easy to test
          and to reuse.
 EXTEND : Add count_char(text, char, *, ignore_case=False).
=====================================================================
"""

DEFAULT_WIDTH = 20
DEFAULT_SUFFIX = "..."


def word_count(text: str) -> int:
    """Number of words separated by whitespace."""
    count = 0
    in_word = False
    for char in text:
        if char.isspace():
            in_word = False
        elif not in_word:
            in_word = True
            count += 1
    return count


def title_case(text: str) -> str:
    """Upper-case the first letter of every word."""
    result = ""
    previous = " "
    for char in text:
        result += char.upper() if previous.isspace() else char.lower()
        previous = char
    return result


def truncate(text: str, width: int = DEFAULT_WIDTH, *, suffix: str = DEFAULT_SUFFIX) -> str:
    """Cut text to at most ``width`` characters at a word boundary, adding ``suffix`` if cut."""
    if len(text) <= width:
        return text
    cut = text[: width - len(suffix) + 1]  # +1: peek one char to see if a word ends there
    last_space = cut.rfind(" ")
    # Drop the half-cut word; with no space at all (one long word), drop the peeked char.
    end = last_space if last_space > 0 else len(cut) - 1
    return cut[:end].rstrip() + suffix


def letters_only(text: str) -> str:
    """Lower-case letters, everything else removed."""
    result = ""
    for char in text:
        if char.isalpha():
            result += char.lower()
    return result


def is_palindrome(text: str) -> bool:
    """Reads the same backwards, ignoring case, spaces and punctuation."""
    cleaned = letters_only(text)
    return cleaned == cleaned[::-1]


def initials(text: str) -> str:
    """First letter of every word, upper-case, each followed by a dot."""
    result = ""
    for word in text.split():
        result += word[0].upper() + "."
    return result


def slugify(text: str, *, max_words: int | None = None) -> str:
    """Lower-case words joined by hyphens, for use in a URL."""
    words = text.lower().split()
    if max_words is not None:
        words = words[:max_words]
    return "-".join(words)


def main() -> None:
    sentence = "The quick brown fox jumps over the lazy dog"
    print("word_count:", word_count(sentence))
    print("title_case:", title_case(sentence))
    print("truncate:", truncate(sentence))
    print("truncate(width=12, suffix=' >>'):", truncate(sentence, width=12, suffix=" >>"))
    print("is_palindrome('Never odd or even'):", is_palindrome("Never odd or even"))
    print("is_palindrome('Python'):", is_palindrome("Python"))
    print("initials:", initials(sentence))
    print("slugify:", slugify(sentence, max_words=4))


if __name__ == "__main__":
    main()
