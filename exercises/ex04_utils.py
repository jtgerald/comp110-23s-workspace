"""List Utility Functions."""


__author__ = "730475086"


def all(num: list[int], desire: int) -> bool:
    """Given a list of ints, all should return a bool."""
    ind: int = 0
    if len(num) == 0:
        return False
    while len(num) > ind:
        if num[ind] == desire:
            ind += 1
        else:
            return False
    return True


def max(num2: list[int]) -> int:
    """Given a list of ints, max should return the largest."""
    ind: int = 0
    if len(num2) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        x: int = num2[ind]
        while len(num2) > ind + 1:
            if x < num2[ind + 1]:
                x = num2[ind + 1]
            ind += 1
        return x


def is_equal(num3: list[int], num4: list[int]) -> bool:
    """Given two lists of ints, returns True if every element is equal."""
    i: int = 0
    if len(num3) != len(num4):
        return False
    while i < len(num3):
        if num3[i] == num4[i]:
            i += 1
        else:
            return False
    return True