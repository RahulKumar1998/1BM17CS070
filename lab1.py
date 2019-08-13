import sys
def fibonacci(n):
    ls=['1']
    ls.clear()
    ls.append(0)
    ls.append(1)
    for i in range(2,n):
        ls.append(ls[i-1]+ls[i-2])

    print("fibonacci numbers are: ")
    print(ls)

x=int(input("enter how many fibonacci numbers you want?"))
fibonacci(x)