"""
### **Завдання для розробника**
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

### **Вимоги до реалізації**
1. **Коректний вхід:**
   - Якщо елемент списку є рядком із числами, розділеними комами 
   (наприклад, `"1,2,3"`), функція повинна повернути їхню суму як ціле число.
   - Наприклад, `sum_numbers_in_list(["1,2,3", "4,0,6"]) → [6, 10]`.

2. **Некоректні рядки:**
   - Якщо рядок містить некоректні символи (наприклад, `"4/0,6"`, `"asas7,8,9"`), 
   функція повинна повернути `"Не можу це зробити!"` для цього елемента.

3. **Некоректні типи:**
   - Якщо елемент списку **не є рядком** (наприклад, число, функція або словник), 
   функція повинна повертати `"Не можу це зробити! AttributeError"`.

4. **Порожній список:**
   - Якщо передано порожній список `[]`, функція повинна викликати `ValueError`.

5. **Неправильний тип вхідних даних:**
   - Якщо передано не список (наприклад, `"21"` або `3`), функція повинна 
   викликати `ValueError`.

### **Очікувані результати тестів**
Функція повинна успішно проходити всі тестові випадки, наведені у класі 
`TestSumNumbersInList`.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```

**Вимоги до коду:**
- Використовувати Python 3.
- Дотримуватись принципів чистого коду.
- Перевірити роботу функції за допомогою `unittest`.

"""


# def sum_numbers_in_list():
#     """Повертає список сум чисел зі списку строк,
#     які складаються з чисел, розділених комою."""

#     result = []
#     for i in string_list:
#         try:
#             result.append(sum([int(x) for x in i.split(",")]))
#         except ValueError as e:
#             result.append("Не можу це зробити!")

#     return result


# if __name__ == "__main__":
#     output = sum_numbers_in_list(["1,2,3", "4,0,6"])
#     print(output)

#     output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
#     print(output)
#     """
#     sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
#     sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
#     sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
#     sum_numbers_in_list([])  # ValueError
#     sum_numbers_in_list("21")  # ValueError
#     """

def sum_numbers_in_list(strings) -> list:
    """
    Функція приймає список рядків, у яких числа розділені комами,
    і повертає список їхніх сум або повідомлення про помилки.

    Валідація:
    - Якщо передано не список, викликає ValueError.
    - Якщо список порожній, викликає ValueError.
    - Якщо елемент списку не є рядком, повертає "Не можу це зробити! AttributeError".
    - Якщо в рядку є нечислові символи, повертає "Не можу це зробити".
    
    :param strings: Список рядків із числами, розділеними комами.
    :return: Список сум чисел або повідомлення про помилки.
    """
    if not isinstance(strings, list):
        raise ValueError("A list of strings is expected!")
    if not strings:
        raise ValueError("The list cannot be empty! Please enter a value.")

    results = []
    
    for s in strings:
        if not isinstance(s, str):
            results.append("Не можу це зробити! AttributeError")
        else:
            try:
                numbers = list(map(int, s.split(','))) 
                results.append(sum(numbers))
            except ValueError:
                results.append("Не можу це зробити!")

    return results 

# **Перевірка коду**
if __name__ == "__main__":
   try:
      print(sum_numbers_in_list(["1,2,3", "4,0,6"]))  

      print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))  

      print(sum_numbers_in_list(["1,2,3,4", 7]))  

      print(sum_numbers_in_list([]))

   except ValueError as e:
      print(f"{e}")

   try:
      print(sum_numbers_in_list("21"))
   except ValueError as e:
      print(f"{e}")
