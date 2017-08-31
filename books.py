#!/usr/bin/env python

import argparse
import sqlite3
from pprint import pprint

from book_list.book_list_file_reader import BookListFileReader
from book_list.book_list import BookList

# Config
SQLITE3_DB_FILE = './db/booklist.sqlite3'
file_import_list = {
    'csv' : './code-test-source-files/csv',
    'pipe' : './code-test-source-files/pipe',
    'slash' : './code-test-source-files/slash',
}

# Command line parsing
parser = argparse.ArgumentParser(
    prog='Read multiple formats of book data and display them filtered and sorted.'
)
parser.add_argument('--filter', action='store', default=None,
                    help='show a subset of books, looks for the argument as a substring of any of the fields')
parser.add_argument('--year', action='store_true', default=False,
                    help="sort the books by year, ascending instead of default sort")
parser.add_argument('--reverse', action='store_true', default=False,
                    help='reverse sort')
args = parser.parse_args()

# Read files and populate book list
sqlite3_connection = sqlite3.Connection(SQLITE3_DB_FILE);
book_list = BookList(sqlite3_connection)
for parse_type, file_path in file_import_list.iteritems():
    reader = BookListFileReader(file_path, parse_type)
    while True:
        row = reader.get_result()
        if row == None:
            break
        book_list.insert_record(row)

# Make query based on command line arguments
book_list.query_book_list(filter=args.filter, year=args.year, reverse=args.reverse)

# Output
while True:
    row = book_list.get_record()
    if row == None:
        break
    pprint(row)