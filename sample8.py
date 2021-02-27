n = int ( input ("please enter any number: "))
f=1
if n<0:
	print("cant in negative")
elif n==0:
	print ("factorial of 0 is 1")
else:
	for i in range(1,n+1):
		print(i)
		factorial = f*i
	print("factorial of", n ,"is ",factorial)