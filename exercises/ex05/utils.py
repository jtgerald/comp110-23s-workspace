"""List Utility Functions."""

__author__ = "730475086"


def only_evens(integers: list[int]) -> list[int]:
    """Function that returns only even integers within the given list."""
    result: list[int] = list()
    for item in integers:
        if item % 2 == 0:
            result.append(item)
    return result


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Function that combines two lists."""
    result: list[int] = list()
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result


def sub(integers: list[int], start_index: int, end_index: int) -> list[int]:
    """Function that returns the items between two indices within the given list."""
    result: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > len(integers):
        end_index = len(integers)
    if integers == 0 or start_index > len(integers) or end_index <= 0:
        return result
    while start_index < end_index:
        result.append(integers[start_index])
        start_index += 1
    return result