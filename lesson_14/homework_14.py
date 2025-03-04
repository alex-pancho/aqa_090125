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
def check_permissions(func):
    """
    Decorator for checking user permissions while calling instance methods for.
    'admin' - grant all privileges
    'blocked' - restrict access to all attributes
    'moderator' and 'user' - grant read-only access to attributes
    """
    def wrapper(instance, *args, **kwargs):
        # Extract 'permission' from instance
        permission = getattr(instance, f"_{instance.__class__.__name__}__permission", None)
        if permission == 'admin':
            return func(instance, *args, **kwargs)
        elif permission == 'blocked':
            user_name = getattr(instance, f"_{instance.__class__.__name__}__name", None)
            print(f"User: '{user_name}' blocked")
        else:
            # Don't allow change attributes (setter) with no-admin privileges. Instead allow reading (getter).
            if args or kwargs:
                attr_value = getattr(instance, f"{func.__name__}", None)
                print(f"You don\'t have permissions to overwrite this attribute ({func.__name__}). Value still: '{attr_value}'")
            else:
                return func(instance, *args, **kwargs)
    return wrapper

class SiteUser:
    def __init__(self, *, name, email, permission):
        self.__name = name
        self.__email = email
        self.__permission = permission
        self.__log_count = 0

    def __repr__(self):
        return f"User: '{self.__name}' (status:{self.__permission}) logged {self.__log_count} times"

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            result = self.__permission == other.__permission
            return result

    # Simulate 'login' feature to increase 'log_count'
    @check_permissions
    def __call__(self):
        print(f"User: '{self.name}' logged in...")
        self.__log_count += 1

    # User with 'admin' privileges can change permissions of other users
    @check_permissions
    def change_permission(self, *, target_user, new_permission):
        if isinstance(target_user, SiteUser) and isinstance(new_permission, str):
            target_user.__permission = new_permission
            print(f"Permission for user: '{target_user.name}' has been changed")

    @property
    @check_permissions
    def log_count(self):
        return self.__log_count

    @log_count.setter
    @check_permissions
    def log_count(self, value):
        if isinstance(value, int):
            self.__log_count = value
            print('Log count saved')

    @property
    @check_permissions
    def email(self):
        return self.__email

    @email.setter
    @check_permissions
    def email(self, value):
        if isinstance(value, str) and value:
            self.__email = value
            print('Email saved')

    @property
    @check_permissions
    def name(self):
        return self.__name

    @name.setter
    @check_permissions
    def name(self, new_name):
        if isinstance(new_name, str) and new_name:
            self.__name = new_name
            print('Name saved')


if __name__ == '__main__':

    user1 = SiteUser(name="John Doe", email="john.doe@example.com", permission="user")
    user2 = SiteUser(name="Jane Smith", email="jane.smith@example.com", permission="admin")
    user3 = SiteUser(name="John Waine", email="john.waine@example.com", permission="blocked")
    user4 = SiteUser(name="Axel Murphy", email="axel@example.com", permission="moderator")
    # user5 = SiteUser(name='Unknown', email='unknown')

    print(user1.log_count)
    user1.log_count = 10
    user1()
    print(user1)
    user3()
    user3.log_count = 3
    print(user1.log_count)
    print(user2)
    user2.log_count = 10
    print(user2.log_count)
    user1.email = '123'
    print(user1.email)
    user2()
    print(user2)
    user4()
    print(user4)
    user4.name = 'George'
    print(user3)
    user3.email = '123@example.com'
    user1.change_permission(target_user=user3, new_permission='user')
    user2.change_permission(target_user=user3, new_permission='user')
    # user3()
    print(user3)
    print(user1 == user4)
    # print(user1.get)
    user1.change_permission(target_user=user1, new_permission='user')