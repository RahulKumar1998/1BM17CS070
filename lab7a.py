import sys
import os
f1=open("prime.txt","r")
f2=open("happy.txt","r")
s1=f1.read()
s2=f2.read()
l1=s1.split(", ")
l2=s2.split(", ")
"""print(l1)
print()
print(l2)"""
ls=[]
count=0
for i in l1:
	if i in l2 and i!="," and i!=" ":
		ls.append(i)
		count+=1
	
print(ls)
print("count: ",count)
f1.close()
f2.close()
