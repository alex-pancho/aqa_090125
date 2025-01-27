import re
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
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

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


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_of_h = adwentures_of_tom_sawer.count("h")
print(f' Кількість символу h в тексті дорівнює {count_of_h}')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_of_capital_A = adwentures_of_tom_sawer.count("A")
count_of_capital_B = adwentures_of_tom_sawer.count("B")
count_of_capital_C = adwentures_of_tom_sawer.count("C")
count_of_capital_D = adwentures_of_tom_sawer.count("D")
count_of_capital_E = adwentures_of_tom_sawer.count("E")
count_of_capital_F = adwentures_of_tom_sawer.count("F")
count_of_capital_G = adwentures_of_tom_sawer.count("G")
count_of_capital_H = adwentures_of_tom_sawer.count("H")
count_of_capital_I = adwentures_of_tom_sawer.count("I")
count_of_capital_J = adwentures_of_tom_sawer.count("J")
count_of_capital_K = adwentures_of_tom_sawer.count("K")
count_of_capital_L = adwentures_of_tom_sawer.count("L")
count_of_capital_M = adwentures_of_tom_sawer.count("M")
count_of_capital_N = adwentures_of_tom_sawer.count("N")
count_of_capital_O = adwentures_of_tom_sawer.count("O")
count_of_capital_P = adwentures_of_tom_sawer.count("P")
count_of_capital_Q = adwentures_of_tom_sawer.count("Q")
count_of_capital_R = adwentures_of_tom_sawer.count("R")
count_of_capital_S = adwentures_of_tom_sawer.count("S")
count_of_capital_T = adwentures_of_tom_sawer.count("T")
count_of_capital_U = adwentures_of_tom_sawer.count("U")
count_of_capital_V = adwentures_of_tom_sawer.count("V")
count_of_capital_W = adwentures_of_tom_sawer.count("W")
count_of_capital_X = adwentures_of_tom_sawer.count("X")
count_of_capital_Y = adwentures_of_tom_sawer.count("Y")
count_of_capital_Z = adwentures_of_tom_sawer.count("Z")

# Обчислення суми всіх змінних
total_sum = (
    count_of_capital_A + count_of_capital_B + count_of_capital_C +
    count_of_capital_D + count_of_capital_E + count_of_capital_F +
    count_of_capital_G + count_of_capital_H + count_of_capital_I +
    count_of_capital_J + count_of_capital_K + count_of_capital_L +
    count_of_capital_M + count_of_capital_N + count_of_capital_O +
    count_of_capital_P + count_of_capital_Q + count_of_capital_R +
    count_of_capital_S + count_of_capital_T + count_of_capital_U +
    count_of_capital_V + count_of_capital_W + count_of_capital_X +
    count_of_capital_Y + count_of_capital_Z
)

print(f"Сума всіх слів: {total_sum}")



# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
second_tom_position = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)
print(f"Слово 'Tom' вдруге зустрічається на позиції {second_tom_position}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer = re.split(r'\.\s*', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer[3].lower()
print(adwentures_of_tom_sawer[3])
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts_with_by_the_time = adwentures_of_tom_sawer[0].startswith("By the time")
print (starts_with_by_the_time)
starts_with_by_the_time = adwentures_of_tom_sawer[1].startswith("By the time")
print (starts_with_by_the_time)
starts_with_by_the_time = adwentures_of_tom_sawer[2].startswith("By the time")
print (starts_with_by_the_time)
starts_with_by_the_time = adwentures_of_tom_sawer[3].startswith("By the time")
print (starts_with_by_the_time)
starts_with_by_the_time = adwentures_of_tom_sawer[4].startswith("By the time")
print (starts_with_by_the_time)
#print(f"Чи є речення, яке починається з 'By the time': {starts_with_by_the_time}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
#last_sentence_word_count = len(adwentures_of_tom_sawer[-1])
#print(last_sentence_word_count)
print(adwentures_of_tom_sawer[4])
worlds_in_last_sentence = len(adwentures_of_tom_sawer[4].split())
print(f"Кількість слів в останньому реченні {worlds_in_last_sentence})")

#done

