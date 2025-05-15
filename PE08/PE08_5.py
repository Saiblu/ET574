""" 5. Displays a rank in the defined dictionary.
a) Create a dictionary, rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
b) Request a user input for a number of years.
c) Print the value of the matching key in the dictionary.
d) Print the error message if input is invalid."""

# a) Create a dictionary
rank = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"} # This is a dictionary with keys and values.

# b) Request a user input for a number of years
try:
    years = int(input("Enter the number of years (1-4): ")) # This will request a user input for a number of years.

    # c) Print the value of the matching key in the dictionary
    if years in rank:
        print(f"Rank: {rank[years]}")
    else:
        # d) Print the error message if input is invalid
        print("Error: Invalid input. Please enter a number between 1 and 4.")
except ValueError:
    print("Error: Please enter a valid integer.")