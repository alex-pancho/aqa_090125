import unittest
from unittest.mock import patch

try:
    from lesson_11.homework_11 import log_event
except ImportError:
    from homework_11 import log_event

class TestLogger(unittest.TestCase):

    @patch('logging.getLogger')
    def test_01_success_login(self, mock_getLogger):
        """Check for success login"""
        mock_logger = mock_getLogger.return_value
        log_event("Andy Tue", "success")
        mock_logger.info.assert_called_once_with("Login event - Username: Andy Tue, Status: success")

    @patch('logging.getLogger')
    def test_02_expired_password(self, mock_getLogger):
        """Check for expired password"""
        mock_logger = mock_getLogger.return_value
        log_event("John Doe", "expired")
        mock_logger.warning.assert_called_once_with("Login event - Username: John Doe, Status: expired")

    @patch('logging.getLogger')
    def test_03_wrong_password(self, mock_getLogger):
        """Check for wrong pass"""
        mock_logger = mock_getLogger.return_value
        log_event("Martha Smith", "failed")
        mock_logger.error.assert_called_once_with("Login event - Username: Martha Smith, Status: failed")

if __name__ == "__main__":
    unittest.main(verbosity=2)

        