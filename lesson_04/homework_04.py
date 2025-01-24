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
adwentures_of_tom_sawer  = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

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
count_h = adwentures_of_tom_sawer.count("h")
print(f"У тексті літера \"h\" зустрічається {count_h} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_upper_words = len(list(filter(str.isupper, adwentures_of_tom_sawer)))
print(f"В тексті {count_upper_words} слів, які починаються з великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom_index = adwentures_of_tom_sawer.find("Tom")
second_tom_index = adwentures_of_tom_sawer.find("Tom", first_tom_index+1)
print(f"Позиція, на якій слово Tom зустрічається вдруге: {second_tom_index}")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace(". ", ".")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_sentences.split(".")
adwentures_of_tom_sawer_sentences = list(filter(None, adwentures_of_tom_sawer_sentences))
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_lower = fourth_sentence.lower()
print(f"Четверте речення, яке написано в нижньому регістрі: {fourth_sentence_lower}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
start_with_by_the_time = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
if start_with_by_the_time is True:
    print(f"Так, в тексті є речення, яке починається з \"By the time\"")
else:
    print(f"Ні, в тексті немає речення, яке починається з \"By the time\"")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = len(last_sentence.split( ))
print(f"В останньому реченні {words_in_last_sentence} слова")

