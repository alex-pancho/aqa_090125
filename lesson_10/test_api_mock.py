import unittest
import json
from unittest.mock import patch, MagicMock
from api_real_and_mock import get_content, create_content, update_content, delete_content, BASE_URL
from api_real_and_mock import mock_get_content


def test_mock_get_content():
    result = json.loads(mock_get_content())
    assert result == {"content": []}


class TestAPI(unittest.TestCase):
    @patch("api_real_and_mock.return_content")
    @patch("urllib.request.urlopen")
    def test_get_content_1(self, mock_urlopen, return_content):
        return_content.return_value = {"content": []}
        mock_urlopen.return_value = get_content()
        result = get_content()
        self.assertEqual(result, {"content": []})
    
    @patch("api_real_and_mock.get_content")
    def test_get_content_2(self, get_content):
        result = get_content.return_value = {"content": []}
        self.assertEqual(result, {"content": []})
    

    # @patch("urllib.request.urlopen")
    # def test_create_content(self, mock_urlopen):
    #     mock_urlopen.return_value = mock_create_content()
    #     result = create_content()
    #     self.assertEqual(result, {"message": "Content created successfully!"})

    # @patch("urllib.request.urlopen")
    # def test_update_content(self, mock_urlopen):
    #     mock_urlopen.return_value = mock_update_content()
    #     result = update_content()
    #     self.assertEqual(result, {"message": "Content updated successfully!"})

    # @patch("urllib.request.urlopen")
    # def test_delete_content(self, mock_urlopen):
    #     mock_urlopen.return_value = mock_delete_content()
    #     result = delete_content()
    #     self.assertEqual(result, {"message": "Content deleted successfully!"})


if __name__ == "__main__":
    unittest.main()
