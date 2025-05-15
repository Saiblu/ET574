""" Requests a name from the user. Save the code as PE4_5.py.
a) Use Input() to prompt and request a full name.
b) After the user types the full name and presses the Enter (or Return) key,
display the first name and last name in two separate lines """

full_name = input ('Enter your full name')

names= full_name.split()

if len(names) >= 2:
    first_name = names[0]
    last_name = names[-1]
    
    print('first name:')