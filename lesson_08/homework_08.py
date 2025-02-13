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


def sum_numbers_in_list(some_list: list):
    """Counts sum of numbers in each string"""
    if not isinstance(some_list, list):
        raise ValueError("Не можу це зробити!")
    elif some_list == []:
        raise ValueError("Не можу це зробити!")
    sum_of_numb = []
    for el in some_list:
        try:
            sum_of_numb.append(sum([int(num) for num in el.split(',')]))
        except ValueError as value_err:
            sum_of_numb.append(f'Не можу це зробити! :{value_err}')
        except AttributeError as at_err:
            sum_of_numb.append(f'Не можу це зробити! :{at_err}')     
    return sum_of_numb


if __name__ == "__main__":
    output = sum_numbers_in_list("21")
    print(output)

    # output = sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50"])
    # print(output)

    # output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    # print(output)

    # output = sum_numbers_in_list(["1,2,3", 7])
    # print(output)

    # output = sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50", sum, min(1, 2)])
    # print(output)

    # output = sum_numbers_in_list([
    #                 "1,2,3,4",
    #                 "1,2,3,4,50",
    #                 "qwerty1,2,3",
    #                 {"country": "Ukraine", "continent": "Europe", "size": 123},
    #             ])
    # print(output)

    # output = sum_numbers_in_list([])
    # print(output)

    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """
