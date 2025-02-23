import unittest
import logging
import os

from homework_11 import log_event

class TestLogEvent(unittest.TestCase):

    def setUp(self):
        """Set up before each test"""
        self.log_filename = "test_login_system.log"
        logging.basicConfig(filename=self.log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger("log_event")
        self.logger.handlers = []

    def tearDown(self):
        """Cleaning after each test"""
        logging.shutdown()
        if os.path.exists(self.log_filename):
            os.remove(self.log_filename)

    def test_log_success(self):
        """Verifying successful login logging"""
        username = "John Snow"
        status = "success"
        log_event(username, status)

        with open(self.log_filename, "r") as f:
            log_content = f.read()

        expected_log = f"Login event - Username: {username}, Status: {status}"
        self.assertTrue(expected_log in log_content)

    def test_log_expired(self):
        """Verify logging an outdated password"""
        username = "Clara Osvin Osvald"
        status = "expired"
        log_event(username, status)

        with open(self.log_filename, "r") as f:
            log_content = f.read()

        expected_log = f"Login event - Username: {username}, Status: {status}"
        self.assertTrue(expected_log in log_content)

    def test_log_failed(self):
        """Verify failed login logging"""
        username = "Doctor Who"
        status = "failed"
        log_event(username, status)

        with open(self.log_filename, "r") as f:
            log_content = f.read()

        expected_log = f"Login event - Username: {username}, Status: {status}"
        self.assertTrue(expected_log in log_content)

    def test_log_invalid_status(self):
        """Verify a login with an invalid status (should be handled as an error)"""
        username = "Luke Skywalker"
        status = "invalid"
        log_event(username, status)

        with open(self.log_filename, "r") as f:
            log_content = f.read()

        expected_log = f"Login event - Username: {username}, Status: {status}"
        self.assertTrue(expected_log in log_content)

if __name__ == '__main__':
    unittest.main(verbosity=2)