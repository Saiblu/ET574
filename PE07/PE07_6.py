import random

# a) Request an integer input for the number of grades or what it can be determined in general. 
num_grades = int(input("Enter the number of grades in the list: "))

# b) Using a loop generater to from 1-100.
grades = []
i = 0
while i < num_grades:
    grades.append(random.randint(1, 100))
    i += 1

# c) Request a user input for the passing grade
passing_grade = int(input("Enter the passing grade: "))

# d) Use a loop to store all the passing grades into a new list
passGrades = []
i = 0
while i < len(grades):
    if grades[i] >= passing_grade:
        passGrades.append(grades[i])
    i += 1

# e) Print all the lists
print("Updated List:", passGrades)
print("Original List:", grades)