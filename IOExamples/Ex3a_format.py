# Variables
# Using format method
# S. Trowbridge/J. Sun

fruit1 = "apples"
fruit2 = "pears"

price1 = 12.3456789
price2 = 19.9595
qty = 100

# zero-based numbering system - Numbering begins with zero instead of one
# string format() method
# order of arguments is the same
print( "I want to buy {} and {}."
.format(fruit1, fruit2) )
print()

print( "I want to buy {} and {}."
.format(fruit2, fruit1) )
print()

# order of arguments is different (use indexes)
print( "I want to buy {1} and {0}.".format(fruit1, fruit2) )
print( "I want to buy {1} and {1}.".format(fruit1, fruit2) )
print()

# width of 10 spaces for first parameter and precision of 2 for second parameter
print("012345678901234567890123456789")
print( "{:10}{:1}{:.2f}".format(fruit1.title(), '$', price1) )
print( "{:10}{:1}{:.2f}".format(fruit2.title(), '$', price2) )
print()

# set width, justification and precision
print("012345678901234567890123456789")
print( "${0:<10.2f}{2:>10}{1:>10}".format(price1, qty, fruit1))
print( "${0:<10.2f}{2:>10}{1:>10}".format(price2, 1000, fruit2))
print()

print("012345678901234567890123456789")
print( "{:^10}${:<10.2f}{:>10}".format(fruit1, price1, qty) )
print( "{:^10}${:<10.2f}{:>10}".format('pineapple', price2, qty) )
print()
