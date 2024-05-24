import unittest
import tkinter as tk
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import DISABLED, NORMAL
from unittest.mock import patch

from calc import plus, minus, mul, div, sin, cos, floor, ceil, mod, calculate, on_dropdown_change


class TestCalculator(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(3, 5), 8)

    def test_minus(self):
        self.assertEqual(minus(8, 3), 5)

    def test_mul(self):
        self.assertEqual(mul(2, 4), 8)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)

    def test_floor(self):
        self.assertEqual(floor(5.6), 5)

    def test_ceil(self):
        self.assertEqual(ceil(5.6), 6)

    def test_mod(self):
        self.assertEqual(mod(10, 3), 1)


if __name__ == '__main__':
    unittest.main()