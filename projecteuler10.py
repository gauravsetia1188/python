from math import *
x=10005
j=0
prime=[1 for j in range(100000)]
p=2
while p < int(floor(sqrt(x))):
	if prime[p]==1:
		i=p*2
		while i<=x:
			prime[i]=0
			i+=p
	p+=1
p=2
s=[]
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
		sum=sum+s[i]
	if n==1:
		print '0'
	else:
		print sum
