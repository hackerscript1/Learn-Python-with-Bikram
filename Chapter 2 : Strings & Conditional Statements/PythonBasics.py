# Strings ✅ 
# Strings are immutable
# Strings are sequences of characters
# Strings are enclosed in single quotes or double quotes
# Strings can be concatenated using the + operator
# Strings can be repeated using the * operator
# Strings can be indexed using square brackets
# Strings can be sliced using the slice operator
# Strings can be formatted using the format() method
# Strings can be converted to uppercase or lowercase using the upper() and lower() methods
# Strings can be split into a list of words using the split() method
# Strings can be joined into a single string using the join() method
# Strings can be searched for a substring using the find() method
# Strings can be replaced using the replace() method

str1 = "This is 1st String."
str2 = 'This is 2nd String.'
str3 = """This is 3rd String."""

str = "Thsi is a string. \nWe are creating it in \tpython"
print(str)

str1 = "Hello"
str2 = "World"
finalString = str1 + " " + str2
print(finalString)

str = "This is String."
print(len(str))

# Indexing ✅ 
str = "This is String."

print(str[0]) # T
print(str[1]) # h
print(str[2]) # i
print(str[3]) # s

# Slicing ✅ 
str = "This is String."

print(str[0:3]) # Thi
print(str[0:4]) # This
print(str[0:7]) # This is
print(str[0:-1]) # This is String
print(str[-9:-2]) # s Strin

# String Functions ✅ 
str = "This is String."

print(str.upper()) # THIS IS STRING.
print(str.lower()) # this is string.
print(str.capitalize()) # This is string.
print(str.title()) # This Is String.
print(str.swapcase()) # tHIS IS sTRING.
print(str.endswith("ng")) # return true if string ends with substr
print(str.startswith("Th")) # return true if string starts with substr
print(str.replace("is", "was")) # Thwas was String.
print(str.find("is")) # return index of first occurrence of substring
print(str.count("is")) # return number of occurrences of substring

# Let's Practice ✅ 
# Write a program to input user's first name & print its length. 
name = input("Enter your name: ")
print(len(name))

# Write a program to find the occurrence of '$' is a String. 
str = "This $ is a $ string."
print(str.find("$"))
print(str.count("$"))

# Conditional Statements ✅ 
age = int(input("Enter your age: "))

if(age >= 18):
    print("You are eligible to vote.")
elif(age < 18):
    print("You are not eligible to vote.")
else:
    print("Invalid age")
    
# Grade students based on marks ✅ 
marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Grade: A")
elif(marks >= 80):
    print("Grade: B")
elif(marks >= 70):
    print("Grade: C")
elif(marks >= 60):
    print("Grade: D")
else:
    print("Grade: F")

# Let's Practice ✅ 
# Write a program to check whether a number is positive or negative. 
num = int(input("Enter a number: "))

if(num > 0):
    print("Positive number")
elif(num < 0):
    print("Negative number")
else:
    print("Zero")
    
# Write a program to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Even number")
else:
    print("Odd number")
    
# Write a program to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

# if(num1 > num2):
#     if(num1 > num3):
#         print("Greatest number is: ", num1)
#     else:
#         print("Greatest number is: ", num3)
# else:
#     if(num2 > num3):
#         print("Greatest number is: ", num2)
#     else:
#         print("Greatest number is: ", num3)

if(num1>num2 and num1>num3):
    print("Greatest number is: ", num1)
elif(num2>num1 and num2>num3):
    print("Greatest number is: ", num2)
elif(num3>num2 and num3>num1):
    print("Greatest number is: ", num3)
        
# Write a program to check if a number is a multiple of 7 or not.
num = int(input("Enter a number: "))

if(num % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")


# Write a program to find the greatest of 4 numbers entered by the user.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print("Greatest number is: ", num1)
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("Greatest number is: ", num2)
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("Greatest number is: ", num3)
elif(num4 > num1 and num4 > num2 and num4 > num3):
    print("Greatest number is: ", num4)
else:
    print("All numbers are equal")


