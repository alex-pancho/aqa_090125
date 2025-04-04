class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a  
    
    @property
    def side_a(self):
        return self._side_a
    
    @side_a.setter
    def side_a(self, value):
        if value <= 0:
            raise ValueError
        self._side_a = value
    
    @property
    def angle_a(self):
        return self._angle_a
    
    @angle_a.setter
    def angle_a(self, value):
        if not (0 < value < 180):
            raise ValueError
        self._angle_a = value
        self._angle_b = 180 - value  # оновлюємо суміжний кут
    
    def __str__(self):
        return f"Ромб: сторона={self.side_a}, кут1={self.angle_a}°, кут2={self.angle_b}°"
    
    try:
    rhomb = Rhombus(5, 60)
    print(rhomb)  # Ромб зі стороною 5, кутом A=60°, кутом B=120°
    
    # Спробуємо змінити кут_a
    rhomb.angle_a = 45
    print(rhomb)  # Ромб зі стороною 5, кутом A=45°, кутом B=135°
    
except Exception as e:
print(f"Помилка: {e}")