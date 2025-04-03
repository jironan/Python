#function = A block of reusable code
#            place() after the function name

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old")
    print("Happy birthday to you")



happy_birthday("Steve",20)

# return: function used to return arguments
#         and send results back to caller

def add(x,y):
    z=x+y
    return z

def sub(x,y):
    z= x - y
    return z

def mul(x,y):
    z = x * y
    return z

print (add(1,2))
print (mul(1,2))
print (mul(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name =create_name("Steve", "Jobbs")
print(full_name)