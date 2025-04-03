#Polymorphism = Greek word that means to "have many forms or faces
#               Poly = Many
#               Morphe = Form


#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck typing" =  Object must have necessary attributes / methods

from abc import ABC, abstractmethod
class Shape:
     
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self): 
      return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self,width):
        self.width = width
    
    def area(self): 
      return self.width * self.width


class Triangle(Shape):
     def __init__(self,width,height):
        self.width = width
        self.height = height

     def area(self): 
      return self.width * self.height *0.5
     
class Pizza(Circle):
   def __init__(self,topping, radius):
      super().__init__(radius)
      self.topping = topping
      


shapes = [Circle(4), Square(5),Triangle(6,7),Pizza("Peproni",8)]

for shape in shapes:
   print(f"{shape.area()}cm²")

