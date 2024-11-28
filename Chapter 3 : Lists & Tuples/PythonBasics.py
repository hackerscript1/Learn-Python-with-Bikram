# Lists in Python ✅ 
# Lists in Python are ordered collections of items that can be of any data type, including strings, integers, floats, and other lists. They are denoted by square brackets `[]` and are mutable. 

marks = [87, 64, 33, 95, 76]

print(marks)  # Output: [87, 64, 33, 95, 76]
print(type(marks))  # Output: <class 'list'>

student = ["Sumit", 19, "West Bengal"]
print(student)  # Output: ['Sumit', 19, 'West Bengal']
print(student[0]) # Output: Sumit
print(len(student))

# List Slicing ✅ 
marks = [87, 96, 84, 65, 78, 54, 92]

print(marks[1:4]) # Output: [96, 84, 65] 
print(marks[:4]) # Output: [87, 96, 84, 65] 
print(marks[1:])  # Output: [96, 84, 65, 78, 54, 92]
print(marks[-3:-1]) # Output: [78, 54]

# List Methods ✅ 
list = [2, 1, 3]

# Append 
list.append(4)
print(list) # Output: [2, 1, 3, 4]

# Short
print(list) # Output: [2, 1, 3]
list.sort() 
print(list) # Output: [1, 2, 3]

# Reverse
print(list) # Output: [1, 2, 3]
list.reverse()
print(list) # Output: [3, 2, 1]
list.sort(reverse=True)
print(list) # Output: [3, 2, 1]

# Insert 
list = [1, 2, 3, 4, 5]
list.insert(2, 6)
print(list) # Output: [1, 2, 6, 3, 4, 5]

# Remove 
list = [1, 2, 3, 4, 5]
list.remove(3)
print(list) # Output: [1, 2, 4, 5]

# Pop
list = [1, 2, 3, 4, 5]
print(list.pop()) # Output: 5

# Tuples in Python ✅ 
# Tuples are similar to lists but are immutable. They are defined by enclosing a sequence of values

tup = (87, 64, 33, 95, 76) 
print(tup) # Output: (87, 64, 33, 95, 76)

# tup[0] = 43 # are not allowed in Python

tup1 = ()
tup2 = (1, )
tup3 = (1, 2, 3)

# Tuples Methods ✅
# Tuples are immutable, so they do not have any methods to add or remove elements.

tup = (2, 1, 3, 1)

# index
print(tup.index(1)) # Output: 1

# count
print(tup.count(1)) # Output: 2

# Let's Practice ✅ 
# Create a list of 5 numbers and sort it in ascending order. Then, remove the first element and print the list. 
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers) # Output: [1, 2, 5, 8, 9] 
print(numbers.pop(0)) # Output: 1

# Write a Program to ask the user to enter names of their 3 favorite movies & store them in a list. 
moves = []
moves.append(input("Enter 1st move name: "))
moves.append(input("Enter 2nd move name: "))
moves.append(input("Enter 3rd move name: "))
print(moves) # Output: ['movie1', 'movie2', 'movie3'] 

# Write a Program to check if a list contains a palindrome of elements. (Hint: use copy() method) 
list = [1, 2, 3, 2, 1]

copy_list = list.copy()
copy_list.sort()

if(list == copy_list):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

# Next Solution
list = [1, 2, 3, 2, 1]

if list == list[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

# Write a Program to count the number of students with the "A" grade in the following tuple. 
grades = ('A', 'B', 'A', 'D' 'C', 'A', 'B')
count = grades.count('A')
print("Number of students with 'A' grade: ", count)

# Sort the above values in a list & sort them from 'A' to 'D'. 
grades.sort()
print(grades)

grades = ('A', 'B', 'A', 'D', 'C', 'A', 'B')
grades_list = sorted(grades)
print(grades_list)  # Output: ['A', 'A', 'A', 'B', 'B', 'C', 'D']


