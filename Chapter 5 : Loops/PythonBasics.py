# Loops in Python ✅ 
# Loops are used to repeat instructions.
'''
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
'''

# While Loops ✅ 
'''
count = 1
while count <= 5:
    print("Hello")
    count += 1
    
print(count)
'''

# Let‘s Practice ✅ 
# Question : 1 | Print numbers from 1 to 100. 
'''
i = 1
while i <= 100:
    print(i)
    i += 1
'''

# Question : 2 | Print numbers from 100 to 1.
'''
i = 100
while i >= 1:
    print(i)
    i -= 1
''' 

# Question : 3 | Print the multiplication table of a number n.
'''
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1
'''

# Question : 4 | Print the elements of the following list using a loop: 
'''
l = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
while i < len(l):
    print(l[i])
    i += 1
'''

# Question : 5 | Search for a number x in this tuple using loop: 
'''
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)
x = int(input("Enter a number: "))

i = 0
while i < len(t): 
    if t[i] == x:
        print(f"Number found: Index Number = {i}")
    else:
        print("Finding...")
    i += 1
'''

'''
t = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter a number: "))
i = 0
found = False
while i < len(t):
    if t[i] == x:
        print(f"Number found: Index Number = {i}")
        found = True
        break
    i += 1
    
if not found:
    print("Number not found!") 
'''

# Break & Continue ✅ 
# Break : used to terminate the loop when encountered. 
'''
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
'''

# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration. 
'''
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
'''

# ODD & EVEN Number
'''
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
'''

'''
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
'''
 
# For Loops ✅ 
# Loops are used used for sequential traversal. For traversing list, string, tuples etc. 
'''
list = [1, 2, 3, 4, 5, 6, 7]
for val in list:
    print(val)
'''  

'''
veggies_List = ['broccoli', 'carrots', 'cucumber', 'spinach', 'tomatoes'] 
for el in veggies_List:
    print(el)
'''

'''
tup = (2, 6, 4, 3, 8, 9, 1)
for i in tup:
    print(i)
'''

'''
str = "Mr. Hacker Bikram"
for char in str:
    print(char)
'''

# for Loop with else ✅ 
'''
str = "Bikram"
for char in str:
    print(char)
else:
    print("No more characters in the string")
'''

'''
str = "Bikram"
for char in str:
    if(char == 'k'):
        print("k found")
        break
    print(char)
else:
    print("No more characters in the string")
'''

# Let‘s Practice ✅ 
# Question : 1 | Print the elements of the following list using a loop: 
'''
l = [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
for el in l:
    print(el)
'''

# Question : 2 | Search for a number x in this tuple using loop: 
'''
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100) 
x = int(input("Enter a number: "))
idx = 0
for i in tup:
    if(i == x):
        print(x, "is found in the tuple | Index Number is:", idx)
        break
    idx += 1
else:
    print(x, "is not found in the tuple")
'''      

# range() ✅
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. 
# range(start?, stop, step?) 
# start: The starting number of the sequence. Default is 0.
# stop: The end value of the sequence. This is exclusive, which means the stop value will be excluded from the sequence. Default is the maximum possible integer value.
# step: The difference between each number in the sequence. Default is 1.
'''
for el in range(10):
    print(el)
'''

'''
for el in range(1, 10):
    print(el)
''' 

'''
for el in range(2, 100, 2):
    print(el)
'''

# Let‘s Practice ✅ 
# Question : 1  | Print numbers from 1 to 100.
'''
for num in range(1, 101):
    print(num)
'''

# Question : 2 | Print numbers from 100 to 1.
'''
for num in range(100, 0, -1):
    print(num)
'''

# Question : 3 | Print the multiplication table of a number n. 
'''
x = int(input("Enter number: "))
for idx in range(1, 11):
    print(f"{x} X {idx} = {x*idx}")
'''

# pass Statement ✅ 
# pass is a null statement that does nothing. It is used as a placeholder for future code. 
'''
for i in range(5):
    pass

print("Importent Work!")
'''

# Let‘s Practice ✅ 
# Question : 1 | Write a Program to find the factorial of first n natural numbers. (using while)
'''
x = int(input("Enter number: "))
factorial = 0
i = 1
while(i <= x):
    factorial += i
    i += 1
print("factorial of first n natural number is:", factorial)
'''

# Question : 2 | Write a Program to find the factorial of first n numbers. (using for) 
'''
x = int(input("Enter number: "))
factorial = 1
for idx in range(x, 0, -1):
    factorial *= idx
print("Factorial of first n number is:", factorial)
'''

'''
x = int(input("Enter number: "))
factorial = 1

for idx in range(1, x + 1):
    factorial *= idx

print("Factorial of first n numbers is:", factorial)
'''

