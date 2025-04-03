#Iterable: An object/collection that can return its element
#          one at a time, allowing it to iterated over in a loop

numbers = [1,2,3,4,5]

for number in reversed(numbers):
    print(number, end="-")
print()

#Tuples are also iterable

fruits = { "apple", "orange", "coconut"}

for fruit in fruits:
    print(fruit)

name="Foxie"
for character in name:
    print(character)


my_dictionary = {"A":1,"B":2,"C":3}
for key,value in my_dictionary.items():
 print(f"{key} : {value}")