#Concession stand program

menu = { "pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "momo" : 5.00,
        "chips" : 2.50,
        "coke" : 2.00 }

cart = []
total = 0
print("------ MENU ------")
for key, value in menu.items():
    
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: {total:.2f}")