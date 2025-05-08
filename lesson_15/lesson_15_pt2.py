class Mama:
    common_field = "значення від Mama"
    def method1(self):
        print("Виклик методу method1 з Parent1")
    
class Papa:
    common_field = "значення від Dad"
    def method2(self):
        print("Виклик методу method2 з Parent2")

class Child(Mama, Papa):  # успадковуємо від обох батьків
    
    @property
    def common_field(self):
        self._common_field = [Mama.common_field,  Papa.common_field] # Звертаємося до класу Mama # and Papa
        return self._common_field

baby = Child()
baby.method1()
baby.method2()
print(baby.common_field)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Абстрактний метод


class Mammal(Animal):
    def __init__(self, name, num_legs):
        Animal.__init__(self, name)
        self.num_legs = num_legs


class Bird(Animal):
    def __init__(self, name, wingspan):
        Animal.__init__(self, name)
        self.wingspan = wingspan


class Bat(Mammal, Bird):  # Ромбовидне наслідування
    def __init__(self, name, num_legs, wingspan):
        Mammal.__init__(self, name, num_legs)
        Bird.__init__(self, name, wingspan)

    def sound(self):
        return "Squeak"  # Звук кажана
    
batman = Bat("Robin", 2, 2)
print(batman.sound())