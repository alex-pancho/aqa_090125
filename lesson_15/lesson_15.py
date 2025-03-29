class Car:
    _count = 0
    #new_attr = ""
    def __new__(cls, *args, **kwargs):
        cls.add_new_car()
        instance = super().__new__(cls)
        return instance

    def __init__(self, make, model):
        self.make = make
        self.model = model
        #Car.add_new_car()
    
    def __str__(self):
        return f"Car {self.make} model {self.model}"
    
    def __repr__(self):
        return f"The Car {self.make} model {self.model}"

    @classmethod
    def add_attr(cls, new_attr):
        cls.new_attr = "default"
    
    @classmethod
    def add_new_car(cls):
        cls._count += 1
    
    @property
    def count(self):
        return self._count
  
    @staticmethod
    def loop(counter:int):
        n = 0
        for i in range(1, counter):
            n = i + n
        return i
    
    def __len__(self):
        return self._count * self._count
    
    def __del__(self):
        pass
        #print(f"The {self.make} {self.model} object has been destroyed.")
    
    def __add__(self, other_point):
        self.model = self.model + " " + str(other_point)
        return self.model

class Person:
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)


if __name__ == "__main__":
    my_car_1 = Car("Toyota", "Camry")
    Car.add_attr("new_attr")
    my_car_1.new_attr = "New attr"
    print(my_car_1.new_attr)
    print("my_car_1", my_car_1.count)
    my_car_2 = Car("Mersedes", "C200")
    print(my_car_2.new_attr)
    print("my_car_2", my_car_2.count)
    print("my_car_1", my_car_1.count)
    mc3 = Car("Porshe", "PanAmera")
    print("my_car_1", my_car_1.count)
    del mc3
    mc = Car.loop(5)
    print(mc)
    print("my_car_1", my_car_1.count)
    print(my_car_2)
    print(len(my_car_2))
    new_var = my_car_2 + "dfldjlfsj"
    print(my_car_2)
    print(new_var)
    setattr(Car, "totaly_new", 0)
    print(my_car_2.totaly_new)
    # Створюємо екземпляр класу Person
    person = Person()
    # Встановлюємо атрибути
    person.name = 'Alice'
    person.age = 30
    # Перевіряємо встановлені значення
    print(f'Name: {person.name}')  # Виведе: Name: Alice
    print(f'Age: {person.age}')    # Виведе: Age: 30
