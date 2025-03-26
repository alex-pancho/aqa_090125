adwentures_of_tom_sawer = ("""
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
rolling in wealth.""")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
import re
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)


# task 04
h_count = adwentures_of_tom_sawer.count('h')
print("Occurrences of 'h':", h_count)


# task 05
capital_words = sum(1 for word in adwentures_of_tom_sawer.split() if word.istitle())
print("Words starting with capital letter:", capital_words)



# task 06
first_tom_index = adwentures_of_tom_sawer.find('Tom')
second_tom_index = adwentures_of_tom_sawer.find('Tom', first_tom_index + 1)
print("Second occurrence of 'Tom':", second_tom_index)


# task 07
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
adwentures_of_tom_sawer_sentences = None

# task 08
if len(adwentures_of_tom_sawer_sentences) >= 4:
    print("Fourth sentence (lowercase):", adwentures_of_tom_sawer_sentences[3].lower())



# task 09
starts_with_phrase = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print("Does any sentence start with 'By the time'?:", starts_with_phrase)


# task 10
last_sentence_word_count = len(adwentures_of_tom_sawer_sentences[-1].split())
print("Number of words in the last sentence:", last_sentence_word_count)

