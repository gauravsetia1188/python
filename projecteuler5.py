def gcd(a,b):
	if a%b==0:
		return b;
	if b%a==0:
		return a;
	if a>b:
		return gcd(a%b,b);
	if b>a:
		return gcd(a,b%a);
 
t=eval(raw_input())
for k in range(t):
	n=eval(raw_input())
	ans=1
	c=2
	for i in range(n):
		if i==0:
			pass
		a=c*(i+1)
		b=gcd(c,i+1)
		c=a/b
	if n==1:
		print '1'
	else:
		print c
