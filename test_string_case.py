
from unittest import TestCase
from string_calculator import add

class TestStringCalculator(TestCase):

    def test_two_number_sum(self):
        self.assertEqual(add("1, 2, 4"), 7)
    
    def test_sum_with_newline(self):
        self.assertEqual(add("1 \n 2, 4"), 7)

        