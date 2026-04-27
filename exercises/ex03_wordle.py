"""A complete Wordle game!"""

__author__ = "730640030"


def input_guess(secret_word_len: int) -> str:
    """Takes a word length and asks for a word of that length, continuing to ask until the correct lengthed word is given."""
    word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


"""This function was difficult to figure out as I struggled to tie the variable word to an input. I realized I did not have to use the print function, which solved the issue entirely."""


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Takes one parameter and chekcs if the other, single letter parameter is within it, evaluating to a boolean."""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index = index + 1
    return False


def emojified(word_guess: str, secret: str) -> str:
    """Compares two strings of equal length(guess and secret word), returing emojis based on how accurate the guess is."""
    assert len(secret) == len(word_guess)
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    WHITE_BOX: str = "\U00002b1c"
    index: int = 0
    result: str = ""
    while index < len(secret):
        if secret[index] == word_guess[index]:
            result = result + GREEN_BOX
        elif contains_char(secret, word_guess[index]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        index = index + 1
    return result


"""I briefly struggled to add together the colors; but I realized if I used the variable index and the index function, the colors would simply add together as it moved through every letter of the word."""


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn = turn + 1
    return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
