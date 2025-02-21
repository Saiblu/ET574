# Variables
# Using f-string to format columns
# S. Trowbridge/J.Sun


fruit1 = "apples"
brand1 = "gala"
fruit2 = "pears"
brand2 = "european"
qty = 100

# align information into columns of specific width
# :10 indicates that the current field should have a column width of 10 characters
print("0123456789"*3)
print(f"{fruit1.title():10}{brand1.title()}")
print(f"{fruit2.upper():10}{brand2.upper()}")
print()

# two 10 character columns
# justify first column to the right, second column to the left
print("012345678901234567890123456789")
print(f"{fruit1:>10} {brand1:<10}")
print(f"{fruit2:>10} {brand2:<10}")
print()

# two 10 character columns
# justify first column to the left, second column to the right,
# third column to the center
print("012345678901234567890123456789")
print(f"{fruit1:<10}{brand1:>10}{qty:^10}")
print(f"{fruit2:<10}{brand2:>10}{10000:^10}")
print()
