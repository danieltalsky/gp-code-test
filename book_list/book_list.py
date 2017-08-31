from sqlite3 import Connection, Cursor
from pprint import pprint

class BookList:

    DELETE_TABLE_SQL = """DROP TABLE IF EXISTS book_list"""

    TABLE_CREATION_SQL = """
        CREATE TABLE IF NOT EXISTS book_list (
            id INTEGER PRIMARY KEY,
            book_title varchar(255), 
            author_first varchar(255), 
            author_last varchar(255), 
            publication_year varchar(4)
        )"""

    INSERT_BOOK_SQL = """
        INSERT INTO book_list (book_title, author_first, author_last, publication_year) VALUES (?, ? ,?, ?)
    """

    SELECT_BOOK_LIST_SQL = """SELECT book_title, author_first, author_last, publication_year FROM book_list {} ORDER BY {} {} """

    SELECT_BOOK_WHERE_CLAUSE = """
        WHERE book_title LIKE ? OR author_first LIKE ? OR author_last LIKE ? OR publication_year LIKE ?
    """

    BOOK_TITLE_FIELDNAME = 'book_title'
    AUTHOR_FIRST_FIELDNAME = 'author_first'
    AUTHOR_LAST_FIELDNAME = 'author_last'
    PUBLICATION_YEAR_FIELDNAME = 'publication_year'

    def __init__(self, db_handle):
        self.cursor = db_handle.cursor()
        self.create_book_list_table()
        pass
    __init__.__annotations__ = {'dbHandle': Connection}


    def create_book_list_table(self):
        self.cursor.execute(self.TABLE_CREATION_SQL)


    def insert_record(self, record):
        positional_record = (
            record['Book Title'].strip(),
            record['First Name'].strip(),
            record['Last Name'].strip(),
            record['Book Publication Date'].strip()
        )
        self.cursor.execute(self.INSERT_BOOK_SQL, positional_record)


    def query_book_list(self, filter=None, reverse=False, year=False):
        sort_field = self.PUBLICATION_YEAR_FIELDNAME if year else self.AUTHOR_LAST_FIELDNAME
        sort_direction = 'desc' if reverse else 'asc'
        filter = None
        if (filter != None):
            like = '%'+filter+'%'
            self.cursor.execute(self.SELECT_BOOK_LIST_SQL.format(self.SELECT_BOOK_WHERE_CLAUSE, sort_field, sort_direction),
                                (like, like, like, like))
        else:
            self.cursor.execute(self.SELECT_BOOK_LIST_SQL.format('', sort_field, sort_direction))

        self.cursor.execute('SELECT * FROM book_list')
        pprint(self.cursor.rowcount)
        #pprint(self.SELECT_BOOK_LIST_SQL.format('', sort_field, sort_direction))

    def get_record(self):
        if (self.cursor.rowcount < 1):
            record = None
        else:
            record = self.cursor.fetchone()
        return record
