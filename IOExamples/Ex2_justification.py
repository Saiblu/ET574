# Variables
# J. Sun

## Demonstrate justificarion of output.
print("01234567")
print("Hi".center(8))
print("01234567")
print("Hi".ljust(8))
print("01234567")
print("Hi".rjust(8))
print()


print("0123456789"*3)
print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
print('1'.center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")
print('2'.center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep="")
print('3'.center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep="")
print()

print("0123456789"*3)
print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
print("{0:^5n}{1:<20s}{2:>3n}".format(2, "Hank Aaron", 755))
print("{0:^5n}{1:<20s}{2:>3n}".format(3, "Babe Ruth", 714))
print()
