import unittest

from homework_14 import SiteUser

class TestSiteUser(unittest.TestCase):
    #тестуємо створення об'єктів
    def test_user_creation(self):
        user = SiteUser("John Doe","john.doe@example.com", "user")
        self.assertEqual(user.name, "John Doe"),
        self.assertEqual(user.email, "john.doe@example.com"),
        self.assertEqual(user.access_level, "user")
        self.assertEqual(user.logcount, 0)

    def test_default_access_level(self):
        user = SiteUser("Jane Smith", "jane.smith@example.com")
        self.assertEqual(user.access_level, "user")

    #тестуємо гетери
    def test_get_name(self):
        user = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertEqual(user.name, "Jane Smith")

    def test_get_email(self):
        user = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertEqual(user.email, "jane.smith@example.com")

    def test_get_access_level(self):
        user = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertEqual(user.access_level, "admin")

    def test_get_logcount(self):
        user = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertEqual(user.logcount, 0)

    def test_getters_after_setters(self):
        user = SiteUser("John Doe","john.doe@example.com", "user")

        user.name = "Jane Smith"
        user.email = "jane.smith@example.com"
        user.access_level = "admin"
        user.logcount = 5

        self.assertEqual(user.name, "Jane Smith")
        self.assertEqual(user.email, "jane.smith@example.com")
        self.assertEqual(user.access_level, "admin")
        self.assertEqual(user.logcount, 5)

    def test_logcount_increase(self):
        user = SiteUser("John Doe","john.doe@example.com", "user")

        user.login()
        user.login()
        user.login()

        self.assertEqual(user.logcount, 3)

    #тестуємо сетери
    def test_set_name(self):
        user = SiteUser("John Doe", "john.doe@example.com")
        user.name = "Jane Smith"
        self.assertEqual(user.name, "Jane Smith")

    def test_set_email(self):
        user = SiteUser("John Doe", "john.doe@example.com")
        user.email = "jane.smith@example.com"
        self.assertEqual(user.email, "jane.smith@example.com")

    def test_set_access_level(self):
        user = SiteUser("John Doe", "john.doe@example.com")
        user.access_level = "admin"
        self.assertEqual(user.access_level, "admin")

    def test_set_invalid_access_level(self):
        user = SiteUser("John Doe", "john.doe@example.com")
        with self.assertRaises(ValueError) as e:
            user.access_level = "superadmin"
        self.assertEqual(str(e.exception), "Невірний рівень доступу")

    def test_set_invalid_logcount(self):
        user = SiteUser("John Doe", "john.doe@example.com")
        with self.assertRaises(ValueError) as e:
            user.logcount = -1
        self.assertEqual(str(e.exception), "Лічильник логінів має бути невід'ємним цілим числом")

        with self.assertRaises(ValueError):
            user.logcount = 5.5

        with self.assertRaises(ValueError):
            user.logcount = "ten"

    #Перевірка __eq__ (порівняння рівнів доступу)
    def test_eq_same_access_level(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "admin")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.assertTrue(user1 == user2)

    def test_eq_diff_access_level(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "admin")
        user2 = SiteUser("Jane Smith", "jane.smith@example.com", "user")
        self.assertFalse(user1 == user2)

    def test_eq_non_user_object(self):
        user1 = SiteUser("John Doe", "john.doe@example.com", "admin")
        user2 = "not a user"
        self.assertFalse(user1 == user2)

    #Перевірка __str__
    def test_str_represent(self):
        user = SiteUser("John Doe", "john.doe@example.com", "admin")
        expected_str = "SiteUser: John Doe, mailbox: john.doe@example.com, access level: admin"
        self.assertEqual(str(user), expected_str)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
