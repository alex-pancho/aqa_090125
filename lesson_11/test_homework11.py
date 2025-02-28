import unittest
import logging
import os
from homework_11 import log_event

class TestLogEvent(unittest.TestCase):
    def setUp(self):
        self.log_file = "login_system.log"
        logging.shutdown()
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def read_last_log_line(self):
        """Функція, яка отримує останній запис
        у файлі логів після виклику функції log_event()"""
        with open(self.log_file, "r", encoding="utf8") as f:
            lines = f.readlines()
        return lines[-1] if lines else ""

    def test_01_success(self):
        log_event("user1", "success") #запускаємо функцію
        last_log = self.read_last_log_line() #перевіряємо останній запис
        self.assertIn("Username: user1, Status: success", last_log)
        self.assertIn("INFO", last_log)

    def test_02_expired(self):
        log_event("user2", "expired")
        last_log = self.read_last_log_line()
        self.assertIn("Username: user2, Status: expired", last_log)
        self.assertIn("WARNING", last_log)

    def test_03_failed(self):
        log_event("user3", "failed")
        last_log = self.read_last_log_line()
        self.assertIn("Username: user3, Status: failed", last_log)
        self.assertIn("ERROR", last_log)

    def test_04_unknown_status(self):
        log_event("user4", "unknown")
        last_log = self.read_last_log_line()
        self.assertIn("Username: user4, Status: unknown", last_log)
        self.assertIn("ERROR", last_log)

    def test_05_empty_username(self):
        log_event("", "success")
        last_log = self.read_last_log_line()
        self.assertIn("Username: , Status: success", last_log)
        self.assertIn("INFO", last_log)

    def test_06_empty_username_unknown_status(self):
        log_event("", "unknown")
        last_log = self.read_last_log_line()
        self.assertIn("Username: , Status: unknown", last_log)
        self.assertIn("ERROR", last_log)

    def test_07_empty_status(self):
        log_event("user7", "")
        last_log = self.read_last_log_line()
        self.assertIn("Username: user7, Status: ", last_log)
        self.assertIn("ERROR", last_log)

    def test_08_negative(self):
        with self.assertRaises(TypeError):
            log_event(None)

if __name__ == "__main__":
    unittest.main(verbosity = 2)

