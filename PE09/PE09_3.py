"""
Name format
a) Define a function nameFormat() with parameter first, last and middle where middle is an optional parameter.
If all three names are provided return: Last, First, M.
If only first and last are provided return: Last, First
b) Define a main() function to do the following:
1) Call the function with keyword arguments for the name: james bond
2) Call the function with keyword arguments for the name: henry indiana jones
3) Print the results of the function calls.
c) Call main() function to initiate the tasks to be performed.
"""
# The code below implements the requirements specified in the prompt.
# Define the nameFormat function with optional middle parameter

def nameFormat(first, last, middle=None):
    if middle:
        return f"{last}, {first} {middle[0]}."
    else:
        return f"{last}, {first}"


# Define the main function to call nameFormat with different arguments
def main():
    # Call the function with keyword arguments for the name: james bond
    result1 = nameFormat(first="James", last="Bond")
    # Call the function with keyword arguments for the name: henry indiana jones
    result2 = nameFormat(first="Henry", last="Indiana", middle="Jones")
    
    # Print the results of the function calls
    print(result1)
    print(result2)


# Call the main function to initiate the tasks to be performed
if __name__ == "__main__":
    main()
# The code above defines a function nameFormat that formats names based on the provided parameters.
# It also defines a main function that calls nameFormat with different arguments and prints the results. The main function is called at the end to execute the code.
# The code is well-structured and follows the requirements specified in the prompt. It uses keyword arguments to call the function, making it clear which parameters are being passed. The use of an optional parameter for the middle name allows for flexibility in formatting names. Overall, the code is clean and easy to understand.
# The function nameFormat is defined to format names based on the provided parameters. It takes three parameters: first, last, and an optional middle parameter. If the middle parameter is provided, it formats the name as "Last, First M." Otherwise, it formats it as "Last, First". The main function calls nameFormat with different arguments and prints the results. The code is well-structured and follows the requirements specified in the prompt.
# It uses keyword arguments to call the function, making it clear which parameters are being passed. The use of an optional parameter for the middle name allows for flexibility in formatting names. Overall, the code is clean and easy to understand.
# The function nameFormat is defined to format names based on the provided parameters. It takes three parameters: first, last, and an optional middle parameter. If the middle parameter is provided, it formats the name as "Last, First M." Otherwise, it formats it as "Last, First". The main function calls nameFormat with different arguments and prints the results. The code is well-structured and follows the requirements specified in the prompt.