import unittest
from unittest.mock import patch
from homework_11 import log_event 

class TestLogEvent(unittest.TestCase):
    @patch("homework_11.logging.getLogger") 
    def test_log_success(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value 
        log_event("Anna", "success")
        mock_logger.info.assert_called_once_with("Login event - Username: Anna, Status: success")

    @patch("homework_11.logging.getLogger")
    def test_log_expired(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("Sveta", "expired")
        mock_logger.warning.assert_called_once_with("Login event - Username: Sveta, Status: expired")

    @patch("homework_11.logging.getLogger")
    def test_log_failed(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("Kirill", "failed")
        mock_logger.error.assert_called_once_with("Login event - Username: Kirill, Status: failed")

    @patch("homework_11.logging.getLogger")
    def test_log_unknown_status(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("Dima", "unknown")
        mock_logger.error.assert_called_once_with("Login event - Username: Dima, Status: unknown")

if __name__ == "__main__":
    unittest.main()