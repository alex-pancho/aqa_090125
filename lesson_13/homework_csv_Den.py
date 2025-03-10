import csv
import os

print("Текущая рабочая директория:", os.getcwd())

file1 = "r-m-c.csv"
file2 = "random-michaels.csv"
output_file = "uniq_row_Den.csv"

def read_csv_as_list(filename):
    """Читает CSV и возвращает список строк (без заголовка)"""
    with open(filename, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = [tuple(row) for row in reader]  # Преобразуем строки в кортежи
    return header, rows

# Читаем данные из обоих файлов
header1, rows1 = read_csv_as_list(file1)
header2, rows2 = read_csv_as_list(file2)

# Проверяем, совпадают ли заголовки
if header1 != header2:
    print("\n⚠️ Ошибка: Заголовки в файлах не совпадают!")
    exit(1)

# Вычисляем уникальные строки
unique_rows = set(rows1) ^ set(rows2)  # Симметрическая разность (строки, которые есть только в одном файле)

# Записываем уникальные строки в новый файл
with open(output_file, "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(header1)
    writer.writerows(unique_rows)

print(f"\n✅ Файл {output_file} был успешно создан.")
print(f"  🔹 Уникальных строк записано: {len(unique_rows)}")

# 📌 Проверка результата
def count_rows(filename):
    """Считает количество строк в файле (без заголовка)"""
    with open(filename, "r", encoding="utf8") as file:
        return sum(1 for _ in file) - 1  # Вычитаем заголовок

count1 = count_rows(file1)
count2 = count_rows(file2)
count_out = count_rows(output_file)

print("\n📊 Итоговая проверка:")
print(f"  📂 {file1}: {count1} строк")
print(f"  📂 {file2}: {count2} строк")
print(f"  📂 {output_file}: {count_out} уникальных строк")

# Проверка на дубликаты
with open(output_file, "r", encoding="utf8") as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    rows = list(reader)

    if len(rows) == len(set(map(tuple, rows))):
        print("\n🎯 Проверка уникальности пройдена: Дубликатов нет!")
    else:
        print("\n⚠️ В файле результата все еще есть дубликаты!")
