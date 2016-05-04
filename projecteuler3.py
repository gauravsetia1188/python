#largest prime factor of a given no n
# 2conditions are needed to be checked :1-no is prime 2-it is a factor of n
from math import *
t=eval(raw_input())
 
def isprime(i):
	if i==2 or i==3:
		return 1
	elif i==1 or i%2==0:
		return 0
	else:
		p=3			
		while p<ceil(sqrt(i)):   #prime checking
			if i%p==0:
				return 0
			p+=2
		return 1
 
 
for k in range(t):
	n=eval(raw_input())
	i=3   #started from 3 an is incremented by 2 so as to avoid even no prime checking as 2 is the only even prime no
	maxi=0
	while i<=n:    # for all i less than n it checks whether i is a factor of n and if it is then it checks whether it is prime
		if n%i==0:
			x=isprime(i)
			if x==1:
				maxi=i
		i+=2
	print maxi   #maxi is largest prime factor
