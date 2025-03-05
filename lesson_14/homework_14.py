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

    def __init__(self, name, email, access_level, logcount = 0):
        self.name = name
        self.email = email
        self.access_level = access_level
        self.__logcount = logcount


    @property
    def logcount(self):
        return self.__logcount

    @logcount.setter
    def logcount(self, quantity):
        if not isinstance(quantity, int):
            raise ValueError("logcount must be int")
        if quantity < 0:
            raise ValueError("logcount must be positive")
        if quantity < self.__logcount:
            raise ValueError("logcount must be greater than previous")
        self.__logcount += quantity


    def __str__(self):
        return f"SiteUser: {self.name}, mailbox: {self.email}, access level: {self.access_level}"
    

    def __eq__(self, other:object):
        if not isinstance(other, SiteUser):
            raise ValueError("other must be SiteUser")
        
        if self.access_level == other.access_level:
            return True
        else:
            return False






if __name__ == "__main__":

    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
    print(user1)
    user1.logcount = 1
    print(user1.logcount)
    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")