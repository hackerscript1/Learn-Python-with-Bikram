# Functions in Python ✅ 
# Block of statements that perform a specific task. 
# Functions can take arguments, return values, and be reused. 
# Functions are a key feature of programming that allows us to write reusable code. 
# Functions in Python are defined using the `def` keyword. 

'''
# Calculation
a = 5
b = 10
sum = a + b
print(sum)  # Output: 15 

# more line of code
a = 2
b = 10
sum = a + b
print(sum)  # Output: 12

# more line of code 
a = 12
b = 17 
sum = a + b
print(sum)  # Output: 29
'''

# Using Function 
'''
def calculate_sum(a, b):
    sum = a + b
    return sum

print(calculate_sum(6, 4))  # calling function
print(calculate_sum(12, 17))  # calling function
print(calculate_sum(16, 4))  # calling function
'''

# Average of 3 numbers
'''
def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

print(average(94, 84, 96))  # calling function
'''

# Default Parameters 
# Assigning a default value to parameter, which is used when no argument is passed. 
'''
def cal_prod(a=1, b=1):
    product = a * b
    print(a * b)
    return product

cal_prod()
'''

# Let‘s Practice ✅ 
# Question : 1 | Write a Function to print the length of a list. ( list is the parameter) 
'''
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["Iron Man", "Captain America", "Thor", "Hulk"]

def print_len(lst):
    print(len(lst))

print_len(cities)
print_len(heroes)
'''

# Question : 2 | Write a Function to print the elements of a list in a single line. ( list is the parameter) 
'''
cities = ["delhi", "gurgaon", "noida", "pune",]
heroes = ["Iron Man", "Captain America", "Thor", "Hulk"]

def print_elements(lst):
    for item in lst:
        print(item, end=" ")

print_elements(cities)
print_elements(heroes)
'''

# Question : 3 | Write a Function to find the factorial of n. (n is the parameter) 
'''
n = int(input("Enter a numbre: "))

def factorial(num):
    fact = 1
    for idx in range(1, num+1):
        fact *= idx
    return fact

print(factorial(n))
'''

# Question : 4 | Write a Function to convert USD to INR.
# (USD is the parameter)
'''
USD = float(input("Enter USD: "))
INR = USD * 83.88
print(INR)
'''

'''
def convert_usd_to_inr(USD):
    INR = USD * 83.88
    print(f"{USD} USD = {INR} INR")
    # return INR

convert_usd_to_inr(7)
# print(convert_usd_to_inr(2))
'''

# Question : 5 | Write a Function to find the number is Odd or Even.
'''
n = int(input("Enter a number: "))

def check_odd_or_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
check_odd_or_even(n)
'''

# Recursion ✅ 
# When a function calls itself repeatedly. 

# prints n to 1 backwards
'''
def show(n):
    if(n == 0): #Base Case
        return
    print(n)
    show(n-1)
    
show(5) # Output: 5 4 3 2 1
'''

# returns n!
'''
def fact(n):
    if (n == 0 or n == 1): #Base Case
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
'''

# Let‘s Practice ✅ 
# Question : 1 | Write a recursive function to calculate the sum of first n natural numbers. 
'''
def sum(n):
    if(n == 0):
        return 0
    return n + sum(n-1)

print(sum(5))
'''

# Question : 2 | Write a recursive function to print all elements in a list. Hint : use list & index as parameters. 
'''
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry'] 

def print_list(lst):
    if len(lst) == 0:
        return
    print(lst[0])
    print_list(lst[1:])

print_list(fruits)
'''

