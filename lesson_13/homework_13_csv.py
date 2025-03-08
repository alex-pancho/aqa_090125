import csv

def remove_duplicates(file1, file2, result_file):
    """Функція зчитує два CSV-файли, порівнює їх і видаляє дублікати.
        Результат записується у новий файл."""
    unique_rows = set()

    with open(file1, newline='', encoding='utf-8') as csvfile1:
        reader = csv.reader(csvfile1)
        for row in reader:
            unique_rows.add(tuple(row))

    with open(file2, newline='', encoding='utf-8') as csvfile2:
        reader = csv.reader(csvfile2)
        for row in reader:
            unique_rows.add(tuple(row))

    with open(result_file, 'w', newline='', encoding='utf-8') as file_out:
        writer = csv.writer(file_out)
        writer.writerows(unique_rows)

remove_duplicates('random.csv', 'random-michaels.csv', 'result_Dovhan.csv')