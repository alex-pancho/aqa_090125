"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

    сторона_а (довжина сторони a).
    кут_а (кут між сторонами a і b).
    кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:

    Значення сторони сторона_а повинно бути більше 0.
    Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення
    кут_б обчислюється автоматично.
    Для встановлення значень атрибутів використовуйте метод __setattr__.
"""
class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError("Значення side_a повинно бути більше 0.")
        super().__setattr__(name, value)

        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут angle_a має бути в межах (0, 180).")
            super().__setattr__("angle_b", 180 - value)

    def __str__(self):
        return f"Rhombus: side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b}"

Rhombus_1 = Rhombus(5, 60)
print(Rhombus_1)
Rhombus_2 = Rhombus(15, 15)
print(Rhombus_2)
#Rhombus_3 = Rhombus(5, 225)
#print(Rhombus_3)
#Rhombus_4 = Rhombus(-5, 25)
#print(Rhombus_4)
