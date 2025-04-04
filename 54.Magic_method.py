#Magic methods =  Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built operations
#                 They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author =author
        self.num_pages = num_pages

    def __str__(self):
        return f"title: {self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __gt__(self,other):
        return self.num_pages> other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__ (self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__ (self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The Hobbit", "j.r.r Tolkein", 310)
book4 = Book("The Hobbit", "j.r.r Tolkein", 310)
book2 = Book("Harry Potter", "J K Rolling", 223)
book3 = Book("Varry Motter", "L K Bolling", 322)

print(book1)
print(book1 == book4)
print(book2<book3)
print(book2+book3)
print("Varry" in book3)
print(book2['title'])
print(book3['author'])
print(book1['num_pages'])


    
print(book1['audio'])
   
    

