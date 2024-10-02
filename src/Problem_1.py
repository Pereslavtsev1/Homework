def focus(a: int, b: int, n: int):
    result = (((a + 1) * (b + 1)) - a - b - (a * b)) ** n
    return result


# Since raising 1 to any power always equals 1, the result will always be 1.
