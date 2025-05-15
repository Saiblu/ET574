# a) Request lower and upper bounds
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# b) Request increment value
incVal = int(input("Enter the increment value: "))

# c) Use while loop to print increments horizontally
print("Incremented values (horizontal):")
current = lower
while current <= upper:
    print(current, end=' ')
    current += incVal
print()  # For spacing

# d) Use while loop to vertically print values in increments
print("Values printed vertically using while loop:")
current = lower
while current <= upper:
    print(current)
    current += incVal

# e) Use for loop to vertically print values in increments
print("Values printed vertically using for loop:")
for value in range(lower, upper + 1, incVal):
    print(value)