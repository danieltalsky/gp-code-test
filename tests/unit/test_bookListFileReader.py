import unittest
from unittest import TestCase
from book_list.book_list_file_reader import BookListFileReader
import os


class TestBookListFileReader(TestCase):
    def setUp(self):
        self.fixture_dir = os.path.dirname(os.path.realpath(__file__))
        self.source = self.fixture_dir + "/../../code-test-source-files/pipe"
        self.reader = BookListFileReader(self.source, 'pipe')

    def test_get_result_for_pipe_format(self):
        rec = self.reader.get_result()
        self.assertEquals(rec, {'Book Publication Date': ' 2002', 'Book Title': ' Test-Driven Development ',
                                'First Name': 'Kent ', 'Last Name': ' Beck '})

    def tests___there_would_be_more_of_them(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
