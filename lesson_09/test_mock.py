import unittest
from unittest.mock import patch, Mock
import urllib.request
import json


def get_webpage(url = 'https://example.com'):
    response = urllib.request.urlopen(url).read()
    try:
        response = response.decode('utf-8')
        json_response = json.loads(response)
    except json.decoder.JSONDecodeError:
        json_response = {}
    return json_response


class TestAPIClient(unittest.TestCase):
    
    @patch('urllib.request.urlopen')
    def test_get_webpage(self, mock_urlopen):
        mock_urlopen.return_value = Mock()
        mock_urlopen.return_value.read.return_value = b'{"key": "value"}'
        actual_result = get_webpage()
        expected_result = {"key": "value"}
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    print(get_webpage())
    #unittest.main(verbosity=2)