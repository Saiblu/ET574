"""
Write an if-elif-else chain that determines a person’s stage of life.
a) Set your age for the variable age.
b) If the age is less than 0, print an error message, invalid age.
c) If the age is less than 2 years old, print a message, you’re a baby.
d) If the age is at least 2 years old but less than 4, print a message, you’re a toddler.
e) If the age is at least 4 years old but less than 13, print a message, you’re a kid.
f) If the age is at least 13 years old but less than 20, print a message, you’re a teenager.
g) If the age is at least 20 years old but less than 65, print a message, you’re an adult.
h) If the age is 65 or older, print a message, you’re an elder.
Example Output
Age = 20
You’re an adult.
"""

age= int(input("Enter your age:"))

if age <0:
    print("How is that possible? There's no way.")
elif age < 2:
    print("You're a baby.")
elif age < 4:
    print("You're a toddler.")
elif age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're an elder.")