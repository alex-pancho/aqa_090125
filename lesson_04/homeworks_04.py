adwentures_of_tom_sawer = """
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


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# Розділили текст на частини на основі роздільника "пробіл" та повернули список отриманих частин (слів).
words = adwentures_of_tom_sawer.split()
# Об'єднали слова зі списку за допомогою роздільника ' '.
adwentures_of_tom_sawer = ' '.join(words)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# Розділили текст на частини на основі роздільника "h" та повернули список отриманих частин.
new_adwentures_of_tom_sawer4 = adwentures_of_tom_sawer.split('h')
# Порахували кількість отриманих частин та відняли "1" для розуміння скількі разів у тексті зустрічається літера "h"
count_strings = len(new_adwentures_of_tom_sawer4) - 1
# Вивід результату
print(f'У тексті зустрічається літера "h" {count_strings} раз.')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# Лічильнику слів з великої букви даємо значення "0"
count = 0
# Перевіряємо всі слова зі списку
for word in words:
    # По умові, що слово у тексті починається з Великої літери
    if word.istitle():
        # Якщо так, додаємо "1"
        count = count + 1
# Вивід результату        
print(f'У тексті з Великої літери починається {count} слів.')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# Індекс першого слова "Tom"
index_1 = adwentures_of_tom_sawer.find("Tom")
# Індекс другого слова "Tom"
index_2 = adwentures_of_tom_sawer.find("Tom", index_1 + 1)
# Вивід результату
print(f'Слово Tom зустрічається вдруге на позиції з індексом {index_2}.')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())



# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False
# Перевірка кожного речення
for sentence in adwentures_of_tom_sawer_sentences:
    # на умову чи починається якесь речення з "By the time"
    if sentence.startswith("By the time"):
        found = True
# Вивід результатів відповідно до умови       
if found == True:
    print('Found "By the time" on the start of the sentence')
else: 
    print('Not found "By the time" on the start of the sentence')
    
# 
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
# Розбиваємо останнє речення на основі роздільника " "
last_sentence_words = adwentures_of_tom_sawer_sentences[-1].split()
# Рахуємо кількість слів останнього речення
count = len(last_sentence_words)
# Вивід результатів 
print(f'Кількість слів останнього речення з adwentures_of_tom_sawer_sentences: {count}')
