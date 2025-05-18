import unittest
from homework_14 import SiteUser


class TestSiteUser(unittest.TestCase):

    def setUp(self):
        self.user1 = SiteUser("John Doe", "john.doe@example.com", "user", 5)
        self.user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin", 1)
        self.user3 = SiteUser("Kyryl Kurliandskyi", "kyryl.kurliandskyi@example.com", "admin", 1)

    def test_01_user_creation(self):
        self.assertEqual(self.user1.name, "John Doe")
        self.assertEqual(self.user1.email, "john.doe@example.com")
        self.assertEqual(self.user1.access_level, "user")
        self.assertEqual(self.user1.logcount, 5)

    def test_02_str(self):
        self.assertEqual(str(self.user1), "SiteUser: John Doe, mailbox: john.doe@example.com, access level: user")

    def test_03_logcount_getter(self):
        self.assertEqual(self.user2.logcount, 1)

    def test_04_logcount_setter_valid(self):
        self.user1.logcount = 5
        self.assertEqual(self.user1.logcount, 10)

    def test_05_logcount_setter_negativ(self):
        with self.assertRaises(ValueError):
            self.user1.logcount = -5

    def test_06_logcount_setter_not_int(self):
        with self.assertRaises(ValueError):
            self.user1.logcount = "5"

    def test_07_logcount_setter_lower_value(self):
        with self.assertRaises(ValueError):
            self.user1.logcount = 2

    def test_08_eq_same_access_level(self):
        self.assertEqual(self.user2, self.user3)

    def test_09_eq_different_access_level(self):
        self.assertNotEqual(self.user1, self.user2)

    def test_10_eq_different_objects(self):
        with self.assertRaises(ValueError):
            self.user1 == "not a user"


if __name__ == "__main__":
    unittest.main(verbosity=2)