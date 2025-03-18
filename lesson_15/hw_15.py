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

    def __setattr__(self, key, value):
        if key == "side_a" and value <= 0:
            raise ValueError("Side length must be greater than 0")
        if key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle must be between 0 and 180 degrees")
            object.__setattr__(self, "angle_b", 180 - value)
        object.__setattr__(self, key, value)

    def __str__(self):
        return f"Rhombus: side = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"
