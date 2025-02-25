import unittest
import logging
import os

from homework_11 import log_event


class TestLogEvent(unittest.TestCase):

    def setUp(self):
        """Set up before each test"""
        self.log_filename = "test_login_system.log"
        self.logger = logging.getLogger("log_event")
        self.logger.setLevel(logging.DEBUG)

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        handler = logging.FileHandler(self.log_filename)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def tearDown(self):
        """Cleaning after each test"""
        logging.shutdown()
        if os.path.exists(self.log_filename):
            os.remove(self.log_filename)

    def read_log_file(self):
        with open(self.log_filename, "r") as f:
            return f.read()

    def test_log_success(self):
        """Verifying successful login logging"""
        log_event("Nadiia Protsenko", "success")
        log_content = self.read_log_file()
        self.assertIn("INFO", log_content)
        self.assertIn("Username: Nadiia Protsenko, Status: success", log_content)

    def test_log_expired(self):
        """Verify logging an outdated password"""
        log_event("Van Hallen", "expired")
        log_content = self.read_log_file()
        self.assertIn("WARNING", log_content)
        self.assertIn("Username: Van Hallen, Status: expired", log_content)

    def test_log_failed(self):
        """Verify failed login logging"""
        log_event("Doctor Dre", "failed")
        log_content = self.read_log_file()
        self.assertIn("ERROR", log_content)
        self.assertIn("Username: Doctor Dre, Status: failed", log_content)

    def test_log_invalid_status(self):
        """Verify a login with an invalid status (should be handled as an error)"""
        log_event("Zdislav Beskinski Zde", "invalid")
        log_content = self.read_log_file()
        self.assertIn("ERROR", log_content)
        self.assertIn("Username: Zdislav Beskinski Zde, Status: invalid", log_content)

    def test_empty_username(self):
        """Verify logging with an empty username"""
        log_event("", "success")
        log_content = self.read_log_file()
        self.assertIn("INFO", log_content)
        self.assertIn("Username: , Status: success", log_content)

    def test_empty_status(self):
        """Verify logging with an empty status (should be treated as an error)"""
        log_event("Anonymous", "")
        log_content = self.read_log_file()
        self.assertIn("ERROR", log_content)
        self.assertIn("Username: Anonymous, Status: ", log_content)


if __name__ == '__main__':
    unittest.main(verbosity=2)