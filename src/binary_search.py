def binary_search(array: list, target):
    desc = False
    if len(array) == 0:
        return -1
    if array[0] > array[len(array) - 1]:
        desc = True
    return binary_search_helper(array, target, 0, len(array) - 1, desc)


def binary_search_helper(
    array: list, target: int, start: int, end: int, desc: bool
) -> int:
    if start > end:
        return -1

    m = start + (end - start) // 2

    if array[m] == target:
        return m

    if desc:
        if array[m] < target:
            return binary_search_helper(array, target, start, m - 1, desc)
        return binary_search_helper(array, target, m + 1, end, desc)
    else:
        if array[m] > target:
            return binary_search_helper(array, target, start, m - 1, desc)
        return binary_search_helper(array, target, m + 1, end, desc)
