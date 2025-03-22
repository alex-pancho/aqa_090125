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
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
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

class SiteUser:
    def __init__(self, name, email, access):
        self.__name = name
        self.__email = email
        self.__access = access
        self.__logcount = 1

    def __str__(self):
        return f"User name: {self.__name}, Email: {self.__email}, Access level: {self.__access}"

    def logcount(self):
        return self.__logcount

    def _increment_log(self):
        self.__logcount += 1

    @property
    def name(self):
        self._increment_log()
        return self.__name

    @property
    def email(self):
        self._increment_log()
        return self.__email

    @email.setter
    def email(self, new_email):
        self._increment_log()
        if "@" in new_email and "." in new_email.split("@")[-1]:
            self.__email = new_email
        else:
            print("Некоректний імейл")

    @property
    def access(self):
        self._increment_log()
        return self.__access

    @access.setter
    def access(self, new_access):
        self._increment_log()
        if self.__access  in ["admin", "moderator"]:
            self.__access = new_access
        else:
            print("Немає прав змінювати рівень доступу")

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self.__access == other.__access
        return False

user1 = SiteUser("John Doe", "john.doe@example.com", "user")
user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
user3 = SiteUser("L S", "ls@example.com", "admin")

user1.access = "admin"
print(user2)
print(user1 == user2)
print(user2 == user3)

