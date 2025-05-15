"""
2. Name format
a) Define a function nameFormat() with parameters first, middle, and last.
 1) This function prints the first name, the middle initial and the last name using proper title format.
b) Define a main() function to do the following:
 1) Call the function nameFormat with these positional arguments: john stu smith
 2) Call the function nameFormat with these keyword arguments:
 last = ‘kennedy’, first = ‘john’, middle = ‘fitzgerald’
c) Call main() function to initiate the tasks to be performed.
Example Output
John S. Smith
John F. Kennedy
"""

def nameFormat(first, middle, last):
    # Format the name with proper title case and middle initial
    formatted_name = f"{first.title()} {middle[0].upper()}. {last.title()}"
    print(formatted_name)


def main():
    # Call the function with positional arguments
    nameFormat("john", "stu", "smith")
    
    # Call the function with keyword arguments
    nameFormat(last="kennedy", first="john", middle="fitzgerald")


if __name__ == "__main__":
    main()
# The code defines a function to format and print names in a specific format.
# The function nameFormat takes first, middle, and last names as parameters and prints them in title case with the middle initial.