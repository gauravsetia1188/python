#Find the greatest product of K consecutive digits in the N digit number.
t=eval(raw_input())
for k in range(t):
	n,k=map(int,raw_input().split(' '))
	d=raw_input()
	s=list(d)
	product=1
	maxproduct=0
	for i in range(n-k+1):   #Brute force method used
		j=i		  #picks first no from the list and finds product of k no's then i is incremented and so on
		product=1
		r=k
		while r>0:
			product=product*int(s[j])  #product variable stores the present product
			r-=1			   #int is used to explicitly type cast the string value
			j+=1
		if product>maxproduct:  #max product stores the largest product uptil now
			maxproduct=product
	print maxproduct
