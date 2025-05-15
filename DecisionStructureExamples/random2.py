x = int(input('Type a number:'))

if (x < 0):
    print( 'negative')
else:
    if (x == 0):
        print('zero')
    else:
        print('positive')
        
cars= ['bmw', 'Bmw' , 'Audi', 'honda' ]
old_car= input('enter the car you desire')

if old_car in cars:
    index = cars.index(old_car)    
    cars[index] = cars
else:
    print("sorry amigo, that's not on the list. Maybe you should gamble your life svings instead. :)")

print(cars)

x = int(input('type the value for:'))


n = 6
if n > 5 and n < 9 :
    print("Yes")
else:
    print("No")