n = int ( input ("Please enter a numeric value: "))
a = n
s=0
while a > 0:
	d = a % 10
	s +=  d**3  
	a //= 10 

if n == s:
	print (n, "  is an armstrong  ")
else:
	print (n, "  is not an armstrong  ")

