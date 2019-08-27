def divisors(n):
	for i in range(1,n+1):
		if n%i==0:
			print(i)

x=int(input("enter the number whose divisors you need to find?"))
divisors(x)
