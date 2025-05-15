"""
Dictionary
a) Define a function createUser() with an arbitrary dictionary parameter.
This function returns a dictionary based upon input arguments.
b) Define a function printUser() with a parameter user which is a dictionary.
This function prints the contents of the dictionary user.
c) Create and print the user: John, age 43, job Programmer, Hobby Biking
d) Create and print the user: Sara, age 20, school QCC, major CSIS
Example Output
name: John
age: 43
job: Programmer
hobby: Biking
name: Sara
age: 24
school: QCC
major: CSIS
"""
# The code below implements the requirements specified in the prompt.
# Define the createUser function with an arbitrary dictionary parameter


def createUser(**kwargs):
    return kwargs


# Define the printUser function with a parameter user which is a dictionary
def printUser(user):
    for key, value in user.items():
        print(f"{key}: {value}")
        

# Create and print the user: John, age 43, job Programmer, Hobby Biking
user1 = createUser(name="John", age=43, job="Programmer", hobby="Biking")
printUser(user1)
print()  # Print a blank line for separation

# Create and print the user: Sara, age 20, school QCC, major CSIS
user2 = createUser(name="Sara", age=20, school="QCC", major="CSIS")
printUser(user2)

# The code above defines two functions: createUser and printUser. The createUser function takes arbitrary keyword arguments and returns them as a dictionary. The printUser function takes a dictionary as input and prints its contents in a formatted manner. The code then creates two user dictionaries (user1 and user2) with different attributes and prints their contents using the printUser function. The use of **kwargs allows for flexibility in the number of attributes that can be passed to the createUser function, making it versatile for different use cases. Overall, the code is well-structured and effectively demonstrates the functionality of the defined functions.
# The code above defines two functions: createUser and printUser. The createUser function takes arbitrary keyword arguments and returns them as a dictionary. The printUser function takes a dictionary as input and prints its contents in a formatted manner. The code then creates two user dictionaries (user1 and user2) with different attributes and prints their contents using the printUser function. The use of **kwargs allows for flexibility in the number of attributes that can be passed to the createUser function, making it versatile for different use cases. Overall, the code is well-structured and effectively demonstrates the functionality of the defined functions.
