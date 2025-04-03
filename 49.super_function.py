# super() = Function in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality to the inherited methods

class Shapes:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shapes):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius

#METHOD OVERIDING
    def describe(self):
        
        print(f"The are of circle is {3.14 * self.radius * self.radius}")
        super().describe()

class Square(Shapes):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width

    def describe(self):
        
        print(f"The are of circle is { self.width * self.width}")
        super().describe()

class Triangle(Shapes):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height

    def describe(self):
        
        print(f"The are of circle is { self.width * self.height / 2}")
        super().describe()

circle= Circle(color="red", filled=True, radius=5)
square= Square(color="yellow", filled=False, width=3)
triangle= Triangle(color="blue", filled=False, width=6,height=10)
print(circle.color)
print(circle.filled)
print(f"{circle.radius}cm")
circle.describe()
print()

print(square.color)
print(square.filled)
print(f"{square.width}cm")
square.describe()

print()

print(triangle.color)
print(triangle.filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()
