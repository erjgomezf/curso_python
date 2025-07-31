import unittest
from src.calculator import sum, subtract, multiply, divide

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(3, 4), 7, "Expected sum of 3 and 4 to be 7")


    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5, "Expected difference of 10 and 5 to be 5")

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12, "Expected product of 3 and 4 to be 12")

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4, "Expected division of 8 by 2 to be 4")
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0),  "Expected division by zero to raise ZeroDivisionError"
