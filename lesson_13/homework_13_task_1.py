# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv 
# порівняйте на наявність дублікатів і приберіть їх. 
# Результат запишіть у файл result_<your_second_name>.csv

import csv
from pathlib import Path
from collections import OrderedDict

def process_csv(file_path):
    all_rows = OrderedDict() 
    rows = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_tuple = tuple(row)  # convert to tuple
            if row_tuple not in all_rows:
                all_rows[row_tuple] = None  
                rows.append(row)  # add row to dict
    return rows     

def remove_duplicates_and_merge_csv(file1_path, file2_path, restlt_path):
   
    rows1 = list(process_csv(file1_path))
    rows2 = list(process_csv(file2_path))

    # Writte joined data in results file
    with open(restlt_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if rows1 and rows1[0] == rows2[0]: # check header
             writer.writerow(rows1[0]) # add header
             writer.writerows(rows1[1:])
             writer.writerows(rows2[1:])
        else:
             writer.writerows(rows1)
             writer.writerows(rows2)


file1_path = Path(__file__).parent / "rmc.csv"
file2_path = Path(__file__).parent / "r-m-c.csv"
restlt_path = Path(__file__).parent / "result_lesyk.csv"

remove_duplicates_and_merge_csv(file1_path, file2_path, restlt_path)
