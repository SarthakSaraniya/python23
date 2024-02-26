#Write a Python program to find the second smallest number in a list
l1=[1,2,3,4,5,6,4,6,3]
l=list(set(l1))

if len(l)<2:
    print("There is no second smallest element in the list")

else:
    
    for i in range(len(l)):
        
        for j in range(i+1,len(l)):
           
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp

print("second smallest number in list is :",l[1])
print(l)                    