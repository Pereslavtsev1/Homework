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


if __name__ == "__main__":
    unittest.main()
