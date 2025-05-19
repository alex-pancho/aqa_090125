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
        self.__setattr__('side_a', side_a)
        self.__setattr__('angle_a', angle_a)
        self.__setattr__('angle_b', 180 - angle_a)

    def __setattr__(self, name, value):
        if name == 'side_a' and value <= 0:
            print("Error: The value of side_a must be greater than 0")
            return
        if name == 'angle_a' and not (0 < value < 180):
            print("Error: angle_a must be between 0 and 180 degrees")
            return
        super().__setattr__(name, value)

    def __str__(self):
        try:
            return f"Rhombus: side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b}"
        except AttributeError:
            return "Invalid Rhombus: missing or incorrect attributes"