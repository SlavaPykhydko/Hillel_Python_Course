# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_new_function(num1 , num2):
    return num1 + num2

res_1 = sum_new_function(5, 2)
print(res_1)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
list_1 = [1, 4, 3, 5, 7, 45, 22]

def avg_from_list(lst):
    return round(sum(lst) / len(lst), 2)

print(avg_from_list(list_1))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(str):
    return str[::-1]

str_1 = "Hello, world!"
print(reverse_string(str_1))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

word_list = ["apple", "banana123", "cherry000001"]

def the_longest_word(lst):
    return max(lst, key=len)
print(the_longest_word(word_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        # index = str1.find(str2,0) # можна і через find
        index = str1.index(str2)
        return index
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# from task 6_3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def filter_list(lst, data_type):
    if data_type == int:
        return [i for i in lst if isinstance(i, data_type) and not isinstance(i, bool)]
    return [i for i in lst if isinstance(i, data_type)]

print(filter_list(lst1, int))

# from task 6_4
list2 = [12, 3, 1, 44, 54, 55, 565, 43, 44]

sum1 =0
def sum_even_digits(lst):
    global sum1
    for i in lst:
        if i % 2 == 0:
            sum1 += i
    return sum1

print(sum_even_digits(list2))

# from task 6_1
str3 = input("Enter some sentence: ")
list_1 = list(str3)

def count_unique_symbols(lst):
    set_1 = set(lst)
    return len(set_1)

print(count_unique_symbols(list_1))

# from task #6_2
def enter_word_with_particular_letter(letter):
    while True:
        str_2 = input(f"Enter a word which consist char {letter} or {letter.capitalize()}: ")
        if letter in str_2.lower():
            print(f"The word contains {letter}. Exiting the loop.")
            break

enter_word_with_particular_letter("h")
