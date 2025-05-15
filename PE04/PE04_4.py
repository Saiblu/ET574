# Create/Make PE4_4.py to do the following:
# a) Create an empty list named grades.
# b) Add any five grades one at a time to grades.
# c) Print the current list.
# d) Compute the total of these grades using the indexing to reference each number in grades.
# e) Compute the average of these grades using the len () function.
# f) Print the average with a precision of two decimal places.
# g) Use two different methods to remove all failing grades (lower than 60) one at a time from the list.
# h) Print the updated list.
# i) Use the built-in functions, sum () and len () to compute the average with three decimal places and print
# the updated result in one statement.
grades= []
grades.append(85)
grades.append(90)
grades.append(45)
grades.append(76)
grades.append(50)

print("current list of grades:", grades)

total = grades[0] + grades[1] + grades[2] + grades[3] + grades[4]

average = total / len(grades)

print("Aeverage of grades: {:.2f}".format(average))

grades.remove(45)
del grades[grades.index(50)]

print("Updated list of grades:", grades)

new_average = sum(grades) / len(grades)
print("Updated average of grades: {:.3f}" .format(new_average))




