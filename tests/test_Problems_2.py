from Problem_2 import solution


def test():
    assert solution(5,[5,10]) == 7.5
    assert solution(0,[1,2,3,4,5]) == 4.03125
    assert solution(0,[5,4,3,2,1]) == 4.03125