"""This is where I will implement my function skeletons and implementations."""

__author__ = "730463283"

def only_evens(evnum: list[int]) -> list[int]:
    "This function will return only the even values."
    idx: int = 0
    even_list = []
    while idx < len(evnum):
        if evnum[idx] % 2 == 0:
            even_list.append (evnum[idx])
            idx = idx + 1
        else:
            idx = idx+ 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    "This function will put two list into one list without modifying either list."
    concat_list = []
    concat_list = list1 + list2
    return concat_list


def sub(subnum: list[int], start: int, end: int) -> list[int]:
    "This function will return numbers only between the start and end index points."
    sub_list: list[int] = []
    idx: int = 0
    if start < 0:
        start = 0
    if end > len(subnum) + 1:
        end = len(subnum) + 1
    if len(subnum) == 0:
        return sub_list
    else:
        while idx < len(subnum):
            if idx >= start and idx <= end - 1:
                sub_list.append(subnum[idx])
            idx = idx + 1
        return sub_list