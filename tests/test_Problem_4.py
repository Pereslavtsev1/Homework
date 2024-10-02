from Problem_4 import solution


def test():
    test1 = [2, 6, 12]
    assert (solution([2, 4, 6, 8, 10, 12, 10, 8, 6, 4],[2, 3, 6, 9, 12, 15, 18]) == test1)
    assert solution([], []) == []
    assert solution([1, 2, 4, 5], [1, 2, 4, 5]) == [1, 2, 4, 5]
    assert solution([1, 2, 3], [1, 2, 3, 4, 5, 6]) == [1, 2, 3]
    assert solution([1, 2, 3, 4, 5, 6], [1, 2, 3]) == [1, 2, 3]