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

class SiteUser():
    def __init__(self, name: str, email: str, access_level: str) -> None:
        self.__name = name
        self.__email = email
        self.__access_level = access_level
        self.__logcount = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("Некоректний формат name")
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if not isinstance(email, str):
            raise ValueError("Некоректний формат email")
        self.__email = email

    @property
    def access_level(self) -> str:
        return self.__access_level

    @access_level.setter
    def access_level(self, access_level: str) -> None:
        if access_level not in ["admin", "moderator", "user", "blocked"]:
            raise ValueError("Некоректний access level")
        self.__access_level = access_level

    @property
    def logcount(self) -> int:
        return self.__logcount

    def increment_logcount(self):
        self.__logcount += 1
    

    def __str__(self) -> str:
        return f"SiteUser: {self.name}, mailbox: {self.email}, access level: {self.access_level}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SiteUser):
            return self.__access_level == other.access_level
        return False

"""if __name__ == "__main__":

    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "user")
    print(user1)
    print(user2)
    user1.increment_logcount()
    user1.increment_logcount()
    user2.increment_logcount()
    print(f"{user1.name} logcount:{user1.logcount}")
    print(f"{user2.name} logcount:{user2.logcount}")
    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")
"""