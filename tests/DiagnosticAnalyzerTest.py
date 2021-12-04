import unittest
from src import diagnostic_analyzer

class DiagnosticAnalyzerTest(unittest.TestCase):

    def test_pilot(self):
        input_file = "/Users/brad/github/advent2021/input3a_small.txt"
        input = diagnostic_analyzer.read_inputs(input_file)
        power = diagnostic_analyzer.analyze_diagnostic(input)
        self.assertEqual(198, power)


if __name__ == '__main__':
    unittest.main()