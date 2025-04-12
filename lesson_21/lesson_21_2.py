from datetime import datetime, timedelta

now = datetime.now()
print(now)

unixtime = 1744044660
# Створення об'єкта datetime з мітки часу
dt = datetime.fromtimestamp(unixtime)
print(dt)

to_unix = datetime.timestamp(now)
print(to_unix)
anna_born = "1996-06-05"
anna_format = "%Y-%m-%d"
anna_to_dt = datetime.strptime(anna_born, anna_format)
print(anna_to_dt)
to_unix = datetime.timestamp(anna_to_dt)
print(to_unix)

begin_unix_time = datetime.fromtimestamp(0)
print("begin_unix_time", begin_unix_time)

today_date = datetime.today()
print(today_date)
format_european = "%Y-%m-%d %H:%M:%S"
format_gbuk = "%Y/%d/%m %I:%M %p"
for format in [format_european, format_gbuk]:
    current_formated_date = datetime.strftime(today_date, format)
    print(current_formated_date)
print("ISO", datetime.isoformat(today_date))

td = timedelta(days=5, hours=3, minutes=30)
td2 = timedelta(days=1)
print(td+td2)
# Поточна дата та час
now = datetime.now()
# Попередня дата та час (наприклад, якщо ви хочете визначити, що було 5 днів тому)
past_date = now - timedelta(days=5)
time_difference = now - past_date

print(f"Поточна дата та час: {now}")
print(f"Попередня дата та час: {past_date}")
print(f"Різниця між датами: {time_difference}")

diff_time = now - dt
print(f"Різниця між датами {now} i {dt}: {diff_time}")
if diff_time > timedelta(minutes=43):
    print("More than 30 mins")

