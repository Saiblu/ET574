"""
6. Averaging
a) Define a function average() with a parameter grades that can accept an arbitrary number of integer values.
 This function returns the average of all values.
b) Define a main() function to do the following:
 1) Call the average() function with the following arguments: 95,87,83,74
 2) Create two random integers, x and y. x is from range -100 to 0, and y is range from 0 to 100 inclusively.
 3) Call the average() function with x and y.
 4) Print al the results with the average computed to two decimal places.
c) Call main() function to initiate the tasks to be performed.
Example Output
Average of 95,87,83,74: 84.75
Average of any two random numbers, -7, 66: 29.50
"""

import random
from typing import Tuple, Union

def average(*grades: Union[int, float]) -> float:
    """Calculate the average of given grades.

    Args:
        *grades: Arbitrary number of integer or float values representing grades.

    Returns:
        float: The average of the grades.
    """
    if not grades:  # Check if no grades are provided
        return 0.0  # Return 0.0 if no grades are given

    total = sum(grades)  # Calculate the sum of all grades
    count = len(grades)  # Count the number of grades
    return total / count  # Return the average


def main() -> None:
    """Main function to demonstrate the average calculation."""
    # Call the average() function with specific grades
    avg1 = average(95, 87, 83, 74)
    print(f"Average of 95, 87, 83, 74: {avg1:.2f}")  # Print the average with two decimal places

    # Generate two random integers x and y
    x = random.randint(-100, 0)  # Random integer from -100 to 0
    y = random.randint(0, 100)   # Random integer from 0 to 100

    # Call the average() function with x and y
    avg2 = average(x, y)
    print(f"Average of any two random numbers, {x}, {y}: {avg2:.2f}")  # Print the average with two decimal places


if __name__ == "__main__":
    main()  # Call the main() function to initiate the tasks to be performed.
# The code defines a function to calculate the average of an arbitrary number of grades and demonstrates its usage with specific and random values.
# The average function takes a variable number of arguments, calculates the sum and count, and returns the average.
# The main function calls the average function with specific grades and two random integers, printing the results formatted to two decimal places.
# The random integers are generated within specified ranges, and the results are displayed in a user-friendly format.
# The code uses type hints to indicate that the average function can accept integers or floats and returns a float.