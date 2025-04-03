""" print("hello") 
print("pizza is really good")
#Variable

#string
first_name="Ronan"
print(first_name)
print(f"Hello {first_name}")

#Integer
age = 21
print(age)
print(f"You are {age}")

#Float
price = 99.99
print(price)
print(f"Price is {price}")

#Boolean
is_worker = True
is_not_Worker = False
if is_worker:
    print(is_worker)
else :
    print(is_not_Worker)"""
#-----------------------------------------------------------------------------------------------------------------------------


#Type casting =  the process of converting a variable from one data type to anorther 
#str(), int(), float(), bool()

#name ="Chelsea"
#position = 4
#fan = 77
#stadium = "Stamford Bridge"
#-----------------------------------------------------------------------------------------------------------------------------


#input() = A function that prompts the user to enter data
#name = input ("What is your favourite team ? :")
#Player = input("Who's your favourite player? :")
#position = input ("Enter your clubs current position? :")
#int(position)

#print(f"My favourite team is {name}. My favourite player is {Player}. My clubs postion is {position}"
#-----------------------------------------------------------------------------------------------------------------------------

#test area of rectangle A=lw

#*/ l = float(input("Enter length of rectangle: "))
#w = float(input("Enter width of rectangle: "))
#a = l*w
#print (f"Area of rectangle is {a} cm ") 

#Arithemetic 
#ADD a+=1 / a=a+1
#Subtract a-=1
#Multiply a*=1
#Div a/=1
#Power a**=2
#Remainderv a %= 2

#x= 6.9
#y= 8
#z =11
#result = round(x)
#result = abs(x) -Absolute value
#result = pow(y , y)
#result = max(x,y,z)
#result = min(x,y,z)

#print(result)

#response = input("Would you like food ? (Y/N): ")
#if response == "Y":
 #print("Have some food")
#else:
  # print("no food for yOU")

#operator = input("Enter an operator (+ - * /):")
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

#if operator == "+":
#print (f"Sum is {num1 + num2}")
#elif operator == "-":
 #print (f"Sub is {num1 - num2}")
#elif operator == "*":
 #print (f"Multiplication is {num1 * num2}")
#elif operator == "/":
  # print(f"Division is {num1 / num2}")
#else:
 # print("Invalid")

#--------------------------------------------------------------------------

#LOGICAL OPERATORES
  #OR > One of the conditions must be true
  #AND > Both conditions must be true
  #NOT > Both conditions must be false

#CONDITIONAL EXPRESSION =A oneline   hortcut for if-else statement (ternary operator)
#fORMULA ==  X if condition else Y

#num=5
#Print("Even" if num% 2 ==0 else  "ODD")

#name = input('Enter your full name: ')
#phone_number = input("Enter phone number:")

#result = len(name)
#result = name.find ("o")
#result = name.rfind("o")
#result = name.capitalize()
#result = name.upper()
#result= name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#result = phone_number.replace("-", " ")
#print (result)

#validate user input excercise
#1.username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

#name = input("Enter your username: ")
#count =  len(name)
#space = name.find(" ")
#characters = name.isalpha()
#print("Validated" if count <=12 and space <= 0 and characters == True else ("Not validated"))

#----------------------------------------------------------------------------------------------------------------
# INDEXING
# accessing elements of a sequence using [] (indexing operator)
#[start : end : step]


#credit_number = "1234-5678-9012-3456"
#print (credit_number[0])
#print (credit_number[0:6])
#print(credit_number[:4])
#print(credit_number[::3])
#print (credit_number[15:])
#---------------------------------------------------------------------------------------------------------

#FORMAT SPECIFIERS
#> {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left specify
# :> = right justify
# :^ = center align
# :+ = use + sign to indicate positive value
# := = place a sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator 

#price1 = 3.1456
#price2 = -9.87
#price3 = 12.67

#print(f"print 1 is ${price1:.<f}")
#print(f"print 2 is ${price2:.>f}")
#print(f"print 3 is ${price3:.^f}")
#--------------------------------------------------------------------------------------------------
\
#WHILE LOOP = use while statement

#age = int(input("Enter your age: "))
#while age<0:
  #  print("Age accounnt be negative")
    #age = int(input("Enter your age: "))
#print(f"your age is {age}")
#-------------------------------------------------------------------------------------------------------------

