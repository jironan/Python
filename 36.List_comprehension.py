#List comprehension =  A concise was to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#ubles = [x * 2 for x in range (1,10)]
#print(doubles)

#triples=[y*3 for y in range(1,11)]
#print(triples)

#squares = [ x*x for x in range(1,11)]
#print(squares)

##fruits =["apple", "berry","banana"]
#fruits=[fruit.upper()for fruit in fruits]
#fruits=[fruit[0] for fruit in fruits]
#print(fruits)

numbers=[-1,2,-3,4,-5,6]
positive_num = [num for num in numbers if num>=0]
print(positive_num)

negative_num  = [num for num in numbers if num<=0]
print(negative_num)


