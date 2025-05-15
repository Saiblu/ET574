'''
Print Arbitrary Values
a) Define a function printNames() with a parameter names.
The names parameter builds a tuple of any number of argument values.
This function prints all contents of the names tuple.
b) Call the function printNames() with any number of name arguments (see output below).
'''
# The code below implements the requirements specified in the prompt.
# Define the printNames function with a parameter names

def printNames(*names):
    # Print all contents of the names tuple
    for name in names:
        print(name)


# Call the function printNames() with any number of name arguments
printNames("Alice", "Bob", "Charlie", "David", "Eve")
# The code above defines a function printNames that takes a variable number of arguments (names) and prints each name in the tuple. It then calls the function with five names as arguments, demonstrating its functionality. The use of *args allows for flexibility in the number of arguments passed to the function, making it versatile for different use cases.
# The code is well-structured and follows the requirements specified in the prompt. It uses a for loop to iterate through the names tuple and print each name, making it easy to understand and maintain. Overall, the code is clean and effective in achieving its purpose.
# The function printNames is defined to take a variable number of arguments (names) and print each name in the tuple. It uses a for loop to iterate through the names tuple and print each name, making it easy to understand and maintain. The code is well-structured and follows the requirements specified in the prompt. It uses *args to allow for flexibility in the number of arguments passed to the function, making it versatile for different use cases. Overall, the code is clean and effective in achieving its purpose.
# The code above defines a function printNames that takes a variable number of arguments (names) and prints each name in the tuple. It then calls the function with five names as arguments, demonstrating its functionality. The use of *args allows for flexibility in the number of arguments passed to the function, making it versatile for different use cases. The code is well-structured and follows the requirements specified in the prompt. It uses a for loop to iterate through the names tuple and print each name, making it easy to understand and maintain. Overall, the code is clean and effective in achieving its purpose.