"""
Implement the following to create a list and produce the multiplication table. Save it as PE5_5.py.
a) Request an integer input range.
b) Implement a list of the numbers 1 to range inclusive.
c) Request an integer input number.
d) Use a loop upon this list to compute and print the multiplication table of the input number.
Input text can be any content. Just make sure to precisely match the output format below    
"""
#A 
num_range = int(input("Enter the range for the multiplication table: "))

numbers = list(range(1, num_range + 1))

multiplier = int(input("enter the number of multiply:"))

print (f"\nMultiplication table of {multiplier}:")
for num in numbers:
    print(f"{multiplier} x {num} = {multiplier * num}")