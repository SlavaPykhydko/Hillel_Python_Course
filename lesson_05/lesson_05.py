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