def isProfitable(balance: int, temp: int) -> bool:
    return (balance + temp) / 2 > balance


def temp_function():
    n = int(input("Count:"))
    if n < 0:
        raise RuntimeError("Count can not be negative")
    s = input()
    s = list(map(int, s.split(" ")))

    balance = int(input("Balance:"))
    if balance < 0:
        raise RuntimeError("Balance can not be negative")
    return solution(balance, s)


def solution(balance: int, array: list) -> float:
    array = sorted(array)
    for i in array:
        if i < 0:
            raise RuntimeError("Husband balance can not be negative")
        if isProfitable(balance, i):
            balance = (balance + i) / 2
    return balance


print(solution(5,[5,10]))