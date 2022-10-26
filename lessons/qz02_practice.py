def odd_and_even(list_1: list[int]) -> list[int]:
    """Will return an odd number with an even index."""
    for num in list_1:
        if num % 2 != 1:
            list_1[num].pop
    i: int = 0
    while i < len[list_1]:
        if i % 2 != 0:
            list_1[i].pop
    return list_1