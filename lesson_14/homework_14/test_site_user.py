import unittest
from homework_14 import SiteUser


class TestSiteUser(unittest.TestCase):
    def setUp(self):
        self.user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        self.user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

    def test_user_creation(self):
        self.assertEqual(self.user1.name, "John Doe")
        self.assertEqual(self.user1.email, "john.doe@example.com")
        self.assertEqual(self.user1.access_level, "user")
        self.assertEqual(self.user1.logcount, 0)

    def test_string_representation(self):
        self.assertEqual(
            str(self.user1),
            "SiteUser: John Doe, mailbox: john.doe@example.com, access level: user",
        )

    def test_access_level_comparison(self):
        user3 = SiteUser("Alice Brown", "alice.brown@example.com", "user")
        self.assertTrue(self.user1 == user3)
        self.assertFalse(self.user1 == self.user2)

    def test_increment_logcount(self):
        self.user1.increment_logcount()
        self.assertEqual(self.user1.logcount, 1)
        self.user1.increment_logcount()
        self.assertEqual(self.user1.logcount, 2)

    def test_setters(self):
        self.user1.name = "Johnny Doe"
        self.assertEqual(self.user1.name, "Johnny Doe")
        
        self.user1.email = "new.email@example.com"
        self.assertEqual(self.user1.email, "new.email@example.com")
        
        self.user1.access_level = "moderator"
        self.assertEqual(self.user1.access_level, "moderator")


if __name__ == "__main__":
    unittest.main( verbosity=2)

