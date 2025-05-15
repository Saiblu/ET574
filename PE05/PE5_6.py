# Identifying the errors in these said codes.

#A (Original)
""""
fruits = ["apple", "banana", "cherry"]
for item in fruits
print(item)
"""
# Fixed issue
fruits = ["apple", "banana", "cherry"]
for item in fruits: # there were no ":"
    print(item) #Space or tab the print.

#B (original)
"""
for i in range(1, 4):
    print(i + '\t' + 2**i) #missing the string for i, as well 
"""
#B (Fixed)
for i in range (1, 4):
    print(str(i) + '\t' + str(2**i)) 

#C
for j in range (1, 6, -1): #which means it is counting backwards
    print(j)

#C (fixed)
for j in range(1, 6, 1): #ranges 1 and 6
    print(j)
    
#D (Original)
""""
letters = ['a', 'b', 'c']
for letter in letters:
letter = letter.upper() converting each letter to a uppercase and stoes it in the list.
print(letters)
"""

#D (Fixed)
letters = ['a', 'b', 'c']
for i in range(len(letters)):
    letters[i] = letters[i].upper()
print(letters)

#E (original)
"""
fruits = ('apple', 'banana', 'cherry')
print(fruits)
fruits[0] = 'orange' this is a typo, doesn't support the item itself that has been assigned.
fruits.append('pineapple') does not have a attribute 'append'
print(fruits)
"""

#E (fixed)
fruits = ('apple', 'banana', 'cherry')

fruits_list = list(fruits) # convert tuple to list

fruits_list[0] = 'orange' # modifying the first element 

fruits_list.append('pineapple') # append to add a new item

fruits = tuple(fruits_list) # Converts bback t tuple

print(fruits)