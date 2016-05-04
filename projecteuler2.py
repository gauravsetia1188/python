#sum of all even fibonacci numbers below n
t=eval(raw_input())
for k in range(t):
	n=eval(raw_input())
	x=1
	y=2
	evensum=2
	next=0
	while 1:
		next=x+y
		if next>n:
			break
		if next%2==0:
			evensum=evensum+next
		x=y
		y=next
	print evensum
