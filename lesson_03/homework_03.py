alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_black_sea = 436_402
square_azov_sea = 37_800
square_total = square_black_sea + square_azov_sea
print(f"Площа Чорного та Азовського моря разом : {square_total} км2\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# store_1 + store_2 + store_3 = 375_291
# store_1 + store_2 = 250_449
# store_2 + store_3 = 222_950
total = 375_291
store_3 = 375_291 - 250_449
store_1 = 375_291 - 222_950
store_2 = 375_291 - (store_1 + store_3)

print(f"На Першому складі товарів : {store_1} \n"
      f"на дургому складі товарів : {store_2} \n"
      f"на третьому складі товарів : {store_3} \n"
      f"Перевірка, всього товарів : {store_1 + store_2 +  store_3} \n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
amount_per_month = 1179
qnt_months = 18
total_amount = amount_per_month * qnt_months
print(f"За 18 міс потрібно буде заплатити : {total_amount} грн\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
print(f"a : {a}")
b = 9907 % 7
print(f"b : {b}")
c = 2789 % 7
print(f"c : {c}")
d = 7248 % 6
print(f"d : {d}")
e = 7128 % 5
print(f"e : {e}")
f = 19224 % 9
print(f"f : {f}\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274
pizza_medium = 218
juice = 35
cake = 350
water = 21

total_sum = pizza_big*4 + pizza_medium*2 + juice*4 + cake + water*3
print(f"Для даного її замовлення знадобиться : {total_sum} грн\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo_amount = 232
max_qnt_per_one_page = 8
qnt_pages = total_photo_amount / max_qnt_per_one_page
print(f"Щоб вклеїти всі фото знадобиться : {qnt_pages} сторінок\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
qnt_gas_per_one_hundred_km = 9
tank_volume = 48
total_gas_amount = ( distance / 100 ) * qnt_gas_per_one_hundred_km
total_qnt_stops = total_gas_amount / tank_volume

print(f"Для такої подорожі знадобиться : {total_gas_amount} л бензину")
print(f"Щонайменше родині потрібно заправитися : {total_qnt_stops} рази")