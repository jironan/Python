#Membership operator = used to test a value or variable is found in a sequence
#                    (string, list, tuple, set, or dictionary)
#                    1.in
#                    2.not in

word="APPLE"

letter = input("Guess a letter in secret word: ").upper()

if letter  in word:
    print(f"There is a {letter}.")
else:
        print(f" {letter} was not found.")


#----------------------------------------

if letter  not in word:
    print(f" {letter} was not found.")
    
else:
        print(f"There is a {letter}.")

students ={"spongebob", "Patrick", "Sandy"}

student = input("Enter name of student: ").lower

grades ={"Sandy": "A", 
         "Ram": "B", 
         "Shyam": "A"}

student = input("Enter the name of student: ")

if student in grades:
      print(f"{student}'s grade is {grades[student]}")
else:
      print("Student not found")


email= "abc@gmail.com"
if "@" in email and "." in email:
      print(f"{email} is valid email")
else:
      print("Is not a valid email")