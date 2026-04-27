"""Test the functions from dictionary.py"""

__author__ = "730640030"

# unit tests for five functions.
import pytest
from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)

# pytest exercises/ex05/dictionary_test.py.


# invert
def test_invert_use() -> None:
    """Tests that invert actually inverts keys and values in a dict."""
    fowards: dict[str, str] = {"Ben": "Barber", "James": "Knight", "Mike": "Hardie"}

    assert invert(fowards) == {"Barber": "Ben", "Knight": "James", "Hardie": "Mike"}


def test_invert_use_2() -> None:
    """Tests that invert works on a different string"""
    fowards: dict[str, str] = {"x": "y", "z": "k", "m": "n"}

    assert invert(fowards) == {"y": "x", "k": "z", "n": "m"}


def test_invert_edge_empty() -> None:
    """Tests that invert works with an empty dictionary."""
    assert invert({}) == {}


def test_invert_edge_duplicate() -> None:
    """Tests whether the function correctly responses to duplicate values"""

    with pytest.raises(KeyError):
        my_dictionary = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(my_dictionary)


# favorite_color.
def test_favorite_color_use() -> None:
    """Tests that favorite_color returns the most common color."""
    favorites: dict[str, str] = {
        "Ben": "Yellow",
        "Kyle": "Brown",
        "James": "Brown",
        "Jeff": "Red",
    }

    assert favorite_color(favorites) == "Brown"


def test_favorite_color_tie_use() -> None:
    """Tests that in a tie, favorite_color returns the color first mentioned."""
    favorites: dict[str, str] = {
        "Ben": "Yellow",
        "Kyle": "Brown",
        "James": "Brown",
        "Jeff": "Red",
        "Alex": "Yellow",
    }

    assert favorite_color(favorites) == "Yellow"


def test_favorite_color_empty_edge() -> None:
    """Edge case that tests whether the function works when empty."""
    assert favorite_color({}) == ""


# count.
def test_count_use() -> None:
    """Tests that count returns a dict of counted unique values from a given list"""
    test: list[str] = ["x", "y", "z", "x", "y", "x"]

    assert count(test) == {"x": 3, "y": 2, "z": 1}


def test_count_use_same() -> None:
    """Tests that count returns a dict of counted unique values from a list of the same exact strings."""
    test: list[str] = ["x", "x", "x", "x", "x"]

    assert count(test) == {"x": 5}


def test_count_edge_empty() -> None:
    """Tests that count returns an empty list when given an empty list."""
    test: list[str] = []

    assert count(test) == {}


# alphabetizer.
def test_alphabetizer_use() -> None:
    test: list[str] = ["dog", "cat", "drink", "cookie", "zebra"]

    assert alphabetizer(test) == {
        "d": ["dog", "drink"],
        "c": ["cat", "cookie"],
        "z": ["zebra"],
    }


def test_alphabetizer_use_lower() -> None:
    """Tests that the function returns the letters as lowercase in the dictorionary."""
    test: list[str] = ["Dog", "Cat", "Drink", "Cookie", "Zebra"]

    assert alphabetizer(test) == {
        "d": ["Dog", "Drink"],
        "c": ["Cat", "Cookie"],
        "z": ["Zebra"],
    }


def test_alphabetizer_edge_empty() -> None:
    """Tests the edge case of an input of an empty list"""
    test: list[str] = []

    assert alphabetizer(test) == {}


# update_attendance.


def test_update_attendance_existing_day_use() -> None:
    """Adds a person to an already existing day, tests that log is updated accordingly"""
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}

    update_attendance(log, "Monday", "Mike")

    assert log == {"Monday": ["Vrinda", "Kaleb", "Mike"], "Tuesday": ["Alyssa"]}


def test_update_attendance_day_new_use() -> None:
    """Adds a person to a new day, tests that log is updated accordingly"""
    log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}

    update_attendance(log, "Wednesday", "Ben")

    assert log == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa"],
        "Wednesday": ["Ben"],
    }


def test_update_attendance_edge_empty_addition() -> None:
    """Tests that an empty case can be added to and give the expected output."""
    log: dict[str, list[str]] = {}

    update_attendance(log, "Wednesday", "Ben")

    assert log == {"Wednesday": ["Ben"]}
