from unittest import TestCase, main
from sorting.sorting_algorithms import insertion_sort, reverse_sort, search_in_list, selection_sort


class Test(TestCase):

    def setUp(self) -> None:
        self.list_to_sort = [7, 2, 5, 12, 4, 11, 16, 25, 10, 1, 3, 8]
        self.sorted_list = [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 16, 25]
        self.sorted_reversely = [25, 16, 12, 11, 10, 8, 7, 5, 4, 3, 2, 1]

    def tearDown(self) -> None:
        self.list_to_sort.clear()

    def test_insertion_sort(self):
        sorted_list = insertion_sort(self.list_to_sort)
        self.assertEqual(sorted_list, self.sorted_list)

    def test_reverse_sort(self):
        sorted_list = reverse_sort(self.list_to_sort)
        self.assertEqual(sorted_list, self.sorted_reversely)

    def test_search_in_list(self):
        target = 5
        index = 2
        result = search_in_list(self.list_to_sort, target)
        self.assertEqual(index, result)

    def test_search_in_list_for_nonexistent(self):
        target = 50
        index = None
        result = search_in_list(self.list_to_sort, target)
        self.assertEqual(index, result)

    def test_selection_sort(self):
        result = selection_sort(self.list_to_sort)
        self.assertEqual(self.sorted_list, result)


if __name__ == '__main__':
    main()
