"""
Parses a JSON array to a string and vice versa
"""
from flask import json


class ArrayParser:

    def __init__(self):
        pass

    def parse(self, data, **kwargs):
        to_json = kwargs.pop('json', False)
        if not to_json:
            result = ''
            for session_round in data:
                for key, value in session_round.items():
                    result += '{round}:{seconds} '.format(round=key, seconds=value)
            # remove last trim
            result = result[:-1]
        else:
            round_raw = data.split()
            result = []
            for item in round_raw:
                val = item.split(':')
                result.append({val[0]: int(val[1])})
            result = json.dumps(result)
        return result
