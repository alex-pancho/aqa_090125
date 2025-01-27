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
print("task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
print("______________________________________________________________________________________")
# task 02 ==
""" Замініть .... на пробіл
"""
print("task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
print("______________________________________________________________________________________")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("task 03")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)
print("______________________________________________________________________________________")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("task 04\n"
      "Виведіть, скількі разів у тексті зустрічається літера 'h'.")
count_h = adwentures_of_tom_sawer.count("h")
print(f"Відповідь: {count_h} разів зустрічається літера 'h' у тексті.")
print("______________________________________________________________________________________")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("task 05\n"
        "Виведіть, скільки слів у тексті починається з Великої літери?")
count_ABC = adwentures_of_tom_sawer.count("A")+adwentures_of_tom_sawer.count("B")+adwentures_of_tom_sawer.count("C")
count_DEF = adwentures_of_tom_sawer.count("D")+adwentures_of_tom_sawer.count("E")+adwentures_of_tom_sawer.count("F")
count_GHI = adwentures_of_tom_sawer.count("G")+adwentures_of_tom_sawer.count("H")+adwentures_of_tom_sawer.count("I")
count_JKL = adwentures_of_tom_sawer.count("J")+adwentures_of_tom_sawer.count("K")+adwentures_of_tom_sawer.count("L")
count_MNO = adwentures_of_tom_sawer.count("M")+adwentures_of_tom_sawer.count("N")+adwentures_of_tom_sawer.count("O")
count_PQR = adwentures_of_tom_sawer.count("P")+adwentures_of_tom_sawer.count("Q")+adwentures_of_tom_sawer.count("R")
count_STU = adwentures_of_tom_sawer.count("S")+adwentures_of_tom_sawer.count("T")+adwentures_of_tom_sawer.count("U")
count_VWX = adwentures_of_tom_sawer.count("V")+adwentures_of_tom_sawer.count("W")+adwentures_of_tom_sawer.count("X")
count_YZ = adwentures_of_tom_sawer.count("Y")+adwentures_of_tom_sawer.count("Z")
all_upper = count_ABC+count_DEF+count_GHI+count_JKL+count_MNO+count_PQR+count_STU+count_VWX+count_YZ
print(f"Відповідь: {all_upper} слів у тексті починається з Великої літери.")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("task 06\n"
        "Виведіть позицію, на якій слово Tom зустрічається вдруге.")
position = adwentures_of_tom_sawer.find("Tom")
position = adwentures_of_tom_sawer.find("Tom", position+1)
print(f"Відповідь: {position} позиція, на якій слово Tom зустрічається вдруге.")
print("______________________________________________________________________________________")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
print("task 07\n"
        "Розділіть змінну adwentures_of_tom_sawer по кінцю речення.")  
print("Variant 1 Split by .")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences) 
print("Variant 2    In case if we will split by ;!. and use regular expression.")
import re
adwentures_of_tom_sawer_sentences = re.split(r"[.;!]", adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)
print("______________________________________________________________________________________")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("task 08\n"
        "Виведіть четверте речення з adwentures_of_tom_sawer_sentences."
        "Перетворіть рядок у нижній регістр.")
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)
print("______________________________________________________________________________________")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("task 09\n"
        "Перевірте чи починається якесь речення з 'By the time'.")
check_sentence = bool(adwentures_of_tom_sawer.find("By the time"))
print(f"Відповід: {check_sentence}")
print("______________________________________________________________________________________")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("task 10\n"
        "Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.")
last_sentence = adwentures_of_tom_sawer_sentences[-2]
last_sentence = last_sentence.split()
print(f"Відповідь: {len(last_sentence)} слів у останньому реченні.")


