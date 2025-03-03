import unittest
from homework_11 import log_event
class TestLogEvent(unittest.TestCase):
    def test_01_log_event(self):
        """тест status = success"""
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("Anna_username", "success")
        self.assertEqual(['INFO:log_event:Login event - Username: Anna_username, Status: success'], log.output)
    def test_02_log_event(self):
        """тест status = expired"""
        with self.assertLogs('log_event', level='WARNING') as log:
            log_event("Anna_username", "expired")
        self.assertEqual(['WARNING:log_event:Login event - Username: Anna_username, Status: expired'], log.output)
    def test_03_log_event(self):
        """тест status = failed"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("Anna_username", "failed")
        self.assertEqual(['ERROR:log_event:Login event - Username: Anna_username, Status: failed'], log.output)
    def test_04_log_event(self):
        """тест status = else"""
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("Anna_username", "else")
        self.assertEqual(['ERROR:log_event:Login event - Username: Anna_username, Status: else'], log.output)
    def test_05_log_event(self):
        """тест status = empty status """
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("Anna_username", "")
        self.assertEqual(['ERROR:log_event:Login event - Username: Anna_username, Status: '], log.output)
    def test_06_log_event(self):
        """тест empty username on level INFO"""
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("", "success")
        self.assertEqual(['INFO:log_event:Login event - Username: , Status: success'], log.output)
    def test_07_log_event(self):
        """тест empty username on level ERROR"""
        with self.assertRaises(AssertionError):
            with self.assertLogs('log_event', level='ERROR'):
                log_event("", "success")