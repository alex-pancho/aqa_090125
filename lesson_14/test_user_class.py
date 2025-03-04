from homework_14 import SiteUser
import unittest

class UsersTest(unittest.TestCase):

    def setUp(self):
        """ Set up instances of class with different start values. """
        self.user1 = SiteUser(name="John Doe", email="john.doe@example.com", permission="user")
        self.user2 = SiteUser(name="Jane Smith", email="jane.smith@example.com", permission="admin")
        self.user3 = SiteUser(name="John Waine", email="john.waine@example.com", permission="blocked")
        self.user4 = SiteUser(name="Axel Murphy", email="axel@example.com", permission="moderator")
        self.user5 = SiteUser(name="Robert Tribe", email="robert@example.com", permission="user")

    def test_get_attributes_of_user_positive(self):
        """ Test of getting attributes using 'property' getter """
        expected_name = 'John Doe'
        expected_email = "john.doe@example.com"
        self.assertEqual(expected_name, self.user1.name)
        self.assertEqual(expected_email, self.user1.email)

    def test_users_log_count(self):
        """ Test of changing 'log_count' attribute while logging in. """
        start_log_count = 0
        end_log_count = 1
        self.assertEqual(start_log_count, self.user1.log_count)
        self.user1() # Log in, increasing log in count
        self.assertEqual(end_log_count, self.user1.log_count)

    def test_blocked_users_access_to_attributes(self):
        """ Blocked users can't access to attributes and log in. """
        self.user3()  # Try to log in...
        self.assertEqual(None, self.user3.log_count)
        self.assertEqual(None, self.user3.name)

    def test_admin_changes_permission_method(self):
        """ Test 'admin' instance ability to change permissions of other accounts. """
        expected_log_count = 1
        expected_name = 'John Waine'
        self.user3() # Try to log in...
        self.assertEqual(None, self.user3.log_count)
        self.assertEqual(None, self.user3.name)
        self.user2.change_permission(target_user=self.user3, new_permission='user')  # Changes permissions by 'Admin User'
        self.user3() # Log in...
        self.assertEqual(expected_log_count, self.user3.log_count)
        self.assertEqual(expected_name, self.user3.name)

    def test_restrict_user_changes_own_attributes(self):
        """ User can't change own attributes, read-only access only. """
        expected_name = 'John Doe'
        expected_email = 'john.doe@example.com'
        self.user1.name = 'James Bond'
        self.user1.email = '007@example.com'
        self.assertEqual(expected_name, self.user1.name)
        self.assertEqual(expected_email, self.user1.email)

    def test_comparing_users_instances_with_equal_permissions(self):
        """ Test of comparing user instances with equal permissions. """
        self.assertEqual(self.user1, self.user5)

    def test_undefined_method_calling(self):
        """ Test of calling undefined method from user instance. Raising error. """
        with self.assertRaises(AttributeError):
            self.user1.get_names()

    def test_creating_user_instance_without_any_parameter(self):
        """ Test of creating user instance without any parameters. Raising error. """
        with self.assertRaises(TypeError):
            new_user_instance = SiteUser(name='unknown', email='unknown')

    def test_changes_permission_method_without_args(self):
        """ Test of calling 'changes permission' method from user instance without arguments. """
        with self.assertRaises(TypeError):
            self.user2.change_permission()

if __name__ == '__main__':
    unittest.main()