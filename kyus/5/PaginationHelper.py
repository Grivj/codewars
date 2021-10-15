"""
    For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

    The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

    The following are some examples of how this class is used:

    helper = PaginationHelper(['a','b','c','d','e','f'], 4)
    helper.page_count() # should == 2
    helper.item_count() # should == 6
    helper.page_item_count(0)  # should == 4
    helper.page_item_count(1) # last page - should == 2
    helper.page_item_count(2) # should == -1 since the page is invalid

    # page_index takes an item index and returns the page that it belongs on
    helper.page_index(5) # should == 1 (zero based index)
    helper.page_index(2) # should == 0
    helper.page_index(20) # should == -1
    helper.page_index(-10) # should == -1 because negative indexes are invalid
"""


import unittest
from math import ceil
from typing import List


class PaginationHelper:

    def __init__(self, collection: List[any], items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self) -> int:
        """Returns the number of items within the entire collection."""
        return len(self.collection)

    def page_count(self) -> int:
        """Returns the number of pages."""
        return ceil(len(self.collection) / self.items_per_page)

    def page_item_count(self, page_index) -> int:
        """
        Returns the number of items on the current page. page_index is zero based.
        This method should return -1 for page_index values that are out of range
        """
        page_count = self.page_count()
        if 0 < page_index > page_count - 1:
            return -1

        if page_index < page_count - 1:
            return self.items_per_page

        return (self.item_count() - (page_index * self.items_per_page))

    def page_index(self, item_index) -> int:
        """
        Determines what page an item is on. Zero based indexes.
        This method should return -1 for item_index values that are out of range.
        """
        if item_index not in range(len(self.collection)):
            return -1

        return item_index % self.page_count()


class TestPaginationHelper(unittest.TestCase):
    def basic_tests(self):
        collection = range(1, 25)
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.page_count(), 3,
                         'page_count is returning incorrect value.')
        self.assertEqual(helper.page_index(23), 2,
                         'page_index returned incorrect value')
        self.assertEqual(helper.item_count(), 24,
                         'item_count returned incorrect value')

    def examples_tests(self):
        helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        self.assertEqual(helper.page_count(), 2,
                         'page_count is returning incorrect value.')
        self.assertEqual(helper.item_count(), 6,
                         'item_count is returning incorrect value.')
        self.assertEqual(helper.page_item_count(0), 4,
                         'page_item_count returned incorrect value')
        self.assertEqual(helper.page_item_count(1), 2,
                         'page_item_count returned incorrect value')
        self.assertEqual(helper.page_item_count(2), -1,
                         'page_item_count returned incorrect value')
        self.assertEqual(helper.page_index(5), 1,
                         'page_index returned incorrect value')
        self.assertEqual(helper.page_index(2), 0,
                         'page_index returned incorrect value')
        self.assertEqual(helper.page_index(20), -1,
                         'page_index returned incorrect value')
        self.assertEqual(helper.page_index(-10), -1,
                         'page_index returned incorrect value')


def main():
    test = TestPaginationHelper()
    test.examples_tests()
    test.basic_tests()


if __name__ == '__main__':
    main()
