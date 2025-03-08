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
    def __init__(self, *, side:float, angle_a:float):
        self.side = side
        self.angle_a = angle_a

    def __str__(self):
        return f"Rhombus parameters: side={self.side}, angleA={self.angle_a}, angleB={self.angle_b}"

    def __setattr__(self, name, value):
        if isinstance(value, int | float):
            if name == 'side' and value > 0:
                super().__setattr__(name, value)  # Another solution: self.__dict__[name] = value
            elif name == 'angle_a' and 0 < value < 180:
                super().__setattr__(name, value)
                super().__setattr__('angle_b', 180 - value)
            elif name == 'angle_b' and 0 < value < 180:
                super().__setattr__(name, value)
                super().__setattr__('angle_a', 180 - value)
            else:
                raise ValueError(f"Value error: '{name}'={value}, not in range")
        else:
            raise TypeError(f"Type error: '{value}' must be integer/float type. Current type: {type(value).__name__}")


if __name__=='__main__':
    res = Rhombus(side=14.1, angle_a=15.1)
    print(res)
    res.angle_b = 10
    print(res)
    res.angle_a = 40.5
    print(res)
