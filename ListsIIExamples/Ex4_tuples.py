# Lists II & For loops & Tuples
# J. Sun

## tuples: ordered sequences of items
print('\nTuples\n')
t = 5, 7, 6, 2
print(t)
print(len(t), max(t), min(t))
print(t[0], t[-1], t[:2])

# tuple slicing:
print(t[-7:7])
print(t[-7:2])
#del t[1:4]  #TypeError: 'tuple' does not support item delection
del t
#print(t)    #NameError: name 't' is not defined

# out of bounds error
#print(t[7])
#print(t[-7])

# creating new tuples
a = 1, 2, 3
b = ('a', 'b', 'c')
c = a + b
t = (a, b, c)
print(t)

tNums = tuple(range(6))
print(tNums[:3])

# use for loop to display items in tuples
for n in tNums[:3]:
    print(n, end = " | ")
print()
