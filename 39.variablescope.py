#variable scope = whereas vaariable is visible and accessible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

#Enclosed example
def func1():
    x=1
    print(x)

    def func2():
     x =2
     print(x)
    func2()

func1()

#Global
def func1():
 print(x) 

def func2():
 print(x) 

x=3

func1()
func2()

#Built in

from math import e
def func3():
 print(e)