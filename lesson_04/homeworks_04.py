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
print(f"Replace the end of paragraph with a space: {adwentures_of_tom_sawer}")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"Replace '....' with a space: {adwentures_of_tom_sawer}")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f"Make one space between words: {adwentures_of_tom_sawer}")


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_word_count = adwentures_of_tom_sawer.count("h")
print(f"Count of 'h' in the text: {h_word_count}")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
titles_count = len([i for i in adwentures_of_tom_sawer.split() if i.istitle()])
print(f"Number of words starting with a capital letter {titles_count=}")

# second variant
count = 0
for i in adwentures_of_tom_sawer.split():
    if i.istitle():
        count += 1
print(f"Number of words starting with a capital letter: {count=}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
start_index = adwentures_of_tom_sawer.find("Tom")
tom_index = adwentures_of_tom_sawer.find("Tom", start_index + 1)
print(f"Second 'Tom' position is: {tom_index}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(f"Split the text into separate sentences: {adwentures_of_tom_sawer_sentences}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence_lower = adwentures_of_tom_sawer_sentences[3].lower()
print(f"{fourth_sentence_lower=}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
is_sentence_start_from_by_the_time = any(i.startswith("By the time") for i in adwentures_of_tom_sawer_sentences)
print(f"{is_sentence_start_from_by_the_time=}")

# variant 2
is_by_the_time = False
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        is_by_the_time = True
print(f"{is_by_the_time=}")

# variant 3
count = 0
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        count += 1
print(f"Is 'By that time' in the beginning of the sentences: {is_by_the_time > 0}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
word_count_last_sentence = len(adwentures_of_tom_sawer_sentences[-1].split())
print(f"{word_count_last_sentence=}")
