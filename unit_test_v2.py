import unittest
from calc import perform_calculation

class TestCalculate(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(perform_calculation(1, 2, '+'), 3)

    def test_minus(self):
        self.assertEqual(perform_calculation(5, 3, '-'), 2)

    def test_mul(self):
        self.assertEqual(perform_calculation(2, 3, '*'), 6)

    def test_div(self):
        self.assertEqual(perform_calculation(6, 2, '/'), 3)

    def test_sin(self):
        self.assertAlmostEqual(perform_calculation(0.5, None, 'sin'), 0.479425538604203)

    def test_cos(self):
        self.assertAlmostEqual(perform_calculation(0.5, None, 'cos'), 0.8775825618903728)

    def test_floor(self):
        self.assertEqual(perform_calculation(3.7, None, 'floor'), 3)

    def test_ceil(self):
        self.assertEqual(perform_calculation(3.3, None, 'ceil'), 4)

    def test_mod(self):
        self.assertEqual(perform_calculation(5, 2, 'mod'), 1)

if __name__ == '__main__':
    unittest.main()