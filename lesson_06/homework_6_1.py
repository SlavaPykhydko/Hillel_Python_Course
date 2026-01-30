
str = input("Enter some sentence: ")
list_1 = list(str)

# Solution #1
unique_chars_part_1 = [i for i in list_1 if list_1.count(i) == 1]
unique_chars_part_2 = [i for i in list_1 if list_1.count(i) > 1]
set_from_unique_chars_part_2 = set(unique_chars_part_2)
list_2_from_set = list(set_from_unique_chars_part_2)
print(f"unique_chars_part_1 = {unique_chars_part_1}")
print(f"unique_chars_part_2 = {unique_chars_part_2}")
print(f"list_2_from_set = {list_2_from_set}")
unique_chars_part_1.extend(list_2_from_set)
print(f"unique_chars_part_1 = {unique_chars_part_1}")
count = len(unique_chars_part_1)
print(f"count = {count}")

#Solution #2
set_1 = set(list_1)
print(f"set_1 = {set_1}")
count_unique_charts_from_set_1 = len(set_1)
print(f"count_unique_charts_from_set_1 = {count_unique_charts_from_set_1}")

