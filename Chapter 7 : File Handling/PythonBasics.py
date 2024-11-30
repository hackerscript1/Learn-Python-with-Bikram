# File I/O in Python ✅ 
# Python can be used to perform operations on a file. (read & write data)

# Types of all files
# Text Files : .txt, .docx, .log etc.1.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc. 

# Open, read & close File ✅ 
# We have to open a file before reading or writing. 

'''
f = open("demo.txt", "r")

# data = f.read()
# data = f.read(5)
# data = f.readline()
data = f.readlines()

print(data)
# print(type(data))
f.close()
'''

# Writing to a file ✅ 
'''
f = open("demo.txt", "w")
f.write("Hello, Python!\nHow are you?")
f.close()
'''

# Append to a file ✅ 
'''
f = open("demo.txt", "a")
f.write("\nI am good, thank you!")
f.close()
'''

# with Syntax ✅ 
'''
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    # with statement automatically closes the file after execution.
'''

'''
with open("demo.txt", "w") as f:
    f.write("Hello, Python!\nHow are you?")
    # with statement automatically closes the file after execution.
'''

# Deleting a File ✅ 
# using the os module 
# Module (like a code library) is a file written by another programmer that generally has a functions we can use. 
'''
import os
os.remove("demo.txt")
'''


# Let‘s Practice ✅ 
# Question : 1 | Create a new file “practice.txt” using python. Add the following data in it: 
# “Hello, Python! How are you?”
# “I am good, thank you!”
# “What is your name?”
# “My name is Python.”
# “I am a programming language.”
'''
with open("practice.txt", "w") as f:
    f.write("Hello, Python! How are you?\n")
    f.write("I am good, thank you!\n")
    f.write("What is your name?\n")
    f.write("My name is Python.\n")
    f.write("I am a programming language.\n")
'''

# Question : 2 | Write a Function that replace all occurrences of “java” with “python” in above file. 
# Hint: Use the read() and write() methods of the file object.
'''
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
'''

# using function
'''
def replace_java_with_python():
    with open("practice.txt", "r") as f:
        data = f.read()
        new_data = data.replace("Java", "Python")
        with open("practice.txt", "w") as f:
            f.write(new_data)
            
replace_java_with_python()
'''

# Question : 3 | Search if the word “learning” exists in the file or not.
'''
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if word in data:
        print("The word 'learning' exists in the file.")
    else:
        print("The word 'learning' does not exist in the file.")
'''

# Question : 4 | Write a Function to find in which line of the file does the word “learning” occur first.
# Print -1 if word not found.
'''
word = "learning"
with open("practice.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        if word in data[i]:
            print(f"The word 'learning' occurs first in line {i+1}")
            break
    else:
        print(f"The word 'learning' does not exist in the file")
'''

# From a file containing numbers separated by comma, print the count of even numbers.
'''
with open("numbers.txt", "r") as f:
    data = f.read()
    numbers = [int(num) for num in data.split(",")]
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"Count of even numbers: {even_count}")
'''

'''
count = 0

with open("numbers.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")  
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)
'''


