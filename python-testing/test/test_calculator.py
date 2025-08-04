import unittest
from src.calculator import sum, subtract, multiply, divide

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(3, 4), 7, "la suma de 3 y 4 debe ser 7")

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5, "la resta de 10 y 5 debe ser 5")

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12, "la multiplicación de 3 y 4 debe ser 12")

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4, "la división de 8 entre 2 debe ser 4")
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
    