"""EX04 'list' Utility Functions."""

__author__ = "730463283"

def all(num_list: list[int], num: int) -> bool:
    """The goal of this function is to identify if all the numbers in a list match the indicated number """
    idx: int = 0
    while idx < len(num_list):
        if num_list[idx] == num:
            idx = idx + 1
        else:
            return False
    return True
        

def max(max_list: list[int]) -> int:
    """This function determines the largest number in a list."""
    idx: int = 0
    max_v: int = 0
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    while idx < len(max_list):
        if max_list[idx] > max_v:
            max_v = max_list[idx]
        idx = idx + 1
    return max_v
        

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if list1 == list2:
        return True
    else:
        return False