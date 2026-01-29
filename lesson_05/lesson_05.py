list_1 = [1, -2, 3, -5, 6]

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