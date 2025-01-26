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

task_01 = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""

task_02 = task_01.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

task_03 = " ".join(task_02.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(task_03.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

task_05 = task_03.split()
count = 0
for word in task_05:
    if word.istitle():
        count += 1
print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_Tom = task_03.find("Tom")
task_05 = task_03.find("Tom", first_Tom+1)
print(task_05)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = task_03.split(". ")
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
task_08 = adwentures_of_tom_sawer_sentences[3].lower()
print(task_08)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for task_09 in adwentures_of_tom_sawer_sentences:
    if task_09.startswith("By the time"):
        print("This sentence starts with 'By the time' - ", task_09)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

task_10 = adwentures_of_tom_sawer_sentences[-1].split()
print(len(task_10))