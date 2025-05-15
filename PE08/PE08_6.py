# a) Create three stuInfo dictionaries
stu1 = {'name': 'tom cat', 'gpa': 3.456} # This will create a dictionaries with the name and GPA of the students.
stu2 = {'name': 'jerry mouse', 'gpa': 4.0} 
stu3 = {'name': 'sponge bob', 'gpa': 3.99}

# b) Create a list stuClass, add all dictionaries to this list
stuClass = [stu1, stu2, stu3]

# Print the list
print("All students in the list:") # This will print the information of all students in the list.
print(stuClass)
print()

# c) Use a loop to print all students
print("All students information:") # This will print the information of all students in the list.
for idx, student in enumerate(stuClass, start=1):
    print(f"student {idx} {student}")
print()

# d) Use a loop to print all the GPA
print("All gpa information:") # This will print the GPA of all students in the list.
for i, student in enumerate(stuClass): # Use enumerate to get the index and student
    if i != len(stuClass) - 1:
        print(f"{student['gpa']}|", end="") # This will print the GPA of all students in the list, except the last one.
    else:
        print(f"{student['gpa']}")
print()

# e) Change the last student’s GPA to 4.0
stuClass[-1]['gpa'] = 4.0

# f) Add a new student info
new_student = {'name': 'john smith', 'gpa': 3.99} # This will create a new dictionary with the name and GPA of the new student.
stuClass.append(new_student) # This will add the new student to the list.

# g) Use a loop to print all names and GPA properly formatted
print("All the updated information:") # This will print the updated information of all students in the list.
for student in stuClass: # This will loop through all students in the list.
    print(f"{student['name'].title():<15}{student['gpa']:.2f}")
