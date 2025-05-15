a,b,c = 2,3,0 
print(a ** b == b ** a) #Part A. Outcome is False.
print(a < b or b < a) #Part B. Outcome is True

animals= 'dog', 'cat', 'mouse' 
mobile = 'train'

print('dog' > 'cat' + 'mouse') #Part C. Output is True
print('Car' < 'Train') #Part D. Output is True.

print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b))) #Part E. Output is False.
print(not ((a < b) and (a < (b + a)))) #Part G. Outcome is False.
print("small" > "large" and (not c )) #Part H. Outcome is True.
print(isinstance(c, int)) #Part I. Outcome is True. 
print(isinstance(3.14, float)) #Part J. Outcome is True.

if (a < b < c): #Part K. Outcome will be 0.
    b = c + a
else:
    b = c * a
print(b)

if ('A' in 'apple'): #Part L. Outcome is 'Oops, not there' might be because there isn't a variable set for 'A' and could it be because it's case sensitive?
    print("A as apple." )
else:
    print('Oops, not there.')

# different variation of replacing 'A' with 'a' 
if ('a' in 'apple'): #still using the same if statement but changing within the parentheses. 
    print('a as in apple')
else:
    print('Oops, not there')

x = 6 #Part M. Outcome is positive, 
if (x < 0):
    print('negative')
else:
    if (x == 0):
        print('zero')
    else:
        print('positive')

n = 1 #Part N. Outcome will be 
if n <= 9: #
    print ("Less than ten.") 
elif n == 1:
    print("Equal to one.")

let = input("Enter A, B or C: \n") #Part O. 
let = let.upper()

if (let == 'A'):
    print('\nA, my name is Alice.')
elif (let == 'B'):
    print('\nTo be, or not to be.')
elif (let == 'C'):
    print('\nOh, say, can you see.')
else:
    print('\nInvalid letter.')