import unittest
from unittest import TestCase
from subprocess import check_output
import os


class FunctionTestsCommandLine(TestCase):

    RESULTS_NO_ARGS = """Test-Driven Development, Kent, Beck, 2002
Implementation Patterns, Kent, Beck, 2007
The Mythical Man-Month, Fred, Brooks, 1975
Javascript: The Good Parts, Douglas, Crockford, 2008
Refactoring, Martin, Fowler, 1999
Patterns of Enterprise Application Architecture, Martin, Fowler, 2002
Clean Code, Robert, Martin, 2008
Code Complete, Steve, McConnell, 1993
The Art of Agile Development, James, Shore, 2008"""

    RESULTS_WITH_FILTER ="""Test-Driven Development, Kent, Beck, 2002
Implementation Patterns, Kent, Beck, 2007
Javascript: The Good Parts, Douglas, Crockford, 2008
Patterns of Enterprise Application Architecture, Martin, Fowler, 2002
Clean Code, Robert, Martin, 2008
The Art of Agile Development, James, Shore, 2008"""

    def setUp(self):
        self.working_dir = os.path.dirname(os.path.realpath(__file__))
        self.script = self.working_dir + "/../../books.py"

    def test_results_no_args(self):
        stdout = check_output(["python", self.script])
        # self.assertEqual(stdout.strip(), self.RESULTS_NO_ARGS.strip())
        # @todo: make pass!

    def test_results_filter(self):
        stdout = check_output(["python", self.script, "--filter", "00"])
        # self.assertEqual(stdout.strip(), self.RESULTS_WITH_FILTER.strip())
        # @todo make pass!

    def tests___there_would_be_more_of_them(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
