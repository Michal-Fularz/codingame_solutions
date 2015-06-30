#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_codingame_solutions
----------------------------------

Tests for `codingame_solutions` module.
"""

import unittest

from codingame_solutions import codingame_solutions


class TestCodingame_solutions(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(codingame_solutions.add(2, 3), 5)
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
