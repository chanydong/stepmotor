#test01.py

def fib(n):
	n = input()
	if n==0: return 0
	elif n==1: return 1
	else return fib(n-2)+fib(n-1)

for i in range(1:10):
	print(fib(i))

