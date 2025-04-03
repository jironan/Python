import random

value = ("rock", "paper", "scissor")
running = True

while running:
    computer = random.choice(value)

    
    print("-------- Welcome to rock paper scissor -------")
    player= input("Enter rock, paper or scissor: ").lower()

    while player not in value:
        print("Invalid options")
        player= input("Enter rock, paper or scissor: ").lower()

    print(f"Computer: {computer}")
    print(f"Player: {player}")



    if computer == player:
                print("It's is tie")
    elif computer == "rock" and player == "paper":
                print("You win")
    elif computer == "paper" and player == "scissor":
                print("You win")
    elif computer == "scissor" and player == "rock":
                print("You win")
    else: 
                print ("You lose")
    cont = input("Do you still want to play: (y/n): ").lower()

    if not cont == "y":
      running = False
print("Thank you!")
 
     

    








