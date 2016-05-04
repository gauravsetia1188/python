#Find the sum of all the primes not greater than given N
#algorithm: sieve of erastothenes,precomputation
from math import *
x=10005
j=0
prime=[1 for j in range(100000)]
p=2
while p < int(floor(sqrt(x))):   #precomputation of prime nos
	if prime[p]==1:
		i=p*2
		while i<=x:
			prime[i]=0
			i+=p
	p+=1
p=2
s=[]   #list s stores all computed prime no's
while p<=x:
	if prime[p]==1:
		s.append(p)
	p+=1
t=eval(raw_input())
for k in range(t):
	n=eval(raw_input())
	sum=0
	for i in range(len(s)):
		if s[i]>n:
			break
		sum=sum+s[i]   #computing the sum
	if n==1:
		print '0'  #corner case
	else:
		print sum
