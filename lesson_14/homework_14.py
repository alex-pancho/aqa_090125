"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user, blocked).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкти за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = SiteUser("John Doe", "john.doe@example.com", "user")
user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: SiteUser: John Doe, mailbox: john.doe@example.com, access level: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""
class SiteUser():
    def __init__(self, name, email, excess_level:str, log_count:int = 0):
        self.name = name
        self.email = email
        self.excess_level = excess_level
        self.log_count = log_count

    def __str__(self):
        return f"SiteUser: {self.name}, mailbox: {self.email}, access level: {self.excess_level}, logcount: {self.log_count}"

    def __eq__(self, other: object):
        if self.name == other.name and self.email == other.email and self.excess_level == other.excess_level:
            return "Користувачі однакові"
        else:
            return "Користувачі різні"

    def login_user(self):
        self.log_count += 1


if __name__ == "__main__":
    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
    user3 = SiteUser("John Doe", "john.doe@example.com", "user")
    print(user1)
    print(user2)
    print(user1 == user2)
    print(user1 == user3)
    print(user1.login_user())
    print(user1)

import unittest
class TestSiteUser(unittest.TestCase):
    def test_01_setUp(self):
        test_user = SiteUser("John Doe", "john.doe@example.com", "user", )
        self.assertEqual(test_user.name, "John Doe")
        self.assertEqual(test_user.email, "john.doe@example.com")
        self.assertEqual(test_user.excess_level, "user")

    def test_02_user_equality(self):
        test_user_1 = SiteUser("John Doe", "john.doe@example.com", "admin")
        test_user_2 = SiteUser("John Doe", "john.doe@example.com", "admin")
        test_user_3 = SiteUser("Jane Smith", "jane.smith@example.com", "moderator")
        self.assertEqual(test_user_1 == test_user_2, "Користувачі однакові")
        self.assertEqual(test_user_1 == test_user_3, "Користувачі різні")

    def test_03_login_user(self):
        test_user = SiteUser("John Doe", "john.doe@example.com", "user", )
        test_user.login_user()
        self.assertEqual(test_user.log_count, 1)
        test_user.login_user()
        self.assertEqual(test_user.log_count, 2)

if __name__ == "__main__":
    unittest.main()