"""Defining functions to use in my analysis notebook."""


def column_values(row_table: list[dict[str, str]], column: str) -> list[str]:
    """Makes a list of strings from a row."""
    result: list[str] = []

    for d in row_table:
        value: str = d[column]
        result.append(value)

    return result
