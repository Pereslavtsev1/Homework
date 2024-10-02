import pytest

from Problem_3 import calculate_max_pieces


def test_calculate_max_pieces_with_positive_number():
    assert calculate_max_pieces(3) == 7
    assert calculate_max_pieces(2) == 4
    assert calculate_max_pieces(0) == 1

def test_calculate_max_pieces_with_negative_number():
    with pytest.raises(RuntimeError, match="n can not be negative"):
        calculate_max_pieces(-1)
