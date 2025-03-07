import unittest

try:
    from lesson_14.homework_14 import SiteUser
except ImportError:
    from homework_14 import SiteUser

class TestSiteUser(unittest.TestCase):

    def setUp(self):
        """Create users for tests"""
        self.user1 = SiteUser("Mary Swan", "marysw@gmail.com", "admin")
        self.user2 = SiteUser("Ann Klint", "annklint@gmail.com", "user")
        self.user3 = SiteUser("Ivan Shpak", "shpaky@gmail.com", "moderator")
        self.user4 = SiteUser("John Smith", "jsmth@gmail.com", "blocked")
        self.user5 = SiteUser("Max Stake", "jstake@gmail.com", "admin")

    def test_01_check_user_data(self):
        """Check whether objects are instances of a class"""
        self.assertIsInstance(self.user1, SiteUser)
        self.assertIsInstance(self.user2, SiteUser)
        self.assertIsInstance(self.user3, SiteUser)
        self.assertIsInstance(self.user4, SiteUser)
        self.assertIsInstance(self.user5, SiteUser)

    def test_02_user1_info(self):
        """Check the attributes of user1"""
        self.assertEqual(self.user1.name, "Mary Swan")
        self.assertEqual(self.user1.email, "marysw@gmail.com")
        self.assertEqual(self.user1.access_lvl, "admin")
        self.assertEqual(self.user1.logcount, 0)

    def test_03_user2_setter_getter(self):
        """Get data of user 2"""
        self.user2.name = "Ann Klint"
        self.assertEqual(self.user2.name, "Ann Klint")
        self.user1.email = "annklint@gmail.com"
        self.assertEqual(self.user2.email, "annklint@gmail.com")
        self.user1.access_lvl = "user"
        self.assertEqual(self.user2.access_lvl, "user")

    def test_04_logcount_user3(self):
        """Check number of logins of user3"""
        self.user3.logcount_plus()
        self.user3.logcount_plus()
        self.assertEqual(self.user3.logcount, 2)

    def test_05_str_method_user4(self):
        """Check __str__ method of user4"""
        expected_str = "Name: John Smith, email: jsmth@gmail.com, access level: blocked, number of logins: 0"
        self.assertEqual(str(self.user4), expected_str)

    def test_06_eq_users(self):
        """"Check equivalence of users"""
        self.assertEqual(self.user1 == self.user2, f'{False}, Користувачі різні')
        self.assertEqual(self.user1 == self.user5, f'{True}, Користувачі однакові')

    def test_07_logcount_setter_for_user2(self):
        """"Positive and negative checks for logcount of user2"""
        self.user2.logcount = 3
        self.assertEqual(self.user2.logcount, 3)

        with self.assertRaises(ValueError):
            self.user2.logcount = "this is str"

if __name__ == "__main__":
    unittest.main(verbosity=2)
