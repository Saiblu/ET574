"""
2. Name format
a) Define a function nameFormat() with parameters first, middle, and last.
1) This function prints the first name, the middle initial and the last name using proper title format.
b) Define a main() function to do the following:
1) Call the function nameFormat with these positional arguments: john stu smith
2) Call the function nameFormat with these keyword arguments:
last = ‘kennedy’, first = ‘john’, middle = ‘fitzgerald’
c) Call main() function to initiate the tasks to be performed.
"""

def nameformat(first, middle, last):
    print(f"{first.title()} {middle[0].upper()}. {last.title()}")

def main():
    nameformat("john", "stu" , "smith")
    nameformat(first="john", middle="fitzgerald", last="kennedy")
main()