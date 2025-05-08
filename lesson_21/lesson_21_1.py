import time


# Отримуємо поточний час у вигляді кортежу
current_time = time.localtime()
print(current_time)
date_in_database_1 = "2021-09-02 13:12:00"
date_in_database_2 = "2021/02/09 1:12 PM"
format_european = "%Y-%m-%d %H:%M:%S"
format_gbuk = "%Y/%d/%m %I:%M %p"

py_date_in_database_1 = time.strptime(date_in_database_1, format_european)
print(py_date_in_database_1)

py_date_in_database_2 = time.strptime(date_in_database_2, format_gbuk)
print(py_date_in_database_2)
print(py_date_in_database_1 == py_date_in_database_2)

str_date_in_database_1 = time.strftime(format_gbuk, py_date_in_database_1)
print(str_date_in_database_1)
time.sleep(1)
current_time = time.localtime()
print(current_time)

unixtime = 1744044660
my_datetime = time.ctime(unixtime)
print(my_datetime)