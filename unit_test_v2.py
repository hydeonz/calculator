import unittest
from calc import calculate

class TestCalculate(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(calculate(1, 2, '+', 0), 3)

    def test_minus(self):
        self.assertEqual(calculate(5, 3, '-', 0), 2)

    def test_mul(self):
        self.assertEqual(calculate(2, 3, '*', 0), 6)

    def test_div(self):
        self.assertEqual(calculate(6, 2, '/', 0), 3)

    def test_sin(self):
        self.assertAlmostEqual(calculate(0.5, 0, 'sin', 0), 0.479425538604203)

    def test_cos(self):
        self.assertAlmostEqual(calculate(0.5, 0, 'cos', 0), 0.8775825618903728)

    def test_floor(self):
        self.assertEqual(calculate(3.7, 0, 'floor', 0), 3)

    def test_ceil(self):
        self.assertEqual(calculate(3.3, 0, 'ceil', 0), 4)

    def test_mod(self):
        self.assertEqual(calculate(5, 2, 'mod', 0), 1)

if __name__ == '__main__':
    unittest.main()
