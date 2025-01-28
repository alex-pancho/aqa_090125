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

adwentures_of_tom_sawer_1 = adwentures_of_tom_sawer.replace("\n", " ")
print("Changed text aftre compleaton of task 1 :", adwentures_of_tom_sawer_1, sep= '\n')



# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_2 = adwentures_of_tom_sawer_1.replace("....", " ")
print("Changed text aftre compleaton of task 2 :", adwentures_of_tom_sawer_2, sep= '\n')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_3 = adwentures_of_tom_sawer_2.replace("   ", " ").replace("  ", " ")
print("Changed text aftre compleaton of task 3 :", adwentures_of_tom_sawer_3, sep= '\n')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adwentures_of_tom_sawer_4 = adwentures_of_tom_sawer_3
h_letter_count = adwentures_of_tom_sawer_4.count("h")
print("Total ammount of \"h\" letter in the text :", h_letter_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capital_letter_count = (
    adwentures_of_tom_sawer_4.count("A")+ 
    adwentures_of_tom_sawer_4.count("B")+ 
    adwentures_of_tom_sawer_4.count("C")+ 
    adwentures_of_tom_sawer_4.count("D")+ 
    adwentures_of_tom_sawer_4.count("E")+ 
    adwentures_of_tom_sawer_4.count("F")+ 
    adwentures_of_tom_sawer_4.count("G")+ 
    adwentures_of_tom_sawer_4.count("H")+ 
    adwentures_of_tom_sawer_4.count("I")+ 
    adwentures_of_tom_sawer_4.count("J")+ 
    adwentures_of_tom_sawer_4.count("K")+ 
    adwentures_of_tom_sawer_4.count("L")+ 
    adwentures_of_tom_sawer_4.count("M")+ 
    adwentures_of_tom_sawer_4.count("N")+ 
    adwentures_of_tom_sawer_4.count("O")+ 
    adwentures_of_tom_sawer_4.count("P")+ 
    adwentures_of_tom_sawer_4.count("Q")+ 
    adwentures_of_tom_sawer_4.count("R")+ 
    adwentures_of_tom_sawer_4.count("S")+ 
    adwentures_of_tom_sawer_4.count("T")+ 
    adwentures_of_tom_sawer_4.count("U")+ 
    adwentures_of_tom_sawer_4.count("V")+ 
    adwentures_of_tom_sawer_4.count("W")+ 
    adwentures_of_tom_sawer_4.count("X")+ 
    adwentures_of_tom_sawer_4.count("Y")+ 
    adwentures_of_tom_sawer_4.count("Z")
)
print("Total ammount of words started with capital letter in the text :", capital_letter_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
second_word_tom = adwentures_of_tom_sawer_3.find("Tom", 1)
print(f"Word \"Tom\" second time occurs in position: {second_word_tom} in the text." )

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_3.split('.')
print(f"Text splited dy sentance: {adwentures_of_tom_sawer_sentences}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence_lowercase = adwentures_of_tom_sawer_sentences[3].lower()
print(f"The Fourth sentence in the lower case : {fourth_sentence_lowercase}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
is_sentence_start_from_by_the_time = any(adwentures_of_tom_sawer_sentences.strip().startswith('By the time')
                                     for adwentures_of_tom_sawer_sentences in adwentures_of_tom_sawer_sentences)
print("Does any of sentence started from \"By the time\" : " , is_sentence_start_from_by_the_time)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
words_count_last_sentence = len(adwentures_of_tom_sawer_sentences[-2])
print(F"Last sentence contains {words_count_last_sentence} words.")