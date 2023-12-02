import unittest
import os
from aoc.d02_cubes import main


class TestCubes(unittest.TestCase):
    def test_cubes_part1(self):
        self.assertEqual(8, main(os.path.abspath('data/test_d2p1.txt'))['possible'])
    
    def test_cubes_part2(self):
        self.assertEqual(2286, main(os.path.abspath('data/test_d2p1.txt'))['power'])