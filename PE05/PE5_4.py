"""
Implement the code that replaces the name of each month with its three-letter abbreviation. Save it as
PE5_4.py.
a) Create a list below and print it out.
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
'december']
b) Use a for loop to store each month with its first three-letter abbreviation into a new list.
c) Print the value of each month in uppercase separated by a ‘|’ in a row as displayed in the example output.
d) Print the new list.
"""
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
          'august', 'september', 'october', 'november', 'december']
print("original list of months:", months)

months_abbreviations = []
for month in months:
    months_abbreviations.append(month[:3])

print("|".join(month.upper() for month in months_abbreviations))

print("abbreviated months list:", months_abbreviations)