def sum_numbers_in_list(input_list):
    """Повертає список сум чисел зі списку строк або повідомлення про помилку."""
    if not isinstance(input_list, list):
        raise ValueError("Очікується список!")

    if not input_list:
        raise ValueError("Список порожній")

    result = []
    for item in input_list:
        if not isinstance(item, str):
            result.append("Не можу це зробити! AttributeError")
            continue

        try:
            numbers = [int(x) for x in item.split(",")]
            result.append(sum(numbers))
        except ValueError:
            result.append("Не можу це зробити!")

    return result


if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)  # [6, 10]

    output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(output)  # [6, "Не можу це зробити!", "Не можу це зробити!"]

    output = sum_numbers_in_list(["1,2,3", 7])
    print(output)  # [6, "Не можу це зробити! AttributeError"]

    try:
        sum_numbers_in_list([])
    except ValueError as e:
        print(f"Помилка {e}")  # Помилка Список порожній

    try:
        sum_numbers_in_list("21")
    except ValueError as e:
        print(f"Помилка {e}")  # Помилка Очікується список!
