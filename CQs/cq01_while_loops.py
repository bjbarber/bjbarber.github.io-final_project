"""First challenge question of the semester: while loops"""

__author__ = "730640030"


def num_instances(phrase: str, search_char: str) -> int:
    """Takes a phrase and returns the number of times a character occurs."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        """We use < instead of <= because index starts at 0, since if phrase is "hello" and index = 4, already count = 5 and len = 5."""
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1
    return count


def get_evens(numbers: str) -> str:
    """Takes a string of integers and returns a string of only the even integers."""
    index: int = 0
    evens: str = ""
    holder: str = ""
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            holder = numbers[index]
            evens = evens + holder
            index = index + 1
        else:
            index = index + 1
    return evens
