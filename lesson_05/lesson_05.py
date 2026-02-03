from operator import indexOf

list_1 = [1, -2, 3, -5, 6, 8, 9 , 23]

list_2 = [ l * -1 for l in list_1]
print(list_2)

list_3 = [2, 4, 5, 6, -20, -10, -13]
list_4 = [l for l in list_3 if l > 0]
sum = 0
for l in list_3:
    if l < 0:
        sum += l

print(len(list_4))
print(sum)
list_5 = list()
list_5.append(len(list_4))
list_5.append(sum)
print(list_5)

list_6 = [l for l in list_1 if list_1.index(l) %2 == 0]
print(f" list_6 = {list_6}")

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"d": 4, "e": 5, "f": 6}
# dict_3 = {**dict_1, **dict_2}
dict_3 = {}
dict_3.update(dict_1)
dict_3.update(dict_2)
print(dict_3)

dict_4 = {"a": 1, "b": 2, "c": 3}
dict_5 = {"d": 4, "e": 5, "f": 6}
# dict_4 = dict_4 | dict_5
dict_4 |= dict_5
print(f"{dict_4= }")

lst = ['a', 'b', 'a', 'c', 'a']

indices = [i for i, v in enumerate(lst) if v == 'a']
print(indices)

products = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

new_dict = {}
for title, price in products.items():
    new_dict[title] = price
print(new_dict)

new_dict_2 = {title: '%.2f' % (price * 1.1) for title, price in products.items() if price > 1}
print(new_dict_2)

dict_6 = {n: n*n for n in range(1,6)}
print(dict_6)

sum_1=0
dict_7 = {'data_1': 100, 'data_2': -54, 'data_3': 247}
for k, v in dict_7.items():
    sum_1 += v
print(f"sum_1 = {sum_1}")

dict_8 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_8 = ['x', 'y', 'b', 'd', 'e']
dict_8 = {k: v for k, v in dict_8.items() if k not in list_8}
print(dict_8)

dict_9 = {'n': 1, 'k': 2, 'c': 3, 'a': 4}
# sorted_dict_9 = {k:v for k, v in dict_9.items() if v > 0}
sorted_dict_9 = dict(sorted(dict_9.items(), key=lambda item: item[0]))
print(sorted_dict_9)


dict_10 = {'a': 1, 'b': 20, 'c': 3, 'd': 5, 'e': 134, 'k': 40, 'm': -8}

min2= min(dict_10.values())
max2 = max(dict_10.values())
print(type(dict_10.values()))
print(min2)
print(max2)

min3 = max3 = i = 0
for el in dict_10.values():
    if i == 0:
        min3 = el
        i += 1
        continue
    if max3 < el:
        max3 = el
    if min3 > el:
        min3 = el
print(f'max3 = {max3}')
print(f'min3 = {min3}')

a = 1
b = 2
# temp = a
# a = b
# b = temp
(a , b) = (b, a)
print(f'{a=}, {b=}')

set_1 = {1, 2, 3}
set_1.update({'3434', '345', 'rdfv'})
set_1.update(['dfd','mss'])
print(set_1)

a = 1
b = 3
c =4
t1 = (a, b, c)
l1 = [a, b, c]
l1[0]=8
print(t1)
print(l1)

set_3 = {'a', 'b', 'c', 'd', 'e'}
set_4 = {'a', 'k', 'c', 'l', 'n'}
set_res = set_3.intersection(set_4)
print(f'set_res = {set_res}')
set_res_2 = {el for el in set_3 if el in set_4}
print(f'set_res_2 = {set_res_2}')

# set_res_3 = set_3 - set_4
# set_res_4 = set_4 - set_3

set_res_3 = set_3.difference(set_4)
set_res_4 = set_4.difference(set_3)
print(f'set_res_3 = {set_res_3}')
print(f'set_res_4 = {set_res_4}')

l_2 = [1, 3, 4, 5, 5, 7, 2, 3, 4, 8]
l_res = []
[l_res.append(el) for el in l_2 if el not in l_res]
print(f'l_res = {l_res}')
