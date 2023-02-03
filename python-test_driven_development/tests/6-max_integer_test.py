#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests for the function max_integer """

    def test_empty_args(self):
        self.assertEqual(max_integer([]), None)

    def test_max_first(self):
        self.assertEqual(max_integer([62, 9, 7, 1, 48]), 62)

    def test_max_middle(self):
        self.assertEqual(max_integer([9, 7, 62, 48, 1]), 62)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 9, 7, 48, 62]), 62)

    def test_negativ_number(self):
        self.assertEqual(max_integer([-1, 7, -48, 62, 9]), 62)

    def test_full_negativ_number(self):
        self.assertEqual(max_integer([-9, -1, -7, -48, -62]), -1)

    def test_one_single_element(self):
        self.assertEqual(max_integer([62]), 62)
