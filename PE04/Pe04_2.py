n=[]
n.extend([2,4])
print(n)
n.insert(0,0)
n.insert(1,1)
print("n before insert #3:" , n)
n.insert(3,3)
print(n)
n.insert(5,5)
print(n)
n.append(5)
n.remove(0)

firstnum = n.pop(1)
print ("first number removed", firstnum)
print(n)
secondnum= n.pop(2)
print ("second number reomved", secondnum)
print(n)
# remember immutable and mutuable, will be noticable later on in the course. 
print (firstnum + secondnum)
n[0]= 100
n[-1]=9.9
print(n)

newNum = list(n)
print(newNum)
n.clear()
print (n)
print(newNum)