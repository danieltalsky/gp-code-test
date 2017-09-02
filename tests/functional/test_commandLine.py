import unittest
from unittest import TestCase
from subprocess import check_output
import os


class FunctionTestsCommandLine(TestCase):
    RESULTS_EXAMPLE_1 ="""McConnell, Steve, Code Complete, 1993
Fowler, Martin, Refactoring, 1999"""

    RESULTS_EXAMPLE_2 = """Fowler, Martin, Refactoring, 1999
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Beck, Kent, Implementation Patterns, 2007
Martin, Robert, Clean Code, 2008"""

    RESULTS_EXAMPLE_3 = """Beck, Kent, Test-Driven Development, 2002
Beck, Kent, Implementation Patterns, 2007
Brooks, Fred, The Mythical Man-Month, 1975
Crockford, Douglas, Javascript: The Good Parts, 2008
Fowler, Martin, Refactoring, 1999
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Martin, Robert, Clean Code, 2008
McConnell, Steve, Code Complete, 1993
Shore, James, The Art of Agile Development, 2008"""

    RESULTS_WITH_FILTER = """Beck, Kent, Test-Driven Development, 2002
Beck, Kent, Implementation Patterns, 2007
Crockford, Douglas, Javascript: The Good Parts, 2008
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Martin, Robert, Clean Code, 2008
Shore, James, The Art of Agile Development, 2008"""

    def setUp(self):
        self.working_dir = os.path.dirname(os.path.realpath(__file__))
        self.script = self.working_dir + "/../../books.py"

    def test_sample_output_in_readme_txt(self):
        # example 1
        stdout = check_output(["python", self.script, "--filter", "199", "--reverse"])
        self.assertEqual(stdout.strip(), self.RESULTS_EXAMPLE_1.strip())

        # example 2
        stdout = check_output(["python", self.script, "--filter", "er", "--year"])
        # print(stdout.strip())
        self.assertEqual(stdout.strip(), self.RESULTS_EXAMPLE_2.strip())

        # example 3
        stdout = check_output(["python", self.script])
        self.assertEqual(stdout.strip(), self.RESULTS_EXAMPLE_3.strip())

    def test_results_filter(self):
        stdout = check_output(["python", self.script, "--filter", "00"])
        self.assertEqual(stdout.strip(), self.RESULTS_WITH_FILTER.strip())

    def tests___there_would_be_more_of_them(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
