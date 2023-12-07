import unittest
import os
from aoc.d04_scratchcards import main


class TestScratchcards(unittest.TestCase):
    def test_totalvalue(self):
        self.assertEqual(13, main(os.path.abspath('data/test_d4.txt'))['score'])
    
    def test_totalquantity(self):
        self.assertEqual(30, main(os.path.abspath('data/test_d4.txt'))['quantity'])
    