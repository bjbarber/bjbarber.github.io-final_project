"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730640030"


def input_word() -> str:
    """This function calls the user to enter a 5-character word and determines whether it is 5 characters or not"""
    word = input("Enter a 5-character word: ")

    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()

    return word


""" Took a minute to figure out the code for this. However, after looking over notes I realized it was much simpler than I realized. I did not realize I just needed to call input_word() in the trailhead to call the fn and it worked well."""


def input_letter() -> str:
    """This function calls the user to enter a single character and determines whether it is a single character or not"""
    letter = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Tells us at what indexes matching letters are found."""
    print("Searching for", letter, "in", word)

    count: int = 0
    """Establishes a counter"""

    if letter == word[0]:
        print(letter, "found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter, "found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter, "found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter, "found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter, "found at index 4")
        count = count + 1

    if count == 0:
        print("No instances of", letter, "found in", word)
    elif count == 1:
        print("1 instance of", letter, "found in", word)
    else:
        print(count, "instances of", letter, "found in", word)


"""This was definitely the hardest funtion to write in the program. I had attempted this part before the previous lecture, but after the lecture on Thursday, I realized I could make variables that added onto each other to count letters. Also the elif part of if,else made the code much simpler at the end."""


def main() -> None:
    """This function calls on all other functions."""
    return contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    """This function calls on the function to start the program, when the program is initially run."""
    main()
