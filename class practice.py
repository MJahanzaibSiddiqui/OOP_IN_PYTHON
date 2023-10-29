# class myfirstclass:
#     j=0
    
# j1=myfirstclass()
# print(j1.j)

# class mysecondclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=mysecondclass("jazzy",19)
# print(p1.age,p1.name)

# class mysecondclass:
#     def function(self):
#         print("Hello WORLD")
    
# p1=mysecondclass()
# p1.function()
# print(p1.function()) 


# class mythirdclass:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"{self.x}{self.y}"      
# p1=mythirdclass("jazzy",19)
# print(p1)         

# second method

# class mythirdclass:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return str(self.x) + str(self.y)
# p1 = mythirdclass("jazzy", 19)
# print(p1)

# class mythirdclass:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"{self.x}{self.y}"
# p1 = mythirdclass("jazzy", 19)
# print(p1)

# In Python, __str__ is a special method (also known as a "magic method" or "dunder method") that is used to define a human-readable string representation of an object. This method is automatically called by functions like str() and print() when you want to obtain a string representation of an object.

# class myfourthclass:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("hello world " +self.name, +self.age)
# p1 = myfourthclass("Jazzy ", 19 ) 
# p1.myfunc()       
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# #Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()
# class Student(Person):
#   pass
# x = Student("Mike", "Olsen")
# x.printname()

# class father:
#     def __init__(self,fname,sname):
#         self.fathername=fname
#         self.sirname=sname        
#     def printtree(self):
#         print(self.fathername, self.sirname)    
# f=father("Imran", "Siddiqui")
# # f.printtree()
# class son(father):
#     def __init__(self, bname, sname):
#         # father.__init__(self,fname,sname)
#         # or
#         super().__init__(bname, sname)
#         self.boyname=bname
#     def welcome(self):
#        print("Welcome", self.boyname, self.sirname)
# s=son("Jahanzaib","siddiqui")
# f.printtree()
# s.welcome()

#ONE MORE METHOD

# class Parent:
#     def hi(self, fname, lname):
#         self.fname = fname  
#         self.lname = lname  

# class Student(Parent):
#     def hello(self,sname):
#         self.studentname=sname
#         print(f"{self.fname} {self.lname}{self.studentname}")

# p2 = Student()
# p2.hi("ehtisham", "afzal")  
# p2.hello("Boy")


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    print(model,brand)

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()
print





        
        
        
        
                      
        