import unittest
from unittest.mock import MagicMock

from profile import ProfileController


class ProfileTest(unittest.TestCase):

    def setUp(self):
        database_manager = MagicMock()
        crypto = MagicMock()
        self.controller = ProfileController(database_manager=database_manager, crypto=crypto)

    def test_test(self):
        y = self.x + 2
        self.assertEqual(y, 4)
