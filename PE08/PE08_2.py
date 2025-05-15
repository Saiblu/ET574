"""Convert the following two lists into one dictionary"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30] #This is a list of values.
print("Keys:", keys) #This will print the keys of the dictionary.
print("Values:", values) #This will print the values of the dictionary.
print("Keys:", keys) #This will print the first key and value of the dictionary.
print("Values:", values) #This will print the first key and value of the dictionary.
result = dict(zip(keys, values)) #This will create a dictionary from the two lists.
print(result)