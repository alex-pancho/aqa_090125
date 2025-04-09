'''Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек - наприкладTimestamp 05:45:40, а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)

Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік - Key TSTFEED0300|7E3E|0400

Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt

відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
       3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.

Обов’язково включіть результат роботи — файл hb_test.log в PR.
'''

from datetime import datetime
from logger import logger

def analyze_heartbeat():
    with open('hblog.txt', 'r', encoding='utf-8') as f:
        filtered = [line for line in f if 'TSTFEED0300|7E3E|0400' in line]
    

    times = []
    for line in filtered:
        pos = line.find("Timestamp ")
        if pos != -1:
            time_str = line[pos+10:pos+18]
            times.append(datetime.strptime(time_str, "%H:%M:%S"))
    
    
    for i in range(len(times)-1):
        diff = (times[i] - times[i+1]).total_seconds()
        
        if 31 < diff < 33:
            logger.warning(f"Heartbeat delay: {diff}sec between {times[i+1].time()} and {times[i].time()}")
        elif diff >= 33:
            logger.error(f"Heartbeat delay: {diff}sec between {times[i+1].time()} and {times[i].time()}")

if __name__ == '__main__':
    analyze_heartbeat()