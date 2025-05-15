# Decision Structure
# J. Sun

## Relational Operators
print('\nRelational Operators\n')

#An int can be compared to a float.
print ("1 == 1.0\t\t", 1 == 1.0)
print("9 == 9.9\t\t", 9 == 9.9)
print()

PI = 3.14
print('PI != "PI"\t\t', PI != "PI")
print()

print('"123" == 123\t\t', "123" == 123 )
print('123 == [123, ]\t\t', 123 == [123,])
print()

#Relational operators can be applied to lists or tuples
str = "abc"
tup = ('a', 'b', 'c')
lst = ['a', 'b', 'c']
print('str is not tup\t\t', str is not tup )
print( "lst is tup\t\t", lst is tup)
print("tup[0] == lst[0]\t", tup[0][0] == lst[0])
print("tup[0] == str[0]\t", tup[0][0] == str[0])
print()

# same size, look for the the larger one
print("[3, 5] == [3,7]\n", [3, 5] == [3, 7])
# same value with different size, look for the longer one
print("[3, 5] < [3, 5, 6]\n", [3, 5] < [3, 5, 6])
#same size, look for the the first larger one
print("[3, 5, 7] <= [3, 7, 2]\n", [3, 5, 7] <= [3, 7, 2])
#look for the first larger value, string use ascii of the first letter
print('[7, "three" 5] < [7, "two", 2]\n',
[7, "three", 5] < [7, "two", 2])
print()
