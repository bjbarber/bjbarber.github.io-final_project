"""Data related utility functions."""

__author__ = ["730640030", "730735849"]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted


"""These are the functions we wrote/will write in class!"""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Takes the first n rows from data table and populates it in a new dict()."""
    shortened_data_table: dict[str, list[str]] = {}
    # {} or dict() implements empty dict.

    for key in data_table:
        shortened_data_table[key] = data_table[key][:n]
        # appends key and corresponding list[str].
        # [:n] takes the lists in datatable[key] up to n value, including n.
        # key represents the title of list; list is vertically oriented so [:n] takes n rows from that list.

    return shortened_data_table


def select(data_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Takes a list of names, corresponding to each column, and populates those names as str for list of rows."""
    new_table: dict[str, list[str]] = {}

    for key in data_table:
        if key in names:
            new_table[key] = data_table[key]

    return new_table


def concat(
    table1: dict[str, list[str]], table2: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Creates a column based-table based from two different column-based tables."""
    new_table: dict[str, list[str]] = {}

    for key in table1:
        new_table[key] = table1[key][:]
        # makes a new table that is exactly the same as table 1.
        # [:] slices value from list so it is independent/a copy, creating an entirely new list with new references.

    for key in table2:
        if key in new_table:
            new_table[key] += table2[key]
            # you only use append when adding a single element to a list.
            # += allows us to add the full list.

        else:
            new_table[key] = table2[key][:]

    return new_table


def count(input: list[str]) -> dict[str, int]:
    """Takes a list (column) and counts how many times a particular string is present in that list, storing the information as a dict()."""
    count: dict[str, int] = {}

    for key in input:
        if key in count:
            count[key] += 1
        else:
            count[key] = 1

    return count


def count_attendance(input: list[str]) -> int:
    """Takes a list, representing a single column in the dataset, and counts every int value that does not equal zero."""

    attended: int = 0

    for key in input:
        if key != "0":
            attended += 1

    return attended
