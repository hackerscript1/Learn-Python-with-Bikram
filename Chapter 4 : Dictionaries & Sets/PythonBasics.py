# Dictionary in Python ✅ 
# A dictionary is a collection of key-value pairs. It is an unordered collection of items, where each item is a pair of a key and a value. The key is unique and cannot be repeated, while the value can be repeated. Dictionaries are mutable, meaning they can be changed after creation.

dict = {
    "Name" : "Bikram",
    "Age" : 22,
    "Is_Adult" : True,
    "Subject" : ["Python", "C", "Java"],
    "Topics" : ("Dict", "Set"),
    "Marks" : [98, 94, 96],
    "CGPA" : 98.5,
}

print(type(dict))
print(dict)
dict["Name"] = "Susmita"
print(dict)
dict["Marks"] = [98, 96, 98]
print(dict)

null_dict = {}
null_dict["Name"] = "Mr. Hacker Bikram"
print(null_dict)  # Output: {} 


# Nested Dictionaries ✅ 
# A nested dictionary is a dictionary that contains another dictionary as its value. This is useful when you want to store a collection of key-value pairs where each value is another dictionary.

nested_dict = {
    "Name" : "Susmita",
    "Age" : 22,
    "Address" : {
        "Vill" : "Kulahariya",
        "District" : "Ara",
        "Pin" : 700001,
        "State" : "Bihar",
    },
    "Profesion" : "Ethical Hacker"
}

print(len(nested_dict))
print(nested_dict.keys())
print(list(nested_dict.keys()))
print(nested_dict)


# Dictionary Methods ✅ 
# Dictionaries have several methods that can be used to perform various operations.
# Here are some of the most commonly used methods:

my_Dict = {
    "Name" : "Bikram",
    "Age" : 22,
    "Profesion" : "Penetration Tester",
}

# key() #returns all keys 
my_Dict.keys()
print(my_Dict.keys())

# values() #returns all values
my_Dict.values()
print(my_Dict.values())

# items() #returns all key-value pairs
my_Dict.items()
print(my_Dict.items())

# get() #returns the value for a given key
my_Dict.get("Name")
print(my_Dict.get("Name"))

# pop() #removes and returns the value for a given key
my_Dict.pop("Age")
print(my_Dict)

# update() #updates the dictionary with the items from another dictionary
my_Dict.update({"CGPA": 98.5})
print(my_Dict)


# Set in Python ✅ 
# A set is an unordered collection of unique elements.
# repeated elements stored only once.
# Sets are used to store a collection of items that need to be accessed randomly.
# Sets are mutable, meaning they can be changed after creation.
# Sets are denoted by curly brackets {}.

collection = {1, 2, 2, 2, "Hello", "World" , "World", 4}
print(collection)
print(type(collection))
print(len(collection))


# Empty Set Syntax ✅ 
# An empty set can be created using the set() function or by using curly brackets {}. 

# This is worng 
# This is not a set. This is a dict. 
empty_set = {}
print(empty_set)
print(type(empty_set))

# This is write
# This is a empty set
null_set = set()
print(null_set)
print(type(null_set))


# Set Methods ✅ 
collection = set()

# add() #adds an element to the set
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
print(collection)

# remove() #removes an element from the set if it exists
collection.remove(2)
print(collection)

# pop() #removes and returns an arbitrary element from the set
collection.pop()
print(collection)

# clear() #removes all elements from the set 
collection.clear()
print(collection)

# set1.union(set2) #combines both set values & returns new
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))

# set1.intersection(set2) #combines common values & returns new 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))


# Let‘s Practice ✅ 
# Question: 1 | Store following word meanings in a python dictionary :
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal” 
dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal",
}
print(dict)

# Question: 2 | You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students. 
# ”python”, “java”, “C++”, “python”, “javascript”, “java”, “python”, “java”, “C++”, “C” 
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"] 
unique_subjects = set(subjects)
print(len(unique_subjects))

# Question: 3 | Write a Program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value. 
marks = {}
subject1 = input("Enter subject 1 name: ")
marks[subject1] = int(input("Enter marks of " + subject1 + ": "))
subject2 = input("Enter subject 2 name: ")
marks[subject2] = int(input("Enter marks of " + subject2 + ": "))
subject3 = input("Enter subject 3 name: ")
marks[subject3] = int(input("Enter marks of " + subject3 + ": "))
print(marks)

# Question: 4 | Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types) 
set1 = {9, 9.0}
set1 = {'9', 9.0}
print(set1)

values = {
    ("float", 9.0),
    ("int", 9),
}
print(values)

