import unittest
from src import pilot

class PilotTest(unittest.TestCase):

    def test_pilot(self):
        input_file = "/Users/brad/github/advent2021/input2_small.txt"
        input = pilot.read_inputs(input_file)
        horiz_pos, depth = pilot.pilot(input)
        self.assertEqual(150, horiz_pos*depth)


if __name__ == '__main__':
    unittest.main()
