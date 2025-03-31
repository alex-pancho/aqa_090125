from variables import _a as a, Varias
# LEGB
# L-local - локальній області видимості всередині функції 
# E-enclosing - у локальних областях видимості охоплюючих функцій
# G-global - глобальна
# B-built-in  - вбудовані

# def print(arg):
#     return arg
# a = 5
print("Hello world", a)


def print_a():
    a = 6
    print(a)

print_a()
print("19>", a)

def sum_(a, b):
    return sum([a, b]) # a+b

print(sum_(1, 2))

# Приклад локальної області видимості
def example_function():
    x = 10
    print(x)

# Приклад глобальної області видимості
y = 20

def another_function():
    print(y)

# Приклад нелокальної області видимості
def outer_function():
    z = 30

    def inner_function():
        print(z)  # Звертається до змінної з більш високого рівня

    inner_function()
outer_function()

def run(a):
    a = 2  # re-write 'a' and retun always be 3
    return a + 1

PDV = 20
class MyBuh():
    b = 5  # Enclosing

    def count(self):
        print("b>", self.b)
        # PDV = 21  # DONT DO IT!!!
        print("ПДВ:", PDV)  # Global


coun_buh = MyBuh()
coun_buh.count()
print(PDV)
print(Varias.a)
# Varias.a = 2
# print(Varias.a)

class Parent1:
    def method1(self):
        print("Виклик методу method1 з Parent1")

class Parent2:
    def method2(self):
        print("Виклик методу method2 з Parent2")

class Child(Parent1, Parent2):  # успадковуємо від обох батьків
    pass

child = Child()
child.method1()  # Виведе: Виклик методу method1 з Parent1
child.method2()  # Виведе: Виклик методу method2 з Parent2

class Parent1:
    x = 10

class Parent2:
    y = 20

class Child(Parent1, Parent2):
    pass

child = Child()
print(child.x)  # Виведе: 10, змінна x успадкована від Parent1
print(child.y)  # Виведе: 20, змінна y успадкована від Parent2

class Mama:
    common_field = "значення від Mama"

class Dad:
    common_field = "значення від Dad"
#4
            #3.1  #3.2
class Child(Mama, Dad):
    #2
    def access_common_field(self):
        #1
        common_field_from_mama = Mama.common_field  # Звертаємося до класу Mama
        common_field_from_dad = Dad.common_field  # Звертаємося до класу Dad
        print("Значення common_field з Mama:", common_field_from_mama)
        print("Значення common_field з Dad:", common_field_from_dad)
        print("From self:", self.common_field)

child = Child()
child.access_common_field()