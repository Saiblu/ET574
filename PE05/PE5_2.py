"""
List slicing. Save it as PE5_2.py.
a) Use a list comprehension to generate a list of all even numbers from 0 to 100 inclusive.
b) Use slicing to print the first five even numbers in the list.
c) Use slicing to print the last five even numbers in the list.
d) Use slicing to print all list numbers between 20 and 30 inclusive
"""
#A
even_num= [n for n in range(0, 101, 2)]

#B
print("first five even number:", even_num[:5])

#C
print("Last five even number:", even_num[-5:])

#D
print("Numbers between 20 and 30:", even_num[10:16])