# Variables
# J. Sun
# Enhanced output can be produced by the print function
# with optional arguments, sep and end

## Demonstrate use of print argument sep
# Print function uses string consisting of one space character as separator
print("Hello", "World!")        # default sep vaule = " "
print("Hello", "World!", sep = " ")

# Optionally change the separator to any string we like with the sep argument
print("Hello", "World!", sep = "")
print("Hello", "World!", sep ="**")
print("1", "two", "3", sep = " ")
print("Name: Apple", "Brand: Gala",
"Color: Red", "B-code: 123456", sep ="\t")
print("Hello", "Python", "World!", sep ="\n")
print("Hello","\n", "Python","\n", "World!", sep="")
print()


## Demonstrate use of print argument end
# Print statement ends by executing a newline operation.
print("Hello")              # default end vaule = "\n"
print("World!")
print("Hello", end = "\n")
print("World!", end = '\n')

# Optionally change the ending operation with the end argument
print("Hello", end = " ")
print("World!")
print("Hello", end = "*")
print("World!")
print("Hello", end = " Python ")
print("World!")
print("Hello", end = "")
print("World!")
print()


## Demonstrate use of escape sequences and expandtabs()
# expandtabs() controls the number of position between horizontal tab stops
print("01234567890123456")
print("a\tb\tc")            # default \t vaule = 8 spaces
print("a\tb\tc".expandtabs(8))
print("a\tb\tc".expandtabs(5))

print("01234567890123456789")
print("Home,\tSweet\tHome!".expandtabs(5))

print("012345678901234567890")
print("123\t456\n789\tabc".expandtabs(10))
print()
