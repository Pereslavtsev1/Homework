import unittest

from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_ascending_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 6), 5)
        self.assertEqual(binary_search(arr, 10), -1)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 8)

    def test_descending_array(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(binary_search(arr, 6), 3)
        self.assertEqual(binary_search(arr, 10), -1)
        self.assertEqual(binary_search(arr, 9), 0)
        self.assertEqual(binary_search(arr, 1), 8)

    def test_empty_array(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)

    def test_single_element_array(self):
        arr = [1]
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 2), -1)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = binary_search(arr, 2)
        self.assertTrue(1 <= result <= 3)


if __name__ == "__main__":
    unittest.main()
