import unittest
from src import depth_measurer


class DepthMeasurerTest(unittest.TestCase):

    def test_calculate_depth_changes(self):
        input_file = "/Users/brad/github/advent2021/input1_small.txt"
        measurements = depth_measurer.read_inputs(input_file)
        count = depth_measurer.calculate_depth_changes(measurements)
        self.assertEqual(7, count)

    def test_calculate_window_changes(self):
        input_file = "/Users/brad/github/advent2021/input1b_small.txt"
        measurements = depth_measurer.read_inputs(input_file)
        count = depth_measurer.calculate_window_changes(measurements)
        self.assertEqual(5, count)


if __name__ == "__main__":
    unittest.main()