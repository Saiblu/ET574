"""
1 - 12 evaluate the numeric expression without the computer, and then use Python to check your answer.
1) 2+3*4 4) (3+4)*5 7) 7//3
10) 14//4*4
2) 1-7**2 5) (5%3)*4 8) 14%4 11) 5//2+2
3) 1//2**3
6) (-2)**(-2) 9) 1+7%4 12) 5%5*5


"""
print (2+3*4)
print (1-7**2)
print (1//2**3)
print ((3+4)*5)
print ((5%3)*4)
print ((-2)**(-2))
print (7//3)
print (14%4)
print (1+4%4)
print (5//2+2)
print (5%5*5)

#question 13-18
#13. NewYear.sales is invalid because of the "." is not used in variable name
#14. room&color the "&" is also not allowed as a variable name.
#15. TorF_1040. Yes this is considered a variable, because it contains, letters and letters.
#16. 311Hotline isn't allowed because it starts with a number which isn't allowed.
#17. expense# the symble "#" isn't allowed as a variable name.
#18 Income 101 is invalid due to the fact there is a space in between which can not be used as a variable.
cost= 10
sum = 20
product =50
num = 5
rate = 2
total = 100
quotient = 9

cost += 5
sum *=  rate
product /=10
cost //= num
total -= cost
quotient %= rate

print("cost:", cost)
print("sum:", sum)
print("product:", product)
print("cost (after //=num):", cost)
print("total:", total)
print("quotient:", quotient)

a = 5
b = 3

print(int(-a / b))
print(round(a / b , 2))
print(abs(b - a))
