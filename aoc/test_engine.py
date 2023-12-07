import unittest
import os
from aoc.d03_engines import main


class TestEngines(unittest.TestCase):
    def test_engines_part1(self):
        self.assertEqual(4361, main(os.path.abspath('data/test_d3p1.txt'))['parts'])
    
    def test_engines_part2(self):
        self.assertEqual(467835, main(os.path.abspath('data/test_d3p1.txt'))['ratio'])
    
