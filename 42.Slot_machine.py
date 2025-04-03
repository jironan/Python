import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # Fixed index error
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0

def main():
    balance = 100
    print("---------------------------")
    print(" Welcome to Python Slots ")
    print(" Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("---------------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")
        try:
            bet = int(input("Enter your bet amount: "))
        except (ValueError, OSError):
            print("Invalid input. Please enter a valid number.")
            continue
        
        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        print("Spinning.......")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost this bet")
        
        balance += payout
    
    print(f"Your final balance is ${balance}")

if __name__ == '__main__':
    main()