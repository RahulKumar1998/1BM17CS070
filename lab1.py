import sys

ls1=[]
ls2=[]
n=int(input("Enter how many numbers you want in the list?"))

for i in range(0,n):
	x=int(input("enter the number"))
 	ls1.append(x)

for y in ls1:
	if(y%2==0):
        	ls2.append(y)

print(ls2)
