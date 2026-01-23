import re

adventures_of_tom_sawer = """
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
new_part_1 = adventures_of_tom_sawer.replace("\n", " ")
print(new_part_1)
print(" = " * 20)

# task 02 ==
""" Замініть .... на пробіл
"""
new_part_2 = new_part_1.replace("....", " ")
print(new_part_2)
print(" = " * 20)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
new_part_3 = re.sub("\s+", " ", new_part_2 ).strip()
print(new_part_3)
print(" = " * 20)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
qnt_h = new_part_3.count("h")
print(qnt_h)
print(" = " * 20)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_with_upper_first_letter = []
list_with_lower_first_letter = []
qnt_upper_first_two_letters = 0

separate_words = new_part_3.split()

for word in separate_words:
    first_two_letters = word[:2]
    if any( letter.isupper() for letter in first_two_letters ):
        list_with_upper_first_letter.append(word)
    else:
        list_with_lower_first_letter.append(word)
print(f"list_with_upper_first_letter :\n  {list_with_upper_first_letter}")
print(f"list_with_lower_first_letter :\n  {list_with_lower_first_letter}")

qnt_upper_first_two_letters = len(list_with_upper_first_letter)
print(f"слів у тексті починається з Великої літери : {qnt_upper_first_two_letters}")
print(" = " * 20)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
word = "Tom"
n = 2

index = -1
start = 0

for _ in range(n):
    index = new_part_3.find(word,start)
    if index == -1:
        break
    start = index + 1

print(f"слово Tom зустрічається вдруге на позициї =: {index}")



# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#adventures_of_tom_sawer_sentences = [s.strip() for s in new_part_3.split(".") if s.strip()]
adventures_of_tom_sawer_sentences = []
for s in new_part_3.split("."):
    if s.strip():
        adventures_of_tom_sawer_sentences.append(s.strip())
print(f"adventures_of_tom_sawer_sentences -->\n {adventures_of_tom_sawer_sentences}")
print(" = " * 20)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
third_sentence = adventures_of_tom_sawer_sentences[3].lower()
print(third_sentence)
print(" = " * 20)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
word_2 = "By the time"
qnt_symbols = 0

for part in adventures_of_tom_sawer_sentences:
    if part[:12].strip() == word_2:
        print(part)
    else:
        print(f"There is no sentence with {word_2}")
print(" = " * 20)




# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adventures_of_tom_sawer_sentences[-1]
print(f"last_sentence : \n {last_sentence}")
words = last_sentence.split()
qnt_f_words = len(words)
print(f"кількість слів останнього речення з adventures_of_tom_sawer_sentences  -- {qnt_f_words}")
