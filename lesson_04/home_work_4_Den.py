adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
text_gap = ("\n" * 3)
adwentures_of_tom_sawer_task_1 = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer_task_1, text_gap)



# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_task_2 = adwentures_of_tom_sawer_task_1.replace("....", " ")
print(adwentures_of_tom_sawer_task_2, text_gap)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_task_3 = adwentures_of_tom_sawer_task_2.replace("   ", " ")
print(adwentures_of_tom_sawer_task_3, text_gap)
# Вот тут вопросик: все не одинарные пробелы были тройными как я понял, так что их легко реплейснуть.
# Сложности бы были, если то двойной, то пятирной пробел встречался. Такое пофиксить только через цикл можно было б?

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adwentures_of_tom_sawer_task_4 = adwentures_of_tom_sawer_task_3
h_quantity = adwentures_of_tom_sawer_task_4.count("h")
print(h_quantity, text_gap)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer_task_5 = adwentures_of_tom_sawer_task_4
capital_letter_quantity = (
    adwentures_of_tom_sawer_task_5.count("A") +
    adwentures_of_tom_sawer_task_5.count("B") +
    adwentures_of_tom_sawer_task_5.count("C") +
    adwentures_of_tom_sawer_task_5.count("D") +
    adwentures_of_tom_sawer_task_5.count("E") +
    adwentures_of_tom_sawer_task_5.count("F") +
    adwentures_of_tom_sawer_task_5.count("G") +
    adwentures_of_tom_sawer_task_5.count("H") +
    adwentures_of_tom_sawer_task_5.count("I") +
    adwentures_of_tom_sawer_task_5.count("J") +
    adwentures_of_tom_sawer_task_5.count("K") +
    adwentures_of_tom_sawer_task_5.count("L") +
    adwentures_of_tom_sawer_task_5.count("M") +
    adwentures_of_tom_sawer_task_5.count("N") +
    adwentures_of_tom_sawer_task_5.count("O") +
    adwentures_of_tom_sawer_task_5.count("P") +
    adwentures_of_tom_sawer_task_5.count("Q") +
    adwentures_of_tom_sawer_task_5.count("R") +
    adwentures_of_tom_sawer_task_5.count("S") +
    adwentures_of_tom_sawer_task_5.count("T") +
    adwentures_of_tom_sawer_task_5.count("U") +
    adwentures_of_tom_sawer_task_5.count("V") +
    adwentures_of_tom_sawer_task_5.count("W") +
    adwentures_of_tom_sawer_task_5.count("X") +
    adwentures_of_tom_sawer_task_5.count("Y") +
    adwentures_of_tom_sawer_task_5.count("Z")
)
print(f"Кількість литер верхнього регістру у тексті дорівнює: {capital_letter_quantity}{text_gap}")
# Странно, их же вроде 13 должно быть


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adwentures_of_tom_sawer_task_6 = adwentures_of_tom_sawer_task_5
tom_second_position_is = adwentures_of_tom_sawer_task_6.find("Tom", 1)
print(tom_second_position_is, text_gap)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_task_7 = adwentures_of_tom_sawer_task_6
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_task_7.split(".")
print(f"{adwentures_of_tom_sawer_sentences}, \n {type(adwentures_of_tom_sawer_sentences)}{len(adwentures_of_tom_sawer_sentences)}{text_gap}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_task_8 = adwentures_of_tom_sawer_sentences
print(f"{(adwentures_of_tom_sawer_sentences[3].lower())}{text_gap}")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_task_9 = adwentures_of_tom_sawer_task_8
# Вот так отлично было б, и не ломало последовательность "наследования" переменных
print(f"Чи є реченя, яке починається з \"By the time\"?: {any(sentences.startswith(" By the time") for sentences in adwentures_of_tom_sawer_task_9)}\n")
# Но пусть будет попроще, тогда нужно "наследоваться" до того как мы разбили стрингу на список
adwentures_of_tom_sawer_task_9a = adwentures_of_tom_sawer
print(f"Чи є реченя, яке починається з \"By the time\"?: {adwentures_of_tom_sawer_task_9a.startswith(' By the time')}\n")
# вот это всегда возвращает "фолс". Ну не начинаеться вся строка ' By the time', ну окей. Как тогда сделать проще хммм....?
print(f"Does 1 sentence begin with the line \"By the time\"?: {adwentures_of_tom_sawer_task_9[0].startswith(" By the time")}\n" + \
      f"Does 2 sentence begin with the line \"By the time\"?: {adwentures_of_tom_sawer_task_9[1].startswith(" By the time")}\n" + \
      f"Does 3 sentence begin with the line \"By the time\"?: {adwentures_of_tom_sawer_task_9[2].startswith(" By the time")}\n" + \
      f"Does 4 sentence begin with the line \"By the time\"?: {adwentures_of_tom_sawer_task_9[3].startswith(" By the time")}\n" + \
      f"Does 5 sentence begin with the line \"By the time\"?: {adwentures_of_tom_sawer_task_9[4].startswith(" By the time")}\n" + \
      f"Does 6 sentence begin with the line \"By the time\"?: {adwentures_of_tom_sawer_task_9[5].startswith(" By the time")}{text_gap}")



# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_task_10 = adwentures_of_tom_sawer_sentences
print(f"{len(adwentures_of_tom_sawer_task_10[-2].lstrip(' ').split(' '))}\n")
print(adwentures_of_tom_sawer_task_10[-2].split(' '), "\n")
# Хух, ну вроде всё....))
