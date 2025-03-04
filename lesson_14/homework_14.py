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
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        self.__logcount = 0

    @property
    def logcount(self):
        return self.__logcount

    @logcount.setter
    def logcount(self, value):
        if not isinstance(value, int):
            raise TypeError("Value should be an integer")
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__logcount = value

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self.role == other.role
        return False

    def __add__(self, other):   # I decided to play with it
        if isinstance(other, SiteUser) and type(self) == type(other):
            self.logcount += other.logcount
        elif isinstance(other, int):
            self.logcount += other
        else:
            raise TypeError("Set type int or SiteUser object")

    def __str__(self):
        return f"SiteUser: {self.name}, mailbox: {self.email}, access level: {self.role}"


class AnotherSiteUsers(SiteUser):
    def __init__(self, name, email, role):
        super().__init__(name, email, role)


if __name__ == "__main__":

    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

    print(user1)

    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")

    print(user1.logcount)
    user1.logcount = 1
    print(user1.logcount)
    user2.logcount = 1
    print(user2.logcount)

    user1 + user2
    print(user1.logcount)
    user1 + 5
    print(user1.logcount)
