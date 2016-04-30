from math import *
t=eval(raw_input())
 
def isprime(i):
	if i==2 or i==3:
		return 1
	elif i==1 or i%2==0:
		return 0
	else:
		p=3
		while p<ceil(sqrt(i)):
			if i%p==0:
				return 0
			p+=2
		return 1
 
 
for k in range(t):
	n=eval(raw_input())
	i=3
	maxi=0
	while i<=n:
		if n%i==0:
			x=isprime(i)
			if x==1:
				maxi=i
		i+=2
	print maxi
