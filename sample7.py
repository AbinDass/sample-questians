terms = int ( input ("enter how many terms: "))
count=0
n1=0
n2=1

if terms<=0:
	print(" enter a +ve intiger:")
elif terms == 1:
	print(n1)
else:
	while count<terms:
		print(n1)
		a=n1+n2
		n1=n2
		n2=a
		count+=1
