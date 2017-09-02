import unittest
from unittest import TestCase
from book_list.book_list import BookList
import sqlite3


class TestBookList(TestCase):
    def setUp(self):
        self.con = sqlite3.connect(':memory:')
        self.cursor = self.con.cursor()

    def tearDown(self):
        self.con.close()

    def test_create_book_list_table(self):
        book_list = BookList(self.con)
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.assertEquals(self.cursor.fetchall(), [(u'book_list',)])

    def test_there_would_be_more_test_cases(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
