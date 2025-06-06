import unittest
from assignment5 import fahrenheitToCelsius, fibonacci

class TestCalculators(unittest.TestCase):
    def test_fahrenheitToCelsius(self):
        self.assertAlmostEqual(fahrenheitToCelsius(0), -17.78)
        self.assertAlmostEqual(fahrenheitToCelsius(32), 0)
        self.assertAlmostEqual(fahrenheitToCelsius(50), 10)
        self.assertAlmostEqual(fahrenheitToCelsius(90), 32.22)
        self.assertAlmostEqual(fahrenheitToCelsius(-15), -26.11)

    def test_fibonaci(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == "__main__":
    unittest.main()