# Decision Structure
# J. Sun

## Boolean values
print('\nBoolean values\n')

#Objects True and False are said to have Boolean data type
x = 2
y = 3
var = (x < y)
print("2 < 3", var)

x = 5
var = (x < y)
print("5 < 3", var)
print("When x = 5, x>10 and x<=20\n", x>10 and x<=20)

x = 12
print("When x = 12, x>10 and x<=20\n", x>10 and x<=20)
print("When x = 12, 10<x<=20\n", 10<x<=20)

print("When x = 12, x<=10 or x>20\n", x<=10 or x>20)
print("When x = 12, not(10<x<=20)\n", not(10<x<=20))
print()

#Lists or tuples can sometimes be used to simplify long compound conditions
state = "NY"
expression = (state == "MD") or (state =="VA") or (state =="WV") or (state =="DE")
print(state, expression)
print(state, state in ["MD", "VA", "WV", "DE"])
print()
