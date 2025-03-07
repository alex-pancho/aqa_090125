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
    def __init__(self, name, email, access_lvl):
        # рівень доступу (admin, moderator, user, blocked)
        self.__name = name
        self.__email = email
        self.__access_lvl = access_lvl
        self.__logcount = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
    
    @property
    def access_lvl(self):
        return self.__access_lvl
    
    @access_lvl.setter
    def access_lvl(self, value):
        self.__access_lvl = value
        
    @property
    def logcount(self):
        return self.__logcount
    
    def logcount_plus(self):
        self.__logcount += 1

    @logcount.setter
    def logcount(self, value):
        if not isinstance(value, int):
            raise ValueError("Дані не є числом!")
        self.__logcount = value

    def __str__(self):
        return f'Name: {self.__name}, email: {self.__email}, access level: {self.__access_lvl}, number of logins: {self.__logcount}'

    def __eq__(self, other_user):
        if self.__access_lvl == other_user.__access_lvl:
            return f'{True}, Користувачі однакові'
        else:
            return f'{False}, Користувачі різні'