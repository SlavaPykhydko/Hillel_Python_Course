# Solution #1
i = 1

while i:
    str = input("Enter a word which consist char h or H: ")
    if str.count("h") >= 1 or str.count("H") >= 1:
        print("The word contains 'h' or 'H'. Exiting the loop.")
        i = 0

# Solution #2
while True:
    str_2 = input("Enter a word which consist char h or H: ")
    if "h" in str_2.lower():
        print("The word contains 'h'. Exiting the loop.")
        break

