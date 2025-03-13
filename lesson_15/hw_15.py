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
        if name == 'side_a':
            if value <= 0:
                raise ValueError("Довжина сторони має бути більше 0")
        elif name == 'angle_a':
            if value <= 0 or value >= 180:
                raise ValueError("Кут має бути від 0 до 180")
            self.__dict__['angle_b'] = 180 - value
        elif name == 'angle_b':
            raise AttributeError("Не можна задати кут b")
        self.__dict__[name] = value

    def __str__(self):
        return f"Ромб: сторона a={self.side_a}, кут а={self.angle_a}, кут b={self.angle_b}"

if __name__ == "__main__": 
    rhombus = Rhombus(15, 34)
    print(rhombus)
