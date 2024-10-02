def calculate_max_pieces(n):
    if n < 0:
        raise RuntimeError("n can not be negative")
    max_pieces = (n**2 + n + 2) // 2
    return max_pieces


def temp_function():
    n: int = input("input n: ")
    calculate_max_pieces(n)

