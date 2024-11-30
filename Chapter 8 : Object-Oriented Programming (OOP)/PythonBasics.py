# OOP in Python ✅ 
# To map with real world scenarios, we started using objects in code. 
# This is called object oriented programming. 

# Class & Object in Python ✅ 
# Class is a blueprint for creating objects. 
'''
# creating class
class Student:
    name = "Bikram"

# creating object (instance)
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)
'''

'''
class Car:
    color = "Blue"
    model = "Toyota"
    
car1 = Car()
print(car1.color)
print(car1.model)

car2 = Car()
print(car2.color)
print(car2.model)
'''

# __init__ Function ✅ 
# This function is used to initialize the attributes of a class.
# Constructor : All classes have a function called __init__(), which is always executed when the object is being initiated. 
'''
# creating class 
class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
        
# creating object (instance)
s1 = Student("Bikram", 22, 3)
print(s1.name)
print(s1.age)
print(s1.rollno)

s2 = Student("Sumit", 20, 5)
print(s2.name)
print(s2.age)
print(s2.rollno)
'''

# Class & Instance Attributes ✅ 
# Class attributes are shared by all instances of a class.
# Instance attributes are unique to each instance of a class.
'''
class Student:
    college = "ABC College"  # Class attribute
    def __init__(self, name, age, rollno):  # Instance attribute
        self.name = name
        self.age = age
        self.rollno = rollno
        
# creating object (instance)
s1 = Student("Bikram", 22, 3)
print(s1.name)
print(s1.age)
print(s1.rollno)
print(s1.college)  # Accessing class attribute
print(Student.college)  # Accessing class attribute
'''

# Methods ✅ 
# Methods are functions that belong to objects.
# Methods are functions that are defined inside a class.
# They are used to perform some operation on the data members of the class.
'''
# creating class
class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    
    def display(self):  # Method
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.rollno)

# creating object
s1 = Student("Bikram", 22, 3)
s1.display()  # calling method
'''

# Let‘s Practice ✅ 
# Question : 1 | Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average. 
'''
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3
    
s1 = Student("Bikram", 96, 94, 98)
print(f"Hello, {s1.name}! your avg marks is : {s1.average()}")

s1.name = "Sumit"
print(f"Hello, {s1.name}! your avg marks is : {s1.average()}")
'''

# Static Methods ✅ 
# Methods that don’t use the self parameter (work at class level) 
'''
class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
        
    @staticmethod   # decorator
    def greet():
        print("Hello, Welcome to our class!")
    
    def display(self):  # Method
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.rollno)

s1 = Student("Bikram", 22, 3)
s1.greet()
s1.display()

# *Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it 
'''

# Important ✅ 
# 1. Abstraction : Hiding the implementation details of a class and only showing the essential features to the user. 
# 2. Encapsulation : Wrapping data and functions into a single unit (object).
'''
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")
    
car1 = Car()
car1.start()
'''

# Let‘s Practice ✅ 
# Question : 1 | Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance. 
'''
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Debited amount:", amount)
            print("Remaining balance:", self.balance)
        
    def credit(self, amount):
        self.balance += amount
        print("Credited amount:", amount)
        print("Remaining balance:", self.balance)
    
    def print_balance(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

# Account : 1
account1 = Account(1000, 12345)
account1.print_balance()
account1.debit(500)
account1.credit(2000)

# Account : 2
account2 = Account(500, 67890)
account2.print_balance()
account2.credit(4500)
account2.debit(100)
'''

# del keyword ✅ 
# Used to delete object properties or object itself.
# del s1.name
# del s1
'''
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("John")
print(s1.name)
del s1.name
print(s1.name)
'''

# Private(like) attributes & methods ✅ 
# Conceptual Implementations in Python 
# Private attributes & methods are meant to be use only within the class and are not accessible  from outside the class. 
'''
class Account:
    def __init__(self, account_no, account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass
        
    def reset_pass(self):
        print(self.__account_pass)
        self.__account_pass = "new_password"
        
acc1 = Account("1234", "abc")
print(acc1.account_no) # Accessible
# print(acc1.__account_pass) # Not Accessible
print(acc1._Account__account_pass) # Accessible but not recommended

print(acc1.account_no)
print(acc1.reset_pass())
# print(acc1.__account_pass) # Not Accessible
print(acc1._Account__account_pass) # Accessible but not recommended
'''

'''
class Person:
    __name = "anonymous"
    def __init__(self, name):
        self.name = name

# print(Person.__name) # Not Accessible
# print(Person._Person__name) # Accessible but not recommended
'''

'''
class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello, " + self.__name)
    
    def welcome(self):
        self.__hello()
        
p1 = Person()
# print(p1.__name) # Not Accessible
# print(p1._Person__name) # Accessible but not recommended
print(p1.welcome()) # Accessible
# print(p1._Person__hello()) # Accessible but not recommended
'''

# In Python, we can't directly access private attributes and methods from outside the class. But we can access them using the name mangling feature. Name mangling is a feature in Python that renames the attribute or method with a double underscore prefix. This makes it difficult to access the attribute or method from outside the class, but it doesn't make it impossible. 


# The name mangling feature is used to prevent accidental access to private attributes and methods. It's not a security feature, but rather a way to indicate that the attribute or method is intended to be private and should not be accessed directly from outside the class.


