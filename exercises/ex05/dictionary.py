"""Practice with Dictionary Functions"""

__author__ = "730640030"


def invert(fowards: dict[str, str]) -> dict[str, str]:
    """Swaps every key and value into a new dictionary."""
    inverted: dict[str, str] = {}
    for key in fowards:
        value: str = fowards[key]
        if value in inverted:
            raise KeyError("Duplicate Values! Try a new list.")
        inverted[value] = key
    return inverted


"""Had trouble understanding how to add elements to a dictionary; I realized it goes by dict name[key] = value. To check for duplicate values, I realized the if ... in would check to see if the new key contained dupicates."""


def favorite_color(a: dict[str, str]) -> str:
    """Takes a dictionary of people and their favorite colors and returns the most repeated favorite number. In a tie, return the color that comes first."""
    count: dict[str, int] = {}
    for x in a:
        color: str = a[x]
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
    maximum: int = 0
    favorite: str = ""
    for color in count:
        if count[color] > maximum:
            maximum = count[color]
            favorite = color
    return favorite


"""I struggled to work out the logic for this; especially for picking the color that came first when there was a tie. I realized that by making a maximum variable, I could use boolean operators so that in a tie, the second would never become the favorite."""


def count(a: list[str]) -> dict[str, int]:
    """Takes unique values (str) from a list and counts them in a dictionary."""
    result: dict[str, int] = {}
    for x in a:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


"""Because we're taking a list, we access the value by just writing the element."""


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    """Takes the first letter from every word in a list and groups them by that letter as a dictionary."""
    result: dict[str, list[str]] = {}
    for x in a:
        key: str = x[0].lower()
        if x.isalpha():
            if key in result:
                result[key].append(x)
            else:
                result[key] = [x]
    return result


"""Making a variable for x[0].lower() made the code much more organized. I was having difficulty following it before."""


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Takes a dictionary of a day and list of students, and adds a student on a given day."""
    if day in attendance_log:
        attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]


"""When adding a new key to this list for a new day, the value needs to be written in bracket since it is a list."""