#PYTHON COMPOUND INTEREST CALCULATOR
"""p= float(input("Enter your principal balance: "))
r =float(input("Enter your interest rate: "))
t = int(input("Enter your time in years: "))
while p <= 0:
    p = float(input("Enter your principal balance: "))
    if p <= 0:
        print("Principle cant be zero. ")
    
while r <= 0:
    r = float(input("Enter your interest rate: "))
    if r <= 0:
        print("Interest cant be zero. ")

while t <= 0:
    t = int(input("Enter your time in years: "))
    if t <= 0:
        print("Time cant be zero. ")
      
A= p * pow(1 + r/100, t)
print(f"Total balance is {A}") """
#------------------------------------------------------------------------------------------
#For loops
#Execute a block of code a fixed number of times
#You can interate over a range, string, sequence, etc

#for  x in reversed(range(1, 11,2)):
 #  range(11, 1)
  
#credit_card = "1234-5678-9012-3456"
#for x in credit_card:
  #print (x)
  #----------------------------------------------------------------------------------------------

"""import time
my_time =int(input("Enter time on seconds: "))
for x in range(my_time, 0, -1):
    seconds = x% 60
    minutes = int (x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print ("Time is up") """

#Nested Loop = A loop inside another loop (outer, inner)
 
#rows = int(input("Enter the number of rows: "))
#columns= int(input("Enter the number of columns: "))
#symbol  = input("Enter a symbol to use: ")

#for x in range(rows):
    #for y in range(columns):
     #   print(symbol, end="") 
    #print()
      
 #-------------------------------------------------------------------------------------
 # collection: singlr "variable" used to store multiple values
 # List = [] ordered and changeable. Duplicates OK
 # Set = {} unordered and immutable, but  ADD/REMOVE OK, NO duplicates
 # Tuple = ()ordered and unchangeable. Duplicates OK. Faster

#fruits = ["apple","orange","banana", "coconut"]
#print(fruits[::3])
#for fruit in fruits:
 #print(fruit[2])
 #print(dir(fruits))
 #print(help(fruits))

#fruits[0] = "pineapple" > To add the value at the start 
#fruits.append("pineapple") > to add value at the end
#fruits.remove("apple") > to remove a value
#fruits.insert(0, "pineapple")
#fruits.reverse()
#fruits.sort()
#fruits.clear()
#print("apple" in fruits )
#print(fruits.index("apple"))
#for fruit in fruits:
    #print(fruit)

    #SET

#fruits = {"apple","orange","banana", "coconut"}
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
#fruits.add("pineapple")
#fruits.remove("apple")#or fruit in fruits:
    #print(fruits)

    #TUPLES

#fruits = ("apple","orange","banana", "coconut")
#print(len(fruits))
#print(fruits.index("apple"))

#SHOPPING CART PROGRAM

#foods = []
#prices = []
#total = 0

#while True:
 #   food = input("Enter a food to buy (q to quit): ")
  #  if food.lower() == "q":
   #     break
    #else:
     #   price = float(input(f"Enter the price of a {food}: $"))
      #  foods.append(food)
       # prices.append(price)

#print("----- Your Cart -----")
#for food in foods:
 #   print(food)

#for price in prices:
 #   total = total + price

#print(f"Your total is ${total}")

#--#fruits = ["apple","orange","banana", "coconut"]
#vegetables = ["celery", "onion", "tomatoes"]
#meats = ["chicken", "fish", "turkey"]

#groceries = [["apple","orange","banana", "coconut"],
           #   ["celery", "onion", "tomatoes"],
            #    ["chicken", "fish", "turkey"]]
#print(fruits)
#print(groceries[2])
#rint(groceries[0][1])

#for collection in groceries:
 #   for food in collection:
  #      print(food, end=" ")
   # print()

#num_pad = ((1, 2, 3),
 #          (4, 5, 6),
  #         (7, 8, 9),
   #        ("*", 0, "#"))

#for row in num_pad:
 #       for num in row:
  #              print (num, end=" ")
   #     print()

#------------------------------------------------------------------------------------
questions= ( "Country without rectangular flag? ",
            "Which animal lays largest eggs? ",
            "What is capital of Canada? " )

options= (("A.Canada", "B.Haiti", "C.Mauritis", "D.Nepal"),
          ("A.Shark", "B.Ostrich", "C.Swan", "D.Goose"),
          ("A.Toronto", "B.Montral", "C.Ottawa", "D.Vancouver"))

answers = ("D", "B", "C")
guesses = []
score = 0
question_num= 0

for question in questions:
  print("---------------^--------------)")
  print (question)
  for option in options[question_num]:
    print(option)
  guess = input ("Enter (A, B, C, D): ")
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("Correct")
  else:
    print("Incorrect")

  question_num += 1
print("-----------------------")
print("       RESULTS !!      ")
print("-----------------------")
print ("answers: ", end=" ") 
for answer in answers:
  print(answer, end=" ")
print()

print ("guesses: ", end=" ")
for guess in guesses:
  print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")