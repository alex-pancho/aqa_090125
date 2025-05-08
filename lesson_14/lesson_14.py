

class Car():
    wheels = 4
    engine_on = False
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_type = "diesel"
    
    def start_engine(self):
        self.engine_on = True

toyota_car = Car("Toyota", "Camry")  # init call here
print(toyota_car)
print(toyota_car.brand)
print(toyota_car.model)
print(toyota_car.engine_type)
print(toyota_car.wheels)

mersedes_car = Car("Mersedes", "S300")  # init call here
print(mersedes_car)
print(mersedes_car.brand)
print(mersedes_car.model)
print(mersedes_car.engine_type)
print(mersedes_car.wheels)
print(type(mersedes_car))
print("Before mersedes", mersedes_car.engine_on)
print(mersedes_car.start_engine())
print("After mersedes",mersedes_car.engine_on)
print("Before toyota", toyota_car.engine_on)

class BankAccount():
    def __init__(self, init_balance:int = 0):
        self.__balance = init_balance
    
    def get_balance(self):  # it is getter
        return self.__balance
    
    def withdraw(self, value):
        if value < 0:
            raise ValueError("Use positive number")
        if value > self.__balance:
            raise ValueError("Try less value")
        else:
            self.__balance = self.__balance - value

    @property
    def withdraw_1(self):
        self.withdraw(1)
    
    def refill(self, value):
        self.__balance = self.__balance + value


account = BankAccount(1000)
print(account.get_balance())
account.withdraw_1
print(account.get_balance())
account.withdraw(9)
account.refill(100000)
print(account.get_balance())

acc_2 = BankAccount()
# acc_2.withdraw(1)

class Animal:
    def __init__(self, name:str, legs:int = 4):
        self.name = name
        self.legs = legs
    
    def speak(self):
        return ""

class Dog(Animal):
    def speak(self):
        return "Woh!"

class Cat(Animal):
    def speak(self):
        return "Meaw!"

jerry = Dog("Jerry")
tom = Cat("Tom")

# jerry.legs = 5

print(jerry.name, f"has a {jerry.legs} legs", jerry.speak())
print(tom.name, f"has a {tom.legs} legs",tom.speak())

class Person():
    def __init__(self, age:int = 0) -> None:
        self.__age = age
        self.__name = ""

    @property  # it is getter
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, years:int):
        #self.__age = years
        if not isinstance(years, int):
            raise ValueError("add_year must be int")
        if years >= self.__age:
            self.__age = years
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if not isinstance(new_name, str):
            raise ValueError("new_name must be str")
        if len(new_name) >= len(self.__name):
            self.__name = new_name


p = Person(3)
print(p.age)
p.age = 2
print(p.age)
p.name = "A"
print(p.name)
p.name = "Bb"
print(p.name)
p.name = "c"
print(p.name)
