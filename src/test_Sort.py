import unittest

from Sort import Sort


class TestSort(unittest.TestCase):
    def setUp(self):
        self.sorter = Sort()

    def test_bubble_sort_empty_array(self):
        self.assertEqual(self.sorter.bubble_sort([]), [])

    def test_bubble_sort_single_element(self):
        self.assertEqual(self.sorter.bubble_sort([1]), [1])

    def test_bubble_sort_already_sorted(self):
        self.assertEqual(self.sorter.bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_bubble_sort_reverse_sorted(self):
        self.assertEqual(self.sorter.bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_bubble_sort_duplicate_elements(self):
        self.assertEqual(self.sorter.bubble_sort([3, 1, 3, 2]), [1, 2, 3, 3])

    def test_bubble_sort_negative_numbers(self):
        self.assertEqual(self.sorter.bubble_sort(
            [-3, 5, -1, 0]), [-3, -1, 0, 5])

    def test_quick_sort_empty_array(self):
        self.assertEqual(self.sorter.quick_sort([]), [])

    def test_quick_sort_single_element(self):
        self.assertEqual(self.sorter.quick_sort([1]), [1])

    def test_quick_sort_already_sorted(self):
        self.assertEqual(self.sorter.quick_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_quick_sort_reverse_sorted(self):
        self.assertEqual(self.sorter.quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_quick_sort_duplicate_elements(self):
        self.assertEqual(self.sorter.quick_sort([3, 1, 3, 2]), [1, 2, 3, 3])

    def test_quick_sort_negative_numbers(self):
        self.assertEqual(self.sorter.quick_sort(
            [-3, 5, -1, 0]), [-3, -1, 0, 5])

    def test_quick_sort_all_same_elements(self):
        self.assertEqual(self.sorter.quick_sort([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_quick_sort_large_numbers(self):
        self.assertEqual(self.sorter.quick_sort(
            [1000, 1, 100, 10]), [1, 10, 100, 1000])

    def test_merge_sort_empty_array(self):
        self.assertEqual(self.sorter.merge_sort([]), [])

    def test_merge_sort_single_element(self):
        self.assertEqual(self.sorter.merge_sort([1]), [1])

    def test_merge_sort_already_sorted(self):
        self.assertEqual(self.sorter.merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_merge_sort_reverse_sorted(self):
        self.assertEqual(self.sorter.merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_merge_sort_duplicate_elements(self):
        self.assertEqual(self.sorter.merge_sort([3, 1, 3, 2]), [1, 2, 3, 3])

    def test_merge_sort_negative_numbers(self):
        self.assertEqual(self.sorter.merge_sort(
            [-3, 5, -1, 0]), [-3, -1, 0, 5])

    def test_merge_sort_all_same_elements(self):
        self.assertEqual(self.sorter.merge_sort([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_merge_sort_large_numbers(self):
        self.assertEqual(self.sorter.merge_sort(
            [1000, 1, 100, 10]), [1, 10, 100, 1000])

    def test_insertion_sort_normal_case(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(self.sorter.insertion_sort(arr), expected)

    def test_insertion_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.sorter.insertion_sort(arr), expected)

    def test_insertion_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.sorter.insertion_sort(arr), expected)

    def test_insertion_sort_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(self.sorter.insertion_sort(arr), expected)

    def test_insertion_sort_duplicate_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
        self.assertEqual(self.sorter.insertion_sort(arr), expected)

    def test_insertion_sort_negative_numbers(self):
        arr = [-5, -10, 0, -3, 8, -9, 1]
        expected = [-10, -9, -5, -3, 0, 1, 8]
        self.assertEqual(self.sorter.insertion_sort(arr), expected)


if __name__ == "__main__":
    unittest.main()
