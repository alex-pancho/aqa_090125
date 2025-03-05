import unittest
from homework_14 import SiteUser

class TestSiteUser(unittest.TestCase):
    def setUp(self):
        self.user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        self.user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

    def test_user_date(self):
        self.assertEqual(str(self.user1), "SiteUser: John Doe, mailbox: john.doe@example.com, access level: user")
        self.assertEqual(str(self.user2), "SiteUser: Jane Smith, mailbox: jane.smith@example.com, access level: admin")
    
    def test_user_name(self):
        self.assertEqual(self.user1.name, "John Doe")
        self.assertEqual(self.user2.name, "Jane Smith")

    def test_user_email(self):
        self.assertEqual(self.user1.email, "john.doe@example.com")
        self.assertEqual(self.user2.email, "jane.smith@example.com")

    def test_user_access_level(self):
        self.assertEqual(self.user1.access_level, "user")
        self.assertEqual(self.user2.access_level, "admin")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            self.user1.name = 123

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user1.email = 456

    def test_invalid_access_level(self):
        with self.assertRaises(ValueError):
            self.user1.access_level = "god"
    
    def test_increment_logcount_user1(self):
        self.user1.increment_logcount()
        self.user1.increment_logcount()
        self.assertEqual(self.user1.logcount, 2)

    def test_increment_logcount_user2(self):
        self.user2.increment_logcount()
        self.user2.increment_logcount()
        self.user2.increment_logcount()
        self.assertEqual(self.user2.logcount, 3)

        
    def test_zero_increment_logcount(self):
        self.assertEqual(self.user1.logcount, 0)

    def test_eq_method(self):
        self.assertNotEqual(self.user1, self.user2)
        user3 = SiteUser("Bill Gray", "bbgg@ex.com", "admin")
        self.assertEqual(self.user2, user3)

    
    



if __name__ == "__main__":
    unittest.main()