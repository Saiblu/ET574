# Write the codes and precisely produce the output format below. Save the code as PE4_3.py.
# a) Create a list called courses containing the names of your current courses.
# b) Print the list of courses.
# c) Use the len method to print “I am taking X courses” where X is the number of courses in the list.
# d) Using indexes to print the first and last item from the list.
# e) Using slicing to print the first four classes.
# f) Using slicing to print the last four classes.
# g) Using slicing to print the classes except for the first and last classes

courses= ["Python","English", "Linux", "Astromy"] #A
print(courses) #B
print(f'I am taking {len(courses)} courses') #C
print(courses[0]) #D1
print(courses[-1]) #D2
print(courses[:4]) #E
print(courses[-4:]) #F
print(courses[1:-1]) #G