import unittest
from unittest.mock import patch
import logging


class TestLogEvent(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("log_event")
        self.logger.setLevel(logging.INFO)
        
        # Створення буфера для збору логів
        self.log_capture = []
        self.handler = logging.StreamHandler()
        self.handler.setStream(self.log_capture)
        self.logger.addHandler(self.handler)

    def tearDown(self):
        self.logger.removeHandler(self.handler)
        self.handler.close()

    @patch('logging.Logger.info')
    def test_success_status_logging(self, mock_info):
        """Тест логування успішного входу"""
        username = "test_user"
        status = "success"
        
        log_event(username, status)
        mock_info.assert_called_once_with(
            f"Login event - Username: {username}, Status: {status}"
        )

    @patch('logging.Logger.warning')
    def test_expired_status_logging(self, mock_warning):
        """Тест логування застарілого паролю"""
        username = "old_user"
        status = "expired"
        
        log_event(username, status)
        
        # Перевіряємо, що був виклик warning з правильним повідомленням
        mock_warning.assert_called_once_with(
            f"Login event - Username: {username}, Status: {status}"
        )

    @patch('logging.Logger.error')
    def test_failed_status_logging(self, mock_error):
        """Тест логування невдалого входу"""
        username = "wrong_pass_user"
        status = "failed"
        
        log_event(username, status)
        
        # Перевіряємо, що був виклик error з правильним повідомленням
        mock_error.assert_called_once_with(
            f"Login event - Username: {username}, Status: {status}"
        )

    @patch('logging.Logger.error')
    def test_unknown_status_logging(self, mock_error):
        """Тест логування невідомого статусу"""
        username = "strange_user"
        status = "unknown_status"
        
        log_event(username, status)     
        
        # Перевіряємо, що був виклик error (оскільки статус невідомий)
        mock_error.assert_called_once_with(
            f"Login event - Username: {username}, Status: {status}"
        )

    def test_log_message_format(self):
        """Тест формату повідомлення в лозі"""
        username = "format_test_user"
        status = "success"
        expected_message = f"Login event - Username: {username}, Status: {status}"
        
        with patch('logging.Logger.info') as mock_info:
            log_event(username, status)
            actual_message = mock_info.call_args[0][0]
            self.assertEqual(actual_message, expected_message)

if __name__ == '__main__':
    unittest.main()