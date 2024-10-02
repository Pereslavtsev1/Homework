def solution(list1: list, list2: list):
    set1 = set(list1)
    set2 = set(list2)
    result = set1.intersection(set2)
    return sorted(list(result))


