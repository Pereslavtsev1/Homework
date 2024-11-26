class Sort:

    def bubble_sort(self, array):
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def quick_sort(self, array: list):
        self.__quick_sort_helper(array, 0, len(array) - 1)
        return array

    def __quick_sort_helper(self, array: list, low, high):
        s = low
        e = high
        if s >= e:
            return
        m = s + (e - s) // 2
        pivot = array[m]

        while s <= e:
            while array[s] < pivot:
                s += 1
            while array[e] > pivot:
                e -= 1
            if s <= e:
                array[s], array[e] = array[e], array[s]
                s += 1
                e -= 1

        self.__quick_sort_helper(array, low, e)
        self.__quick_sort_helper(array, s, high)

    def insertion_sort(self, array):
        for i in range(len(array)):
            j = i - 1
            key = array[i]
            while array[j] > key and j >= 0:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def merge_sort(self, array):
        self.__mergeSort(array, 0, len(array) - 1)
        return array

    def __mergeSort(self, array, l, r):
        if l >= r:
            return

        mid = (l + r) // 2
        self.__mergeSort(array, l, mid)
        self.__mergeSort(array, mid + 1, r)

        left = array[l: mid + 1]
        right = array[mid + 1: r + 1]

        i = j = 0
        k = l

        while i < len(left) or j < len(right):
            if i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            else:
                if i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1
                else:
                    array[k] = right[j]
                    j += 1
                    k += 1
