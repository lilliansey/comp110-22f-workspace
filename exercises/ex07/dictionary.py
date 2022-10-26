"""EX07 - Dictionary Functions."""

__author__ = "730463283"


def invert(variables: dict[str, str]) -> dict[str, str]:
    """This function will invert the values and keys of a dictionary."""
    final_dict: dict[str, str] = {}
    for key in variables:
        if variables[key] in final_dict:
            raise KeyError("Opps! You have entered duplicatr keys.")
        else:
            final_dict[variables[key]] = key
    return final_dict


def favorite_color(option: dict[str, str]) -> str:
    """The function will assess a list of colors and determine the most popular."""
    most_color: str = ""
    values: list[str] = []
    for name in option:
        values.append(option[name])
    new_dict: dict[str, int] = count(values)
    max: int = 0
    for color in new_dict:
        if new_dict[color] > max:
            max = new_dict[color]
    for final in new_dict:
        if new_dict[final] == max:
            return final
    return most_color
            

def count(number: list[str]) -> dict[str, int]:
    """This function will count the number of times a value appears in an inputted list."""
    empty: dict[str, int] = {}
    i: int = 0
    while i < len(number):
        if number[i] in empty:
            empty[number[i]] += 1
        else:
            empty[number[i]] = 1
        i += 1
    return empty