import csv
from pathlib import Path

csv_path = Path(__file__).parent / "new.csv"

with open(csv_path, 'r', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=";")
    print(type(reader))
    for row in reader:
        print(type(row))
        print(', '.join(row))

data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

csv_2_path = Path(__file__).parent / "new2.csv"
with open(csv_2_path, 'w', encoding="utf8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(data)
