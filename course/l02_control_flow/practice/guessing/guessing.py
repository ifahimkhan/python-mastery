"""
=====================================================================
 PRACTICE 02.C - Number guessing game (CLI)
=====================================================================
 GOAL   : Loop until the player finds the secret number, giving
          "higher" or "lower" hints and rejecting bad input.
 RUN    : uv run python -m course.l02_control_flow.practice.guessing.guessing
 OUTPUT : (example session: the secret is random, here it was 37)
          I'm thinking of a number from 1 to 100.
          Your guess: 50
          Too high!
          Your guess: abc
          'abc' is not a whole number from 1 to 100.
          Your guess: 25
          Too low!
          Your guess: 37
          Correct! You needed 3 guesses.
 DESIGN : judge() and parse_guess() have no input or output, so tests
          check them directly. play() gets the secret as an argument, so
          tests can pick it instead of relying on chance.
 NOTE   : Previews: `None` (level 05), `import random` (level 09).
 EXTEND : Give the player at most 7 guesses. Is 7 always enough for 1..100? Why?
=====================================================================
"""

import random

LOWEST = 1
HIGHEST = 100


def parse_guess(text: str) -> int | None:
    """The guess as a number, or None if it isn't a whole number in range."""
    text = text.strip()
    if not text.isdecimal():
        return None
    guess = int(text)
    if not LOWEST <= guess <= HIGHEST:
        return None
    return guess


def judge(guess: int, secret: int) -> str:
    if guess < secret:
        return "Too low!"
    if guess > secret:
        return "Too high!"
    return "Correct!"


def play(secret: int) -> int:
    """Runs one game and returns how many valid guesses it took."""
    print(f"I'm thinking of a number from {LOWEST} to {HIGHEST}.")
    guesses = 0
    while True:
        text = input("Your guess: ")
        guess = parse_guess(text)
        if guess is None:
            print(f"{text.strip()!r} is not a whole number from {LOWEST} to {HIGHEST}.")
            continue  # bad input doesn't count as a guess
        guesses += 1
        verdict = judge(guess, secret)
        if verdict == "Correct!":
            return guesses
        print(verdict)


def main() -> None:
    guesses = play(random.randint(LOWEST, HIGHEST))
    print(f"Correct! You needed {guesses} guesses.")


if __name__ == "__main__":
    main()
