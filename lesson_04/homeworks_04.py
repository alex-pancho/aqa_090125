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
print (adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print (adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ").replace("  ", " ")
print (adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

count_h = adwentures_of_tom_sawer.count("h")
print(f'The letter "h" appears {count_h} times in the text.')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

start_with_capital_word_count = sum(word.istitle() for word in adwentures_of_tom_sawer.split())
print(f'{start_with_capital_word_count} words in the text begin with a capital letter.')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

second_tom_position = adwentures_of_tom_sawer.find("Tom", +1)
print(f'The word Tom occurs a second time at position {second_tom_position}.')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

# adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace(". ", ".")
adwentures_of_tom_sawer_sentences = list(adwentures_of_tom_sawer.split('. '))
adwentures_of_tom_sawer_sentences [-1] = adwentures_of_tom_sawer_sentences[-1].rstrip(".")
print (adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

adwentures_of_tom_sawer_sentence_4 = adwentures_of_tom_sawer_sentences[3].lower()
print (adwentures_of_tom_sawer_sentence_4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

print(f'Does any sentance starts with "By the time": {any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)}')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentance_words_count = len(adwentures_of_tom_sawer_sentences[-1].split(' '))
print(f'Count of words in the last sentence is {last_sentance_words_count}.')