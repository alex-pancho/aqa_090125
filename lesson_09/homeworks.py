# homework 8

def do_sum(numbers: list) -> list:

    if not isinstance(numbers, list):
        raise TypeError("Value is not list")
    if not numbers:
        raise ValueError("List is empty")

    res = []

    for i in numbers:
        if not isinstance(i, str):
            raise TypeError("Type is not a str")
        if not i.replace(",", "").isdigit():
            raise ValueError("There are not only digits")
        res.append(sum(map(int, i.split(","))))

    return res


def get_sum_of_numbers(numbers: list) -> list:
    try:
        return do_sum(numbers)
    except (ValueError, TypeError) as e:
        print("Не можу це зробити:", e)


def revers_string(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Input data is not string")
    return string[::-1]


def get_common_set_data(set_1: set, set_2: set) -> set:
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        raise TypeError("Input type is not a set")
    return set_1 & set_2


def sort_people_by_age(person_list: list[tuple[str, int]]) -> dict:
    data = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
    for person in person_list:
        name, age = person
        if 10 <= age <= 19:
            data['10-19'].append(name)
        elif 20 <= age <= 29:
            data['20-29'].append(name)
        elif 30 <= age <= 39:
            data['30-39'].append(name)
        elif 40 <= age <= 49:
            data['40-49'].append(name)
        else:
            raise ValueError("Value is not in range")
    return data


if __name__ == "__main__":

    print(get_sum_of_numbers(["1,2,3,4"]))
    print(get_sum_of_numbers(["1,2,3,4,50"]))
    print(get_sum_of_numbers("1,2,3,4,50"))
    print(get_sum_of_numbers(["qwerty1,2,3"]))
    print(get_sum_of_numbers([]))
    print(get_sum_of_numbers({}))
    print(get_sum_of_numbers(12345))
    print(get_sum_of_numbers(["1,2,3,4,5", "1,2,3,4"]))
    print(get_common_set_data({1, 2, 3}, {2, 3, 4}))
    print(sort_people_by_age([('Alice', 25), ('Boby', 19), ('Charlie', 32),('David', 28), ('Emma', 22), ('Frank', 45)]))
