
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
            raise ValueError("Side_a must be greater than 0")
        if name == "angle_a" and not (0 < value < 180):
            raise ValueError("Angle_a must be between 0 and 180")
        object.__setattr__(self, name, value)

    @property
    def angle_b(self):
        """Обчислює суміжний кут β"""
        return 180 - self.angle_a
    
    def __str__(self):
        return (f"Rhombus: side a = {self.side_a}, angle a = {self.angle_a}°, angle b = {self.angle_b}°.")

if __name__ == "__main__":
# Приклад використання
    rhomb = Rhombus(10, 120)
    print(rhomb)

    # rhomb.angle_a = 190
    # rhomb.side_a = -5
