import csv


class BookListFileReader:
    """
    Opens a string-delimited (CSV) file and outputs an iterator
    """
    DELIMITERS = {
        'csv': ',',
        'pipe': '|',
        'slash': '/',
    }

    FIELD_ORDER = {
        'csv': ['Book Title', 'Last Name', 'First Name', 'Book Publication Date'],
        'pipe': ['First Name', 'Last Name', 'Book Title', 'Book Publication Date'],
        'slash': ['Book Publication Date', 'First Name', 'Last Name', 'Book Title'],
    }

    def __init__(self, file_path, input_file_type='csv'):
        self.reader = None
        self.file_path = file_path
        if input_file_type in self.DELIMITERS.keys():
            self.input_file_type = input_file_type
        else:
            raise ValueError('Type: {} is not a valid input file type.'.format(input_file_type))

    def get_result(self):
        """
        Get the next CSV result and normalize as a dict with the correct headers
        :return:
        """
        if (self.reader == None):
            csvfile = open(self.file_path)
            self.reader = csv.reader(csvfile, delimiter=self.DELIMITERS[self.input_file_type])
        try:
            row = dict(zip(
                self.FIELD_ORDER[self.input_file_type],
                self.reader.next())
            )
            return row
        except StopIteration:
            return None
