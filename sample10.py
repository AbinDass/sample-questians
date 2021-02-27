l=[]
n=int(input("enter the number of elements in the index:"))
for i in range(0,n):
	elements=int(input("Enter the elements :"))
	l.append(elements)

for i in l:
	if i % 2 == 0:
		print(i,end = "  ")