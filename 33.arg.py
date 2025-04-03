#*arg = allows you multiple non-key arguments
#**kwargs = allows you to pass multiple keyword arguments
#              *unpacking operator
#              1. positional 2.default 3.keyword 4.ARBITRARY

#def add(*args):
 ##  for arg in args:
   #     total+= arg
    #return total
#print (add(1,2,3))

#def display_name(*args):
 #   for arg in args:
  #      print(arg, end=" ")
#display_name("Ram", "Shrestha", "is", "my" " friend")

#def print_address(**kwargs):
    #for key,value in kwargs.items():
        #rint(f"{key}:{value}")

#print_address(street="Caxton Close", city="Halifax",state="Nova Scotia",zip="B3M 4J5")

def shipping_label(*args, **kwargs):
 for arg in args:
  print(arg, end=" ")
 print()
 for key, value in kwargs.items():
   print(f"{key}: {value}")

shipping_label("Dr", "Sponge", "Squarepants" , "III",
               street="Caxton Close", 
               city="Halifax",
               state="Nova Scotia",
               zip="B3M 4J5")
               
