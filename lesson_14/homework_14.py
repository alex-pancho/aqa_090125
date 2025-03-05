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
   
    def __init__(self, name:str, email:str, level_access, logcount = 0):
        self.name = name
        self.__email = email
        self.__level_access = level_access
        self.logcount = logcount

    @property  
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email:str):
            self.__email = email
        
    @property  
    def level_access(self):
        return self.__level_access
    
    @level_access.setter
    def level_access(self, level_access:str):
            self.__level_access = level_access    

    def track_logcount(self):
        self.logcount += 1 

    def __str__(self):
        return f"SiteUser: {self.name}, email: {self.__email}, access level: {self.__level_access}, logcount: {self.logcount}"
    
    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self.__level_access == other.__level_access
        return False
         
user1 = SiteUser("John Doe", "john.doe@example.com", "user")
user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: SiteUser: John Doe, mailbox: john.doe@example.com, access level: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

user2.track_logcount()
print(user2)
user2.track_logcount()
print(user2)
