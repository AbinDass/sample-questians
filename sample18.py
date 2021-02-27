l = [1,2,3,4,5,6,7]

# a=filter(lambda s:s<5,l)
# print(list(a))

# b=map(lambda s:s>3,l)
# print(list(b))


from functools import reduce
def mul(x,y):
	return x*y
print(reduce(mul,l))