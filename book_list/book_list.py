from sqlite3 import Connection, Cursor


class BookList:

    TABLE_CREATION_SQL = """
        CREATE TABLE IF NOT EXISTS book_list (
            id INTEGER PRIMARY KEY,
            book_title varchar(255), 
            author_first varchar(255), 
            author_last varchar(255), 
            publication_year varchar(4)
        );"""

    INSERT_BOOK_SQL = """
        INSERT INTO book_list (book_title, author_first, author_last, publication_year) VALUES (?, ? ,?, ?);
    );"""

    BOOK_TITLE_FIELDNAME = 'book_title'
    AUTHOR_FIRST_FIELDNAME = 'author_first'
    AUTHOR_LAST_FIELDNAME = 'author_last'
    PUBLICATION_YEAR_FIELDNAME = 'publication_year'

    def __init__(self, db_handle):
        self.cursor = db_handle.cursor()
        self.create_book_list_table()
        pass
    __init__.__annotations__ = {'dbHandle': Connection}

    def query_book_list(self, filter_string=None, sort_by=BOOK_TITLE_FIELDNAME, sort_ascending=True):
        pass

    def get_record(self):
        if (self.cursor.rowcount < 1):
            record = None
        else:
            record = self.cursor.fetchone()
        return record


    def read(self):
        pass

    def create_book_list_table(self):
        self.cursor.execute(self.TABLE_CREATION_SQL)
        pass

    def insert_record(self, record):
        positional_record = tuple(
            record['Book Title'],
            record['First Name'],
            record['Last Name'],
            record['Book Publication Date']
        )
        self.cursor.execute(self.INSERT_BOOK_SQL, positional_record)
        pass