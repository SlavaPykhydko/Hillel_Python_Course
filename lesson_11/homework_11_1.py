l1 = ['1,2,3,4', '1,2,3,4,50,e', 'qwerty1,2,3', '1,2,7,10']

l2 = []
error_count = 0
ordinal_list_item = -1

for i in l1:
    total = 0
    ordinal_list_item += 1
    numbers = i.split(',')
    for num in numbers:
        try:
            total += int(num)
        except ValueError:
            error_count += 1
            print(f'В масиві присутній символ який не може бути числом, '
                  f'тому він буде пропущеним і не буде брати участі в утворенні суми ')
            print(f'порядковий номер в списку l1 = {ordinal_list_item}')
    l2.append(total)
print(f'error_count = {error_count}')
print(l2)