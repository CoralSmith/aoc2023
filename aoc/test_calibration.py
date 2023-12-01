import unittest
import os
from aoc.d01_calibration import main


class TestCalibration(unittest.TestCase):
    def test_calibration_part1(self):
        self.assertEqual(142, main(os.path.abspath('data/test_d1p1.txt')))

    def test_calibration_part2(self):   
        self.assertEqual(281, main(os.path.abspath('data/test_d1p2.txt')))