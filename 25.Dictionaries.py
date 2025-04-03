# dictionay =a collection of {key:value} pairs
#             ordered and changeable.No duplicates

capitals = {"USA": "Washington",
            "Canada": "Halifax",
            "China": "Beijing",
           "Russia":  "Moscow"}

#print(dir(capitals))

#print(capitals.get("USA"))
#if capitals.get("Canada"):
 #   print("The capital exists")
#else:
#    print("The capital doesn't exist")
#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("China")
#capitals.popitem()
#keys = capitals.keys()

##   print(key, end=" ")

#values = capitals.values()
#print (values)  
#for value in values:
  #  print(value)

items = capitals.items
for key, value in capitals.items():
    print(f"{key} : {value}")