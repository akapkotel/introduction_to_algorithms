#!/usr/bin/env python
from typing import List


def insertion_sort(list_to_sort: List) -> List:
    list_to_sort = [e for e in list_to_sort]  # to avoid sorting in place, comment this to change original list
    for j in range(1, len(list_to_sort)):
        sorted_element = list_to_sort[j]
        # print('sorted element:', sorted_element)
        i = j - 1
        while i >= 0 and list_to_sort[i] > sorted_element:
            list_to_sort[i + 1] = list_to_sort[i]
            i -= 1
        list_to_sort[i + 1] = sorted_element
        # print('list after insertion:', list_to_sort)
    return list_to_sort


def reverse_sort(list_to_sort: List) -> List:
    """
    The same as insertion_sort, but order is reversed.
    :param list_to_sort: List
    :return: List
    """
    if len(list_to_sort) == 1:
        return list_to_sort
    list_to_sort = [e for e in list_to_sort]  # to avoid sorting in place, comment this to change original list
    for j in range(len(list_to_sort) - 2, -1, -1):
        sorted_element = list_to_sort[j]
        # print('sorted element:', sorted_element)
        i = j + 1
        while i < len(list_to_sort) and list_to_sort[i] > sorted_element:
            list_to_sort[i - 1] = list_to_sort[i]
            i += 1
        list_to_sort[i - 1] = sorted_element
        # print('list after insertion:', list_to_sort)
    return list_to_sort


def search_in_list(a_list: List, element: int) -> int:
    for i, x in enumerate(a_list):
        if x == element:
            return i


def selection_sort(list_to_sort: List) -> List:
    sorted_list = []
    # print(list_to_sort, sorted_list)
    while list_to_sort:
        smallest = 0
        for i, elem in enumerate(list_to_sort):
            if elem < list_to_sort[smallest]:
                smallest = i
        sorted_list.append(list_to_sort.pop(smallest))
        # print(list_to_sort, sorted_list)
    return sorted_list
