# a & b) Creating a list operator.
numbers = []

# c) Sentinel loop: keep asking for input until the user enters 0
while True:
    user_input = input("Enter a number or 0 to stop: ")
    number = float(user_input)
    if number == 0:
        break
    numbers.append(number)

# d) Print the results
print("List of numbers:", numbers)
print("Sum:", sum(numbers))

# Avoid division by zero in case the list is empty
if len(numbers) > 0:
    print("Average:", sum(numbers) / len(numbers))
else:
    print("Average: 0")