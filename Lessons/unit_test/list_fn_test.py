"""Tests the list functions."""

# import list functions by writing:
from Lessons.unit_test.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first_names_output() -> None:
    """Test get first with names in a list for output."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    assert get_first(names) == "Alyssa"


# if the function is working properly, it should be true!


def test_get_and_remove_first_names_output() -> None:
    """Test get and remove first with names in a list for output."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    assert get_and_remove_first(names) == "Alyssa"


def test_remove_first_names_behavior() -> None:
    """Test remove first behavior on names."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    remove_first(names)
    assert names == ["Izzi", "Anusha", "Benjamin"]
    # asserts only the first entry was removed but we still have everything else.


def test_get_and_remove_first_names_behavior() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    get_and_remove_first(names)
    assert names == ["Izzi", "Anusha", "Benjamin"]


def test_get_first_names_behavior() -> None:
    """Test get first behavior on names"""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    get_first(names)
    assert names == ["Alyssa", "Izzi", "Anusha", "Benjamin"]
    # makes sure that names is still equal to the same thing.


# syntax for running unit test: python -m pytest path/to/testfile.py

#edge case
def test_get_first_empty_output() -> None:
    
    assert get_first([]) == IndexError