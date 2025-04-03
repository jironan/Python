from script1 import *
print(__name__)

def fav_drink(drink):
    print(f"Your fav drink is {drink}")

print("This is script 2")

fav_drink("coffee")
favourite_food("Momo")
print("Good bye!")

if __name__ == '__main__':
    main()