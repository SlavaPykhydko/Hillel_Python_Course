from importlib.resources import read_text

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3, 4, 5, 6]

def get_double(x):
    return x * 2

# list_1 = list(map(get_double, list_1))
# print(list_1)

list_1 = list(map(lambda x: x * 2, list_1))
print(list_1)

def get_even(x: int) -> bool:
    return x % 2 == 0

# list_2 = list(filter(get_even, list_2))
# print(list_2)

list_2 = list(filter(lambda x: x % 2 ==0, list_2))
print(list_2)

list_num = [1, 2, 3]
list_str = ['one', 'two', 'three']

res_dict = dict(zip(list_str, list_num ))
res_list = list(zip(list_str, list_num ))
print(res_dict)

a, b = zip(*res_list)
print(a)
print(b)

d = list(zip(*res_dict.items()))
print(d)

list_3 = ['peter', 'slava', 'anya']
tuple_3 = ('maks', 'jenifer', 'igor')

# list_res_1 = [i.capitalize() for i in list_3]
# print(list_res_1)
#
# tuple_res_1 = tuple(i.capitalize() for i in tuple_3)
# print(tuple_res_1)

# list_res_2 = list(map(lambda x: x.capitalize(), list_3))
# print(list_res_2)
# tuple_res_2 = tuple(map(lambda x: x.capitalize(), tuple_3))
# print(tuple_res_2)

def cap_first_letter(letter: str) -> str:
    return letter.capitalize()

def set_cap_first_letter(lst, tpl=False):
    if tpl:
        return tuple(el.capitalize() for el in lst)
    return [el.capitalize() for el in lst]

list_res_4 = set_cap_first_letter(list_3)
print(f'list_res_4 = {list_res_4}')
tuple_res_4 = set_cap_first_letter(tuple_3, tpl=True)
print(f'tuple_res_4 = {tuple_res_4}')


list_res_3 = list(map(cap_first_letter, list_3))
print(list_res_3)
tuple_res_3 = tuple(map(cap_first_letter, tuple_3))
print(tuple_res_3)

cities = [
    ['Mexico', 8_800_123],
    ['Paris', 6_300_234],
    ['Tokio', 37_032_100],
    ['Kyiv', 5_432_323],
    ['Kharkiv', 2_432_000]
]

def cities_filter(population_count : int, city_list: list) -> bool:
    if population_count < city_list[1]:
        return True
    else:
        return False


filtered_cities_1 = list(filter(lambda city: cities_filter(3_000_000, city), cities))
print(filtered_cities_1)

filtered_cities_2 = list(city for city in cities if city[1] > 3_000_000)
print(filtered_cities_2)

filtered_cities_3 = list(filter(lambda city: city[1] > 3_000_000, cities))
print(filtered_cities_3)

filtered_cities_4 = []
for city in cities:
    if city[1] > 3_000_000:
        filtered_cities_4.append(city)
print(filtered_cities_4)

def filter_cities_2(lst, population_count):
    return list(el for el in lst if el[1] > population_count)

filtered_cities_5 = filter_cities_2(cities, 3_000_000)
print(filtered_cities_5)
