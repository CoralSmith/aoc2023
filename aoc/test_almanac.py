import unittest
import os
from aoc.d05_almanac import main


class TestAlmanac(unittest.TestCase):
    def test_almanac_part1(self):
        self.assertEqual(35, main(os.path.abspath('data/test_d5.txt'))['part1'])

    def test_almanac_part2(self):
        self.assertEqual(46, main(os.path.abspath('data/test_d5.txt'))['part2'])
