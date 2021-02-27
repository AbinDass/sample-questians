# l1 = [1,2,3,4,5,6]
# l2 = [7,8,9,10]
# print(l1+l2)

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 =  [i + j for i, j in zip(list1, list2)]
print(list3)