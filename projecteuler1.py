#Find the sum of all the multiples of 3 or 5 below N.
t=eval(raw_input())
for k in range(t):
	n=eval(raw_input())
	n-=1
	n1=n/3   #no of multiples of 3 below n
	n2=n/5   #no of multiples of 5 below n
	n3=n/15  #no of multiples of 15 below n,,15 is lcm of 3 and 5 
	sum1=(3*n1*(n1+1))/2
	sum2=(5*n2*(n2+1))/2
	sum3=(15*n3*(n3+1))/2   #subtracts the nos which are added twice(multiples of both 3 and 5 e,g 30)
	sum=sum1+sum2-sum3
	print sum
