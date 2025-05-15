#A 
a = list(range(5))
print (a)

#B
b = []
for i in range (5):
    b.append (i)
print(b)

#C
x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))

#D
even_num = list(range(2, 11, 2))
print (min(x), max(x), sum(x))

#E
odd_num = [n for n in range(1, 10, 2)]
print(odd_num)

#F
cubes= [] # To make the list horizontial
for value in range (1, 11):
    cubes.append(value**3)
print(cubes)
print()

#G
cubes = [value**3 for value in range(1, 10)]
print(cubes)
print()
