import sys

def search(list,key):
	print("The list is->",ls)	
	if key in list:
		return True
	else:
		return False


ls=[]
n=int(input("Enter no of items in list"))
print("Enter the list in asc order")
for i in range(n):
	x=int(input())
	ls.append(x)

b=int(input("enter number to be searched"))
print(search(ls,b))
