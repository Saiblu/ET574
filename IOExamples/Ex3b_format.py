# Variables
# Using format method
# S. Trowbridge/J.Sun

item1 = "Apple"
price1 = 5.99
barcode1 = "14235643"

item2 = "Pears"
price2 = 6.99
barcode2 = "52345123"

tax = .0875

# combination of width, precision, justfication and calculations
print( "{0:8}{1:1}{2:10}{3:1}{4:<11}{5:1}{6:<5.2f}"
.format(item1, "#", barcode1, "$", price1, "$", price1*tax ) )
print()

# combination of width, precision, justfication and calculations
print( "{0:8}{1:1}{2:10}{3:1}{4:<11}{5:1}{6:<5.2f}"
.format(item2, "#", barcode2, "$", price2, "$", price2*tax ) )
print()
