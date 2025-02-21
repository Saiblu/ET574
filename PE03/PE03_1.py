print("012345678901234567890")
print('A'.rjust(5), 'B'.center(5), 'C'.ljust(5), sep = "")
#Output is A B C#
print("01234567890123456")
print("{0:^7}{1:4}{2:>6s}".format("one", "two", "three"))
print(f"{'one':^7}{'two':4}{'three':>6s}")
#Output is one, two, three#
n=1234
print("01234567890123456789")
print(f"{n:10}{n:^10}")
print("01234567890123456789")
print(f"{n:<10}{n:>10}")
print("01234567890123456789")
print(f"{n:10.3f}{n:10,.2f}{n}")
print("012345678901234567890123456789")
print(f"{n:10.2%}{n:12,.2%}")

q1= '''"If {0:s} dream it, {0:s} do it. - Walt Disney"'''
print(q1.format('you can'))
a = "One"
b = "Day"
q2 = f"\"{a} {b} or {b} {a}. You decide. Paulo Coelho\""
print(q2)