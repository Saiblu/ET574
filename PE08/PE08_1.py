NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI":0.47}
print((NY['QS'])) #Part A 
print(NY.get('QS'))
print() #Output will be 2.25

print(NY.get("LI", "Not in")) #Part B, same with this as well.
print(NY.get("SI", "absent")) #Sine it isn't in the dictionary, it will return "absent"
print(NY.setdefault('SI', 0.48))
print()

print('LI' in NY) #Part C, this will return False since LI isn't in the dictionary.
print('MN' not in NY) #Part C, this will return False since LI is not in the dictionary, so the output will be False.
print()

print(len(NY), min(NY), max(NY)) #Part D, this will return the length of the dictionary, the minimum value and the maximum value.
print(len(NY.items()), #This will return the length of the dictionary items.
max(NY.keys()), min(NY.values())) # This will return the maximum key and the minimum value of the dictionary.
print()

print(round(NY['QS'])) #Part E, this will round the value of QS to the nearest integer.
NY['QS'] += .3 #This will add 0.3 to the value of QS.
print(round(NY['QS'], 1)) #This will round the value of QS to 1 decimal place.