# 3. Inheritance : When one class (child/derived) derives the properties & methods of another class (parent/base).
# Single Inheritance
'''
class Car:
    @staticmethod
    def start():
        return "Car started..."
    
    @staticmethod
    def stop():
        return "Car stopped..."
    
class ToyotaCar(Car):
    def __init__(self, color):
        self.color = color

    def start(self):
        return Car.start() + " " + self.color + " Toyota Car started..."

    def stop(self):
        return Car.stop() + " " + self.color + " Toyota Car stopped..."
    
car1 = ToyotaCar("blue")
print(car1.start())
print(car1.stop())

car2 = ToyotaCar("white")
print(car2.start())
print(car2.stop())
'''

# Inheritance Types ✅ 
# 1. Single Inheritance : When one class inherits from another class.
# 2. Multi-level Inheritance : When one class inherits from another class and that class
# 3. Multiple Inheritance : When one class inherits from more than one class.

# Multi-level Inheritance
'''
class Car:
    @staticmethod
    def start():
        return "Car started..."
    
    @staticmethod
    def stop():
        return "Car stopped..."
    
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
 
car1 = Fortuner("diesel")
print(car1.start())
'''

# Multiple Inheritance
'''
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C:
    varC = "Welcome to class C"

class D(A, B, C):
    varD = "Welcome to class D"

d1 = D()
print(d1.varD) 
print(d1.varC)
print(d1.varB)
print(d1.varA)
'''

# Super method ✅ 
# super() method is used to access methods of the parcent class. 
'''
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    @staticmethod
    def start():
        return "Car started..."
    
    @staticmethod
    def stop():
        return "Car stopped..."
    
class ToyotaCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
car1 = ToyotaCar("Toyota", "Prius")
print(car1.start())
print(car1.stop())
print(car1.brand)
print(car1.model)
'''

# class method ✅ 
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.
'''
class Student:
    school = "Springfield Elementary"
    
    def changeScool(self, school):
        self.school = school
        
s1 = Student()
s1.changeScool("Chandipur B.R.S High School (H.S)")
print(s1.school)
print(Student.school)
'''

'''
class Student:
    school = "Springfield Elementary"
    
    def changeScool(self, school):
        # Student.school = school
        self.__class__.school = school
        
s1 = Student()
s1.changeScool("Chandipur B.R.S High School (H.S)")
print(s1.school)
print(Student.school)
'''

# class method ✅ 
'''
class Student:
    school = "Springfield Elementary"
    
    @classmethod
    def changeScool(cls, school):
        cls.school = school
        
s1 = Student()
s1.changeScool("Chandipur B.R.S High School (H.S)")
print(s1.school)
print(Student.school)
'''

# Property ✅ 
# We use @property decorator on any method in the class to use the method as a property.
'''
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def calcPercentage(self):
        return (self.phy + self.chem + self.math) / 3
    
s1 = Student(98, 94, 96)
print(s1.calcPercentage)

s1.phy = 86
print(s1.phy)
print(s1.calcPercentage)
'''


# Polymorphism: Operator Overloading ✅ 
# When the same operator is allowed to have different meaning according to the context. 

# Operator & Dunder Functions 
# Dunder functions are special functions in Python classes that are surrounded by double underscores on either side.
# They are used to overload operators in Python classes.

# a+b   #addition           #a.__add__(b)
'''
print(1 + 2) #3
print("Hello" + "World") #HelloWorld
print([1, 2] + [3, 4]) #[1, 2, 3, 4]
''' 

'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")
    
    def __add__(self, other):
        newReal = self.real + other.real
        newImag = self.imag + other.imag
        return Complex(newReal, newImag)
        # return Complex(self.real + other.real, self.imag + other.imag)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

addition = num1 + num2
addition.showNumber()  # Output: 5i + 9j
'''

# a-b   #subtraction        #a.__sub__(b)
'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")
    
    def __sub__(self, other):
        newReal = self.real - other.real
        newImag = self.imag - other.imag
        return Complex(newReal, newImag)
        # return Complex(self.real - other.real, self.imag - other.imag)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

subtraction = num1 - num2
subtraction.showNumber()
'''

# a*b   #multiplication     #a.__mul__(b)
# a/b   #division           #a.__truediv__(b)
# a%b   #modulus            #a.__mod__(b)


# Let's Practice ✅ 
# Question : 1 | Define a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to claculate  the perimeter of the circle.
'''
class Circle:
    def __init__(self, r):
        self.radius = r
        
    def Area(self):
        return (22/7) * (self.radius ** 2)
    
    def Perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(f"Area of the circle is: {c1.Area()}")
print(f"Perimeter of the circle is: {c1.Perimeter()}")
'''

# Question : 2 | Define a Employee class with attributes role, deparment & salary. This class also a showDetails() method. 
# Create a Enginner class that inherits properties from Employee & has additional attributes : name & age.
'''
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        return f"Role: {self.role}, Department: {self.department}, Salary: {self
    .salary}"

class Enginner(Employee):
    def __init__(self, name, age, role, department, salary):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)
    
    def showDetails(self):
        return f"Name: {self.name}, Age: {self.age}, " + super().showDetails()

e1 = Enginner("Bikram", 22, "Penetration Tester", "Cyber Security", 85000)
print(e1.showDetails())
'''

# Question : 3 | Create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that : order1 > order2 if price of order1 > price of order2 
'''
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

o1 = Order("Apple", 100)
o2 = Order("Banana", 50)
print(o1 > o2)  # Output: True
print(o2 > o1)  # Output: False
'''


