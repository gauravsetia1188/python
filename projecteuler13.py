#Work out the first ten digits of the sum of N 50-digit numbers.
n=eval(raw_input())
d=[]
for k in range(n):
	d.append(int(raw_input()))
p=sum(d)
s=str(p)
print s[0:10]
