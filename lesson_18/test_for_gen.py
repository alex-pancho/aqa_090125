import pytest

def add_numbers(a, b):
	return a + b

def test_zip():
    a_values = [1, 2, 3]
    b_values = [10, 20, 30]
    expected = [11, 22, 33]
    for (a, b), exp in zip(zip(a_values, b_values), expected):
        assert add_numbers(a, b) == exp, f"Помилка: {a} + {b} != {exp}"

test_zip()

def multiply_by_two(x):
	return x * 2

def test_map():
    data = [1, 2, 3, 4, 5]
    expected = [2, 4, 6, 8, 10]
    result = list(map(multiply_by_two, data))
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ test_map() пройшов успішно!")

test_map()

def file_line_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Використання генератора


# def test_data():
#     for i in range(1, 6):
#         yield f"Test case {i}"

# # Використання у тестуванні
# for data in test_data():
#     print(f"Running test with: {data}")


