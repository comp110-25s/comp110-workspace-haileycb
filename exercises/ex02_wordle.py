"""Coding a wordle!"""

__author__: str = "730562399"


def contains_char(word: str, letter: str) -> bool:
    """See if word contains character"""
    assert (
        len(letter) == 1
    ), f"len('{letter}') is not 1"  # error if input doesn't equal required length
    index: int = 0
    while index < len(word):
        if letter == word[index]:
            return True
        index += 1
    return False  # boolean return to check if the input letter is anywhere in the word


def emojified(guess: str, secret: str) -> str:
    """Emoji demonstration of letter and position validity"""
    assert len(guess) == len(
        secret
    ), "Guess must be same length as secret"  # error code if the lengths of the input word and secret are not the same
    index: int = 0  # starting the position check at the first letter
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # defining the variables which hold the emojis
    emojis: str = (
        ""  # starting a variable which will hold all of the emojis after evaluating each letter individually
    )
    while index < len(guess):
        if contains_char(secret, guess[index]) == False:
            emojis += WHITE_BOX
        else:
            if guess[index] != secret[index]:
                emojis += YELLOW_BOX
            else:
                emojis += GREEN_BOX
        index += 1  # moving on to check the next letter
    return emojis


def input_guess(N: int) -> str:
    guess: str = input(
        f"Enter a {N} character word:"
    )  # storing in a new variable as a string the input
    while len(guess) != N:
        guess = input(
            f"That wasn't {N} chars! Try again:"
        )  # storing a new value in the guess variable as they enter a new one
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # stores the turn number in a variable starting at the first turn
    secret_length: int = len(secret)
    print(f"=== Turn {turn}/6 ===")
    guess: str = input_guess(secret_length)
    print(emojified(guess, secret))
    while (
        guess != secret and turn < 6
    ):  # loop through different guesses to check if it's correct and within turns
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_length)
        print(emojified(guess, secret))
    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print(
            f"You won in {turn}/6 turns!"
        )  # if the guess matches the secret and is under the number of turns, it will print the number of guesses you got it in


if __name__ == "__main__":
    main(secret="codes")
