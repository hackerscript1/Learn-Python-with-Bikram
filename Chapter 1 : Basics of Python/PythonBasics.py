print("My name is Bikram.", "My age is 22.")
print("Hello World")
print("My age is 22")
print(22)
print(22+34)

# Variables ✅ 
# Variable is a container for storing data values.
name = "Bikram"
age = 22
price = 25.99

print(name)
print(age)
print(price)

print("My name is: ", name)
print("My age is: ", age)

print(type(name))
print(type(age))
print(type(price))

# Data Types ✅ 
# String
name1 = "BM"
name2 = 'BM'
name3 = '''BM'''

print(name1)
print(name2)
print(name3)

# Integer
num1 = 64
num2 = -64

print(num1)
print(num2)

# Float
PI = 3.14
print(PI)
print(type(PI))

# Boolean
age1 = True
age2 = False

print(type(age1))
print(type(age2))

# None
a = None
print(type(a))

# Print Sum ✅ 
a = 2
b = 5
sum = a + b
print(sum)

# Comments in Python ✅ 
# Single Line Comment
# print("Hello World") # This is a comment

# Multi Line Comment
"""
print("Hello World")
print("Hello World")
"""

# Arithmetic Operators ✅ 
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# Relational Operators ✅ 
a = 50
b = 20

print(a == b)   # Equal to
print(a != b)   # Not Equal to
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to

# Assignment Operators ✅ 
a = 5
b = 2

a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a %= b  # a = a % b
a **= b # a = a ** b
a //= b # a = a // b

# Logical Operators ✅ 
a = 5
b = 2
c = 3

print(a > b and c > a) # and
print(a > b or c > a) # or
print(not a > b) # not

# Type Conversion ✅ 
a = 5
b = 2.0

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(a + b)) # <class 'float'>

# Type Casting ✅ 
a = 5
b = 2.0

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(int(a + b))) # <class 'int'>

# Input in Python ✅ 
name = input("Enter your name: ")
print("Hello " + name + "!")

# Enter name, age, marks ✅ 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print(name)
print(age)
print(marks)

# Let's Practice ✅ 
# Write a program to input 2 numbers & print their sum. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2 
print("Sum is: ", sum)

# Write a program to input side of a square & print its area. 
side = float(input("Enter side of square: "))
area = side * side
# area = side ** 2
print("Area of square is: ", area)

# Write a program to input 2 floating point numbers & print their average.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("Average is: ", average)

# Write a program to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a>=b)
