# Write a Python program to get unique values from a list 

l1 = [1,1,1,2,3,4,5,5,6,7,8,8,9,10,1,11,2,3,8,6,5]
l2 = []

for i in l1 :
    if i not in l2 :
        l2.append(i)
        
print("Unique value of list are : ",l2)