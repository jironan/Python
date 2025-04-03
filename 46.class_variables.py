#class variables = Shared among all instances of clas
#                  Defined outside the contructor
#                  Allow you to share data among all the objects created from that class

class Student:

    class_year = 2024
    num_std = 0
    def __init__(self, name, age):
        self.age = age
        self.name = name
        Student.num_std += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Bhire", 20)
student4 = Student("Sandy", 20)

print(student1.name) 
print(student1.age)
print(Student.class_year)
print(Student.num_std)

print(f"My graduating class of {Student.class_year} has {Student.num_std} students")
print(f"{student1.name}")
print(f"{student2.name}")
print(f"{student3.name}")
print(f"{student4.name}")

