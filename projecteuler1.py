t=eval(raw_input())
for k in range(t):
	n=eval(raw_input())
	n-=1
	n1=n/3
	n2=n/5
	n3=n/15
	sum1=(3*n1*(n1+1))/2
	sum2=(5*n2*(n2+1))/2
	sum3=(15*n3*(n3+1))/2
	sum=sum1+sum2-sum3
	print sum
