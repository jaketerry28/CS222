import unittest
from calculator import Calculator



class Test_Calculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1,1), 2)
        self.assertEqual(self.calc.add(0,0), 0)
        self.assertEqual(self.calc.add(0.5,-1), -0.5)
        self.assertEqual(self.calc.add(-2,-1), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1,1), 0)
        self.assertEqual(self.calc.subtract(0,0), 0)
        self.assertEqual(self.calc.subtract(0.5,-1), 1.5)
        self.assertEqual(self.calc.subtract(-2,-1), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1,1), 1)
        self.assertEqual(self.calc.multiply(0,0), 0)
        self.assertEqual(self.calc.multiply(0.5,-1), -0.5)
        self.assertEqual(self.calc.multiply(-2,-1), 2)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)
        self.assertEqual(self.calc.divide(1,1), 1)
        self.assertEqual(self.calc.divide(0.5,-1), -0.5)
        self.assertEqual(self.calc.divide(-2,-1), 2)
        self.assertEqual(self.calc.divide(0, 100), 0)

if __name__ == "__main__":
    unittest.main()