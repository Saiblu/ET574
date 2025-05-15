# Decision Structure
# J. Sun

## Using ASCII value
print('\nASCII\n')

#chr(n) returns single-character of ASCII value n
letter = chr(65)
print(letter)
print(chr(97))
print()

# ord() returns ordinal value of its argument
symbol = ord('?')
print(symbol)
print(ord('0'), ord('#'), ord('%'))
print(ord('a') - ord('A'))
print()

#Concatenation can be used with chr to obtain string
print(chr(104) + chr(105))

#using the higer ASCII characters.
print("Today's temperature: 32" + chr(176) + "F")
print("1 " + chr(247) + " 2 = " + chr(189))
