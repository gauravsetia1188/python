#What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
#e.g 2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
def gcd(a,b):
	if a%b==0:
		return b;   #gcd using recursion
	if b%a==0:
		return a;
	if a>b:
		return gcd(a%b,b);
	if b>a:
		return gcd(a,b%a);
 
t=eval(raw_input())   #logic:we need to find lowest common multiple of all the numbers uptil n
for k in range(t):
	n=eval(raw_input())
	ans=1
	c=2
	for i in range(n):
		if i==0:
			pass
		a=c*(i+1)
		b=gcd(c,i+1)    #formula for lcm=a*b/gcd(a,b)
		c=a/b
	if n==1:    #corner case
		print '1'
	else:
		print c
