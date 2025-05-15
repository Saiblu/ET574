"""
3. Name format
a) Define a function nameFormat() with parameter first, last and middle where middle is an optional parameter.
 If all three names are provided return: Last, First, M.
 If only first and last are provided return: Last, First
b) Define a main() function to do the following:
 1) Call the function with keyword arguments for the name: james bond
 2) Call the function with keyword arguments for the name: henry indiana jones
 3) Print the results of the function calls.
c) Call main() function to initiate the tasks to be performed.
"""

def nameFormat(first, last, middle=""):
    if middle: # If middle name is provided
        return f"{last}, {first} {middle[0].upper()}." # Format with middle initial
    else: # If only first and last names are provided
        return f"{last}, {first}" # Format without middle initial

def main(): # Call the function with keyword arguments for the name: james bond
    result1= nameFormat(first="James", last="Bond") # Call the function with keyword arguments for the name: henry indiana jones
    result2 = nameFormat(first="Henry", last="Jones", middle="Indiana") # Call the function with keyword arguments for the name: henry indiana jones
    print(result1) # Print the results of the function calls.
    print(result2) # Print the results of the function calls.

main() # Call main() function to initiate the tasks to be performed.