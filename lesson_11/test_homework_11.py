import unittest

from homework_11 import log_event


class TestLogEvent(unittest.TestCase):
    def test_pos_log_event_success(self):
        """Test positive log event with success status and level INFO"""
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("test_user", "success")
        self.assertEqual(['INFO:log_event:Login event - Username: test_user, Status: success'], log.output)

    def test_pos_log_event_expired(self):
        """Test positive log event with expired status and level WARNING"""
        with self.assertLogs('log_event', level='WARNING') as log:
            log_event("test_user", "expired")
        self.assertEqual(['WARNING:log_event:Login event - Username: test_user, Status: expired'], log.output)

    def test_pos_log_event_failed(self):
        """Test positive log event with ERROR level and failed status"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("test_user", "failed")
        self.assertEqual(["ERROR:log_event:Login event - Username: test_user, Status: failed"], log.output)

    def test_neg_log_event_invalid_status(self):
        """Test negative log event with unknown status and level ERROR"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("test_user", "unknown_status")
        self.assertEqual(
            ["ERROR:log_event:Login event - Username: test_user, Status: unknown_status"],
            log.output
        )

    def test_neg_log_event_success_status_level(self):
        """Test negative log event success status is not higher than INFO level"""
        with self.assertRaises(AssertionError):
            with self.assertLogs('log_event', level='WARNING'):
                log_event("test_user", "success")

    def test_neg_log_event_expired_status_level(self):
        """Test negative log event expired status is not higher than WARNING level"""
        with self.assertRaises(AssertionError):
            with self.assertLogs('log_event', level='ERROR'):
                log_event("test_user", "expired")

    def test_neg_log_event_error_level(self):
        """Test negative log event any statuses except success and expire are not higher than ERROR level"""
        with self.assertRaises(AssertionError):
            with self.assertLogs('log_event', level='CRITICAL'):
                log_event("test_user", "failed")


if __name__ == "__main__":
    unittest.main()
