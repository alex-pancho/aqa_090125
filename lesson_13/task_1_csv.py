import csv
from pathlib import Path


def delete_duplicates(list_to_process):
    """ Remove duplicate items from nested list """
    index = len(list_to_process) - 1
    while True:
        if index < 1:
            return
        if list_to_process[index] == list_to_process[index - 1]:
            del list_to_process[index]
            index -= 1
            continue
        index -= 1

def dataset_processing(*, datasets, output_file):
    """ Function receive two or more 'csv' files, process them, create new array with distinct values, write file """
    temp_data_array = []
    header = None

    for dataset in datasets:
        # Open 'csv' file from datasets
        with open(dataset, 'r', encoding='utf-8') as csv_file_to_read:
            data_object = csv.reader(csv_file_to_read, delimiter=',')
            for row in list(data_object):
                # Creating header of document
                if not header:
                    header = row
                # Process row, if 'contactID' has integer type and greater than 0
                if row[0].isdigit() and int(row[0]) > 0:
                    for col_index in range(len(row)):
                        # Replacing special and some other symbols in cols to make more uniform view of document
                        row[col_index] = row[col_index].replace('\n', ' ')
                        row[4] = row[4].replace('.', '/')
                        row[-5] = row[-5].replace('.', '/')
                        # Alternative approach: row[col_index] = row[col_index].replace('/', '.')
                    # Delete last empty element
                    row.pop() if not row[-1] else None
                    temp_data_array.append(row)

    # Sorting array before checking for duplicates
    temp_data_array.sort()
    # Checking for duplicates
    delete_duplicates(temp_data_array)
    # Sort array for 'contact_id' key and inserting header
    temp_data_array.sort(key=lambda contact_id: int(contact_id[0]))
    temp_data_array.insert(0, header)

    # writing result data to file
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file_to_write:
        csv.writer(csv_file_to_write).writerows(temp_data_array)


if __name__ == '__main__':
    ext = '.csv'
    datasets_dir = Path(__file__).parent / "csv_files/"
    list_of_files = [file for file in datasets_dir.iterdir() if file.suffix == ext]
    filtered_csv = Path(__file__).parent / "task_1_filtered.csv"
    dataset_processing(datasets=list_of_files, output_file=filtered_csv)
