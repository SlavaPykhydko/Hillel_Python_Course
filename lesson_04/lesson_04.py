
list_1 = list('Hello World !')
print(list_1)

list_2 = [i for i in 'Hello World !' if i !=' ' and i !=',' and i !='!']
print(list_2)

list_3 = [i for i in 'Hello World !' if i not in [' ', ',','!']]
print(list_3)

symbols = [' ', ',','!']
list_4 = [i for i in 'Hello World !' if i not in symbols]
print(list_4)

symbols = [' ', ',','!']
list_5 = [i.lower() for i in 'Hello World !' if i not in symbols]
print(list_5)

list_6 = list(range(1,11))
del list_6[2]

last_el = list_6.pop()
print(list_6)
print(last_el)


list_7 = list('Hello, World !')
print(list_7[2:5])
print(list_7[::2])
print(list_7[::-1]) #перевернутий ліст



list_8 = list('Hello, World !')
for index, element in enumerate(list_8):
    print(f'{index} - {element}')

if 'e' in list_8:
    list_8.remove('e')
    print(list_8)