
some_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", [], {}, (), 12345]


def do_sum(numbers: str) -> int:
    if not isinstance(numbers, str):
        raise TypeError("Type is not a str")
    elif not numbers.replace(",", "").isdigit():
        raise ValueError("There are not only digits")
    return sum(map(int, numbers.split(",")))


def get_sum_of_numbers(numbers: str) -> int:
    try:
        return do_sum(numbers)
    except (ValueError, TypeError) as e:
        print("Не можу це зробити:", e)


for i, element in enumerate(some_list):
    print(get_sum_of_numbers(some_list[i]))
