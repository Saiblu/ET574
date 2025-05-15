# a & b) Request two integer inputs from the user
n1 = int(input("Enter the first number (n1): "))
n2 = int(input("Enter the second number (n2): "))

# c) If n1 < n2, use while loop to increment and print
if n1 < n2:
    while n1 <= n2:
        print(n1, end=' ')
        n1 += 1
    print()

# d) If n1 > n2, use for loop to decrement and print
elif n1 > n2:
    for num in range(n1, n2 - 1, -1):
        print(num, end=' ')
    print()

# e) If n1 == n2, print message
else:
    print("n1 = n2")
    