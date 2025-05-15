"""
Lists, comprehensions, loops and slicing. Save it as PE5_3.py.
a) Create a list comprehension of multiples of 4 from 0 to 10 inclusive.
b) Print this list as displayed in the example output.
c) Create a second empty list.
d) Use a loop to insert all elements from the first list to the second list.
Before storing into the new list, divide each copied element by 2.
This results in a new list of all multiples of 2 from 0 to 10 inclusive.
e) Print the second list as displayed in the example output.
f) Use slicing to copy the second list to a new third list.
g) Use a loop to divide and store each element of the third list by 2.
This will result in a list of the numbers 0 to 10 inclusive.
h) Print the third list as displayed in the example output.
"""
multiples_of_4 = [n * 4 for n in range (0, 11)]

print("multiples of 4:", multiples_of_4)

multiples_of_2 = []
for num in multiples_of_4:
    multiples_of_2.append(num / 2)
print("multiples_of_2:", multiples_of_2)

numbers_0_to_10 = multiples_of_2[:]

for i in range(len(numbers_0_to_10)):
    numbers_0_to_10[i] /=2

print("numbers from 0 to 10:", numbers_0_to_10)
