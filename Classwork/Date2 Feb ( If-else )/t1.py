s = input("Enter the string : ")

if len(s)%2 == 1 and len(s)>4 :
    s1 = int(len(s)/2)
    
    print(s[s1-1],end="")
    print(s[s1],end="")
    print(s[s1+1],end="")
    
else :
    pass
 