# Variables
# Using f-strings
# S. Trowbridge/J. Sun

fruit1 = "apples"
fruit2 = "pears"
qty = 7

# f-strings are used to format string content
print(f"I want to buy {qty} " 
f"{fruit1} and {fruit2}.\n")
print(f"Hi my favorite number is {qty}!\n")

 # f-strings can be used upon variables
txt = f"Hi, do you want to buy {qty} {fruit1}?\n"
print(txt)

 # f-strings can span multiple lines if parenthesis are used
txt = (f"{fruit1.title()}"
f" and {fruit2} are delicious.\n")
print(txt)

txt = (f"{fruit1.title()} \
and {fruit2.title()} are delicious.\n")
print(txt)

shoppingList = f"I want to buy {qty} {fruit1} and {fruit2}.\n"
print(shoppingList)
#print(f"I want to buy {qty} {fruit1} and {fruit2}.\n")
print()
