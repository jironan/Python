#Hangman in python
import random
from Wordslist  import words

#Dictionary of key:()
hangman_art={
    0: ("   ", #tupple
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "   "),
    4: (" O ",
        "/|\\ ",
        "   "),
    5: (" O ",
        "/|\\ ",
        "/  "),
    6: (" O ",
        "/|\\ ",
        "/ \\"),
     
}



def display_main(wrong_guesses):
    print("---------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("---------------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_main(wrong_guesses)
        display_hint(hint)
        guess = input("Enter you guessed letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("***Invalid input***")
            continue

        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
            
        guessed_letter.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess 
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_main(wrong_guesses)
            display_answer(answer)
            print( "YOU WINN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_main(wrong_guesses)
            display_answer(answer)
            print( "YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()