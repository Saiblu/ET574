"""
 Print Arbitrary Values
a) Define a function printNames() with a parameter names.
 The names parameter builds a tuple of any number of argument values.
 This function prints all contents of the names tuple.
b) Call the function printNames() with any number of name arguments (see output below).
Example Output
Ann Bianca Coco Dora Emily
"""
# 1. Print Arbitrary Values
def printNames(*names):  # Accepts any number of arguments as a tuple
    for name in names:  # Iterate through each name in the tuple
        print(name, end=' ')  # Print each name followed by a space ' ' which indicates a space between names.
    print()  # Print a newline at the end

# The function printNames() takes a variable number of arguments and prints them in a single line separated by spaces.
def main():
    # Call the function with any number of name arguments
    printNames("Ann", "Bianca", "Coco", "Dora", "Emily")  # Example call with multiple names

if __name__ == "__main__": # # Check if the script is being run directly
    main()  # Call main() function to initiate the tasks to be performed.
# The code defines a function to print an arbitrary number of names passed as arguments.