#Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.
t=eval(raw_input())
d=[i**2 for i in range(10001)]   #initialising the list
for k in range(t):
	n=eval(raw_input())
	sums=(n*(n+1))/2
	sums1=sums**2 
	r=n+1
	sqsum=0
	for p in range(n+1):
		sqsum+=d[p]
	print (sums1)-sqsum
