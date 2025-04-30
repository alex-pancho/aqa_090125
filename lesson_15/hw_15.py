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
        if isinstance(value, (int, float)):

            if name == "side_a":

                if value <= 0:
                    raise ValueError("Length must be positive")

            if name == "angle_a":

                if not (0 < value < 180):
                    raise ValueError("Angle should be between 0 and 180 degree")

                super().__setattr__("angle_b", 180 - value)

            if name == "angle_b":

                if not (0 < value < 180):
                    raise ValueError("Angle should be between 0 and 180 degree")

                super().__setattr__("angle_a", 180 - value)

            super().__setattr__(name, value)

        else:
            raise ValueError(f"Value of {name} should be int ot float type")

    def __str__(self):
        return f"Rhombus: side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b}"


if __name__ == "__main__":

    rhombus = Rhombus(5, 60)
    print(rhombus)
    print(rhombus.side_a)
    print(rhombus.angle_a)
    print(rhombus.angle_b)
    rhombus.angle_b = 50
    print(rhombus.angle_a)
