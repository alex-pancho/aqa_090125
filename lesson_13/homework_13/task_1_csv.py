import csv
from pathlib import Path
from collections import OrderedDict

def read_csv(file_name):
    """Зчитуємо дані з CSV файлу та повертаємо список рядків"""
    file_path = Path(__file__).parent / file_name
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def remove_duplicates(data1, data2):
    """Прибираємо дублікати з двох списків"""
    # Об'єднуємо два списки
    combined_data = data1 + data2
    # Створюємо множину для унікальних рядків
    unique_data = []
    seen = set()
    for row in combined_data:
        row_tuple = tuple(row)  # Перетворюємо рядок у кортеж для порівняння
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)
    return unique_data

def write_csv(file_name, data):
    """Записуємо дані в CSV файл"""
    file_path = Path(__file__).parent / file_name
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def parse(data):
    """Парсить дані для очищення і форматування"""
    result = OrderedDict()
    for row in data:
        id_, *data = map(str.strip, row)

        if len(data) < 13:
            print(f"Error in {id_}: {data}")
            data += [""] * (15 - len(data))

        if data[-1] == "":
            del data[-1]

        # Прибираємо дублікати, якщо вони є
        if id_ not in result:
            result[id_] = data
        else:
            continue  # Пропускаємо дублікати

    return result

def main():
    # Читаємо два CSV файли
    data1 = read_csv('random.csv')
    data2 = read_csv('random-michaels.csv')

    # Прибираємо дублікати
    unique_data = remove_duplicates(data1, data2)

    # Парсимо дані та очищуємо
    parsed_data = parse(unique_data)

    # Записуємо результат в файл result_Protsenko.csv
    write_csv('result_Protsenko.csv', parsed_data)
    print("Дублікати прибрані, результат записано у файл result_Protsenko.csv")

if __name__ == '__main__':
    main()
