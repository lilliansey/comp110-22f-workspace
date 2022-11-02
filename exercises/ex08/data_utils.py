"""Dictionary related utility functions."""

__author__ = "730463283"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # One a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
   
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column whose name is the second parameter."""
    col_val: list[str] = []
    for row in table:
        item: str = row[column]
        col_val.append(item)
    return col_val


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of a data for each column."""
    result: dict[str, list[str]] = {}
    # THIS IS HAVING ISSUES
    for first in table:
        list_1: list[str] = []
        i: int = 0
        a: list[str] = table[first]
        if rows >= len(table[first]):
            result[first] = a
        else:
            while i < rows:
                list_1.append(a[i])
                i += 1
            result[first] = list_1
    return result


def select(column: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for i in name:
        result[i] = column[i]
    
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    combined_dict: dict[str, list[str]] = {}
    for i in table1:
        store_table: list[str] = table1[i]
        combined_dict[i] = store_table
    for i in table2:
        store_table2: list[str] = table2[i]
        if i in combined_dict:
            combined_dict[i] += store_table2
        else:
            combined_dict[i] = store_table2
    return combined_dict


def count(freq: list[str]) -> dict[str, int:]:
    """This function will produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input this."""
    result: dict[str, int] = {}
    for item in freq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result