import unittest

from homework_14 import SiteUser, AnotherSiteUsers


class TestHomework14(unittest.TestCase):

    def test_pos_site_uer_output(self):
        name = "John Doe"
        email = "john.doe@example.com"
        role = "user"

        self.assertEqual(
            f"SiteUser: {name}, mailbox: {email}, access level: {role}",
            str(SiteUser(name, email, role)),
        )

    def test_pos_site_user_attributes_presence(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")

        self.assertTrue(hasattr(user, "name"), "name attr is missing")
        self.assertTrue(hasattr(user, "email"), "email attr is missing")
        self.assertTrue(hasattr(user, "role"), "role attr is missing")
        self.assertTrue(hasattr(user, "logcount"), "logcount attr is missing")

    def test_pos_site_user_attributes_values(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")

        self.assertEqual("John Doe", getattr(user, "name"))
        self.assertEqual("john.doe@example.com", getattr(user, "email"))
        self.assertEqual("user", getattr(user, "role"))
        self.assertEqual(0, getattr(user, "logcount"))

    def test_pos_site_user_logcount_value_changing(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        def_value = user.logcount
        user.logcount = 1

        self.assertNotEqual(def_value, user.logcount)
        self.assertEqual(1, user.logcount)

    def test_pos_site_user_obj_equal(self):
        user_1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user_2 = SiteUser("John Doe", "john.doe@example.com", "moderator")
        user_3 = SiteUser("John Test", "test.doe@example.com", "user")

        self.assertTrue(user_1 == user_3, "users should be equal")
        self.assertFalse(user_1 == user_2, "users should not be equal")

    def test_pos_site_user_add_logcount_int(self):
        user_1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user_1 + 5

        self.assertEqual(5, user_1.logcount)

    def test_pos_site_user_add_logcount_class_obj(self):
        user_1 = SiteUser("John Doe", "john.doe@example.com", "user")
        user_2 = SiteUser("John Doe", "john.doe@example.com", "moderator")

        user_1.logcount = 5
        user_2.logcount = 2
        user_1 + user_2

        self.assertEqual(7, user_1.logcount)
        self.assertEqual(2, user_2.logcount)

    def test_neg_site_user_logncount(self):
        user = SiteUser("John Doe", "john.doe@example.com", "user")
        with self.assertRaises(TypeError):
            user.logcount = "1"
        with self.assertRaises(TypeError):
            user + '1'
        with self.assertRaises(TypeError):
            user_1 = AnotherSiteUsers("John Doe", "john.doe@example.com", "user")
            user_2 = SiteUser("John Doe", "john.doe@example.com", "user")
            user_1 + user_2
        with self.assertRaises(ValueError):
            user.logcount = -1

    def test_neg_site_user_obj_equal(self):
        user_1 = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertFalse(user_1 == "user", "It is not a SiteUser object")


if __name__ == '__main__':
    unittest.main()
