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
    def __init__(self, name, email, access_level="user"):
        self.__name = name
        self.__email = email
        self._access_level = access_level
        self._logcount = 0

    # Гетери
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def access_level(self):
        return self._access_level
    
    @property
    def logcount(self):
        return self._logcount
    
    # сетери
    @name.setter
    def name(self, name):
        self.__name = name

    @email.setter
    def email(self, email):
        self.__email = email

    @access_level.setter
    def access_level(self, access_level):
        if access_level in ["admin", "moderator", "user", "blocked"]:
            self._access_level = access_level
        else:
            raise ValueError("Невірний рівень доступу")

    @logcount.setter 
    def logcount(self, count):
        if isinstance(count, int) and count>=0:
            self._logcount = count
        else:
            raise ValueError("Лічильник логінів має бути невід'ємним цілим числом")

    # Метод для збільшення logcount
    def increase_logcount(self):
        self._logcount +=1

    
    # Логін користувача
    def login(self):
        if self._access_level == "blocked":
            print(f"Користувач {self.__name} заблокований і не може увійти.")
        else:
            self.increase_logcount()
            print(f"{self.__name} увійшов в систему. Вхід №{self._logcount}.")


    def __str__(self):
        return f"SiteUser: {self.__name}, mailbox: {self.__email}, access level: {self._access_level}"

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self._access_level == other._access_level
        return False

if __name__ == "__main__": 
      
    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

    # user2.access_level = "superadmin"
    # user2.logcount = -1

    user1.login()
    user1.login()
    user2.login()

    print(user1)
    print(user2)

    # Порівняння користувачів
    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")

    # Порівняння за рівнем доступу
    print(user1 == user2)  
    user2.access_level = "user"
    print(user1 == user2)  # Тепер рівні доступу однакові