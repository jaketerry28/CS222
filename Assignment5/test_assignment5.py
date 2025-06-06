import unittest
from assignment5 import fahrenheitToCelsius, fibonacci

class TestCalculators(unittest.TestCase):
    def test_fahrenheitToCelsius(self):
        self.assertEqual(fahrenheitToCelsius(0), -17.78)
        self.assertEqual(fahrenheitToCelsius(32), 0)
        self.assertEqual(fahrenheitToCelsius(50), 10)
        self.assertEqual(fahrenheitToCelsius(90), 32.22)
        self.assertEqual(fahrenheitToCelsius(-15), -26.11)

    def test_fibonaci(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == "__main__":
    unittest.main()