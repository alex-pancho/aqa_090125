from operator import index

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
print("\n", "task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Якщо у тексті замінити кінець абзацу на пробіл, вийде: " + adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("\n", "task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print("Якщо у тексті замінити .... на пробіл, вийде: " + adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("\n", "task 03")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print("Якщо зробити так, щоб у тексті не було більше одного пробілу, вийде: " + adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("\n", "task 04")
count_h = adwentures_of_tom_sawer.count("h")
print(f"Літера h зустрічається у тексті {count_h} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("\n", "task 05")
split_adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
k=0
for slovo in split_adwentures_of_tom_sawer:
    if slovo.istitle():
        k=k+1
print("Слів, що починаються з великої літери у тексті ",k)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("\n", "task 06")
tomPosition = adwentures_of_tom_sawer.find("Tom",2)
print("Позиція, на якій слово Tom зустрічається вдруге: ", tomPosition)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("\n", "task 07")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print("Змінна adwentures_of_tom_sawer розділена по кінцю речення: ", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("\n", "task 08")
positionFour = adwentures_of_tom_sawer_sentences[3]
lowerPositionFour = positionFour.lower()
print("Четверте речення з adwentures_of_tom_sawer_sentences: ",positionFour)
print("Четверте значення у нижньому регістрі: ", lowerPositionFour)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("\n", "task 09")
#for start in adwentures_of_tom_sawer_sentences:
#    if start.startswith("By the time"):
#        print("true")
#    else:
#        print("false")
k=0
for start in adwentures_of_tom_sawer_sentences:
    if start.startswith("By the time"):
        k=k+1
print("Кількість pечень, що починаються з ""By the time"": ",k)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\n", "task 10")
lastSentens = len(adwentures_of_tom_sawer_sentences[-1].split(" "))
print("Кількість слів останнього речення з adwentures_of_tom_sawer_sentences: ",lastSentens)
