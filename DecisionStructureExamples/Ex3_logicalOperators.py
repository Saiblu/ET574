# Decision Structure
# J. Sun

## Logical Operators
print('\nLogical Operators\n')

print("not True\t\t", not True)
print("True and False\t\t", True and False)
print("True or False\t\t", True or False)
print()

#Enables combining multiple relational operators
n = 4
answ = 'Y'
print('(a) (2 < n) and (n < 6)\n', (2 < n) and (n < 6) )
print('(b) (2 < n) or (n == 6)\n', (2 < n) or (n == 6) )
print('(c) not (n < 6)\n', not (n < 6))
print('(d) (answ == "Y") or (answ == "y")\n', (answ == "Y") or (answ == "y") )
print('(e) (answ == "Y") and (answ == "y")\n', (answ == "Y") and (answ == "y") )
print('(f) not (answ == "y")\n', not (answ == "y"))
print('(g) ((2 < n) and (n == 5+1)) or (answ == "No")\n',
           ((2 < n) and (n == 5+1)) or (answ == "No"))
print('(h) ((n == 2) and (n == 7)) or (answ == "Y")\n',
           ((n == 2) and (n == 7)) or (answ == "Y"))
print('(i) (n == 2) and ((n == 7) or (answ == "Y"))\n',
           (n == 2) and ((n == 7) or (answ == "Y")))
print()
