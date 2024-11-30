import unittest
from io import StringIO
import sys
from Data.Lab2.Classes.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        # Redirect stdout to suppress print statements during tests
        self._original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore original stdout after each test
        sys.stdout = self._original_stdout

    # Test for addition with positive numbers
    def test_addition_positive(self):
        result = self.calc.calculate(5, '+', 3)
        self.assertEqual(result, 8, "5 + 3 should be 8")

    # Test for addition with negative numbers
    def test_addition_negative(self):
        result = self.calc.calculate(-5, '+', -3)
        self.assertEqual(result, -8, "-5 + -3 should be -8")

    # Test for addition with mixed positive and negative numbers
    def test_addition_mixed(self):
        result = self.calc.calculate(-5, '+', 3)
        self.assertEqual(result, -2, "-5 + 3 should be -2")

    # Test for subtraction with positive result
    def test_subtraction_positive(self):
        result = self.calc.calculate(5, '-', 3)
        self.assertEqual(result, 2, "5 - 3 should be 2")

    # Test for subtraction with negative result
    def test_subtraction_negative(self):
        result = self.calc.calculate(3, '-', 5)
        self.assertEqual(result, -2, "3 - 5 should be -2")

    # Test for subtraction with mixed positive and negative numbers
    def test_subtraction_mixed(self):
        result = self.calc.calculate(-5, '-', 3)
        self.assertEqual(result, -8, "-5 - 3 should be -8")

    # Test for multiplication with positive numbers
    def test_multiplication_positive(self):
        result = self.calc.calculate(5, '*', 3)
        self.assertEqual(result, 15, "5 * 3 should be 15")

    # Test for multiplication with a negative number
    def test_multiplication_negative(self):
        result = self.calc.calculate(-5, '*', 3)
        self.assertEqual(result, -15, "-5 * 3 should be -15")

    # Test for multiplication with zero
    def test_multiplication_zero(self):
        result = self.calc.calculate(5, '*', 0)
        self.assertEqual(result, 0, "5 * 0 should be 0")

    # Test for division with positive numbers
    def test_division_positive(self):
        result = self.calc.calculate(6, '/', 3)
        self.assertEqual(result, 2, "6 / 3 should be 2")

    # Test for division resulting in a negative number
    def test_division_negative(self):
        result = self.calc.calculate(6, '/', -3)
        self.assertEqual(result, -2, "6 / -3 should be -2")

    # Test for division by zero
    def test_division_by_zero(self):
        result = self.calc.calculate(5, '/', 0)
        self.assertIsNone(result, "Division by zero should return None")

    # Test for division with zero as dividend
    def test_division_zero_dividend(self):
        result = self.calc.calculate(0, '/', 3)
        self.assertEqual(result, 0, "0 / 3 should be 0")

    # Test for invalid input (non-numeric)
    def test_invalid_input(self):
        result = self.calc.calculate("a", '+', "b")
        self.assertIsNone(result, "Non-numeric input should return None")

    # Test for invalid operator
    def test_invalid_operator(self):
        result = self.calc.calculate(5, '#', 3)
        self.assertIsNone(result, "Invalid operator should return None")

if __name__ == "__main__":
    unittest.main()
