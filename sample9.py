n=int(input ("enter the num : "))
rev=0
while(n>0):
	reminder=n%10
	rev=(rev*10)+reminder
	n = n // 10
print("reverse of the num : ",rev)