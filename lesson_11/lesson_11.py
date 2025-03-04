""" Задано дані (список списків) про багаж (кількість речей і загальна вага багажу) пасажирів. 
1. Скласти функцію, яка повертає тапл де міститься: 
    * кількість пасажирів, які мають більше двох речей; 
    * чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг; 
    * число пасажирів, кількість речей яких перевершує середнє число речей всіх пасажирів.
2. Напишіть тести для перевірки роботу функції на різних вхідних даних.
# Алгоритм вирішення
1. Проведіь розрахунок кількості пасажирів з більше ніж 2 речами
2. Виконайте перевірку наявності пасажира з однією річчю вагою менше 25 кг
3. Проведіь обчислення середнього числа речей
4. З'ясуйте кількість пасажирів, які мають більше речей за середнє значення
"""

# Приклад вхідних даних
passengers = [
    {'number_of_items': 3, 'total_weight': 30},
    {'number_of_items': 2, 'total_weight': 20},
    {'number_of_items': 1, 'total_weight': 15},
    {'number_of_items': 4, 'total_weight': 40},
    {'number_of_items': 1, 'total_weight': 10},
    {'number_of_items': 5, 'total_weight': 50},
    {'number_of_items': 2, 'total_weight': 18},
    {'number_of_items': 3, 'total_weight': 35},
    {'number_of_items': 1, 'total_weight': 5},
    {'number_of_items': 4, 'total_weight': 45}
]

import unittest

def check_passanger(passengers): 
    count_more_then_two_items = 0
    has_one_item_less_25 = False
    total_items = sum(p['number_of_items'] for p in passengers)
    avg_items = total_items / len(passengers)
    count_above_avg = 0 
    
    for p in passengers:
        if p['number_of_items'] > avg_items:
            count_above_avg += 1
    
    for p in passengers:
        if p['number_of_items'] > 2:
            count_more_then_two_items += 1
            
        if p['number_of_items'] == 1 and p['total_weight'] < 25:
            has_one_item_less_25 = True

    

    return count_more_then_two_items, has_one_item_less_25, count_above_avg


class TestCheckPassenger(unittest.TestCase):
    
    def test_count_more_then_two_items(self):
        result = check_passanger(passengers)
        self.assertEqual(result[0] , 5)
        
    def test_has_one_item_less_25(self):
        result = check_passanger(passengers)
        self.assertTrue(result[1])
        
    def test_calculate_avg_items(self):
        result = check_passanger(passengers)
        total_items = sum(p['number_of_items'] for p in passengers)
        avg_items = total_items / len(passengers)
        
        count_above_avg = 0
        for p in passengers:
            if p['number_of_items'] > avg_items:
                count_above_avg += 1
        
        self.assertEqual(result[2], count_above_avg)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
    
    result = check_passanger(passengers)
    print(result)
        

        