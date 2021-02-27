num = int (input ("enter a positive number: ")) 
s=0
for i in range (0,num):
	if  num>0:
		s += num
		num -= 1

print ("The sum b/w 1 and entered number is: ",s)



# num = int ( input ( "enter a positive number: "))
# if num<0:
# 	print (" enter a +ve number")
# else:
# 	s=0
# 	while (num>0):
# 		s += num
# 		num -= 1
# 	print (" the sum is ",s)