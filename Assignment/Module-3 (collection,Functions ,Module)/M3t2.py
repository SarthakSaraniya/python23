l = [1,24,28,43,25]
temp = None

l.sort()
print(l)

print("Max value :",l[-1])  # min value in list
print("MIn value :",l[0])   # Max value print

sum = 0

for i in range(0,len(l)):
    sum  = sum + l[i]    
    
print("Sum of all number in list : ",sum)