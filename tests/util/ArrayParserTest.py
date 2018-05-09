import unittest

from util.parsing.ArrayParser import ArrayParser


class ArrayParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = ArrayParser()

    def test_parse_one_result_to_string(self):
        data = [{1: 30}]

        result = self.parser.parse(data)

        self.assertEqual('1:30', result)

    def test_parse_multiple_results_to_string(self):
        data = [{1: 30}, {2: 30}, {3: 50}]

        result = self.parser.parse(data)

        self.assertEqual('1:30 2:30 3:50', result)

    def test_parse_no_result_to_string(self):
        data = []

        result = self.parser.parse(data)

        self.assertEqual('', result)

    def test_parse_a_result_to_json_string(self):
        data = '1:30'

        result = self.parser.parse(data, json=True)

        self.assertEqual('[{"1": 30}]', result)

    def test_parse_a_result_to_json_string(self):
        data = '1:30 4:23'

        result = self.parser.parse(data, json=True)

        self.assertEqual('[{"1": 30}, {"4": 23}]', result)
