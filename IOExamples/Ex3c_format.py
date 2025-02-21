# Variables
# J. Sun

## Demonstrate use of the format method.
print("0123456789")
print("{0:10d}".format(12345678))
print("{0:10,d}".format(12345678))
print("{0:10.2f}".format(1234.5678))
print("{0:10,.2f}".format(1234.5678))
print("{0:10,.3f}".format(1234.5678))
print("{0:10.2%}".format(12.345678))
print("{0:10,.3%}".format(12.345678))
print()

print("---Use format to control strings, numbers and calculations ")
print("The area of {0:s} is {1:,d} square miles.".format("Texas", 268820))
str1 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str1.format("Texas", 26448000 / 309000000))
print()

print("---Use f-string to control strings, numbers and calculations ")
print(f"The area of Texas is {268820} square miles.")
print(f"The population of Texas is {26448000/309000000:.2%} of the U.S. population.")
print()

state = "Texas"
area = 268820
population = 26448000/309000000

print("---Variables/f-string to control strings, numbers and calculations ")
print(f"The area of {state} is {area} square miles.")
print(f"The population of {state} is {population:.2%} of the U.S. population.")
print()

print("---Variables/format to control strings, numbers and calculations ")
print("The area of {0:s} is {1:.2%} square miles.".format(state, area))
str1 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str1.format(state, population))
