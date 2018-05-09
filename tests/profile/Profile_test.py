import unittest
from unittest.mock import MagicMock


class ProfileTest(unittest.TestCase):

    def setUp(self):
        self.x = 2

    def test_test(self):
        y = self.x +2
        self.assertEqual(y, 4)