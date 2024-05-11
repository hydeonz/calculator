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


if __name__ == '__main__':
    unittest.main()