#default arguments: A defau;t value for certain parameter
#                     1.positional 2.default 3.keyword 4. arbitary

#POSITIONAL
#tax = 0.05
#def net_price(last_price, discount=0, tax=0.05):
 #   return (last_price * (1-discount) * (1+tax) )

# print(net_price(500))

#DEFAULT
#import time

#def count (end, start=0):
 #   for x in range (start,end+1):
  #      print (x)
   #     time.sleep(0.5)
    #print("DONE !")

#count(30, 15)

#def hello(greeting, title, first, last):
 #   print(f"{greeting} {title}{first} {last}")
    
#hello(title="Mr.", last="Sapkota", first="Shristi", greeting="Hi")

# for x in range(1,11):
  #  print(x, end=" ")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=647,first=769,last= 6412)
print(phone_num)