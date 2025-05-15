""" Create a dictionary and use loops to print keys and values:
a) Create a dictionary, stuInfo with the keys name, gpa, and age. Give appropriate values for each key.
b) Use a loop and the items() method to print all keys and values.
c) Use the update() method to change the gpa to 4.0.
d) Use a loop and the keys() method to print all keys and values.
e) Add a key major with the value to the dictionary.
f) Use a loop and the values() method to print all values.
g) Use two different ways to delete gpa and age in the dictionary.
h) Print the updated dictionary."""

# a) Create a dictionary, stuInfo with the keys name, gpa, and age.
stuInfo = {'name': 'John Doe', 'gpa': 3.5, 'age': 20} #These are the keys and values of the dictionary.

# b) Use a loop and the items() method to print all keys and values.
print("Keys and Values:") #This will print the keys and values of the dictionary.
for key, value in stuInfo.items():
    print(f"{key}: {value}")

# c) Use the update() method to change the gpa to 4.0.
stuInfo.update({'gpa': 4.0}) #This will update the value of gpa to 4.0.

# d) Use a loop and the keys() method to print all keys and values.
print("\nKeys and Values (after update):") #This will print the keys and values of the dictionary after the update.
for key in stuInfo.keys(): #Will print the keys of the dictionary.
    print(f"{key}: {stuInfo[key]}")

# e) Add a key major with the value to the dictionary.
stuInfo['major'] = 'CSIS' #This will add a new key and value to the dictionary.
output = f"{stuInfo['name']}|{stuInfo['gpa']}|{stuInfo['age']}|{stuInfo['major']}" #This will create a string with the values of the dictionary.

# f) Use a loop and the values() method to print all values.
print("\nValues:")
for value in stuInfo.values(): #This will print the values of the dictionary.
    print(value)

# g) Use two different ways to delete gpa and age in the dictionary.

# First way: Use the del statement
del stuInfo['gpa']

# Second way: Use the pop() method
stuInfo.pop('age')

# h) Print the updated dictionary.
print("\nUpdated Dictionary:") #This will print the updated dictionary after deleting the keys.
print(output)
print(stuInfo)

