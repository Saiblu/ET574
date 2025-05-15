"""
5. Dictionary
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

def createUser(**kwargs):  # Accepts arbitrary keyword arguments as a dictionary
    return kwargs  # Returns the dictionary created from the keyword arguments


def printUser(user):  # Accepts a dictionary as a parameter
    for key, value in user.items():  # Iterate through each key-value pair in the dictionary
        print(f"{key}: {value}")  # Print the key and its corresponding value


def main():
    # Create and print the user: John, age 43, job Programmer, Hobby Biking
    user1 = createUser(name="John", age=43, job="Programmer", hobby="Biking")
    printUser(user1)  # Print the user information

    # Create and print the user: Sara, age 20, school QCC, major CSIS
    user2 = createUser(name="Sara", age=20, school="QCC", major="CSIS")
    printUser(user2)  # Print the user information


if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call main() function to initiate the tasks to be performed.
# The code defines functions to create and print user information using dictionaries.
# The createUser function accepts arbitrary keyword arguments and returns them as a dictionary.
# The printUser function takes a dictionary and prints its contents in a formatted manner.
# The main function demonstrates the usage of these functions by creating and printing two user profiles.
# The output displays the user information in a structured format, showing the keys and their corresponding values.