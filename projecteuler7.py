# find nth prime no
#algorithm used sieve of eratothenes,prcomputation
from math import *
x=10005
j=0
prime=[1 for j in range(100000)]   #setting all no's in the list as true, precomputation
p=2
while p < int(floor(sqrt(x))):   #sieve of erastothenes
	if prime[p]==1:
		i=p*2
		while i<=x:
			prime[i]=0
			i+=p
	p+=1       
p=2
s=[]
while p<=x:      #storing all prime no's computed above in a separate list
	if prime[p]==1:
		s.append(p)
	p+=1
t=eval(raw_input())   #no of test cases
for k in range(t):
	n=eval(raw_input())
	print s[n-1]  #directly picking from the precomputed list in O(1) time complexity
