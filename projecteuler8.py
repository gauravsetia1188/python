t=eval(raw_input())
for k in range(t):
	n,k=map(int,raw_input().split(' '))
	d=raw_input()
	s=list(d)
	product=1
	maxproduct=0
	for i in range(n-k+1):
		j=i
		product=1
		r=k
		while r>0:
			product=product*int(s[j])
			r-=1
			j+=1
		if product>maxproduct:
			maxproduct=product
	print maxproduct
