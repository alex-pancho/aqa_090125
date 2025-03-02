import unittest
from homework_11 import log_event



class TestLogEvent(unittest.TestCase):

    def test_01_log_event_success(self):
        """Test for successful login"""
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("test_user", "success")
        self.assertEqual(['INFO:log_event:Login event - Username: test_user, Status: success'], log.output)

    def test_02_log_event_expired(self):
        """Test for an outdated password"""
        with self.assertLogs('log_event', level='WARNING') as log:
            log_event("test_user", "expired")
        self.assertEqual(['WARNING:log_event:Login event - Username: test_user, Status: expired'], log.output)

    def test_03_log_event_failed(self):
        """Test for an incorrect password"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("test_user", "failed")
        self.assertEqual(["ERROR:log_event:Login event - Username: test_user, Status: failed"], log.output)

    def test_04_log_event_invalid_status(self):
        """Test for unknown status"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("test_user", "some_status")
        self.assertEqual(
            ["ERROR:log_event:Login event - Username: test_user, Status: some_status"],log.output)

    def test_05_log_event_empty_username(self):
        """Test for an empty username"""
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("", "success")
        self.assertEqual(["INFO:log_event:Login event - Username: , Status: success"], log.output)

    def test_06_log_event_empty_status(self):
        """Test for an empty status"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("test_user", "")
        self.assertEqual(["ERROR:log_event:Login event - Username: test_user, Status: "], log.output)

   


if __name__ == "__main__":
    unittest.main(verbosity=2)
        
