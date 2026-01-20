# here will be some study staff from online lesson

# some new changes in order to test GitHub Desktop

tasks_1 = ("study", "work", "walk")
tasks_2 = ("work", "study" , "walk")

print(tasks_1.__eq__(tasks_2))

# if "walk" in tasks:
#     print("Time for a walk!")


tasks_3 = [ "work", "study", "walk"]
tasks_4 = ["study", "work", "walk"]

print(tasks_3.__eq__(tasks_4))

fruits_1 = {"apple", "banana", "cherry"}
fruits_2 = {"apple", "cherry", "banana"}
print(fruits_1.__eq__(fruits_2)) # поверне True, тому що set